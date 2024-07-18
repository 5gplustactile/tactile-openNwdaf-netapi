from ..models.qos_sustainability_info import QosSustainabilityInfo
from ..models.event_notification import EventNotification
from ..models.nnwdaf_events_subscription import NnwdafEventsSubscription
from ..models.event_subscription import EventSubscription
from ..models.network_area_info import NetworkAreaInfo
from ..models.nf_load_level_information import NfLoadLevelInformation
from ..models.network_perf_info import NetworkPerfInfo
from ..models.user_data_congestion_info import UserDataCongestionInfo
from ..models.congestion_info import CongestionInfo
from ..models.threshold_level import ThresholdLevel
from ..db.data_db import MongoDatabase
from ..util import clean_empty
import math
import requests

import pymongo
import os


class notification():
    client = MongoDatabase()

    # def get_direction(self, previous_throughput, current_throughput):
    #     if previous_throughput < current_throughput:
    #         return "ASCENDING"
    #     elif previous_throughput > current_throughput:
    #         return "DESCENDING"
    #     else:
    #         return "CROSSED"

    # def qos_sustainability_threshold_notification(self, body:NnwdafEventsSubscription, sub:EventSubscription):
    #     collection = self.client.get_coll(os.getenv('MONGO_QOS_ANALYTICS_COL'))
    #     document = collection.find_one(sort=[('createdAt', pymongo.DESCENDING)])
    #     ecgi_list = []
    #     try:
    #         for ecgi in sub.network_area.ecgis:
    #             ecgi_list.append(int(ecgi.eutra_cell_id, 16))

    #     except:
    #         raise Exception()

    #     data_by_cellid = [[] for _ in range(len(ecgi_list))]

    #     for qos in document["data"]:
    #         if qos["CELLID"] in ecgi_list:
    #             index = ecgi_list.index(qos["CELLID"])
    #             data_by_cellid[index].append(qos)

    #     qos_infos = []
    #     for data_list in data_by_cellid:
    #         previous_throughput = data_list[-2]['nr1477']
    #         current_throughput = data_list[-1]['nr1477']

    #         crossed_threshold = False

    #         for threshold in sub.thresholds:
    #         # Procesar el umbral para obtener el valor numérico en MBps
    #             threshold_value = float(threshold.split()[0])
    #             threshold_unit = threshold.split()[1]
    #             if threshold_unit == "Mbps":
    #                 threshold_mbps = threshold_value
    #             elif threshold_unit == "Gbps":
    #                 threshold_mbps = threshold_value * 1024
    #             elif threshold_unit == "Kbps":
    #                 threshold_mbps = threshold_value / 1024
    #             elif threshold_unit == "bps":
    #                 threshold_mbps = threshold_value / (1024 * 1024)
    #             elif threshold_unit == "Tbps":
    #                 threshold_mbps = threshold_value * 1024 * 1024

    #             if previous_throughput <= threshold_mbps < current_throughput:
    #                     crossed_threshold = True
    #             if crossed_threshold:
    #                 direction = self.get_direction(previous_throughput, current_throughput)

    #                 if direction == sub.matching_dir:
                
    #                     if qos["CELLID"] in ecgi_list:
    #                             qos_info = QosSustainabilityInfo(ran_ue_throu_thd=threshold,
    #                                                             start_ts=qos["timestamp_str"],
    #                                                             area_info=NetworkAreaInfo().from_dict({"ecgis":[{"plmnId":{"mcc":"214", "mnc":"07"},"eutraCellId": str(hex(qos["CELLID"])[2:].zfill(7))}]}))
    #                             qos_infos.append(qos_info)
    #     event_notify = EventNotification()
    #     event_notify.event="QOS_SUSTAINABILITY"
    #     event_notify.qos_sustain_infos = qos_infos
    #     return event_notify.to_dict()


    def nf_load_periodic_notification(self, body, sub:EventSubscription):
        collection = self.client.get_coll(os.getenv('MONGO_CORE_ANALYTICS_COL'))
        document = collection.find_one(sort=[('createdAt', pymongo.DESCENDING)])
        if document is None:
            raise requests.exceptions.RequestException(document)
        event_notify = EventNotification()
        event_notify.event="NF_LOAD"
        load_levels = []
        if sub.nf_types is None or len(sub.nf_types) == 0:
            for key in document["data"]["metric.value"]:
                load_level = NfLoadLevelInformation(nf_cpu_usage=document["data"]["metric.value"][key], nf_type=key.split('-')[1].upper())
                load_levels.append(load_level)
        else:
            for nf in sub.nf_types:
                key = "open5gs-"+nf.lower()
                if key in document["data"]["metric.value"]:
                    load_level = NfLoadLevelInformation(nf_cpu_usage=document["data"]["metric.value"][key],
                                                        nf_type=nf)
                    load_levels.append(load_level)
        if load_levels != []:
            event_notify.nf_load_level_infos = load_levels
        return event_notify.to_dict()

    def qos_sustainability_periodic_notification(self, body:NnwdafEventsSubscription, sub:EventSubscription):
        collection = self.client.get_coll(os.getenv('MONGO_QOS_ANALYTICS_COL'))
        document = collection.find(sort=[('createdAt', pymongo.DESCENDING)])[4]
        ecgi_list = []
        try:
            for ecgi in sub.network_area.ecgis:
                ecgi_list.append(int(ecgi.eutra_cell_id, 16))
        except:
            raise Exception()
        # current_app.logger.debug(f"Result: {document}")
        filtered_data = sorted(
            [item for item in document["data"] if item["CELLID"] in ecgi_list],
            key=lambda x: x["timestamp_str"]
        )
        qos_infos = []
        for qos in filtered_data:
            qos_info = QosSustainabilityInfo(ran_ue_throu_thd=f"{qos['nr1477']} Mbps",
                                            start_ts=qos["timestamp_str"],
                                            area_info=NetworkAreaInfo().from_dict({"ecgis":[{"plmnId":{"mcc":"214", "mnc":"07"},"eutraCellId": str(hex(qos["CELLID"])[2:].zfill(7))}]}))
            qos_infos.append(qos_info)
        event_notify = EventNotification()
        event_notify.event="QOS_SUSTAINABILITY"
        event_notify.qos_sustain_infos = qos_infos
        return event_notify.to_dict()
    
    def network_performance_periodic_notification(self, body:NnwdafEventsSubscription, sub:EventSubscription):

        collection = self.client.get_coll(os.getenv("MONGO_NETPERF_COL"))
        document = collection.find(sort=[('eventdate', pymongo.DESCENDING)])[4]
        event_notify = EventNotification()
        event_notify.event="NETWORK_PERFORMANCE"
        net_perfs = []

        
        cells_id=[
                {"name":"V/AVENIDA DEL PUERTO", "eutra_cell":{"plmn_id":{"mcc":"214","mnc":"07"}, "eutra_cell_id":"0000001", "nid": None}}
            ]

        for ecgi in sub.network_area.ecgis:
            for cell_id in cells_id:
                if cell_id["eutra_cell"] == ecgi.to_dict():
                    for data in document["data"]:
                        if cell_id["name"] == data["EMPLAZAMIENTO"]:
                            net_perf = None
                            for perf in sub.nw_perf_requs:
                                net_perf = NetworkPerfInfo(network_area=NetworkAreaInfo(ecgis=[ecgi]), nw_perf_type=perf.nw_perf_type)
                                if perf.nw_perf_type == "NUM_OF_UE":
                                    net_perf.absolute_num=math.trunc(data["connected_users"])
                                else:
                                    raise Exception("nwPerfTypes", perf.nw_perf_type)
                            if net_perf:   
                                net_perfs.append(net_perf)
                else:
                    raise Exception("ecgi", ecgi) 

        if net_perfs != []:
            event_notify.qos_sustain_infos = net_perfs
        return event_notify.to_dict()
    
    def user_data_congestion_periodic_notification(self, body:NnwdafEventsSubscription, sub:EventSubscription):
        collection = self.client.get_coll(os.getenv("MONGO_CONGESTION_COL"))
        document = collection.find_one(sort=[('eventdate', pymongo.DESCENDING)])
        event_notify = EventNotification()
        event_notify.event="USER_DATA_CONGESTION"
        
        cells_id=[
                {"name":"V/AVENIDA DEL PUERTO", "eutra_cell":{"plmn_id":{"mcc":"214","mnc":"07"}, "eutra_cell_id":"0000001", "nid": None}}
            ]

        data_cong = []
        for ecgi in sub.network_area.ecgis:
            for cell_id in cells_id:
                if cell_id["eutra_cell"] == ecgi.to_dict():
                    for data in document["data"]:
                        if cell_id["name"] == data["CELL_ID"]:
                            cong = UserDataCongestionInfo(network_area=NetworkAreaInfo(ecgis=[ecgi]), 
                                                            congestion_info=CongestionInfo(cong_type="USER_PLANE", 
                                                                                            nsi=ThresholdLevel(cong_level=data["congestion"])))

                            data_cong.append(cong)
                else:
                    raise Exception("ecgi", ecgi) 

        if data_cong != []:
            event_notify.user_data_cong_infos = data_cong
        return event_notify.to_dict()
            

    # def make_notification(body, sub):
    #     db = current_app.config["db"].get_coll_data("nwdafNokiaAnalytics")
    #     document = db.find({'eventNotifications.event':sub["event"]}).sort("createdAt", -1).limit(1)
    #     event_notify = NnwdafEventsSubscriptionNotification()
    #     event_notify.event_notifications = document[0]["eventNotifications"]
    #     return event_notify
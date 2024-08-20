from ..db.db import MongoDatabase
from ..models.event_reporting_requirement import EventReportingRequirement
from ..models.event_filter import EventFilter
from ..models.target_ue_information import TargetUeInformation
from ..models.analytics_data import AnalyticsData
from ..models.nf_load_level_information import NfLoadLevelInformation
from ..models.network_area_info import NetworkAreaInfo
from ..models.qos_sustainability_info import QosSustainabilityInfo
from ..models.retainability_threshold import RetainabilityThreshold
from ..models.network_perf_info import NetworkPerfInfo
from ..models.user_data_congestion_info import UserDataCongestionInfo
from ..models.congestion_info import CongestionInfo
from ..models.threshold_level import ThresholdLevel
import dateutil
from flask import current_app
import os
import pymongo
import math
from datetime import datetime, timedelta

class prediction:
    def get_pred(self, d:AnalyticsData, event, ana_req:EventReportingRequirement, event_filter:EventFilter, supported_features, tgt_ue:TargetUeInformation):
        collection = current_app.config["db"].get_coll("analyticsPred")
        collection = current_app.config["db"].get_coll_data("eventsNfLoadOpen5gs")

        if event == "NF_LOAD":
            collection = current_app.config["db"].get_coll_data(os.getenv('MONGO_CORE_PREDICTIONS_COL'))
            document = collection.find_one(sort=[('createdAt', pymongo.DESCENDING)])
            current_app.logger.debug(f"Result: {document}")
            if document:
                load_levels=[]
                for nf in event_filter.nf_types:
                    key = "open5gs-"+nf.lower()
                    if key in document['data']["metric.value"]:
                        load_level = NfLoadLevelInformation(nf_cpu_usage=document["data"]['metric.value'][key], nf_type=nf)
                        load_levels.append(load_level)
                

                if load_levels != []:
                    d.nf_load_level_infos= load_levels
                else:
                    raise Exception("204", "Not Data") 

        if event == "NETWORK_PERFORMANCE":
            current_app.logger.debug(f"Searching for {event}")
            current_app.logger.debug(f"Event_filter: {event_filter}")

            collection = current_app.config["db"].get_coll_data(os.getenv("MONGO_NETPERF_COL"))
            document = collection.find(sort=[('eventdate', pymongo.DESCENDING)])[3]
            
            cells_id=[
                {"name":"V/AVENIDA DEL PUERTO", "eutra_cell":{"plmn_id":{"mcc":"214","mnc":"07"}, "eutra_cell_id":"0000001", "nid": None}}
            ]
            
            net_perfs = []
            if document is not None:
                for ecgi in event_filter.network_area.ecgis:
                    for cell_id in cells_id:
                        if cell_id["eutra_cell"] == ecgi.to_dict():
                            for data in document["data"]:
                                if cell_id["name"] == data["EMPLAZAMIENTO"]:
                                    predict = [15, 30, 45, 60]
                                    for i in predict:
                                        net_perf = None
                                        for perf_type in event_filter.nw_perf_types:
                                            net_perf = NetworkPerfInfo(network_area=NetworkAreaInfo(ecgis=[ecgi]), nw_perf_type=perf_type)
                                            if perf_type == "NUM_OF_UE":
                                                net_perf.absolute_num=math.trunc(data[f"connected_users_forecast_{i}_minutes"])
                                            else:
                                                raise Exception("nwPerfTypes", perf_type)
                                        if net_perf:   
                                            net_perfs.append(net_perf)
                        else:
                            raise Exception("ecgi", ecgi) 

            if net_perfs != []:
                d.nw_perfs = net_perfs
            else:
                raise Exception("204", "Not Data") 
            
        if event == "USER_DATA_CONGESTION":
            current_app.logger.debug(f"Searching for {event}")
            current_app.logger.debug(f"Event_filter: {event_filter}")

            collection = current_app.config["db"].get_coll_data(os.getenv("MONGO_CONGESTION_COL"))
            document = collection.find(sort=[('eventdate', pymongo.DESCENDING)])[3]
            
            cells_id=[
                {"name":"V/AVENIDA DEL PUERTO", "eutra_cell":{"plmn_id":{"mcc":"214","mnc":"07"}, "eutra_cell_id":"0000001", "nid": None}}
            ]
            
            data_cong = []
            for ecgi in event_filter.network_area.ecgis:
                for cell_id in cells_id:
                    if cell_id["eutra_cell"] == ecgi.to_dict():
                        for data in document["data"]:
                            if cell_id["name"] == data["CELL_ID"]:
                                predict = [15, 30, 45, 60]
                                for i in predict:
                                    cong = UserDataCongestionInfo(network_area=NetworkAreaInfo(ecgis=[ecgi]), 
                                                                    congestion_info=CongestionInfo(cong_type="USER_PLANE", 
                                                                                                    nsi=ThresholdLevel(cong_level=data[f"congestion_forecast_{i}_minutes"])))

                                    data_cong.append(cong)
                    else:
                        raise Exception("ecgi", ecgi) 

            if data_cong != []:
                d._user_data_cong_infos = data_cong
            else:
                raise Exception("204", "Not Data") 
            
        
        if event == "QOS_SUSTAINABILITY":
            
            ecgi_list = []
            if "ecgis" in event_filter.network_area.to_dict():
                for ecgi in event_filter.network_area.to_dict()["ecgis"]:
                    ecgi_list.append(int(ecgi["eutra_cell_id"],16))

        
            if event_filter.qos_requ.to_dict()["res_type"] is not None and event_filter.qos_requ.to_dict()["gfbr_dl"] is not None:
                threshold = float(event_filter.qos_requ.to_dict()["gfbr_dl"].split()[0])
                current_app.logger.debug(f"Threshold: {threshold}")

                collection = current_app.config["db"].get_coll_data(os.getenv('MONGO_QOS_PREDICTIONS_COL'))
                document = collection.find_one(sort=[('createdAt', pymongo.DESCENDING)])

                current_app.logger.debug(f"Document: {document}")
                qos_infos = []
                for cell in ecgi_list:
                    percent = 0
                    count = 0
                    for qos in document["data"]:
                        if qos["CELLID"] == cell:
                            count+=1
                            if qos['nr1477'] < threshold:
                                percent+=1
                    if count != 0: 
                        qos_info = QosSustainabilityInfo(ran_ue_throu_thd=event_filter.qos_requ.to_dict()["gfbr_dl"],
                                                    qos_flow_ret_thd=RetainabilityThreshold(rel_flow_ratio=int((percent/count)*100)),
                                                    start_ts=qos["timestamp_str"],
                                                    area_info=NetworkAreaInfo().from_dict({"ecgis":[{"plmnId":{"mcc":"214", "mnc":"07"},"eutraCellId": str(hex(cell)[2:].zfill(7))}]}))
                        qos_infos.append(qos_info)
                if qos_infos != []:
                    d.qos_sustain_infos = qos_infos
                else:
                    raise Exception("204", "Not Data") 
        return d
        



from ..db.db import MongoDatabase
from ..models.event_reporting_requirement import EventReportingRequirement
from ..models.event_filter import EventFilter
from ..models.analytics_data import AnalyticsData
from ..models.target_ue_information import TargetUeInformation
from ..models.nf_load_level_information import NfLoadLevelInformation
from ..models.qos_sustainability_info import QosSustainabilityInfo
from ..models.retainability_threshold import RetainabilityThreshold
from ..models.network_area_info import NetworkAreaInfo
from ..models.network_perf_info import NetworkPerfInfo
from ..models.user_data_congestion_info import UserDataCongestionInfo
from ..models.congestion_info import CongestionInfo
from ..models.threshold_level import ThresholdLevel
from ..core.query_methods import query_snssais, query_network_areas,query_qos_requ, add_and, search
from ..core.responses import bad_request_error, not_found_error
from flask import current_app
from datetime import datetime
from ..util import dict_to_camel_case
import os
import math
import re
import pymongo

class statistics:
    def get_stats(self, d:AnalyticsData, event, ana_req:EventReportingRequirement, event_filter:EventFilter, supported_features, tgt_ue:TargetUeInformation):
        #Query
        q={}
        #Commons filter
        q["data.ts"]= {"$gte": ana_req.start_ts, "$lte": ana_req.end_ts}

        #Filters for the event LOAD_LEVEL_INFORMATION
        # if event == "LOAD_LEVEL_INFORMATION":
        #     q["eventType"]="LOAD_LEVEL_INFORMATION"
        #     if event_filter.snssais != None:
        #         q = add_and(q, {"$or":query_snssais(event_filter.snssais, "snssais")})
        #     current_app.logger.debug(q)
        #     res = search(q, d, "sliceLoadLevelInfos")
        #     if len(res)==0:
        #         return not_found_error(detail="No data found", cause="")
        #     d.slice_load_level_infos = res
            
        
        # #Filters for the event NSI_LOAD_LEVEL_INFORMACTION
        # if event == "NSI_LOAD_LEVEL":
        #     q["eventType"]="NSI_LOAD_LEVEL"
        #     if event_filter.snssais != None:
        #         q = add_and(q, {"$or":query_snssais(event_filter.snssais, "snssai")})
        #     current_app.logger.debug(q)
        #     res = search(q, d, "nsiLoadLevelInfos")
        #     if len(res)==0:
        #         return not_found_error(detail="No data found", cause="")
        #     d.nsi_load_level_infos = res
            
        #Filters for the event NF_LOAD
        if event == "NF_LOAD":
            current_app.logger.debug(f"Searching for {event}")
            q["eventType"]="NF_LOAD"

            if not tgt_ue.any_ue:
                q["data.supi"] = {"$in": tgt_ue.supis}
                q["data.intGroupId"]={"$in":tgt_ue.int_group_ids}
                q["data.gpsis"]={"$in":tgt_ue.gpsis}
                
            if event_filter.nf_set_ids is not None:
                q["data.nfSetId"] = {"$in": event_filter.nf_set_ids}

            if event_filter.nf_instance_ids is not None:
                q["data.nfInstanceId"]={"$in": event_filter.nf_instance_ids}


            q["data.nfType"]={"$in": event_filter.nf_types}

            if event_filter.snssais is not None:
                q = add_and(q, {"$or":query_snssais(event_filter.snssais, "snssai")})
            
            #Network Area
            if event_filter.network_area is not None:
                or_conditions_list = []
                for key, value in event_filter.network_area.to_dict().items():
                    or_conditions_list.extend(query_network_areas(value, key, "networkArea"))
                q = add_and(q, {"$or":or_conditions_list})

            current_app.logger.debug(f"Query: {q}")
            collection = current_app.config["db"].get_coll_data(os.getenv('MONGO_CORE_ANALYTICS_COL'))
            document = collection.find_one(sort=[('createdAt', pymongo.DESCENDING)])
            current_app.logger.debug(f"Result of query: {document}")

            if document:
                load_levels=[]
                for nf in event_filter.nf_types:
                    key = "open5gs-"+nf.lower()
                    if key in document["data"]["metric.value"]:
                        load_level = NfLoadLevelInformation(nf_cpu_usage=document["data"]["metric.value"][key], nf_type=nf)
                        load_levels.append(load_level)
                if load_levels != []:
                    d.nf_load_level_infos= load_levels
                else:
                    raise Exception(204, "Not Found") 
                current_app.logger.debug(f"Result {d.to_dict()}")
                
        if event == "NETWORK_PERFORMANCE":
            current_app.logger.debug(f"Searching for {event}")
            current_app.logger.debug(f"Event_filter: {event_filter}")
            q={}
            q["eventdate"]={"$gte": ana_req.start_ts, "$lte": ana_req.end_ts}

            collection = current_app.config["db"].get_coll_data(os.getenv("MONGO_NETPERF_COL"))
            documents = collection.find(q)
            
            cells_id=[
                {"name":"V/AVENIDA DEL PUERTO", "eutra_cell":{"plmn_id":{"mcc":"214","mnc":"07"}, "eutra_cell_id":"0000001", "nid": None}}
            ]
            
            net_perfs = []
            for ecgi in event_filter.network_area.ecgis:
                for cell_id in cells_id:
                    if cell_id["eutra_cell"] == ecgi.to_dict():
                        for document in documents:
                            for data in document["data"]:
                                if cell_id["name"] == data["EMPLAZAMIENTO"]:
                                    net_perf = None
                                    for perf_type in event_filter.nw_perf_types:
                                        net_perf = NetworkPerfInfo(network_area=NetworkAreaInfo(ecgis=[ecgi]), nw_perf_type=perf_type)
                                        if perf_type == "NUM_OF_UE":
                                            net_perf.absolute_num=math.trunc(data["connected_users"])
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
            q={}
            q["eventdate"]={"$gte": ana_req.start_ts, "$lte": ana_req.end_ts}

            collection = current_app.config["db"].get_coll_data(os.getenv("MONGO_CONGESTION_COL"))
            documents = collection.find(q)
            
            cells_id=[
                {"name":"V/AVENIDA DEL PUERTO", "eutra_cell":{"plmn_id":{"mcc":"214","mnc":"07"}, "eutra_cell_id":"0000001", "nid": None}}
            ]
            
            data_cong = []
            for ecgi in event_filter.network_area.ecgis:
                for cell_id in cells_id:
                    if cell_id["eutra_cell"] == ecgi.to_dict():
                        for document in documents:
                            current_app.logger.debug(document)
                            for data in document["data"]:
                                if cell_id["name"] == data["CELL_ID"]:
                                    cong = UserDataCongestionInfo(network_area=NetworkAreaInfo(ecgis=[ecgi]), 
                                                                  congestion_info=CongestionInfo(cong_type="USER_PLANE", 
                                                                                                 nsi=ThresholdLevel(cong_level=data["congestion"])))

                                    data_cong.append(cong)
                    else:
                        raise Exception("ecgi", ecgi) 

            if data_cong != []:
                d._user_data_cong_infos = data_cong
            else:
                raise Exception("204", "Not Data") 


        #Filters for the event QOS_SUSTAINABILITY
        if event == "QOS_SUSTAINABILITY":
            current_app.logger.debug(f"Searching for {event}")

            current_app.logger.debug(f"Event_filter: {event_filter}")
            q["eventType"]="QOS_SUSTAINABILITY"

            #Search the data
            query = {}
            query["data.timestamp_str"]={"$gte": ana_req.start_ts.strftime("%Y-%m-%d %H:%M:%S"), "$lte": ana_req.end_ts.strftime("%Y-%m-%d %H:%M:%S")}
            
            ecgi_list = []
            if "ecgis" in event_filter.network_area.to_dict():
                for ecgi in event_filter.network_area.to_dict()["ecgis"]:
                    ecgi_list.append(int(ecgi["eutra_cell_id"],16))

            if event_filter.qos_requ.to_dict()["res_type"] is not None and event_filter.qos_requ.to_dict()["gfbr_dl"] is not None:
                threshold = float(event_filter.qos_requ.to_dict()["gfbr_dl"].split()[0])
                current_app.logger.debug(f"Threshold: {threshold}")

                qos_infos = []
                for cell in ecgi_list:
                    current_app.logger.debug(f"Query: {query}")
                    collection = current_app.config["db"].get_coll_data(os.getenv('MONGO_QOS_ANALYTICS_COL'))
                    documents = collection.find(query)
                    percent = 0
                    count = 0
                    for document in documents:
                        for qos in document["data"]:
                            if qos["CELLID"] == cell:
                                count+=1
                                if qos['nr1477'] < threshold:
                                    percent+=1
                    if count != 0: 
                        current_app.logger.debug(f"count: {count}, percent: {percent}")
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



    



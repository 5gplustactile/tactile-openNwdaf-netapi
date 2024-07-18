
from ..models.nnwdaf_events_subscription import NnwdafEventsSubscription
from ..models.event_subscription import EventSubscription
from ..models.failure_event_info import FailureEventInfo
from ..core.responses import internal_server_error
from flask import current_app
  

#NF_LOAD
def check_nf_load(body:dict, sub:dict):
    current_app.logger.debug("Ckeck nf load")

    # identificationoftargetUE(s)towhichthesubscriptionappliesby"supis"or"anyUe"inthe"tgtUe"attribute; and

    if sub["tgt_ue"] is None or (sub["tgt_ue"]["any_ue" ] is None or sub["tgt_ue"]["any_ue"] is False):
        return internal_server_error(detail="Unable to obtain the required data referring to the given tgtUe.", cause="UNAVAILABLE_DATA",)

    # NFloadlevelthresholdsinthe"nfLoadLvlThds"attributeifthe"notifMethod"attributein"evtReq"attribute is set
    #  to "ON_EVENT_DETECTION" or the "notificationMethod" attribute in "eventSubscriptions" attribute is set to
    # "THRESHOLD" or omitted;

    if body["evt_req"]["notif_method"] is not None and body["evt_req"]["rep_period"] is not None:
        if body["evt_req"]["notif_method"] == "ON_EVENT_DETECTION" and (sub["matching_dir"] is None or sub["nf_load_lvl_thds"] is None):
            return internal_server_error(detail="For the notifMethod 'ON_EVENT_DETECTION' you need to specify the matchingDir and the nfLoadLvlThds", cause="UNAVAILABLE_DATA",)

        else:
            if sub["notification_method"] in ["THRESHOLD", None] and (sub["matching_dir"] is None or sub["nf_load_lvl_thds"] is None):
                return internal_server_error(detail="For the notification_method 'THRESHOLD' you need to specify the matchingDir and the nfLoadLvlThds", cause="UNAVAILABLE_DATA",)

    else:
        if sub["notification_method"] in ["THRESHOLD", None] and (sub["matching_dir"] is None or sub["nf_load_lvl_thds"] is None or sub["repetition_period"] is None):
            return internal_server_error(detail="For the notification_method 'THRESHOLD' you need to specify the matchingDir and the nfLoadLvlThds", cause="UNAVAILABLE_DATA",)
    
    if sub["nf_instance_ids"] is not None or sub["nf_set_ids"] is not None:
        return internal_server_error(detail="nfInstanceIds and nfSetIds are not supported", cause="UNAVAILABLE_DATA",)

    if sub["snssaia"] is not None:
        return internal_server_error(detail="snssaia is not supported", cause="UNAVAILABLE_DATA")
    
    if sub["network_area"] is not None:
        return internal_server_error(detail="networkArea is not supported", cause="UNAVAILABLE_DATA")
    
    if sub["list_of_ana_subsets"] is not None:
        return internal_server_error(detail="listOfAnaSubsets is not supported", cause="UNAVAILABLE_DATA")

    return 0


#QOS_SUSTAINABILITY
def check_qos(body:dict, sub:dict):
    current_app.logger.debug("Ckeck qos")
    # Cells that support NaaS
    ecgis = [{"plmn_id":{"mcc":"214", "mnc":"07"},"eutra_cell_id": "0000001", "nid": None},
            {"plmn_id":{"mcc":"214", "mnc":"07"},"eutra_cell_id": "0000002", "nid": None},
            {"plmn_id":{"mcc":"214", "mnc":"07"},"eutra_cell_id": "0000003", "nid": None},
            {"plmn_id":{"mcc":"214", "mnc":"07"},"eutra_cell_id": "00003E9", "nid": None},
            {"plmn_id":{"mcc":"214", "mnc":"07"},"eutra_cell_id": "00003EA", "nid": None},
            {"plmn_id":{"mcc":"214", "mnc":"07"},"eutra_cell_id": "00003EB", "nid": None}]

    # identificationofnetworkareatowhichthesubscriptionappliesviaidentificationofnetworkareaby "networkArea" attribute;
    if sub["network_area"] is None:
        return internal_server_error(detail="You need to specify the networkArea", cause="UNAVAILABLE_DATA")
    else:
        if sub["network_area"]["ecgis"] is None:
            return internal_server_error(detail="You need to specify the networkArea ecgis", cause="UNAVAILABLE_DATA")
        else:
            for ecgi in sub["network_area"]["ecgis"]:
                if ecgi not in ecgis:
                    return internal_server_error(detail=f"The ecgi {ecgi} is not supported.", cause="UNAVAILABLE_DATA")

    # heQoSrequirementsvia"qosRequ"attribute
    
    # # #QoSflowretainabilitythreshold(s)bythe"qosFlowRetThds"attributeforthe5QIofGBRresourcetypeor RAN UE 
    # # throughout threshold(s) by the "ranUeThrouThds" attribute for the 5QI of non-GBR resource type, if the "notifMethod"
    #  attribute in "evtReq" attribute is set to "ON_EVENT_DETECTION" or the "notificationMethod" attribute in
    # "eventSubscriptions" attribute is set to "THRESHOLD" or omitted; and

    if sub["qos_requ"] is None:
        return internal_server_error(detail="You need to specify the qosRequ", cause="UNAVAILABLE_DATA")
    else:
        if body["evt_req"]["notif_method"] in ["ON_EVENT_DETECTION", None] and sub["notification_method"] in ["THRESHOLD", None]:
             return internal_server_error(detail="Only support periodic requests.", cause="UNAVAILABLE_DATA")
    #     if sub["qos_requ"]["res_type"] != "NON_GBR" or sub["qos_requ"]["gfbr_dl"] is None:
    #         return internal_server_error(detail="Only support qosrequ resType NON_GBR", cause="UNAVAILABLE_DATA")

    # if body["evt_req"]["notif_method"] is not None and body["evt_req"]["rep_period"] is not None:
    #     if body["evt_req"]["notif_method"] == "ON_EVENT_DETECTION" and (sub["matching_dir"] is None or sub["ran_ue_throu_thds"] is None):
    #             return internal_server_error(detail="For the notifMethod 'ON_EVENT_DETECTION' you need to specify the matchingDir and the ran_ue_throu_thds", cause="UNAVAILABLE_DATA",)
    #     else:
    #         if sub["notification_method"] in ["THRESHOLD", None] and (sub["matching_dir"] is None or sub["ran_ue_throu_thds"] is None):
    #             return internal_server_error(detail="For the notification_method 'THRESHOLD' you need to specify the matchingDir and the ran_ue_throu_thds", cause="UNAVAILABLE_DATA",)
    # else:
    #     if sub["notification_method"] in ["THRESHOLD", None] and (sub["matching_dir"] is None or sub["ran_ue_throu_thds"] is None or sub["repetition_period"] is None):
    #         return internal_server_error(detail="For the notification_method 'THRESHOLD' you need to specify the matchingDir and the nfLoadLvlThds", cause="UNAVAILABLE_DATA",)
    # # identificationoftargetUE(s)towhichthesubscriptionappliesby"anyUe"inthe"tgtUe"attribute;
    if sub["tgt_ue"] is None or (sub["tgt_ue"]["any_ue" ] is None or sub["tgt_ue"]["any_ue"] is False):
        return internal_server_error(detail="Unable to obtain the required data referring to the given tgtUe.", cause="UNAVAILABLE_DATA",)
    # and may include:
    # 1) identificationofnetworkslice(s)by"snssais"attribute;and/or
    if sub["snssaia"] is not None:
        return internal_server_error(detail="snssaia is not supported", cause="UNAVAILABLE_DATA")
    
    return 0

def check_network_perf(body:dict, sub:dict):
    current_app.logger.debug("Ckeck network performance")

    ecgis=[
                {"name":"V/AVENIDA DEL PUERTO", "eutra_cell":{"plmn_id":{"mcc":"214","mnc":"07"}, "eutra_cell_id":"0000001", "nid": None}}
            ]
    
    if sub["tgt_ue"] is None or (sub["tgt_ue"]["any_ue" ] is None or sub["tgt_ue"]["any_ue"] is False):
        return internal_server_error(detail="Unable to obtain the required data referring to the given tgtUe.", cause="UNAVAILABLE_DATA",)
    if sub["network_area"] is None:
        return internal_server_error(detail="You need to specify the networkArea", cause="UNAVAILABLE_DATA")
        
    else:
        if sub["network_area"]["ecgis"] is None:
            return internal_server_error(detail="You need to specify the networkArea ecgis", cause="UNAVAILABLE_DATA")
        else:
            for ecgi in sub["network_area"]["ecgis"]:
                for cell in ecgis:
                    if cell["eutra_cell"] != ecgi:
                        return internal_server_error(detail=f"The ecgi {ecgi} is not supported.", cause="UNAVAILABLE_DATA")
                
    if sub["nw_perf_requs"] is None:

         return internal_server_error(detail="You need to specify the nwPerfRequs", cause="UNAVAILABLE_DATA")

    return 0

def check_user_data_congestion(body:dict, sub:dict):
    current_app.logger.debug("Check user data congestion")

    ecgis=[
                {"name":"V/AVENIDA DEL PUERTO", "eutra_cell":{"plmn_id":{"mcc":"214","mnc":"07"}, "eutra_cell_id":"0000001", "nid": None}}
            ]
    
    if sub["tgt_ue"] is None or (sub["tgt_ue"]["any_ue" ] is None or sub["tgt_ue"]["any_ue"] is False):
        return internal_server_error(detail="Unable to obtain the required data referring to the given tgtUe.", cause="UNAVAILABLE_DATA",)
    if sub["network_area"] is None:
        return internal_server_error(detail="You need to specify the networkArea", cause="UNAVAILABLE_DATA")
        
    else:
        if sub["network_area"]["ecgis"] is None:
            return internal_server_error(detail="You need to specify the networkArea ecgis", cause="UNAVAILABLE_DATA")
        else:
            for ecgi in sub["network_area"]["ecgis"]:
                for cell in ecgis:
                    if cell["eutra_cell"] != ecgi:
                        current_app.logger.debug(ecgis)
                        return internal_server_error(detail=f"The ecgi {ecgi} is not supported.", cause="UNAVAILABLE_DATA")

    return 0


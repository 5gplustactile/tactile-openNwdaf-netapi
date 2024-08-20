from ..models.event_filter import EventFilter
from ..models.target_ue_information import TargetUeInformation
from .responses import internal_server_error


def check(self, event, event_filter: EventFilter, tgt_ue:TargetUeInformation):
    if event == "LOAD_LEVEL_INFORMATION":
        if event_filter.snssais is None and event_filter.any_slice is False:
            return internal_server_error("", "UNAVAILABLE_DATA")

    if event == "NSI_LOAD_LEVEL":
        if event_filter.nsi_id_infos is None and event_filter.any_slice is None:
            return internal_server_error("", "UNAVAILABLE_DATA")

    if event == "NF_LOAD":
        if tgt_ue.supis is None and tgt_ue.any_ue is False:
            return internal_server_error("", "UNAVAILABLE_DATA")

    if event == "UE_MOBILITY":
        if tgt_ue.supis is None and tgt_ue.int_group_ids is None:
            return internal_server_error("", "UNAVAILABLE_DATA")

    if event == "UE_COMM":
        if tgt_ue.supis is None and tgt_ue.int_group_ids is None:
            return internal_server_error("", "UNAVAILABLE_DATA")

    if event == "NETWORK_PERFORMANCE":
        if (tgt_ue.supis is None and tgt_ue.int_group_ids is None and tgt_ue.any_ue is False) or event_filter.nw_perf_types is None:
            return internal_server_error("", "UNAVAILABLE_DATA")

    if event == "SERVICE_EXPERIENCE":
        if (tgt_ue.supis is None and tgt_ue.int_group_ids is None and tgt_ue.any_ue is None) or (event_filter.any_slice is None and event_filter.nsi_id_infos is None):
            return internal_server_error("", "UNAVAILABLE_DATA")
        
    if event == "QOS_SUSTAINABILITY":
        if (event_filter.network_area is None and event_filter.qos_requ is None) or tgt_ue.any_ue is False:
            return internal_server_error("", "UNAVAILABLE_DATA")

    if event == "ABNORMAL_BEHAVIOUR":
        if (tgt_ue.supis is None and tgt_ue.int_group_ids is None and tgt_ue.any_ue is None) or event_filter.expt_ana_type is None and event_filter.excep_ids is None:
            return internal_server_error("", "UNAVAILABLE_DATA")

    if event == "USER_DATA_CONGESTION":
        if tgt_ue.supis is None and tgt_ue.gpsis is None and tgt_ue.any_ue is None:
            return internal_server_error("", "UNAVAILABLE_DATA")
        
    if event == "SM_CONGESTION":
        if (event_filter.dnns is None and event_filter.snssais is None) or tgt_ue.supis is None:
            return internal_server_error("", "UNAVAILABLE_DATA")

    if event == "DISPERSION":
        if (tgt_ue.supis is None and tgt_ue.int_group_ids is None and (tgt_ue.any_ue is None or (tgt_ue.any_ue is not None and (event_filter.snssais is None and event_filter.network_area is None and event_filter.disper_reqs is None)))):
            return internal_server_error("", "UNAVAILABLE_DATA")

    if event == "RED_TRANS_EXP":
        if (tgt_ue.supis is None and tgt_ue.int_group_ids is None and tgt_ue.any_ue is None):
            return internal_server_error("", "UNAVAILABLE_DATA")
        
    if event == "WLAN_PERFORMANCE":
        if (tgt_ue.supis is None and tgt_ue.int_group_ids is None and (tgt_ue.any_ue is None or (tgt_ue.any_ue is not None and (event_filter.network_area is None and event_filter.wlan_reqs.ssids is None and event_filter.wlan_reqs.bssids is None)))):
            return internal_server_error("", "UNAVAILABLE_DATA")

    if event == "DN_PERFORMANCE":
        if (tgt_ue.supis is None and tgt_ue.int_group_ids is None and tgt_ue.any_ue is None):
            return internal_server_error("", "UNAVAILABLE_DATA")

    return 0


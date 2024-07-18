import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union
from flask import current_app
from ..core.responses import bad_request_error
import urllib.parse
import json

from openapi_server.models.analytics_data import AnalyticsData  # noqa: E501
from openapi_server.models.event_filter import EventFilter  # noqa: E501
from openapi_server.models.event_id import EventId  # noqa: E501
from openapi_server.models.event_reporting_requirement import EventReportingRequirement  # noqa: E501
from openapi_server.models.problem_details import ProblemDetails  # noqa: E501
from openapi_server.models.problem_details_analytics_info_request import ProblemDetailsAnalyticsInfoRequest  # noqa: E501
from openapi_server.models.target_ue_information import TargetUeInformation  # noqa: E501
from openapi_server import util
from ..core.analytics_controller import analytics_controller

analytics_controller = analytics_controller()

def get_nwdaf_analytics(event_id, ana_req=None, event_filter=None, supported_features=None, tgt_ue=None):  # noqa: E501
    """Read a NWDAF Analytics

     # noqa: E501

    :param event_id: Identify the analytics.
    :type event_id: dict | bytes
    :param ana_req: Identifies the analytics reporting requirement information.
    :type ana_req: dict | bytes
    :param event_filter: Identify the analytics.
    :type event_filter: dict | bytes
    :param supported_features: To filter irrelevant responses related to unsupported features.
    :type supported_features: str
    :param tgt_ue: Identify the target UE information.
    :type tgt_ue: dict | bytes

    :rtype: Union[AnalyticsData, Tuple[AnalyticsData, int], Tuple[AnalyticsData, int, Dict[str, str]]
    
    if connexion.request.is_json:
        event_id =  EventId.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        ana_req =  EventReportingRequirement.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        event_filter =  EventFilter.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        tgt_ue =  TargetUeInformation.from_dict(connexion.request.get_json())  # noqa: E501
    """
    #ana_req_dict = json.loads(ana_req)
   # ana_req = EventReportingRequirement.from_dict(ana_req_dict)
    #ana_req= ana_req.replace('\\', '')
    EVENTS=["LOAD_LEVEL_INFORMATION", "NSI_LOAD_LEVEL", "NF_LOAD", "NETWORK_PERFORMANCE", "QOS_SUSTAINABILITY", "USER_DATA_CONGESTION"]
    #Only developed events
    if event_id not in EVENTS:
        return bad_request_error(detail="The event_id is wrong", cause="No such event_id", invalid_params="event_id")
    if ana_req!=None:
        ana_req_dict = json.loads(ana_req)
        ana_req = EventReportingRequirement.from_dict(ana_req_dict)
    else:
        ana_req = EventReportingRequirement()

    if event_filter!=None:
        event_filter_dict = json.loads(event_filter)
        event_filter = EventFilter.from_dict(event_filter_dict)
    else:
        event_filter = EventFilter()

    if tgt_ue!=None:
        tgt_ue_dict = json.loads(tgt_ue)
        tgt_ue = TargetUeInformation.from_dict(tgt_ue_dict)
    else:
        tgt_ue = TargetUeInformation()

    # current_app.logger.debug(f"event: {event_id}")
    # current_app.logger.debug(f"anareq: {ana_req}")
    # current_app.logger.debug(f"event_filter: {event_filter}")
    # #current_app.logger.debug(supported_features)
    # current_app.logger.debug(f"tgt_ue: {tgt_ue}")
    
    res = analytics_controller.get_requests(event_id, ana_req, event_filter, supported_features, tgt_ue)
    current_app.logger.debug(res)

    return res

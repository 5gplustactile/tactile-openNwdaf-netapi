import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.analytics_subscriptions_transfer import AnalyticsSubscriptionsTransfer  # noqa: E501
from openapi_server.models.problem_details import ProblemDetails  # noqa: E501
from openapi_server import util
from ..core.transferDB_controller import transferDB_controller

transfer_controller = transferDB_controller()

def create_nwdaf_event_subscription_transfer(body):  # noqa: E501
    """Provide information about requested analytics subscriptions transfer and potentially create a new Individual NWDAF Event Subscription Transfer resource.

     # noqa: E501

    :param analytics_subscriptions_transfer: 
    :type analytics_subscriptions_transfer: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        body = AnalyticsSubscriptionsTransfer.from_dict(connexion.request.get_json())  # noqa: E501
    
    r = transfer_controller.insert_transfer(body)

    return r

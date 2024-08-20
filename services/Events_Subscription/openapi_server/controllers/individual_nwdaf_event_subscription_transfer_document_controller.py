import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.analytics_subscriptions_transfer import AnalyticsSubscriptionsTransfer  # noqa: E501
from openapi_server.models.problem_details import ProblemDetails  # noqa: E501
from openapi_server.models.redirect_response import RedirectResponse  # noqa: E501
from openapi_server import util
from ..core.transferDB_controller import transferDB_controller

transfer_controller = transferDB_controller()

def delete_nwdaf_event_subscription_transfer(transfer_id):  # noqa: E501
    """Delete an existing Individual NWDAF Event Subscription Transfer

     # noqa: E501

    :param transfer_id: String identifying a request for an analytics subscription transfer to the  Nnwdaf_EventsSubscription Service 
    :type transfer_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    r = transfer_controller.delete_transfer(transfer_id)

    return r


def update_nwdaf_event_subscription_transfer(transfer_id, body):  # noqa: E501
    """Update an existing Individual NWDAF Event Subscription Transfer

     # noqa: E501

    :param transfer_id: String identifying a request for an analytics subscription transfer to the  Nnwdaf_EventsSubscription Service 
    :type transfer_id: str
    :param analytics_subscriptions_transfer: 
    :type analytics_subscriptions_transfer: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        body = AnalyticsSubscriptionsTransfer.from_dict(connexion.request.get_json())  # noqa: E501
    r = transfer_controller.update_transfer(transfer_id, body)
    return r

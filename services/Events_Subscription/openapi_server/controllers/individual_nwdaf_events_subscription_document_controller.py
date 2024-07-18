import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.nnwdaf_events_subscription import NnwdafEventsSubscription  # noqa: E501
from openapi_server.models.problem_details import ProblemDetails  # noqa: E501
from openapi_server.models.redirect_response import RedirectResponse  # noqa: E501
from openapi_server import util
from ..core.eventsSubscriptions import delete_sub, update_sub

def delete_nwdaf_events_subscription(subscription_id):  # noqa: E501
    """Delete an existing Individual NWDAF Events Subscription

     # noqa: E501

    :param subscription_id: String identifying a subscription to the Nnwdaf_EventsSubscription Service
    :type subscription_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    r = delete_sub(subscription_id)
    return r


def update_nwdaf_events_subscription(subscription_id, body):  # noqa: E501
    """Update an existing Individual NWDAF Events Subscription

     # noqa: E501

    :param subscription_id: String identifying a subscription to the Nnwdaf_EventsSubscription Service
    :type subscription_id: str
    :param nnwdaf_events_subscription: 
    :type nnwdaf_events_subscription: dict | bytes

    :rtype: Union[NnwdafEventsSubscription, Tuple[NnwdafEventsSubscription, int], Tuple[NnwdafEventsSubscription, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        body = NnwdafEventsSubscription.from_dict(connexion.request.get_json())  # noqa: E501
    
    r = update_sub(subscription_id, body)
    return r

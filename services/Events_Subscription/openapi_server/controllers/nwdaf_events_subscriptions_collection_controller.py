import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.nnwdaf_events_subscription import NnwdafEventsSubscription  # noqa: E501
from openapi_server.models.problem_details import ProblemDetails  # noqa: E501
from openapi_server import util
from ..core.eventsSubscriptions import insert_sub
from flask import current_app

def create_nwdaf_events_subscription(body):  # noqa: E501
    """Create a new Individual NWDAF Events Subscription

     # noqa: E501

    :param nnwdaf_events_subscription: 
    :type nnwdaf_events_subscription: dict | bytes

    :rtype: Union[NnwdafEventsSubscription, Tuple[NnwdafEventsSubscription, int], Tuple[NnwdafEventsSubscription, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        body = NnwdafEventsSubscription.from_dict(connexion.request.get_json())  # noqa: E501

    current_app.logger.info("Creating subscription")
    r = insert_sub(body)
    current_app.logger.debug("Subscription created")
    return r

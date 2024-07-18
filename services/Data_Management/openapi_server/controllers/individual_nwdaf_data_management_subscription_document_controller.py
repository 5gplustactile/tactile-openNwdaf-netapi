import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.nnwdaf_data_management_subsc import NnwdafDataManagementSubsc  # noqa: E501
from openapi_server.models.problem_details import ProblemDetails  # noqa: E501
from openapi_server.models.redirect_response import RedirectResponse  # noqa: E501
from openapi_server import util
from ..core.data_controller import data_controller

data_controller = data_controller()

def delete_nwdaf_data_subscription(subscription_id):  # noqa: E501
    """unsubscribe from notifications

     # noqa: E501

    :param subscription_id: Event Subscription ID
    :type subscription_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """

    r = data_controller.delete_sub(subscription_id)
    return r


def update_nwdaf_data_subscription(subscription_id, body):  # noqa: E501
    """Update an existing Individual NWDAF Data Subscription.

     # noqa: E501

    :param subscription_id: Event Subscription ID
    :type subscription_id: str
    :param nnwdaf_data_management_subsc: 
    :type nnwdaf_data_management_subsc: dict | bytes

    :rtype: Union[NnwdafDataManagementSubsc, Tuple[NnwdafDataManagementSubsc, int], Tuple[NnwdafDataManagementSubsc, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        body = NnwdafDataManagementSubsc.from_dict(connexion.request.get_json())  # noqa: E501
    
    r = data_controller.update_sub(subscription_id, body)
    return r

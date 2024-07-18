import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.nnwdaf_data_management_subsc import NnwdafDataManagementSubsc  # noqa: E501
from openapi_server.models.problem_details import ProblemDetails  # noqa: E501
from openapi_server import util
from ..core.data_controller import data_controller

data_controller = data_controller()


def create_individual_subcription(body):  # noqa: E501
    """subscribe to notifications

     # noqa: E501

    :param nnwdaf_data_management_subsc: 
    :type nnwdaf_data_management_subsc: dict | bytes

    :rtype: Union[NnwdafDataManagementSubsc, Tuple[NnwdafDataManagementSubsc, int], Tuple[NnwdafDataManagementSubsc, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        body = NnwdafDataManagementSubsc.from_dict(connexion.request.get_json())  # noqa: E501

    r = data_controller.insert_sub(body)
    return r

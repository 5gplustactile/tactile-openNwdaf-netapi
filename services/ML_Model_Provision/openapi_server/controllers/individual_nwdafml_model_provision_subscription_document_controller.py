import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union
from ..core.mlSubs_controller import mlSubs_controller

from openapi_server.models.nwdaf_ml_model_prov_subsc import NwdafMLModelProvSubsc  # noqa: E501
from openapi_server.models.problem_details import ProblemDetails  # noqa: E501
from openapi_server.models.redirect_response import RedirectResponse  # noqa: E501
from openapi_server import util

mlsubs_controller = mlSubs_controller()
def delete_nwdafml_model_provision_subcription(subscription_id):  # noqa: E501
    """Delete an existing Individual NWDAF ML Model Provision Subscription.

     # noqa: E501

    :param subscription_id: String identifying a subscription to the Nnwdaf_MLModelProvision Service.
    :type subscription_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    r = mlsubs_controller.delete_mlsub(subscription_id)

    return r


def update_nwdafml_model_provision_subcription(subscription_id, body):  # noqa: E501
    """update an existing Individual NWDAF ML Model Provision Subscription

     # noqa: E501

    :param subscription_id: String identifying a subscription to the Nnwdaf_MLModelProvision Service.
    :type subscription_id: str
    :param nwdaf_ml_model_prov_subsc: 
    :type nwdaf_ml_model_prov_subsc: dict | bytes

    :rtype: Union[NwdafMLModelProvSubsc, Tuple[NwdafMLModelProvSubsc, int], Tuple[NwdafMLModelProvSubsc, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        body = NwdafMLModelProvSubsc.from_dict(connexion.request.get_json())  # noqa: E501
    
    r = mlsubs_controller.update_mlsub(subscription_id, body)
    return r

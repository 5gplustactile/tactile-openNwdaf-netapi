import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union
from ..core.mlSubs_controller import mlSubs_controller

from openapi_server.models.nwdaf_ml_model_prov_subsc import NwdafMLModelProvSubsc  # noqa: E501
from openapi_server.models.problem_details import ProblemDetails  # noqa: E501
from openapi_server import util

mlsubs_controller = mlSubs_controller()

def create_nwdafml_model_provision_subcription(body):  # noqa: E501
   """Create a new Individual NWDAF ML Model Provision Subscription resource.

   # noqa: E501

   :param nwdaf_ml_model_prov_subsc: 
   :type nwdaf_ml_model_prov_subsc: dict | bytes

    rtype: Union[NwdafMLModelProvSubsc, Tuple[NwdafMLModelProvSubsc, int], Tuple[NwdafMLModelProvSubsc, int, Dict[str, str]]
   """
   if connexion.request.is_json:
       body = NwdafMLModelProvSubsc.from_dict(connexion.request.get_json())  # noqa: E501
      
   r = mlsubs_controller.insert_mlsub(body)
   
   return r

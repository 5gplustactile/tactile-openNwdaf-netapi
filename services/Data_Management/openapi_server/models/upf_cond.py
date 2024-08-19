# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.tai import Tai
from openapi_server import util

from openapi_server.models.tai import Tai  # noqa: E501

class UpfCond(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, condition_type=None, smf_serving_area=None, tai_list=None):  # noqa: E501
        """UpfCond - a model defined in OpenAPI

        :param condition_type: The condition_type of this UpfCond.  # noqa: E501
        :type condition_type: str
        :param smf_serving_area: The smf_serving_area of this UpfCond.  # noqa: E501
        :type smf_serving_area: List[str]
        :param tai_list: The tai_list of this UpfCond.  # noqa: E501
        :type tai_list: List[Tai]
        """
        self.openapi_types = {
            'condition_type': str,
            'smf_serving_area': List[str],
            'tai_list': List[Tai]
        }

        self.attribute_map = {
            'condition_type': 'conditionType',
            'smf_serving_area': 'smfServingArea',
            'tai_list': 'taiList'
        }

        self._condition_type = condition_type
        self._smf_serving_area = smf_serving_area
        self._tai_list = tai_list

    @classmethod
    def from_dict(cls, dikt) -> 'UpfCond':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UpfCond of this UpfCond.  # noqa: E501
        :rtype: UpfCond
        """
        return util.deserialize_model(dikt, cls)

    @property
    def condition_type(self):
        """Gets the condition_type of this UpfCond.


        :return: The condition_type of this UpfCond.
        :rtype: str
        """
        return self._condition_type

    @condition_type.setter
    def condition_type(self, condition_type):
        """Sets the condition_type of this UpfCond.


        :param condition_type: The condition_type of this UpfCond.
        :type condition_type: str
        """
        allowed_values = ["UPF_COND"]  # noqa: E501
        if condition_type not in allowed_values:
            raise ValueError(
                "Invalid value for `condition_type` ({0}), must be one of {1}"
                .format(condition_type, allowed_values)
            )

        self._condition_type = condition_type

    @property
    def smf_serving_area(self):
        """Gets the smf_serving_area of this UpfCond.


        :return: The smf_serving_area of this UpfCond.
        :rtype: List[str]
        """
        return self._smf_serving_area

    @smf_serving_area.setter
    def smf_serving_area(self, smf_serving_area):
        """Sets the smf_serving_area of this UpfCond.


        :param smf_serving_area: The smf_serving_area of this UpfCond.
        :type smf_serving_area: List[str]
        """
        if smf_serving_area is not None and len(smf_serving_area) < 1:
            raise ValueError("Invalid value for `smf_serving_area`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._smf_serving_area = smf_serving_area

    @property
    def tai_list(self):
        """Gets the tai_list of this UpfCond.


        :return: The tai_list of this UpfCond.
        :rtype: List[Tai]
        """
        return self._tai_list

    @tai_list.setter
    def tai_list(self, tai_list):
        """Sets the tai_list of this UpfCond.


        :param tai_list: The tai_list of this UpfCond.
        :type tai_list: List[Tai]
        """
        if tai_list is not None and len(tai_list) < 1:
            raise ValueError("Invalid value for `tai_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._tai_list = tai_list
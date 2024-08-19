# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ddd_traffic_descriptor import DddTrafficDescriptor
from openapi_server.models.snssai import Snssai
from openapi_server import util

from openapi_server.models.ddd_traffic_descriptor import DddTrafficDescriptor  # noqa: E501
from openapi_server.models.snssai import Snssai  # noqa: E501

class TrafficDescriptor(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, dnn=None, s_nssai=None, ddd_traffic_descriptor_list=None):  # noqa: E501
        """TrafficDescriptor - a model defined in OpenAPI

        :param dnn: The dnn of this TrafficDescriptor.  # noqa: E501
        :type dnn: str
        :param s_nssai: The s_nssai of this TrafficDescriptor.  # noqa: E501
        :type s_nssai: Snssai
        :param ddd_traffic_descriptor_list: The ddd_traffic_descriptor_list of this TrafficDescriptor.  # noqa: E501
        :type ddd_traffic_descriptor_list: List[DddTrafficDescriptor]
        """
        self.openapi_types = {
            'dnn': str,
            's_nssai': Snssai,
            'ddd_traffic_descriptor_list': List[DddTrafficDescriptor]
        }

        self.attribute_map = {
            'dnn': 'dnn',
            's_nssai': 'sNssai',
            'ddd_traffic_descriptor_list': 'dddTrafficDescriptorList'
        }

        self._dnn = dnn
        self._s_nssai = s_nssai
        self._ddd_traffic_descriptor_list = ddd_traffic_descriptor_list

    @classmethod
    def from_dict(cls, dikt) -> 'TrafficDescriptor':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TrafficDescriptor of this TrafficDescriptor.  # noqa: E501
        :rtype: TrafficDescriptor
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dnn(self):
        """Gets the dnn of this TrafficDescriptor.

        String representing a Data Network as defined in clause 9A of 3GPP TS 23.003;  it shall contain either a DNN Network Identifier, or a full DNN with both the Network  Identifier and Operator Identifier, as specified in 3GPP TS 23.003 clause 9.1.1 and 9.1.2. It shall be coded as string in which the labels are separated by dots  (e.g. \"Label1.Label2.Label3\").   # noqa: E501

        :return: The dnn of this TrafficDescriptor.
        :rtype: str
        """
        return self._dnn

    @dnn.setter
    def dnn(self, dnn):
        """Sets the dnn of this TrafficDescriptor.

        String representing a Data Network as defined in clause 9A of 3GPP TS 23.003;  it shall contain either a DNN Network Identifier, or a full DNN with both the Network  Identifier and Operator Identifier, as specified in 3GPP TS 23.003 clause 9.1.1 and 9.1.2. It shall be coded as string in which the labels are separated by dots  (e.g. \"Label1.Label2.Label3\").   # noqa: E501

        :param dnn: The dnn of this TrafficDescriptor.
        :type dnn: str
        """

        self._dnn = dnn

    @property
    def s_nssai(self):
        """Gets the s_nssai of this TrafficDescriptor.


        :return: The s_nssai of this TrafficDescriptor.
        :rtype: Snssai
        """
        return self._s_nssai

    @s_nssai.setter
    def s_nssai(self, s_nssai):
        """Sets the s_nssai of this TrafficDescriptor.


        :param s_nssai: The s_nssai of this TrafficDescriptor.
        :type s_nssai: Snssai
        """

        self._s_nssai = s_nssai

    @property
    def ddd_traffic_descriptor_list(self):
        """Gets the ddd_traffic_descriptor_list of this TrafficDescriptor.


        :return: The ddd_traffic_descriptor_list of this TrafficDescriptor.
        :rtype: List[DddTrafficDescriptor]
        """
        return self._ddd_traffic_descriptor_list

    @ddd_traffic_descriptor_list.setter
    def ddd_traffic_descriptor_list(self, ddd_traffic_descriptor_list):
        """Sets the ddd_traffic_descriptor_list of this TrafficDescriptor.


        :param ddd_traffic_descriptor_list: The ddd_traffic_descriptor_list of this TrafficDescriptor.
        :type ddd_traffic_descriptor_list: List[DddTrafficDescriptor]
        """
        if ddd_traffic_descriptor_list is not None and len(ddd_traffic_descriptor_list) < 1:
            raise ValueError("Invalid value for `ddd_traffic_descriptor_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ddd_traffic_descriptor_list = ddd_traffic_descriptor_list
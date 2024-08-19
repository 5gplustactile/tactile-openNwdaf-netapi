# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.dnn_mb_smf_info_item import DnnMbSmfInfoItem
from openapi_server.models.ext_snssai import ExtSnssai
from openapi_server import util

from openapi_server.models.dnn_mb_smf_info_item import DnnMbSmfInfoItem  # noqa: E501
from openapi_server.models.ext_snssai import ExtSnssai  # noqa: E501

class SnssaiMbSmfInfoItem(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, s_nssai=None, dnn_info_list=None):  # noqa: E501
        """SnssaiMbSmfInfoItem - a model defined in OpenAPI

        :param s_nssai: The s_nssai of this SnssaiMbSmfInfoItem.  # noqa: E501
        :type s_nssai: ExtSnssai
        :param dnn_info_list: The dnn_info_list of this SnssaiMbSmfInfoItem.  # noqa: E501
        :type dnn_info_list: List[DnnMbSmfInfoItem]
        """
        self.openapi_types = {
            's_nssai': ExtSnssai,
            'dnn_info_list': List[DnnMbSmfInfoItem]
        }

        self.attribute_map = {
            's_nssai': 'sNssai',
            'dnn_info_list': 'dnnInfoList'
        }

        self._s_nssai = s_nssai
        self._dnn_info_list = dnn_info_list

    @classmethod
    def from_dict(cls, dikt) -> 'SnssaiMbSmfInfoItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SnssaiMbSmfInfoItem of this SnssaiMbSmfInfoItem.  # noqa: E501
        :rtype: SnssaiMbSmfInfoItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def s_nssai(self):
        """Gets the s_nssai of this SnssaiMbSmfInfoItem.


        :return: The s_nssai of this SnssaiMbSmfInfoItem.
        :rtype: ExtSnssai
        """
        return self._s_nssai

    @s_nssai.setter
    def s_nssai(self, s_nssai):
        """Sets the s_nssai of this SnssaiMbSmfInfoItem.


        :param s_nssai: The s_nssai of this SnssaiMbSmfInfoItem.
        :type s_nssai: ExtSnssai
        """
        if s_nssai is None:
            raise ValueError("Invalid value for `s_nssai`, must not be `None`")  # noqa: E501

        self._s_nssai = s_nssai

    @property
    def dnn_info_list(self):
        """Gets the dnn_info_list of this SnssaiMbSmfInfoItem.


        :return: The dnn_info_list of this SnssaiMbSmfInfoItem.
        :rtype: List[DnnMbSmfInfoItem]
        """
        return self._dnn_info_list

    @dnn_info_list.setter
    def dnn_info_list(self, dnn_info_list):
        """Sets the dnn_info_list of this SnssaiMbSmfInfoItem.


        :param dnn_info_list: The dnn_info_list of this SnssaiMbSmfInfoItem.
        :type dnn_info_list: List[DnnMbSmfInfoItem]
        """
        if dnn_info_list is None:
            raise ValueError("Invalid value for `dnn_info_list`, must not be `None`")  # noqa: E501
        if dnn_info_list is not None and len(dnn_info_list) < 1:
            raise ValueError("Invalid value for `dnn_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._dnn_info_list = dnn_info_list
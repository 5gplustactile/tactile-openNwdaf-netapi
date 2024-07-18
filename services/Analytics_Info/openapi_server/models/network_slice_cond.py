# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.snssai import Snssai
from openapi_server import util

from openapi_server.models.snssai import Snssai  # noqa: E501

class NetworkSliceCond(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, snssai_list=None, nsi_list=None):  # noqa: E501
        """NetworkSliceCond - a model defined in OpenAPI

        :param snssai_list: The snssai_list of this NetworkSliceCond.  # noqa: E501
        :type snssai_list: List[Snssai]
        :param nsi_list: The nsi_list of this NetworkSliceCond.  # noqa: E501
        :type nsi_list: List[str]
        """
        self.openapi_types = {
            'snssai_list': List[Snssai],
            'nsi_list': List[str]
        }

        self.attribute_map = {
            'snssai_list': 'snssaiList',
            'nsi_list': 'nsiList'
        }

        self._snssai_list = snssai_list
        self._nsi_list = nsi_list

    @classmethod
    def from_dict(cls, dikt) -> 'NetworkSliceCond':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NetworkSliceCond of this NetworkSliceCond.  # noqa: E501
        :rtype: NetworkSliceCond
        """
        return util.deserialize_model(dikt, cls)

    @property
    def snssai_list(self):
        """Gets the snssai_list of this NetworkSliceCond.


        :return: The snssai_list of this NetworkSliceCond.
        :rtype: List[Snssai]
        """
        return self._snssai_list

    @snssai_list.setter
    def snssai_list(self, snssai_list):
        """Sets the snssai_list of this NetworkSliceCond.


        :param snssai_list: The snssai_list of this NetworkSliceCond.
        :type snssai_list: List[Snssai]
        """
        if snssai_list is None:
            raise ValueError("Invalid value for `snssai_list`, must not be `None`")  # noqa: E501

        self._snssai_list = snssai_list

    @property
    def nsi_list(self):
        """Gets the nsi_list of this NetworkSliceCond.


        :return: The nsi_list of this NetworkSliceCond.
        :rtype: List[str]
        """
        return self._nsi_list

    @nsi_list.setter
    def nsi_list(self, nsi_list):
        """Sets the nsi_list of this NetworkSliceCond.


        :param nsi_list: The nsi_list of this NetworkSliceCond.
        :type nsi_list: List[str]
        """

        self._nsi_list = nsi_list

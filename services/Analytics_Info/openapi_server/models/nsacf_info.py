# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.nsacf_capability import NsacfCapability
from openapi_server.models.tai import Tai
from openapi_server.models.tai_range import TaiRange
from openapi_server import util

from openapi_server.models.nsacf_capability import NsacfCapability  # noqa: E501
from openapi_server.models.tai import Tai  # noqa: E501
from openapi_server.models.tai_range import TaiRange  # noqa: E501

class NsacfInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, nsacf_capability=None, tai_list=None, tai_range_list=None):  # noqa: E501
        """NsacfInfo - a model defined in OpenAPI

        :param nsacf_capability: The nsacf_capability of this NsacfInfo.  # noqa: E501
        :type nsacf_capability: NsacfCapability
        :param tai_list: The tai_list of this NsacfInfo.  # noqa: E501
        :type tai_list: List[Tai]
        :param tai_range_list: The tai_range_list of this NsacfInfo.  # noqa: E501
        :type tai_range_list: List[TaiRange]
        """
        self.openapi_types = {
            'nsacf_capability': NsacfCapability,
            'tai_list': List[Tai],
            'tai_range_list': List[TaiRange]
        }

        self.attribute_map = {
            'nsacf_capability': 'nsacfCapability',
            'tai_list': 'taiList',
            'tai_range_list': 'taiRangeList'
        }

        self._nsacf_capability = nsacf_capability
        self._tai_list = tai_list
        self._tai_range_list = tai_range_list

    @classmethod
    def from_dict(cls, dikt) -> 'NsacfInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NsacfInfo of this NsacfInfo.  # noqa: E501
        :rtype: NsacfInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nsacf_capability(self):
        """Gets the nsacf_capability of this NsacfInfo.


        :return: The nsacf_capability of this NsacfInfo.
        :rtype: NsacfCapability
        """
        return self._nsacf_capability

    @nsacf_capability.setter
    def nsacf_capability(self, nsacf_capability):
        """Sets the nsacf_capability of this NsacfInfo.


        :param nsacf_capability: The nsacf_capability of this NsacfInfo.
        :type nsacf_capability: NsacfCapability
        """
        if nsacf_capability is None:
            raise ValueError("Invalid value for `nsacf_capability`, must not be `None`")  # noqa: E501

        self._nsacf_capability = nsacf_capability

    @property
    def tai_list(self):
        """Gets the tai_list of this NsacfInfo.


        :return: The tai_list of this NsacfInfo.
        :rtype: List[Tai]
        """
        return self._tai_list

    @tai_list.setter
    def tai_list(self, tai_list):
        """Sets the tai_list of this NsacfInfo.


        :param tai_list: The tai_list of this NsacfInfo.
        :type tai_list: List[Tai]
        """
        if tai_list is not None and len(tai_list) < 1:
            raise ValueError("Invalid value for `tai_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._tai_list = tai_list

    @property
    def tai_range_list(self):
        """Gets the tai_range_list of this NsacfInfo.


        :return: The tai_range_list of this NsacfInfo.
        :rtype: List[TaiRange]
        """
        return self._tai_range_list

    @tai_range_list.setter
    def tai_range_list(self, tai_range_list):
        """Sets the tai_range_list of this NsacfInfo.


        :param tai_range_list: The tai_range_list of this NsacfInfo.
        :type tai_range_list: List[TaiRange]
        """
        if tai_range_list is not None and len(tai_range_list) < 1:
            raise ValueError("Invalid value for `tai_range_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._tai_range_list = tai_range_list
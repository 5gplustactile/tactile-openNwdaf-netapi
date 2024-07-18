# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.mbs_session import MbsSession
from openapi_server.models.snssai_mb_smf_info_item import SnssaiMbSmfInfoItem
from openapi_server.models.tai import Tai
from openapi_server.models.tai_range import TaiRange
from openapi_server.models.tmgi_range import TmgiRange
from openapi_server import util

from openapi_server.models.mbs_session import MbsSession  # noqa: E501
from openapi_server.models.snssai_mb_smf_info_item import SnssaiMbSmfInfoItem  # noqa: E501
from openapi_server.models.tai import Tai  # noqa: E501
from openapi_server.models.tai_range import TaiRange  # noqa: E501
from openapi_server.models.tmgi_range import TmgiRange  # noqa: E501

class MbSmfInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, s_nssai_info_list=None, tmgi_range_list=None, tai_list=None, tai_range_list=None, mbs_session_list=None):  # noqa: E501
        """MbSmfInfo - a model defined in OpenAPI

        :param s_nssai_info_list: The s_nssai_info_list of this MbSmfInfo.  # noqa: E501
        :type s_nssai_info_list: Dict[str, SnssaiMbSmfInfoItem]
        :param tmgi_range_list: The tmgi_range_list of this MbSmfInfo.  # noqa: E501
        :type tmgi_range_list: Dict[str, TmgiRange]
        :param tai_list: The tai_list of this MbSmfInfo.  # noqa: E501
        :type tai_list: List[Tai]
        :param tai_range_list: The tai_range_list of this MbSmfInfo.  # noqa: E501
        :type tai_range_list: List[TaiRange]
        :param mbs_session_list: The mbs_session_list of this MbSmfInfo.  # noqa: E501
        :type mbs_session_list: Dict[str, MbsSession]
        """
        self.openapi_types = {
            's_nssai_info_list': Dict[str, SnssaiMbSmfInfoItem],
            'tmgi_range_list': Dict[str, TmgiRange],
            'tai_list': List[Tai],
            'tai_range_list': List[TaiRange],
            'mbs_session_list': Dict[str, MbsSession]
        }

        self.attribute_map = {
            's_nssai_info_list': 'sNssaiInfoList',
            'tmgi_range_list': 'tmgiRangeList',
            'tai_list': 'taiList',
            'tai_range_list': 'taiRangeList',
            'mbs_session_list': 'mbsSessionList'
        }

        self._s_nssai_info_list = s_nssai_info_list
        self._tmgi_range_list = tmgi_range_list
        self._tai_list = tai_list
        self._tai_range_list = tai_range_list
        self._mbs_session_list = mbs_session_list

    @classmethod
    def from_dict(cls, dikt) -> 'MbSmfInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MbSmfInfo of this MbSmfInfo.  # noqa: E501
        :rtype: MbSmfInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def s_nssai_info_list(self):
        """Gets the s_nssai_info_list of this MbSmfInfo.

        A map (list of key-value pairs) where a valid JSON string serves as key  # noqa: E501

        :return: The s_nssai_info_list of this MbSmfInfo.
        :rtype: Dict[str, SnssaiMbSmfInfoItem]
        """
        return self._s_nssai_info_list

    @s_nssai_info_list.setter
    def s_nssai_info_list(self, s_nssai_info_list):
        """Sets the s_nssai_info_list of this MbSmfInfo.

        A map (list of key-value pairs) where a valid JSON string serves as key  # noqa: E501

        :param s_nssai_info_list: The s_nssai_info_list of this MbSmfInfo.
        :type s_nssai_info_list: Dict[str, SnssaiMbSmfInfoItem]
        """
        if s_nssai_info_list is not None and len(s_nssai_info_list) < 1:
            raise ValueError("Invalid value for `s_nssai_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._s_nssai_info_list = s_nssai_info_list

    @property
    def tmgi_range_list(self):
        """Gets the tmgi_range_list of this MbSmfInfo.

        A map (list of key-value pairs) where a valid JSON string serves as key  # noqa: E501

        :return: The tmgi_range_list of this MbSmfInfo.
        :rtype: Dict[str, TmgiRange]
        """
        return self._tmgi_range_list

    @tmgi_range_list.setter
    def tmgi_range_list(self, tmgi_range_list):
        """Sets the tmgi_range_list of this MbSmfInfo.

        A map (list of key-value pairs) where a valid JSON string serves as key  # noqa: E501

        :param tmgi_range_list: The tmgi_range_list of this MbSmfInfo.
        :type tmgi_range_list: Dict[str, TmgiRange]
        """
        if tmgi_range_list is not None and len(tmgi_range_list) < 1:
            raise ValueError("Invalid value for `tmgi_range_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._tmgi_range_list = tmgi_range_list

    @property
    def tai_list(self):
        """Gets the tai_list of this MbSmfInfo.


        :return: The tai_list of this MbSmfInfo.
        :rtype: List[Tai]
        """
        return self._tai_list

    @tai_list.setter
    def tai_list(self, tai_list):
        """Sets the tai_list of this MbSmfInfo.


        :param tai_list: The tai_list of this MbSmfInfo.
        :type tai_list: List[Tai]
        """
        if tai_list is not None and len(tai_list) < 1:
            raise ValueError("Invalid value for `tai_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._tai_list = tai_list

    @property
    def tai_range_list(self):
        """Gets the tai_range_list of this MbSmfInfo.


        :return: The tai_range_list of this MbSmfInfo.
        :rtype: List[TaiRange]
        """
        return self._tai_range_list

    @tai_range_list.setter
    def tai_range_list(self, tai_range_list):
        """Sets the tai_range_list of this MbSmfInfo.


        :param tai_range_list: The tai_range_list of this MbSmfInfo.
        :type tai_range_list: List[TaiRange]
        """
        if tai_range_list is not None and len(tai_range_list) < 1:
            raise ValueError("Invalid value for `tai_range_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._tai_range_list = tai_range_list

    @property
    def mbs_session_list(self):
        """Gets the mbs_session_list of this MbSmfInfo.

        A map (list of key-value pairs) where a valid JSON string serves as key  # noqa: E501

        :return: The mbs_session_list of this MbSmfInfo.
        :rtype: Dict[str, MbsSession]
        """
        return self._mbs_session_list

    @mbs_session_list.setter
    def mbs_session_list(self, mbs_session_list):
        """Sets the mbs_session_list of this MbSmfInfo.

        A map (list of key-value pairs) where a valid JSON string serves as key  # noqa: E501

        :param mbs_session_list: The mbs_session_list of this MbSmfInfo.
        :type mbs_session_list: Dict[str, MbsSession]
        """
        if mbs_session_list is not None and len(mbs_session_list) < 1:
            raise ValueError("Invalid value for `mbs_session_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._mbs_session_list = mbs_session_list

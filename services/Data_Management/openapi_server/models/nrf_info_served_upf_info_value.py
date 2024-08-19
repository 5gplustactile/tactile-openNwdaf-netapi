# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.atsss_capability import AtsssCapability
from openapi_server.models.interface_upf_info_item import InterfaceUpfInfoItem
from openapi_server.models.pdu_session_type import PduSessionType
from openapi_server.models.snssai_upf_info_item import SnssaiUpfInfoItem
from openapi_server.models.tai import Tai
from openapi_server.models.tai_range import TaiRange
from openapi_server.models.tngf_info import TngfInfo
from openapi_server.models.twif_info import TwifInfo
from openapi_server.models.upf_info import UpfInfo
from openapi_server.models.w_agf_info import WAgfInfo
from openapi_server import util

from openapi_server.models.atsss_capability import AtsssCapability  # noqa: E501
from openapi_server.models.interface_upf_info_item import InterfaceUpfInfoItem  # noqa: E501
from openapi_server.models.pdu_session_type import PduSessionType  # noqa: E501
from openapi_server.models.snssai_upf_info_item import SnssaiUpfInfoItem  # noqa: E501
from openapi_server.models.tai import Tai  # noqa: E501
from openapi_server.models.tai_range import TaiRange  # noqa: E501
from openapi_server.models.tngf_info import TngfInfo  # noqa: E501
from openapi_server.models.twif_info import TwifInfo  # noqa: E501
from openapi_server.models.upf_info import UpfInfo  # noqa: E501
from openapi_server.models.w_agf_info import WAgfInfo  # noqa: E501

class NrfInfoServedUpfInfoValue(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, s_nssai_upf_info_list=None, smf_serving_area=None, interface_upf_info_list=None, iwk_eps_ind=False, sxa_ind=None, pdu_session_types=None, atsss_capability=None, ue_ip_addr_ind=False, tai_list=None, tai_range_list=None, w_agf_info=None, tngf_info=None, twif_info=None, priority=None, redundant_gtpu=False, ipups=False, data_forwarding=False, supported_pfcp_features=None):  # noqa: E501
        """NrfInfoServedUpfInfoValue - a model defined in OpenAPI

        :param s_nssai_upf_info_list: The s_nssai_upf_info_list of this NrfInfoServedUpfInfoValue.  # noqa: E501
        :type s_nssai_upf_info_list: List[SnssaiUpfInfoItem]
        :param smf_serving_area: The smf_serving_area of this NrfInfoServedUpfInfoValue.  # noqa: E501
        :type smf_serving_area: List[str]
        :param interface_upf_info_list: The interface_upf_info_list of this NrfInfoServedUpfInfoValue.  # noqa: E501
        :type interface_upf_info_list: List[InterfaceUpfInfoItem]
        :param iwk_eps_ind: The iwk_eps_ind of this NrfInfoServedUpfInfoValue.  # noqa: E501
        :type iwk_eps_ind: bool
        :param sxa_ind: The sxa_ind of this NrfInfoServedUpfInfoValue.  # noqa: E501
        :type sxa_ind: bool
        :param pdu_session_types: The pdu_session_types of this NrfInfoServedUpfInfoValue.  # noqa: E501
        :type pdu_session_types: List[PduSessionType]
        :param atsss_capability: The atsss_capability of this NrfInfoServedUpfInfoValue.  # noqa: E501
        :type atsss_capability: AtsssCapability
        :param ue_ip_addr_ind: The ue_ip_addr_ind of this NrfInfoServedUpfInfoValue.  # noqa: E501
        :type ue_ip_addr_ind: bool
        :param tai_list: The tai_list of this NrfInfoServedUpfInfoValue.  # noqa: E501
        :type tai_list: List[Tai]
        :param tai_range_list: The tai_range_list of this NrfInfoServedUpfInfoValue.  # noqa: E501
        :type tai_range_list: List[TaiRange]
        :param w_agf_info: The w_agf_info of this NrfInfoServedUpfInfoValue.  # noqa: E501
        :type w_agf_info: WAgfInfo
        :param tngf_info: The tngf_info of this NrfInfoServedUpfInfoValue.  # noqa: E501
        :type tngf_info: TngfInfo
        :param twif_info: The twif_info of this NrfInfoServedUpfInfoValue.  # noqa: E501
        :type twif_info: TwifInfo
        :param priority: The priority of this NrfInfoServedUpfInfoValue.  # noqa: E501
        :type priority: int
        :param redundant_gtpu: The redundant_gtpu of this NrfInfoServedUpfInfoValue.  # noqa: E501
        :type redundant_gtpu: bool
        :param ipups: The ipups of this NrfInfoServedUpfInfoValue.  # noqa: E501
        :type ipups: bool
        :param data_forwarding: The data_forwarding of this NrfInfoServedUpfInfoValue.  # noqa: E501
        :type data_forwarding: bool
        :param supported_pfcp_features: The supported_pfcp_features of this NrfInfoServedUpfInfoValue.  # noqa: E501
        :type supported_pfcp_features: str
        """
        self.openapi_types = {
            's_nssai_upf_info_list': List[SnssaiUpfInfoItem],
            'smf_serving_area': List[str],
            'interface_upf_info_list': List[InterfaceUpfInfoItem],
            'iwk_eps_ind': bool,
            'sxa_ind': bool,
            'pdu_session_types': List[PduSessionType],
            'atsss_capability': AtsssCapability,
            'ue_ip_addr_ind': bool,
            'tai_list': List[Tai],
            'tai_range_list': List[TaiRange],
            'w_agf_info': WAgfInfo,
            'tngf_info': TngfInfo,
            'twif_info': TwifInfo,
            'priority': int,
            'redundant_gtpu': bool,
            'ipups': bool,
            'data_forwarding': bool,
            'supported_pfcp_features': str
        }

        self.attribute_map = {
            's_nssai_upf_info_list': 'sNssaiUpfInfoList',
            'smf_serving_area': 'smfServingArea',
            'interface_upf_info_list': 'interfaceUpfInfoList',
            'iwk_eps_ind': 'iwkEpsInd',
            'sxa_ind': 'sxaInd',
            'pdu_session_types': 'pduSessionTypes',
            'atsss_capability': 'atsssCapability',
            'ue_ip_addr_ind': 'ueIpAddrInd',
            'tai_list': 'taiList',
            'tai_range_list': 'taiRangeList',
            'w_agf_info': 'wAgfInfo',
            'tngf_info': 'tngfInfo',
            'twif_info': 'twifInfo',
            'priority': 'priority',
            'redundant_gtpu': 'redundantGtpu',
            'ipups': 'ipups',
            'data_forwarding': 'dataForwarding',
            'supported_pfcp_features': 'supportedPfcpFeatures'
        }

        self._s_nssai_upf_info_list = s_nssai_upf_info_list
        self._smf_serving_area = smf_serving_area
        self._interface_upf_info_list = interface_upf_info_list
        self._iwk_eps_ind = iwk_eps_ind
        self._sxa_ind = sxa_ind
        self._pdu_session_types = pdu_session_types
        self._atsss_capability = atsss_capability
        self._ue_ip_addr_ind = ue_ip_addr_ind
        self._tai_list = tai_list
        self._tai_range_list = tai_range_list
        self._w_agf_info = w_agf_info
        self._tngf_info = tngf_info
        self._twif_info = twif_info
        self._priority = priority
        self._redundant_gtpu = redundant_gtpu
        self._ipups = ipups
        self._data_forwarding = data_forwarding
        self._supported_pfcp_features = supported_pfcp_features

    @classmethod
    def from_dict(cls, dikt) -> 'NrfInfoServedUpfInfoValue':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NrfInfo_servedUpfInfo_value of this NrfInfoServedUpfInfoValue.  # noqa: E501
        :rtype: NrfInfoServedUpfInfoValue
        """
        return util.deserialize_model(dikt, cls)

    @property
    def s_nssai_upf_info_list(self):
        """Gets the s_nssai_upf_info_list of this NrfInfoServedUpfInfoValue.


        :return: The s_nssai_upf_info_list of this NrfInfoServedUpfInfoValue.
        :rtype: List[SnssaiUpfInfoItem]
        """
        return self._s_nssai_upf_info_list

    @s_nssai_upf_info_list.setter
    def s_nssai_upf_info_list(self, s_nssai_upf_info_list):
        """Sets the s_nssai_upf_info_list of this NrfInfoServedUpfInfoValue.


        :param s_nssai_upf_info_list: The s_nssai_upf_info_list of this NrfInfoServedUpfInfoValue.
        :type s_nssai_upf_info_list: List[SnssaiUpfInfoItem]
        """
        if s_nssai_upf_info_list is None:
            raise ValueError("Invalid value for `s_nssai_upf_info_list`, must not be `None`")  # noqa: E501
        if s_nssai_upf_info_list is not None and len(s_nssai_upf_info_list) < 1:
            raise ValueError("Invalid value for `s_nssai_upf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._s_nssai_upf_info_list = s_nssai_upf_info_list

    @property
    def smf_serving_area(self):
        """Gets the smf_serving_area of this NrfInfoServedUpfInfoValue.


        :return: The smf_serving_area of this NrfInfoServedUpfInfoValue.
        :rtype: List[str]
        """
        return self._smf_serving_area

    @smf_serving_area.setter
    def smf_serving_area(self, smf_serving_area):
        """Sets the smf_serving_area of this NrfInfoServedUpfInfoValue.


        :param smf_serving_area: The smf_serving_area of this NrfInfoServedUpfInfoValue.
        :type smf_serving_area: List[str]
        """
        if smf_serving_area is not None and len(smf_serving_area) < 1:
            raise ValueError("Invalid value for `smf_serving_area`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._smf_serving_area = smf_serving_area

    @property
    def interface_upf_info_list(self):
        """Gets the interface_upf_info_list of this NrfInfoServedUpfInfoValue.


        :return: The interface_upf_info_list of this NrfInfoServedUpfInfoValue.
        :rtype: List[InterfaceUpfInfoItem]
        """
        return self._interface_upf_info_list

    @interface_upf_info_list.setter
    def interface_upf_info_list(self, interface_upf_info_list):
        """Sets the interface_upf_info_list of this NrfInfoServedUpfInfoValue.


        :param interface_upf_info_list: The interface_upf_info_list of this NrfInfoServedUpfInfoValue.
        :type interface_upf_info_list: List[InterfaceUpfInfoItem]
        """
        if interface_upf_info_list is not None and len(interface_upf_info_list) < 1:
            raise ValueError("Invalid value for `interface_upf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._interface_upf_info_list = interface_upf_info_list

    @property
    def iwk_eps_ind(self):
        """Gets the iwk_eps_ind of this NrfInfoServedUpfInfoValue.


        :return: The iwk_eps_ind of this NrfInfoServedUpfInfoValue.
        :rtype: bool
        """
        return self._iwk_eps_ind

    @iwk_eps_ind.setter
    def iwk_eps_ind(self, iwk_eps_ind):
        """Sets the iwk_eps_ind of this NrfInfoServedUpfInfoValue.


        :param iwk_eps_ind: The iwk_eps_ind of this NrfInfoServedUpfInfoValue.
        :type iwk_eps_ind: bool
        """

        self._iwk_eps_ind = iwk_eps_ind

    @property
    def sxa_ind(self):
        """Gets the sxa_ind of this NrfInfoServedUpfInfoValue.


        :return: The sxa_ind of this NrfInfoServedUpfInfoValue.
        :rtype: bool
        """
        return self._sxa_ind

    @sxa_ind.setter
    def sxa_ind(self, sxa_ind):
        """Sets the sxa_ind of this NrfInfoServedUpfInfoValue.


        :param sxa_ind: The sxa_ind of this NrfInfoServedUpfInfoValue.
        :type sxa_ind: bool
        """

        self._sxa_ind = sxa_ind

    @property
    def pdu_session_types(self):
        """Gets the pdu_session_types of this NrfInfoServedUpfInfoValue.


        :return: The pdu_session_types of this NrfInfoServedUpfInfoValue.
        :rtype: List[PduSessionType]
        """
        return self._pdu_session_types

    @pdu_session_types.setter
    def pdu_session_types(self, pdu_session_types):
        """Sets the pdu_session_types of this NrfInfoServedUpfInfoValue.


        :param pdu_session_types: The pdu_session_types of this NrfInfoServedUpfInfoValue.
        :type pdu_session_types: List[PduSessionType]
        """
        if pdu_session_types is not None and len(pdu_session_types) < 1:
            raise ValueError("Invalid value for `pdu_session_types`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._pdu_session_types = pdu_session_types

    @property
    def atsss_capability(self):
        """Gets the atsss_capability of this NrfInfoServedUpfInfoValue.


        :return: The atsss_capability of this NrfInfoServedUpfInfoValue.
        :rtype: AtsssCapability
        """
        return self._atsss_capability

    @atsss_capability.setter
    def atsss_capability(self, atsss_capability):
        """Sets the atsss_capability of this NrfInfoServedUpfInfoValue.


        :param atsss_capability: The atsss_capability of this NrfInfoServedUpfInfoValue.
        :type atsss_capability: AtsssCapability
        """

        self._atsss_capability = atsss_capability

    @property
    def ue_ip_addr_ind(self):
        """Gets the ue_ip_addr_ind of this NrfInfoServedUpfInfoValue.


        :return: The ue_ip_addr_ind of this NrfInfoServedUpfInfoValue.
        :rtype: bool
        """
        return self._ue_ip_addr_ind

    @ue_ip_addr_ind.setter
    def ue_ip_addr_ind(self, ue_ip_addr_ind):
        """Sets the ue_ip_addr_ind of this NrfInfoServedUpfInfoValue.


        :param ue_ip_addr_ind: The ue_ip_addr_ind of this NrfInfoServedUpfInfoValue.
        :type ue_ip_addr_ind: bool
        """

        self._ue_ip_addr_ind = ue_ip_addr_ind

    @property
    def tai_list(self):
        """Gets the tai_list of this NrfInfoServedUpfInfoValue.


        :return: The tai_list of this NrfInfoServedUpfInfoValue.
        :rtype: List[Tai]
        """
        return self._tai_list

    @tai_list.setter
    def tai_list(self, tai_list):
        """Sets the tai_list of this NrfInfoServedUpfInfoValue.


        :param tai_list: The tai_list of this NrfInfoServedUpfInfoValue.
        :type tai_list: List[Tai]
        """
        if tai_list is not None and len(tai_list) < 1:
            raise ValueError("Invalid value for `tai_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._tai_list = tai_list

    @property
    def tai_range_list(self):
        """Gets the tai_range_list of this NrfInfoServedUpfInfoValue.


        :return: The tai_range_list of this NrfInfoServedUpfInfoValue.
        :rtype: List[TaiRange]
        """
        return self._tai_range_list

    @tai_range_list.setter
    def tai_range_list(self, tai_range_list):
        """Sets the tai_range_list of this NrfInfoServedUpfInfoValue.


        :param tai_range_list: The tai_range_list of this NrfInfoServedUpfInfoValue.
        :type tai_range_list: List[TaiRange]
        """
        if tai_range_list is not None and len(tai_range_list) < 1:
            raise ValueError("Invalid value for `tai_range_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._tai_range_list = tai_range_list

    @property
    def w_agf_info(self):
        """Gets the w_agf_info of this NrfInfoServedUpfInfoValue.


        :return: The w_agf_info of this NrfInfoServedUpfInfoValue.
        :rtype: WAgfInfo
        """
        return self._w_agf_info

    @w_agf_info.setter
    def w_agf_info(self, w_agf_info):
        """Sets the w_agf_info of this NrfInfoServedUpfInfoValue.


        :param w_agf_info: The w_agf_info of this NrfInfoServedUpfInfoValue.
        :type w_agf_info: WAgfInfo
        """

        self._w_agf_info = w_agf_info

    @property
    def tngf_info(self):
        """Gets the tngf_info of this NrfInfoServedUpfInfoValue.


        :return: The tngf_info of this NrfInfoServedUpfInfoValue.
        :rtype: TngfInfo
        """
        return self._tngf_info

    @tngf_info.setter
    def tngf_info(self, tngf_info):
        """Sets the tngf_info of this NrfInfoServedUpfInfoValue.


        :param tngf_info: The tngf_info of this NrfInfoServedUpfInfoValue.
        :type tngf_info: TngfInfo
        """

        self._tngf_info = tngf_info

    @property
    def twif_info(self):
        """Gets the twif_info of this NrfInfoServedUpfInfoValue.


        :return: The twif_info of this NrfInfoServedUpfInfoValue.
        :rtype: TwifInfo
        """
        return self._twif_info

    @twif_info.setter
    def twif_info(self, twif_info):
        """Sets the twif_info of this NrfInfoServedUpfInfoValue.


        :param twif_info: The twif_info of this NrfInfoServedUpfInfoValue.
        :type twif_info: TwifInfo
        """

        self._twif_info = twif_info

    @property
    def priority(self):
        """Gets the priority of this NrfInfoServedUpfInfoValue.


        :return: The priority of this NrfInfoServedUpfInfoValue.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this NrfInfoServedUpfInfoValue.


        :param priority: The priority of this NrfInfoServedUpfInfoValue.
        :type priority: int
        """
        if priority is not None and priority > 65535:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value less than or equal to `65535`")  # noqa: E501
        if priority is not None and priority < 0:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value greater than or equal to `0`")  # noqa: E501

        self._priority = priority

    @property
    def redundant_gtpu(self):
        """Gets the redundant_gtpu of this NrfInfoServedUpfInfoValue.


        :return: The redundant_gtpu of this NrfInfoServedUpfInfoValue.
        :rtype: bool
        """
        return self._redundant_gtpu

    @redundant_gtpu.setter
    def redundant_gtpu(self, redundant_gtpu):
        """Sets the redundant_gtpu of this NrfInfoServedUpfInfoValue.


        :param redundant_gtpu: The redundant_gtpu of this NrfInfoServedUpfInfoValue.
        :type redundant_gtpu: bool
        """

        self._redundant_gtpu = redundant_gtpu

    @property
    def ipups(self):
        """Gets the ipups of this NrfInfoServedUpfInfoValue.


        :return: The ipups of this NrfInfoServedUpfInfoValue.
        :rtype: bool
        """
        return self._ipups

    @ipups.setter
    def ipups(self, ipups):
        """Sets the ipups of this NrfInfoServedUpfInfoValue.


        :param ipups: The ipups of this NrfInfoServedUpfInfoValue.
        :type ipups: bool
        """

        self._ipups = ipups

    @property
    def data_forwarding(self):
        """Gets the data_forwarding of this NrfInfoServedUpfInfoValue.


        :return: The data_forwarding of this NrfInfoServedUpfInfoValue.
        :rtype: bool
        """
        return self._data_forwarding

    @data_forwarding.setter
    def data_forwarding(self, data_forwarding):
        """Sets the data_forwarding of this NrfInfoServedUpfInfoValue.


        :param data_forwarding: The data_forwarding of this NrfInfoServedUpfInfoValue.
        :type data_forwarding: bool
        """

        self._data_forwarding = data_forwarding

    @property
    def supported_pfcp_features(self):
        """Gets the supported_pfcp_features of this NrfInfoServedUpfInfoValue.


        :return: The supported_pfcp_features of this NrfInfoServedUpfInfoValue.
        :rtype: str
        """
        return self._supported_pfcp_features

    @supported_pfcp_features.setter
    def supported_pfcp_features(self, supported_pfcp_features):
        """Sets the supported_pfcp_features of this NrfInfoServedUpfInfoValue.


        :param supported_pfcp_features: The supported_pfcp_features of this NrfInfoServedUpfInfoValue.
        :type supported_pfcp_features: str
        """

        self._supported_pfcp_features = supported_pfcp_features
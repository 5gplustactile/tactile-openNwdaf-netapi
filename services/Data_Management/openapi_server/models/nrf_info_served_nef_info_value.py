# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.af_event_exposure_data import AfEventExposureData
from openapi_server.models.identity_range import IdentityRange
from openapi_server.models.nef_info import NefInfo
from openapi_server.models.pfd_data import PfdData
from openapi_server.models.tai import Tai
from openapi_server.models.tai_range import TaiRange
from openapi_server.models.un_trust_af_info import UnTrustAfInfo
from openapi_server import util

from openapi_server.models.af_event_exposure_data import AfEventExposureData  # noqa: E501
from openapi_server.models.identity_range import IdentityRange  # noqa: E501
from openapi_server.models.nef_info import NefInfo  # noqa: E501
from openapi_server.models.pfd_data import PfdData  # noqa: E501
from openapi_server.models.tai import Tai  # noqa: E501
from openapi_server.models.tai_range import TaiRange  # noqa: E501
from openapi_server.models.un_trust_af_info import UnTrustAfInfo  # noqa: E501

class NrfInfoServedNefInfoValue(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, nef_id=None, pfd_data=None, af_ee_data=None, gpsi_ranges=None, external_group_identifiers_ranges=None, served_fqdn_list=None, tai_list=None, tai_range_list=None, dnai_list=None, un_trust_af_info_list=None, uas_nf_functionality_ind=False):  # noqa: E501
        """NrfInfoServedNefInfoValue - a model defined in OpenAPI

        :param nef_id: The nef_id of this NrfInfoServedNefInfoValue.  # noqa: E501
        :type nef_id: str
        :param pfd_data: The pfd_data of this NrfInfoServedNefInfoValue.  # noqa: E501
        :type pfd_data: PfdData
        :param af_ee_data: The af_ee_data of this NrfInfoServedNefInfoValue.  # noqa: E501
        :type af_ee_data: AfEventExposureData
        :param gpsi_ranges: The gpsi_ranges of this NrfInfoServedNefInfoValue.  # noqa: E501
        :type gpsi_ranges: List[IdentityRange]
        :param external_group_identifiers_ranges: The external_group_identifiers_ranges of this NrfInfoServedNefInfoValue.  # noqa: E501
        :type external_group_identifiers_ranges: List[IdentityRange]
        :param served_fqdn_list: The served_fqdn_list of this NrfInfoServedNefInfoValue.  # noqa: E501
        :type served_fqdn_list: List[str]
        :param tai_list: The tai_list of this NrfInfoServedNefInfoValue.  # noqa: E501
        :type tai_list: List[Tai]
        :param tai_range_list: The tai_range_list of this NrfInfoServedNefInfoValue.  # noqa: E501
        :type tai_range_list: List[TaiRange]
        :param dnai_list: The dnai_list of this NrfInfoServedNefInfoValue.  # noqa: E501
        :type dnai_list: List[str]
        :param un_trust_af_info_list: The un_trust_af_info_list of this NrfInfoServedNefInfoValue.  # noqa: E501
        :type un_trust_af_info_list: List[UnTrustAfInfo]
        :param uas_nf_functionality_ind: The uas_nf_functionality_ind of this NrfInfoServedNefInfoValue.  # noqa: E501
        :type uas_nf_functionality_ind: bool
        """
        self.openapi_types = {
            'nef_id': str,
            'pfd_data': PfdData,
            'af_ee_data': AfEventExposureData,
            'gpsi_ranges': List[IdentityRange],
            'external_group_identifiers_ranges': List[IdentityRange],
            'served_fqdn_list': List[str],
            'tai_list': List[Tai],
            'tai_range_list': List[TaiRange],
            'dnai_list': List[str],
            'un_trust_af_info_list': List[UnTrustAfInfo],
            'uas_nf_functionality_ind': bool
        }

        self.attribute_map = {
            'nef_id': 'nefId',
            'pfd_data': 'pfdData',
            'af_ee_data': 'afEeData',
            'gpsi_ranges': 'gpsiRanges',
            'external_group_identifiers_ranges': 'externalGroupIdentifiersRanges',
            'served_fqdn_list': 'servedFqdnList',
            'tai_list': 'taiList',
            'tai_range_list': 'taiRangeList',
            'dnai_list': 'dnaiList',
            'un_trust_af_info_list': 'unTrustAfInfoList',
            'uas_nf_functionality_ind': 'uasNfFunctionalityInd'
        }

        self._nef_id = nef_id
        self._pfd_data = pfd_data
        self._af_ee_data = af_ee_data
        self._gpsi_ranges = gpsi_ranges
        self._external_group_identifiers_ranges = external_group_identifiers_ranges
        self._served_fqdn_list = served_fqdn_list
        self._tai_list = tai_list
        self._tai_range_list = tai_range_list
        self._dnai_list = dnai_list
        self._un_trust_af_info_list = un_trust_af_info_list
        self._uas_nf_functionality_ind = uas_nf_functionality_ind

    @classmethod
    def from_dict(cls, dikt) -> 'NrfInfoServedNefInfoValue':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NrfInfo_servedNefInfo_value of this NrfInfoServedNefInfoValue.  # noqa: E501
        :rtype: NrfInfoServedNefInfoValue
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nef_id(self):
        """Gets the nef_id of this NrfInfoServedNefInfoValue.

        Identity of the NEF  # noqa: E501

        :return: The nef_id of this NrfInfoServedNefInfoValue.
        :rtype: str
        """
        return self._nef_id

    @nef_id.setter
    def nef_id(self, nef_id):
        """Sets the nef_id of this NrfInfoServedNefInfoValue.

        Identity of the NEF  # noqa: E501

        :param nef_id: The nef_id of this NrfInfoServedNefInfoValue.
        :type nef_id: str
        """

        self._nef_id = nef_id

    @property
    def pfd_data(self):
        """Gets the pfd_data of this NrfInfoServedNefInfoValue.


        :return: The pfd_data of this NrfInfoServedNefInfoValue.
        :rtype: PfdData
        """
        return self._pfd_data

    @pfd_data.setter
    def pfd_data(self, pfd_data):
        """Sets the pfd_data of this NrfInfoServedNefInfoValue.


        :param pfd_data: The pfd_data of this NrfInfoServedNefInfoValue.
        :type pfd_data: PfdData
        """

        self._pfd_data = pfd_data

    @property
    def af_ee_data(self):
        """Gets the af_ee_data of this NrfInfoServedNefInfoValue.


        :return: The af_ee_data of this NrfInfoServedNefInfoValue.
        :rtype: AfEventExposureData
        """
        return self._af_ee_data

    @af_ee_data.setter
    def af_ee_data(self, af_ee_data):
        """Sets the af_ee_data of this NrfInfoServedNefInfoValue.


        :param af_ee_data: The af_ee_data of this NrfInfoServedNefInfoValue.
        :type af_ee_data: AfEventExposureData
        """

        self._af_ee_data = af_ee_data

    @property
    def gpsi_ranges(self):
        """Gets the gpsi_ranges of this NrfInfoServedNefInfoValue.


        :return: The gpsi_ranges of this NrfInfoServedNefInfoValue.
        :rtype: List[IdentityRange]
        """
        return self._gpsi_ranges

    @gpsi_ranges.setter
    def gpsi_ranges(self, gpsi_ranges):
        """Sets the gpsi_ranges of this NrfInfoServedNefInfoValue.


        :param gpsi_ranges: The gpsi_ranges of this NrfInfoServedNefInfoValue.
        :type gpsi_ranges: List[IdentityRange]
        """
        if gpsi_ranges is not None and len(gpsi_ranges) < 1:
            raise ValueError("Invalid value for `gpsi_ranges`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._gpsi_ranges = gpsi_ranges

    @property
    def external_group_identifiers_ranges(self):
        """Gets the external_group_identifiers_ranges of this NrfInfoServedNefInfoValue.


        :return: The external_group_identifiers_ranges of this NrfInfoServedNefInfoValue.
        :rtype: List[IdentityRange]
        """
        return self._external_group_identifiers_ranges

    @external_group_identifiers_ranges.setter
    def external_group_identifiers_ranges(self, external_group_identifiers_ranges):
        """Sets the external_group_identifiers_ranges of this NrfInfoServedNefInfoValue.


        :param external_group_identifiers_ranges: The external_group_identifiers_ranges of this NrfInfoServedNefInfoValue.
        :type external_group_identifiers_ranges: List[IdentityRange]
        """
        if external_group_identifiers_ranges is not None and len(external_group_identifiers_ranges) < 1:
            raise ValueError("Invalid value for `external_group_identifiers_ranges`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._external_group_identifiers_ranges = external_group_identifiers_ranges

    @property
    def served_fqdn_list(self):
        """Gets the served_fqdn_list of this NrfInfoServedNefInfoValue.


        :return: The served_fqdn_list of this NrfInfoServedNefInfoValue.
        :rtype: List[str]
        """
        return self._served_fqdn_list

    @served_fqdn_list.setter
    def served_fqdn_list(self, served_fqdn_list):
        """Sets the served_fqdn_list of this NrfInfoServedNefInfoValue.


        :param served_fqdn_list: The served_fqdn_list of this NrfInfoServedNefInfoValue.
        :type served_fqdn_list: List[str]
        """
        if served_fqdn_list is not None and len(served_fqdn_list) < 1:
            raise ValueError("Invalid value for `served_fqdn_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_fqdn_list = served_fqdn_list

    @property
    def tai_list(self):
        """Gets the tai_list of this NrfInfoServedNefInfoValue.


        :return: The tai_list of this NrfInfoServedNefInfoValue.
        :rtype: List[Tai]
        """
        return self._tai_list

    @tai_list.setter
    def tai_list(self, tai_list):
        """Sets the tai_list of this NrfInfoServedNefInfoValue.


        :param tai_list: The tai_list of this NrfInfoServedNefInfoValue.
        :type tai_list: List[Tai]
        """
        if tai_list is not None and len(tai_list) < 1:
            raise ValueError("Invalid value for `tai_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._tai_list = tai_list

    @property
    def tai_range_list(self):
        """Gets the tai_range_list of this NrfInfoServedNefInfoValue.


        :return: The tai_range_list of this NrfInfoServedNefInfoValue.
        :rtype: List[TaiRange]
        """
        return self._tai_range_list

    @tai_range_list.setter
    def tai_range_list(self, tai_range_list):
        """Sets the tai_range_list of this NrfInfoServedNefInfoValue.


        :param tai_range_list: The tai_range_list of this NrfInfoServedNefInfoValue.
        :type tai_range_list: List[TaiRange]
        """
        if tai_range_list is not None and len(tai_range_list) < 1:
            raise ValueError("Invalid value for `tai_range_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._tai_range_list = tai_range_list

    @property
    def dnai_list(self):
        """Gets the dnai_list of this NrfInfoServedNefInfoValue.


        :return: The dnai_list of this NrfInfoServedNefInfoValue.
        :rtype: List[str]
        """
        return self._dnai_list

    @dnai_list.setter
    def dnai_list(self, dnai_list):
        """Sets the dnai_list of this NrfInfoServedNefInfoValue.


        :param dnai_list: The dnai_list of this NrfInfoServedNefInfoValue.
        :type dnai_list: List[str]
        """
        if dnai_list is not None and len(dnai_list) < 1:
            raise ValueError("Invalid value for `dnai_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._dnai_list = dnai_list

    @property
    def un_trust_af_info_list(self):
        """Gets the un_trust_af_info_list of this NrfInfoServedNefInfoValue.


        :return: The un_trust_af_info_list of this NrfInfoServedNefInfoValue.
        :rtype: List[UnTrustAfInfo]
        """
        return self._un_trust_af_info_list

    @un_trust_af_info_list.setter
    def un_trust_af_info_list(self, un_trust_af_info_list):
        """Sets the un_trust_af_info_list of this NrfInfoServedNefInfoValue.


        :param un_trust_af_info_list: The un_trust_af_info_list of this NrfInfoServedNefInfoValue.
        :type un_trust_af_info_list: List[UnTrustAfInfo]
        """
        if un_trust_af_info_list is not None and len(un_trust_af_info_list) < 1:
            raise ValueError("Invalid value for `un_trust_af_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._un_trust_af_info_list = un_trust_af_info_list

    @property
    def uas_nf_functionality_ind(self):
        """Gets the uas_nf_functionality_ind of this NrfInfoServedNefInfoValue.


        :return: The uas_nf_functionality_ind of this NrfInfoServedNefInfoValue.
        :rtype: bool
        """
        return self._uas_nf_functionality_ind

    @uas_nf_functionality_ind.setter
    def uas_nf_functionality_ind(self, uas_nf_functionality_ind):
        """Sets the uas_nf_functionality_ind of this NrfInfoServedNefInfoValue.


        :param uas_nf_functionality_ind: The uas_nf_functionality_ind of this NrfInfoServedNefInfoValue.
        :type uas_nf_functionality_ind: bool
        """

        self._uas_nf_functionality_ind = uas_nf_functionality_ind
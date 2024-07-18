# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.access_type import AccessType
from openapi_server.models.ip_addr import IpAddr
from openapi_server.models.smf_info import SmfInfo
from openapi_server.models.snssai_smf_info_item import SnssaiSmfInfoItem
from openapi_server.models.tai import Tai
from openapi_server.models.tai_range import TaiRange
import re
from openapi_server import util

from openapi_server.models.access_type import AccessType  # noqa: E501
from openapi_server.models.ip_addr import IpAddr  # noqa: E501
from openapi_server.models.smf_info import SmfInfo  # noqa: E501
from openapi_server.models.snssai_smf_info_item import SnssaiSmfInfoItem  # noqa: E501
from openapi_server.models.tai import Tai  # noqa: E501
from openapi_server.models.tai_range import TaiRange  # noqa: E501
import re  # noqa: E501

class NrfInfoServedSmfInfoValue(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, s_nssai_smf_info_list=None, tai_list=None, tai_range_list=None, pgw_fqdn=None, pgw_ip_addr_list=None, access_type=None, priority=None, vsmf_support_ind=None, pgw_fqdn_list=None, smf_onboarding_capability=False, ismf_support_ind=None, smf_uprp_capability=False):  # noqa: E501
        """NrfInfoServedSmfInfoValue - a model defined in OpenAPI

        :param s_nssai_smf_info_list: The s_nssai_smf_info_list of this NrfInfoServedSmfInfoValue.  # noqa: E501
        :type s_nssai_smf_info_list: List[SnssaiSmfInfoItem]
        :param tai_list: The tai_list of this NrfInfoServedSmfInfoValue.  # noqa: E501
        :type tai_list: List[Tai]
        :param tai_range_list: The tai_range_list of this NrfInfoServedSmfInfoValue.  # noqa: E501
        :type tai_range_list: List[TaiRange]
        :param pgw_fqdn: The pgw_fqdn of this NrfInfoServedSmfInfoValue.  # noqa: E501
        :type pgw_fqdn: str
        :param pgw_ip_addr_list: The pgw_ip_addr_list of this NrfInfoServedSmfInfoValue.  # noqa: E501
        :type pgw_ip_addr_list: List[IpAddr]
        :param access_type: The access_type of this NrfInfoServedSmfInfoValue.  # noqa: E501
        :type access_type: List[AccessType]
        :param priority: The priority of this NrfInfoServedSmfInfoValue.  # noqa: E501
        :type priority: int
        :param vsmf_support_ind: The vsmf_support_ind of this NrfInfoServedSmfInfoValue.  # noqa: E501
        :type vsmf_support_ind: bool
        :param pgw_fqdn_list: The pgw_fqdn_list of this NrfInfoServedSmfInfoValue.  # noqa: E501
        :type pgw_fqdn_list: List[str]
        :param smf_onboarding_capability: The smf_onboarding_capability of this NrfInfoServedSmfInfoValue.  # noqa: E501
        :type smf_onboarding_capability: bool
        :param ismf_support_ind: The ismf_support_ind of this NrfInfoServedSmfInfoValue.  # noqa: E501
        :type ismf_support_ind: bool
        :param smf_uprp_capability: The smf_uprp_capability of this NrfInfoServedSmfInfoValue.  # noqa: E501
        :type smf_uprp_capability: bool
        """
        self.openapi_types = {
            's_nssai_smf_info_list': List[SnssaiSmfInfoItem],
            'tai_list': List[Tai],
            'tai_range_list': List[TaiRange],
            'pgw_fqdn': str,
            'pgw_ip_addr_list': List[IpAddr],
            'access_type': List[AccessType],
            'priority': int,
            'vsmf_support_ind': bool,
            'pgw_fqdn_list': List[str],
            'smf_onboarding_capability': bool,
            'ismf_support_ind': bool,
            'smf_uprp_capability': bool
        }

        self.attribute_map = {
            's_nssai_smf_info_list': 'sNssaiSmfInfoList',
            'tai_list': 'taiList',
            'tai_range_list': 'taiRangeList',
            'pgw_fqdn': 'pgwFqdn',
            'pgw_ip_addr_list': 'pgwIpAddrList',
            'access_type': 'accessType',
            'priority': 'priority',
            'vsmf_support_ind': 'vsmfSupportInd',
            'pgw_fqdn_list': 'pgwFqdnList',
            'smf_onboarding_capability': 'smfOnboardingCapability',
            'ismf_support_ind': 'ismfSupportInd',
            'smf_uprp_capability': 'smfUPRPCapability'
        }

        self._s_nssai_smf_info_list = s_nssai_smf_info_list
        self._tai_list = tai_list
        self._tai_range_list = tai_range_list
        self._pgw_fqdn = pgw_fqdn
        self._pgw_ip_addr_list = pgw_ip_addr_list
        self._access_type = access_type
        self._priority = priority
        self._vsmf_support_ind = vsmf_support_ind
        self._pgw_fqdn_list = pgw_fqdn_list
        self._smf_onboarding_capability = smf_onboarding_capability
        self._ismf_support_ind = ismf_support_ind
        self._smf_uprp_capability = smf_uprp_capability

    @classmethod
    def from_dict(cls, dikt) -> 'NrfInfoServedSmfInfoValue':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NrfInfo_servedSmfInfo_value of this NrfInfoServedSmfInfoValue.  # noqa: E501
        :rtype: NrfInfoServedSmfInfoValue
        """
        return util.deserialize_model(dikt, cls)

    @property
    def s_nssai_smf_info_list(self):
        """Gets the s_nssai_smf_info_list of this NrfInfoServedSmfInfoValue.


        :return: The s_nssai_smf_info_list of this NrfInfoServedSmfInfoValue.
        :rtype: List[SnssaiSmfInfoItem]
        """
        return self._s_nssai_smf_info_list

    @s_nssai_smf_info_list.setter
    def s_nssai_smf_info_list(self, s_nssai_smf_info_list):
        """Sets the s_nssai_smf_info_list of this NrfInfoServedSmfInfoValue.


        :param s_nssai_smf_info_list: The s_nssai_smf_info_list of this NrfInfoServedSmfInfoValue.
        :type s_nssai_smf_info_list: List[SnssaiSmfInfoItem]
        """
        if s_nssai_smf_info_list is None:
            raise ValueError("Invalid value for `s_nssai_smf_info_list`, must not be `None`")  # noqa: E501
        if s_nssai_smf_info_list is not None and len(s_nssai_smf_info_list) < 1:
            raise ValueError("Invalid value for `s_nssai_smf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._s_nssai_smf_info_list = s_nssai_smf_info_list

    @property
    def tai_list(self):
        """Gets the tai_list of this NrfInfoServedSmfInfoValue.


        :return: The tai_list of this NrfInfoServedSmfInfoValue.
        :rtype: List[Tai]
        """
        return self._tai_list

    @tai_list.setter
    def tai_list(self, tai_list):
        """Sets the tai_list of this NrfInfoServedSmfInfoValue.


        :param tai_list: The tai_list of this NrfInfoServedSmfInfoValue.
        :type tai_list: List[Tai]
        """
        if tai_list is not None and len(tai_list) < 1:
            raise ValueError("Invalid value for `tai_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._tai_list = tai_list

    @property
    def tai_range_list(self):
        """Gets the tai_range_list of this NrfInfoServedSmfInfoValue.


        :return: The tai_range_list of this NrfInfoServedSmfInfoValue.
        :rtype: List[TaiRange]
        """
        return self._tai_range_list

    @tai_range_list.setter
    def tai_range_list(self, tai_range_list):
        """Sets the tai_range_list of this NrfInfoServedSmfInfoValue.


        :param tai_range_list: The tai_range_list of this NrfInfoServedSmfInfoValue.
        :type tai_range_list: List[TaiRange]
        """
        if tai_range_list is not None and len(tai_range_list) < 1:
            raise ValueError("Invalid value for `tai_range_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._tai_range_list = tai_range_list

    @property
    def pgw_fqdn(self):
        """Gets the pgw_fqdn of this NrfInfoServedSmfInfoValue.

        Fully Qualified Domain Name  # noqa: E501

        :return: The pgw_fqdn of this NrfInfoServedSmfInfoValue.
        :rtype: str
        """
        return self._pgw_fqdn

    @pgw_fqdn.setter
    def pgw_fqdn(self, pgw_fqdn):
        """Sets the pgw_fqdn of this NrfInfoServedSmfInfoValue.

        Fully Qualified Domain Name  # noqa: E501

        :param pgw_fqdn: The pgw_fqdn of this NrfInfoServedSmfInfoValue.
        :type pgw_fqdn: str
        """
        if pgw_fqdn is not None and len(pgw_fqdn) > 253:
            raise ValueError("Invalid value for `pgw_fqdn`, length must be less than or equal to `253`")  # noqa: E501
        if pgw_fqdn is not None and len(pgw_fqdn) < 4:
            raise ValueError("Invalid value for `pgw_fqdn`, length must be greater than or equal to `4`")  # noqa: E501
        if pgw_fqdn is not None and not re.search(r'^([0-9A-Za-z]([-0-9A-Za-z]{0,61}[0-9A-Za-z])?\.)+[A-Za-z]{2,63}\.?$', pgw_fqdn):  # noqa: E501
            raise ValueError("Invalid value for `pgw_fqdn`, must be a follow pattern or equal to `/^([0-9A-Za-z]([-0-9A-Za-z]{0,61}[0-9A-Za-z])?\.)+[A-Za-z]{2,63}\.?$/`")  # noqa: E501

        self._pgw_fqdn = pgw_fqdn

    @property
    def pgw_ip_addr_list(self):
        """Gets the pgw_ip_addr_list of this NrfInfoServedSmfInfoValue.


        :return: The pgw_ip_addr_list of this NrfInfoServedSmfInfoValue.
        :rtype: List[IpAddr]
        """
        return self._pgw_ip_addr_list

    @pgw_ip_addr_list.setter
    def pgw_ip_addr_list(self, pgw_ip_addr_list):
        """Sets the pgw_ip_addr_list of this NrfInfoServedSmfInfoValue.


        :param pgw_ip_addr_list: The pgw_ip_addr_list of this NrfInfoServedSmfInfoValue.
        :type pgw_ip_addr_list: List[IpAddr]
        """
        if pgw_ip_addr_list is not None and len(pgw_ip_addr_list) < 1:
            raise ValueError("Invalid value for `pgw_ip_addr_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._pgw_ip_addr_list = pgw_ip_addr_list

    @property
    def access_type(self):
        """Gets the access_type of this NrfInfoServedSmfInfoValue.


        :return: The access_type of this NrfInfoServedSmfInfoValue.
        :rtype: List[AccessType]
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """Sets the access_type of this NrfInfoServedSmfInfoValue.


        :param access_type: The access_type of this NrfInfoServedSmfInfoValue.
        :type access_type: List[AccessType]
        """
        if access_type is not None and len(access_type) < 1:
            raise ValueError("Invalid value for `access_type`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._access_type = access_type

    @property
    def priority(self):
        """Gets the priority of this NrfInfoServedSmfInfoValue.


        :return: The priority of this NrfInfoServedSmfInfoValue.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this NrfInfoServedSmfInfoValue.


        :param priority: The priority of this NrfInfoServedSmfInfoValue.
        :type priority: int
        """
        if priority is not None and priority > 65535:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value less than or equal to `65535`")  # noqa: E501
        if priority is not None and priority < 0:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value greater than or equal to `0`")  # noqa: E501

        self._priority = priority

    @property
    def vsmf_support_ind(self):
        """Gets the vsmf_support_ind of this NrfInfoServedSmfInfoValue.


        :return: The vsmf_support_ind of this NrfInfoServedSmfInfoValue.
        :rtype: bool
        """
        return self._vsmf_support_ind

    @vsmf_support_ind.setter
    def vsmf_support_ind(self, vsmf_support_ind):
        """Sets the vsmf_support_ind of this NrfInfoServedSmfInfoValue.


        :param vsmf_support_ind: The vsmf_support_ind of this NrfInfoServedSmfInfoValue.
        :type vsmf_support_ind: bool
        """

        self._vsmf_support_ind = vsmf_support_ind

    @property
    def pgw_fqdn_list(self):
        """Gets the pgw_fqdn_list of this NrfInfoServedSmfInfoValue.


        :return: The pgw_fqdn_list of this NrfInfoServedSmfInfoValue.
        :rtype: List[str]
        """
        return self._pgw_fqdn_list

    @pgw_fqdn_list.setter
    def pgw_fqdn_list(self, pgw_fqdn_list):
        """Sets the pgw_fqdn_list of this NrfInfoServedSmfInfoValue.


        :param pgw_fqdn_list: The pgw_fqdn_list of this NrfInfoServedSmfInfoValue.
        :type pgw_fqdn_list: List[str]
        """
        if pgw_fqdn_list is not None and len(pgw_fqdn_list) < 1:
            raise ValueError("Invalid value for `pgw_fqdn_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._pgw_fqdn_list = pgw_fqdn_list

    @property
    def smf_onboarding_capability(self):
        """Gets the smf_onboarding_capability of this NrfInfoServedSmfInfoValue.


        :return: The smf_onboarding_capability of this NrfInfoServedSmfInfoValue.
        :rtype: bool
        """
        return self._smf_onboarding_capability

    @smf_onboarding_capability.setter
    def smf_onboarding_capability(self, smf_onboarding_capability):
        """Sets the smf_onboarding_capability of this NrfInfoServedSmfInfoValue.


        :param smf_onboarding_capability: The smf_onboarding_capability of this NrfInfoServedSmfInfoValue.
        :type smf_onboarding_capability: bool
        """

        self._smf_onboarding_capability = smf_onboarding_capability

    @property
    def ismf_support_ind(self):
        """Gets the ismf_support_ind of this NrfInfoServedSmfInfoValue.


        :return: The ismf_support_ind of this NrfInfoServedSmfInfoValue.
        :rtype: bool
        """
        return self._ismf_support_ind

    @ismf_support_ind.setter
    def ismf_support_ind(self, ismf_support_ind):
        """Sets the ismf_support_ind of this NrfInfoServedSmfInfoValue.


        :param ismf_support_ind: The ismf_support_ind of this NrfInfoServedSmfInfoValue.
        :type ismf_support_ind: bool
        """

        self._ismf_support_ind = ismf_support_ind

    @property
    def smf_uprp_capability(self):
        """Gets the smf_uprp_capability of this NrfInfoServedSmfInfoValue.


        :return: The smf_uprp_capability of this NrfInfoServedSmfInfoValue.
        :rtype: bool
        """
        return self._smf_uprp_capability

    @smf_uprp_capability.setter
    def smf_uprp_capability(self, smf_uprp_capability):
        """Sets the smf_uprp_capability of this NrfInfoServedSmfInfoValue.


        :param smf_uprp_capability: The smf_uprp_capability of this NrfInfoServedSmfInfoValue.
        :type smf_uprp_capability: bool
        """

        self._smf_uprp_capability = smf_uprp_capability

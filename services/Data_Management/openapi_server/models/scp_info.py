# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ip_reachability import IpReachability
from openapi_server.models.ipv4_address_range import Ipv4AddressRange
from openapi_server.models.ipv6_prefix import Ipv6Prefix
from openapi_server.models.ipv6_prefix_range import Ipv6PrefixRange
from openapi_server.models.plmn_id import PlmnId
from openapi_server.models.plmn_id_nid import PlmnIdNid
from openapi_server.models.scp_capability import ScpCapability
from openapi_server.models.scp_domain_info import ScpDomainInfo
from openapi_server import util

from openapi_server.models.ip_reachability import IpReachability  # noqa: E501
from openapi_server.models.ipv4_address_range import Ipv4AddressRange  # noqa: E501
from openapi_server.models.ipv6_prefix import Ipv6Prefix  # noqa: E501
from openapi_server.models.ipv6_prefix_range import Ipv6PrefixRange  # noqa: E501
from openapi_server.models.plmn_id import PlmnId  # noqa: E501
from openapi_server.models.plmn_id_nid import PlmnIdNid  # noqa: E501
from openapi_server.models.scp_capability import ScpCapability  # noqa: E501
from openapi_server.models.scp_domain_info import ScpDomainInfo  # noqa: E501

class ScpInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, scp_domain_info_list=None, scp_prefix=None, scp_ports=None, address_domains=None, ipv4_addresses=None, ipv6_prefixes=None, ipv4_addr_ranges=None, ipv6_prefix_ranges=None, served_nf_set_id_list=None, remote_plmn_list=None, remote_snpn_list=None, ip_reachability=None, scp_capabilities=None):  # noqa: E501
        """ScpInfo - a model defined in OpenAPI

        :param scp_domain_info_list: The scp_domain_info_list of this ScpInfo.  # noqa: E501
        :type scp_domain_info_list: Dict[str, ScpDomainInfo]
        :param scp_prefix: The scp_prefix of this ScpInfo.  # noqa: E501
        :type scp_prefix: str
        :param scp_ports: The scp_ports of this ScpInfo.  # noqa: E501
        :type scp_ports: Dict[str, int]
        :param address_domains: The address_domains of this ScpInfo.  # noqa: E501
        :type address_domains: List[str]
        :param ipv4_addresses: The ipv4_addresses of this ScpInfo.  # noqa: E501
        :type ipv4_addresses: List[str]
        :param ipv6_prefixes: The ipv6_prefixes of this ScpInfo.  # noqa: E501
        :type ipv6_prefixes: List[Ipv6Prefix]
        :param ipv4_addr_ranges: The ipv4_addr_ranges of this ScpInfo.  # noqa: E501
        :type ipv4_addr_ranges: List[Ipv4AddressRange]
        :param ipv6_prefix_ranges: The ipv6_prefix_ranges of this ScpInfo.  # noqa: E501
        :type ipv6_prefix_ranges: List[Ipv6PrefixRange]
        :param served_nf_set_id_list: The served_nf_set_id_list of this ScpInfo.  # noqa: E501
        :type served_nf_set_id_list: List[str]
        :param remote_plmn_list: The remote_plmn_list of this ScpInfo.  # noqa: E501
        :type remote_plmn_list: List[PlmnId]
        :param remote_snpn_list: The remote_snpn_list of this ScpInfo.  # noqa: E501
        :type remote_snpn_list: List[PlmnIdNid]
        :param ip_reachability: The ip_reachability of this ScpInfo.  # noqa: E501
        :type ip_reachability: IpReachability
        :param scp_capabilities: The scp_capabilities of this ScpInfo.  # noqa: E501
        :type scp_capabilities: List[ScpCapability]
        """
        self.openapi_types = {
            'scp_domain_info_list': Dict[str, ScpDomainInfo],
            'scp_prefix': str,
            'scp_ports': Dict[str, int],
            'address_domains': List[str],
            'ipv4_addresses': List[str],
            'ipv6_prefixes': List[Ipv6Prefix],
            'ipv4_addr_ranges': List[Ipv4AddressRange],
            'ipv6_prefix_ranges': List[Ipv6PrefixRange],
            'served_nf_set_id_list': List[str],
            'remote_plmn_list': List[PlmnId],
            'remote_snpn_list': List[PlmnIdNid],
            'ip_reachability': IpReachability,
            'scp_capabilities': List[ScpCapability]
        }

        self.attribute_map = {
            'scp_domain_info_list': 'scpDomainInfoList',
            'scp_prefix': 'scpPrefix',
            'scp_ports': 'scpPorts',
            'address_domains': 'addressDomains',
            'ipv4_addresses': 'ipv4Addresses',
            'ipv6_prefixes': 'ipv6Prefixes',
            'ipv4_addr_ranges': 'ipv4AddrRanges',
            'ipv6_prefix_ranges': 'ipv6PrefixRanges',
            'served_nf_set_id_list': 'servedNfSetIdList',
            'remote_plmn_list': 'remotePlmnList',
            'remote_snpn_list': 'remoteSnpnList',
            'ip_reachability': 'ipReachability',
            'scp_capabilities': 'scpCapabilities'
        }

        self._scp_domain_info_list = scp_domain_info_list
        self._scp_prefix = scp_prefix
        self._scp_ports = scp_ports
        self._address_domains = address_domains
        self._ipv4_addresses = ipv4_addresses
        self._ipv6_prefixes = ipv6_prefixes
        self._ipv4_addr_ranges = ipv4_addr_ranges
        self._ipv6_prefix_ranges = ipv6_prefix_ranges
        self._served_nf_set_id_list = served_nf_set_id_list
        self._remote_plmn_list = remote_plmn_list
        self._remote_snpn_list = remote_snpn_list
        self._ip_reachability = ip_reachability
        self._scp_capabilities = scp_capabilities

    @classmethod
    def from_dict(cls, dikt) -> 'ScpInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ScpInfo of this ScpInfo.  # noqa: E501
        :rtype: ScpInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def scp_domain_info_list(self):
        """Gets the scp_domain_info_list of this ScpInfo.

        A map (list of key-value pairs) where the key of the map shall be the string identifying an SCP domain   # noqa: E501

        :return: The scp_domain_info_list of this ScpInfo.
        :rtype: Dict[str, ScpDomainInfo]
        """
        return self._scp_domain_info_list

    @scp_domain_info_list.setter
    def scp_domain_info_list(self, scp_domain_info_list):
        """Sets the scp_domain_info_list of this ScpInfo.

        A map (list of key-value pairs) where the key of the map shall be the string identifying an SCP domain   # noqa: E501

        :param scp_domain_info_list: The scp_domain_info_list of this ScpInfo.
        :type scp_domain_info_list: Dict[str, ScpDomainInfo]
        """
        if scp_domain_info_list is not None and len(scp_domain_info_list) < 1:
            raise ValueError("Invalid value for `scp_domain_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._scp_domain_info_list = scp_domain_info_list

    @property
    def scp_prefix(self):
        """Gets the scp_prefix of this ScpInfo.


        :return: The scp_prefix of this ScpInfo.
        :rtype: str
        """
        return self._scp_prefix

    @scp_prefix.setter
    def scp_prefix(self, scp_prefix):
        """Sets the scp_prefix of this ScpInfo.


        :param scp_prefix: The scp_prefix of this ScpInfo.
        :type scp_prefix: str
        """

        self._scp_prefix = scp_prefix

    @property
    def scp_ports(self):
        """Gets the scp_ports of this ScpInfo.

        Port numbers for HTTP and HTTPS. The key of the map shall be \"http\" or \"https\".   # noqa: E501

        :return: The scp_ports of this ScpInfo.
        :rtype: Dict[str, int]
        """
        return self._scp_ports

    @scp_ports.setter
    def scp_ports(self, scp_ports):
        """Sets the scp_ports of this ScpInfo.

        Port numbers for HTTP and HTTPS. The key of the map shall be \"http\" or \"https\".   # noqa: E501

        :param scp_ports: The scp_ports of this ScpInfo.
        :type scp_ports: Dict[str, int]
        """
        if scp_ports is not None and len(scp_ports) < 1:
            raise ValueError("Invalid value for `scp_ports`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._scp_ports = scp_ports

    @property
    def address_domains(self):
        """Gets the address_domains of this ScpInfo.


        :return: The address_domains of this ScpInfo.
        :rtype: List[str]
        """
        return self._address_domains

    @address_domains.setter
    def address_domains(self, address_domains):
        """Sets the address_domains of this ScpInfo.


        :param address_domains: The address_domains of this ScpInfo.
        :type address_domains: List[str]
        """
        if address_domains is not None and len(address_domains) < 1:
            raise ValueError("Invalid value for `address_domains`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._address_domains = address_domains

    @property
    def ipv4_addresses(self):
        """Gets the ipv4_addresses of this ScpInfo.


        :return: The ipv4_addresses of this ScpInfo.
        :rtype: List[str]
        """
        return self._ipv4_addresses

    @ipv4_addresses.setter
    def ipv4_addresses(self, ipv4_addresses):
        """Sets the ipv4_addresses of this ScpInfo.


        :param ipv4_addresses: The ipv4_addresses of this ScpInfo.
        :type ipv4_addresses: List[str]
        """
        if ipv4_addresses is not None and len(ipv4_addresses) < 1:
            raise ValueError("Invalid value for `ipv4_addresses`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ipv4_addresses = ipv4_addresses

    @property
    def ipv6_prefixes(self):
        """Gets the ipv6_prefixes of this ScpInfo.


        :return: The ipv6_prefixes of this ScpInfo.
        :rtype: List[Ipv6Prefix]
        """
        return self._ipv6_prefixes

    @ipv6_prefixes.setter
    def ipv6_prefixes(self, ipv6_prefixes):
        """Sets the ipv6_prefixes of this ScpInfo.


        :param ipv6_prefixes: The ipv6_prefixes of this ScpInfo.
        :type ipv6_prefixes: List[Ipv6Prefix]
        """
        if ipv6_prefixes is not None and len(ipv6_prefixes) < 1:
            raise ValueError("Invalid value for `ipv6_prefixes`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ipv6_prefixes = ipv6_prefixes

    @property
    def ipv4_addr_ranges(self):
        """Gets the ipv4_addr_ranges of this ScpInfo.


        :return: The ipv4_addr_ranges of this ScpInfo.
        :rtype: List[Ipv4AddressRange]
        """
        return self._ipv4_addr_ranges

    @ipv4_addr_ranges.setter
    def ipv4_addr_ranges(self, ipv4_addr_ranges):
        """Sets the ipv4_addr_ranges of this ScpInfo.


        :param ipv4_addr_ranges: The ipv4_addr_ranges of this ScpInfo.
        :type ipv4_addr_ranges: List[Ipv4AddressRange]
        """
        if ipv4_addr_ranges is not None and len(ipv4_addr_ranges) < 1:
            raise ValueError("Invalid value for `ipv4_addr_ranges`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ipv4_addr_ranges = ipv4_addr_ranges

    @property
    def ipv6_prefix_ranges(self):
        """Gets the ipv6_prefix_ranges of this ScpInfo.


        :return: The ipv6_prefix_ranges of this ScpInfo.
        :rtype: List[Ipv6PrefixRange]
        """
        return self._ipv6_prefix_ranges

    @ipv6_prefix_ranges.setter
    def ipv6_prefix_ranges(self, ipv6_prefix_ranges):
        """Sets the ipv6_prefix_ranges of this ScpInfo.


        :param ipv6_prefix_ranges: The ipv6_prefix_ranges of this ScpInfo.
        :type ipv6_prefix_ranges: List[Ipv6PrefixRange]
        """
        if ipv6_prefix_ranges is not None and len(ipv6_prefix_ranges) < 1:
            raise ValueError("Invalid value for `ipv6_prefix_ranges`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ipv6_prefix_ranges = ipv6_prefix_ranges

    @property
    def served_nf_set_id_list(self):
        """Gets the served_nf_set_id_list of this ScpInfo.


        :return: The served_nf_set_id_list of this ScpInfo.
        :rtype: List[str]
        """
        return self._served_nf_set_id_list

    @served_nf_set_id_list.setter
    def served_nf_set_id_list(self, served_nf_set_id_list):
        """Sets the served_nf_set_id_list of this ScpInfo.


        :param served_nf_set_id_list: The served_nf_set_id_list of this ScpInfo.
        :type served_nf_set_id_list: List[str]
        """
        if served_nf_set_id_list is not None and len(served_nf_set_id_list) < 1:
            raise ValueError("Invalid value for `served_nf_set_id_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_nf_set_id_list = served_nf_set_id_list

    @property
    def remote_plmn_list(self):
        """Gets the remote_plmn_list of this ScpInfo.


        :return: The remote_plmn_list of this ScpInfo.
        :rtype: List[PlmnId]
        """
        return self._remote_plmn_list

    @remote_plmn_list.setter
    def remote_plmn_list(self, remote_plmn_list):
        """Sets the remote_plmn_list of this ScpInfo.


        :param remote_plmn_list: The remote_plmn_list of this ScpInfo.
        :type remote_plmn_list: List[PlmnId]
        """
        if remote_plmn_list is not None and len(remote_plmn_list) < 1:
            raise ValueError("Invalid value for `remote_plmn_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._remote_plmn_list = remote_plmn_list

    @property
    def remote_snpn_list(self):
        """Gets the remote_snpn_list of this ScpInfo.


        :return: The remote_snpn_list of this ScpInfo.
        :rtype: List[PlmnIdNid]
        """
        return self._remote_snpn_list

    @remote_snpn_list.setter
    def remote_snpn_list(self, remote_snpn_list):
        """Sets the remote_snpn_list of this ScpInfo.


        :param remote_snpn_list: The remote_snpn_list of this ScpInfo.
        :type remote_snpn_list: List[PlmnIdNid]
        """
        if remote_snpn_list is not None and len(remote_snpn_list) < 1:
            raise ValueError("Invalid value for `remote_snpn_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._remote_snpn_list = remote_snpn_list

    @property
    def ip_reachability(self):
        """Gets the ip_reachability of this ScpInfo.


        :return: The ip_reachability of this ScpInfo.
        :rtype: IpReachability
        """
        return self._ip_reachability

    @ip_reachability.setter
    def ip_reachability(self, ip_reachability):
        """Sets the ip_reachability of this ScpInfo.


        :param ip_reachability: The ip_reachability of this ScpInfo.
        :type ip_reachability: IpReachability
        """

        self._ip_reachability = ip_reachability

    @property
    def scp_capabilities(self):
        """Gets the scp_capabilities of this ScpInfo.


        :return: The scp_capabilities of this ScpInfo.
        :rtype: List[ScpCapability]
        """
        return self._scp_capabilities

    @scp_capabilities.setter
    def scp_capabilities(self, scp_capabilities):
        """Sets the scp_capabilities of this ScpInfo.


        :param scp_capabilities: The scp_capabilities of this ScpInfo.
        :type scp_capabilities: List[ScpCapability]
        """

        self._scp_capabilities = scp_capabilities

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.identity_range import IdentityRange
from openapi_server.models.ipv4_address_range import Ipv4AddressRange
from openapi_server.models.ipv6_prefix_range import Ipv6PrefixRange
from openapi_server.models.supi_range import SupiRange
import re
from openapi_server import util

from openapi_server.models.identity_range import IdentityRange  # noqa: E501
from openapi_server.models.ipv4_address_range import Ipv4AddressRange  # noqa: E501
from openapi_server.models.ipv6_prefix_range import Ipv6PrefixRange  # noqa: E501
from openapi_server.models.supi_range import SupiRange  # noqa: E501
import re  # noqa: E501

class BsfInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, dnn_list=None, ip_domain_list=None, ipv4_address_ranges=None, ipv6_prefix_ranges=None, rx_diam_host=None, rx_diam_realm=None, group_id=None, supi_ranges=None, gpsi_ranges=None):  # noqa: E501
        """BsfInfo - a model defined in OpenAPI

        :param dnn_list: The dnn_list of this BsfInfo.  # noqa: E501
        :type dnn_list: List[str]
        :param ip_domain_list: The ip_domain_list of this BsfInfo.  # noqa: E501
        :type ip_domain_list: List[str]
        :param ipv4_address_ranges: The ipv4_address_ranges of this BsfInfo.  # noqa: E501
        :type ipv4_address_ranges: List[Ipv4AddressRange]
        :param ipv6_prefix_ranges: The ipv6_prefix_ranges of this BsfInfo.  # noqa: E501
        :type ipv6_prefix_ranges: List[Ipv6PrefixRange]
        :param rx_diam_host: The rx_diam_host of this BsfInfo.  # noqa: E501
        :type rx_diam_host: str
        :param rx_diam_realm: The rx_diam_realm of this BsfInfo.  # noqa: E501
        :type rx_diam_realm: str
        :param group_id: The group_id of this BsfInfo.  # noqa: E501
        :type group_id: str
        :param supi_ranges: The supi_ranges of this BsfInfo.  # noqa: E501
        :type supi_ranges: List[SupiRange]
        :param gpsi_ranges: The gpsi_ranges of this BsfInfo.  # noqa: E501
        :type gpsi_ranges: List[IdentityRange]
        """
        self.openapi_types = {
            'dnn_list': List[str],
            'ip_domain_list': List[str],
            'ipv4_address_ranges': List[Ipv4AddressRange],
            'ipv6_prefix_ranges': List[Ipv6PrefixRange],
            'rx_diam_host': str,
            'rx_diam_realm': str,
            'group_id': str,
            'supi_ranges': List[SupiRange],
            'gpsi_ranges': List[IdentityRange]
        }

        self.attribute_map = {
            'dnn_list': 'dnnList',
            'ip_domain_list': 'ipDomainList',
            'ipv4_address_ranges': 'ipv4AddressRanges',
            'ipv6_prefix_ranges': 'ipv6PrefixRanges',
            'rx_diam_host': 'rxDiamHost',
            'rx_diam_realm': 'rxDiamRealm',
            'group_id': 'groupId',
            'supi_ranges': 'supiRanges',
            'gpsi_ranges': 'gpsiRanges'
        }

        self._dnn_list = dnn_list
        self._ip_domain_list = ip_domain_list
        self._ipv4_address_ranges = ipv4_address_ranges
        self._ipv6_prefix_ranges = ipv6_prefix_ranges
        self._rx_diam_host = rx_diam_host
        self._rx_diam_realm = rx_diam_realm
        self._group_id = group_id
        self._supi_ranges = supi_ranges
        self._gpsi_ranges = gpsi_ranges

    @classmethod
    def from_dict(cls, dikt) -> 'BsfInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BsfInfo of this BsfInfo.  # noqa: E501
        :rtype: BsfInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dnn_list(self):
        """Gets the dnn_list of this BsfInfo.


        :return: The dnn_list of this BsfInfo.
        :rtype: List[str]
        """
        return self._dnn_list

    @dnn_list.setter
    def dnn_list(self, dnn_list):
        """Sets the dnn_list of this BsfInfo.


        :param dnn_list: The dnn_list of this BsfInfo.
        :type dnn_list: List[str]
        """
        if dnn_list is not None and len(dnn_list) < 1:
            raise ValueError("Invalid value for `dnn_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._dnn_list = dnn_list

    @property
    def ip_domain_list(self):
        """Gets the ip_domain_list of this BsfInfo.


        :return: The ip_domain_list of this BsfInfo.
        :rtype: List[str]
        """
        return self._ip_domain_list

    @ip_domain_list.setter
    def ip_domain_list(self, ip_domain_list):
        """Sets the ip_domain_list of this BsfInfo.


        :param ip_domain_list: The ip_domain_list of this BsfInfo.
        :type ip_domain_list: List[str]
        """
        if ip_domain_list is not None and len(ip_domain_list) < 1:
            raise ValueError("Invalid value for `ip_domain_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ip_domain_list = ip_domain_list

    @property
    def ipv4_address_ranges(self):
        """Gets the ipv4_address_ranges of this BsfInfo.


        :return: The ipv4_address_ranges of this BsfInfo.
        :rtype: List[Ipv4AddressRange]
        """
        return self._ipv4_address_ranges

    @ipv4_address_ranges.setter
    def ipv4_address_ranges(self, ipv4_address_ranges):
        """Sets the ipv4_address_ranges of this BsfInfo.


        :param ipv4_address_ranges: The ipv4_address_ranges of this BsfInfo.
        :type ipv4_address_ranges: List[Ipv4AddressRange]
        """
        if ipv4_address_ranges is not None and len(ipv4_address_ranges) < 1:
            raise ValueError("Invalid value for `ipv4_address_ranges`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ipv4_address_ranges = ipv4_address_ranges

    @property
    def ipv6_prefix_ranges(self):
        """Gets the ipv6_prefix_ranges of this BsfInfo.


        :return: The ipv6_prefix_ranges of this BsfInfo.
        :rtype: List[Ipv6PrefixRange]
        """
        return self._ipv6_prefix_ranges

    @ipv6_prefix_ranges.setter
    def ipv6_prefix_ranges(self, ipv6_prefix_ranges):
        """Sets the ipv6_prefix_ranges of this BsfInfo.


        :param ipv6_prefix_ranges: The ipv6_prefix_ranges of this BsfInfo.
        :type ipv6_prefix_ranges: List[Ipv6PrefixRange]
        """
        if ipv6_prefix_ranges is not None and len(ipv6_prefix_ranges) < 1:
            raise ValueError("Invalid value for `ipv6_prefix_ranges`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ipv6_prefix_ranges = ipv6_prefix_ranges

    @property
    def rx_diam_host(self):
        """Gets the rx_diam_host of this BsfInfo.

        Fully Qualified Domain Name  # noqa: E501

        :return: The rx_diam_host of this BsfInfo.
        :rtype: str
        """
        return self._rx_diam_host

    @rx_diam_host.setter
    def rx_diam_host(self, rx_diam_host):
        """Sets the rx_diam_host of this BsfInfo.

        Fully Qualified Domain Name  # noqa: E501

        :param rx_diam_host: The rx_diam_host of this BsfInfo.
        :type rx_diam_host: str
        """
        if rx_diam_host is not None and len(rx_diam_host) > 253:
            raise ValueError("Invalid value for `rx_diam_host`, length must be less than or equal to `253`")  # noqa: E501
        if rx_diam_host is not None and len(rx_diam_host) < 4:
            raise ValueError("Invalid value for `rx_diam_host`, length must be greater than or equal to `4`")  # noqa: E501
        if rx_diam_host is not None and not re.search(r'^([0-9A-Za-z]([-0-9A-Za-z]{0,61}[0-9A-Za-z])?\.)+[A-Za-z]{2,63}\.?$', rx_diam_host):  # noqa: E501
            raise ValueError("Invalid value for `rx_diam_host`, must be a follow pattern or equal to `/^([0-9A-Za-z]([-0-9A-Za-z]{0,61}[0-9A-Za-z])?\.)+[A-Za-z]{2,63}\.?$/`")  # noqa: E501

        self._rx_diam_host = rx_diam_host

    @property
    def rx_diam_realm(self):
        """Gets the rx_diam_realm of this BsfInfo.

        Fully Qualified Domain Name  # noqa: E501

        :return: The rx_diam_realm of this BsfInfo.
        :rtype: str
        """
        return self._rx_diam_realm

    @rx_diam_realm.setter
    def rx_diam_realm(self, rx_diam_realm):
        """Sets the rx_diam_realm of this BsfInfo.

        Fully Qualified Domain Name  # noqa: E501

        :param rx_diam_realm: The rx_diam_realm of this BsfInfo.
        :type rx_diam_realm: str
        """
        if rx_diam_realm is not None and len(rx_diam_realm) > 253:
            raise ValueError("Invalid value for `rx_diam_realm`, length must be less than or equal to `253`")  # noqa: E501
        if rx_diam_realm is not None and len(rx_diam_realm) < 4:
            raise ValueError("Invalid value for `rx_diam_realm`, length must be greater than or equal to `4`")  # noqa: E501
        if rx_diam_realm is not None and not re.search(r'^([0-9A-Za-z]([-0-9A-Za-z]{0,61}[0-9A-Za-z])?\.)+[A-Za-z]{2,63}\.?$', rx_diam_realm):  # noqa: E501
            raise ValueError("Invalid value for `rx_diam_realm`, must be a follow pattern or equal to `/^([0-9A-Za-z]([-0-9A-Za-z]{0,61}[0-9A-Za-z])?\.)+[A-Za-z]{2,63}\.?$/`")  # noqa: E501

        self._rx_diam_realm = rx_diam_realm

    @property
    def group_id(self):
        """Gets the group_id of this BsfInfo.

        Identifier of a group of NFs.  # noqa: E501

        :return: The group_id of this BsfInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this BsfInfo.

        Identifier of a group of NFs.  # noqa: E501

        :param group_id: The group_id of this BsfInfo.
        :type group_id: str
        """

        self._group_id = group_id

    @property
    def supi_ranges(self):
        """Gets the supi_ranges of this BsfInfo.


        :return: The supi_ranges of this BsfInfo.
        :rtype: List[SupiRange]
        """
        return self._supi_ranges

    @supi_ranges.setter
    def supi_ranges(self, supi_ranges):
        """Sets the supi_ranges of this BsfInfo.


        :param supi_ranges: The supi_ranges of this BsfInfo.
        :type supi_ranges: List[SupiRange]
        """
        if supi_ranges is not None and len(supi_ranges) < 1:
            raise ValueError("Invalid value for `supi_ranges`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._supi_ranges = supi_ranges

    @property
    def gpsi_ranges(self):
        """Gets the gpsi_ranges of this BsfInfo.


        :return: The gpsi_ranges of this BsfInfo.
        :rtype: List[IdentityRange]
        """
        return self._gpsi_ranges

    @gpsi_ranges.setter
    def gpsi_ranges(self, gpsi_ranges):
        """Sets the gpsi_ranges of this BsfInfo.


        :param gpsi_ranges: The gpsi_ranges of this BsfInfo.
        :type gpsi_ranges: List[IdentityRange]
        """
        if gpsi_ranges is not None and len(gpsi_ranges) < 1:
            raise ValueError("Invalid value for `gpsi_ranges`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._gpsi_ranges = gpsi_ranges

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.flow_direction import FlowDirection
import re
from openapi_server import util

from openapi_server.models.flow_direction import FlowDirection  # noqa: E501
import re  # noqa: E501

class EthFlowDescription(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, dest_mac_addr=None, eth_type=None, f_desc=None, f_dir=None, source_mac_addr=None, vlan_tags=None, src_mac_addr_end=None, dest_mac_addr_end=None):  # noqa: E501
        """EthFlowDescription - a model defined in OpenAPI

        :param dest_mac_addr: The dest_mac_addr of this EthFlowDescription.  # noqa: E501
        :type dest_mac_addr: str
        :param eth_type: The eth_type of this EthFlowDescription.  # noqa: E501
        :type eth_type: str
        :param f_desc: The f_desc of this EthFlowDescription.  # noqa: E501
        :type f_desc: str
        :param f_dir: The f_dir of this EthFlowDescription.  # noqa: E501
        :type f_dir: FlowDirection
        :param source_mac_addr: The source_mac_addr of this EthFlowDescription.  # noqa: E501
        :type source_mac_addr: str
        :param vlan_tags: The vlan_tags of this EthFlowDescription.  # noqa: E501
        :type vlan_tags: List[str]
        :param src_mac_addr_end: The src_mac_addr_end of this EthFlowDescription.  # noqa: E501
        :type src_mac_addr_end: str
        :param dest_mac_addr_end: The dest_mac_addr_end of this EthFlowDescription.  # noqa: E501
        :type dest_mac_addr_end: str
        """
        self.openapi_types = {
            'dest_mac_addr': str,
            'eth_type': str,
            'f_desc': str,
            'f_dir': FlowDirection,
            'source_mac_addr': str,
            'vlan_tags': List[str],
            'src_mac_addr_end': str,
            'dest_mac_addr_end': str
        }

        self.attribute_map = {
            'dest_mac_addr': 'destMacAddr',
            'eth_type': 'ethType',
            'f_desc': 'fDesc',
            'f_dir': 'fDir',
            'source_mac_addr': 'sourceMacAddr',
            'vlan_tags': 'vlanTags',
            'src_mac_addr_end': 'srcMacAddrEnd',
            'dest_mac_addr_end': 'destMacAddrEnd'
        }

        self._dest_mac_addr = dest_mac_addr
        self._eth_type = eth_type
        self._f_desc = f_desc
        self._f_dir = f_dir
        self._source_mac_addr = source_mac_addr
        self._vlan_tags = vlan_tags
        self._src_mac_addr_end = src_mac_addr_end
        self._dest_mac_addr_end = dest_mac_addr_end

    @classmethod
    def from_dict(cls, dikt) -> 'EthFlowDescription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EthFlowDescription of this EthFlowDescription.  # noqa: E501
        :rtype: EthFlowDescription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dest_mac_addr(self):
        """Gets the dest_mac_addr of this EthFlowDescription.

        String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042.   # noqa: E501

        :return: The dest_mac_addr of this EthFlowDescription.
        :rtype: str
        """
        return self._dest_mac_addr

    @dest_mac_addr.setter
    def dest_mac_addr(self, dest_mac_addr):
        """Sets the dest_mac_addr of this EthFlowDescription.

        String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042.   # noqa: E501

        :param dest_mac_addr: The dest_mac_addr of this EthFlowDescription.
        :type dest_mac_addr: str
        """
        if dest_mac_addr is not None and not re.search(r'^([0-9a-fA-F]{2})((-[0-9a-fA-F]{2}){5})$', dest_mac_addr):  # noqa: E501
            raise ValueError("Invalid value for `dest_mac_addr`, must be a follow pattern or equal to `/^([0-9a-fA-F]{2})((-[0-9a-fA-F]{2}){5})$/`")  # noqa: E501

        self._dest_mac_addr = dest_mac_addr

    @property
    def eth_type(self):
        """Gets the eth_type of this EthFlowDescription.


        :return: The eth_type of this EthFlowDescription.
        :rtype: str
        """
        return self._eth_type

    @eth_type.setter
    def eth_type(self, eth_type):
        """Sets the eth_type of this EthFlowDescription.


        :param eth_type: The eth_type of this EthFlowDescription.
        :type eth_type: str
        """
        if eth_type is None:
            raise ValueError("Invalid value for `eth_type`, must not be `None`")  # noqa: E501

        self._eth_type = eth_type

    @property
    def f_desc(self):
        """Gets the f_desc of this EthFlowDescription.

        Defines a packet filter of an IP flow.  # noqa: E501

        :return: The f_desc of this EthFlowDescription.
        :rtype: str
        """
        return self._f_desc

    @f_desc.setter
    def f_desc(self, f_desc):
        """Sets the f_desc of this EthFlowDescription.

        Defines a packet filter of an IP flow.  # noqa: E501

        :param f_desc: The f_desc of this EthFlowDescription.
        :type f_desc: str
        """

        self._f_desc = f_desc

    @property
    def f_dir(self):
        """Gets the f_dir of this EthFlowDescription.


        :return: The f_dir of this EthFlowDescription.
        :rtype: FlowDirection
        """
        return self._f_dir

    @f_dir.setter
    def f_dir(self, f_dir):
        """Sets the f_dir of this EthFlowDescription.


        :param f_dir: The f_dir of this EthFlowDescription.
        :type f_dir: FlowDirection
        """

        self._f_dir = f_dir

    @property
    def source_mac_addr(self):
        """Gets the source_mac_addr of this EthFlowDescription.

        String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042.   # noqa: E501

        :return: The source_mac_addr of this EthFlowDescription.
        :rtype: str
        """
        return self._source_mac_addr

    @source_mac_addr.setter
    def source_mac_addr(self, source_mac_addr):
        """Sets the source_mac_addr of this EthFlowDescription.

        String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042.   # noqa: E501

        :param source_mac_addr: The source_mac_addr of this EthFlowDescription.
        :type source_mac_addr: str
        """
        if source_mac_addr is not None and not re.search(r'^([0-9a-fA-F]{2})((-[0-9a-fA-F]{2}){5})$', source_mac_addr):  # noqa: E501
            raise ValueError("Invalid value for `source_mac_addr`, must be a follow pattern or equal to `/^([0-9a-fA-F]{2})((-[0-9a-fA-F]{2}){5})$/`")  # noqa: E501

        self._source_mac_addr = source_mac_addr

    @property
    def vlan_tags(self):
        """Gets the vlan_tags of this EthFlowDescription.


        :return: The vlan_tags of this EthFlowDescription.
        :rtype: List[str]
        """
        return self._vlan_tags

    @vlan_tags.setter
    def vlan_tags(self, vlan_tags):
        """Sets the vlan_tags of this EthFlowDescription.


        :param vlan_tags: The vlan_tags of this EthFlowDescription.
        :type vlan_tags: List[str]
        """
        if vlan_tags is not None and len(vlan_tags) > 2:
            raise ValueError("Invalid value for `vlan_tags`, number of items must be less than or equal to `2`")  # noqa: E501
        if vlan_tags is not None and len(vlan_tags) < 1:
            raise ValueError("Invalid value for `vlan_tags`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._vlan_tags = vlan_tags

    @property
    def src_mac_addr_end(self):
        """Gets the src_mac_addr_end of this EthFlowDescription.

        String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042.   # noqa: E501

        :return: The src_mac_addr_end of this EthFlowDescription.
        :rtype: str
        """
        return self._src_mac_addr_end

    @src_mac_addr_end.setter
    def src_mac_addr_end(self, src_mac_addr_end):
        """Sets the src_mac_addr_end of this EthFlowDescription.

        String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042.   # noqa: E501

        :param src_mac_addr_end: The src_mac_addr_end of this EthFlowDescription.
        :type src_mac_addr_end: str
        """
        if src_mac_addr_end is not None and not re.search(r'^([0-9a-fA-F]{2})((-[0-9a-fA-F]{2}){5})$', src_mac_addr_end):  # noqa: E501
            raise ValueError("Invalid value for `src_mac_addr_end`, must be a follow pattern or equal to `/^([0-9a-fA-F]{2})((-[0-9a-fA-F]{2}){5})$/`")  # noqa: E501

        self._src_mac_addr_end = src_mac_addr_end

    @property
    def dest_mac_addr_end(self):
        """Gets the dest_mac_addr_end of this EthFlowDescription.

        String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042.   # noqa: E501

        :return: The dest_mac_addr_end of this EthFlowDescription.
        :rtype: str
        """
        return self._dest_mac_addr_end

    @dest_mac_addr_end.setter
    def dest_mac_addr_end(self, dest_mac_addr_end):
        """Sets the dest_mac_addr_end of this EthFlowDescription.

        String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042.   # noqa: E501

        :param dest_mac_addr_end: The dest_mac_addr_end of this EthFlowDescription.
        :type dest_mac_addr_end: str
        """
        if dest_mac_addr_end is not None and not re.search(r'^([0-9a-fA-F]{2})((-[0-9a-fA-F]{2}){5})$', dest_mac_addr_end):  # noqa: E501
            raise ValueError("Invalid value for `dest_mac_addr_end`, must be a follow pattern or equal to `/^([0-9a-fA-F]{2})((-[0-9a-fA-F]{2}){5})$/`")  # noqa: E501

        self._dest_mac_addr_end = dest_mac_addr_end

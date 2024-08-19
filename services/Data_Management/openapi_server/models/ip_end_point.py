# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ipv6_addr import Ipv6Addr
from openapi_server.models.transport_protocol1 import TransportProtocol1
import re
from openapi_server import util

from openapi_server.models.ipv6_addr import Ipv6Addr  # noqa: E501
from openapi_server.models.transport_protocol1 import TransportProtocol1  # noqa: E501
import re  # noqa: E501

class IpEndPoint(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ipv4_address=None, ipv6_address=None, transport=None, port=None):  # noqa: E501
        """IpEndPoint - a model defined in OpenAPI

        :param ipv4_address: The ipv4_address of this IpEndPoint.  # noqa: E501
        :type ipv4_address: str
        :param ipv6_address: The ipv6_address of this IpEndPoint.  # noqa: E501
        :type ipv6_address: Ipv6Addr
        :param transport: The transport of this IpEndPoint.  # noqa: E501
        :type transport: TransportProtocol1
        :param port: The port of this IpEndPoint.  # noqa: E501
        :type port: int
        """
        self.openapi_types = {
            'ipv4_address': str,
            'ipv6_address': Ipv6Addr,
            'transport': TransportProtocol1,
            'port': int
        }

        self.attribute_map = {
            'ipv4_address': 'ipv4Address',
            'ipv6_address': 'ipv6Address',
            'transport': 'transport',
            'port': 'port'
        }

        self._ipv4_address = ipv4_address
        self._ipv6_address = ipv6_address
        self._transport = transport
        self._port = port

    @classmethod
    def from_dict(cls, dikt) -> 'IpEndPoint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IpEndPoint of this IpEndPoint.  # noqa: E501
        :rtype: IpEndPoint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ipv4_address(self):
        """Gets the ipv4_address of this IpEndPoint.

        String identifying a IPv4 address formatted in the 'dotted decimal' notation as defined in RFC 1166.   # noqa: E501

        :return: The ipv4_address of this IpEndPoint.
        :rtype: str
        """
        return self._ipv4_address

    @ipv4_address.setter
    def ipv4_address(self, ipv4_address):
        """Sets the ipv4_address of this IpEndPoint.

        String identifying a IPv4 address formatted in the 'dotted decimal' notation as defined in RFC 1166.   # noqa: E501

        :param ipv4_address: The ipv4_address of this IpEndPoint.
        :type ipv4_address: str
        """
        if ipv4_address is not None and not re.search(r'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$', ipv4_address):  # noqa: E501
            raise ValueError("Invalid value for `ipv4_address`, must be a follow pattern or equal to `/^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$/`")  # noqa: E501

        self._ipv4_address = ipv4_address

    @property
    def ipv6_address(self):
        """Gets the ipv6_address of this IpEndPoint.


        :return: The ipv6_address of this IpEndPoint.
        :rtype: Ipv6Addr
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        """Sets the ipv6_address of this IpEndPoint.


        :param ipv6_address: The ipv6_address of this IpEndPoint.
        :type ipv6_address: Ipv6Addr
        """

        self._ipv6_address = ipv6_address

    @property
    def transport(self):
        """Gets the transport of this IpEndPoint.


        :return: The transport of this IpEndPoint.
        :rtype: TransportProtocol1
        """
        return self._transport

    @transport.setter
    def transport(self, transport):
        """Sets the transport of this IpEndPoint.


        :param transport: The transport of this IpEndPoint.
        :type transport: TransportProtocol1
        """

        self._transport = transport

    @property
    def port(self):
        """Gets the port of this IpEndPoint.


        :return: The port of this IpEndPoint.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this IpEndPoint.


        :param port: The port of this IpEndPoint.
        :type port: int
        """
        if port is not None and port > 65535:  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value less than or equal to `65535`")  # noqa: E501
        if port is not None and port < 0:  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value greater than or equal to `0`")  # noqa: E501

        self._port = port
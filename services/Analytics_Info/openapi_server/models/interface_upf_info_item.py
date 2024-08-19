# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ipv6_addr import Ipv6Addr
from openapi_server.models.up_interface_type import UPInterfaceType
import re
from openapi_server import util

from openapi_server.models.ipv6_addr import Ipv6Addr  # noqa: E501
from openapi_server.models.up_interface_type import UPInterfaceType  # noqa: E501
import re  # noqa: E501

class InterfaceUpfInfoItem(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, interface_type=None, ipv4_endpoint_addresses=None, ipv6_endpoint_addresses=None, endpoint_fqdn=None, network_instance=None):  # noqa: E501
        """InterfaceUpfInfoItem - a model defined in OpenAPI

        :param interface_type: The interface_type of this InterfaceUpfInfoItem.  # noqa: E501
        :type interface_type: UPInterfaceType
        :param ipv4_endpoint_addresses: The ipv4_endpoint_addresses of this InterfaceUpfInfoItem.  # noqa: E501
        :type ipv4_endpoint_addresses: List[str]
        :param ipv6_endpoint_addresses: The ipv6_endpoint_addresses of this InterfaceUpfInfoItem.  # noqa: E501
        :type ipv6_endpoint_addresses: List[Ipv6Addr]
        :param endpoint_fqdn: The endpoint_fqdn of this InterfaceUpfInfoItem.  # noqa: E501
        :type endpoint_fqdn: str
        :param network_instance: The network_instance of this InterfaceUpfInfoItem.  # noqa: E501
        :type network_instance: str
        """
        self.openapi_types = {
            'interface_type': UPInterfaceType,
            'ipv4_endpoint_addresses': List[str],
            'ipv6_endpoint_addresses': List[Ipv6Addr],
            'endpoint_fqdn': str,
            'network_instance': str
        }

        self.attribute_map = {
            'interface_type': 'interfaceType',
            'ipv4_endpoint_addresses': 'ipv4EndpointAddresses',
            'ipv6_endpoint_addresses': 'ipv6EndpointAddresses',
            'endpoint_fqdn': 'endpointFqdn',
            'network_instance': 'networkInstance'
        }

        self._interface_type = interface_type
        self._ipv4_endpoint_addresses = ipv4_endpoint_addresses
        self._ipv6_endpoint_addresses = ipv6_endpoint_addresses
        self._endpoint_fqdn = endpoint_fqdn
        self._network_instance = network_instance

    @classmethod
    def from_dict(cls, dikt) -> 'InterfaceUpfInfoItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InterfaceUpfInfoItem of this InterfaceUpfInfoItem.  # noqa: E501
        :rtype: InterfaceUpfInfoItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def interface_type(self):
        """Gets the interface_type of this InterfaceUpfInfoItem.


        :return: The interface_type of this InterfaceUpfInfoItem.
        :rtype: UPInterfaceType
        """
        return self._interface_type

    @interface_type.setter
    def interface_type(self, interface_type):
        """Sets the interface_type of this InterfaceUpfInfoItem.


        :param interface_type: The interface_type of this InterfaceUpfInfoItem.
        :type interface_type: UPInterfaceType
        """
        if interface_type is None:
            raise ValueError("Invalid value for `interface_type`, must not be `None`")  # noqa: E501

        self._interface_type = interface_type

    @property
    def ipv4_endpoint_addresses(self):
        """Gets the ipv4_endpoint_addresses of this InterfaceUpfInfoItem.


        :return: The ipv4_endpoint_addresses of this InterfaceUpfInfoItem.
        :rtype: List[str]
        """
        return self._ipv4_endpoint_addresses

    @ipv4_endpoint_addresses.setter
    def ipv4_endpoint_addresses(self, ipv4_endpoint_addresses):
        """Sets the ipv4_endpoint_addresses of this InterfaceUpfInfoItem.


        :param ipv4_endpoint_addresses: The ipv4_endpoint_addresses of this InterfaceUpfInfoItem.
        :type ipv4_endpoint_addresses: List[str]
        """
        if ipv4_endpoint_addresses is not None and len(ipv4_endpoint_addresses) < 1:
            raise ValueError("Invalid value for `ipv4_endpoint_addresses`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ipv4_endpoint_addresses = ipv4_endpoint_addresses

    @property
    def ipv6_endpoint_addresses(self):
        """Gets the ipv6_endpoint_addresses of this InterfaceUpfInfoItem.


        :return: The ipv6_endpoint_addresses of this InterfaceUpfInfoItem.
        :rtype: List[Ipv6Addr]
        """
        return self._ipv6_endpoint_addresses

    @ipv6_endpoint_addresses.setter
    def ipv6_endpoint_addresses(self, ipv6_endpoint_addresses):
        """Sets the ipv6_endpoint_addresses of this InterfaceUpfInfoItem.


        :param ipv6_endpoint_addresses: The ipv6_endpoint_addresses of this InterfaceUpfInfoItem.
        :type ipv6_endpoint_addresses: List[Ipv6Addr]
        """
        if ipv6_endpoint_addresses is not None and len(ipv6_endpoint_addresses) < 1:
            raise ValueError("Invalid value for `ipv6_endpoint_addresses`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ipv6_endpoint_addresses = ipv6_endpoint_addresses

    @property
    def endpoint_fqdn(self):
        """Gets the endpoint_fqdn of this InterfaceUpfInfoItem.

        Fully Qualified Domain Name  # noqa: E501

        :return: The endpoint_fqdn of this InterfaceUpfInfoItem.
        :rtype: str
        """
        return self._endpoint_fqdn

    @endpoint_fqdn.setter
    def endpoint_fqdn(self, endpoint_fqdn):
        """Sets the endpoint_fqdn of this InterfaceUpfInfoItem.

        Fully Qualified Domain Name  # noqa: E501

        :param endpoint_fqdn: The endpoint_fqdn of this InterfaceUpfInfoItem.
        :type endpoint_fqdn: str
        """
        if endpoint_fqdn is not None and len(endpoint_fqdn) > 253:
            raise ValueError("Invalid value for `endpoint_fqdn`, length must be less than or equal to `253`")  # noqa: E501
        if endpoint_fqdn is not None and len(endpoint_fqdn) < 4:
            raise ValueError("Invalid value for `endpoint_fqdn`, length must be greater than or equal to `4`")  # noqa: E501
        if endpoint_fqdn is not None and not re.search(r'^([0-9A-Za-z]([-0-9A-Za-z]{0,61}[0-9A-Za-z])?\.)+[A-Za-z]{2,63}\.?$', endpoint_fqdn):  # noqa: E501
            raise ValueError("Invalid value for `endpoint_fqdn`, must be a follow pattern or equal to `/^([0-9A-Za-z]([-0-9A-Za-z]{0,61}[0-9A-Za-z])?\.)+[A-Za-z]{2,63}\.?$/`")  # noqa: E501

        self._endpoint_fqdn = endpoint_fqdn

    @property
    def network_instance(self):
        """Gets the network_instance of this InterfaceUpfInfoItem.


        :return: The network_instance of this InterfaceUpfInfoItem.
        :rtype: str
        """
        return self._network_instance

    @network_instance.setter
    def network_instance(self, network_instance):
        """Sets the network_instance of this InterfaceUpfInfoItem.


        :param network_instance: The network_instance of this InterfaceUpfInfoItem.
        :type network_instance: str
        """

        self._network_instance = network_instance
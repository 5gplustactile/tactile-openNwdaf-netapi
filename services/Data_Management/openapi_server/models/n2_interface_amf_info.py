# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ipv6_addr import Ipv6Addr
import re
from openapi_server import util

from openapi_server.models.ipv6_addr import Ipv6Addr  # noqa: E501
import re  # noqa: E501

class N2InterfaceAmfInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ipv4_endpoint_address=None, ipv6_endpoint_address=None, amf_name=None):  # noqa: E501
        """N2InterfaceAmfInfo - a model defined in OpenAPI

        :param ipv4_endpoint_address: The ipv4_endpoint_address of this N2InterfaceAmfInfo.  # noqa: E501
        :type ipv4_endpoint_address: List[str]
        :param ipv6_endpoint_address: The ipv6_endpoint_address of this N2InterfaceAmfInfo.  # noqa: E501
        :type ipv6_endpoint_address: List[Ipv6Addr]
        :param amf_name: The amf_name of this N2InterfaceAmfInfo.  # noqa: E501
        :type amf_name: str
        """
        self.openapi_types = {
            'ipv4_endpoint_address': List[str],
            'ipv6_endpoint_address': List[Ipv6Addr],
            'amf_name': str
        }

        self.attribute_map = {
            'ipv4_endpoint_address': 'ipv4EndpointAddress',
            'ipv6_endpoint_address': 'ipv6EndpointAddress',
            'amf_name': 'amfName'
        }

        self._ipv4_endpoint_address = ipv4_endpoint_address
        self._ipv6_endpoint_address = ipv6_endpoint_address
        self._amf_name = amf_name

    @classmethod
    def from_dict(cls, dikt) -> 'N2InterfaceAmfInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The N2InterfaceAmfInfo of this N2InterfaceAmfInfo.  # noqa: E501
        :rtype: N2InterfaceAmfInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ipv4_endpoint_address(self):
        """Gets the ipv4_endpoint_address of this N2InterfaceAmfInfo.


        :return: The ipv4_endpoint_address of this N2InterfaceAmfInfo.
        :rtype: List[str]
        """
        return self._ipv4_endpoint_address

    @ipv4_endpoint_address.setter
    def ipv4_endpoint_address(self, ipv4_endpoint_address):
        """Sets the ipv4_endpoint_address of this N2InterfaceAmfInfo.


        :param ipv4_endpoint_address: The ipv4_endpoint_address of this N2InterfaceAmfInfo.
        :type ipv4_endpoint_address: List[str]
        """
        if ipv4_endpoint_address is not None and len(ipv4_endpoint_address) < 1:
            raise ValueError("Invalid value for `ipv4_endpoint_address`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ipv4_endpoint_address = ipv4_endpoint_address

    @property
    def ipv6_endpoint_address(self):
        """Gets the ipv6_endpoint_address of this N2InterfaceAmfInfo.


        :return: The ipv6_endpoint_address of this N2InterfaceAmfInfo.
        :rtype: List[Ipv6Addr]
        """
        return self._ipv6_endpoint_address

    @ipv6_endpoint_address.setter
    def ipv6_endpoint_address(self, ipv6_endpoint_address):
        """Sets the ipv6_endpoint_address of this N2InterfaceAmfInfo.


        :param ipv6_endpoint_address: The ipv6_endpoint_address of this N2InterfaceAmfInfo.
        :type ipv6_endpoint_address: List[Ipv6Addr]
        """
        if ipv6_endpoint_address is not None and len(ipv6_endpoint_address) < 1:
            raise ValueError("Invalid value for `ipv6_endpoint_address`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ipv6_endpoint_address = ipv6_endpoint_address

    @property
    def amf_name(self):
        """Gets the amf_name of this N2InterfaceAmfInfo.

        Fully Qualified Domain Name  # noqa: E501

        :return: The amf_name of this N2InterfaceAmfInfo.
        :rtype: str
        """
        return self._amf_name

    @amf_name.setter
    def amf_name(self, amf_name):
        """Sets the amf_name of this N2InterfaceAmfInfo.

        Fully Qualified Domain Name  # noqa: E501

        :param amf_name: The amf_name of this N2InterfaceAmfInfo.
        :type amf_name: str
        """
        if amf_name is not None and len(amf_name) > 253:
            raise ValueError("Invalid value for `amf_name`, length must be less than or equal to `253`")  # noqa: E501
        if amf_name is not None and len(amf_name) < 4:
            raise ValueError("Invalid value for `amf_name`, length must be greater than or equal to `4`")  # noqa: E501
        if amf_name is not None and not re.search(r'^([0-9A-Za-z]([-0-9A-Za-z]{0,61}[0-9A-Za-z])?\.)+[A-Za-z]{2,63}\.?$', amf_name):  # noqa: E501
            raise ValueError("Invalid value for `amf_name`, must be a follow pattern or equal to `/^([0-9A-Za-z]([-0-9A-Za-z]{0,61}[0-9A-Za-z])?\.)+[A-Za-z]{2,63}\.?$/`")  # noqa: E501

        self._amf_name = amf_name

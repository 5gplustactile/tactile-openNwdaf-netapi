# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ip_packet_filter_set import IpPacketFilterSet
from openapi_server import util

from openapi_server.models.ip_packet_filter_set import IpPacketFilterSet  # noqa: E501

class ServiceDataFlowDescription(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, flow_description=None, domain_name=None):  # noqa: E501
        """ServiceDataFlowDescription - a model defined in OpenAPI

        :param flow_description: The flow_description of this ServiceDataFlowDescription.  # noqa: E501
        :type flow_description: IpPacketFilterSet
        :param domain_name: The domain_name of this ServiceDataFlowDescription.  # noqa: E501
        :type domain_name: str
        """
        self.openapi_types = {
            'flow_description': IpPacketFilterSet,
            'domain_name': str
        }

        self.attribute_map = {
            'flow_description': 'flowDescription',
            'domain_name': 'domainName'
        }

        self._flow_description = flow_description
        self._domain_name = domain_name

    @classmethod
    def from_dict(cls, dikt) -> 'ServiceDataFlowDescription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ServiceDataFlowDescription of this ServiceDataFlowDescription.  # noqa: E501
        :rtype: ServiceDataFlowDescription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def flow_description(self):
        """Gets the flow_description of this ServiceDataFlowDescription.


        :return: The flow_description of this ServiceDataFlowDescription.
        :rtype: IpPacketFilterSet
        """
        return self._flow_description

    @flow_description.setter
    def flow_description(self, flow_description):
        """Sets the flow_description of this ServiceDataFlowDescription.


        :param flow_description: The flow_description of this ServiceDataFlowDescription.
        :type flow_description: IpPacketFilterSet
        """

        self._flow_description = flow_description

    @property
    def domain_name(self):
        """Gets the domain_name of this ServiceDataFlowDescription.


        :return: The domain_name of this ServiceDataFlowDescription.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ServiceDataFlowDescription.


        :param domain_name: The domain_name of this ServiceDataFlowDescription.
        :type domain_name: str
        """

        self._domain_name = domain_name

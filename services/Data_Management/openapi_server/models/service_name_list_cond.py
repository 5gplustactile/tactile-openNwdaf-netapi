# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.service_name import ServiceName
from openapi_server import util

from openapi_server.models.service_name import ServiceName  # noqa: E501

class ServiceNameListCond(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, condition_type=None, service_name_list=None):  # noqa: E501
        """ServiceNameListCond - a model defined in OpenAPI

        :param condition_type: The condition_type of this ServiceNameListCond.  # noqa: E501
        :type condition_type: str
        :param service_name_list: The service_name_list of this ServiceNameListCond.  # noqa: E501
        :type service_name_list: List[ServiceName]
        """
        self.openapi_types = {
            'condition_type': str,
            'service_name_list': List[ServiceName]
        }

        self.attribute_map = {
            'condition_type': 'conditionType',
            'service_name_list': 'serviceNameList'
        }

        self._condition_type = condition_type
        self._service_name_list = service_name_list

    @classmethod
    def from_dict(cls, dikt) -> 'ServiceNameListCond':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ServiceNameListCond of this ServiceNameListCond.  # noqa: E501
        :rtype: ServiceNameListCond
        """
        return util.deserialize_model(dikt, cls)

    @property
    def condition_type(self):
        """Gets the condition_type of this ServiceNameListCond.


        :return: The condition_type of this ServiceNameListCond.
        :rtype: str
        """
        return self._condition_type

    @condition_type.setter
    def condition_type(self, condition_type):
        """Sets the condition_type of this ServiceNameListCond.


        :param condition_type: The condition_type of this ServiceNameListCond.
        :type condition_type: str
        """
        allowed_values = ["SERVICE_NAME_LIST_COND"]  # noqa: E501
        if condition_type not in allowed_values:
            raise ValueError(
                "Invalid value for `condition_type` ({0}), must be one of {1}"
                .format(condition_type, allowed_values)
            )

        self._condition_type = condition_type

    @property
    def service_name_list(self):
        """Gets the service_name_list of this ServiceNameListCond.


        :return: The service_name_list of this ServiceNameListCond.
        :rtype: List[ServiceName]
        """
        return self._service_name_list

    @service_name_list.setter
    def service_name_list(self, service_name_list):
        """Sets the service_name_list of this ServiceNameListCond.


        :param service_name_list: The service_name_list of this ServiceNameListCond.
        :type service_name_list: List[ServiceName]
        """
        if service_name_list is None:
            raise ValueError("Invalid value for `service_name_list`, must not be `None`")  # noqa: E501
        if service_name_list is not None and len(service_name_list) < 1:
            raise ValueError("Invalid value for `service_name_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._service_name_list = service_name_list
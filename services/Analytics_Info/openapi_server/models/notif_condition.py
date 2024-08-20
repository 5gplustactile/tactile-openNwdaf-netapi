# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class NotifCondition(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, monitored_attributes=None, unmonitored_attributes=None):  # noqa: E501
        """NotifCondition - a model defined in OpenAPI

        :param monitored_attributes: The monitored_attributes of this NotifCondition.  # noqa: E501
        :type monitored_attributes: List[str]
        :param unmonitored_attributes: The unmonitored_attributes of this NotifCondition.  # noqa: E501
        :type unmonitored_attributes: List[str]
        """
        self.openapi_types = {
            'monitored_attributes': List[str],
            'unmonitored_attributes': List[str]
        }

        self.attribute_map = {
            'monitored_attributes': 'monitoredAttributes',
            'unmonitored_attributes': 'unmonitoredAttributes'
        }

        self._monitored_attributes = monitored_attributes
        self._unmonitored_attributes = unmonitored_attributes

    @classmethod
    def from_dict(cls, dikt) -> 'NotifCondition':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NotifCondition of this NotifCondition.  # noqa: E501
        :rtype: NotifCondition
        """
        return util.deserialize_model(dikt, cls)

    @property
    def monitored_attributes(self):
        """Gets the monitored_attributes of this NotifCondition.


        :return: The monitored_attributes of this NotifCondition.
        :rtype: List[str]
        """
        return self._monitored_attributes

    @monitored_attributes.setter
    def monitored_attributes(self, monitored_attributes):
        """Sets the monitored_attributes of this NotifCondition.


        :param monitored_attributes: The monitored_attributes of this NotifCondition.
        :type monitored_attributes: List[str]
        """
        if monitored_attributes is not None and len(monitored_attributes) < 1:
            raise ValueError("Invalid value for `monitored_attributes`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._monitored_attributes = monitored_attributes

    @property
    def unmonitored_attributes(self):
        """Gets the unmonitored_attributes of this NotifCondition.


        :return: The unmonitored_attributes of this NotifCondition.
        :rtype: List[str]
        """
        return self._unmonitored_attributes

    @unmonitored_attributes.setter
    def unmonitored_attributes(self, unmonitored_attributes):
        """Sets the unmonitored_attributes of this NotifCondition.


        :param unmonitored_attributes: The unmonitored_attributes of this NotifCondition.
        :type unmonitored_attributes: List[str]
        """
        if unmonitored_attributes is not None and len(unmonitored_attributes) < 1:
            raise ValueError("Invalid value for `unmonitored_attributes`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._unmonitored_attributes = unmonitored_attributes

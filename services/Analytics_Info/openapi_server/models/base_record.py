# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class BaseRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, timestamp=None):  # noqa: E501
        """BaseRecord - a model defined in OpenAPI

        :param timestamp: The timestamp of this BaseRecord.  # noqa: E501
        :type timestamp: datetime
        """
        self.openapi_types = {
            'timestamp': datetime
        }

        self.attribute_map = {
            'timestamp': 'timestamp'
        }

        self._timestamp = timestamp

    @classmethod
    def from_dict(cls, dikt) -> 'BaseRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BaseRecord of this BaseRecord.  # noqa: E501
        :rtype: BaseRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def timestamp(self):
        """Gets the timestamp of this BaseRecord.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :return: The timestamp of this BaseRecord.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this BaseRecord.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :param timestamp: The timestamp of this BaseRecord.
        :type timestamp: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp
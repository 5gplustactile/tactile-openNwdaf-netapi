# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.user_location import UserLocation
from openapi_server import util

from openapi_server.models.user_location import UserLocation  # noqa: E501

class UeTrajectoryInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ts=None, location=None):  # noqa: E501
        """UeTrajectoryInfo - a model defined in OpenAPI

        :param ts: The ts of this UeTrajectoryInfo.  # noqa: E501
        :type ts: datetime
        :param location: The location of this UeTrajectoryInfo.  # noqa: E501
        :type location: UserLocation
        """
        self.openapi_types = {
            'ts': datetime,
            'location': UserLocation
        }

        self.attribute_map = {
            'ts': 'ts',
            'location': 'location'
        }

        self._ts = ts
        self._location = location

    @classmethod
    def from_dict(cls, dikt) -> 'UeTrajectoryInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UeTrajectoryInfo of this UeTrajectoryInfo.  # noqa: E501
        :rtype: UeTrajectoryInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ts(self):
        """Gets the ts of this UeTrajectoryInfo.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :return: The ts of this UeTrajectoryInfo.
        :rtype: datetime
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """Sets the ts of this UeTrajectoryInfo.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :param ts: The ts of this UeTrajectoryInfo.
        :type ts: datetime
        """
        if ts is None:
            raise ValueError("Invalid value for `ts`, must not be `None`")  # noqa: E501

        self._ts = ts

    @property
    def location(self):
        """Gets the location of this UeTrajectoryInfo.


        :return: The location of this UeTrajectoryInfo.
        :rtype: UserLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this UeTrajectoryInfo.


        :param location: The location of this UeTrajectoryInfo.
        :type location: UserLocation
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

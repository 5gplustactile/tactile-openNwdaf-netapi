# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SACEventState(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, active=None, remain_reports=None, remain_duration=None):  # noqa: E501
        """SACEventState - a model defined in OpenAPI

        :param active: The active of this SACEventState.  # noqa: E501
        :type active: bool
        :param remain_reports: The remain_reports of this SACEventState.  # noqa: E501
        :type remain_reports: int
        :param remain_duration: The remain_duration of this SACEventState.  # noqa: E501
        :type remain_duration: int
        """
        self.openapi_types = {
            'active': bool,
            'remain_reports': int,
            'remain_duration': int
        }

        self.attribute_map = {
            'active': 'active',
            'remain_reports': 'remainReports',
            'remain_duration': 'remainDuration'
        }

        self._active = active
        self._remain_reports = remain_reports
        self._remain_duration = remain_duration

    @classmethod
    def from_dict(cls, dikt) -> 'SACEventState':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SACEventState of this SACEventState.  # noqa: E501
        :rtype: SACEventState
        """
        return util.deserialize_model(dikt, cls)

    @property
    def active(self):
        """Gets the active of this SACEventState.


        :return: The active of this SACEventState.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this SACEventState.


        :param active: The active of this SACEventState.
        :type active: bool
        """
        if active is None:
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def remain_reports(self):
        """Gets the remain_reports of this SACEventState.


        :return: The remain_reports of this SACEventState.
        :rtype: int
        """
        return self._remain_reports

    @remain_reports.setter
    def remain_reports(self, remain_reports):
        """Sets the remain_reports of this SACEventState.


        :param remain_reports: The remain_reports of this SACEventState.
        :type remain_reports: int
        """

        self._remain_reports = remain_reports

    @property
    def remain_duration(self):
        """Gets the remain_duration of this SACEventState.

        indicating a time in seconds.  # noqa: E501

        :return: The remain_duration of this SACEventState.
        :rtype: int
        """
        return self._remain_duration

    @remain_duration.setter
    def remain_duration(self, remain_duration):
        """Sets the remain_duration of this SACEventState.

        indicating a time in seconds.  # noqa: E501

        :param remain_duration: The remain_duration of this SACEventState.
        :type remain_duration: int
        """

        self._remain_duration = remain_duration

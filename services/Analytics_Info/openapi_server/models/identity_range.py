# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class IdentityRange(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, start=None, end=None, pattern=None):  # noqa: E501
        """IdentityRange - a model defined in OpenAPI

        :param start: The start of this IdentityRange.  # noqa: E501
        :type start: str
        :param end: The end of this IdentityRange.  # noqa: E501
        :type end: str
        :param pattern: The pattern of this IdentityRange.  # noqa: E501
        :type pattern: str
        """
        self.openapi_types = {
            'start': str,
            'end': str,
            'pattern': str
        }

        self.attribute_map = {
            'start': 'start',
            'end': 'end',
            'pattern': 'pattern'
        }

        self._start = start
        self._end = end
        self._pattern = pattern

    @classmethod
    def from_dict(cls, dikt) -> 'IdentityRange':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IdentityRange of this IdentityRange.  # noqa: E501
        :rtype: IdentityRange
        """
        return util.deserialize_model(dikt, cls)

    @property
    def start(self):
        """Gets the start of this IdentityRange.


        :return: The start of this IdentityRange.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this IdentityRange.


        :param start: The start of this IdentityRange.
        :type start: str
        """
        if start is not None and not re.search(r'^[0-9]+$', start):  # noqa: E501
            raise ValueError("Invalid value for `start`, must be a follow pattern or equal to `/^[0-9]+$/`")  # noqa: E501

        self._start = start

    @property
    def end(self):
        """Gets the end of this IdentityRange.


        :return: The end of this IdentityRange.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this IdentityRange.


        :param end: The end of this IdentityRange.
        :type end: str
        """
        if end is not None and not re.search(r'^[0-9]+$', end):  # noqa: E501
            raise ValueError("Invalid value for `end`, must be a follow pattern or equal to `/^[0-9]+$/`")  # noqa: E501

        self._end = end

    @property
    def pattern(self):
        """Gets the pattern of this IdentityRange.


        :return: The pattern of this IdentityRange.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this IdentityRange.


        :param pattern: The pattern of this IdentityRange.
        :type pattern: str
        """

        self._pattern = pattern

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class SdRange(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, start=None, end=None):  # noqa: E501
        """SdRange - a model defined in OpenAPI

        :param start: The start of this SdRange.  # noqa: E501
        :type start: str
        :param end: The end of this SdRange.  # noqa: E501
        :type end: str
        """
        self.openapi_types = {
            'start': str,
            'end': str
        }

        self.attribute_map = {
            'start': 'start',
            'end': 'end'
        }

        self._start = start
        self._end = end

    @classmethod
    def from_dict(cls, dikt) -> 'SdRange':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SdRange of this SdRange.  # noqa: E501
        :rtype: SdRange
        """
        return util.deserialize_model(dikt, cls)

    @property
    def start(self):
        """Gets the start of this SdRange.

        First value identifying the start of an SD range. This string shall be formatted as specified for the sd attribute of the Snssai data type in clause 5.4.4.2.   # noqa: E501

        :return: The start of this SdRange.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this SdRange.

        First value identifying the start of an SD range. This string shall be formatted as specified for the sd attribute of the Snssai data type in clause 5.4.4.2.   # noqa: E501

        :param start: The start of this SdRange.
        :type start: str
        """
        if start is not None and not re.search(r'^[A-Fa-f0-9]{6}$', start):  # noqa: E501
            raise ValueError("Invalid value for `start`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{6}$/`")  # noqa: E501

        self._start = start

    @property
    def end(self):
        """Gets the end of this SdRange.

        Last value identifying the end of an SD range. This string shall be formatted as specified for the sd attribute of the Snssai data type in clause 5.4.4.2.   # noqa: E501

        :return: The end of this SdRange.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this SdRange.

        Last value identifying the end of an SD range. This string shall be formatted as specified for the sd attribute of the Snssai data type in clause 5.4.4.2.   # noqa: E501

        :param end: The end of this SdRange.
        :type end: str
        """
        if end is not None and not re.search(r'^[A-Fa-f0-9]{6}$', end):  # noqa: E501
            raise ValueError("Invalid value for `end`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{6}$/`")  # noqa: E501

        self._end = end
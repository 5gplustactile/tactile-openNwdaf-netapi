# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.internal_group_id_range import InternalGroupIdRange
from openapi_server.models.supi_range import SupiRange
from openapi_server import util

from openapi_server.models.internal_group_id_range import InternalGroupIdRange  # noqa: E501
from openapi_server.models.supi_range import SupiRange  # noqa: E501

class NssaafInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, supi_ranges=None, internal_group_identifiers_ranges=None):  # noqa: E501
        """NssaafInfo - a model defined in OpenAPI

        :param supi_ranges: The supi_ranges of this NssaafInfo.  # noqa: E501
        :type supi_ranges: List[SupiRange]
        :param internal_group_identifiers_ranges: The internal_group_identifiers_ranges of this NssaafInfo.  # noqa: E501
        :type internal_group_identifiers_ranges: List[InternalGroupIdRange]
        """
        self.openapi_types = {
            'supi_ranges': List[SupiRange],
            'internal_group_identifiers_ranges': List[InternalGroupIdRange]
        }

        self.attribute_map = {
            'supi_ranges': 'supiRanges',
            'internal_group_identifiers_ranges': 'internalGroupIdentifiersRanges'
        }

        self._supi_ranges = supi_ranges
        self._internal_group_identifiers_ranges = internal_group_identifiers_ranges

    @classmethod
    def from_dict(cls, dikt) -> 'NssaafInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NssaafInfo of this NssaafInfo.  # noqa: E501
        :rtype: NssaafInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def supi_ranges(self):
        """Gets the supi_ranges of this NssaafInfo.


        :return: The supi_ranges of this NssaafInfo.
        :rtype: List[SupiRange]
        """
        return self._supi_ranges

    @supi_ranges.setter
    def supi_ranges(self, supi_ranges):
        """Sets the supi_ranges of this NssaafInfo.


        :param supi_ranges: The supi_ranges of this NssaafInfo.
        :type supi_ranges: List[SupiRange]
        """
        if supi_ranges is not None and len(supi_ranges) < 1:
            raise ValueError("Invalid value for `supi_ranges`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._supi_ranges = supi_ranges

    @property
    def internal_group_identifiers_ranges(self):
        """Gets the internal_group_identifiers_ranges of this NssaafInfo.


        :return: The internal_group_identifiers_ranges of this NssaafInfo.
        :rtype: List[InternalGroupIdRange]
        """
        return self._internal_group_identifiers_ranges

    @internal_group_identifiers_ranges.setter
    def internal_group_identifiers_ranges(self, internal_group_identifiers_ranges):
        """Sets the internal_group_identifiers_ranges of this NssaafInfo.


        :param internal_group_identifiers_ranges: The internal_group_identifiers_ranges of this NssaafInfo.
        :type internal_group_identifiers_ranges: List[InternalGroupIdRange]
        """
        if internal_group_identifiers_ranges is not None and len(internal_group_identifiers_ranges) < 1:
            raise ValueError("Invalid value for `internal_group_identifiers_ranges`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._internal_group_identifiers_ranges = internal_group_identifiers_ranges

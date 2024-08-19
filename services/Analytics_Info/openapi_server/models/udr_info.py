# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.data_set_id import DataSetId
from openapi_server.models.identity_range import IdentityRange
from openapi_server.models.shared_data_id_range import SharedDataIdRange
from openapi_server.models.supi_range import SupiRange
from openapi_server import util

from openapi_server.models.data_set_id import DataSetId  # noqa: E501
from openapi_server.models.identity_range import IdentityRange  # noqa: E501
from openapi_server.models.shared_data_id_range import SharedDataIdRange  # noqa: E501
from openapi_server.models.supi_range import SupiRange  # noqa: E501

class UdrInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, group_id=None, supi_ranges=None, gpsi_ranges=None, external_group_identifiers_ranges=None, supported_data_sets=None, shared_data_id_ranges=None):  # noqa: E501
        """UdrInfo - a model defined in OpenAPI

        :param group_id: The group_id of this UdrInfo.  # noqa: E501
        :type group_id: str
        :param supi_ranges: The supi_ranges of this UdrInfo.  # noqa: E501
        :type supi_ranges: List[SupiRange]
        :param gpsi_ranges: The gpsi_ranges of this UdrInfo.  # noqa: E501
        :type gpsi_ranges: List[IdentityRange]
        :param external_group_identifiers_ranges: The external_group_identifiers_ranges of this UdrInfo.  # noqa: E501
        :type external_group_identifiers_ranges: List[IdentityRange]
        :param supported_data_sets: The supported_data_sets of this UdrInfo.  # noqa: E501
        :type supported_data_sets: List[DataSetId]
        :param shared_data_id_ranges: The shared_data_id_ranges of this UdrInfo.  # noqa: E501
        :type shared_data_id_ranges: List[SharedDataIdRange]
        """
        self.openapi_types = {
            'group_id': str,
            'supi_ranges': List[SupiRange],
            'gpsi_ranges': List[IdentityRange],
            'external_group_identifiers_ranges': List[IdentityRange],
            'supported_data_sets': List[DataSetId],
            'shared_data_id_ranges': List[SharedDataIdRange]
        }

        self.attribute_map = {
            'group_id': 'groupId',
            'supi_ranges': 'supiRanges',
            'gpsi_ranges': 'gpsiRanges',
            'external_group_identifiers_ranges': 'externalGroupIdentifiersRanges',
            'supported_data_sets': 'supportedDataSets',
            'shared_data_id_ranges': 'sharedDataIdRanges'
        }

        self._group_id = group_id
        self._supi_ranges = supi_ranges
        self._gpsi_ranges = gpsi_ranges
        self._external_group_identifiers_ranges = external_group_identifiers_ranges
        self._supported_data_sets = supported_data_sets
        self._shared_data_id_ranges = shared_data_id_ranges

    @classmethod
    def from_dict(cls, dikt) -> 'UdrInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UdrInfo of this UdrInfo.  # noqa: E501
        :rtype: UdrInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def group_id(self):
        """Gets the group_id of this UdrInfo.

        Identifier of a group of NFs.  # noqa: E501

        :return: The group_id of this UdrInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this UdrInfo.

        Identifier of a group of NFs.  # noqa: E501

        :param group_id: The group_id of this UdrInfo.
        :type group_id: str
        """

        self._group_id = group_id

    @property
    def supi_ranges(self):
        """Gets the supi_ranges of this UdrInfo.


        :return: The supi_ranges of this UdrInfo.
        :rtype: List[SupiRange]
        """
        return self._supi_ranges

    @supi_ranges.setter
    def supi_ranges(self, supi_ranges):
        """Sets the supi_ranges of this UdrInfo.


        :param supi_ranges: The supi_ranges of this UdrInfo.
        :type supi_ranges: List[SupiRange]
        """
        if supi_ranges is not None and len(supi_ranges) < 1:
            raise ValueError("Invalid value for `supi_ranges`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._supi_ranges = supi_ranges

    @property
    def gpsi_ranges(self):
        """Gets the gpsi_ranges of this UdrInfo.


        :return: The gpsi_ranges of this UdrInfo.
        :rtype: List[IdentityRange]
        """
        return self._gpsi_ranges

    @gpsi_ranges.setter
    def gpsi_ranges(self, gpsi_ranges):
        """Sets the gpsi_ranges of this UdrInfo.


        :param gpsi_ranges: The gpsi_ranges of this UdrInfo.
        :type gpsi_ranges: List[IdentityRange]
        """
        if gpsi_ranges is not None and len(gpsi_ranges) < 1:
            raise ValueError("Invalid value for `gpsi_ranges`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._gpsi_ranges = gpsi_ranges

    @property
    def external_group_identifiers_ranges(self):
        """Gets the external_group_identifiers_ranges of this UdrInfo.


        :return: The external_group_identifiers_ranges of this UdrInfo.
        :rtype: List[IdentityRange]
        """
        return self._external_group_identifiers_ranges

    @external_group_identifiers_ranges.setter
    def external_group_identifiers_ranges(self, external_group_identifiers_ranges):
        """Sets the external_group_identifiers_ranges of this UdrInfo.


        :param external_group_identifiers_ranges: The external_group_identifiers_ranges of this UdrInfo.
        :type external_group_identifiers_ranges: List[IdentityRange]
        """
        if external_group_identifiers_ranges is not None and len(external_group_identifiers_ranges) < 1:
            raise ValueError("Invalid value for `external_group_identifiers_ranges`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._external_group_identifiers_ranges = external_group_identifiers_ranges

    @property
    def supported_data_sets(self):
        """Gets the supported_data_sets of this UdrInfo.


        :return: The supported_data_sets of this UdrInfo.
        :rtype: List[DataSetId]
        """
        return self._supported_data_sets

    @supported_data_sets.setter
    def supported_data_sets(self, supported_data_sets):
        """Sets the supported_data_sets of this UdrInfo.


        :param supported_data_sets: The supported_data_sets of this UdrInfo.
        :type supported_data_sets: List[DataSetId]
        """
        if supported_data_sets is not None and len(supported_data_sets) < 1:
            raise ValueError("Invalid value for `supported_data_sets`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._supported_data_sets = supported_data_sets

    @property
    def shared_data_id_ranges(self):
        """Gets the shared_data_id_ranges of this UdrInfo.


        :return: The shared_data_id_ranges of this UdrInfo.
        :rtype: List[SharedDataIdRange]
        """
        return self._shared_data_id_ranges

    @shared_data_id_ranges.setter
    def shared_data_id_ranges(self, shared_data_id_ranges):
        """Sets the shared_data_id_ranges of this UdrInfo.


        :param shared_data_id_ranges: The shared_data_id_ranges of this UdrInfo.
        :type shared_data_id_ranges: List[SharedDataIdRange]
        """
        if shared_data_id_ranges is not None and len(shared_data_id_ranges) < 1:
            raise ValueError("Invalid value for `shared_data_id_ranges`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._shared_data_id_ranges = shared_data_id_ranges
# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.locality_type import LocalityType
from openapi_server import util

from openapi_server.models.locality_type import LocalityType  # noqa: E501

class LocalityDescriptionItem(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, locality_type=None, locality_value=None):  # noqa: E501
        """LocalityDescriptionItem - a model defined in OpenAPI

        :param locality_type: The locality_type of this LocalityDescriptionItem.  # noqa: E501
        :type locality_type: LocalityType
        :param locality_value: The locality_value of this LocalityDescriptionItem.  # noqa: E501
        :type locality_value: str
        """
        self.openapi_types = {
            'locality_type': LocalityType,
            'locality_value': str
        }

        self.attribute_map = {
            'locality_type': 'localityType',
            'locality_value': 'localityValue'
        }

        self._locality_type = locality_type
        self._locality_value = locality_value

    @classmethod
    def from_dict(cls, dikt) -> 'LocalityDescriptionItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LocalityDescriptionItem of this LocalityDescriptionItem.  # noqa: E501
        :rtype: LocalityDescriptionItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def locality_type(self):
        """Gets the locality_type of this LocalityDescriptionItem.


        :return: The locality_type of this LocalityDescriptionItem.
        :rtype: LocalityType
        """
        return self._locality_type

    @locality_type.setter
    def locality_type(self, locality_type):
        """Sets the locality_type of this LocalityDescriptionItem.


        :param locality_type: The locality_type of this LocalityDescriptionItem.
        :type locality_type: LocalityType
        """
        if locality_type is None:
            raise ValueError("Invalid value for `locality_type`, must not be `None`")  # noqa: E501

        self._locality_type = locality_type

    @property
    def locality_value(self):
        """Gets the locality_value of this LocalityDescriptionItem.


        :return: The locality_value of this LocalityDescriptionItem.
        :rtype: str
        """
        return self._locality_value

    @locality_value.setter
    def locality_value(self, locality_value):
        """Sets the locality_value of this LocalityDescriptionItem.


        :param locality_value: The locality_value of this LocalityDescriptionItem.
        :type locality_value: str
        """
        if locality_value is None:
            raise ValueError("Invalid value for `locality_value`, must not be `None`")  # noqa: E501

        self._locality_value = locality_value
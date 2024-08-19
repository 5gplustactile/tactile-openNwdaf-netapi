# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.collective_behaviour_filter_type import CollectiveBehaviourFilterType
from openapi_server import util

from openapi_server.models.collective_behaviour_filter_type import CollectiveBehaviourFilterType  # noqa: E501

class CollectiveBehaviourFilter(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, value=None, list_of_ue_ind=None):  # noqa: E501
        """CollectiveBehaviourFilter - a model defined in OpenAPI

        :param type: The type of this CollectiveBehaviourFilter.  # noqa: E501
        :type type: CollectiveBehaviourFilterType
        :param value: The value of this CollectiveBehaviourFilter.  # noqa: E501
        :type value: str
        :param list_of_ue_ind: The list_of_ue_ind of this CollectiveBehaviourFilter.  # noqa: E501
        :type list_of_ue_ind: bool
        """
        self.openapi_types = {
            'type': CollectiveBehaviourFilterType,
            'value': str,
            'list_of_ue_ind': bool
        }

        self.attribute_map = {
            'type': 'type',
            'value': 'value',
            'list_of_ue_ind': 'listOfUeInd'
        }

        self._type = type
        self._value = value
        self._list_of_ue_ind = list_of_ue_ind

    @classmethod
    def from_dict(cls, dikt) -> 'CollectiveBehaviourFilter':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CollectiveBehaviourFilter of this CollectiveBehaviourFilter.  # noqa: E501
        :rtype: CollectiveBehaviourFilter
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this CollectiveBehaviourFilter.


        :return: The type of this CollectiveBehaviourFilter.
        :rtype: CollectiveBehaviourFilterType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CollectiveBehaviourFilter.


        :param type: The type of this CollectiveBehaviourFilter.
        :type type: CollectiveBehaviourFilterType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def value(self):
        """Gets the value of this CollectiveBehaviourFilter.

        Value of the parameter type as in the type attribute.  # noqa: E501

        :return: The value of this CollectiveBehaviourFilter.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CollectiveBehaviourFilter.

        Value of the parameter type as in the type attribute.  # noqa: E501

        :param value: The value of this CollectiveBehaviourFilter.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def list_of_ue_ind(self):
        """Gets the list_of_ue_ind of this CollectiveBehaviourFilter.

        Indicates whether request list of UE IDs that fulfill a collective behaviour within the area of interest. This attribute shall set to \"true\" if request the list of UE IDs, otherwise, set to \"false\". May only be present and sets to \"true\" if \"AfEvent\" sets to \"COLLECTIVE_BEHAVIOUR\".   # noqa: E501

        :return: The list_of_ue_ind of this CollectiveBehaviourFilter.
        :rtype: bool
        """
        return self._list_of_ue_ind

    @list_of_ue_ind.setter
    def list_of_ue_ind(self, list_of_ue_ind):
        """Sets the list_of_ue_ind of this CollectiveBehaviourFilter.

        Indicates whether request list of UE IDs that fulfill a collective behaviour within the area of interest. This attribute shall set to \"true\" if request the list of UE IDs, otherwise, set to \"false\". May only be present and sets to \"true\" if \"AfEvent\" sets to \"COLLECTIVE_BEHAVIOUR\".   # noqa: E501

        :param list_of_ue_ind: The list_of_ue_ind of this CollectiveBehaviourFilter.
        :type list_of_ue_ind: bool
        """

        self._list_of_ue_ind = list_of_ue_ind
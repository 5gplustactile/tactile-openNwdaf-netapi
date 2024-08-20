# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.geographical_coordinates import GeographicalCoordinates
from openapi_server import util

from openapi_server.models.geographical_coordinates import GeographicalCoordinates  # noqa: E501

class PointAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, point=None):  # noqa: E501
        """PointAllOf - a model defined in OpenAPI

        :param point: The point of this PointAllOf.  # noqa: E501
        :type point: GeographicalCoordinates
        """
        self.openapi_types = {
            'point': GeographicalCoordinates
        }

        self.attribute_map = {
            'point': 'point'
        }

        self._point = point

    @classmethod
    def from_dict(cls, dikt) -> 'PointAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Point_allOf of this PointAllOf.  # noqa: E501
        :rtype: PointAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def point(self):
        """Gets the point of this PointAllOf.


        :return: The point of this PointAllOf.
        :rtype: GeographicalCoordinates
        """
        return self._point

    @point.setter
    def point(self, point):
        """Sets the point of this PointAllOf.


        :param point: The point of this PointAllOf.
        :type point: GeographicalCoordinates
        """
        if point is None:
            raise ValueError("Invalid value for `point`, must not be `None`")  # noqa: E501

        self._point = point

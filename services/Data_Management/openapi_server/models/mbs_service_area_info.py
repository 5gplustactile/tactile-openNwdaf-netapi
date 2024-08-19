# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.mbs_service_area import MbsServiceArea
from openapi_server import util

from openapi_server.models.mbs_service_area import MbsServiceArea  # noqa: E501

class MbsServiceAreaInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, area_session_id=None, mbs_service_area=None):  # noqa: E501
        """MbsServiceAreaInfo - a model defined in OpenAPI

        :param area_session_id: The area_session_id of this MbsServiceAreaInfo.  # noqa: E501
        :type area_session_id: int
        :param mbs_service_area: The mbs_service_area of this MbsServiceAreaInfo.  # noqa: E501
        :type mbs_service_area: MbsServiceArea
        """
        self.openapi_types = {
            'area_session_id': int,
            'mbs_service_area': MbsServiceArea
        }

        self.attribute_map = {
            'area_session_id': 'areaSessionId',
            'mbs_service_area': 'mbsServiceArea'
        }

        self._area_session_id = area_session_id
        self._mbs_service_area = mbs_service_area

    @classmethod
    def from_dict(cls, dikt) -> 'MbsServiceAreaInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MbsServiceAreaInfo of this MbsServiceAreaInfo.  # noqa: E501
        :rtype: MbsServiceAreaInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def area_session_id(self):
        """Gets the area_session_id of this MbsServiceAreaInfo.

        Integer where the allowed values correspond to the value range of an unsigned 16-bit integer.  # noqa: E501

        :return: The area_session_id of this MbsServiceAreaInfo.
        :rtype: int
        """
        return self._area_session_id

    @area_session_id.setter
    def area_session_id(self, area_session_id):
        """Sets the area_session_id of this MbsServiceAreaInfo.

        Integer where the allowed values correspond to the value range of an unsigned 16-bit integer.  # noqa: E501

        :param area_session_id: The area_session_id of this MbsServiceAreaInfo.
        :type area_session_id: int
        """
        if area_session_id is None:
            raise ValueError("Invalid value for `area_session_id`, must not be `None`")  # noqa: E501
        if area_session_id is not None and area_session_id > 65535:  # noqa: E501
            raise ValueError("Invalid value for `area_session_id`, must be a value less than or equal to `65535`")  # noqa: E501
        if area_session_id is not None and area_session_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `area_session_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._area_session_id = area_session_id

    @property
    def mbs_service_area(self):
        """Gets the mbs_service_area of this MbsServiceAreaInfo.


        :return: The mbs_service_area of this MbsServiceAreaInfo.
        :rtype: MbsServiceArea
        """
        return self._mbs_service_area

    @mbs_service_area.setter
    def mbs_service_area(self, mbs_service_area):
        """Sets the mbs_service_area of this MbsServiceAreaInfo.


        :param mbs_service_area: The mbs_service_area of this MbsServiceAreaInfo.
        :type mbs_service_area: MbsServiceArea
        """
        if mbs_service_area is None:
            raise ValueError("Invalid value for `mbs_service_area`, must not be `None`")  # noqa: E501

        self._mbs_service_area = mbs_service_area
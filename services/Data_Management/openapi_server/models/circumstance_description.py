# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.network_area_info import NetworkAreaInfo
from openapi_server import util

from openapi_server.models.network_area_info import NetworkAreaInfo  # noqa: E501

class CircumstanceDescription(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, freq=None, tm=None, loc_area=None, vol=None):  # noqa: E501
        """CircumstanceDescription - a model defined in OpenAPI

        :param freq: The freq of this CircumstanceDescription.  # noqa: E501
        :type freq: float
        :param tm: The tm of this CircumstanceDescription.  # noqa: E501
        :type tm: datetime
        :param loc_area: The loc_area of this CircumstanceDescription.  # noqa: E501
        :type loc_area: NetworkAreaInfo
        :param vol: The vol of this CircumstanceDescription.  # noqa: E501
        :type vol: int
        """
        self.openapi_types = {
            'freq': float,
            'tm': datetime,
            'loc_area': NetworkAreaInfo,
            'vol': int
        }

        self.attribute_map = {
            'freq': 'freq',
            'tm': 'tm',
            'loc_area': 'locArea',
            'vol': 'vol'
        }

        self._freq = freq
        self._tm = tm
        self._loc_area = loc_area
        self._vol = vol

    @classmethod
    def from_dict(cls, dikt) -> 'CircumstanceDescription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CircumstanceDescription of this CircumstanceDescription.  # noqa: E501
        :rtype: CircumstanceDescription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def freq(self):
        """Gets the freq of this CircumstanceDescription.

        string with format 'float' as defined in OpenAPI.  # noqa: E501

        :return: The freq of this CircumstanceDescription.
        :rtype: float
        """
        return self._freq

    @freq.setter
    def freq(self, freq):
        """Sets the freq of this CircumstanceDescription.

        string with format 'float' as defined in OpenAPI.  # noqa: E501

        :param freq: The freq of this CircumstanceDescription.
        :type freq: float
        """

        self._freq = freq

    @property
    def tm(self):
        """Gets the tm of this CircumstanceDescription.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :return: The tm of this CircumstanceDescription.
        :rtype: datetime
        """
        return self._tm

    @tm.setter
    def tm(self, tm):
        """Sets the tm of this CircumstanceDescription.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :param tm: The tm of this CircumstanceDescription.
        :type tm: datetime
        """

        self._tm = tm

    @property
    def loc_area(self):
        """Gets the loc_area of this CircumstanceDescription.


        :return: The loc_area of this CircumstanceDescription.
        :rtype: NetworkAreaInfo
        """
        return self._loc_area

    @loc_area.setter
    def loc_area(self, loc_area):
        """Sets the loc_area of this CircumstanceDescription.


        :param loc_area: The loc_area of this CircumstanceDescription.
        :type loc_area: NetworkAreaInfo
        """

        self._loc_area = loc_area

    @property
    def vol(self):
        """Gets the vol of this CircumstanceDescription.

        Unsigned integer identifying a volume in units of bytes.  # noqa: E501

        :return: The vol of this CircumstanceDescription.
        :rtype: int
        """
        return self._vol

    @vol.setter
    def vol(self, vol):
        """Sets the vol of this CircumstanceDescription.

        Unsigned integer identifying a volume in units of bytes.  # noqa: E501

        :param vol: The vol of this CircumstanceDescription.
        :type vol: int
        """
        if vol is not None and vol < 0:  # noqa: E501
            raise ValueError("Invalid value for `vol`, must be a value greater than or equal to `0`")  # noqa: E501

        self._vol = vol

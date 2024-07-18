# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.matching_direction import MatchingDirection
from openapi_server.models.wlan_ordering_criterion import WlanOrderingCriterion
from openapi_server import util

from openapi_server.models.matching_direction import MatchingDirection  # noqa: E501
from openapi_server.models.wlan_ordering_criterion import WlanOrderingCriterion  # noqa: E501

class WlanPerformanceReq(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ss_ids=None, bss_ids=None, wlan_order_criter=None, order=None):  # noqa: E501
        """WlanPerformanceReq - a model defined in OpenAPI

        :param ss_ids: The ss_ids of this WlanPerformanceReq.  # noqa: E501
        :type ss_ids: List[str]
        :param bss_ids: The bss_ids of this WlanPerformanceReq.  # noqa: E501
        :type bss_ids: List[str]
        :param wlan_order_criter: The wlan_order_criter of this WlanPerformanceReq.  # noqa: E501
        :type wlan_order_criter: WlanOrderingCriterion
        :param order: The order of this WlanPerformanceReq.  # noqa: E501
        :type order: MatchingDirection
        """
        self.openapi_types = {
            'ss_ids': List[str],
            'bss_ids': List[str],
            'wlan_order_criter': WlanOrderingCriterion,
            'order': MatchingDirection
        }

        self.attribute_map = {
            'ss_ids': 'ssIds',
            'bss_ids': 'bssIds',
            'wlan_order_criter': 'wlanOrderCriter',
            'order': 'order'
        }

        self._ss_ids = ss_ids
        self._bss_ids = bss_ids
        self._wlan_order_criter = wlan_order_criter
        self._order = order

    @classmethod
    def from_dict(cls, dikt) -> 'WlanPerformanceReq':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The WlanPerformanceReq of this WlanPerformanceReq.  # noqa: E501
        :rtype: WlanPerformanceReq
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ss_ids(self):
        """Gets the ss_ids of this WlanPerformanceReq.


        :return: The ss_ids of this WlanPerformanceReq.
        :rtype: List[str]
        """
        return self._ss_ids

    @ss_ids.setter
    def ss_ids(self, ss_ids):
        """Sets the ss_ids of this WlanPerformanceReq.


        :param ss_ids: The ss_ids of this WlanPerformanceReq.
        :type ss_ids: List[str]
        """
        if ss_ids is not None and len(ss_ids) < 1:
            raise ValueError("Invalid value for `ss_ids`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ss_ids = ss_ids

    @property
    def bss_ids(self):
        """Gets the bss_ids of this WlanPerformanceReq.


        :return: The bss_ids of this WlanPerformanceReq.
        :rtype: List[str]
        """
        return self._bss_ids

    @bss_ids.setter
    def bss_ids(self, bss_ids):
        """Sets the bss_ids of this WlanPerformanceReq.


        :param bss_ids: The bss_ids of this WlanPerformanceReq.
        :type bss_ids: List[str]
        """
        if bss_ids is not None and len(bss_ids) < 1:
            raise ValueError("Invalid value for `bss_ids`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._bss_ids = bss_ids

    @property
    def wlan_order_criter(self):
        """Gets the wlan_order_criter of this WlanPerformanceReq.


        :return: The wlan_order_criter of this WlanPerformanceReq.
        :rtype: WlanOrderingCriterion
        """
        return self._wlan_order_criter

    @wlan_order_criter.setter
    def wlan_order_criter(self, wlan_order_criter):
        """Sets the wlan_order_criter of this WlanPerformanceReq.


        :param wlan_order_criter: The wlan_order_criter of this WlanPerformanceReq.
        :type wlan_order_criter: WlanOrderingCriterion
        """

        self._wlan_order_criter = wlan_order_criter

    @property
    def order(self):
        """Gets the order of this WlanPerformanceReq.


        :return: The order of this WlanPerformanceReq.
        :rtype: MatchingDirection
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this WlanPerformanceReq.


        :param order: The order of this WlanPerformanceReq.
        :type order: MatchingDirection
        """

        self._order = order

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.cm_info import CmInfo
from openapi_server import util

from openapi_server.models.cm_info import CmInfo  # noqa: E501

class CmInfoReport(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, old_cm_info_list=None, new_cm_info_list=None):  # noqa: E501
        """CmInfoReport - a model defined in OpenAPI

        :param old_cm_info_list: The old_cm_info_list of this CmInfoReport.  # noqa: E501
        :type old_cm_info_list: List[CmInfo]
        :param new_cm_info_list: The new_cm_info_list of this CmInfoReport.  # noqa: E501
        :type new_cm_info_list: List[CmInfo]
        """
        self.openapi_types = {
            'old_cm_info_list': List[CmInfo],
            'new_cm_info_list': List[CmInfo]
        }

        self.attribute_map = {
            'old_cm_info_list': 'oldCmInfoList',
            'new_cm_info_list': 'newCmInfoList'
        }

        self._old_cm_info_list = old_cm_info_list
        self._new_cm_info_list = new_cm_info_list

    @classmethod
    def from_dict(cls, dikt) -> 'CmInfoReport':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CmInfoReport of this CmInfoReport.  # noqa: E501
        :rtype: CmInfoReport
        """
        return util.deserialize_model(dikt, cls)

    @property
    def old_cm_info_list(self):
        """Gets the old_cm_info_list of this CmInfoReport.


        :return: The old_cm_info_list of this CmInfoReport.
        :rtype: List[CmInfo]
        """
        return self._old_cm_info_list

    @old_cm_info_list.setter
    def old_cm_info_list(self, old_cm_info_list):
        """Sets the old_cm_info_list of this CmInfoReport.


        :param old_cm_info_list: The old_cm_info_list of this CmInfoReport.
        :type old_cm_info_list: List[CmInfo]
        """
        if old_cm_info_list is not None and len(old_cm_info_list) > 2:
            raise ValueError("Invalid value for `old_cm_info_list`, number of items must be less than or equal to `2`")  # noqa: E501
        if old_cm_info_list is not None and len(old_cm_info_list) < 1:
            raise ValueError("Invalid value for `old_cm_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._old_cm_info_list = old_cm_info_list

    @property
    def new_cm_info_list(self):
        """Gets the new_cm_info_list of this CmInfoReport.


        :return: The new_cm_info_list of this CmInfoReport.
        :rtype: List[CmInfo]
        """
        return self._new_cm_info_list

    @new_cm_info_list.setter
    def new_cm_info_list(self, new_cm_info_list):
        """Sets the new_cm_info_list of this CmInfoReport.


        :param new_cm_info_list: The new_cm_info_list of this CmInfoReport.
        :type new_cm_info_list: List[CmInfo]
        """
        if new_cm_info_list is None:
            raise ValueError("Invalid value for `new_cm_info_list`, must not be `None`")  # noqa: E501
        if new_cm_info_list is not None and len(new_cm_info_list) > 2:
            raise ValueError("Invalid value for `new_cm_info_list`, number of items must be less than or equal to `2`")  # noqa: E501
        if new_cm_info_list is not None and len(new_cm_info_list) < 1:
            raise ValueError("Invalid value for `new_cm_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._new_cm_info_list = new_cm_info_list
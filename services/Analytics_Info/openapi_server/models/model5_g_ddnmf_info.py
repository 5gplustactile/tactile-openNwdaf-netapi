# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.plmn_id import PlmnId
from openapi_server import util

from openapi_server.models.plmn_id import PlmnId  # noqa: E501

class Model5GDdnmfInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, plmn_id=None):  # noqa: E501
        """Model5GDdnmfInfo - a model defined in OpenAPI

        :param plmn_id: The plmn_id of this Model5GDdnmfInfo.  # noqa: E501
        :type plmn_id: PlmnId
        """
        self.openapi_types = {
            'plmn_id': PlmnId
        }

        self.attribute_map = {
            'plmn_id': 'plmnId'
        }

        self._plmn_id = plmn_id

    @classmethod
    def from_dict(cls, dikt) -> 'Model5GDdnmfInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The 5GDdnmfInfo of this Model5GDdnmfInfo.  # noqa: E501
        :rtype: Model5GDdnmfInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plmn_id(self):
        """Gets the plmn_id of this Model5GDdnmfInfo.


        :return: The plmn_id of this Model5GDdnmfInfo.
        :rtype: PlmnId
        """
        return self._plmn_id

    @plmn_id.setter
    def plmn_id(self, plmn_id):
        """Sets the plmn_id of this Model5GDdnmfInfo.


        :param plmn_id: The plmn_id of this Model5GDdnmfInfo.
        :type plmn_id: PlmnId
        """
        if plmn_id is None:
            raise ValueError("Invalid value for `plmn_id`, must not be `None`")  # noqa: E501

        self._plmn_id = plmn_id

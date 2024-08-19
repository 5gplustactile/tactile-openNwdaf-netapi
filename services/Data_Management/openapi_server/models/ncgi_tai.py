# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ncgi import Ncgi
from openapi_server.models.tai import Tai
from openapi_server import util

from openapi_server.models.ncgi import Ncgi  # noqa: E501
from openapi_server.models.tai import Tai  # noqa: E501

class NcgiTai(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, tai=None, cell_list=None):  # noqa: E501
        """NcgiTai - a model defined in OpenAPI

        :param tai: The tai of this NcgiTai.  # noqa: E501
        :type tai: Tai
        :param cell_list: The cell_list of this NcgiTai.  # noqa: E501
        :type cell_list: List[Ncgi]
        """
        self.openapi_types = {
            'tai': Tai,
            'cell_list': List[Ncgi]
        }

        self.attribute_map = {
            'tai': 'tai',
            'cell_list': 'cellList'
        }

        self._tai = tai
        self._cell_list = cell_list

    @classmethod
    def from_dict(cls, dikt) -> 'NcgiTai':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NcgiTai of this NcgiTai.  # noqa: E501
        :rtype: NcgiTai
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tai(self):
        """Gets the tai of this NcgiTai.


        :return: The tai of this NcgiTai.
        :rtype: Tai
        """
        return self._tai

    @tai.setter
    def tai(self, tai):
        """Sets the tai of this NcgiTai.


        :param tai: The tai of this NcgiTai.
        :type tai: Tai
        """
        if tai is None:
            raise ValueError("Invalid value for `tai`, must not be `None`")  # noqa: E501

        self._tai = tai

    @property
    def cell_list(self):
        """Gets the cell_list of this NcgiTai.

        List of List of NR cell ids  # noqa: E501

        :return: The cell_list of this NcgiTai.
        :rtype: List[Ncgi]
        """
        return self._cell_list

    @cell_list.setter
    def cell_list(self, cell_list):
        """Sets the cell_list of this NcgiTai.

        List of List of NR cell ids  # noqa: E501

        :param cell_list: The cell_list of this NcgiTai.
        :type cell_list: List[Ncgi]
        """
        if cell_list is None:
            raise ValueError("Invalid value for `cell_list`, must not be `None`")  # noqa: E501
        if cell_list is not None and len(cell_list) < 1:
            raise ValueError("Invalid value for `cell_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._cell_list = cell_list
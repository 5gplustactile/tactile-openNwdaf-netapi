# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ext_snssai import ExtSnssai
from openapi_server.models.plmn_id import PlmnId
import re
from openapi_server import util

from openapi_server.models.ext_snssai import ExtSnssai  # noqa: E501
from openapi_server.models.plmn_id import PlmnId  # noqa: E501
import re  # noqa: E501

class PlmnSnssai(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, plmn_id=None, s_nssai_list=None, nid=None):  # noqa: E501
        """PlmnSnssai - a model defined in OpenAPI

        :param plmn_id: The plmn_id of this PlmnSnssai.  # noqa: E501
        :type plmn_id: PlmnId
        :param s_nssai_list: The s_nssai_list of this PlmnSnssai.  # noqa: E501
        :type s_nssai_list: List[ExtSnssai]
        :param nid: The nid of this PlmnSnssai.  # noqa: E501
        :type nid: str
        """
        self.openapi_types = {
            'plmn_id': PlmnId,
            's_nssai_list': List[ExtSnssai],
            'nid': str
        }

        self.attribute_map = {
            'plmn_id': 'plmnId',
            's_nssai_list': 'sNssaiList',
            'nid': 'nid'
        }

        self._plmn_id = plmn_id
        self._s_nssai_list = s_nssai_list
        self._nid = nid

    @classmethod
    def from_dict(cls, dikt) -> 'PlmnSnssai':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PlmnSnssai of this PlmnSnssai.  # noqa: E501
        :rtype: PlmnSnssai
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plmn_id(self):
        """Gets the plmn_id of this PlmnSnssai.


        :return: The plmn_id of this PlmnSnssai.
        :rtype: PlmnId
        """
        return self._plmn_id

    @plmn_id.setter
    def plmn_id(self, plmn_id):
        """Sets the plmn_id of this PlmnSnssai.


        :param plmn_id: The plmn_id of this PlmnSnssai.
        :type plmn_id: PlmnId
        """
        if plmn_id is None:
            raise ValueError("Invalid value for `plmn_id`, must not be `None`")  # noqa: E501

        self._plmn_id = plmn_id

    @property
    def s_nssai_list(self):
        """Gets the s_nssai_list of this PlmnSnssai.


        :return: The s_nssai_list of this PlmnSnssai.
        :rtype: List[ExtSnssai]
        """
        return self._s_nssai_list

    @s_nssai_list.setter
    def s_nssai_list(self, s_nssai_list):
        """Sets the s_nssai_list of this PlmnSnssai.


        :param s_nssai_list: The s_nssai_list of this PlmnSnssai.
        :type s_nssai_list: List[ExtSnssai]
        """
        if s_nssai_list is None:
            raise ValueError("Invalid value for `s_nssai_list`, must not be `None`")  # noqa: E501
        if s_nssai_list is not None and len(s_nssai_list) < 1:
            raise ValueError("Invalid value for `s_nssai_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._s_nssai_list = s_nssai_list

    @property
    def nid(self):
        """Gets the nid of this PlmnSnssai.

        This represents the Network Identifier, which together with a PLMN ID is used to identify an SNPN (see 3GPP TS 23.003 and 3GPP TS 23.501 clause 5.30.2.1).    # noqa: E501

        :return: The nid of this PlmnSnssai.
        :rtype: str
        """
        return self._nid

    @nid.setter
    def nid(self, nid):
        """Sets the nid of this PlmnSnssai.

        This represents the Network Identifier, which together with a PLMN ID is used to identify an SNPN (see 3GPP TS 23.003 and 3GPP TS 23.501 clause 5.30.2.1).    # noqa: E501

        :param nid: The nid of this PlmnSnssai.
        :type nid: str
        """
        if nid is not None and not re.search(r'^[A-Fa-f0-9]{11}$', nid):  # noqa: E501
            raise ValueError("Invalid value for `nid`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{11}$/`")  # noqa: E501

        self._nid = nid
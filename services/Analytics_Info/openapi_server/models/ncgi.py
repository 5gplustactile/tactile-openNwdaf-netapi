# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.plmn_id import PlmnId
import re
from openapi_server import util

from openapi_server.models.plmn_id import PlmnId  # noqa: E501
import re  # noqa: E501

class Ncgi(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, plmn_id=None, nr_cell_id=None, nid=None):  # noqa: E501
        """Ncgi - a model defined in OpenAPI

        :param plmn_id: The plmn_id of this Ncgi.  # noqa: E501
        :type plmn_id: PlmnId
        :param nr_cell_id: The nr_cell_id of this Ncgi.  # noqa: E501
        :type nr_cell_id: str
        :param nid: The nid of this Ncgi.  # noqa: E501
        :type nid: str
        """
        self.openapi_types = {
            'plmn_id': PlmnId,
            'nr_cell_id': str,
            'nid': str
        }

        self.attribute_map = {
            'plmn_id': 'plmnId',
            'nr_cell_id': 'nrCellId',
            'nid': 'nid'
        }

        self._plmn_id = plmn_id
        self._nr_cell_id = nr_cell_id
        self._nid = nid

    @classmethod
    def from_dict(cls, dikt) -> 'Ncgi':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Ncgi of this Ncgi.  # noqa: E501
        :rtype: Ncgi
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plmn_id(self):
        """Gets the plmn_id of this Ncgi.


        :return: The plmn_id of this Ncgi.
        :rtype: PlmnId
        """
        return self._plmn_id

    @plmn_id.setter
    def plmn_id(self, plmn_id):
        """Sets the plmn_id of this Ncgi.


        :param plmn_id: The plmn_id of this Ncgi.
        :type plmn_id: PlmnId
        """
        if plmn_id is None:
            raise ValueError("Invalid value for `plmn_id`, must not be `None`")  # noqa: E501

        self._plmn_id = plmn_id

    @property
    def nr_cell_id(self):
        """Gets the nr_cell_id of this Ncgi.

        36-bit string identifying an NR Cell Id as specified in clause 9.3.1.7 of 3GPP TS 38.413,  in hexadecimal representation. Each character in the string shall take a value of \"0\" to \"9\",  \"a\" to \"f\" or \"A\" to \"F\" and shall represent 4 bits. The most significant character  representing the 4 most significant bits of the Cell Id shall appear first in the string, and  the character representing the 4 least significant bit of the Cell Id shall appear last in the  string.    # noqa: E501

        :return: The nr_cell_id of this Ncgi.
        :rtype: str
        """
        return self._nr_cell_id

    @nr_cell_id.setter
    def nr_cell_id(self, nr_cell_id):
        """Sets the nr_cell_id of this Ncgi.

        36-bit string identifying an NR Cell Id as specified in clause 9.3.1.7 of 3GPP TS 38.413,  in hexadecimal representation. Each character in the string shall take a value of \"0\" to \"9\",  \"a\" to \"f\" or \"A\" to \"F\" and shall represent 4 bits. The most significant character  representing the 4 most significant bits of the Cell Id shall appear first in the string, and  the character representing the 4 least significant bit of the Cell Id shall appear last in the  string.    # noqa: E501

        :param nr_cell_id: The nr_cell_id of this Ncgi.
        :type nr_cell_id: str
        """
        if nr_cell_id is None:
            raise ValueError("Invalid value for `nr_cell_id`, must not be `None`")  # noqa: E501
        if nr_cell_id is not None and not re.search(r'^[A-Fa-f0-9]{9}$', nr_cell_id):  # noqa: E501
            raise ValueError("Invalid value for `nr_cell_id`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{9}$/`")  # noqa: E501

        self._nr_cell_id = nr_cell_id

    @property
    def nid(self):
        """Gets the nid of this Ncgi.

        This represents the Network Identifier, which together with a PLMN ID is used to identify an SNPN (see 3GPP TS 23.003 and 3GPP TS 23.501 clause 5.30.2.1).    # noqa: E501

        :return: The nid of this Ncgi.
        :rtype: str
        """
        return self._nid

    @nid.setter
    def nid(self, nid):
        """Sets the nid of this Ncgi.

        This represents the Network Identifier, which together with a PLMN ID is used to identify an SNPN (see 3GPP TS 23.003 and 3GPP TS 23.501 clause 5.30.2.1).    # noqa: E501

        :param nid: The nid of this Ncgi.
        :type nid: str
        """
        if nid is not None and not re.search(r'^[A-Fa-f0-9]{11}$', nid):  # noqa: E501
            raise ValueError("Invalid value for `nid`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{11}$/`")  # noqa: E501

        self._nid = nid

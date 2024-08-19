# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ext_snssai import ExtSnssai
from openapi_server import util

from openapi_server.models.ext_snssai import ExtSnssai  # noqa: E501

class SupportedSnssai(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, s_nssai=None, restriction_ind=False):  # noqa: E501
        """SupportedSnssai - a model defined in OpenAPI

        :param s_nssai: The s_nssai of this SupportedSnssai.  # noqa: E501
        :type s_nssai: ExtSnssai
        :param restriction_ind: The restriction_ind of this SupportedSnssai.  # noqa: E501
        :type restriction_ind: bool
        """
        self.openapi_types = {
            's_nssai': ExtSnssai,
            'restriction_ind': bool
        }

        self.attribute_map = {
            's_nssai': 'sNssai',
            'restriction_ind': 'restrictionInd'
        }

        self._s_nssai = s_nssai
        self._restriction_ind = restriction_ind

    @classmethod
    def from_dict(cls, dikt) -> 'SupportedSnssai':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SupportedSnssai of this SupportedSnssai.  # noqa: E501
        :rtype: SupportedSnssai
        """
        return util.deserialize_model(dikt, cls)

    @property
    def s_nssai(self):
        """Gets the s_nssai of this SupportedSnssai.


        :return: The s_nssai of this SupportedSnssai.
        :rtype: ExtSnssai
        """
        return self._s_nssai

    @s_nssai.setter
    def s_nssai(self, s_nssai):
        """Sets the s_nssai of this SupportedSnssai.


        :param s_nssai: The s_nssai of this SupportedSnssai.
        :type s_nssai: ExtSnssai
        """
        if s_nssai is None:
            raise ValueError("Invalid value for `s_nssai`, must not be `None`")  # noqa: E501

        self._s_nssai = s_nssai

    @property
    def restriction_ind(self):
        """Gets the restriction_ind of this SupportedSnssai.


        :return: The restriction_ind of this SupportedSnssai.
        :rtype: bool
        """
        return self._restriction_ind

    @restriction_ind.setter
    def restriction_ind(self, restriction_ind):
        """Sets the restriction_ind of this SupportedSnssai.


        :param restriction_ind: The restriction_ind of this SupportedSnssai.
        :type restriction_ind: bool
        """

        self._restriction_ind = restriction_ind
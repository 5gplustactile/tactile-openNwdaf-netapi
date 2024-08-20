# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class AmfCond(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, amf_set_id=None, amf_region_id=None):  # noqa: E501
        """AmfCond - a model defined in OpenAPI

        :param amf_set_id: The amf_set_id of this AmfCond.  # noqa: E501
        :type amf_set_id: str
        :param amf_region_id: The amf_region_id of this AmfCond.  # noqa: E501
        :type amf_region_id: str
        """
        self.openapi_types = {
            'amf_set_id': str,
            'amf_region_id': str
        }

        self.attribute_map = {
            'amf_set_id': 'amfSetId',
            'amf_region_id': 'amfRegionId'
        }

        self._amf_set_id = amf_set_id
        self._amf_region_id = amf_region_id

    @classmethod
    def from_dict(cls, dikt) -> 'AmfCond':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AmfCond of this AmfCond.  # noqa: E501
        :rtype: AmfCond
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amf_set_id(self):
        """Gets the amf_set_id of this AmfCond.

        String identifying the AMF Set ID (10 bits) as specified in clause 2.10.1 of 3GPP TS 23.003.  It is encoded as a string of 3 hexadecimal characters where the first character is limited to  values 0 to 3 (i.e. 10 bits).   # noqa: E501

        :return: The amf_set_id of this AmfCond.
        :rtype: str
        """
        return self._amf_set_id

    @amf_set_id.setter
    def amf_set_id(self, amf_set_id):
        """Sets the amf_set_id of this AmfCond.

        String identifying the AMF Set ID (10 bits) as specified in clause 2.10.1 of 3GPP TS 23.003.  It is encoded as a string of 3 hexadecimal characters where the first character is limited to  values 0 to 3 (i.e. 10 bits).   # noqa: E501

        :param amf_set_id: The amf_set_id of this AmfCond.
        :type amf_set_id: str
        """
        if amf_set_id is not None and not re.search(r'^[0-3][A-Fa-f0-9]{2}$', amf_set_id):  # noqa: E501
            raise ValueError("Invalid value for `amf_set_id`, must be a follow pattern or equal to `/^[0-3][A-Fa-f0-9]{2}$/`")  # noqa: E501

        self._amf_set_id = amf_set_id

    @property
    def amf_region_id(self):
        """Gets the amf_region_id of this AmfCond.

        String identifying the AMF Set ID (10 bits) as specified in clause 2.10.1 of 3GPP TS 23.003.  It is encoded as a string of 3 hexadecimal characters where the first character is limited to  values 0 to 3 (i.e. 10 bits)   # noqa: E501

        :return: The amf_region_id of this AmfCond.
        :rtype: str
        """
        return self._amf_region_id

    @amf_region_id.setter
    def amf_region_id(self, amf_region_id):
        """Sets the amf_region_id of this AmfCond.

        String identifying the AMF Set ID (10 bits) as specified in clause 2.10.1 of 3GPP TS 23.003.  It is encoded as a string of 3 hexadecimal characters where the first character is limited to  values 0 to 3 (i.e. 10 bits)   # noqa: E501

        :param amf_region_id: The amf_region_id of this AmfCond.
        :type amf_region_id: str
        """
        if amf_region_id is not None and not re.search(r'^[A-Fa-f0-9]{2}$', amf_region_id):  # noqa: E501
            raise ValueError("Invalid value for `amf_region_id`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{2}$/`")  # noqa: E501

        self._amf_region_id = amf_region_id

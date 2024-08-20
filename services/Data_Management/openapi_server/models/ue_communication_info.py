# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.communication_collection import CommunicationCollection
import re
from openapi_server import util

from openapi_server.models.communication_collection import CommunicationCollection  # noqa: E501
import re  # noqa: E501

class UeCommunicationInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, supi=None, inter_group_id=None, app_id=None, comms=None):  # noqa: E501
        """UeCommunicationInfo - a model defined in OpenAPI

        :param supi: The supi of this UeCommunicationInfo.  # noqa: E501
        :type supi: str
        :param inter_group_id: The inter_group_id of this UeCommunicationInfo.  # noqa: E501
        :type inter_group_id: str
        :param app_id: The app_id of this UeCommunicationInfo.  # noqa: E501
        :type app_id: str
        :param comms: The comms of this UeCommunicationInfo.  # noqa: E501
        :type comms: List[CommunicationCollection]
        """
        self.openapi_types = {
            'supi': str,
            'inter_group_id': str,
            'app_id': str,
            'comms': List[CommunicationCollection]
        }

        self.attribute_map = {
            'supi': 'supi',
            'inter_group_id': 'interGroupId',
            'app_id': 'appId',
            'comms': 'comms'
        }

        self._supi = supi
        self._inter_group_id = inter_group_id
        self._app_id = app_id
        self._comms = comms

    @classmethod
    def from_dict(cls, dikt) -> 'UeCommunicationInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UeCommunicationInfo of this UeCommunicationInfo.  # noqa: E501
        :rtype: UeCommunicationInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def supi(self):
        """Gets the supi of this UeCommunicationInfo.

        String identifying a Supi that shall contain either an IMSI, a network specific identifier, a Global Cable Identifier (GCI) or a Global Line Identifier (GLI) as specified in clause  2.2A of 3GPP TS 23.003. It shall be formatted as follows  - for an IMSI \"imsi-<imsi>\", where <imsi> shall be formatted according to clause 2.2    of 3GPP TS 23.003 that describes an IMSI.  - for a network specific identifier \"nai-<nai>, where <nai> shall be formatted    according to clause 28.7.2 of 3GPP TS 23.003 that describes an NAI.  - for a GCI \"gci-<gci>\", where <gci> shall be formatted according to clause 28.15.2    of 3GPP TS 23.003.  - for a GLI \"gli-<gli>\", where <gli> shall be formatted according to clause 28.16.2 of    3GPP TS 23.003.To enable that the value is used as part of an URI, the string shall    only contain characters allowed according to the \"lower-with-hyphen\" naming convention    defined in 3GPP TS 29.501.   # noqa: E501

        :return: The supi of this UeCommunicationInfo.
        :rtype: str
        """
        return self._supi

    @supi.setter
    def supi(self, supi):
        """Sets the supi of this UeCommunicationInfo.

        String identifying a Supi that shall contain either an IMSI, a network specific identifier, a Global Cable Identifier (GCI) or a Global Line Identifier (GLI) as specified in clause  2.2A of 3GPP TS 23.003. It shall be formatted as follows  - for an IMSI \"imsi-<imsi>\", where <imsi> shall be formatted according to clause 2.2    of 3GPP TS 23.003 that describes an IMSI.  - for a network specific identifier \"nai-<nai>, where <nai> shall be formatted    according to clause 28.7.2 of 3GPP TS 23.003 that describes an NAI.  - for a GCI \"gci-<gci>\", where <gci> shall be formatted according to clause 28.15.2    of 3GPP TS 23.003.  - for a GLI \"gli-<gli>\", where <gli> shall be formatted according to clause 28.16.2 of    3GPP TS 23.003.To enable that the value is used as part of an URI, the string shall    only contain characters allowed according to the \"lower-with-hyphen\" naming convention    defined in 3GPP TS 29.501.   # noqa: E501

        :param supi: The supi of this UeCommunicationInfo.
        :type supi: str
        """
        if supi is not None and not re.search(r'^(imsi-[0-9]{5,15}|nai-.+|gci-.+|gli-.+|.+)$', supi):  # noqa: E501
            raise ValueError("Invalid value for `supi`, must be a follow pattern or equal to `/^(imsi-[0-9]{5,15}|nai-.+|gci-.+|gli-.+|.+)$/`")  # noqa: E501

        self._supi = supi

    @property
    def inter_group_id(self):
        """Gets the inter_group_id of this UeCommunicationInfo.

        String identifying a group of devices network internal globally unique ID which identifies a set of IMSIs, as specified in clause 19.9 of 3GPP TS 23.003.    # noqa: E501

        :return: The inter_group_id of this UeCommunicationInfo.
        :rtype: str
        """
        return self._inter_group_id

    @inter_group_id.setter
    def inter_group_id(self, inter_group_id):
        """Sets the inter_group_id of this UeCommunicationInfo.

        String identifying a group of devices network internal globally unique ID which identifies a set of IMSIs, as specified in clause 19.9 of 3GPP TS 23.003.    # noqa: E501

        :param inter_group_id: The inter_group_id of this UeCommunicationInfo.
        :type inter_group_id: str
        """
        if inter_group_id is not None and not re.search(r'^[A-Fa-f0-9]{8}-[0-9]{3}-[0-9]{2,3}-([A-Fa-f0-9][A-Fa-f0-9]){1,10}$', inter_group_id):  # noqa: E501
            raise ValueError("Invalid value for `inter_group_id`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{8}-[0-9]{3}-[0-9]{2,3}-([A-Fa-f0-9][A-Fa-f0-9]){1,10}$/`")  # noqa: E501

        self._inter_group_id = inter_group_id

    @property
    def app_id(self):
        """Gets the app_id of this UeCommunicationInfo.

        String providing an application identifier.  # noqa: E501

        :return: The app_id of this UeCommunicationInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this UeCommunicationInfo.

        String providing an application identifier.  # noqa: E501

        :param app_id: The app_id of this UeCommunicationInfo.
        :type app_id: str
        """

        self._app_id = app_id

    @property
    def comms(self):
        """Gets the comms of this UeCommunicationInfo.


        :return: The comms of this UeCommunicationInfo.
        :rtype: List[CommunicationCollection]
        """
        return self._comms

    @comms.setter
    def comms(self, comms):
        """Sets the comms of this UeCommunicationInfo.


        :param comms: The comms of this UeCommunicationInfo.
        :type comms: List[CommunicationCollection]
        """
        if comms is None:
            raise ValueError("Invalid value for `comms`, must not be `None`")  # noqa: E501
        if comms is not None and len(comms) < 1:
            raise ValueError("Invalid value for `comms`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._comms = comms

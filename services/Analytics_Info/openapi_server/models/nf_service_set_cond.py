# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class NfServiceSetCond(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, nf_service_set_id=None, nf_set_id=None):  # noqa: E501
        """NfServiceSetCond - a model defined in OpenAPI

        :param nf_service_set_id: The nf_service_set_id of this NfServiceSetCond.  # noqa: E501
        :type nf_service_set_id: str
        :param nf_set_id: The nf_set_id of this NfServiceSetCond.  # noqa: E501
        :type nf_set_id: str
        """
        self.openapi_types = {
            'nf_service_set_id': str,
            'nf_set_id': str
        }

        self.attribute_map = {
            'nf_service_set_id': 'nfServiceSetId',
            'nf_set_id': 'nfSetId'
        }

        self._nf_service_set_id = nf_service_set_id
        self._nf_set_id = nf_set_id

    @classmethod
    def from_dict(cls, dikt) -> 'NfServiceSetCond':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NfServiceSetCond of this NfServiceSetCond.  # noqa: E501
        :rtype: NfServiceSetCond
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nf_service_set_id(self):
        """Gets the nf_service_set_id of this NfServiceSetCond.

        NF Service Set Identifier (see clause 28.12 of 3GPP TS 23.003) formatted as the following  string \"set<Set ID>.sn<Service Name>.nfi<NF Instance ID>.5gc.mnc<MNC>.mcc<MCC>\", or  \"set<SetID>.sn<ServiceName>.nfi<NFInstanceID>.5gc.nid<NID>.mnc<MNC>.mcc<MCC>\" with  <MCC> encoded as defined in clause 5.4.2 (\"Mcc\" data type definition)   <MNC> encoding the Mobile Network Code part of the PLMN, comprising 3 digits.    If there are only 2 significant digits in the MNC, one \"0\" digit shall be inserted    at the left side to fill the 3 digits coding of MNC.  Pattern: '^[0-9]{3}$' <NID> encoded as defined in clause 5.4.2 (\"Nid\" data type definition)  <NFInstanceId> encoded as defined in clause 5.3.2  <ServiceName> encoded as defined in 3GPP TS 29.510  <Set ID> encoded as a string of characters consisting of alphabetic    characters (A-Z and a-z), digits (0-9) and/or the hyphen (-) and that shall end    with either an alphabetic character or a digit.   # noqa: E501

        :return: The nf_service_set_id of this NfServiceSetCond.
        :rtype: str
        """
        return self._nf_service_set_id

    @nf_service_set_id.setter
    def nf_service_set_id(self, nf_service_set_id):
        """Sets the nf_service_set_id of this NfServiceSetCond.

        NF Service Set Identifier (see clause 28.12 of 3GPP TS 23.003) formatted as the following  string \"set<Set ID>.sn<Service Name>.nfi<NF Instance ID>.5gc.mnc<MNC>.mcc<MCC>\", or  \"set<SetID>.sn<ServiceName>.nfi<NFInstanceID>.5gc.nid<NID>.mnc<MNC>.mcc<MCC>\" with  <MCC> encoded as defined in clause 5.4.2 (\"Mcc\" data type definition)   <MNC> encoding the Mobile Network Code part of the PLMN, comprising 3 digits.    If there are only 2 significant digits in the MNC, one \"0\" digit shall be inserted    at the left side to fill the 3 digits coding of MNC.  Pattern: '^[0-9]{3}$' <NID> encoded as defined in clause 5.4.2 (\"Nid\" data type definition)  <NFInstanceId> encoded as defined in clause 5.3.2  <ServiceName> encoded as defined in 3GPP TS 29.510  <Set ID> encoded as a string of characters consisting of alphabetic    characters (A-Z and a-z), digits (0-9) and/or the hyphen (-) and that shall end    with either an alphabetic character or a digit.   # noqa: E501

        :param nf_service_set_id: The nf_service_set_id of this NfServiceSetCond.
        :type nf_service_set_id: str
        """
        if nf_service_set_id is None:
            raise ValueError("Invalid value for `nf_service_set_id`, must not be `None`")  # noqa: E501

        self._nf_service_set_id = nf_service_set_id

    @property
    def nf_set_id(self):
        """Gets the nf_set_id of this NfServiceSetCond.

        NF Set Identifier (see clause 28.12 of 3GPP TS 23.003), formatted as the following string \"set<Set ID>.<nftype>set.5gc.mnc<MNC>.mcc<MCC>\", or  \"set<SetID>.<NFType>set.5gc.nid<NID>.mnc<MNC>.mcc<MCC>\" with  <MCC> encoded as defined in clause 5.4.2 (\"Mcc\" data type definition)  <MNC> encoding the Mobile Network Code part of the PLMN, comprising 3 digits.    If there are only 2 significant digits in the MNC, one \"0\" digit shall be inserted    at the left side to fill the 3 digits coding of MNC.  Pattern: '^[0-9]{3}$' <NFType> encoded as a value defined in Table 6.1.6.3.3-1 of 3GPP TS 29.510 but    with lower case characters <Set ID> encoded as a string of characters consisting of    alphabetic characters (A-Z and a-z), digits (0-9) and/or the hyphen (-) and that    shall end with either an alphabetic character or a digit.    # noqa: E501

        :return: The nf_set_id of this NfServiceSetCond.
        :rtype: str
        """
        return self._nf_set_id

    @nf_set_id.setter
    def nf_set_id(self, nf_set_id):
        """Sets the nf_set_id of this NfServiceSetCond.

        NF Set Identifier (see clause 28.12 of 3GPP TS 23.003), formatted as the following string \"set<Set ID>.<nftype>set.5gc.mnc<MNC>.mcc<MCC>\", or  \"set<SetID>.<NFType>set.5gc.nid<NID>.mnc<MNC>.mcc<MCC>\" with  <MCC> encoded as defined in clause 5.4.2 (\"Mcc\" data type definition)  <MNC> encoding the Mobile Network Code part of the PLMN, comprising 3 digits.    If there are only 2 significant digits in the MNC, one \"0\" digit shall be inserted    at the left side to fill the 3 digits coding of MNC.  Pattern: '^[0-9]{3}$' <NFType> encoded as a value defined in Table 6.1.6.3.3-1 of 3GPP TS 29.510 but    with lower case characters <Set ID> encoded as a string of characters consisting of    alphabetic characters (A-Z and a-z), digits (0-9) and/or the hyphen (-) and that    shall end with either an alphabetic character or a digit.    # noqa: E501

        :param nf_set_id: The nf_set_id of this NfServiceSetCond.
        :type nf_set_id: str
        """

        self._nf_set_id = nf_set_id

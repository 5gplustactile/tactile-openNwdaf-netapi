# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.sac_event import SACEvent
import re
from openapi_server import util

from openapi_server.models.sac_event import SACEvent  # noqa: E501
import re  # noqa: E501

class SACEventSubscription(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, event=None, event_notify_uri=None, nf_id=None, notify_correlation_id=None, max_reports=None, expiry=None, supported_features=None):  # noqa: E501
        """SACEventSubscription - a model defined in OpenAPI

        :param event: The event of this SACEventSubscription.  # noqa: E501
        :type event: SACEvent
        :param event_notify_uri: The event_notify_uri of this SACEventSubscription.  # noqa: E501
        :type event_notify_uri: str
        :param nf_id: The nf_id of this SACEventSubscription.  # noqa: E501
        :type nf_id: str
        :param notify_correlation_id: The notify_correlation_id of this SACEventSubscription.  # noqa: E501
        :type notify_correlation_id: str
        :param max_reports: The max_reports of this SACEventSubscription.  # noqa: E501
        :type max_reports: int
        :param expiry: The expiry of this SACEventSubscription.  # noqa: E501
        :type expiry: datetime
        :param supported_features: The supported_features of this SACEventSubscription.  # noqa: E501
        :type supported_features: str
        """
        self.openapi_types = {
            'event': SACEvent,
            'event_notify_uri': str,
            'nf_id': str,
            'notify_correlation_id': str,
            'max_reports': int,
            'expiry': datetime,
            'supported_features': str
        }

        self.attribute_map = {
            'event': 'event',
            'event_notify_uri': 'eventNotifyUri',
            'nf_id': 'nfId',
            'notify_correlation_id': 'notifyCorrelationId',
            'max_reports': 'maxReports',
            'expiry': 'expiry',
            'supported_features': 'supportedFeatures'
        }

        self._event = event
        self._event_notify_uri = event_notify_uri
        self._nf_id = nf_id
        self._notify_correlation_id = notify_correlation_id
        self._max_reports = max_reports
        self._expiry = expiry
        self._supported_features = supported_features

    @classmethod
    def from_dict(cls, dikt) -> 'SACEventSubscription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SACEventSubscription of this SACEventSubscription.  # noqa: E501
        :rtype: SACEventSubscription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def event(self):
        """Gets the event of this SACEventSubscription.


        :return: The event of this SACEventSubscription.
        :rtype: SACEvent
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this SACEventSubscription.


        :param event: The event of this SACEventSubscription.
        :type event: SACEvent
        """
        if event is None:
            raise ValueError("Invalid value for `event`, must not be `None`")  # noqa: E501

        self._event = event

    @property
    def event_notify_uri(self):
        """Gets the event_notify_uri of this SACEventSubscription.

        String providing an URI formatted according to RFC 3986.  # noqa: E501

        :return: The event_notify_uri of this SACEventSubscription.
        :rtype: str
        """
        return self._event_notify_uri

    @event_notify_uri.setter
    def event_notify_uri(self, event_notify_uri):
        """Sets the event_notify_uri of this SACEventSubscription.

        String providing an URI formatted according to RFC 3986.  # noqa: E501

        :param event_notify_uri: The event_notify_uri of this SACEventSubscription.
        :type event_notify_uri: str
        """
        if event_notify_uri is None:
            raise ValueError("Invalid value for `event_notify_uri`, must not be `None`")  # noqa: E501

        self._event_notify_uri = event_notify_uri

    @property
    def nf_id(self):
        """Gets the nf_id of this SACEventSubscription.

        String uniquely identifying a NF instance. The format of the NF Instance ID shall be a  Universally Unique Identifier (UUID) version 4, as described in IETF RFC 4122.    # noqa: E501

        :return: The nf_id of this SACEventSubscription.
        :rtype: str
        """
        return self._nf_id

    @nf_id.setter
    def nf_id(self, nf_id):
        """Sets the nf_id of this SACEventSubscription.

        String uniquely identifying a NF instance. The format of the NF Instance ID shall be a  Universally Unique Identifier (UUID) version 4, as described in IETF RFC 4122.    # noqa: E501

        :param nf_id: The nf_id of this SACEventSubscription.
        :type nf_id: str
        """
        if nf_id is None:
            raise ValueError("Invalid value for `nf_id`, must not be `None`")  # noqa: E501

        self._nf_id = nf_id

    @property
    def notify_correlation_id(self):
        """Gets the notify_correlation_id of this SACEventSubscription.


        :return: The notify_correlation_id of this SACEventSubscription.
        :rtype: str
        """
        return self._notify_correlation_id

    @notify_correlation_id.setter
    def notify_correlation_id(self, notify_correlation_id):
        """Sets the notify_correlation_id of this SACEventSubscription.


        :param notify_correlation_id: The notify_correlation_id of this SACEventSubscription.
        :type notify_correlation_id: str
        """

        self._notify_correlation_id = notify_correlation_id

    @property
    def max_reports(self):
        """Gets the max_reports of this SACEventSubscription.


        :return: The max_reports of this SACEventSubscription.
        :rtype: int
        """
        return self._max_reports

    @max_reports.setter
    def max_reports(self, max_reports):
        """Sets the max_reports of this SACEventSubscription.


        :param max_reports: The max_reports of this SACEventSubscription.
        :type max_reports: int
        """

        self._max_reports = max_reports

    @property
    def expiry(self):
        """Gets the expiry of this SACEventSubscription.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :return: The expiry of this SACEventSubscription.
        :rtype: datetime
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this SACEventSubscription.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :param expiry: The expiry of this SACEventSubscription.
        :type expiry: datetime
        """

        self._expiry = expiry

    @property
    def supported_features(self):
        """Gets the supported_features of this SACEventSubscription.

        A string used to indicate the features supported by an API that is used as defined in clause  6.6 in 3GPP TS 29.500. The string shall contain a bitmask indicating supported features in  hexadecimal representation Each character in the string shall take a value of \"0\" to \"9\",  \"a\" to \"f\" or \"A\" to \"F\" and shall represent the support of 4 features as described in  table 5.2.2-3. The most significant character representing the highest-numbered features shall  appear first in the string, and the character representing features 1 to 4 shall appear last  in the string. The list of features and their numbering (starting with 1) are defined  separately for each API. If the string contains a lower number of characters than there are  defined features for an API, all features that would be represented by characters that are not  present in the string are not supported.   # noqa: E501

        :return: The supported_features of this SACEventSubscription.
        :rtype: str
        """
        return self._supported_features

    @supported_features.setter
    def supported_features(self, supported_features):
        """Sets the supported_features of this SACEventSubscription.

        A string used to indicate the features supported by an API that is used as defined in clause  6.6 in 3GPP TS 29.500. The string shall contain a bitmask indicating supported features in  hexadecimal representation Each character in the string shall take a value of \"0\" to \"9\",  \"a\" to \"f\" or \"A\" to \"F\" and shall represent the support of 4 features as described in  table 5.2.2-3. The most significant character representing the highest-numbered features shall  appear first in the string, and the character representing features 1 to 4 shall appear last  in the string. The list of features and their numbering (starting with 1) are defined  separately for each API. If the string contains a lower number of characters than there are  defined features for an API, all features that would be represented by characters that are not  present in the string are not supported.   # noqa: E501

        :param supported_features: The supported_features of this SACEventSubscription.
        :type supported_features: str
        """
        if supported_features is not None and not re.search(r'^[A-Fa-f0-9]*$', supported_features):  # noqa: E501
            raise ValueError("Invalid value for `supported_features`, must be a follow pattern or equal to `/^[A-Fa-f0-9]*$/`")  # noqa: E501

        self._supported_features = supported_features

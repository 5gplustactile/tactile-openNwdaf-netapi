# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.nef_event_notification import NefEventNotification
from openapi_server.models.nef_event_subs import NefEventSubs
from openapi_server.models.reporting_information import ReportingInformation
import re
from openapi_server import util

from openapi_server.models.nef_event_notification import NefEventNotification  # noqa: E501
from openapi_server.models.nef_event_subs import NefEventSubs  # noqa: E501
from openapi_server.models.reporting_information import ReportingInformation  # noqa: E501
import re  # noqa: E501

class NefEventExposureSubsc(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data_acc_prof_id=None, events_subs=None, events_rep_info=None, notif_uri=None, notif_id=None, event_notifs=None, supp_feat=None):  # noqa: E501
        """NefEventExposureSubsc - a model defined in OpenAPI

        :param data_acc_prof_id: The data_acc_prof_id of this NefEventExposureSubsc.  # noqa: E501
        :type data_acc_prof_id: str
        :param events_subs: The events_subs of this NefEventExposureSubsc.  # noqa: E501
        :type events_subs: List[NefEventSubs]
        :param events_rep_info: The events_rep_info of this NefEventExposureSubsc.  # noqa: E501
        :type events_rep_info: ReportingInformation
        :param notif_uri: The notif_uri of this NefEventExposureSubsc.  # noqa: E501
        :type notif_uri: str
        :param notif_id: The notif_id of this NefEventExposureSubsc.  # noqa: E501
        :type notif_id: str
        :param event_notifs: The event_notifs of this NefEventExposureSubsc.  # noqa: E501
        :type event_notifs: List[NefEventNotification]
        :param supp_feat: The supp_feat of this NefEventExposureSubsc.  # noqa: E501
        :type supp_feat: str
        """
        self.openapi_types = {
            'data_acc_prof_id': str,
            'events_subs': List[NefEventSubs],
            'events_rep_info': ReportingInformation,
            'notif_uri': str,
            'notif_id': str,
            'event_notifs': List[NefEventNotification],
            'supp_feat': str
        }

        self.attribute_map = {
            'data_acc_prof_id': 'dataAccProfId',
            'events_subs': 'eventsSubs',
            'events_rep_info': 'eventsRepInfo',
            'notif_uri': 'notifUri',
            'notif_id': 'notifId',
            'event_notifs': 'eventNotifs',
            'supp_feat': 'suppFeat'
        }

        self._data_acc_prof_id = data_acc_prof_id
        self._events_subs = events_subs
        self._events_rep_info = events_rep_info
        self._notif_uri = notif_uri
        self._notif_id = notif_id
        self._event_notifs = event_notifs
        self._supp_feat = supp_feat

    @classmethod
    def from_dict(cls, dikt) -> 'NefEventExposureSubsc':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NefEventExposureSubsc of this NefEventExposureSubsc.  # noqa: E501
        :rtype: NefEventExposureSubsc
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data_acc_prof_id(self):
        """Gets the data_acc_prof_id of this NefEventExposureSubsc.


        :return: The data_acc_prof_id of this NefEventExposureSubsc.
        :rtype: str
        """
        return self._data_acc_prof_id

    @data_acc_prof_id.setter
    def data_acc_prof_id(self, data_acc_prof_id):
        """Sets the data_acc_prof_id of this NefEventExposureSubsc.


        :param data_acc_prof_id: The data_acc_prof_id of this NefEventExposureSubsc.
        :type data_acc_prof_id: str
        """

        self._data_acc_prof_id = data_acc_prof_id

    @property
    def events_subs(self):
        """Gets the events_subs of this NefEventExposureSubsc.


        :return: The events_subs of this NefEventExposureSubsc.
        :rtype: List[NefEventSubs]
        """
        return self._events_subs

    @events_subs.setter
    def events_subs(self, events_subs):
        """Sets the events_subs of this NefEventExposureSubsc.


        :param events_subs: The events_subs of this NefEventExposureSubsc.
        :type events_subs: List[NefEventSubs]
        """
        if events_subs is None:
            raise ValueError("Invalid value for `events_subs`, must not be `None`")  # noqa: E501
        if events_subs is not None and len(events_subs) < 1:
            raise ValueError("Invalid value for `events_subs`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._events_subs = events_subs

    @property
    def events_rep_info(self):
        """Gets the events_rep_info of this NefEventExposureSubsc.


        :return: The events_rep_info of this NefEventExposureSubsc.
        :rtype: ReportingInformation
        """
        return self._events_rep_info

    @events_rep_info.setter
    def events_rep_info(self, events_rep_info):
        """Sets the events_rep_info of this NefEventExposureSubsc.


        :param events_rep_info: The events_rep_info of this NefEventExposureSubsc.
        :type events_rep_info: ReportingInformation
        """

        self._events_rep_info = events_rep_info

    @property
    def notif_uri(self):
        """Gets the notif_uri of this NefEventExposureSubsc.

        String providing an URI formatted according to RFC 3986.  # noqa: E501

        :return: The notif_uri of this NefEventExposureSubsc.
        :rtype: str
        """
        return self._notif_uri

    @notif_uri.setter
    def notif_uri(self, notif_uri):
        """Sets the notif_uri of this NefEventExposureSubsc.

        String providing an URI formatted according to RFC 3986.  # noqa: E501

        :param notif_uri: The notif_uri of this NefEventExposureSubsc.
        :type notif_uri: str
        """
        if notif_uri is None:
            raise ValueError("Invalid value for `notif_uri`, must not be `None`")  # noqa: E501

        self._notif_uri = notif_uri

    @property
    def notif_id(self):
        """Gets the notif_id of this NefEventExposureSubsc.


        :return: The notif_id of this NefEventExposureSubsc.
        :rtype: str
        """
        return self._notif_id

    @notif_id.setter
    def notif_id(self, notif_id):
        """Sets the notif_id of this NefEventExposureSubsc.


        :param notif_id: The notif_id of this NefEventExposureSubsc.
        :type notif_id: str
        """
        if notif_id is None:
            raise ValueError("Invalid value for `notif_id`, must not be `None`")  # noqa: E501

        self._notif_id = notif_id

    @property
    def event_notifs(self):
        """Gets the event_notifs of this NefEventExposureSubsc.


        :return: The event_notifs of this NefEventExposureSubsc.
        :rtype: List[NefEventNotification]
        """
        return self._event_notifs

    @event_notifs.setter
    def event_notifs(self, event_notifs):
        """Sets the event_notifs of this NefEventExposureSubsc.


        :param event_notifs: The event_notifs of this NefEventExposureSubsc.
        :type event_notifs: List[NefEventNotification]
        """
        if event_notifs is not None and len(event_notifs) < 1:
            raise ValueError("Invalid value for `event_notifs`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._event_notifs = event_notifs

    @property
    def supp_feat(self):
        """Gets the supp_feat of this NefEventExposureSubsc.

        A string used to indicate the features supported by an API that is used as defined in clause  6.6 in 3GPP TS 29.500. The string shall contain a bitmask indicating supported features in  hexadecimal representation Each character in the string shall take a value of \"0\" to \"9\",  \"a\" to \"f\" or \"A\" to \"F\" and shall represent the support of 4 features as described in  table 5.2.2-3. The most significant character representing the highest-numbered features shall  appear first in the string, and the character representing features 1 to 4 shall appear last  in the string. The list of features and their numbering (starting with 1) are defined  separately for each API. If the string contains a lower number of characters than there are  defined features for an API, all features that would be represented by characters that are not  present in the string are not supported.   # noqa: E501

        :return: The supp_feat of this NefEventExposureSubsc.
        :rtype: str
        """
        return self._supp_feat

    @supp_feat.setter
    def supp_feat(self, supp_feat):
        """Sets the supp_feat of this NefEventExposureSubsc.

        A string used to indicate the features supported by an API that is used as defined in clause  6.6 in 3GPP TS 29.500. The string shall contain a bitmask indicating supported features in  hexadecimal representation Each character in the string shall take a value of \"0\" to \"9\",  \"a\" to \"f\" or \"A\" to \"F\" and shall represent the support of 4 features as described in  table 5.2.2-3. The most significant character representing the highest-numbered features shall  appear first in the string, and the character representing features 1 to 4 shall appear last  in the string. The list of features and their numbering (starting with 1) are defined  separately for each API. If the string contains a lower number of characters than there are  defined features for an API, all features that would be represented by characters that are not  present in the string are not supported.   # noqa: E501

        :param supp_feat: The supp_feat of this NefEventExposureSubsc.
        :type supp_feat: str
        """
        if supp_feat is not None and not re.search(r'^[A-Fa-f0-9]*$', supp_feat):  # noqa: E501
            raise ValueError("Invalid value for `supp_feat`, must be a follow pattern or equal to `/^[A-Fa-f0-9]*$/`")  # noqa: E501

        self._supp_feat = supp_feat

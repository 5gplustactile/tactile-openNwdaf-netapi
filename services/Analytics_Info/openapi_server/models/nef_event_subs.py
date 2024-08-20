# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.nef_event import NefEvent
from openapi_server.models.nef_event_filter import NefEventFilter
from openapi_server import util

from openapi_server.models.nef_event import NefEvent  # noqa: E501
from openapi_server.models.nef_event_filter import NefEventFilter  # noqa: E501

class NefEventSubs(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, event=None, event_filter=None):  # noqa: E501
        """NefEventSubs - a model defined in OpenAPI

        :param event: The event of this NefEventSubs.  # noqa: E501
        :type event: NefEvent
        :param event_filter: The event_filter of this NefEventSubs.  # noqa: E501
        :type event_filter: NefEventFilter
        """
        self.openapi_types = {
            'event': NefEvent,
            'event_filter': NefEventFilter
        }

        self.attribute_map = {
            'event': 'event',
            'event_filter': 'eventFilter'
        }

        self._event = event
        self._event_filter = event_filter

    @classmethod
    def from_dict(cls, dikt) -> 'NefEventSubs':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NefEventSubs of this NefEventSubs.  # noqa: E501
        :rtype: NefEventSubs
        """
        return util.deserialize_model(dikt, cls)

    @property
    def event(self):
        """Gets the event of this NefEventSubs.


        :return: The event of this NefEventSubs.
        :rtype: NefEvent
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this NefEventSubs.


        :param event: The event of this NefEventSubs.
        :type event: NefEvent
        """
        if event is None:
            raise ValueError("Invalid value for `event`, must not be `None`")  # noqa: E501

        self._event = event

    @property
    def event_filter(self):
        """Gets the event_filter of this NefEventSubs.


        :return: The event_filter of this NefEventSubs.
        :rtype: NefEventFilter
        """
        return self._event_filter

    @event_filter.setter
    def event_filter(self, event_filter):
        """Sets the event_filter of this NefEventSubs.


        :param event_filter: The event_filter of this NefEventSubs.
        :type event_filter: NefEventFilter
        """

        self._event_filter = event_filter

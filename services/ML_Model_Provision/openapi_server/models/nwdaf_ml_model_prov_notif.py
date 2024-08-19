# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ml_event_notif import MLEventNotif
from openapi_server import util

from openapi_server.models.ml_event_notif import MLEventNotif  # noqa: E501

class NwdafMLModelProvNotif(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, event_notifs=None, subscription_id=None):  # noqa: E501
        """NwdafMLModelProvNotif - a model defined in OpenAPI

        :param event_notifs: The event_notifs of this NwdafMLModelProvNotif.  # noqa: E501
        :type event_notifs: List[MLEventNotif]
        :param subscription_id: The subscription_id of this NwdafMLModelProvNotif.  # noqa: E501
        :type subscription_id: str
        """
        self.openapi_types = {
            'event_notifs': List[MLEventNotif],
            'subscription_id': str
        }

        self.attribute_map = {
            'event_notifs': 'eventNotifs',
            'subscription_id': 'subscriptionId'
        }

        self._event_notifs = event_notifs
        self._subscription_id = subscription_id

    @classmethod
    def from_dict(cls, dikt) -> 'NwdafMLModelProvNotif':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NwdafMLModelProvNotif of this NwdafMLModelProvNotif.  # noqa: E501
        :rtype: NwdafMLModelProvNotif
        """
        return util.deserialize_model(dikt, cls)

    @property
    def event_notifs(self):
        """Gets the event_notifs of this NwdafMLModelProvNotif.

        Notifications about Individual Events.  # noqa: E501

        :return: The event_notifs of this NwdafMLModelProvNotif.
        :rtype: List[MLEventNotif]
        """
        return self._event_notifs

    @event_notifs.setter
    def event_notifs(self, event_notifs):
        """Sets the event_notifs of this NwdafMLModelProvNotif.

        Notifications about Individual Events.  # noqa: E501

        :param event_notifs: The event_notifs of this NwdafMLModelProvNotif.
        :type event_notifs: List[MLEventNotif]
        """
        if event_notifs is None:
            raise ValueError("Invalid value for `event_notifs`, must not be `None`")  # noqa: E501
        if event_notifs is not None and len(event_notifs) < 1:
            raise ValueError("Invalid value for `event_notifs`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._event_notifs = event_notifs

    @property
    def subscription_id(self):
        """Gets the subscription_id of this NwdafMLModelProvNotif.

        String identifying a subscription to the Nnwdaf_MLModelProvision Service.  # noqa: E501

        :return: The subscription_id of this NwdafMLModelProvNotif.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this NwdafMLModelProvNotif.

        String identifying a subscription to the Nnwdaf_MLModelProvision Service.  # noqa: E501

        :param subscription_id: The subscription_id of this NwdafMLModelProvNotif.
        :type subscription_id: str
        """
        if subscription_id is None:
            raise ValueError("Invalid value for `subscription_id`, must not be `None`")  # noqa: E501

        self._subscription_id = subscription_id
# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.af_event_notification import AfEventNotification
from openapi_server import util

from openapi_server.models.af_event_notification import AfEventNotification  # noqa: E501

class AfEventExposureNotif(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, notif_id=None, event_notifs=None):  # noqa: E501
        """AfEventExposureNotif - a model defined in OpenAPI

        :param notif_id: The notif_id of this AfEventExposureNotif.  # noqa: E501
        :type notif_id: str
        :param event_notifs: The event_notifs of this AfEventExposureNotif.  # noqa: E501
        :type event_notifs: List[AfEventNotification]
        """
        self.openapi_types = {
            'notif_id': str,
            'event_notifs': List[AfEventNotification]
        }

        self.attribute_map = {
            'notif_id': 'notifId',
            'event_notifs': 'eventNotifs'
        }

        self._notif_id = notif_id
        self._event_notifs = event_notifs

    @classmethod
    def from_dict(cls, dikt) -> 'AfEventExposureNotif':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AfEventExposureNotif of this AfEventExposureNotif.  # noqa: E501
        :rtype: AfEventExposureNotif
        """
        return util.deserialize_model(dikt, cls)

    @property
    def notif_id(self):
        """Gets the notif_id of this AfEventExposureNotif.


        :return: The notif_id of this AfEventExposureNotif.
        :rtype: str
        """
        return self._notif_id

    @notif_id.setter
    def notif_id(self, notif_id):
        """Sets the notif_id of this AfEventExposureNotif.


        :param notif_id: The notif_id of this AfEventExposureNotif.
        :type notif_id: str
        """
        if notif_id is None:
            raise ValueError("Invalid value for `notif_id`, must not be `None`")  # noqa: E501

        self._notif_id = notif_id

    @property
    def event_notifs(self):
        """Gets the event_notifs of this AfEventExposureNotif.


        :return: The event_notifs of this AfEventExposureNotif.
        :rtype: List[AfEventNotification]
        """
        return self._event_notifs

    @event_notifs.setter
    def event_notifs(self, event_notifs):
        """Sets the event_notifs of this AfEventExposureNotif.


        :param event_notifs: The event_notifs of this AfEventExposureNotif.
        :type event_notifs: List[AfEventNotification]
        """
        if event_notifs is None:
            raise ValueError("Invalid value for `event_notifs`, must not be `None`")  # noqa: E501
        if event_notifs is not None and len(event_notifs) < 1:
            raise ValueError("Invalid value for `event_notifs`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._event_notifs = event_notifs
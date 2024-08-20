# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.amf_event_subscription_info import AmfEventSubscriptionInfo
from openapi_server import util

from openapi_server.models.amf_event_subscription_info import AmfEventSubscriptionInfo  # noqa: E501

class AmfEventSubsSyncInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, subscription_list=None):  # noqa: E501
        """AmfEventSubsSyncInfo - a model defined in OpenAPI

        :param subscription_list: The subscription_list of this AmfEventSubsSyncInfo.  # noqa: E501
        :type subscription_list: List[AmfEventSubscriptionInfo]
        """
        self.openapi_types = {
            'subscription_list': List[AmfEventSubscriptionInfo]
        }

        self.attribute_map = {
            'subscription_list': 'subscriptionList'
        }

        self._subscription_list = subscription_list

    @classmethod
    def from_dict(cls, dikt) -> 'AmfEventSubsSyncInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AmfEventSubsSyncInfo of this AmfEventSubsSyncInfo.  # noqa: E501
        :rtype: AmfEventSubsSyncInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def subscription_list(self):
        """Gets the subscription_list of this AmfEventSubsSyncInfo.


        :return: The subscription_list of this AmfEventSubsSyncInfo.
        :rtype: List[AmfEventSubscriptionInfo]
        """
        return self._subscription_list

    @subscription_list.setter
    def subscription_list(self, subscription_list):
        """Sets the subscription_list of this AmfEventSubsSyncInfo.


        :param subscription_list: The subscription_list of this AmfEventSubsSyncInfo.
        :type subscription_list: List[AmfEventSubscriptionInfo]
        """
        if subscription_list is None:
            raise ValueError("Invalid value for `subscription_list`, must not be `None`")  # noqa: E501
        if subscription_list is not None and len(subscription_list) < 1:
            raise ValueError("Invalid value for `subscription_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._subscription_list = subscription_list

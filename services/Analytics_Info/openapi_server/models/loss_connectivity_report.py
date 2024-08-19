# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.loss_of_connectivity_reason import LossOfConnectivityReason
from openapi_server import util

from openapi_server.models.loss_of_connectivity_reason import LossOfConnectivityReason  # noqa: E501

class LossConnectivityReport(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, loss_of_connect_reason=None):  # noqa: E501
        """LossConnectivityReport - a model defined in OpenAPI

        :param loss_of_connect_reason: The loss_of_connect_reason of this LossConnectivityReport.  # noqa: E501
        :type loss_of_connect_reason: LossOfConnectivityReason
        """
        self.openapi_types = {
            'loss_of_connect_reason': LossOfConnectivityReason
        }

        self.attribute_map = {
            'loss_of_connect_reason': 'lossOfConnectReason'
        }

        self._loss_of_connect_reason = loss_of_connect_reason

    @classmethod
    def from_dict(cls, dikt) -> 'LossConnectivityReport':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LossConnectivityReport of this LossConnectivityReport.  # noqa: E501
        :rtype: LossConnectivityReport
        """
        return util.deserialize_model(dikt, cls)

    @property
    def loss_of_connect_reason(self):
        """Gets the loss_of_connect_reason of this LossConnectivityReport.


        :return: The loss_of_connect_reason of this LossConnectivityReport.
        :rtype: LossOfConnectivityReason
        """
        return self._loss_of_connect_reason

    @loss_of_connect_reason.setter
    def loss_of_connect_reason(self, loss_of_connect_reason):
        """Sets the loss_of_connect_reason of this LossConnectivityReport.


        :param loss_of_connect_reason: The loss_of_connect_reason of this LossConnectivityReport.
        :type loss_of_connect_reason: LossOfConnectivityReason
        """
        if loss_of_connect_reason is None:
            raise ValueError("Invalid value for `loss_of_connect_reason`, must not be `None`")  # noqa: E501

        self._loss_of_connect_reason = loss_of_connect_reason
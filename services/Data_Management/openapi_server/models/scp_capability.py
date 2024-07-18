# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ScpCapability(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self):  # noqa: E501
        """ScpCapability - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'ScpCapability':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ScpCapability of this ScpCapability.  # noqa: E501
        :rtype: ScpCapability
        """
        return util.deserialize_model(dikt, cls)

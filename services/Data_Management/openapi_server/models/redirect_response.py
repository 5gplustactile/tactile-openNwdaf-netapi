# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class RedirectResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cause=None, target_scp=None, target_sepp=None):  # noqa: E501
        """RedirectResponse - a model defined in OpenAPI

        :param cause: The cause of this RedirectResponse.  # noqa: E501
        :type cause: str
        :param target_scp: The target_scp of this RedirectResponse.  # noqa: E501
        :type target_scp: str
        :param target_sepp: The target_sepp of this RedirectResponse.  # noqa: E501
        :type target_sepp: str
        """
        self.openapi_types = {
            'cause': str,
            'target_scp': str,
            'target_sepp': str
        }

        self.attribute_map = {
            'cause': 'cause',
            'target_scp': 'targetScp',
            'target_sepp': 'targetSepp'
        }

        self._cause = cause
        self._target_scp = target_scp
        self._target_sepp = target_sepp

    @classmethod
    def from_dict(cls, dikt) -> 'RedirectResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RedirectResponse of this RedirectResponse.  # noqa: E501
        :rtype: RedirectResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cause(self):
        """Gets the cause of this RedirectResponse.


        :return: The cause of this RedirectResponse.
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """Sets the cause of this RedirectResponse.


        :param cause: The cause of this RedirectResponse.
        :type cause: str
        """

        self._cause = cause

    @property
    def target_scp(self):
        """Gets the target_scp of this RedirectResponse.

        String providing an URI formatted according to RFC 3986.  # noqa: E501

        :return: The target_scp of this RedirectResponse.
        :rtype: str
        """
        return self._target_scp

    @target_scp.setter
    def target_scp(self, target_scp):
        """Sets the target_scp of this RedirectResponse.

        String providing an URI formatted according to RFC 3986.  # noqa: E501

        :param target_scp: The target_scp of this RedirectResponse.
        :type target_scp: str
        """

        self._target_scp = target_scp

    @property
    def target_sepp(self):
        """Gets the target_sepp of this RedirectResponse.

        String providing an URI formatted according to RFC 3986.  # noqa: E501

        :return: The target_sepp of this RedirectResponse.
        :rtype: str
        """
        return self._target_sepp

    @target_sepp.setter
    def target_sepp(self, target_sepp):
        """Sets the target_sepp of this RedirectResponse.

        String providing an URI formatted according to RFC 3986.  # noqa: E501

        :param target_sepp: The target_sepp of this RedirectResponse.
        :type target_sepp: str
        """

        self._target_sepp = target_sepp

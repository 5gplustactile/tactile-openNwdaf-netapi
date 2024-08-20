# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.mbs_service_area_info import MbsServiceAreaInfo
from openapi_server.models.mbs_session_id import MbsSessionId
from openapi_server import util

from openapi_server.models.mbs_service_area_info import MbsServiceAreaInfo  # noqa: E501
from openapi_server.models.mbs_session_id import MbsSessionId  # noqa: E501

class MbsSession(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, mbs_session_id=None, mbs_area_sessions=None):  # noqa: E501
        """MbsSession - a model defined in OpenAPI

        :param mbs_session_id: The mbs_session_id of this MbsSession.  # noqa: E501
        :type mbs_session_id: MbsSessionId
        :param mbs_area_sessions: The mbs_area_sessions of this MbsSession.  # noqa: E501
        :type mbs_area_sessions: Dict[str, MbsServiceAreaInfo]
        """
        self.openapi_types = {
            'mbs_session_id': MbsSessionId,
            'mbs_area_sessions': Dict[str, MbsServiceAreaInfo]
        }

        self.attribute_map = {
            'mbs_session_id': 'mbsSessionId',
            'mbs_area_sessions': 'mbsAreaSessions'
        }

        self._mbs_session_id = mbs_session_id
        self._mbs_area_sessions = mbs_area_sessions

    @classmethod
    def from_dict(cls, dikt) -> 'MbsSession':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MbsSession of this MbsSession.  # noqa: E501
        :rtype: MbsSession
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mbs_session_id(self):
        """Gets the mbs_session_id of this MbsSession.


        :return: The mbs_session_id of this MbsSession.
        :rtype: MbsSessionId
        """
        return self._mbs_session_id

    @mbs_session_id.setter
    def mbs_session_id(self, mbs_session_id):
        """Sets the mbs_session_id of this MbsSession.


        :param mbs_session_id: The mbs_session_id of this MbsSession.
        :type mbs_session_id: MbsSessionId
        """
        if mbs_session_id is None:
            raise ValueError("Invalid value for `mbs_session_id`, must not be `None`")  # noqa: E501

        self._mbs_session_id = mbs_session_id

    @property
    def mbs_area_sessions(self):
        """Gets the mbs_area_sessions of this MbsSession.

        A map (list of key-value pairs) where the key identifies an areaSessionId  # noqa: E501

        :return: The mbs_area_sessions of this MbsSession.
        :rtype: Dict[str, MbsServiceAreaInfo]
        """
        return self._mbs_area_sessions

    @mbs_area_sessions.setter
    def mbs_area_sessions(self, mbs_area_sessions):
        """Sets the mbs_area_sessions of this MbsSession.

        A map (list of key-value pairs) where the key identifies an areaSessionId  # noqa: E501

        :param mbs_area_sessions: The mbs_area_sessions of this MbsSession.
        :type mbs_area_sessions: Dict[str, MbsServiceAreaInfo]
        """
        if mbs_area_sessions is not None and len(mbs_area_sessions) < 1:
            raise ValueError("Invalid value for `mbs_area_sessions`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._mbs_area_sessions = mbs_area_sessions

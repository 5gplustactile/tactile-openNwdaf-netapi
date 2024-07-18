# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class IdleStatusIndication(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, time_stamp=None, active_time=None, subs_reg_timer=None, edrx_cycle_length=None, suggested_num_of_dl_packets=None):  # noqa: E501
        """IdleStatusIndication - a model defined in OpenAPI

        :param time_stamp: The time_stamp of this IdleStatusIndication.  # noqa: E501
        :type time_stamp: datetime
        :param active_time: The active_time of this IdleStatusIndication.  # noqa: E501
        :type active_time: int
        :param subs_reg_timer: The subs_reg_timer of this IdleStatusIndication.  # noqa: E501
        :type subs_reg_timer: int
        :param edrx_cycle_length: The edrx_cycle_length of this IdleStatusIndication.  # noqa: E501
        :type edrx_cycle_length: int
        :param suggested_num_of_dl_packets: The suggested_num_of_dl_packets of this IdleStatusIndication.  # noqa: E501
        :type suggested_num_of_dl_packets: int
        """
        self.openapi_types = {
            'time_stamp': datetime,
            'active_time': int,
            'subs_reg_timer': int,
            'edrx_cycle_length': int,
            'suggested_num_of_dl_packets': int
        }

        self.attribute_map = {
            'time_stamp': 'timeStamp',
            'active_time': 'activeTime',
            'subs_reg_timer': 'subsRegTimer',
            'edrx_cycle_length': 'edrxCycleLength',
            'suggested_num_of_dl_packets': 'suggestedNumOfDlPackets'
        }

        self._time_stamp = time_stamp
        self._active_time = active_time
        self._subs_reg_timer = subs_reg_timer
        self._edrx_cycle_length = edrx_cycle_length
        self._suggested_num_of_dl_packets = suggested_num_of_dl_packets

    @classmethod
    def from_dict(cls, dikt) -> 'IdleStatusIndication':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IdleStatusIndication of this IdleStatusIndication.  # noqa: E501
        :rtype: IdleStatusIndication
        """
        return util.deserialize_model(dikt, cls)

    @property
    def time_stamp(self):
        """Gets the time_stamp of this IdleStatusIndication.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :return: The time_stamp of this IdleStatusIndication.
        :rtype: datetime
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this IdleStatusIndication.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :param time_stamp: The time_stamp of this IdleStatusIndication.
        :type time_stamp: datetime
        """

        self._time_stamp = time_stamp

    @property
    def active_time(self):
        """Gets the active_time of this IdleStatusIndication.

        indicating a time in seconds.  # noqa: E501

        :return: The active_time of this IdleStatusIndication.
        :rtype: int
        """
        return self._active_time

    @active_time.setter
    def active_time(self, active_time):
        """Sets the active_time of this IdleStatusIndication.

        indicating a time in seconds.  # noqa: E501

        :param active_time: The active_time of this IdleStatusIndication.
        :type active_time: int
        """

        self._active_time = active_time

    @property
    def subs_reg_timer(self):
        """Gets the subs_reg_timer of this IdleStatusIndication.

        indicating a time in seconds.  # noqa: E501

        :return: The subs_reg_timer of this IdleStatusIndication.
        :rtype: int
        """
        return self._subs_reg_timer

    @subs_reg_timer.setter
    def subs_reg_timer(self, subs_reg_timer):
        """Sets the subs_reg_timer of this IdleStatusIndication.

        indicating a time in seconds.  # noqa: E501

        :param subs_reg_timer: The subs_reg_timer of this IdleStatusIndication.
        :type subs_reg_timer: int
        """

        self._subs_reg_timer = subs_reg_timer

    @property
    def edrx_cycle_length(self):
        """Gets the edrx_cycle_length of this IdleStatusIndication.


        :return: The edrx_cycle_length of this IdleStatusIndication.
        :rtype: int
        """
        return self._edrx_cycle_length

    @edrx_cycle_length.setter
    def edrx_cycle_length(self, edrx_cycle_length):
        """Sets the edrx_cycle_length of this IdleStatusIndication.


        :param edrx_cycle_length: The edrx_cycle_length of this IdleStatusIndication.
        :type edrx_cycle_length: int
        """

        self._edrx_cycle_length = edrx_cycle_length

    @property
    def suggested_num_of_dl_packets(self):
        """Gets the suggested_num_of_dl_packets of this IdleStatusIndication.


        :return: The suggested_num_of_dl_packets of this IdleStatusIndication.
        :rtype: int
        """
        return self._suggested_num_of_dl_packets

    @suggested_num_of_dl_packets.setter
    def suggested_num_of_dl_packets(self, suggested_num_of_dl_packets):
        """Sets the suggested_num_of_dl_packets of this IdleStatusIndication.


        :param suggested_num_of_dl_packets: The suggested_num_of_dl_packets of this IdleStatusIndication.
        :type suggested_num_of_dl_packets: int
        """

        self._suggested_num_of_dl_packets = suggested_num_of_dl_packets

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.flow_info import FlowInfo
from openapi_server.models.time_window import TimeWindow
import re
from openapi_server import util

from openapi_server.models.flow_info import FlowInfo  # noqa: E501
from openapi_server.models.time_window import TimeWindow  # noqa: E501
import re  # noqa: E501

class UserDataCongestionCollection(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, app_id=None, ip_traffic_filter=None, time_interv=None, thrput_ul=None, thrput_dl=None, thrput_pk_ul=None, thrput_pk_dl=None):  # noqa: E501
        """UserDataCongestionCollection - a model defined in OpenAPI

        :param app_id: The app_id of this UserDataCongestionCollection.  # noqa: E501
        :type app_id: str
        :param ip_traffic_filter: The ip_traffic_filter of this UserDataCongestionCollection.  # noqa: E501
        :type ip_traffic_filter: FlowInfo
        :param time_interv: The time_interv of this UserDataCongestionCollection.  # noqa: E501
        :type time_interv: TimeWindow
        :param thrput_ul: The thrput_ul of this UserDataCongestionCollection.  # noqa: E501
        :type thrput_ul: str
        :param thrput_dl: The thrput_dl of this UserDataCongestionCollection.  # noqa: E501
        :type thrput_dl: str
        :param thrput_pk_ul: The thrput_pk_ul of this UserDataCongestionCollection.  # noqa: E501
        :type thrput_pk_ul: str
        :param thrput_pk_dl: The thrput_pk_dl of this UserDataCongestionCollection.  # noqa: E501
        :type thrput_pk_dl: str
        """
        self.openapi_types = {
            'app_id': str,
            'ip_traffic_filter': FlowInfo,
            'time_interv': TimeWindow,
            'thrput_ul': str,
            'thrput_dl': str,
            'thrput_pk_ul': str,
            'thrput_pk_dl': str
        }

        self.attribute_map = {
            'app_id': 'appId',
            'ip_traffic_filter': 'ipTrafficFilter',
            'time_interv': 'timeInterv',
            'thrput_ul': 'thrputUl',
            'thrput_dl': 'thrputDl',
            'thrput_pk_ul': 'thrputPkUl',
            'thrput_pk_dl': 'thrputPkDl'
        }

        self._app_id = app_id
        self._ip_traffic_filter = ip_traffic_filter
        self._time_interv = time_interv
        self._thrput_ul = thrput_ul
        self._thrput_dl = thrput_dl
        self._thrput_pk_ul = thrput_pk_ul
        self._thrput_pk_dl = thrput_pk_dl

    @classmethod
    def from_dict(cls, dikt) -> 'UserDataCongestionCollection':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserDataCongestionCollection of this UserDataCongestionCollection.  # noqa: E501
        :rtype: UserDataCongestionCollection
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_id(self):
        """Gets the app_id of this UserDataCongestionCollection.

        String providing an application identifier.  # noqa: E501

        :return: The app_id of this UserDataCongestionCollection.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this UserDataCongestionCollection.

        String providing an application identifier.  # noqa: E501

        :param app_id: The app_id of this UserDataCongestionCollection.
        :type app_id: str
        """

        self._app_id = app_id

    @property
    def ip_traffic_filter(self):
        """Gets the ip_traffic_filter of this UserDataCongestionCollection.


        :return: The ip_traffic_filter of this UserDataCongestionCollection.
        :rtype: FlowInfo
        """
        return self._ip_traffic_filter

    @ip_traffic_filter.setter
    def ip_traffic_filter(self, ip_traffic_filter):
        """Sets the ip_traffic_filter of this UserDataCongestionCollection.


        :param ip_traffic_filter: The ip_traffic_filter of this UserDataCongestionCollection.
        :type ip_traffic_filter: FlowInfo
        """

        self._ip_traffic_filter = ip_traffic_filter

    @property
    def time_interv(self):
        """Gets the time_interv of this UserDataCongestionCollection.


        :return: The time_interv of this UserDataCongestionCollection.
        :rtype: TimeWindow
        """
        return self._time_interv

    @time_interv.setter
    def time_interv(self, time_interv):
        """Sets the time_interv of this UserDataCongestionCollection.


        :param time_interv: The time_interv of this UserDataCongestionCollection.
        :type time_interv: TimeWindow
        """

        self._time_interv = time_interv

    @property
    def thrput_ul(self):
        """Gets the thrput_ul of this UserDataCongestionCollection.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :return: The thrput_ul of this UserDataCongestionCollection.
        :rtype: str
        """
        return self._thrput_ul

    @thrput_ul.setter
    def thrput_ul(self, thrput_ul):
        """Sets the thrput_ul of this UserDataCongestionCollection.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :param thrput_ul: The thrput_ul of this UserDataCongestionCollection.
        :type thrput_ul: str
        """
        if thrput_ul is not None and not re.search(r'^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$', thrput_ul):  # noqa: E501
            raise ValueError("Invalid value for `thrput_ul`, must be a follow pattern or equal to `/^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$/`")  # noqa: E501

        self._thrput_ul = thrput_ul

    @property
    def thrput_dl(self):
        """Gets the thrput_dl of this UserDataCongestionCollection.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :return: The thrput_dl of this UserDataCongestionCollection.
        :rtype: str
        """
        return self._thrput_dl

    @thrput_dl.setter
    def thrput_dl(self, thrput_dl):
        """Sets the thrput_dl of this UserDataCongestionCollection.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :param thrput_dl: The thrput_dl of this UserDataCongestionCollection.
        :type thrput_dl: str
        """
        if thrput_dl is not None and not re.search(r'^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$', thrput_dl):  # noqa: E501
            raise ValueError("Invalid value for `thrput_dl`, must be a follow pattern or equal to `/^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$/`")  # noqa: E501

        self._thrput_dl = thrput_dl

    @property
    def thrput_pk_ul(self):
        """Gets the thrput_pk_ul of this UserDataCongestionCollection.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :return: The thrput_pk_ul of this UserDataCongestionCollection.
        :rtype: str
        """
        return self._thrput_pk_ul

    @thrput_pk_ul.setter
    def thrput_pk_ul(self, thrput_pk_ul):
        """Sets the thrput_pk_ul of this UserDataCongestionCollection.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :param thrput_pk_ul: The thrput_pk_ul of this UserDataCongestionCollection.
        :type thrput_pk_ul: str
        """
        if thrput_pk_ul is not None and not re.search(r'^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$', thrput_pk_ul):  # noqa: E501
            raise ValueError("Invalid value for `thrput_pk_ul`, must be a follow pattern or equal to `/^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$/`")  # noqa: E501

        self._thrput_pk_ul = thrput_pk_ul

    @property
    def thrput_pk_dl(self):
        """Gets the thrput_pk_dl of this UserDataCongestionCollection.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :return: The thrput_pk_dl of this UserDataCongestionCollection.
        :rtype: str
        """
        return self._thrput_pk_dl

    @thrput_pk_dl.setter
    def thrput_pk_dl(self, thrput_pk_dl):
        """Sets the thrput_pk_dl of this UserDataCongestionCollection.

        String representing a bit rate; the prefixes follow the standard symbols from The International System of Units, and represent x1000 multipliers, with the exception that prefix \"K\" is used to represent the standard symbol \"k\".   # noqa: E501

        :param thrput_pk_dl: The thrput_pk_dl of this UserDataCongestionCollection.
        :type thrput_pk_dl: str
        """
        if thrput_pk_dl is not None and not re.search(r'^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$', thrput_pk_dl):  # noqa: E501
            raise ValueError("Invalid value for `thrput_pk_dl`, must be a follow pattern or equal to `/^\d+(\.\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$/`")  # noqa: E501

        self._thrput_pk_dl = thrput_pk_dl
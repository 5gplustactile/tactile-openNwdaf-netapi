# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.event_type import EventType
from openapi_server.models.reachability_for_sms_report import ReachabilityForSmsReport
from openapi_server.models.reachability_report import ReachabilityReport
from openapi_server.models.report import Report
import re
from openapi_server import util

from openapi_server.models.event_type import EventType  # noqa: E501
from openapi_server.models.reachability_for_sms_report import ReachabilityForSmsReport  # noqa: E501
from openapi_server.models.reachability_report import ReachabilityReport  # noqa: E501
from openapi_server.models.report import Report  # noqa: E501
import re  # noqa: E501

class MonitoringReport(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, reference_id=None, event_type=None, report=None, reachability_for_sms_report=None, gpsi=None, time_stamp=None, reachability_report=None):  # noqa: E501
        """MonitoringReport - a model defined in OpenAPI

        :param reference_id: The reference_id of this MonitoringReport.  # noqa: E501
        :type reference_id: int
        :param event_type: The event_type of this MonitoringReport.  # noqa: E501
        :type event_type: EventType
        :param report: The report of this MonitoringReport.  # noqa: E501
        :type report: Report
        :param reachability_for_sms_report: The reachability_for_sms_report of this MonitoringReport.  # noqa: E501
        :type reachability_for_sms_report: ReachabilityForSmsReport
        :param gpsi: The gpsi of this MonitoringReport.  # noqa: E501
        :type gpsi: str
        :param time_stamp: The time_stamp of this MonitoringReport.  # noqa: E501
        :type time_stamp: datetime
        :param reachability_report: The reachability_report of this MonitoringReport.  # noqa: E501
        :type reachability_report: ReachabilityReport
        """
        self.openapi_types = {
            'reference_id': int,
            'event_type': EventType,
            'report': Report,
            'reachability_for_sms_report': ReachabilityForSmsReport,
            'gpsi': str,
            'time_stamp': datetime,
            'reachability_report': ReachabilityReport
        }

        self.attribute_map = {
            'reference_id': 'referenceId',
            'event_type': 'eventType',
            'report': 'report',
            'reachability_for_sms_report': 'reachabilityForSmsReport',
            'gpsi': 'gpsi',
            'time_stamp': 'timeStamp',
            'reachability_report': 'reachabilityReport'
        }

        self._reference_id = reference_id
        self._event_type = event_type
        self._report = report
        self._reachability_for_sms_report = reachability_for_sms_report
        self._gpsi = gpsi
        self._time_stamp = time_stamp
        self._reachability_report = reachability_report

    @classmethod
    def from_dict(cls, dikt) -> 'MonitoringReport':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MonitoringReport of this MonitoringReport.  # noqa: E501
        :rtype: MonitoringReport
        """
        return util.deserialize_model(dikt, cls)

    @property
    def reference_id(self):
        """Gets the reference_id of this MonitoringReport.


        :return: The reference_id of this MonitoringReport.
        :rtype: int
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this MonitoringReport.


        :param reference_id: The reference_id of this MonitoringReport.
        :type reference_id: int
        """
        if reference_id is None:
            raise ValueError("Invalid value for `reference_id`, must not be `None`")  # noqa: E501

        self._reference_id = reference_id

    @property
    def event_type(self):
        """Gets the event_type of this MonitoringReport.


        :return: The event_type of this MonitoringReport.
        :rtype: EventType
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this MonitoringReport.


        :param event_type: The event_type of this MonitoringReport.
        :type event_type: EventType
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def report(self):
        """Gets the report of this MonitoringReport.


        :return: The report of this MonitoringReport.
        :rtype: Report
        """
        return self._report

    @report.setter
    def report(self, report):
        """Sets the report of this MonitoringReport.


        :param report: The report of this MonitoringReport.
        :type report: Report
        """

        self._report = report

    @property
    def reachability_for_sms_report(self):
        """Gets the reachability_for_sms_report of this MonitoringReport.


        :return: The reachability_for_sms_report of this MonitoringReport.
        :rtype: ReachabilityForSmsReport
        """
        return self._reachability_for_sms_report

    @reachability_for_sms_report.setter
    def reachability_for_sms_report(self, reachability_for_sms_report):
        """Sets the reachability_for_sms_report of this MonitoringReport.


        :param reachability_for_sms_report: The reachability_for_sms_report of this MonitoringReport.
        :type reachability_for_sms_report: ReachabilityForSmsReport
        """

        self._reachability_for_sms_report = reachability_for_sms_report

    @property
    def gpsi(self):
        """Gets the gpsi of this MonitoringReport.

        String identifying a Gpsi shall contain either an External Id or an MSISDN.  It shall be formatted as follows -External Identifier= \"extid-'extid', where 'extid'  shall be formatted according to clause 19.7.2 of 3GPP TS 23.003 that describes an  External Identifier.    # noqa: E501

        :return: The gpsi of this MonitoringReport.
        :rtype: str
        """
        return self._gpsi

    @gpsi.setter
    def gpsi(self, gpsi):
        """Sets the gpsi of this MonitoringReport.

        String identifying a Gpsi shall contain either an External Id or an MSISDN.  It shall be formatted as follows -External Identifier= \"extid-'extid', where 'extid'  shall be formatted according to clause 19.7.2 of 3GPP TS 23.003 that describes an  External Identifier.    # noqa: E501

        :param gpsi: The gpsi of this MonitoringReport.
        :type gpsi: str
        """
        if gpsi is not None and not re.search(r'^(msisdn-[0-9]{5,15}|extid-[^@]+@[^@]+|.+)$', gpsi):  # noqa: E501
            raise ValueError("Invalid value for `gpsi`, must be a follow pattern or equal to `/^(msisdn-[0-9]{5,15}|extid-[^@]+@[^@]+|.+)$/`")  # noqa: E501

        self._gpsi = gpsi

    @property
    def time_stamp(self):
        """Gets the time_stamp of this MonitoringReport.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :return: The time_stamp of this MonitoringReport.
        :rtype: datetime
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this MonitoringReport.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :param time_stamp: The time_stamp of this MonitoringReport.
        :type time_stamp: datetime
        """
        if time_stamp is None:
            raise ValueError("Invalid value for `time_stamp`, must not be `None`")  # noqa: E501

        self._time_stamp = time_stamp

    @property
    def reachability_report(self):
        """Gets the reachability_report of this MonitoringReport.


        :return: The reachability_report of this MonitoringReport.
        :rtype: ReachabilityReport
        """
        return self._reachability_report

    @reachability_report.setter
    def reachability_report(self, reachability_report):
        """Sets the reachability_report of this MonitoringReport.


        :param reachability_report: The reachability_report of this MonitoringReport.
        :type reachability_report: ReachabilityReport
        """

        self._reachability_report = reachability_report

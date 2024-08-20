# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.access_type import AccessType
from openapi_server.models.amf_event_area import AmfEventArea
from openapi_server.models.amf_event_state import AmfEventState
from openapi_server.models.amf_event_type import AmfEventType
from openapi_server.models.cm_info import CmInfo
from openapi_server.models.communication_failure import CommunicationFailure
from openapi_server.models.idle_status_indication import IdleStatusIndication
from openapi_server.models.loss_of_connectivity_reason import LossOfConnectivityReason
from openapi_server.models.mm_transaction_location_report_item import MmTransactionLocationReportItem
from openapi_server.models.mm_transaction_slice_report_item import MmTransactionSliceReportItem
from openapi_server.models.model5_gs_user_state_info import Model5GsUserStateInfo
from openapi_server.models.rm_info import RmInfo
from openapi_server.models.snssai_tai_mapping import SnssaiTaiMapping
from openapi_server.models.sub_termination_reason import SubTerminationReason
from openapi_server.models.ueid_ext import UEIdExt
from openapi_server.models.ue_access_behavior_report_item import UeAccessBehaviorReportItem
from openapi_server.models.ue_location_trends_report_item import UeLocationTrendsReportItem
from openapi_server.models.ue_reachability import UeReachability
from openapi_server.models.user_location import UserLocation
import re
from openapi_server import util

from openapi_server.models.access_type import AccessType  # noqa: E501
from openapi_server.models.amf_event_area import AmfEventArea  # noqa: E501
from openapi_server.models.amf_event_state import AmfEventState  # noqa: E501
from openapi_server.models.amf_event_type import AmfEventType  # noqa: E501
from openapi_server.models.cm_info import CmInfo  # noqa: E501
from openapi_server.models.communication_failure import CommunicationFailure  # noqa: E501
from openapi_server.models.idle_status_indication import IdleStatusIndication  # noqa: E501
from openapi_server.models.loss_of_connectivity_reason import LossOfConnectivityReason  # noqa: E501
from openapi_server.models.mm_transaction_location_report_item import MmTransactionLocationReportItem  # noqa: E501
from openapi_server.models.mm_transaction_slice_report_item import MmTransactionSliceReportItem  # noqa: E501
from openapi_server.models.model5_gs_user_state_info import Model5GsUserStateInfo  # noqa: E501
from openapi_server.models.rm_info import RmInfo  # noqa: E501
from openapi_server.models.snssai_tai_mapping import SnssaiTaiMapping  # noqa: E501
from openapi_server.models.sub_termination_reason import SubTerminationReason  # noqa: E501
from openapi_server.models.ue_access_behavior_report_item import UeAccessBehaviorReportItem  # noqa: E501
from openapi_server.models.ue_location_trends_report_item import UeLocationTrendsReportItem  # noqa: E501
from openapi_server.models.ue_reachability import UeReachability  # noqa: E501
from openapi_server.models.ueid_ext import UEIdExt  # noqa: E501
from openapi_server.models.user_location import UserLocation  # noqa: E501
import re  # noqa: E501

class AmfEventReport(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, state=None, time_stamp=None, subscription_id=None, any_ue=None, supi=None, area_list=None, ref_id=None, gpsi=None, pei=None, location=None, additional_location=None, timezone=None, access_type_list=None, rm_info_list=None, cm_info_list=None, reachability=None, comm_failure=None, loss_of_connect_reason=None, number_of_ues=None, _5gs_user_state_list=None, type_code=None, registration_number=None, max_availability_time=None, ue_id_ext=None, snssai_tai_list=None, idle_status_indication=None, ue_access_behavior_trends=None, ue_location_trends=None, mm_trans_location_report_list=None, mm_trans_slice_report_list=None, term_reason=None):  # noqa: E501
        """AmfEventReport - a model defined in OpenAPI

        :param type: The type of this AmfEventReport.  # noqa: E501
        :type type: AmfEventType
        :param state: The state of this AmfEventReport.  # noqa: E501
        :type state: AmfEventState
        :param time_stamp: The time_stamp of this AmfEventReport.  # noqa: E501
        :type time_stamp: datetime
        :param subscription_id: The subscription_id of this AmfEventReport.  # noqa: E501
        :type subscription_id: str
        :param any_ue: The any_ue of this AmfEventReport.  # noqa: E501
        :type any_ue: bool
        :param supi: The supi of this AmfEventReport.  # noqa: E501
        :type supi: str
        :param area_list: The area_list of this AmfEventReport.  # noqa: E501
        :type area_list: List[AmfEventArea]
        :param ref_id: The ref_id of this AmfEventReport.  # noqa: E501
        :type ref_id: int
        :param gpsi: The gpsi of this AmfEventReport.  # noqa: E501
        :type gpsi: str
        :param pei: The pei of this AmfEventReport.  # noqa: E501
        :type pei: str
        :param location: The location of this AmfEventReport.  # noqa: E501
        :type location: UserLocation
        :param additional_location: The additional_location of this AmfEventReport.  # noqa: E501
        :type additional_location: UserLocation
        :param timezone: The timezone of this AmfEventReport.  # noqa: E501
        :type timezone: str
        :param access_type_list: The access_type_list of this AmfEventReport.  # noqa: E501
        :type access_type_list: List[AccessType]
        :param rm_info_list: The rm_info_list of this AmfEventReport.  # noqa: E501
        :type rm_info_list: List[RmInfo]
        :param cm_info_list: The cm_info_list of this AmfEventReport.  # noqa: E501
        :type cm_info_list: List[CmInfo]
        :param reachability: The reachability of this AmfEventReport.  # noqa: E501
        :type reachability: UeReachability
        :param comm_failure: The comm_failure of this AmfEventReport.  # noqa: E501
        :type comm_failure: CommunicationFailure
        :param loss_of_connect_reason: The loss_of_connect_reason of this AmfEventReport.  # noqa: E501
        :type loss_of_connect_reason: LossOfConnectivityReason
        :param number_of_ues: The number_of_ues of this AmfEventReport.  # noqa: E501
        :type number_of_ues: int
        :param _5gs_user_state_list: The _5gs_user_state_list of this AmfEventReport.  # noqa: E501
        :type _5gs_user_state_list: List[Model5GsUserStateInfo]
        :param type_code: The type_code of this AmfEventReport.  # noqa: E501
        :type type_code: str
        :param registration_number: The registration_number of this AmfEventReport.  # noqa: E501
        :type registration_number: int
        :param max_availability_time: The max_availability_time of this AmfEventReport.  # noqa: E501
        :type max_availability_time: datetime
        :param ue_id_ext: The ue_id_ext of this AmfEventReport.  # noqa: E501
        :type ue_id_ext: List[UEIdExt]
        :param snssai_tai_list: The snssai_tai_list of this AmfEventReport.  # noqa: E501
        :type snssai_tai_list: List[SnssaiTaiMapping]
        :param idle_status_indication: The idle_status_indication of this AmfEventReport.  # noqa: E501
        :type idle_status_indication: IdleStatusIndication
        :param ue_access_behavior_trends: The ue_access_behavior_trends of this AmfEventReport.  # noqa: E501
        :type ue_access_behavior_trends: List[UeAccessBehaviorReportItem]
        :param ue_location_trends: The ue_location_trends of this AmfEventReport.  # noqa: E501
        :type ue_location_trends: List[UeLocationTrendsReportItem]
        :param mm_trans_location_report_list: The mm_trans_location_report_list of this AmfEventReport.  # noqa: E501
        :type mm_trans_location_report_list: List[MmTransactionLocationReportItem]
        :param mm_trans_slice_report_list: The mm_trans_slice_report_list of this AmfEventReport.  # noqa: E501
        :type mm_trans_slice_report_list: List[MmTransactionSliceReportItem]
        :param term_reason: The term_reason of this AmfEventReport.  # noqa: E501
        :type term_reason: SubTerminationReason
        """
        self.openapi_types = {
            'type': AmfEventType,
            'state': AmfEventState,
            'time_stamp': datetime,
            'subscription_id': str,
            'any_ue': bool,
            'supi': str,
            'area_list': List[AmfEventArea],
            'ref_id': int,
            'gpsi': str,
            'pei': str,
            'location': UserLocation,
            'additional_location': UserLocation,
            'timezone': str,
            'access_type_list': List[AccessType],
            'rm_info_list': List[RmInfo],
            'cm_info_list': List[CmInfo],
            'reachability': UeReachability,
            'comm_failure': CommunicationFailure,
            'loss_of_connect_reason': LossOfConnectivityReason,
            'number_of_ues': int,
            '_5gs_user_state_list': List[Model5GsUserStateInfo],
            'type_code': str,
            'registration_number': int,
            'max_availability_time': datetime,
            'ue_id_ext': List[UEIdExt],
            'snssai_tai_list': List[SnssaiTaiMapping],
            'idle_status_indication': IdleStatusIndication,
            'ue_access_behavior_trends': List[UeAccessBehaviorReportItem],
            'ue_location_trends': List[UeLocationTrendsReportItem],
            'mm_trans_location_report_list': List[MmTransactionLocationReportItem],
            'mm_trans_slice_report_list': List[MmTransactionSliceReportItem],
            'term_reason': SubTerminationReason
        }

        self.attribute_map = {
            'type': 'type',
            'state': 'state',
            'time_stamp': 'timeStamp',
            'subscription_id': 'subscriptionId',
            'any_ue': 'anyUe',
            'supi': 'supi',
            'area_list': 'areaList',
            'ref_id': 'refId',
            'gpsi': 'gpsi',
            'pei': 'pei',
            'location': 'location',
            'additional_location': 'additionalLocation',
            'timezone': 'timezone',
            'access_type_list': 'accessTypeList',
            'rm_info_list': 'rmInfoList',
            'cm_info_list': 'cmInfoList',
            'reachability': 'reachability',
            'comm_failure': 'commFailure',
            'loss_of_connect_reason': 'lossOfConnectReason',
            'number_of_ues': 'numberOfUes',
            '_5gs_user_state_list': '5gsUserStateList',
            'type_code': 'typeCode',
            'registration_number': 'registrationNumber',
            'max_availability_time': 'maxAvailabilityTime',
            'ue_id_ext': 'ueIdExt',
            'snssai_tai_list': 'snssaiTaiList',
            'idle_status_indication': 'idleStatusIndication',
            'ue_access_behavior_trends': 'ueAccessBehaviorTrends',
            'ue_location_trends': 'ueLocationTrends',
            'mm_trans_location_report_list': 'mmTransLocationReportList',
            'mm_trans_slice_report_list': 'mmTransSliceReportList',
            'term_reason': 'termReason'
        }

        self._type = type
        self._state = state
        self._time_stamp = time_stamp
        self._subscription_id = subscription_id
        self._any_ue = any_ue
        self._supi = supi
        self._area_list = area_list
        self._ref_id = ref_id
        self._gpsi = gpsi
        self._pei = pei
        self._location = location
        self._additional_location = additional_location
        self._timezone = timezone
        self._access_type_list = access_type_list
        self._rm_info_list = rm_info_list
        self._cm_info_list = cm_info_list
        self._reachability = reachability
        self._comm_failure = comm_failure
        self._loss_of_connect_reason = loss_of_connect_reason
        self._number_of_ues = number_of_ues
        self.__5gs_user_state_list = _5gs_user_state_list
        self._type_code = type_code
        self._registration_number = registration_number
        self._max_availability_time = max_availability_time
        self._ue_id_ext = ue_id_ext
        self._snssai_tai_list = snssai_tai_list
        self._idle_status_indication = idle_status_indication
        self._ue_access_behavior_trends = ue_access_behavior_trends
        self._ue_location_trends = ue_location_trends
        self._mm_trans_location_report_list = mm_trans_location_report_list
        self._mm_trans_slice_report_list = mm_trans_slice_report_list
        self._term_reason = term_reason

    @classmethod
    def from_dict(cls, dikt) -> 'AmfEventReport':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AmfEventReport of this AmfEventReport.  # noqa: E501
        :rtype: AmfEventReport
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this AmfEventReport.


        :return: The type of this AmfEventReport.
        :rtype: AmfEventType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AmfEventReport.


        :param type: The type of this AmfEventReport.
        :type type: AmfEventType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def state(self):
        """Gets the state of this AmfEventReport.


        :return: The state of this AmfEventReport.
        :rtype: AmfEventState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AmfEventReport.


        :param state: The state of this AmfEventReport.
        :type state: AmfEventState
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def time_stamp(self):
        """Gets the time_stamp of this AmfEventReport.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :return: The time_stamp of this AmfEventReport.
        :rtype: datetime
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this AmfEventReport.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :param time_stamp: The time_stamp of this AmfEventReport.
        :type time_stamp: datetime
        """
        if time_stamp is None:
            raise ValueError("Invalid value for `time_stamp`, must not be `None`")  # noqa: E501

        self._time_stamp = time_stamp

    @property
    def subscription_id(self):
        """Gets the subscription_id of this AmfEventReport.

        String providing an URI formatted according to RFC 3986.  # noqa: E501

        :return: The subscription_id of this AmfEventReport.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this AmfEventReport.

        String providing an URI formatted according to RFC 3986.  # noqa: E501

        :param subscription_id: The subscription_id of this AmfEventReport.
        :type subscription_id: str
        """

        self._subscription_id = subscription_id

    @property
    def any_ue(self):
        """Gets the any_ue of this AmfEventReport.


        :return: The any_ue of this AmfEventReport.
        :rtype: bool
        """
        return self._any_ue

    @any_ue.setter
    def any_ue(self, any_ue):
        """Sets the any_ue of this AmfEventReport.


        :param any_ue: The any_ue of this AmfEventReport.
        :type any_ue: bool
        """

        self._any_ue = any_ue

    @property
    def supi(self):
        """Gets the supi of this AmfEventReport.

        String identifying a Supi that shall contain either an IMSI, a network specific identifier, a Global Cable Identifier (GCI) or a Global Line Identifier (GLI) as specified in clause  2.2A of 3GPP TS 23.003. It shall be formatted as follows  - for an IMSI \"imsi-<imsi>\", where <imsi> shall be formatted according to clause 2.2    of 3GPP TS 23.003 that describes an IMSI.  - for a network specific identifier \"nai-<nai>, where <nai> shall be formatted    according to clause 28.7.2 of 3GPP TS 23.003 that describes an NAI.  - for a GCI \"gci-<gci>\", where <gci> shall be formatted according to clause 28.15.2    of 3GPP TS 23.003.  - for a GLI \"gli-<gli>\", where <gli> shall be formatted according to clause 28.16.2 of    3GPP TS 23.003.To enable that the value is used as part of an URI, the string shall    only contain characters allowed according to the \"lower-with-hyphen\" naming convention    defined in 3GPP TS 29.501.   # noqa: E501

        :return: The supi of this AmfEventReport.
        :rtype: str
        """
        return self._supi

    @supi.setter
    def supi(self, supi):
        """Sets the supi of this AmfEventReport.

        String identifying a Supi that shall contain either an IMSI, a network specific identifier, a Global Cable Identifier (GCI) or a Global Line Identifier (GLI) as specified in clause  2.2A of 3GPP TS 23.003. It shall be formatted as follows  - for an IMSI \"imsi-<imsi>\", where <imsi> shall be formatted according to clause 2.2    of 3GPP TS 23.003 that describes an IMSI.  - for a network specific identifier \"nai-<nai>, where <nai> shall be formatted    according to clause 28.7.2 of 3GPP TS 23.003 that describes an NAI.  - for a GCI \"gci-<gci>\", where <gci> shall be formatted according to clause 28.15.2    of 3GPP TS 23.003.  - for a GLI \"gli-<gli>\", where <gli> shall be formatted according to clause 28.16.2 of    3GPP TS 23.003.To enable that the value is used as part of an URI, the string shall    only contain characters allowed according to the \"lower-with-hyphen\" naming convention    defined in 3GPP TS 29.501.   # noqa: E501

        :param supi: The supi of this AmfEventReport.
        :type supi: str
        """
        if supi is not None and not re.search(r'^(imsi-[0-9]{5,15}|nai-.+|gci-.+|gli-.+|.+)$', supi):  # noqa: E501
            raise ValueError("Invalid value for `supi`, must be a follow pattern or equal to `/^(imsi-[0-9]{5,15}|nai-.+|gci-.+|gli-.+|.+)$/`")  # noqa: E501

        self._supi = supi

    @property
    def area_list(self):
        """Gets the area_list of this AmfEventReport.


        :return: The area_list of this AmfEventReport.
        :rtype: List[AmfEventArea]
        """
        return self._area_list

    @area_list.setter
    def area_list(self, area_list):
        """Sets the area_list of this AmfEventReport.


        :param area_list: The area_list of this AmfEventReport.
        :type area_list: List[AmfEventArea]
        """
        if area_list is not None and len(area_list) < 1:
            raise ValueError("Invalid value for `area_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._area_list = area_list

    @property
    def ref_id(self):
        """Gets the ref_id of this AmfEventReport.


        :return: The ref_id of this AmfEventReport.
        :rtype: int
        """
        return self._ref_id

    @ref_id.setter
    def ref_id(self, ref_id):
        """Sets the ref_id of this AmfEventReport.


        :param ref_id: The ref_id of this AmfEventReport.
        :type ref_id: int
        """

        self._ref_id = ref_id

    @property
    def gpsi(self):
        """Gets the gpsi of this AmfEventReport.

        String identifying a Gpsi shall contain either an External Id or an MSISDN.  It shall be formatted as follows -External Identifier= \"extid-'extid', where 'extid'  shall be formatted according to clause 19.7.2 of 3GPP TS 23.003 that describes an  External Identifier.    # noqa: E501

        :return: The gpsi of this AmfEventReport.
        :rtype: str
        """
        return self._gpsi

    @gpsi.setter
    def gpsi(self, gpsi):
        """Sets the gpsi of this AmfEventReport.

        String identifying a Gpsi shall contain either an External Id or an MSISDN.  It shall be formatted as follows -External Identifier= \"extid-'extid', where 'extid'  shall be formatted according to clause 19.7.2 of 3GPP TS 23.003 that describes an  External Identifier.    # noqa: E501

        :param gpsi: The gpsi of this AmfEventReport.
        :type gpsi: str
        """
        if gpsi is not None and not re.search(r'^(msisdn-[0-9]{5,15}|extid-[^@]+@[^@]+|.+)$', gpsi):  # noqa: E501
            raise ValueError("Invalid value for `gpsi`, must be a follow pattern or equal to `/^(msisdn-[0-9]{5,15}|extid-[^@]+@[^@]+|.+)$/`")  # noqa: E501

        self._gpsi = gpsi

    @property
    def pei(self):
        """Gets the pei of this AmfEventReport.

        String representing a Permanent Equipment Identifier that may contain - an IMEI or IMEISV, as  specified in clause 6.2 of 3GPP TS 23.003; a MAC address for a 5G-RG or FN-RG via  wireline  access, with an indication that this address cannot be trusted for regulatory purpose if this  address cannot be used as an Equipment Identifier of the FN-RG, as specified in clause 4.7.7  of 3GPP TS23.316. Examples are imei-012345678901234 or imeisv-0123456789012345.    # noqa: E501

        :return: The pei of this AmfEventReport.
        :rtype: str
        """
        return self._pei

    @pei.setter
    def pei(self, pei):
        """Sets the pei of this AmfEventReport.

        String representing a Permanent Equipment Identifier that may contain - an IMEI or IMEISV, as  specified in clause 6.2 of 3GPP TS 23.003; a MAC address for a 5G-RG or FN-RG via  wireline  access, with an indication that this address cannot be trusted for regulatory purpose if this  address cannot be used as an Equipment Identifier of the FN-RG, as specified in clause 4.7.7  of 3GPP TS23.316. Examples are imei-012345678901234 or imeisv-0123456789012345.    # noqa: E501

        :param pei: The pei of this AmfEventReport.
        :type pei: str
        """
        if pei is not None and not re.search(r'^(imei-[0-9]{15}|imeisv-[0-9]{16}|mac((-[0-9a-fA-F]{2}){6})(-untrusted)?|eui((-[0-9a-fA-F]{2}){8})|.+)$', pei):  # noqa: E501
            raise ValueError("Invalid value for `pei`, must be a follow pattern or equal to `/^(imei-[0-9]{15}|imeisv-[0-9]{16}|mac((-[0-9a-fA-F]{2}){6})(-untrusted)?|eui((-[0-9a-fA-F]{2}){8})|.+)$/`")  # noqa: E501

        self._pei = pei

    @property
    def location(self):
        """Gets the location of this AmfEventReport.


        :return: The location of this AmfEventReport.
        :rtype: UserLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this AmfEventReport.


        :param location: The location of this AmfEventReport.
        :type location: UserLocation
        """

        self._location = location

    @property
    def additional_location(self):
        """Gets the additional_location of this AmfEventReport.


        :return: The additional_location of this AmfEventReport.
        :rtype: UserLocation
        """
        return self._additional_location

    @additional_location.setter
    def additional_location(self, additional_location):
        """Sets the additional_location of this AmfEventReport.


        :param additional_location: The additional_location of this AmfEventReport.
        :type additional_location: UserLocation
        """

        self._additional_location = additional_location

    @property
    def timezone(self):
        """Gets the timezone of this AmfEventReport.

        String with format \"time-numoffset\" optionally appended by \"daylightSavingTime\", where  - \"time-numoffset\" shall represent the time zone adjusted for daylight saving time and be    encoded as time-numoffset as defined in clause 5.6 of IETF RFC 3339;  - \"daylightSavingTime\" shall represent the adjustment that has been made and shall be    encoded as \"+1\" or \"+2\" for a +1 or +2 hours adjustment.   The example is for 8 hours behind UTC, +1 hour adjustment for Daylight Saving Time.   # noqa: E501

        :return: The timezone of this AmfEventReport.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this AmfEventReport.

        String with format \"time-numoffset\" optionally appended by \"daylightSavingTime\", where  - \"time-numoffset\" shall represent the time zone adjusted for daylight saving time and be    encoded as time-numoffset as defined in clause 5.6 of IETF RFC 3339;  - \"daylightSavingTime\" shall represent the adjustment that has been made and shall be    encoded as \"+1\" or \"+2\" for a +1 or +2 hours adjustment.   The example is for 8 hours behind UTC, +1 hour adjustment for Daylight Saving Time.   # noqa: E501

        :param timezone: The timezone of this AmfEventReport.
        :type timezone: str
        """

        self._timezone = timezone

    @property
    def access_type_list(self):
        """Gets the access_type_list of this AmfEventReport.


        :return: The access_type_list of this AmfEventReport.
        :rtype: List[AccessType]
        """
        return self._access_type_list

    @access_type_list.setter
    def access_type_list(self, access_type_list):
        """Sets the access_type_list of this AmfEventReport.


        :param access_type_list: The access_type_list of this AmfEventReport.
        :type access_type_list: List[AccessType]
        """
        if access_type_list is not None and len(access_type_list) < 1:
            raise ValueError("Invalid value for `access_type_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._access_type_list = access_type_list

    @property
    def rm_info_list(self):
        """Gets the rm_info_list of this AmfEventReport.


        :return: The rm_info_list of this AmfEventReport.
        :rtype: List[RmInfo]
        """
        return self._rm_info_list

    @rm_info_list.setter
    def rm_info_list(self, rm_info_list):
        """Sets the rm_info_list of this AmfEventReport.


        :param rm_info_list: The rm_info_list of this AmfEventReport.
        :type rm_info_list: List[RmInfo]
        """
        if rm_info_list is not None and len(rm_info_list) < 1:
            raise ValueError("Invalid value for `rm_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._rm_info_list = rm_info_list

    @property
    def cm_info_list(self):
        """Gets the cm_info_list of this AmfEventReport.


        :return: The cm_info_list of this AmfEventReport.
        :rtype: List[CmInfo]
        """
        return self._cm_info_list

    @cm_info_list.setter
    def cm_info_list(self, cm_info_list):
        """Sets the cm_info_list of this AmfEventReport.


        :param cm_info_list: The cm_info_list of this AmfEventReport.
        :type cm_info_list: List[CmInfo]
        """
        if cm_info_list is not None and len(cm_info_list) < 1:
            raise ValueError("Invalid value for `cm_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._cm_info_list = cm_info_list

    @property
    def reachability(self):
        """Gets the reachability of this AmfEventReport.


        :return: The reachability of this AmfEventReport.
        :rtype: UeReachability
        """
        return self._reachability

    @reachability.setter
    def reachability(self, reachability):
        """Sets the reachability of this AmfEventReport.


        :param reachability: The reachability of this AmfEventReport.
        :type reachability: UeReachability
        """

        self._reachability = reachability

    @property
    def comm_failure(self):
        """Gets the comm_failure of this AmfEventReport.


        :return: The comm_failure of this AmfEventReport.
        :rtype: CommunicationFailure
        """
        return self._comm_failure

    @comm_failure.setter
    def comm_failure(self, comm_failure):
        """Sets the comm_failure of this AmfEventReport.


        :param comm_failure: The comm_failure of this AmfEventReport.
        :type comm_failure: CommunicationFailure
        """

        self._comm_failure = comm_failure

    @property
    def loss_of_connect_reason(self):
        """Gets the loss_of_connect_reason of this AmfEventReport.


        :return: The loss_of_connect_reason of this AmfEventReport.
        :rtype: LossOfConnectivityReason
        """
        return self._loss_of_connect_reason

    @loss_of_connect_reason.setter
    def loss_of_connect_reason(self, loss_of_connect_reason):
        """Sets the loss_of_connect_reason of this AmfEventReport.


        :param loss_of_connect_reason: The loss_of_connect_reason of this AmfEventReport.
        :type loss_of_connect_reason: LossOfConnectivityReason
        """

        self._loss_of_connect_reason = loss_of_connect_reason

    @property
    def number_of_ues(self):
        """Gets the number_of_ues of this AmfEventReport.


        :return: The number_of_ues of this AmfEventReport.
        :rtype: int
        """
        return self._number_of_ues

    @number_of_ues.setter
    def number_of_ues(self, number_of_ues):
        """Sets the number_of_ues of this AmfEventReport.


        :param number_of_ues: The number_of_ues of this AmfEventReport.
        :type number_of_ues: int
        """

        self._number_of_ues = number_of_ues

    @property
    def _5gs_user_state_list(self):
        """Gets the _5gs_user_state_list of this AmfEventReport.


        :return: The _5gs_user_state_list of this AmfEventReport.
        :rtype: List[Model5GsUserStateInfo]
        """
        return self.__5gs_user_state_list

    @_5gs_user_state_list.setter
    def _5gs_user_state_list(self, _5gs_user_state_list):
        """Sets the _5gs_user_state_list of this AmfEventReport.


        :param _5gs_user_state_list: The _5gs_user_state_list of this AmfEventReport.
        :type _5gs_user_state_list: List[Model5GsUserStateInfo]
        """
        if _5gs_user_state_list is not None and len(_5gs_user_state_list) < 1:
            raise ValueError("Invalid value for `_5gs_user_state_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self.__5gs_user_state_list = _5gs_user_state_list

    @property
    def type_code(self):
        """Gets the type_code of this AmfEventReport.


        :return: The type_code of this AmfEventReport.
        :rtype: str
        """
        return self._type_code

    @type_code.setter
    def type_code(self, type_code):
        """Sets the type_code of this AmfEventReport.


        :param type_code: The type_code of this AmfEventReport.
        :type type_code: str
        """
        if type_code is not None and not re.search(r'^imeitac-[0-9]{8}$', type_code):  # noqa: E501
            raise ValueError("Invalid value for `type_code`, must be a follow pattern or equal to `/^imeitac-[0-9]{8}$/`")  # noqa: E501

        self._type_code = type_code

    @property
    def registration_number(self):
        """Gets the registration_number of this AmfEventReport.


        :return: The registration_number of this AmfEventReport.
        :rtype: int
        """
        return self._registration_number

    @registration_number.setter
    def registration_number(self, registration_number):
        """Sets the registration_number of this AmfEventReport.


        :param registration_number: The registration_number of this AmfEventReport.
        :type registration_number: int
        """

        self._registration_number = registration_number

    @property
    def max_availability_time(self):
        """Gets the max_availability_time of this AmfEventReport.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :return: The max_availability_time of this AmfEventReport.
        :rtype: datetime
        """
        return self._max_availability_time

    @max_availability_time.setter
    def max_availability_time(self, max_availability_time):
        """Sets the max_availability_time of this AmfEventReport.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :param max_availability_time: The max_availability_time of this AmfEventReport.
        :type max_availability_time: datetime
        """

        self._max_availability_time = max_availability_time

    @property
    def ue_id_ext(self):
        """Gets the ue_id_ext of this AmfEventReport.


        :return: The ue_id_ext of this AmfEventReport.
        :rtype: List[UEIdExt]
        """
        return self._ue_id_ext

    @ue_id_ext.setter
    def ue_id_ext(self, ue_id_ext):
        """Sets the ue_id_ext of this AmfEventReport.


        :param ue_id_ext: The ue_id_ext of this AmfEventReport.
        :type ue_id_ext: List[UEIdExt]
        """
        if ue_id_ext is not None and len(ue_id_ext) < 1:
            raise ValueError("Invalid value for `ue_id_ext`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ue_id_ext = ue_id_ext

    @property
    def snssai_tai_list(self):
        """Gets the snssai_tai_list of this AmfEventReport.


        :return: The snssai_tai_list of this AmfEventReport.
        :rtype: List[SnssaiTaiMapping]
        """
        return self._snssai_tai_list

    @snssai_tai_list.setter
    def snssai_tai_list(self, snssai_tai_list):
        """Sets the snssai_tai_list of this AmfEventReport.


        :param snssai_tai_list: The snssai_tai_list of this AmfEventReport.
        :type snssai_tai_list: List[SnssaiTaiMapping]
        """
        if snssai_tai_list is not None and len(snssai_tai_list) < 1:
            raise ValueError("Invalid value for `snssai_tai_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._snssai_tai_list = snssai_tai_list

    @property
    def idle_status_indication(self):
        """Gets the idle_status_indication of this AmfEventReport.


        :return: The idle_status_indication of this AmfEventReport.
        :rtype: IdleStatusIndication
        """
        return self._idle_status_indication

    @idle_status_indication.setter
    def idle_status_indication(self, idle_status_indication):
        """Sets the idle_status_indication of this AmfEventReport.


        :param idle_status_indication: The idle_status_indication of this AmfEventReport.
        :type idle_status_indication: IdleStatusIndication
        """

        self._idle_status_indication = idle_status_indication

    @property
    def ue_access_behavior_trends(self):
        """Gets the ue_access_behavior_trends of this AmfEventReport.


        :return: The ue_access_behavior_trends of this AmfEventReport.
        :rtype: List[UeAccessBehaviorReportItem]
        """
        return self._ue_access_behavior_trends

    @ue_access_behavior_trends.setter
    def ue_access_behavior_trends(self, ue_access_behavior_trends):
        """Sets the ue_access_behavior_trends of this AmfEventReport.


        :param ue_access_behavior_trends: The ue_access_behavior_trends of this AmfEventReport.
        :type ue_access_behavior_trends: List[UeAccessBehaviorReportItem]
        """
        if ue_access_behavior_trends is not None and len(ue_access_behavior_trends) < 1:
            raise ValueError("Invalid value for `ue_access_behavior_trends`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ue_access_behavior_trends = ue_access_behavior_trends

    @property
    def ue_location_trends(self):
        """Gets the ue_location_trends of this AmfEventReport.


        :return: The ue_location_trends of this AmfEventReport.
        :rtype: List[UeLocationTrendsReportItem]
        """
        return self._ue_location_trends

    @ue_location_trends.setter
    def ue_location_trends(self, ue_location_trends):
        """Sets the ue_location_trends of this AmfEventReport.


        :param ue_location_trends: The ue_location_trends of this AmfEventReport.
        :type ue_location_trends: List[UeLocationTrendsReportItem]
        """
        if ue_location_trends is not None and len(ue_location_trends) < 1:
            raise ValueError("Invalid value for `ue_location_trends`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ue_location_trends = ue_location_trends

    @property
    def mm_trans_location_report_list(self):
        """Gets the mm_trans_location_report_list of this AmfEventReport.


        :return: The mm_trans_location_report_list of this AmfEventReport.
        :rtype: List[MmTransactionLocationReportItem]
        """
        return self._mm_trans_location_report_list

    @mm_trans_location_report_list.setter
    def mm_trans_location_report_list(self, mm_trans_location_report_list):
        """Sets the mm_trans_location_report_list of this AmfEventReport.


        :param mm_trans_location_report_list: The mm_trans_location_report_list of this AmfEventReport.
        :type mm_trans_location_report_list: List[MmTransactionLocationReportItem]
        """
        if mm_trans_location_report_list is not None and len(mm_trans_location_report_list) < 1:
            raise ValueError("Invalid value for `mm_trans_location_report_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._mm_trans_location_report_list = mm_trans_location_report_list

    @property
    def mm_trans_slice_report_list(self):
        """Gets the mm_trans_slice_report_list of this AmfEventReport.


        :return: The mm_trans_slice_report_list of this AmfEventReport.
        :rtype: List[MmTransactionSliceReportItem]
        """
        return self._mm_trans_slice_report_list

    @mm_trans_slice_report_list.setter
    def mm_trans_slice_report_list(self, mm_trans_slice_report_list):
        """Sets the mm_trans_slice_report_list of this AmfEventReport.


        :param mm_trans_slice_report_list: The mm_trans_slice_report_list of this AmfEventReport.
        :type mm_trans_slice_report_list: List[MmTransactionSliceReportItem]
        """
        if mm_trans_slice_report_list is not None and len(mm_trans_slice_report_list) < 1:
            raise ValueError("Invalid value for `mm_trans_slice_report_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._mm_trans_slice_report_list = mm_trans_slice_report_list

    @property
    def term_reason(self):
        """Gets the term_reason of this AmfEventReport.


        :return: The term_reason of this AmfEventReport.
        :rtype: SubTerminationReason
        """
        return self._term_reason

    @term_reason.setter
    def term_reason(self, term_reason):
        """Sets the term_reason of this AmfEventReport.


        :param term_reason: The term_reason of this AmfEventReport.
        :type term_reason: SubTerminationReason
        """

        self._term_reason = term_reason

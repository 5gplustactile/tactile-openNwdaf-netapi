# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.data_collection_purpose import DataCollectionPurpose
from openapi_server.models.data_subscription import DataSubscription
from openapi_server.models.formatting_instruction import FormattingInstruction
from openapi_server.models.nnwdaf_events_subscription import NnwdafEventsSubscription
from openapi_server.models.processing_instruction import ProcessingInstruction
from openapi_server.models.time_window import TimeWindow
import re
from openapi_server import util

from openapi_server.models.data_collection_purpose import DataCollectionPurpose  # noqa: E501
from openapi_server.models.data_subscription import DataSubscription  # noqa: E501
from openapi_server.models.formatting_instruction import FormattingInstruction  # noqa: E501
from openapi_server.models.nnwdaf_events_subscription import NnwdafEventsSubscription  # noqa: E501
from openapi_server.models.processing_instruction import ProcessingInstruction  # noqa: E501
from openapi_server.models.time_window import TimeWindow  # noqa: E501
import re  # noqa: E501

class NnwdafDataManagementSubsc(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, adrf_id=None, adrf_set_id=None, ana_sub=None, data_collect_purposes=None, checked_consent_ind=None, data_sub=None, format_instruct=None, notif_corr_id=None, notific_uri=None, proc_instruct=None, multi_proc_instructs=None, supp_feat=None, target_nf_id=None, target_nf_set_id=None, time_period=None):  # noqa: E501
        """NnwdafDataManagementSubsc - a model defined in OpenAPI

        :param adrf_id: The adrf_id of this NnwdafDataManagementSubsc.  # noqa: E501
        :type adrf_id: str
        :param adrf_set_id: The adrf_set_id of this NnwdafDataManagementSubsc.  # noqa: E501
        :type adrf_set_id: str
        :param ana_sub: The ana_sub of this NnwdafDataManagementSubsc.  # noqa: E501
        :type ana_sub: NnwdafEventsSubscription
        :param data_collect_purposes: The data_collect_purposes of this NnwdafDataManagementSubsc.  # noqa: E501
        :type data_collect_purposes: List[DataCollectionPurpose]
        :param checked_consent_ind: The checked_consent_ind of this NnwdafDataManagementSubsc.  # noqa: E501
        :type checked_consent_ind: bool
        :param data_sub: The data_sub of this NnwdafDataManagementSubsc.  # noqa: E501
        :type data_sub: DataSubscription
        :param format_instruct: The format_instruct of this NnwdafDataManagementSubsc.  # noqa: E501
        :type format_instruct: FormattingInstruction
        :param notif_corr_id: The notif_corr_id of this NnwdafDataManagementSubsc.  # noqa: E501
        :type notif_corr_id: str
        :param notific_uri: The notific_uri of this NnwdafDataManagementSubsc.  # noqa: E501
        :type notific_uri: str
        :param proc_instruct: The proc_instruct of this NnwdafDataManagementSubsc.  # noqa: E501
        :type proc_instruct: ProcessingInstruction
        :param multi_proc_instructs: The multi_proc_instructs of this NnwdafDataManagementSubsc.  # noqa: E501
        :type multi_proc_instructs: List[ProcessingInstruction]
        :param supp_feat: The supp_feat of this NnwdafDataManagementSubsc.  # noqa: E501
        :type supp_feat: str
        :param target_nf_id: The target_nf_id of this NnwdafDataManagementSubsc.  # noqa: E501
        :type target_nf_id: str
        :param target_nf_set_id: The target_nf_set_id of this NnwdafDataManagementSubsc.  # noqa: E501
        :type target_nf_set_id: str
        :param time_period: The time_period of this NnwdafDataManagementSubsc.  # noqa: E501
        :type time_period: TimeWindow
        """
        self.openapi_types = {
            'adrf_id': str,
            'adrf_set_id': str,
            'ana_sub': NnwdafEventsSubscription,
            'data_collect_purposes': List[DataCollectionPurpose],
            'checked_consent_ind': bool,
            'data_sub': DataSubscription,
            'format_instruct': FormattingInstruction,
            'notif_corr_id': str,
            'notific_uri': str,
            'proc_instruct': ProcessingInstruction,
            'multi_proc_instructs': List[ProcessingInstruction],
            'supp_feat': str,
            'target_nf_id': str,
            'target_nf_set_id': str,
            'time_period': TimeWindow
        }

        self.attribute_map = {
            'adrf_id': 'adrfId',
            'adrf_set_id': 'adrfSetId',
            'ana_sub': 'anaSub',
            'data_collect_purposes': 'dataCollectPurposes',
            'checked_consent_ind': 'checkedConsentInd',
            'data_sub': 'dataSub',
            'format_instruct': 'formatInstruct',
            'notif_corr_id': 'notifCorrId',
            'notific_uri': 'notificURI',
            'proc_instruct': 'procInstruct',
            'multi_proc_instructs': 'multiProcInstructs',
            'supp_feat': 'suppFeat',
            'target_nf_id': 'targetNfId',
            'target_nf_set_id': 'targetNfSetId',
            'time_period': 'timePeriod'
        }

        self._adrf_id = adrf_id
        self._adrf_set_id = adrf_set_id
        self._ana_sub = ana_sub
        self._data_collect_purposes = data_collect_purposes
        self._checked_consent_ind = checked_consent_ind
        self._data_sub = data_sub
        self._format_instruct = format_instruct
        self._notif_corr_id = notif_corr_id
        self._notific_uri = notific_uri
        self._proc_instruct = proc_instruct
        self._multi_proc_instructs = multi_proc_instructs
        self._supp_feat = supp_feat
        self._target_nf_id = target_nf_id
        self._target_nf_set_id = target_nf_set_id
        self._time_period = time_period

    @classmethod
    def from_dict(cls, dikt) -> 'NnwdafDataManagementSubsc':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NnwdafDataManagementSubsc of this NnwdafDataManagementSubsc.  # noqa: E501
        :rtype: NnwdafDataManagementSubsc
        """
        return util.deserialize_model(dikt, cls)

    @property
    def adrf_id(self):
        """Gets the adrf_id of this NnwdafDataManagementSubsc.

        String uniquely identifying a NF instance. The format of the NF Instance ID shall be a  Universally Unique Identifier (UUID) version 4, as described in IETF RFC 4122.    # noqa: E501

        :return: The adrf_id of this NnwdafDataManagementSubsc.
        :rtype: str
        """
        return self._adrf_id

    @adrf_id.setter
    def adrf_id(self, adrf_id):
        """Sets the adrf_id of this NnwdafDataManagementSubsc.

        String uniquely identifying a NF instance. The format of the NF Instance ID shall be a  Universally Unique Identifier (UUID) version 4, as described in IETF RFC 4122.    # noqa: E501

        :param adrf_id: The adrf_id of this NnwdafDataManagementSubsc.
        :type adrf_id: str
        """

        self._adrf_id = adrf_id

    @property
    def adrf_set_id(self):
        """Gets the adrf_set_id of this NnwdafDataManagementSubsc.

        NF Set Identifier (see clause 28.12 of 3GPP TS 23.003), formatted as the following string \"set<Set ID>.<nftype>set.5gc.mnc<MNC>.mcc<MCC>\", or  \"set<SetID>.<NFType>set.5gc.nid<NID>.mnc<MNC>.mcc<MCC>\" with  <MCC> encoded as defined in clause 5.4.2 (\"Mcc\" data type definition)  <MNC> encoding the Mobile Network Code part of the PLMN, comprising 3 digits.    If there are only 2 significant digits in the MNC, one \"0\" digit shall be inserted    at the left side to fill the 3 digits coding of MNC.  Pattern: '^[0-9]{3}$' <NFType> encoded as a value defined in Table 6.1.6.3.3-1 of 3GPP TS 29.510 but    with lower case characters <Set ID> encoded as a string of characters consisting of    alphabetic characters (A-Z and a-z), digits (0-9) and/or the hyphen (-) and that    shall end with either an alphabetic character or a digit.    # noqa: E501

        :return: The adrf_set_id of this NnwdafDataManagementSubsc.
        :rtype: str
        """
        return self._adrf_set_id

    @adrf_set_id.setter
    def adrf_set_id(self, adrf_set_id):
        """Sets the adrf_set_id of this NnwdafDataManagementSubsc.

        NF Set Identifier (see clause 28.12 of 3GPP TS 23.003), formatted as the following string \"set<Set ID>.<nftype>set.5gc.mnc<MNC>.mcc<MCC>\", or  \"set<SetID>.<NFType>set.5gc.nid<NID>.mnc<MNC>.mcc<MCC>\" with  <MCC> encoded as defined in clause 5.4.2 (\"Mcc\" data type definition)  <MNC> encoding the Mobile Network Code part of the PLMN, comprising 3 digits.    If there are only 2 significant digits in the MNC, one \"0\" digit shall be inserted    at the left side to fill the 3 digits coding of MNC.  Pattern: '^[0-9]{3}$' <NFType> encoded as a value defined in Table 6.1.6.3.3-1 of 3GPP TS 29.510 but    with lower case characters <Set ID> encoded as a string of characters consisting of    alphabetic characters (A-Z and a-z), digits (0-9) and/or the hyphen (-) and that    shall end with either an alphabetic character or a digit.    # noqa: E501

        :param adrf_set_id: The adrf_set_id of this NnwdafDataManagementSubsc.
        :type adrf_set_id: str
        """

        self._adrf_set_id = adrf_set_id

    @property
    def ana_sub(self):
        """Gets the ana_sub of this NnwdafDataManagementSubsc.


        :return: The ana_sub of this NnwdafDataManagementSubsc.
        :rtype: NnwdafEventsSubscription
        """
        return self._ana_sub

    @ana_sub.setter
    def ana_sub(self, ana_sub):
        """Sets the ana_sub of this NnwdafDataManagementSubsc.


        :param ana_sub: The ana_sub of this NnwdafDataManagementSubsc.
        :type ana_sub: NnwdafEventsSubscription
        """

        self._ana_sub = ana_sub

    @property
    def data_collect_purposes(self):
        """Gets the data_collect_purposes of this NnwdafDataManagementSubsc.

        The purposes of data collection. This attribute may only be provided if user consent is reqiured depending on local policy and regulations and the consumer has not checked user consent.   # noqa: E501

        :return: The data_collect_purposes of this NnwdafDataManagementSubsc.
        :rtype: List[DataCollectionPurpose]
        """
        return self._data_collect_purposes

    @data_collect_purposes.setter
    def data_collect_purposes(self, data_collect_purposes):
        """Sets the data_collect_purposes of this NnwdafDataManagementSubsc.

        The purposes of data collection. This attribute may only be provided if user consent is reqiured depending on local policy and regulations and the consumer has not checked user consent.   # noqa: E501

        :param data_collect_purposes: The data_collect_purposes of this NnwdafDataManagementSubsc.
        :type data_collect_purposes: List[DataCollectionPurpose]
        """
        if data_collect_purposes is not None and len(data_collect_purposes) < 1:
            raise ValueError("Invalid value for `data_collect_purposes`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._data_collect_purposes = data_collect_purposes

    @property
    def checked_consent_ind(self):
        """Gets the checked_consent_ind of this NnwdafDataManagementSubsc.

        Indication that the NF service consumer has already checked the user consent.  # noqa: E501

        :return: The checked_consent_ind of this NnwdafDataManagementSubsc.
        :rtype: bool
        """
        return self._checked_consent_ind

    @checked_consent_ind.setter
    def checked_consent_ind(self, checked_consent_ind):
        """Sets the checked_consent_ind of this NnwdafDataManagementSubsc.

        Indication that the NF service consumer has already checked the user consent.  # noqa: E501

        :param checked_consent_ind: The checked_consent_ind of this NnwdafDataManagementSubsc.
        :type checked_consent_ind: bool
        """

        self._checked_consent_ind = checked_consent_ind

    @property
    def data_sub(self):
        """Gets the data_sub of this NnwdafDataManagementSubsc.


        :return: The data_sub of this NnwdafDataManagementSubsc.
        :rtype: DataSubscription
        """
        return self._data_sub

    @data_sub.setter
    def data_sub(self, data_sub):
        """Sets the data_sub of this NnwdafDataManagementSubsc.


        :param data_sub: The data_sub of this NnwdafDataManagementSubsc.
        :type data_sub: DataSubscription
        """

        self._data_sub = data_sub

    @property
    def format_instruct(self):
        """Gets the format_instruct of this NnwdafDataManagementSubsc.


        :return: The format_instruct of this NnwdafDataManagementSubsc.
        :rtype: FormattingInstruction
        """
        return self._format_instruct

    @format_instruct.setter
    def format_instruct(self, format_instruct):
        """Sets the format_instruct of this NnwdafDataManagementSubsc.


        :param format_instruct: The format_instruct of this NnwdafDataManagementSubsc.
        :type format_instruct: FormattingInstruction
        """

        self._format_instruct = format_instruct

    @property
    def notif_corr_id(self):
        """Gets the notif_corr_id of this NnwdafDataManagementSubsc.

        Notification correlation identifier.  # noqa: E501

        :return: The notif_corr_id of this NnwdafDataManagementSubsc.
        :rtype: str
        """
        return self._notif_corr_id

    @notif_corr_id.setter
    def notif_corr_id(self, notif_corr_id):
        """Sets the notif_corr_id of this NnwdafDataManagementSubsc.

        Notification correlation identifier.  # noqa: E501

        :param notif_corr_id: The notif_corr_id of this NnwdafDataManagementSubsc.
        :type notif_corr_id: str
        """
        if notif_corr_id is None:
            raise ValueError("Invalid value for `notif_corr_id`, must not be `None`")  # noqa: E501

        self._notif_corr_id = notif_corr_id

    @property
    def notific_uri(self):
        """Gets the notific_uri of this NnwdafDataManagementSubsc.

        String providing an URI formatted according to RFC 3986.  # noqa: E501

        :return: The notific_uri of this NnwdafDataManagementSubsc.
        :rtype: str
        """
        return self._notific_uri

    @notific_uri.setter
    def notific_uri(self, notific_uri):
        """Sets the notific_uri of this NnwdafDataManagementSubsc.

        String providing an URI formatted according to RFC 3986.  # noqa: E501

        :param notific_uri: The notific_uri of this NnwdafDataManagementSubsc.
        :type notific_uri: str
        """
        if notific_uri is None:
            raise ValueError("Invalid value for `notific_uri`, must not be `None`")  # noqa: E501

        self._notific_uri = notific_uri

    @property
    def proc_instruct(self):
        """Gets the proc_instruct of this NnwdafDataManagementSubsc.


        :return: The proc_instruct of this NnwdafDataManagementSubsc.
        :rtype: ProcessingInstruction
        """
        return self._proc_instruct

    @proc_instruct.setter
    def proc_instruct(self, proc_instruct):
        """Sets the proc_instruct of this NnwdafDataManagementSubsc.


        :param proc_instruct: The proc_instruct of this NnwdafDataManagementSubsc.
        :type proc_instruct: ProcessingInstruction
        """

        self._proc_instruct = proc_instruct

    @property
    def multi_proc_instructs(self):
        """Gets the multi_proc_instructs of this NnwdafDataManagementSubsc.

        Processing instructions to be used for sending event notifications.  # noqa: E501

        :return: The multi_proc_instructs of this NnwdafDataManagementSubsc.
        :rtype: List[ProcessingInstruction]
        """
        return self._multi_proc_instructs

    @multi_proc_instructs.setter
    def multi_proc_instructs(self, multi_proc_instructs):
        """Sets the multi_proc_instructs of this NnwdafDataManagementSubsc.

        Processing instructions to be used for sending event notifications.  # noqa: E501

        :param multi_proc_instructs: The multi_proc_instructs of this NnwdafDataManagementSubsc.
        :type multi_proc_instructs: List[ProcessingInstruction]
        """
        if multi_proc_instructs is not None and len(multi_proc_instructs) < 1:
            raise ValueError("Invalid value for `multi_proc_instructs`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._multi_proc_instructs = multi_proc_instructs

    @property
    def supp_feat(self):
        """Gets the supp_feat of this NnwdafDataManagementSubsc.

        A string used to indicate the features supported by an API that is used as defined in clause  6.6 in 3GPP TS 29.500. The string shall contain a bitmask indicating supported features in  hexadecimal representation Each character in the string shall take a value of \"0\" to \"9\",  \"a\" to \"f\" or \"A\" to \"F\" and shall represent the support of 4 features as described in  table 5.2.2-3. The most significant character representing the highest-numbered features shall  appear first in the string, and the character representing features 1 to 4 shall appear last  in the string. The list of features and their numbering (starting with 1) are defined  separately for each API. If the string contains a lower number of characters than there are  defined features for an API, all features that would be represented by characters that are not  present in the string are not supported.   # noqa: E501

        :return: The supp_feat of this NnwdafDataManagementSubsc.
        :rtype: str
        """
        return self._supp_feat

    @supp_feat.setter
    def supp_feat(self, supp_feat):
        """Sets the supp_feat of this NnwdafDataManagementSubsc.

        A string used to indicate the features supported by an API that is used as defined in clause  6.6 in 3GPP TS 29.500. The string shall contain a bitmask indicating supported features in  hexadecimal representation Each character in the string shall take a value of \"0\" to \"9\",  \"a\" to \"f\" or \"A\" to \"F\" and shall represent the support of 4 features as described in  table 5.2.2-3. The most significant character representing the highest-numbered features shall  appear first in the string, and the character representing features 1 to 4 shall appear last  in the string. The list of features and their numbering (starting with 1) are defined  separately for each API. If the string contains a lower number of characters than there are  defined features for an API, all features that would be represented by characters that are not  present in the string are not supported.   # noqa: E501

        :param supp_feat: The supp_feat of this NnwdafDataManagementSubsc.
        :type supp_feat: str
        """
        if supp_feat is not None and not re.search(r'^[A-Fa-f0-9]*$', supp_feat):  # noqa: E501
            raise ValueError("Invalid value for `supp_feat`, must be a follow pattern or equal to `/^[A-Fa-f0-9]*$/`")  # noqa: E501

        self._supp_feat = supp_feat

    @property
    def target_nf_id(self):
        """Gets the target_nf_id of this NnwdafDataManagementSubsc.

        String uniquely identifying a NF instance. The format of the NF Instance ID shall be a  Universally Unique Identifier (UUID) version 4, as described in IETF RFC 4122.    # noqa: E501

        :return: The target_nf_id of this NnwdafDataManagementSubsc.
        :rtype: str
        """
        return self._target_nf_id

    @target_nf_id.setter
    def target_nf_id(self, target_nf_id):
        """Sets the target_nf_id of this NnwdafDataManagementSubsc.

        String uniquely identifying a NF instance. The format of the NF Instance ID shall be a  Universally Unique Identifier (UUID) version 4, as described in IETF RFC 4122.    # noqa: E501

        :param target_nf_id: The target_nf_id of this NnwdafDataManagementSubsc.
        :type target_nf_id: str
        """

        self._target_nf_id = target_nf_id

    @property
    def target_nf_set_id(self):
        """Gets the target_nf_set_id of this NnwdafDataManagementSubsc.

        NF Set Identifier (see clause 28.12 of 3GPP TS 23.003), formatted as the following string \"set<Set ID>.<nftype>set.5gc.mnc<MNC>.mcc<MCC>\", or  \"set<SetID>.<NFType>set.5gc.nid<NID>.mnc<MNC>.mcc<MCC>\" with  <MCC> encoded as defined in clause 5.4.2 (\"Mcc\" data type definition)  <MNC> encoding the Mobile Network Code part of the PLMN, comprising 3 digits.    If there are only 2 significant digits in the MNC, one \"0\" digit shall be inserted    at the left side to fill the 3 digits coding of MNC.  Pattern: '^[0-9]{3}$' <NFType> encoded as a value defined in Table 6.1.6.3.3-1 of 3GPP TS 29.510 but    with lower case characters <Set ID> encoded as a string of characters consisting of    alphabetic characters (A-Z and a-z), digits (0-9) and/or the hyphen (-) and that    shall end with either an alphabetic character or a digit.    # noqa: E501

        :return: The target_nf_set_id of this NnwdafDataManagementSubsc.
        :rtype: str
        """
        return self._target_nf_set_id

    @target_nf_set_id.setter
    def target_nf_set_id(self, target_nf_set_id):
        """Sets the target_nf_set_id of this NnwdafDataManagementSubsc.

        NF Set Identifier (see clause 28.12 of 3GPP TS 23.003), formatted as the following string \"set<Set ID>.<nftype>set.5gc.mnc<MNC>.mcc<MCC>\", or  \"set<SetID>.<NFType>set.5gc.nid<NID>.mnc<MNC>.mcc<MCC>\" with  <MCC> encoded as defined in clause 5.4.2 (\"Mcc\" data type definition)  <MNC> encoding the Mobile Network Code part of the PLMN, comprising 3 digits.    If there are only 2 significant digits in the MNC, one \"0\" digit shall be inserted    at the left side to fill the 3 digits coding of MNC.  Pattern: '^[0-9]{3}$' <NFType> encoded as a value defined in Table 6.1.6.3.3-1 of 3GPP TS 29.510 but    with lower case characters <Set ID> encoded as a string of characters consisting of    alphabetic characters (A-Z and a-z), digits (0-9) and/or the hyphen (-) and that    shall end with either an alphabetic character or a digit.    # noqa: E501

        :param target_nf_set_id: The target_nf_set_id of this NnwdafDataManagementSubsc.
        :type target_nf_set_id: str
        """

        self._target_nf_set_id = target_nf_set_id

    @property
    def time_period(self):
        """Gets the time_period of this NnwdafDataManagementSubsc.


        :return: The time_period of this NnwdafDataManagementSubsc.
        :rtype: TimeWindow
        """
        return self._time_period

    @time_period.setter
    def time_period(self, time_period):
        """Sets the time_period of this NnwdafDataManagementSubsc.


        :param time_period: The time_period of this NnwdafDataManagementSubsc.
        :type time_period: TimeWindow
        """

        self._time_period = time_period
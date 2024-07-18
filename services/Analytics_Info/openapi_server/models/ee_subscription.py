# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.context_info import ContextInfo
from openapi_server.models.monitoring_configuration import MonitoringConfiguration
from openapi_server.models.reporting_options import ReportingOptions
import re
from openapi_server import util

from openapi_server.models.context_info import ContextInfo  # noqa: E501
from openapi_server.models.monitoring_configuration import MonitoringConfiguration  # noqa: E501
from openapi_server.models.reporting_options import ReportingOptions  # noqa: E501
import re  # noqa: E501

class EeSubscription(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, callback_reference=None, monitoring_configurations=None, reporting_options=None, supported_features=None, subscription_id=None, context_info=None, epc_applied_ind=False, scef_diam_host=None, scef_diam_realm=None, notify_correlation_id=None, second_callback_ref=None, gpsi=None, exclude_gpsi_list=None, include_gpsi_list=None, data_restoration_callback_uri=None):  # noqa: E501
        """EeSubscription - a model defined in OpenAPI

        :param callback_reference: The callback_reference of this EeSubscription.  # noqa: E501
        :type callback_reference: str
        :param monitoring_configurations: The monitoring_configurations of this EeSubscription.  # noqa: E501
        :type monitoring_configurations: Dict[str, MonitoringConfiguration]
        :param reporting_options: The reporting_options of this EeSubscription.  # noqa: E501
        :type reporting_options: ReportingOptions
        :param supported_features: The supported_features of this EeSubscription.  # noqa: E501
        :type supported_features: str
        :param subscription_id: The subscription_id of this EeSubscription.  # noqa: E501
        :type subscription_id: str
        :param context_info: The context_info of this EeSubscription.  # noqa: E501
        :type context_info: ContextInfo
        :param epc_applied_ind: The epc_applied_ind of this EeSubscription.  # noqa: E501
        :type epc_applied_ind: bool
        :param scef_diam_host: The scef_diam_host of this EeSubscription.  # noqa: E501
        :type scef_diam_host: str
        :param scef_diam_realm: The scef_diam_realm of this EeSubscription.  # noqa: E501
        :type scef_diam_realm: str
        :param notify_correlation_id: The notify_correlation_id of this EeSubscription.  # noqa: E501
        :type notify_correlation_id: str
        :param second_callback_ref: The second_callback_ref of this EeSubscription.  # noqa: E501
        :type second_callback_ref: str
        :param gpsi: The gpsi of this EeSubscription.  # noqa: E501
        :type gpsi: str
        :param exclude_gpsi_list: The exclude_gpsi_list of this EeSubscription.  # noqa: E501
        :type exclude_gpsi_list: List[str]
        :param include_gpsi_list: The include_gpsi_list of this EeSubscription.  # noqa: E501
        :type include_gpsi_list: List[str]
        :param data_restoration_callback_uri: The data_restoration_callback_uri of this EeSubscription.  # noqa: E501
        :type data_restoration_callback_uri: str
        """
        self.openapi_types = {
            'callback_reference': str,
            'monitoring_configurations': Dict[str, MonitoringConfiguration],
            'reporting_options': ReportingOptions,
            'supported_features': str,
            'subscription_id': str,
            'context_info': ContextInfo,
            'epc_applied_ind': bool,
            'scef_diam_host': str,
            'scef_diam_realm': str,
            'notify_correlation_id': str,
            'second_callback_ref': str,
            'gpsi': str,
            'exclude_gpsi_list': List[str],
            'include_gpsi_list': List[str],
            'data_restoration_callback_uri': str
        }

        self.attribute_map = {
            'callback_reference': 'callbackReference',
            'monitoring_configurations': 'monitoringConfigurations',
            'reporting_options': 'reportingOptions',
            'supported_features': 'supportedFeatures',
            'subscription_id': 'subscriptionId',
            'context_info': 'contextInfo',
            'epc_applied_ind': 'epcAppliedInd',
            'scef_diam_host': 'scefDiamHost',
            'scef_diam_realm': 'scefDiamRealm',
            'notify_correlation_id': 'notifyCorrelationId',
            'second_callback_ref': 'secondCallbackRef',
            'gpsi': 'gpsi',
            'exclude_gpsi_list': 'excludeGpsiList',
            'include_gpsi_list': 'includeGpsiList',
            'data_restoration_callback_uri': 'dataRestorationCallbackUri'
        }

        self._callback_reference = callback_reference
        self._monitoring_configurations = monitoring_configurations
        self._reporting_options = reporting_options
        self._supported_features = supported_features
        self._subscription_id = subscription_id
        self._context_info = context_info
        self._epc_applied_ind = epc_applied_ind
        self._scef_diam_host = scef_diam_host
        self._scef_diam_realm = scef_diam_realm
        self._notify_correlation_id = notify_correlation_id
        self._second_callback_ref = second_callback_ref
        self._gpsi = gpsi
        self._exclude_gpsi_list = exclude_gpsi_list
        self._include_gpsi_list = include_gpsi_list
        self._data_restoration_callback_uri = data_restoration_callback_uri

    @classmethod
    def from_dict(cls, dikt) -> 'EeSubscription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EeSubscription of this EeSubscription.  # noqa: E501
        :rtype: EeSubscription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def callback_reference(self):
        """Gets the callback_reference of this EeSubscription.

        String providing an URI formatted according to RFC 3986.  # noqa: E501

        :return: The callback_reference of this EeSubscription.
        :rtype: str
        """
        return self._callback_reference

    @callback_reference.setter
    def callback_reference(self, callback_reference):
        """Sets the callback_reference of this EeSubscription.

        String providing an URI formatted according to RFC 3986.  # noqa: E501

        :param callback_reference: The callback_reference of this EeSubscription.
        :type callback_reference: str
        """
        if callback_reference is None:
            raise ValueError("Invalid value for `callback_reference`, must not be `None`")  # noqa: E501

        self._callback_reference = callback_reference

    @property
    def monitoring_configurations(self):
        """Gets the monitoring_configurations of this EeSubscription.

        A map (list of key-value pairs where ReferenceId serves as key) of MonitoringConfigurations  # noqa: E501

        :return: The monitoring_configurations of this EeSubscription.
        :rtype: Dict[str, MonitoringConfiguration]
        """
        return self._monitoring_configurations

    @monitoring_configurations.setter
    def monitoring_configurations(self, monitoring_configurations):
        """Sets the monitoring_configurations of this EeSubscription.

        A map (list of key-value pairs where ReferenceId serves as key) of MonitoringConfigurations  # noqa: E501

        :param monitoring_configurations: The monitoring_configurations of this EeSubscription.
        :type monitoring_configurations: Dict[str, MonitoringConfiguration]
        """
        if monitoring_configurations is None:
            raise ValueError("Invalid value for `monitoring_configurations`, must not be `None`")  # noqa: E501
        if monitoring_configurations is not None and len(monitoring_configurations) < 1:
            raise ValueError("Invalid value for `monitoring_configurations`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._monitoring_configurations = monitoring_configurations

    @property
    def reporting_options(self):
        """Gets the reporting_options of this EeSubscription.


        :return: The reporting_options of this EeSubscription.
        :rtype: ReportingOptions
        """
        return self._reporting_options

    @reporting_options.setter
    def reporting_options(self, reporting_options):
        """Sets the reporting_options of this EeSubscription.


        :param reporting_options: The reporting_options of this EeSubscription.
        :type reporting_options: ReportingOptions
        """

        self._reporting_options = reporting_options

    @property
    def supported_features(self):
        """Gets the supported_features of this EeSubscription.

        A string used to indicate the features supported by an API that is used as defined in clause  6.6 in 3GPP TS 29.500. The string shall contain a bitmask indicating supported features in  hexadecimal representation Each character in the string shall take a value of \"0\" to \"9\",  \"a\" to \"f\" or \"A\" to \"F\" and shall represent the support of 4 features as described in  table 5.2.2-3. The most significant character representing the highest-numbered features shall  appear first in the string, and the character representing features 1 to 4 shall appear last  in the string. The list of features and their numbering (starting with 1) are defined  separately for each API. If the string contains a lower number of characters than there are  defined features for an API, all features that would be represented by characters that are not  present in the string are not supported.   # noqa: E501

        :return: The supported_features of this EeSubscription.
        :rtype: str
        """
        return self._supported_features

    @supported_features.setter
    def supported_features(self, supported_features):
        """Sets the supported_features of this EeSubscription.

        A string used to indicate the features supported by an API that is used as defined in clause  6.6 in 3GPP TS 29.500. The string shall contain a bitmask indicating supported features in  hexadecimal representation Each character in the string shall take a value of \"0\" to \"9\",  \"a\" to \"f\" or \"A\" to \"F\" and shall represent the support of 4 features as described in  table 5.2.2-3. The most significant character representing the highest-numbered features shall  appear first in the string, and the character representing features 1 to 4 shall appear last  in the string. The list of features and their numbering (starting with 1) are defined  separately for each API. If the string contains a lower number of characters than there are  defined features for an API, all features that would be represented by characters that are not  present in the string are not supported.   # noqa: E501

        :param supported_features: The supported_features of this EeSubscription.
        :type supported_features: str
        """
        if supported_features is not None and not re.search(r'^[A-Fa-f0-9]*$', supported_features):  # noqa: E501
            raise ValueError("Invalid value for `supported_features`, must be a follow pattern or equal to `/^[A-Fa-f0-9]*$/`")  # noqa: E501

        self._supported_features = supported_features

    @property
    def subscription_id(self):
        """Gets the subscription_id of this EeSubscription.


        :return: The subscription_id of this EeSubscription.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this EeSubscription.


        :param subscription_id: The subscription_id of this EeSubscription.
        :type subscription_id: str
        """

        self._subscription_id = subscription_id

    @property
    def context_info(self):
        """Gets the context_info of this EeSubscription.


        :return: The context_info of this EeSubscription.
        :rtype: ContextInfo
        """
        return self._context_info

    @context_info.setter
    def context_info(self, context_info):
        """Sets the context_info of this EeSubscription.


        :param context_info: The context_info of this EeSubscription.
        :type context_info: ContextInfo
        """

        self._context_info = context_info

    @property
    def epc_applied_ind(self):
        """Gets the epc_applied_ind of this EeSubscription.


        :return: The epc_applied_ind of this EeSubscription.
        :rtype: bool
        """
        return self._epc_applied_ind

    @epc_applied_ind.setter
    def epc_applied_ind(self, epc_applied_ind):
        """Sets the epc_applied_ind of this EeSubscription.


        :param epc_applied_ind: The epc_applied_ind of this EeSubscription.
        :type epc_applied_ind: bool
        """

        self._epc_applied_ind = epc_applied_ind

    @property
    def scef_diam_host(self):
        """Gets the scef_diam_host of this EeSubscription.

        Fully Qualified Domain Name  # noqa: E501

        :return: The scef_diam_host of this EeSubscription.
        :rtype: str
        """
        return self._scef_diam_host

    @scef_diam_host.setter
    def scef_diam_host(self, scef_diam_host):
        """Sets the scef_diam_host of this EeSubscription.

        Fully Qualified Domain Name  # noqa: E501

        :param scef_diam_host: The scef_diam_host of this EeSubscription.
        :type scef_diam_host: str
        """
        if scef_diam_host is not None and len(scef_diam_host) > 253:
            raise ValueError("Invalid value for `scef_diam_host`, length must be less than or equal to `253`")  # noqa: E501
        if scef_diam_host is not None and len(scef_diam_host) < 4:
            raise ValueError("Invalid value for `scef_diam_host`, length must be greater than or equal to `4`")  # noqa: E501
        if scef_diam_host is not None and not re.search(r'^([0-9A-Za-z]([-0-9A-Za-z]{0,61}[0-9A-Za-z])?\.)+[A-Za-z]{2,63}\.?$', scef_diam_host):  # noqa: E501
            raise ValueError("Invalid value for `scef_diam_host`, must be a follow pattern or equal to `/^([0-9A-Za-z]([-0-9A-Za-z]{0,61}[0-9A-Za-z])?\.)+[A-Za-z]{2,63}\.?$/`")  # noqa: E501

        self._scef_diam_host = scef_diam_host

    @property
    def scef_diam_realm(self):
        """Gets the scef_diam_realm of this EeSubscription.

        Fully Qualified Domain Name  # noqa: E501

        :return: The scef_diam_realm of this EeSubscription.
        :rtype: str
        """
        return self._scef_diam_realm

    @scef_diam_realm.setter
    def scef_diam_realm(self, scef_diam_realm):
        """Sets the scef_diam_realm of this EeSubscription.

        Fully Qualified Domain Name  # noqa: E501

        :param scef_diam_realm: The scef_diam_realm of this EeSubscription.
        :type scef_diam_realm: str
        """
        if scef_diam_realm is not None and len(scef_diam_realm) > 253:
            raise ValueError("Invalid value for `scef_diam_realm`, length must be less than or equal to `253`")  # noqa: E501
        if scef_diam_realm is not None and len(scef_diam_realm) < 4:
            raise ValueError("Invalid value for `scef_diam_realm`, length must be greater than or equal to `4`")  # noqa: E501
        if scef_diam_realm is not None and not re.search(r'^([0-9A-Za-z]([-0-9A-Za-z]{0,61}[0-9A-Za-z])?\.)+[A-Za-z]{2,63}\.?$', scef_diam_realm):  # noqa: E501
            raise ValueError("Invalid value for `scef_diam_realm`, must be a follow pattern or equal to `/^([0-9A-Za-z]([-0-9A-Za-z]{0,61}[0-9A-Za-z])?\.)+[A-Za-z]{2,63}\.?$/`")  # noqa: E501

        self._scef_diam_realm = scef_diam_realm

    @property
    def notify_correlation_id(self):
        """Gets the notify_correlation_id of this EeSubscription.


        :return: The notify_correlation_id of this EeSubscription.
        :rtype: str
        """
        return self._notify_correlation_id

    @notify_correlation_id.setter
    def notify_correlation_id(self, notify_correlation_id):
        """Sets the notify_correlation_id of this EeSubscription.


        :param notify_correlation_id: The notify_correlation_id of this EeSubscription.
        :type notify_correlation_id: str
        """

        self._notify_correlation_id = notify_correlation_id

    @property
    def second_callback_ref(self):
        """Gets the second_callback_ref of this EeSubscription.

        String providing an URI formatted according to RFC 3986.  # noqa: E501

        :return: The second_callback_ref of this EeSubscription.
        :rtype: str
        """
        return self._second_callback_ref

    @second_callback_ref.setter
    def second_callback_ref(self, second_callback_ref):
        """Sets the second_callback_ref of this EeSubscription.

        String providing an URI formatted according to RFC 3986.  # noqa: E501

        :param second_callback_ref: The second_callback_ref of this EeSubscription.
        :type second_callback_ref: str
        """

        self._second_callback_ref = second_callback_ref

    @property
    def gpsi(self):
        """Gets the gpsi of this EeSubscription.

        String identifying a Gpsi shall contain either an External Id or an MSISDN.  It shall be formatted as follows -External Identifier= \"extid-'extid', where 'extid'  shall be formatted according to clause 19.7.2 of 3GPP TS 23.003 that describes an  External Identifier.    # noqa: E501

        :return: The gpsi of this EeSubscription.
        :rtype: str
        """
        return self._gpsi

    @gpsi.setter
    def gpsi(self, gpsi):
        """Sets the gpsi of this EeSubscription.

        String identifying a Gpsi shall contain either an External Id or an MSISDN.  It shall be formatted as follows -External Identifier= \"extid-'extid', where 'extid'  shall be formatted according to clause 19.7.2 of 3GPP TS 23.003 that describes an  External Identifier.    # noqa: E501

        :param gpsi: The gpsi of this EeSubscription.
        :type gpsi: str
        """
        if gpsi is not None and not re.search(r'^(msisdn-[0-9]{5,15}|extid-[^@]+@[^@]+|.+)$', gpsi):  # noqa: E501
            raise ValueError("Invalid value for `gpsi`, must be a follow pattern or equal to `/^(msisdn-[0-9]{5,15}|extid-[^@]+@[^@]+|.+)$/`")  # noqa: E501

        self._gpsi = gpsi

    @property
    def exclude_gpsi_list(self):
        """Gets the exclude_gpsi_list of this EeSubscription.


        :return: The exclude_gpsi_list of this EeSubscription.
        :rtype: List[str]
        """
        return self._exclude_gpsi_list

    @exclude_gpsi_list.setter
    def exclude_gpsi_list(self, exclude_gpsi_list):
        """Sets the exclude_gpsi_list of this EeSubscription.


        :param exclude_gpsi_list: The exclude_gpsi_list of this EeSubscription.
        :type exclude_gpsi_list: List[str]
        """
        if exclude_gpsi_list is not None and len(exclude_gpsi_list) < 1:
            raise ValueError("Invalid value for `exclude_gpsi_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._exclude_gpsi_list = exclude_gpsi_list

    @property
    def include_gpsi_list(self):
        """Gets the include_gpsi_list of this EeSubscription.


        :return: The include_gpsi_list of this EeSubscription.
        :rtype: List[str]
        """
        return self._include_gpsi_list

    @include_gpsi_list.setter
    def include_gpsi_list(self, include_gpsi_list):
        """Sets the include_gpsi_list of this EeSubscription.


        :param include_gpsi_list: The include_gpsi_list of this EeSubscription.
        :type include_gpsi_list: List[str]
        """
        if include_gpsi_list is not None and len(include_gpsi_list) < 1:
            raise ValueError("Invalid value for `include_gpsi_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._include_gpsi_list = include_gpsi_list

    @property
    def data_restoration_callback_uri(self):
        """Gets the data_restoration_callback_uri of this EeSubscription.

        String providing an URI formatted according to RFC 3986.  # noqa: E501

        :return: The data_restoration_callback_uri of this EeSubscription.
        :rtype: str
        """
        return self._data_restoration_callback_uri

    @data_restoration_callback_uri.setter
    def data_restoration_callback_uri(self, data_restoration_callback_uri):
        """Sets the data_restoration_callback_uri of this EeSubscription.

        String providing an URI formatted according to RFC 3986.  # noqa: E501

        :param data_restoration_callback_uri: The data_restoration_callback_uri of this EeSubscription.
        :type data_restoration_callback_uri: str
        """

        self._data_restoration_callback_uri = data_restoration_callback_uri

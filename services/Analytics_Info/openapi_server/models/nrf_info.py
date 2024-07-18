# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.dccf_info import DccfInfo
from openapi_server.models.easdf_info import EasdfInfo
from openapi_server.models.mb_upf_info import MbUpfInfo
from openapi_server.models.mfaf_info import MfafInfo
from openapi_server.models.model5_g_ddnmf_info import Model5GDdnmfInfo
from openapi_server.models.nf_info import NfInfo
from openapi_server.models.nrf_info_served_aanf_info_list_value_value import NrfInfoServedAanfInfoListValueValue
from openapi_server.models.nrf_info_served_amf_info_value import NrfInfoServedAmfInfoValue
from openapi_server.models.nrf_info_served_ausf_info_value import NrfInfoServedAusfInfoValue
from openapi_server.models.nrf_info_served_bsf_info_value import NrfInfoServedBsfInfoValue
from openapi_server.models.nrf_info_served_chf_info_value import NrfInfoServedChfInfoValue
from openapi_server.models.nrf_info_served_gmlc_info_value import NrfInfoServedGmlcInfoValue
from openapi_server.models.nrf_info_served_hss_info_list_value_value import NrfInfoServedHssInfoListValueValue
from openapi_server.models.nrf_info_served_lmf_info_value import NrfInfoServedLmfInfoValue
from openapi_server.models.nrf_info_served_mb_smf_info_list_value_value import NrfInfoServedMbSmfInfoListValueValue
from openapi_server.models.nrf_info_served_nef_info_value import NrfInfoServedNefInfoValue
from openapi_server.models.nrf_info_served_nwdaf_info_value import NrfInfoServedNwdafInfoValue
from openapi_server.models.nrf_info_served_pcf_info_value import NrfInfoServedPcfInfoValue
from openapi_server.models.nrf_info_served_pcscf_info_list_value_value import NrfInfoServedPcscfInfoListValueValue
from openapi_server.models.nrf_info_served_scp_info_list_value import NrfInfoServedScpInfoListValue
from openapi_server.models.nrf_info_served_sepp_info_list_value import NrfInfoServedSeppInfoListValue
from openapi_server.models.nrf_info_served_smf_info_value import NrfInfoServedSmfInfoValue
from openapi_server.models.nrf_info_served_udm_info_value import NrfInfoServedUdmInfoValue
from openapi_server.models.nrf_info_served_udr_info_value import NrfInfoServedUdrInfoValue
from openapi_server.models.nrf_info_served_udsf_info_value import NrfInfoServedUdsfInfoValue
from openapi_server.models.nrf_info_served_upf_info_value import NrfInfoServedUpfInfoValue
from openapi_server.models.nssaaf_info import NssaafInfo
from openapi_server.models.nwdaf_info import NwdafInfo
from openapi_server.models.trust_af_info import TrustAfInfo
from openapi_server.models.tsctsf_info import TsctsfInfo
from openapi_server import util

from openapi_server.models.dccf_info import DccfInfo  # noqa: E501
from openapi_server.models.easdf_info import EasdfInfo  # noqa: E501
from openapi_server.models.mb_upf_info import MbUpfInfo  # noqa: E501
from openapi_server.models.mfaf_info import MfafInfo  # noqa: E501
from openapi_server.models.model5_g_ddnmf_info import Model5GDdnmfInfo  # noqa: E501
from openapi_server.models.nf_info import NfInfo  # noqa: E501
from openapi_server.models.nrf_info_served_aanf_info_list_value_value import NrfInfoServedAanfInfoListValueValue  # noqa: E501
from openapi_server.models.nrf_info_served_amf_info_value import NrfInfoServedAmfInfoValue  # noqa: E501
from openapi_server.models.nrf_info_served_ausf_info_value import NrfInfoServedAusfInfoValue  # noqa: E501
from openapi_server.models.nrf_info_served_bsf_info_value import NrfInfoServedBsfInfoValue  # noqa: E501
from openapi_server.models.nrf_info_served_chf_info_value import NrfInfoServedChfInfoValue  # noqa: E501
from openapi_server.models.nrf_info_served_gmlc_info_value import NrfInfoServedGmlcInfoValue  # noqa: E501
from openapi_server.models.nrf_info_served_hss_info_list_value_value import NrfInfoServedHssInfoListValueValue  # noqa: E501
from openapi_server.models.nrf_info_served_lmf_info_value import NrfInfoServedLmfInfoValue  # noqa: E501
from openapi_server.models.nrf_info_served_mb_smf_info_list_value_value import NrfInfoServedMbSmfInfoListValueValue  # noqa: E501
from openapi_server.models.nrf_info_served_nef_info_value import NrfInfoServedNefInfoValue  # noqa: E501
from openapi_server.models.nrf_info_served_nwdaf_info_value import NrfInfoServedNwdafInfoValue  # noqa: E501
from openapi_server.models.nrf_info_served_pcf_info_value import NrfInfoServedPcfInfoValue  # noqa: E501
from openapi_server.models.nrf_info_served_pcscf_info_list_value_value import NrfInfoServedPcscfInfoListValueValue  # noqa: E501
from openapi_server.models.nrf_info_served_scp_info_list_value import NrfInfoServedScpInfoListValue  # noqa: E501
from openapi_server.models.nrf_info_served_sepp_info_list_value import NrfInfoServedSeppInfoListValue  # noqa: E501
from openapi_server.models.nrf_info_served_smf_info_value import NrfInfoServedSmfInfoValue  # noqa: E501
from openapi_server.models.nrf_info_served_udm_info_value import NrfInfoServedUdmInfoValue  # noqa: E501
from openapi_server.models.nrf_info_served_udr_info_value import NrfInfoServedUdrInfoValue  # noqa: E501
from openapi_server.models.nrf_info_served_udsf_info_value import NrfInfoServedUdsfInfoValue  # noqa: E501
from openapi_server.models.nrf_info_served_upf_info_value import NrfInfoServedUpfInfoValue  # noqa: E501
from openapi_server.models.nssaaf_info import NssaafInfo  # noqa: E501
from openapi_server.models.nwdaf_info import NwdafInfo  # noqa: E501
from openapi_server.models.trust_af_info import TrustAfInfo  # noqa: E501
from openapi_server.models.tsctsf_info import TsctsfInfo  # noqa: E501

class NrfInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, served_udr_info=None, served_udr_info_list=None, served_udm_info=None, served_udm_info_list=None, served_ausf_info=None, served_ausf_info_list=None, served_amf_info=None, served_amf_info_list=None, served_smf_info=None, served_smf_info_list=None, served_upf_info=None, served_upf_info_list=None, served_pcf_info=None, served_pcf_info_list=None, served_bsf_info=None, served_bsf_info_list=None, served_chf_info=None, served_chf_info_list=None, served_nef_info=None, served_nwdaf_info=None, served_nwdaf_info_list=None, served_pcscf_info_list=None, served_gmlc_info=None, served_lmf_info=None, served_nf_info=None, served_hss_info_list=None, served_udsf_info=None, served_udsf_info_list=None, served_scp_info_list=None, served_sepp_info_list=None, served_aanf_info_list=None, served5g_ddnmf_info=None, served_mfaf_info_list=None, served_easdf_info_list=None, served_dccf_info_list=None, served_mb_smf_info_list=None, served_tsctsf_info_list=None, served_mb_upf_info_list=None, served_trust_af_info=None, served_nssaaf_info=None):  # noqa: E501
        """NrfInfo - a model defined in OpenAPI

        :param served_udr_info: The served_udr_info of this NrfInfo.  # noqa: E501
        :type served_udr_info: Dict[str, NrfInfoServedUdrInfoValue]
        :param served_udr_info_list: The served_udr_info_list of this NrfInfo.  # noqa: E501
        :type served_udr_info_list: Dict[str, Dict[str, NrfInfoServedUdrInfoValue]]
        :param served_udm_info: The served_udm_info of this NrfInfo.  # noqa: E501
        :type served_udm_info: Dict[str, NrfInfoServedUdmInfoValue]
        :param served_udm_info_list: The served_udm_info_list of this NrfInfo.  # noqa: E501
        :type served_udm_info_list: Dict[str, Dict[str, NrfInfoServedUdmInfoValue]]
        :param served_ausf_info: The served_ausf_info of this NrfInfo.  # noqa: E501
        :type served_ausf_info: Dict[str, NrfInfoServedAusfInfoValue]
        :param served_ausf_info_list: The served_ausf_info_list of this NrfInfo.  # noqa: E501
        :type served_ausf_info_list: Dict[str, Dict[str, NrfInfoServedAusfInfoValue]]
        :param served_amf_info: The served_amf_info of this NrfInfo.  # noqa: E501
        :type served_amf_info: Dict[str, NrfInfoServedAmfInfoValue]
        :param served_amf_info_list: The served_amf_info_list of this NrfInfo.  # noqa: E501
        :type served_amf_info_list: Dict[str, Dict[str, NrfInfoServedAmfInfoValue]]
        :param served_smf_info: The served_smf_info of this NrfInfo.  # noqa: E501
        :type served_smf_info: Dict[str, NrfInfoServedSmfInfoValue]
        :param served_smf_info_list: The served_smf_info_list of this NrfInfo.  # noqa: E501
        :type served_smf_info_list: Dict[str, Dict[str, NrfInfoServedSmfInfoValue]]
        :param served_upf_info: The served_upf_info of this NrfInfo.  # noqa: E501
        :type served_upf_info: Dict[str, NrfInfoServedUpfInfoValue]
        :param served_upf_info_list: The served_upf_info_list of this NrfInfo.  # noqa: E501
        :type served_upf_info_list: Dict[str, Dict[str, NrfInfoServedUpfInfoValue]]
        :param served_pcf_info: The served_pcf_info of this NrfInfo.  # noqa: E501
        :type served_pcf_info: Dict[str, NrfInfoServedPcfInfoValue]
        :param served_pcf_info_list: The served_pcf_info_list of this NrfInfo.  # noqa: E501
        :type served_pcf_info_list: Dict[str, Dict[str, NrfInfoServedPcfInfoValue]]
        :param served_bsf_info: The served_bsf_info of this NrfInfo.  # noqa: E501
        :type served_bsf_info: Dict[str, NrfInfoServedBsfInfoValue]
        :param served_bsf_info_list: The served_bsf_info_list of this NrfInfo.  # noqa: E501
        :type served_bsf_info_list: Dict[str, Dict[str, NrfInfoServedBsfInfoValue]]
        :param served_chf_info: The served_chf_info of this NrfInfo.  # noqa: E501
        :type served_chf_info: Dict[str, NrfInfoServedChfInfoValue]
        :param served_chf_info_list: The served_chf_info_list of this NrfInfo.  # noqa: E501
        :type served_chf_info_list: Dict[str, Dict[str, NrfInfoServedChfInfoValue]]
        :param served_nef_info: The served_nef_info of this NrfInfo.  # noqa: E501
        :type served_nef_info: Dict[str, NrfInfoServedNefInfoValue]
        :param served_nwdaf_info: The served_nwdaf_info of this NrfInfo.  # noqa: E501
        :type served_nwdaf_info: Dict[str, NrfInfoServedNwdafInfoValue]
        :param served_nwdaf_info_list: The served_nwdaf_info_list of this NrfInfo.  # noqa: E501
        :type served_nwdaf_info_list: Dict[str, Dict[str, NwdafInfo]]
        :param served_pcscf_info_list: The served_pcscf_info_list of this NrfInfo.  # noqa: E501
        :type served_pcscf_info_list: Dict[str, Dict[str, NrfInfoServedPcscfInfoListValueValue]]
        :param served_gmlc_info: The served_gmlc_info of this NrfInfo.  # noqa: E501
        :type served_gmlc_info: Dict[str, NrfInfoServedGmlcInfoValue]
        :param served_lmf_info: The served_lmf_info of this NrfInfo.  # noqa: E501
        :type served_lmf_info: Dict[str, NrfInfoServedLmfInfoValue]
        :param served_nf_info: The served_nf_info of this NrfInfo.  # noqa: E501
        :type served_nf_info: Dict[str, NfInfo]
        :param served_hss_info_list: The served_hss_info_list of this NrfInfo.  # noqa: E501
        :type served_hss_info_list: Dict[str, Dict[str, NrfInfoServedHssInfoListValueValue]]
        :param served_udsf_info: The served_udsf_info of this NrfInfo.  # noqa: E501
        :type served_udsf_info: Dict[str, NrfInfoServedUdsfInfoValue]
        :param served_udsf_info_list: The served_udsf_info_list of this NrfInfo.  # noqa: E501
        :type served_udsf_info_list: Dict[str, Dict[str, NrfInfoServedUdsfInfoValue]]
        :param served_scp_info_list: The served_scp_info_list of this NrfInfo.  # noqa: E501
        :type served_scp_info_list: Dict[str, NrfInfoServedScpInfoListValue]
        :param served_sepp_info_list: The served_sepp_info_list of this NrfInfo.  # noqa: E501
        :type served_sepp_info_list: Dict[str, NrfInfoServedSeppInfoListValue]
        :param served_aanf_info_list: The served_aanf_info_list of this NrfInfo.  # noqa: E501
        :type served_aanf_info_list: Dict[str, Dict[str, NrfInfoServedAanfInfoListValueValue]]
        :param served5g_ddnmf_info: The served5g_ddnmf_info of this NrfInfo.  # noqa: E501
        :type served5g_ddnmf_info: Dict[str, Model5GDdnmfInfo]
        :param served_mfaf_info_list: The served_mfaf_info_list of this NrfInfo.  # noqa: E501
        :type served_mfaf_info_list: Dict[str, MfafInfo]
        :param served_easdf_info_list: The served_easdf_info_list of this NrfInfo.  # noqa: E501
        :type served_easdf_info_list: Dict[str, Dict[str, EasdfInfo]]
        :param served_dccf_info_list: The served_dccf_info_list of this NrfInfo.  # noqa: E501
        :type served_dccf_info_list: Dict[str, DccfInfo]
        :param served_mb_smf_info_list: The served_mb_smf_info_list of this NrfInfo.  # noqa: E501
        :type served_mb_smf_info_list: Dict[str, Dict[str, NrfInfoServedMbSmfInfoListValueValue]]
        :param served_tsctsf_info_list: The served_tsctsf_info_list of this NrfInfo.  # noqa: E501
        :type served_tsctsf_info_list: Dict[str, Dict[str, TsctsfInfo]]
        :param served_mb_upf_info_list: The served_mb_upf_info_list of this NrfInfo.  # noqa: E501
        :type served_mb_upf_info_list: Dict[str, Dict[str, MbUpfInfo]]
        :param served_trust_af_info: The served_trust_af_info of this NrfInfo.  # noqa: E501
        :type served_trust_af_info: Dict[str, TrustAfInfo]
        :param served_nssaaf_info: The served_nssaaf_info of this NrfInfo.  # noqa: E501
        :type served_nssaaf_info: Dict[str, NssaafInfo]
        """
        self.openapi_types = {
            'served_udr_info': Dict[str, NrfInfoServedUdrInfoValue],
            'served_udr_info_list': Dict[str, Dict[str, NrfInfoServedUdrInfoValue]],
            'served_udm_info': Dict[str, NrfInfoServedUdmInfoValue],
            'served_udm_info_list': Dict[str, Dict[str, NrfInfoServedUdmInfoValue]],
            'served_ausf_info': Dict[str, NrfInfoServedAusfInfoValue],
            'served_ausf_info_list': Dict[str, Dict[str, NrfInfoServedAusfInfoValue]],
            'served_amf_info': Dict[str, NrfInfoServedAmfInfoValue],
            'served_amf_info_list': Dict[str, Dict[str, NrfInfoServedAmfInfoValue]],
            'served_smf_info': Dict[str, NrfInfoServedSmfInfoValue],
            'served_smf_info_list': Dict[str, Dict[str, NrfInfoServedSmfInfoValue]],
            'served_upf_info': Dict[str, NrfInfoServedUpfInfoValue],
            'served_upf_info_list': Dict[str, Dict[str, NrfInfoServedUpfInfoValue]],
            'served_pcf_info': Dict[str, NrfInfoServedPcfInfoValue],
            'served_pcf_info_list': Dict[str, Dict[str, NrfInfoServedPcfInfoValue]],
            'served_bsf_info': Dict[str, NrfInfoServedBsfInfoValue],
            'served_bsf_info_list': Dict[str, Dict[str, NrfInfoServedBsfInfoValue]],
            'served_chf_info': Dict[str, NrfInfoServedChfInfoValue],
            'served_chf_info_list': Dict[str, Dict[str, NrfInfoServedChfInfoValue]],
            'served_nef_info': Dict[str, NrfInfoServedNefInfoValue],
            'served_nwdaf_info': Dict[str, NrfInfoServedNwdafInfoValue],
            'served_nwdaf_info_list': Dict[str, Dict[str, NwdafInfo]],
            'served_pcscf_info_list': Dict[str, Dict[str, NrfInfoServedPcscfInfoListValueValue]],
            'served_gmlc_info': Dict[str, NrfInfoServedGmlcInfoValue],
            'served_lmf_info': Dict[str, NrfInfoServedLmfInfoValue],
            'served_nf_info': Dict[str, NfInfo],
            'served_hss_info_list': Dict[str, Dict[str, NrfInfoServedHssInfoListValueValue]],
            'served_udsf_info': Dict[str, NrfInfoServedUdsfInfoValue],
            'served_udsf_info_list': Dict[str, Dict[str, NrfInfoServedUdsfInfoValue]],
            'served_scp_info_list': Dict[str, NrfInfoServedScpInfoListValue],
            'served_sepp_info_list': Dict[str, NrfInfoServedSeppInfoListValue],
            'served_aanf_info_list': Dict[str, Dict[str, NrfInfoServedAanfInfoListValueValue]],
            'served5g_ddnmf_info': Dict[str, Model5GDdnmfInfo],
            'served_mfaf_info_list': Dict[str, MfafInfo],
            'served_easdf_info_list': Dict[str, Dict[str, EasdfInfo]],
            'served_dccf_info_list': Dict[str, DccfInfo],
            'served_mb_smf_info_list': Dict[str, Dict[str, NrfInfoServedMbSmfInfoListValueValue]],
            'served_tsctsf_info_list': Dict[str, Dict[str, TsctsfInfo]],
            'served_mb_upf_info_list': Dict[str, Dict[str, MbUpfInfo]],
            'served_trust_af_info': Dict[str, TrustAfInfo],
            'served_nssaaf_info': Dict[str, NssaafInfo]
        }

        self.attribute_map = {
            'served_udr_info': 'servedUdrInfo',
            'served_udr_info_list': 'servedUdrInfoList',
            'served_udm_info': 'servedUdmInfo',
            'served_udm_info_list': 'servedUdmInfoList',
            'served_ausf_info': 'servedAusfInfo',
            'served_ausf_info_list': 'servedAusfInfoList',
            'served_amf_info': 'servedAmfInfo',
            'served_amf_info_list': 'servedAmfInfoList',
            'served_smf_info': 'servedSmfInfo',
            'served_smf_info_list': 'servedSmfInfoList',
            'served_upf_info': 'servedUpfInfo',
            'served_upf_info_list': 'servedUpfInfoList',
            'served_pcf_info': 'servedPcfInfo',
            'served_pcf_info_list': 'servedPcfInfoList',
            'served_bsf_info': 'servedBsfInfo',
            'served_bsf_info_list': 'servedBsfInfoList',
            'served_chf_info': 'servedChfInfo',
            'served_chf_info_list': 'servedChfInfoList',
            'served_nef_info': 'servedNefInfo',
            'served_nwdaf_info': 'servedNwdafInfo',
            'served_nwdaf_info_list': 'servedNwdafInfoList',
            'served_pcscf_info_list': 'servedPcscfInfoList',
            'served_gmlc_info': 'servedGmlcInfo',
            'served_lmf_info': 'servedLmfInfo',
            'served_nf_info': 'servedNfInfo',
            'served_hss_info_list': 'servedHssInfoList',
            'served_udsf_info': 'servedUdsfInfo',
            'served_udsf_info_list': 'servedUdsfInfoList',
            'served_scp_info_list': 'servedScpInfoList',
            'served_sepp_info_list': 'servedSeppInfoList',
            'served_aanf_info_list': 'servedAanfInfoList',
            'served5g_ddnmf_info': 'served5gDdnmfInfo',
            'served_mfaf_info_list': 'servedMfafInfoList',
            'served_easdf_info_list': 'servedEasdfInfoList',
            'served_dccf_info_list': 'servedDccfInfoList',
            'served_mb_smf_info_list': 'servedMbSmfInfoList',
            'served_tsctsf_info_list': 'servedTsctsfInfoList',
            'served_mb_upf_info_list': 'servedMbUpfInfoList',
            'served_trust_af_info': 'servedTrustAfInfo',
            'served_nssaaf_info': 'servedNssaafInfo'
        }

        self._served_udr_info = served_udr_info
        self._served_udr_info_list = served_udr_info_list
        self._served_udm_info = served_udm_info
        self._served_udm_info_list = served_udm_info_list
        self._served_ausf_info = served_ausf_info
        self._served_ausf_info_list = served_ausf_info_list
        self._served_amf_info = served_amf_info
        self._served_amf_info_list = served_amf_info_list
        self._served_smf_info = served_smf_info
        self._served_smf_info_list = served_smf_info_list
        self._served_upf_info = served_upf_info
        self._served_upf_info_list = served_upf_info_list
        self._served_pcf_info = served_pcf_info
        self._served_pcf_info_list = served_pcf_info_list
        self._served_bsf_info = served_bsf_info
        self._served_bsf_info_list = served_bsf_info_list
        self._served_chf_info = served_chf_info
        self._served_chf_info_list = served_chf_info_list
        self._served_nef_info = served_nef_info
        self._served_nwdaf_info = served_nwdaf_info
        self._served_nwdaf_info_list = served_nwdaf_info_list
        self._served_pcscf_info_list = served_pcscf_info_list
        self._served_gmlc_info = served_gmlc_info
        self._served_lmf_info = served_lmf_info
        self._served_nf_info = served_nf_info
        self._served_hss_info_list = served_hss_info_list
        self._served_udsf_info = served_udsf_info
        self._served_udsf_info_list = served_udsf_info_list
        self._served_scp_info_list = served_scp_info_list
        self._served_sepp_info_list = served_sepp_info_list
        self._served_aanf_info_list = served_aanf_info_list
        self._served5g_ddnmf_info = served5g_ddnmf_info
        self._served_mfaf_info_list = served_mfaf_info_list
        self._served_easdf_info_list = served_easdf_info_list
        self._served_dccf_info_list = served_dccf_info_list
        self._served_mb_smf_info_list = served_mb_smf_info_list
        self._served_tsctsf_info_list = served_tsctsf_info_list
        self._served_mb_upf_info_list = served_mb_upf_info_list
        self._served_trust_af_info = served_trust_af_info
        self._served_nssaaf_info = served_nssaaf_info

    @classmethod
    def from_dict(cls, dikt) -> 'NrfInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NrfInfo of this NrfInfo.  # noqa: E501
        :rtype: NrfInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def served_udr_info(self):
        """Gets the served_udr_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_udr_info of this NrfInfo.
        :rtype: Dict[str, NrfInfoServedUdrInfoValue]
        """
        return self._served_udr_info

    @served_udr_info.setter
    def served_udr_info(self, served_udr_info):
        """Sets the served_udr_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_udr_info: The served_udr_info of this NrfInfo.
        :type served_udr_info: Dict[str, NrfInfoServedUdrInfoValue]
        """
        if served_udr_info is not None and len(served_udr_info) < 1:
            raise ValueError("Invalid value for `served_udr_info`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_udr_info = served_udr_info

    @property
    def served_udr_info_list(self):
        """Gets the served_udr_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_udr_info_list of this NrfInfo.
        :rtype: Dict[str, Dict[str, NrfInfoServedUdrInfoValue]]
        """
        return self._served_udr_info_list

    @served_udr_info_list.setter
    def served_udr_info_list(self, served_udr_info_list):
        """Sets the served_udr_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_udr_info_list: The served_udr_info_list of this NrfInfo.
        :type served_udr_info_list: Dict[str, Dict[str, NrfInfoServedUdrInfoValue]]
        """
        if served_udr_info_list is not None and len(served_udr_info_list) < 1:
            raise ValueError("Invalid value for `served_udr_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_udr_info_list = served_udr_info_list

    @property
    def served_udm_info(self):
        """Gets the served_udm_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_udm_info of this NrfInfo.
        :rtype: Dict[str, NrfInfoServedUdmInfoValue]
        """
        return self._served_udm_info

    @served_udm_info.setter
    def served_udm_info(self, served_udm_info):
        """Sets the served_udm_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_udm_info: The served_udm_info of this NrfInfo.
        :type served_udm_info: Dict[str, NrfInfoServedUdmInfoValue]
        """
        if served_udm_info is not None and len(served_udm_info) < 1:
            raise ValueError("Invalid value for `served_udm_info`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_udm_info = served_udm_info

    @property
    def served_udm_info_list(self):
        """Gets the served_udm_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_udm_info_list of this NrfInfo.
        :rtype: Dict[str, Dict[str, NrfInfoServedUdmInfoValue]]
        """
        return self._served_udm_info_list

    @served_udm_info_list.setter
    def served_udm_info_list(self, served_udm_info_list):
        """Sets the served_udm_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_udm_info_list: The served_udm_info_list of this NrfInfo.
        :type served_udm_info_list: Dict[str, Dict[str, NrfInfoServedUdmInfoValue]]
        """
        if served_udm_info_list is not None and len(served_udm_info_list) < 1:
            raise ValueError("Invalid value for `served_udm_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_udm_info_list = served_udm_info_list

    @property
    def served_ausf_info(self):
        """Gets the served_ausf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_ausf_info of this NrfInfo.
        :rtype: Dict[str, NrfInfoServedAusfInfoValue]
        """
        return self._served_ausf_info

    @served_ausf_info.setter
    def served_ausf_info(self, served_ausf_info):
        """Sets the served_ausf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_ausf_info: The served_ausf_info of this NrfInfo.
        :type served_ausf_info: Dict[str, NrfInfoServedAusfInfoValue]
        """
        if served_ausf_info is not None and len(served_ausf_info) < 1:
            raise ValueError("Invalid value for `served_ausf_info`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_ausf_info = served_ausf_info

    @property
    def served_ausf_info_list(self):
        """Gets the served_ausf_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_ausf_info_list of this NrfInfo.
        :rtype: Dict[str, Dict[str, NrfInfoServedAusfInfoValue]]
        """
        return self._served_ausf_info_list

    @served_ausf_info_list.setter
    def served_ausf_info_list(self, served_ausf_info_list):
        """Sets the served_ausf_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_ausf_info_list: The served_ausf_info_list of this NrfInfo.
        :type served_ausf_info_list: Dict[str, Dict[str, NrfInfoServedAusfInfoValue]]
        """
        if served_ausf_info_list is not None and len(served_ausf_info_list) < 1:
            raise ValueError("Invalid value for `served_ausf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_ausf_info_list = served_ausf_info_list

    @property
    def served_amf_info(self):
        """Gets the served_amf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_amf_info of this NrfInfo.
        :rtype: Dict[str, NrfInfoServedAmfInfoValue]
        """
        return self._served_amf_info

    @served_amf_info.setter
    def served_amf_info(self, served_amf_info):
        """Sets the served_amf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_amf_info: The served_amf_info of this NrfInfo.
        :type served_amf_info: Dict[str, NrfInfoServedAmfInfoValue]
        """
        if served_amf_info is not None and len(served_amf_info) < 1:
            raise ValueError("Invalid value for `served_amf_info`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_amf_info = served_amf_info

    @property
    def served_amf_info_list(self):
        """Gets the served_amf_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_amf_info_list of this NrfInfo.
        :rtype: Dict[str, Dict[str, NrfInfoServedAmfInfoValue]]
        """
        return self._served_amf_info_list

    @served_amf_info_list.setter
    def served_amf_info_list(self, served_amf_info_list):
        """Sets the served_amf_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_amf_info_list: The served_amf_info_list of this NrfInfo.
        :type served_amf_info_list: Dict[str, Dict[str, NrfInfoServedAmfInfoValue]]
        """
        if served_amf_info_list is not None and len(served_amf_info_list) < 1:
            raise ValueError("Invalid value for `served_amf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_amf_info_list = served_amf_info_list

    @property
    def served_smf_info(self):
        """Gets the served_smf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_smf_info of this NrfInfo.
        :rtype: Dict[str, NrfInfoServedSmfInfoValue]
        """
        return self._served_smf_info

    @served_smf_info.setter
    def served_smf_info(self, served_smf_info):
        """Sets the served_smf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_smf_info: The served_smf_info of this NrfInfo.
        :type served_smf_info: Dict[str, NrfInfoServedSmfInfoValue]
        """
        if served_smf_info is not None and len(served_smf_info) < 1:
            raise ValueError("Invalid value for `served_smf_info`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_smf_info = served_smf_info

    @property
    def served_smf_info_list(self):
        """Gets the served_smf_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_smf_info_list of this NrfInfo.
        :rtype: Dict[str, Dict[str, NrfInfoServedSmfInfoValue]]
        """
        return self._served_smf_info_list

    @served_smf_info_list.setter
    def served_smf_info_list(self, served_smf_info_list):
        """Sets the served_smf_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_smf_info_list: The served_smf_info_list of this NrfInfo.
        :type served_smf_info_list: Dict[str, Dict[str, NrfInfoServedSmfInfoValue]]
        """
        if served_smf_info_list is not None and len(served_smf_info_list) < 1:
            raise ValueError("Invalid value for `served_smf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_smf_info_list = served_smf_info_list

    @property
    def served_upf_info(self):
        """Gets the served_upf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_upf_info of this NrfInfo.
        :rtype: Dict[str, NrfInfoServedUpfInfoValue]
        """
        return self._served_upf_info

    @served_upf_info.setter
    def served_upf_info(self, served_upf_info):
        """Sets the served_upf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_upf_info: The served_upf_info of this NrfInfo.
        :type served_upf_info: Dict[str, NrfInfoServedUpfInfoValue]
        """
        if served_upf_info is not None and len(served_upf_info) < 1:
            raise ValueError("Invalid value for `served_upf_info`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_upf_info = served_upf_info

    @property
    def served_upf_info_list(self):
        """Gets the served_upf_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_upf_info_list of this NrfInfo.
        :rtype: Dict[str, Dict[str, NrfInfoServedUpfInfoValue]]
        """
        return self._served_upf_info_list

    @served_upf_info_list.setter
    def served_upf_info_list(self, served_upf_info_list):
        """Sets the served_upf_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_upf_info_list: The served_upf_info_list of this NrfInfo.
        :type served_upf_info_list: Dict[str, Dict[str, NrfInfoServedUpfInfoValue]]
        """
        if served_upf_info_list is not None and len(served_upf_info_list) < 1:
            raise ValueError("Invalid value for `served_upf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_upf_info_list = served_upf_info_list

    @property
    def served_pcf_info(self):
        """Gets the served_pcf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_pcf_info of this NrfInfo.
        :rtype: Dict[str, NrfInfoServedPcfInfoValue]
        """
        return self._served_pcf_info

    @served_pcf_info.setter
    def served_pcf_info(self, served_pcf_info):
        """Sets the served_pcf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_pcf_info: The served_pcf_info of this NrfInfo.
        :type served_pcf_info: Dict[str, NrfInfoServedPcfInfoValue]
        """
        if served_pcf_info is not None and len(served_pcf_info) < 1:
            raise ValueError("Invalid value for `served_pcf_info`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_pcf_info = served_pcf_info

    @property
    def served_pcf_info_list(self):
        """Gets the served_pcf_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_pcf_info_list of this NrfInfo.
        :rtype: Dict[str, Dict[str, NrfInfoServedPcfInfoValue]]
        """
        return self._served_pcf_info_list

    @served_pcf_info_list.setter
    def served_pcf_info_list(self, served_pcf_info_list):
        """Sets the served_pcf_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_pcf_info_list: The served_pcf_info_list of this NrfInfo.
        :type served_pcf_info_list: Dict[str, Dict[str, NrfInfoServedPcfInfoValue]]
        """
        if served_pcf_info_list is not None and len(served_pcf_info_list) < 1:
            raise ValueError("Invalid value for `served_pcf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_pcf_info_list = served_pcf_info_list

    @property
    def served_bsf_info(self):
        """Gets the served_bsf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_bsf_info of this NrfInfo.
        :rtype: Dict[str, NrfInfoServedBsfInfoValue]
        """
        return self._served_bsf_info

    @served_bsf_info.setter
    def served_bsf_info(self, served_bsf_info):
        """Sets the served_bsf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_bsf_info: The served_bsf_info of this NrfInfo.
        :type served_bsf_info: Dict[str, NrfInfoServedBsfInfoValue]
        """
        if served_bsf_info is not None and len(served_bsf_info) < 1:
            raise ValueError("Invalid value for `served_bsf_info`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_bsf_info = served_bsf_info

    @property
    def served_bsf_info_list(self):
        """Gets the served_bsf_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_bsf_info_list of this NrfInfo.
        :rtype: Dict[str, Dict[str, NrfInfoServedBsfInfoValue]]
        """
        return self._served_bsf_info_list

    @served_bsf_info_list.setter
    def served_bsf_info_list(self, served_bsf_info_list):
        """Sets the served_bsf_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_bsf_info_list: The served_bsf_info_list of this NrfInfo.
        :type served_bsf_info_list: Dict[str, Dict[str, NrfInfoServedBsfInfoValue]]
        """
        if served_bsf_info_list is not None and len(served_bsf_info_list) < 1:
            raise ValueError("Invalid value for `served_bsf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_bsf_info_list = served_bsf_info_list

    @property
    def served_chf_info(self):
        """Gets the served_chf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_chf_info of this NrfInfo.
        :rtype: Dict[str, NrfInfoServedChfInfoValue]
        """
        return self._served_chf_info

    @served_chf_info.setter
    def served_chf_info(self, served_chf_info):
        """Sets the served_chf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_chf_info: The served_chf_info of this NrfInfo.
        :type served_chf_info: Dict[str, NrfInfoServedChfInfoValue]
        """
        if served_chf_info is not None and len(served_chf_info) < 1:
            raise ValueError("Invalid value for `served_chf_info`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_chf_info = served_chf_info

    @property
    def served_chf_info_list(self):
        """Gets the served_chf_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_chf_info_list of this NrfInfo.
        :rtype: Dict[str, Dict[str, NrfInfoServedChfInfoValue]]
        """
        return self._served_chf_info_list

    @served_chf_info_list.setter
    def served_chf_info_list(self, served_chf_info_list):
        """Sets the served_chf_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_chf_info_list: The served_chf_info_list of this NrfInfo.
        :type served_chf_info_list: Dict[str, Dict[str, NrfInfoServedChfInfoValue]]
        """
        if served_chf_info_list is not None and len(served_chf_info_list) < 1:
            raise ValueError("Invalid value for `served_chf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_chf_info_list = served_chf_info_list

    @property
    def served_nef_info(self):
        """Gets the served_nef_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_nef_info of this NrfInfo.
        :rtype: Dict[str, NrfInfoServedNefInfoValue]
        """
        return self._served_nef_info

    @served_nef_info.setter
    def served_nef_info(self, served_nef_info):
        """Sets the served_nef_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_nef_info: The served_nef_info of this NrfInfo.
        :type served_nef_info: Dict[str, NrfInfoServedNefInfoValue]
        """
        if served_nef_info is not None and len(served_nef_info) < 1:
            raise ValueError("Invalid value for `served_nef_info`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_nef_info = served_nef_info

    @property
    def served_nwdaf_info(self):
        """Gets the served_nwdaf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_nwdaf_info of this NrfInfo.
        :rtype: Dict[str, NrfInfoServedNwdafInfoValue]
        """
        return self._served_nwdaf_info

    @served_nwdaf_info.setter
    def served_nwdaf_info(self, served_nwdaf_info):
        """Sets the served_nwdaf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_nwdaf_info: The served_nwdaf_info of this NrfInfo.
        :type served_nwdaf_info: Dict[str, NrfInfoServedNwdafInfoValue]
        """
        if served_nwdaf_info is not None and len(served_nwdaf_info) < 1:
            raise ValueError("Invalid value for `served_nwdaf_info`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_nwdaf_info = served_nwdaf_info

    @property
    def served_nwdaf_info_list(self):
        """Gets the served_nwdaf_info_list of this NrfInfo.

        A map (list of key-value pairs) where NF Instance Id serves as key  # noqa: E501

        :return: The served_nwdaf_info_list of this NrfInfo.
        :rtype: Dict[str, Dict[str, NwdafInfo]]
        """
        return self._served_nwdaf_info_list

    @served_nwdaf_info_list.setter
    def served_nwdaf_info_list(self, served_nwdaf_info_list):
        """Sets the served_nwdaf_info_list of this NrfInfo.

        A map (list of key-value pairs) where NF Instance Id serves as key  # noqa: E501

        :param served_nwdaf_info_list: The served_nwdaf_info_list of this NrfInfo.
        :type served_nwdaf_info_list: Dict[str, Dict[str, NwdafInfo]]
        """
        if served_nwdaf_info_list is not None and len(served_nwdaf_info_list) < 1:
            raise ValueError("Invalid value for `served_nwdaf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_nwdaf_info_list = served_nwdaf_info_list

    @property
    def served_pcscf_info_list(self):
        """Gets the served_pcscf_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_pcscf_info_list of this NrfInfo.
        :rtype: Dict[str, Dict[str, NrfInfoServedPcscfInfoListValueValue]]
        """
        return self._served_pcscf_info_list

    @served_pcscf_info_list.setter
    def served_pcscf_info_list(self, served_pcscf_info_list):
        """Sets the served_pcscf_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_pcscf_info_list: The served_pcscf_info_list of this NrfInfo.
        :type served_pcscf_info_list: Dict[str, Dict[str, NrfInfoServedPcscfInfoListValueValue]]
        """
        if served_pcscf_info_list is not None and len(served_pcscf_info_list) < 1:
            raise ValueError("Invalid value for `served_pcscf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_pcscf_info_list = served_pcscf_info_list

    @property
    def served_gmlc_info(self):
        """Gets the served_gmlc_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_gmlc_info of this NrfInfo.
        :rtype: Dict[str, NrfInfoServedGmlcInfoValue]
        """
        return self._served_gmlc_info

    @served_gmlc_info.setter
    def served_gmlc_info(self, served_gmlc_info):
        """Sets the served_gmlc_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_gmlc_info: The served_gmlc_info of this NrfInfo.
        :type served_gmlc_info: Dict[str, NrfInfoServedGmlcInfoValue]
        """
        if served_gmlc_info is not None and len(served_gmlc_info) < 1:
            raise ValueError("Invalid value for `served_gmlc_info`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_gmlc_info = served_gmlc_info

    @property
    def served_lmf_info(self):
        """Gets the served_lmf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_lmf_info of this NrfInfo.
        :rtype: Dict[str, NrfInfoServedLmfInfoValue]
        """
        return self._served_lmf_info

    @served_lmf_info.setter
    def served_lmf_info(self, served_lmf_info):
        """Sets the served_lmf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_lmf_info: The served_lmf_info of this NrfInfo.
        :type served_lmf_info: Dict[str, NrfInfoServedLmfInfoValue]
        """
        if served_lmf_info is not None and len(served_lmf_info) < 1:
            raise ValueError("Invalid value for `served_lmf_info`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_lmf_info = served_lmf_info

    @property
    def served_nf_info(self):
        """Gets the served_nf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_nf_info of this NrfInfo.
        :rtype: Dict[str, NfInfo]
        """
        return self._served_nf_info

    @served_nf_info.setter
    def served_nf_info(self, served_nf_info):
        """Sets the served_nf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_nf_info: The served_nf_info of this NrfInfo.
        :type served_nf_info: Dict[str, NfInfo]
        """
        if served_nf_info is not None and len(served_nf_info) < 1:
            raise ValueError("Invalid value for `served_nf_info`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_nf_info = served_nf_info

    @property
    def served_hss_info_list(self):
        """Gets the served_hss_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_hss_info_list of this NrfInfo.
        :rtype: Dict[str, Dict[str, NrfInfoServedHssInfoListValueValue]]
        """
        return self._served_hss_info_list

    @served_hss_info_list.setter
    def served_hss_info_list(self, served_hss_info_list):
        """Sets the served_hss_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_hss_info_list: The served_hss_info_list of this NrfInfo.
        :type served_hss_info_list: Dict[str, Dict[str, NrfInfoServedHssInfoListValueValue]]
        """
        if served_hss_info_list is not None and len(served_hss_info_list) < 1:
            raise ValueError("Invalid value for `served_hss_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_hss_info_list = served_hss_info_list

    @property
    def served_udsf_info(self):
        """Gets the served_udsf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_udsf_info of this NrfInfo.
        :rtype: Dict[str, NrfInfoServedUdsfInfoValue]
        """
        return self._served_udsf_info

    @served_udsf_info.setter
    def served_udsf_info(self, served_udsf_info):
        """Sets the served_udsf_info of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_udsf_info: The served_udsf_info of this NrfInfo.
        :type served_udsf_info: Dict[str, NrfInfoServedUdsfInfoValue]
        """
        if served_udsf_info is not None and len(served_udsf_info) < 1:
            raise ValueError("Invalid value for `served_udsf_info`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_udsf_info = served_udsf_info

    @property
    def served_udsf_info_list(self):
        """Gets the served_udsf_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_udsf_info_list of this NrfInfo.
        :rtype: Dict[str, Dict[str, NrfInfoServedUdsfInfoValue]]
        """
        return self._served_udsf_info_list

    @served_udsf_info_list.setter
    def served_udsf_info_list(self, served_udsf_info_list):
        """Sets the served_udsf_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_udsf_info_list: The served_udsf_info_list of this NrfInfo.
        :type served_udsf_info_list: Dict[str, Dict[str, NrfInfoServedUdsfInfoValue]]
        """
        if served_udsf_info_list is not None and len(served_udsf_info_list) < 1:
            raise ValueError("Invalid value for `served_udsf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_udsf_info_list = served_udsf_info_list

    @property
    def served_scp_info_list(self):
        """Gets the served_scp_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_scp_info_list of this NrfInfo.
        :rtype: Dict[str, NrfInfoServedScpInfoListValue]
        """
        return self._served_scp_info_list

    @served_scp_info_list.setter
    def served_scp_info_list(self, served_scp_info_list):
        """Sets the served_scp_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_scp_info_list: The served_scp_info_list of this NrfInfo.
        :type served_scp_info_list: Dict[str, NrfInfoServedScpInfoListValue]
        """
        if served_scp_info_list is not None and len(served_scp_info_list) < 1:
            raise ValueError("Invalid value for `served_scp_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_scp_info_list = served_scp_info_list

    @property
    def served_sepp_info_list(self):
        """Gets the served_sepp_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_sepp_info_list of this NrfInfo.
        :rtype: Dict[str, NrfInfoServedSeppInfoListValue]
        """
        return self._served_sepp_info_list

    @served_sepp_info_list.setter
    def served_sepp_info_list(self, served_sepp_info_list):
        """Sets the served_sepp_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_sepp_info_list: The served_sepp_info_list of this NrfInfo.
        :type served_sepp_info_list: Dict[str, NrfInfoServedSeppInfoListValue]
        """
        if served_sepp_info_list is not None and len(served_sepp_info_list) < 1:
            raise ValueError("Invalid value for `served_sepp_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_sepp_info_list = served_sepp_info_list

    @property
    def served_aanf_info_list(self):
        """Gets the served_aanf_info_list of this NrfInfo.

        A map (list of key-value pairs) where NF Instance Id serves as key  # noqa: E501

        :return: The served_aanf_info_list of this NrfInfo.
        :rtype: Dict[str, Dict[str, NrfInfoServedAanfInfoListValueValue]]
        """
        return self._served_aanf_info_list

    @served_aanf_info_list.setter
    def served_aanf_info_list(self, served_aanf_info_list):
        """Sets the served_aanf_info_list of this NrfInfo.

        A map (list of key-value pairs) where NF Instance Id serves as key  # noqa: E501

        :param served_aanf_info_list: The served_aanf_info_list of this NrfInfo.
        :type served_aanf_info_list: Dict[str, Dict[str, NrfInfoServedAanfInfoListValueValue]]
        """

        self._served_aanf_info_list = served_aanf_info_list

    @property
    def served5g_ddnmf_info(self):
        """Gets the served5g_ddnmf_info of this NrfInfo.


        :return: The served5g_ddnmf_info of this NrfInfo.
        :rtype: Dict[str, Model5GDdnmfInfo]
        """
        return self._served5g_ddnmf_info

    @served5g_ddnmf_info.setter
    def served5g_ddnmf_info(self, served5g_ddnmf_info):
        """Sets the served5g_ddnmf_info of this NrfInfo.


        :param served5g_ddnmf_info: The served5g_ddnmf_info of this NrfInfo.
        :type served5g_ddnmf_info: Dict[str, Model5GDdnmfInfo]
        """
        if served5g_ddnmf_info is not None and len(served5g_ddnmf_info) < 1:
            raise ValueError("Invalid value for `served5g_ddnmf_info`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served5g_ddnmf_info = served5g_ddnmf_info

    @property
    def served_mfaf_info_list(self):
        """Gets the served_mfaf_info_list of this NrfInfo.

        A map (list of key-value pairs) where NF Instance Id serves as key  # noqa: E501

        :return: The served_mfaf_info_list of this NrfInfo.
        :rtype: Dict[str, MfafInfo]
        """
        return self._served_mfaf_info_list

    @served_mfaf_info_list.setter
    def served_mfaf_info_list(self, served_mfaf_info_list):
        """Sets the served_mfaf_info_list of this NrfInfo.

        A map (list of key-value pairs) where NF Instance Id serves as key  # noqa: E501

        :param served_mfaf_info_list: The served_mfaf_info_list of this NrfInfo.
        :type served_mfaf_info_list: Dict[str, MfafInfo]
        """
        if served_mfaf_info_list is not None and len(served_mfaf_info_list) < 1:
            raise ValueError("Invalid value for `served_mfaf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_mfaf_info_list = served_mfaf_info_list

    @property
    def served_easdf_info_list(self):
        """Gets the served_easdf_info_list of this NrfInfo.

        A map (list of key-value pairs) where NF Instance Id serves as key  # noqa: E501

        :return: The served_easdf_info_list of this NrfInfo.
        :rtype: Dict[str, Dict[str, EasdfInfo]]
        """
        return self._served_easdf_info_list

    @served_easdf_info_list.setter
    def served_easdf_info_list(self, served_easdf_info_list):
        """Sets the served_easdf_info_list of this NrfInfo.

        A map (list of key-value pairs) where NF Instance Id serves as key  # noqa: E501

        :param served_easdf_info_list: The served_easdf_info_list of this NrfInfo.
        :type served_easdf_info_list: Dict[str, Dict[str, EasdfInfo]]
        """

        self._served_easdf_info_list = served_easdf_info_list

    @property
    def served_dccf_info_list(self):
        """Gets the served_dccf_info_list of this NrfInfo.

        A map (list of key-value pairs) where NF Instance Id serves as key  # noqa: E501

        :return: The served_dccf_info_list of this NrfInfo.
        :rtype: Dict[str, DccfInfo]
        """
        return self._served_dccf_info_list

    @served_dccf_info_list.setter
    def served_dccf_info_list(self, served_dccf_info_list):
        """Sets the served_dccf_info_list of this NrfInfo.

        A map (list of key-value pairs) where NF Instance Id serves as key  # noqa: E501

        :param served_dccf_info_list: The served_dccf_info_list of this NrfInfo.
        :type served_dccf_info_list: Dict[str, DccfInfo]
        """
        if served_dccf_info_list is not None and len(served_dccf_info_list) < 1:
            raise ValueError("Invalid value for `served_dccf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_dccf_info_list = served_dccf_info_list

    @property
    def served_mb_smf_info_list(self):
        """Gets the served_mb_smf_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :return: The served_mb_smf_info_list of this NrfInfo.
        :rtype: Dict[str, Dict[str, NrfInfoServedMbSmfInfoListValueValue]]
        """
        return self._served_mb_smf_info_list

    @served_mb_smf_info_list.setter
    def served_mb_smf_info_list(self, served_mb_smf_info_list):
        """Sets the served_mb_smf_info_list of this NrfInfo.

        A map (list of key-value pairs) where nfInstanceId serves as key  # noqa: E501

        :param served_mb_smf_info_list: The served_mb_smf_info_list of this NrfInfo.
        :type served_mb_smf_info_list: Dict[str, Dict[str, NrfInfoServedMbSmfInfoListValueValue]]
        """
        if served_mb_smf_info_list is not None and len(served_mb_smf_info_list) < 1:
            raise ValueError("Invalid value for `served_mb_smf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_mb_smf_info_list = served_mb_smf_info_list

    @property
    def served_tsctsf_info_list(self):
        """Gets the served_tsctsf_info_list of this NrfInfo.

        A map (list of key-value pairs) where NF Instance Id serves as key  # noqa: E501

        :return: The served_tsctsf_info_list of this NrfInfo.
        :rtype: Dict[str, Dict[str, TsctsfInfo]]
        """
        return self._served_tsctsf_info_list

    @served_tsctsf_info_list.setter
    def served_tsctsf_info_list(self, served_tsctsf_info_list):
        """Sets the served_tsctsf_info_list of this NrfInfo.

        A map (list of key-value pairs) where NF Instance Id serves as key  # noqa: E501

        :param served_tsctsf_info_list: The served_tsctsf_info_list of this NrfInfo.
        :type served_tsctsf_info_list: Dict[str, Dict[str, TsctsfInfo]]
        """
        if served_tsctsf_info_list is not None and len(served_tsctsf_info_list) < 1:
            raise ValueError("Invalid value for `served_tsctsf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_tsctsf_info_list = served_tsctsf_info_list

    @property
    def served_mb_upf_info_list(self):
        """Gets the served_mb_upf_info_list of this NrfInfo.

        A map (list of key-value pairs) where NF Instance Id serves as key  # noqa: E501

        :return: The served_mb_upf_info_list of this NrfInfo.
        :rtype: Dict[str, Dict[str, MbUpfInfo]]
        """
        return self._served_mb_upf_info_list

    @served_mb_upf_info_list.setter
    def served_mb_upf_info_list(self, served_mb_upf_info_list):
        """Sets the served_mb_upf_info_list of this NrfInfo.

        A map (list of key-value pairs) where NF Instance Id serves as key  # noqa: E501

        :param served_mb_upf_info_list: The served_mb_upf_info_list of this NrfInfo.
        :type served_mb_upf_info_list: Dict[str, Dict[str, MbUpfInfo]]
        """
        if served_mb_upf_info_list is not None and len(served_mb_upf_info_list) < 1:
            raise ValueError("Invalid value for `served_mb_upf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_mb_upf_info_list = served_mb_upf_info_list

    @property
    def served_trust_af_info(self):
        """Gets the served_trust_af_info of this NrfInfo.

        A map (list of key-value pairs) where NF Instance Id serves as key  # noqa: E501

        :return: The served_trust_af_info of this NrfInfo.
        :rtype: Dict[str, TrustAfInfo]
        """
        return self._served_trust_af_info

    @served_trust_af_info.setter
    def served_trust_af_info(self, served_trust_af_info):
        """Sets the served_trust_af_info of this NrfInfo.

        A map (list of key-value pairs) where NF Instance Id serves as key  # noqa: E501

        :param served_trust_af_info: The served_trust_af_info of this NrfInfo.
        :type served_trust_af_info: Dict[str, TrustAfInfo]
        """
        if served_trust_af_info is not None and len(served_trust_af_info) < 1:
            raise ValueError("Invalid value for `served_trust_af_info`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_trust_af_info = served_trust_af_info

    @property
    def served_nssaaf_info(self):
        """Gets the served_nssaaf_info of this NrfInfo.

        A map (list of key-value pairs) where NF Instance Id serves as key  # noqa: E501

        :return: The served_nssaaf_info of this NrfInfo.
        :rtype: Dict[str, NssaafInfo]
        """
        return self._served_nssaaf_info

    @served_nssaaf_info.setter
    def served_nssaaf_info(self, served_nssaaf_info):
        """Sets the served_nssaaf_info of this NrfInfo.

        A map (list of key-value pairs) where NF Instance Id serves as key  # noqa: E501

        :param served_nssaaf_info: The served_nssaaf_info of this NrfInfo.
        :type served_nssaaf_info: Dict[str, NssaafInfo]
        """
        if served_nssaaf_info is not None and len(served_nssaaf_info) < 1:
            raise ValueError("Invalid value for `served_nssaaf_info`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._served_nssaaf_info = served_nssaaf_info

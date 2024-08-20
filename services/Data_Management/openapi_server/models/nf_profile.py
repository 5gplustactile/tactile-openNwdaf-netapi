# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.aanf_info import AanfInfo
from openapi_server.models.amf_info import AmfInfo
from openapi_server.models.ausf_info import AusfInfo
from openapi_server.models.bsf_info import BsfInfo
from openapi_server.models.chf_info import ChfInfo
from openapi_server.models.collocated_nf_instance import CollocatedNfInstance
from openapi_server.models.dccf_info import DccfInfo
from openapi_server.models.default_notification_subscription import DefaultNotificationSubscription
from openapi_server.models.easdf_info import EasdfInfo
from openapi_server.models.ext_snssai import ExtSnssai
from openapi_server.models.gmlc_info import GmlcInfo
from openapi_server.models.hss_info import HssInfo
from openapi_server.models.ipv6_addr import Ipv6Addr
from openapi_server.models.iwmsc_info import IwmscInfo
from openapi_server.models.lmf_info import LmfInfo
from openapi_server.models.mb_smf_info import MbSmfInfo
from openapi_server.models.mb_upf_info import MbUpfInfo
from openapi_server.models.mfaf_info import MfafInfo
from openapi_server.models.mnpf_info import MnpfInfo
from openapi_server.models.model5_g_ddnmf_info import Model5GDdnmfInfo
from openapi_server.models.nf_service import NFService
from openapi_server.models.nf_type import NFType
from openapi_server.models.nef_info import NefInfo
from openapi_server.models.nf_status import NfStatus
from openapi_server.models.nrf_info import NrfInfo
from openapi_server.models.nsacf_info import NsacfInfo
from openapi_server.models.nssaaf_info import NssaafInfo
from openapi_server.models.nwdaf_info import NwdafInfo
from openapi_server.models.pcf_info import PcfInfo
from openapi_server.models.pcscf_info import PcscfInfo
from openapi_server.models.plmn_id import PlmnId
from openapi_server.models.plmn_id_nid import PlmnIdNid
from openapi_server.models.plmn_snssai import PlmnSnssai
from openapi_server.models.scp_info import ScpInfo
from openapi_server.models.sepp_info import SeppInfo
from openapi_server.models.smf_info import SmfInfo
from openapi_server.models.smsf_info import SmsfInfo
from openapi_server.models.trust_af_info import TrustAfInfo
from openapi_server.models.tsctsf_info import TsctsfInfo
from openapi_server.models.udm_info import UdmInfo
from openapi_server.models.udr_info import UdrInfo
from openapi_server.models.udsf_info import UdsfInfo
from openapi_server.models.upf_info import UpfInfo
from openapi_server.models.vendor_specific_feature import VendorSpecificFeature
import re
from openapi_server import util

from openapi_server.models.aanf_info import AanfInfo  # noqa: E501
from openapi_server.models.amf_info import AmfInfo  # noqa: E501
from openapi_server.models.ausf_info import AusfInfo  # noqa: E501
from openapi_server.models.bsf_info import BsfInfo  # noqa: E501
from openapi_server.models.chf_info import ChfInfo  # noqa: E501
from openapi_server.models.collocated_nf_instance import CollocatedNfInstance  # noqa: E501
from openapi_server.models.dccf_info import DccfInfo  # noqa: E501
from openapi_server.models.default_notification_subscription import DefaultNotificationSubscription  # noqa: E501
from openapi_server.models.easdf_info import EasdfInfo  # noqa: E501
from openapi_server.models.ext_snssai import ExtSnssai  # noqa: E501
from openapi_server.models.gmlc_info import GmlcInfo  # noqa: E501
from openapi_server.models.hss_info import HssInfo  # noqa: E501
from openapi_server.models.ipv6_addr import Ipv6Addr  # noqa: E501
from openapi_server.models.iwmsc_info import IwmscInfo  # noqa: E501
from openapi_server.models.lmf_info import LmfInfo  # noqa: E501
from openapi_server.models.mb_smf_info import MbSmfInfo  # noqa: E501
from openapi_server.models.mb_upf_info import MbUpfInfo  # noqa: E501
from openapi_server.models.mfaf_info import MfafInfo  # noqa: E501
from openapi_server.models.mnpf_info import MnpfInfo  # noqa: E501
from openapi_server.models.model5_g_ddnmf_info import Model5GDdnmfInfo  # noqa: E501
from openapi_server.models.nef_info import NefInfo  # noqa: E501
from openapi_server.models.nf_service import NFService  # noqa: E501
from openapi_server.models.nf_status import NfStatus  # noqa: E501
from openapi_server.models.nf_type import NFType  # noqa: E501
from openapi_server.models.nrf_info import NrfInfo  # noqa: E501
from openapi_server.models.nsacf_info import NsacfInfo  # noqa: E501
from openapi_server.models.nssaaf_info import NssaafInfo  # noqa: E501
from openapi_server.models.nwdaf_info import NwdafInfo  # noqa: E501
from openapi_server.models.pcf_info import PcfInfo  # noqa: E501
from openapi_server.models.pcscf_info import PcscfInfo  # noqa: E501
from openapi_server.models.plmn_id import PlmnId  # noqa: E501
from openapi_server.models.plmn_id_nid import PlmnIdNid  # noqa: E501
from openapi_server.models.plmn_snssai import PlmnSnssai  # noqa: E501
from openapi_server.models.scp_info import ScpInfo  # noqa: E501
from openapi_server.models.sepp_info import SeppInfo  # noqa: E501
from openapi_server.models.smf_info import SmfInfo  # noqa: E501
from openapi_server.models.smsf_info import SmsfInfo  # noqa: E501
from openapi_server.models.trust_af_info import TrustAfInfo  # noqa: E501
from openapi_server.models.tsctsf_info import TsctsfInfo  # noqa: E501
from openapi_server.models.udm_info import UdmInfo  # noqa: E501
from openapi_server.models.udr_info import UdrInfo  # noqa: E501
from openapi_server.models.udsf_info import UdsfInfo  # noqa: E501
from openapi_server.models.upf_info import UpfInfo  # noqa: E501
from openapi_server.models.vendor_specific_feature import VendorSpecificFeature  # noqa: E501
import re  # noqa: E501

class NFProfile(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, nf_instance_id=None, nf_instance_name=None, nf_type=None, nf_status=None, collocated_nf_instances=None, heart_beat_timer=None, plmn_list=None, snpn_list=None, s_nssais=None, per_plmn_snssai_list=None, nsi_list=None, fqdn=None, inter_plmn_fqdn=None, ipv4_addresses=None, ipv6_addresses=None, allowed_plmns=None, allowed_snpns=None, allowed_nf_types=None, allowed_nf_domains=None, allowed_nssais=None, priority=None, capacity=None, load=None, load_time_stamp=None, locality=None, ext_locality=None, udr_info=None, udr_info_list=None, udm_info=None, udm_info_list=None, ausf_info=None, ausf_info_list=None, amf_info=None, amf_info_list=None, smf_info=None, smf_info_list=None, upf_info=None, upf_info_list=None, pcf_info=None, pcf_info_list=None, bsf_info=None, bsf_info_list=None, chf_info=None, chf_info_list=None, nef_info=None, nrf_info=None, udsf_info=None, udsf_info_list=None, nwdaf_info=None, nwdaf_info_list=None, pcscf_info_list=None, hss_info_list=None, custom_info=None, recovery_time=None, nf_service_persistence=False, nf_services=None, nf_service_list=None, nf_profile_changes_support_ind=False, nf_profile_changes_ind=False, default_notification_subscriptions=None, lmf_info=None, gmlc_info=None, nf_set_id_list=None, serving_scope=None, lc_h_support_ind=False, olc_h_support_ind=False, nf_set_recovery_time_list=None, service_set_recovery_time_list=None, scp_domains=None, scp_info=None, sepp_info=None, vendor_id=None, supported_vendor_specific_features=None, aanf_info_list=None, _5g_ddnmf_info=None, mfaf_info=None, easdf_info_list=None, dccf_info=None, nsacf_info_list=None, mb_smf_info_list=None, tsctsf_info_list=None, mb_upf_info_list=None, trust_af_info=None, nssaaf_info=None, hni_list=None, iwmsc_info=None, mnpf_info=None, smsf_info=None):  # noqa: E501
        """NFProfile - a model defined in OpenAPI

        :param nf_instance_id: The nf_instance_id of this NFProfile.  # noqa: E501
        :type nf_instance_id: str
        :param nf_instance_name: The nf_instance_name of this NFProfile.  # noqa: E501
        :type nf_instance_name: str
        :param nf_type: The nf_type of this NFProfile.  # noqa: E501
        :type nf_type: NFType
        :param nf_status: The nf_status of this NFProfile.  # noqa: E501
        :type nf_status: NfStatus
        :param collocated_nf_instances: The collocated_nf_instances of this NFProfile.  # noqa: E501
        :type collocated_nf_instances: List[CollocatedNfInstance]
        :param heart_beat_timer: The heart_beat_timer of this NFProfile.  # noqa: E501
        :type heart_beat_timer: int
        :param plmn_list: The plmn_list of this NFProfile.  # noqa: E501
        :type plmn_list: List[PlmnId]
        :param snpn_list: The snpn_list of this NFProfile.  # noqa: E501
        :type snpn_list: List[PlmnIdNid]
        :param s_nssais: The s_nssais of this NFProfile.  # noqa: E501
        :type s_nssais: List[ExtSnssai]
        :param per_plmn_snssai_list: The per_plmn_snssai_list of this NFProfile.  # noqa: E501
        :type per_plmn_snssai_list: List[PlmnSnssai]
        :param nsi_list: The nsi_list of this NFProfile.  # noqa: E501
        :type nsi_list: List[str]
        :param fqdn: The fqdn of this NFProfile.  # noqa: E501
        :type fqdn: str
        :param inter_plmn_fqdn: The inter_plmn_fqdn of this NFProfile.  # noqa: E501
        :type inter_plmn_fqdn: str
        :param ipv4_addresses: The ipv4_addresses of this NFProfile.  # noqa: E501
        :type ipv4_addresses: List[str]
        :param ipv6_addresses: The ipv6_addresses of this NFProfile.  # noqa: E501
        :type ipv6_addresses: List[Ipv6Addr]
        :param allowed_plmns: The allowed_plmns of this NFProfile.  # noqa: E501
        :type allowed_plmns: List[PlmnId]
        :param allowed_snpns: The allowed_snpns of this NFProfile.  # noqa: E501
        :type allowed_snpns: List[PlmnIdNid]
        :param allowed_nf_types: The allowed_nf_types of this NFProfile.  # noqa: E501
        :type allowed_nf_types: List[NFType]
        :param allowed_nf_domains: The allowed_nf_domains of this NFProfile.  # noqa: E501
        :type allowed_nf_domains: List[str]
        :param allowed_nssais: The allowed_nssais of this NFProfile.  # noqa: E501
        :type allowed_nssais: List[ExtSnssai]
        :param priority: The priority of this NFProfile.  # noqa: E501
        :type priority: int
        :param capacity: The capacity of this NFProfile.  # noqa: E501
        :type capacity: int
        :param load: The load of this NFProfile.  # noqa: E501
        :type load: int
        :param load_time_stamp: The load_time_stamp of this NFProfile.  # noqa: E501
        :type load_time_stamp: datetime
        :param locality: The locality of this NFProfile.  # noqa: E501
        :type locality: str
        :param ext_locality: The ext_locality of this NFProfile.  # noqa: E501
        :type ext_locality: Dict[str, str]
        :param udr_info: The udr_info of this NFProfile.  # noqa: E501
        :type udr_info: UdrInfo
        :param udr_info_list: The udr_info_list of this NFProfile.  # noqa: E501
        :type udr_info_list: Dict[str, UdrInfo]
        :param udm_info: The udm_info of this NFProfile.  # noqa: E501
        :type udm_info: UdmInfo
        :param udm_info_list: The udm_info_list of this NFProfile.  # noqa: E501
        :type udm_info_list: Dict[str, UdmInfo]
        :param ausf_info: The ausf_info of this NFProfile.  # noqa: E501
        :type ausf_info: AusfInfo
        :param ausf_info_list: The ausf_info_list of this NFProfile.  # noqa: E501
        :type ausf_info_list: Dict[str, AusfInfo]
        :param amf_info: The amf_info of this NFProfile.  # noqa: E501
        :type amf_info: AmfInfo
        :param amf_info_list: The amf_info_list of this NFProfile.  # noqa: E501
        :type amf_info_list: Dict[str, AmfInfo]
        :param smf_info: The smf_info of this NFProfile.  # noqa: E501
        :type smf_info: SmfInfo
        :param smf_info_list: The smf_info_list of this NFProfile.  # noqa: E501
        :type smf_info_list: Dict[str, SmfInfo]
        :param upf_info: The upf_info of this NFProfile.  # noqa: E501
        :type upf_info: UpfInfo
        :param upf_info_list: The upf_info_list of this NFProfile.  # noqa: E501
        :type upf_info_list: Dict[str, UpfInfo]
        :param pcf_info: The pcf_info of this NFProfile.  # noqa: E501
        :type pcf_info: PcfInfo
        :param pcf_info_list: The pcf_info_list of this NFProfile.  # noqa: E501
        :type pcf_info_list: Dict[str, PcfInfo]
        :param bsf_info: The bsf_info of this NFProfile.  # noqa: E501
        :type bsf_info: BsfInfo
        :param bsf_info_list: The bsf_info_list of this NFProfile.  # noqa: E501
        :type bsf_info_list: Dict[str, BsfInfo]
        :param chf_info: The chf_info of this NFProfile.  # noqa: E501
        :type chf_info: ChfInfo
        :param chf_info_list: The chf_info_list of this NFProfile.  # noqa: E501
        :type chf_info_list: Dict[str, ChfInfo]
        :param nef_info: The nef_info of this NFProfile.  # noqa: E501
        :type nef_info: NefInfo
        :param nrf_info: The nrf_info of this NFProfile.  # noqa: E501
        :type nrf_info: NrfInfo
        :param udsf_info: The udsf_info of this NFProfile.  # noqa: E501
        :type udsf_info: UdsfInfo
        :param udsf_info_list: The udsf_info_list of this NFProfile.  # noqa: E501
        :type udsf_info_list: Dict[str, UdsfInfo]
        :param nwdaf_info: The nwdaf_info of this NFProfile.  # noqa: E501
        :type nwdaf_info: NwdafInfo
        :param nwdaf_info_list: The nwdaf_info_list of this NFProfile.  # noqa: E501
        :type nwdaf_info_list: Dict[str, NwdafInfo]
        :param pcscf_info_list: The pcscf_info_list of this NFProfile.  # noqa: E501
        :type pcscf_info_list: Dict[str, PcscfInfo]
        :param hss_info_list: The hss_info_list of this NFProfile.  # noqa: E501
        :type hss_info_list: Dict[str, HssInfo]
        :param custom_info: The custom_info of this NFProfile.  # noqa: E501
        :type custom_info: object
        :param recovery_time: The recovery_time of this NFProfile.  # noqa: E501
        :type recovery_time: datetime
        :param nf_service_persistence: The nf_service_persistence of this NFProfile.  # noqa: E501
        :type nf_service_persistence: bool
        :param nf_services: The nf_services of this NFProfile.  # noqa: E501
        :type nf_services: List[NFService]
        :param nf_service_list: The nf_service_list of this NFProfile.  # noqa: E501
        :type nf_service_list: Dict[str, NFService]
        :param nf_profile_changes_support_ind: The nf_profile_changes_support_ind of this NFProfile.  # noqa: E501
        :type nf_profile_changes_support_ind: bool
        :param nf_profile_changes_ind: The nf_profile_changes_ind of this NFProfile.  # noqa: E501
        :type nf_profile_changes_ind: bool
        :param default_notification_subscriptions: The default_notification_subscriptions of this NFProfile.  # noqa: E501
        :type default_notification_subscriptions: List[DefaultNotificationSubscription]
        :param lmf_info: The lmf_info of this NFProfile.  # noqa: E501
        :type lmf_info: LmfInfo
        :param gmlc_info: The gmlc_info of this NFProfile.  # noqa: E501
        :type gmlc_info: GmlcInfo
        :param nf_set_id_list: The nf_set_id_list of this NFProfile.  # noqa: E501
        :type nf_set_id_list: List[str]
        :param serving_scope: The serving_scope of this NFProfile.  # noqa: E501
        :type serving_scope: List[str]
        :param lc_h_support_ind: The lc_h_support_ind of this NFProfile.  # noqa: E501
        :type lc_h_support_ind: bool
        :param olc_h_support_ind: The olc_h_support_ind of this NFProfile.  # noqa: E501
        :type olc_h_support_ind: bool
        :param nf_set_recovery_time_list: The nf_set_recovery_time_list of this NFProfile.  # noqa: E501
        :type nf_set_recovery_time_list: Dict[str, datetime]
        :param service_set_recovery_time_list: The service_set_recovery_time_list of this NFProfile.  # noqa: E501
        :type service_set_recovery_time_list: Dict[str, datetime]
        :param scp_domains: The scp_domains of this NFProfile.  # noqa: E501
        :type scp_domains: List[str]
        :param scp_info: The scp_info of this NFProfile.  # noqa: E501
        :type scp_info: ScpInfo
        :param sepp_info: The sepp_info of this NFProfile.  # noqa: E501
        :type sepp_info: SeppInfo
        :param vendor_id: The vendor_id of this NFProfile.  # noqa: E501
        :type vendor_id: str
        :param supported_vendor_specific_features: The supported_vendor_specific_features of this NFProfile.  # noqa: E501
        :type supported_vendor_specific_features: Dict[str, List[VendorSpecificFeature]]
        :param aanf_info_list: The aanf_info_list of this NFProfile.  # noqa: E501
        :type aanf_info_list: Dict[str, AanfInfo]
        :param _5g_ddnmf_info: The _5g_ddnmf_info of this NFProfile.  # noqa: E501
        :type _5g_ddnmf_info: Model5GDdnmfInfo
        :param mfaf_info: The mfaf_info of this NFProfile.  # noqa: E501
        :type mfaf_info: MfafInfo
        :param easdf_info_list: The easdf_info_list of this NFProfile.  # noqa: E501
        :type easdf_info_list: Dict[str, EasdfInfo]
        :param dccf_info: The dccf_info of this NFProfile.  # noqa: E501
        :type dccf_info: DccfInfo
        :param nsacf_info_list: The nsacf_info_list of this NFProfile.  # noqa: E501
        :type nsacf_info_list: Dict[str, NsacfInfo]
        :param mb_smf_info_list: The mb_smf_info_list of this NFProfile.  # noqa: E501
        :type mb_smf_info_list: Dict[str, MbSmfInfo]
        :param tsctsf_info_list: The tsctsf_info_list of this NFProfile.  # noqa: E501
        :type tsctsf_info_list: Dict[str, TsctsfInfo]
        :param mb_upf_info_list: The mb_upf_info_list of this NFProfile.  # noqa: E501
        :type mb_upf_info_list: Dict[str, MbUpfInfo]
        :param trust_af_info: The trust_af_info of this NFProfile.  # noqa: E501
        :type trust_af_info: TrustAfInfo
        :param nssaaf_info: The nssaaf_info of this NFProfile.  # noqa: E501
        :type nssaaf_info: NssaafInfo
        :param hni_list: The hni_list of this NFProfile.  # noqa: E501
        :type hni_list: List[str]
        :param iwmsc_info: The iwmsc_info of this NFProfile.  # noqa: E501
        :type iwmsc_info: IwmscInfo
        :param mnpf_info: The mnpf_info of this NFProfile.  # noqa: E501
        :type mnpf_info: MnpfInfo
        :param smsf_info: The smsf_info of this NFProfile.  # noqa: E501
        :type smsf_info: SmsfInfo
        """
        self.openapi_types = {
            'nf_instance_id': str,
            'nf_instance_name': str,
            'nf_type': NFType,
            'nf_status': NfStatus,
            'collocated_nf_instances': List[CollocatedNfInstance],
            'heart_beat_timer': int,
            'plmn_list': List[PlmnId],
            'snpn_list': List[PlmnIdNid],
            's_nssais': List[ExtSnssai],
            'per_plmn_snssai_list': List[PlmnSnssai],
            'nsi_list': List[str],
            'fqdn': str,
            'inter_plmn_fqdn': str,
            'ipv4_addresses': List[str],
            'ipv6_addresses': List[Ipv6Addr],
            'allowed_plmns': List[PlmnId],
            'allowed_snpns': List[PlmnIdNid],
            'allowed_nf_types': List[NFType],
            'allowed_nf_domains': List[str],
            'allowed_nssais': List[ExtSnssai],
            'priority': int,
            'capacity': int,
            'load': int,
            'load_time_stamp': datetime,
            'locality': str,
            'ext_locality': Dict[str, str],
            'udr_info': UdrInfo,
            'udr_info_list': Dict[str, UdrInfo],
            'udm_info': UdmInfo,
            'udm_info_list': Dict[str, UdmInfo],
            'ausf_info': AusfInfo,
            'ausf_info_list': Dict[str, AusfInfo],
            'amf_info': AmfInfo,
            'amf_info_list': Dict[str, AmfInfo],
            'smf_info': SmfInfo,
            'smf_info_list': Dict[str, SmfInfo],
            'upf_info': UpfInfo,
            'upf_info_list': Dict[str, UpfInfo],
            'pcf_info': PcfInfo,
            'pcf_info_list': Dict[str, PcfInfo],
            'bsf_info': BsfInfo,
            'bsf_info_list': Dict[str, BsfInfo],
            'chf_info': ChfInfo,
            'chf_info_list': Dict[str, ChfInfo],
            'nef_info': NefInfo,
            'nrf_info': NrfInfo,
            'udsf_info': UdsfInfo,
            'udsf_info_list': Dict[str, UdsfInfo],
            'nwdaf_info': NwdafInfo,
            'nwdaf_info_list': Dict[str, NwdafInfo],
            'pcscf_info_list': Dict[str, PcscfInfo],
            'hss_info_list': Dict[str, HssInfo],
            'custom_info': object,
            'recovery_time': datetime,
            'nf_service_persistence': bool,
            'nf_services': List[NFService],
            'nf_service_list': Dict[str, NFService],
            'nf_profile_changes_support_ind': bool,
            'nf_profile_changes_ind': bool,
            'default_notification_subscriptions': List[DefaultNotificationSubscription],
            'lmf_info': LmfInfo,
            'gmlc_info': GmlcInfo,
            'nf_set_id_list': List[str],
            'serving_scope': List[str],
            'lc_h_support_ind': bool,
            'olc_h_support_ind': bool,
            'nf_set_recovery_time_list': Dict[str, datetime],
            'service_set_recovery_time_list': Dict[str, datetime],
            'scp_domains': List[str],
            'scp_info': ScpInfo,
            'sepp_info': SeppInfo,
            'vendor_id': str,
            'supported_vendor_specific_features': Dict[str, List[VendorSpecificFeature]],
            'aanf_info_list': Dict[str, AanfInfo],
            '_5g_ddnmf_info': Model5GDdnmfInfo,
            'mfaf_info': MfafInfo,
            'easdf_info_list': Dict[str, EasdfInfo],
            'dccf_info': DccfInfo,
            'nsacf_info_list': Dict[str, NsacfInfo],
            'mb_smf_info_list': Dict[str, MbSmfInfo],
            'tsctsf_info_list': Dict[str, TsctsfInfo],
            'mb_upf_info_list': Dict[str, MbUpfInfo],
            'trust_af_info': TrustAfInfo,
            'nssaaf_info': NssaafInfo,
            'hni_list': List[str],
            'iwmsc_info': IwmscInfo,
            'mnpf_info': MnpfInfo,
            'smsf_info': SmsfInfo
        }

        self.attribute_map = {
            'nf_instance_id': 'nfInstanceId',
            'nf_instance_name': 'nfInstanceName',
            'nf_type': 'nfType',
            'nf_status': 'nfStatus',
            'collocated_nf_instances': 'collocatedNfInstances',
            'heart_beat_timer': 'heartBeatTimer',
            'plmn_list': 'plmnList',
            'snpn_list': 'snpnList',
            's_nssais': 'sNssais',
            'per_plmn_snssai_list': 'perPlmnSnssaiList',
            'nsi_list': 'nsiList',
            'fqdn': 'fqdn',
            'inter_plmn_fqdn': 'interPlmnFqdn',
            'ipv4_addresses': 'ipv4Addresses',
            'ipv6_addresses': 'ipv6Addresses',
            'allowed_plmns': 'allowedPlmns',
            'allowed_snpns': 'allowedSnpns',
            'allowed_nf_types': 'allowedNfTypes',
            'allowed_nf_domains': 'allowedNfDomains',
            'allowed_nssais': 'allowedNssais',
            'priority': 'priority',
            'capacity': 'capacity',
            'load': 'load',
            'load_time_stamp': 'loadTimeStamp',
            'locality': 'locality',
            'ext_locality': 'extLocality',
            'udr_info': 'udrInfo',
            'udr_info_list': 'udrInfoList',
            'udm_info': 'udmInfo',
            'udm_info_list': 'udmInfoList',
            'ausf_info': 'ausfInfo',
            'ausf_info_list': 'ausfInfoList',
            'amf_info': 'amfInfo',
            'amf_info_list': 'amfInfoList',
            'smf_info': 'smfInfo',
            'smf_info_list': 'smfInfoList',
            'upf_info': 'upfInfo',
            'upf_info_list': 'upfInfoList',
            'pcf_info': 'pcfInfo',
            'pcf_info_list': 'pcfInfoList',
            'bsf_info': 'bsfInfo',
            'bsf_info_list': 'bsfInfoList',
            'chf_info': 'chfInfo',
            'chf_info_list': 'chfInfoList',
            'nef_info': 'nefInfo',
            'nrf_info': 'nrfInfo',
            'udsf_info': 'udsfInfo',
            'udsf_info_list': 'udsfInfoList',
            'nwdaf_info': 'nwdafInfo',
            'nwdaf_info_list': 'nwdafInfoList',
            'pcscf_info_list': 'pcscfInfoList',
            'hss_info_list': 'hssInfoList',
            'custom_info': 'customInfo',
            'recovery_time': 'recoveryTime',
            'nf_service_persistence': 'nfServicePersistence',
            'nf_services': 'nfServices',
            'nf_service_list': 'nfServiceList',
            'nf_profile_changes_support_ind': 'nfProfileChangesSupportInd',
            'nf_profile_changes_ind': 'nfProfileChangesInd',
            'default_notification_subscriptions': 'defaultNotificationSubscriptions',
            'lmf_info': 'lmfInfo',
            'gmlc_info': 'gmlcInfo',
            'nf_set_id_list': 'nfSetIdList',
            'serving_scope': 'servingScope',
            'lc_h_support_ind': 'lcHSupportInd',
            'olc_h_support_ind': 'olcHSupportInd',
            'nf_set_recovery_time_list': 'nfSetRecoveryTimeList',
            'service_set_recovery_time_list': 'serviceSetRecoveryTimeList',
            'scp_domains': 'scpDomains',
            'scp_info': 'scpInfo',
            'sepp_info': 'seppInfo',
            'vendor_id': 'vendorId',
            'supported_vendor_specific_features': 'supportedVendorSpecificFeatures',
            'aanf_info_list': 'aanfInfoList',
            '_5g_ddnmf_info': '5gDdnmfInfo',
            'mfaf_info': 'mfafInfo',
            'easdf_info_list': 'easdfInfoList',
            'dccf_info': 'dccfInfo',
            'nsacf_info_list': 'nsacfInfoList',
            'mb_smf_info_list': 'mbSmfInfoList',
            'tsctsf_info_list': 'tsctsfInfoList',
            'mb_upf_info_list': 'mbUpfInfoList',
            'trust_af_info': 'trustAfInfo',
            'nssaaf_info': 'nssaafInfo',
            'hni_list': 'hniList',
            'iwmsc_info': 'iwmscInfo',
            'mnpf_info': 'mnpfInfo',
            'smsf_info': 'smsfInfo'
        }

        self._nf_instance_id = nf_instance_id
        self._nf_instance_name = nf_instance_name
        self._nf_type = nf_type
        self._nf_status = nf_status
        self._collocated_nf_instances = collocated_nf_instances
        self._heart_beat_timer = heart_beat_timer
        self._plmn_list = plmn_list
        self._snpn_list = snpn_list
        self._s_nssais = s_nssais
        self._per_plmn_snssai_list = per_plmn_snssai_list
        self._nsi_list = nsi_list
        self._fqdn = fqdn
        self._inter_plmn_fqdn = inter_plmn_fqdn
        self._ipv4_addresses = ipv4_addresses
        self._ipv6_addresses = ipv6_addresses
        self._allowed_plmns = allowed_plmns
        self._allowed_snpns = allowed_snpns
        self._allowed_nf_types = allowed_nf_types
        self._allowed_nf_domains = allowed_nf_domains
        self._allowed_nssais = allowed_nssais
        self._priority = priority
        self._capacity = capacity
        self._load = load
        self._load_time_stamp = load_time_stamp
        self._locality = locality
        self._ext_locality = ext_locality
        self._udr_info = udr_info
        self._udr_info_list = udr_info_list
        self._udm_info = udm_info
        self._udm_info_list = udm_info_list
        self._ausf_info = ausf_info
        self._ausf_info_list = ausf_info_list
        self._amf_info = amf_info
        self._amf_info_list = amf_info_list
        self._smf_info = smf_info
        self._smf_info_list = smf_info_list
        self._upf_info = upf_info
        self._upf_info_list = upf_info_list
        self._pcf_info = pcf_info
        self._pcf_info_list = pcf_info_list
        self._bsf_info = bsf_info
        self._bsf_info_list = bsf_info_list
        self._chf_info = chf_info
        self._chf_info_list = chf_info_list
        self._nef_info = nef_info
        self._nrf_info = nrf_info
        self._udsf_info = udsf_info
        self._udsf_info_list = udsf_info_list
        self._nwdaf_info = nwdaf_info
        self._nwdaf_info_list = nwdaf_info_list
        self._pcscf_info_list = pcscf_info_list
        self._hss_info_list = hss_info_list
        self._custom_info = custom_info
        self._recovery_time = recovery_time
        self._nf_service_persistence = nf_service_persistence
        self._nf_services = nf_services
        self._nf_service_list = nf_service_list
        self._nf_profile_changes_support_ind = nf_profile_changes_support_ind
        self._nf_profile_changes_ind = nf_profile_changes_ind
        self._default_notification_subscriptions = default_notification_subscriptions
        self._lmf_info = lmf_info
        self._gmlc_info = gmlc_info
        self._nf_set_id_list = nf_set_id_list
        self._serving_scope = serving_scope
        self._lc_h_support_ind = lc_h_support_ind
        self._olc_h_support_ind = olc_h_support_ind
        self._nf_set_recovery_time_list = nf_set_recovery_time_list
        self._service_set_recovery_time_list = service_set_recovery_time_list
        self._scp_domains = scp_domains
        self._scp_info = scp_info
        self._sepp_info = sepp_info
        self._vendor_id = vendor_id
        self._supported_vendor_specific_features = supported_vendor_specific_features
        self._aanf_info_list = aanf_info_list
        self.__5g_ddnmf_info = _5g_ddnmf_info
        self._mfaf_info = mfaf_info
        self._easdf_info_list = easdf_info_list
        self._dccf_info = dccf_info
        self._nsacf_info_list = nsacf_info_list
        self._mb_smf_info_list = mb_smf_info_list
        self._tsctsf_info_list = tsctsf_info_list
        self._mb_upf_info_list = mb_upf_info_list
        self._trust_af_info = trust_af_info
        self._nssaaf_info = nssaaf_info
        self._hni_list = hni_list
        self._iwmsc_info = iwmsc_info
        self._mnpf_info = mnpf_info
        self._smsf_info = smsf_info

    @classmethod
    def from_dict(cls, dikt) -> 'NFProfile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NFProfile of this NFProfile.  # noqa: E501
        :rtype: NFProfile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nf_instance_id(self):
        """Gets the nf_instance_id of this NFProfile.

        String uniquely identifying a NF instance. The format of the NF Instance ID shall be a  Universally Unique Identifier (UUID) version 4, as described in IETF RFC 4122.    # noqa: E501

        :return: The nf_instance_id of this NFProfile.
        :rtype: str
        """
        return self._nf_instance_id

    @nf_instance_id.setter
    def nf_instance_id(self, nf_instance_id):
        """Sets the nf_instance_id of this NFProfile.

        String uniquely identifying a NF instance. The format of the NF Instance ID shall be a  Universally Unique Identifier (UUID) version 4, as described in IETF RFC 4122.    # noqa: E501

        :param nf_instance_id: The nf_instance_id of this NFProfile.
        :type nf_instance_id: str
        """
        if nf_instance_id is None:
            raise ValueError("Invalid value for `nf_instance_id`, must not be `None`")  # noqa: E501

        self._nf_instance_id = nf_instance_id

    @property
    def nf_instance_name(self):
        """Gets the nf_instance_name of this NFProfile.


        :return: The nf_instance_name of this NFProfile.
        :rtype: str
        """
        return self._nf_instance_name

    @nf_instance_name.setter
    def nf_instance_name(self, nf_instance_name):
        """Sets the nf_instance_name of this NFProfile.


        :param nf_instance_name: The nf_instance_name of this NFProfile.
        :type nf_instance_name: str
        """

        self._nf_instance_name = nf_instance_name

    @property
    def nf_type(self):
        """Gets the nf_type of this NFProfile.


        :return: The nf_type of this NFProfile.
        :rtype: NFType
        """
        return self._nf_type

    @nf_type.setter
    def nf_type(self, nf_type):
        """Sets the nf_type of this NFProfile.


        :param nf_type: The nf_type of this NFProfile.
        :type nf_type: NFType
        """
        if nf_type is None:
            raise ValueError("Invalid value for `nf_type`, must not be `None`")  # noqa: E501

        self._nf_type = nf_type

    @property
    def nf_status(self):
        """Gets the nf_status of this NFProfile.


        :return: The nf_status of this NFProfile.
        :rtype: NfStatus
        """
        return self._nf_status

    @nf_status.setter
    def nf_status(self, nf_status):
        """Sets the nf_status of this NFProfile.


        :param nf_status: The nf_status of this NFProfile.
        :type nf_status: NfStatus
        """
        if nf_status is None:
            raise ValueError("Invalid value for `nf_status`, must not be `None`")  # noqa: E501

        self._nf_status = nf_status

    @property
    def collocated_nf_instances(self):
        """Gets the collocated_nf_instances of this NFProfile.


        :return: The collocated_nf_instances of this NFProfile.
        :rtype: List[CollocatedNfInstance]
        """
        return self._collocated_nf_instances

    @collocated_nf_instances.setter
    def collocated_nf_instances(self, collocated_nf_instances):
        """Sets the collocated_nf_instances of this NFProfile.


        :param collocated_nf_instances: The collocated_nf_instances of this NFProfile.
        :type collocated_nf_instances: List[CollocatedNfInstance]
        """

        self._collocated_nf_instances = collocated_nf_instances

    @property
    def heart_beat_timer(self):
        """Gets the heart_beat_timer of this NFProfile.


        :return: The heart_beat_timer of this NFProfile.
        :rtype: int
        """
        return self._heart_beat_timer

    @heart_beat_timer.setter
    def heart_beat_timer(self, heart_beat_timer):
        """Sets the heart_beat_timer of this NFProfile.


        :param heart_beat_timer: The heart_beat_timer of this NFProfile.
        :type heart_beat_timer: int
        """
        if heart_beat_timer is not None and heart_beat_timer < 1:  # noqa: E501
            raise ValueError("Invalid value for `heart_beat_timer`, must be a value greater than or equal to `1`")  # noqa: E501

        self._heart_beat_timer = heart_beat_timer

    @property
    def plmn_list(self):
        """Gets the plmn_list of this NFProfile.


        :return: The plmn_list of this NFProfile.
        :rtype: List[PlmnId]
        """
        return self._plmn_list

    @plmn_list.setter
    def plmn_list(self, plmn_list):
        """Sets the plmn_list of this NFProfile.


        :param plmn_list: The plmn_list of this NFProfile.
        :type plmn_list: List[PlmnId]
        """
        if plmn_list is not None and len(plmn_list) < 1:
            raise ValueError("Invalid value for `plmn_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._plmn_list = plmn_list

    @property
    def snpn_list(self):
        """Gets the snpn_list of this NFProfile.


        :return: The snpn_list of this NFProfile.
        :rtype: List[PlmnIdNid]
        """
        return self._snpn_list

    @snpn_list.setter
    def snpn_list(self, snpn_list):
        """Sets the snpn_list of this NFProfile.


        :param snpn_list: The snpn_list of this NFProfile.
        :type snpn_list: List[PlmnIdNid]
        """
        if snpn_list is not None and len(snpn_list) < 1:
            raise ValueError("Invalid value for `snpn_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._snpn_list = snpn_list

    @property
    def s_nssais(self):
        """Gets the s_nssais of this NFProfile.


        :return: The s_nssais of this NFProfile.
        :rtype: List[ExtSnssai]
        """
        return self._s_nssais

    @s_nssais.setter
    def s_nssais(self, s_nssais):
        """Sets the s_nssais of this NFProfile.


        :param s_nssais: The s_nssais of this NFProfile.
        :type s_nssais: List[ExtSnssai]
        """
        if s_nssais is not None and len(s_nssais) < 1:
            raise ValueError("Invalid value for `s_nssais`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._s_nssais = s_nssais

    @property
    def per_plmn_snssai_list(self):
        """Gets the per_plmn_snssai_list of this NFProfile.


        :return: The per_plmn_snssai_list of this NFProfile.
        :rtype: List[PlmnSnssai]
        """
        return self._per_plmn_snssai_list

    @per_plmn_snssai_list.setter
    def per_plmn_snssai_list(self, per_plmn_snssai_list):
        """Sets the per_plmn_snssai_list of this NFProfile.


        :param per_plmn_snssai_list: The per_plmn_snssai_list of this NFProfile.
        :type per_plmn_snssai_list: List[PlmnSnssai]
        """
        if per_plmn_snssai_list is not None and len(per_plmn_snssai_list) < 1:
            raise ValueError("Invalid value for `per_plmn_snssai_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._per_plmn_snssai_list = per_plmn_snssai_list

    @property
    def nsi_list(self):
        """Gets the nsi_list of this NFProfile.


        :return: The nsi_list of this NFProfile.
        :rtype: List[str]
        """
        return self._nsi_list

    @nsi_list.setter
    def nsi_list(self, nsi_list):
        """Sets the nsi_list of this NFProfile.


        :param nsi_list: The nsi_list of this NFProfile.
        :type nsi_list: List[str]
        """
        if nsi_list is not None and len(nsi_list) < 1:
            raise ValueError("Invalid value for `nsi_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._nsi_list = nsi_list

    @property
    def fqdn(self):
        """Gets the fqdn of this NFProfile.

        Fully Qualified Domain Name  # noqa: E501

        :return: The fqdn of this NFProfile.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this NFProfile.

        Fully Qualified Domain Name  # noqa: E501

        :param fqdn: The fqdn of this NFProfile.
        :type fqdn: str
        """
        if fqdn is not None and len(fqdn) > 253:
            raise ValueError("Invalid value for `fqdn`, length must be less than or equal to `253`")  # noqa: E501
        if fqdn is not None and len(fqdn) < 4:
            raise ValueError("Invalid value for `fqdn`, length must be greater than or equal to `4`")  # noqa: E501
        if fqdn is not None and not re.search(r'^([0-9A-Za-z]([-0-9A-Za-z]{0,61}[0-9A-Za-z])?\.)+[A-Za-z]{2,63}\.?$', fqdn):  # noqa: E501
            raise ValueError("Invalid value for `fqdn`, must be a follow pattern or equal to `/^([0-9A-Za-z]([-0-9A-Za-z]{0,61}[0-9A-Za-z])?\.)+[A-Za-z]{2,63}\.?$/`")  # noqa: E501

        self._fqdn = fqdn

    @property
    def inter_plmn_fqdn(self):
        """Gets the inter_plmn_fqdn of this NFProfile.

        Fully Qualified Domain Name  # noqa: E501

        :return: The inter_plmn_fqdn of this NFProfile.
        :rtype: str
        """
        return self._inter_plmn_fqdn

    @inter_plmn_fqdn.setter
    def inter_plmn_fqdn(self, inter_plmn_fqdn):
        """Sets the inter_plmn_fqdn of this NFProfile.

        Fully Qualified Domain Name  # noqa: E501

        :param inter_plmn_fqdn: The inter_plmn_fqdn of this NFProfile.
        :type inter_plmn_fqdn: str
        """
        if inter_plmn_fqdn is not None and len(inter_plmn_fqdn) > 253:
            raise ValueError("Invalid value for `inter_plmn_fqdn`, length must be less than or equal to `253`")  # noqa: E501
        if inter_plmn_fqdn is not None and len(inter_plmn_fqdn) < 4:
            raise ValueError("Invalid value for `inter_plmn_fqdn`, length must be greater than or equal to `4`")  # noqa: E501
        if inter_plmn_fqdn is not None and not re.search(r'^([0-9A-Za-z]([-0-9A-Za-z]{0,61}[0-9A-Za-z])?\.)+[A-Za-z]{2,63}\.?$', inter_plmn_fqdn):  # noqa: E501
            raise ValueError("Invalid value for `inter_plmn_fqdn`, must be a follow pattern or equal to `/^([0-9A-Za-z]([-0-9A-Za-z]{0,61}[0-9A-Za-z])?\.)+[A-Za-z]{2,63}\.?$/`")  # noqa: E501

        self._inter_plmn_fqdn = inter_plmn_fqdn

    @property
    def ipv4_addresses(self):
        """Gets the ipv4_addresses of this NFProfile.


        :return: The ipv4_addresses of this NFProfile.
        :rtype: List[str]
        """
        return self._ipv4_addresses

    @ipv4_addresses.setter
    def ipv4_addresses(self, ipv4_addresses):
        """Sets the ipv4_addresses of this NFProfile.


        :param ipv4_addresses: The ipv4_addresses of this NFProfile.
        :type ipv4_addresses: List[str]
        """
        if ipv4_addresses is not None and len(ipv4_addresses) < 1:
            raise ValueError("Invalid value for `ipv4_addresses`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ipv4_addresses = ipv4_addresses

    @property
    def ipv6_addresses(self):
        """Gets the ipv6_addresses of this NFProfile.


        :return: The ipv6_addresses of this NFProfile.
        :rtype: List[Ipv6Addr]
        """
        return self._ipv6_addresses

    @ipv6_addresses.setter
    def ipv6_addresses(self, ipv6_addresses):
        """Sets the ipv6_addresses of this NFProfile.


        :param ipv6_addresses: The ipv6_addresses of this NFProfile.
        :type ipv6_addresses: List[Ipv6Addr]
        """
        if ipv6_addresses is not None and len(ipv6_addresses) < 1:
            raise ValueError("Invalid value for `ipv6_addresses`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ipv6_addresses = ipv6_addresses

    @property
    def allowed_plmns(self):
        """Gets the allowed_plmns of this NFProfile.


        :return: The allowed_plmns of this NFProfile.
        :rtype: List[PlmnId]
        """
        return self._allowed_plmns

    @allowed_plmns.setter
    def allowed_plmns(self, allowed_plmns):
        """Sets the allowed_plmns of this NFProfile.


        :param allowed_plmns: The allowed_plmns of this NFProfile.
        :type allowed_plmns: List[PlmnId]
        """
        if allowed_plmns is not None and len(allowed_plmns) < 1:
            raise ValueError("Invalid value for `allowed_plmns`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._allowed_plmns = allowed_plmns

    @property
    def allowed_snpns(self):
        """Gets the allowed_snpns of this NFProfile.


        :return: The allowed_snpns of this NFProfile.
        :rtype: List[PlmnIdNid]
        """
        return self._allowed_snpns

    @allowed_snpns.setter
    def allowed_snpns(self, allowed_snpns):
        """Sets the allowed_snpns of this NFProfile.


        :param allowed_snpns: The allowed_snpns of this NFProfile.
        :type allowed_snpns: List[PlmnIdNid]
        """
        if allowed_snpns is not None and len(allowed_snpns) < 1:
            raise ValueError("Invalid value for `allowed_snpns`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._allowed_snpns = allowed_snpns

    @property
    def allowed_nf_types(self):
        """Gets the allowed_nf_types of this NFProfile.


        :return: The allowed_nf_types of this NFProfile.
        :rtype: List[NFType]
        """
        return self._allowed_nf_types

    @allowed_nf_types.setter
    def allowed_nf_types(self, allowed_nf_types):
        """Sets the allowed_nf_types of this NFProfile.


        :param allowed_nf_types: The allowed_nf_types of this NFProfile.
        :type allowed_nf_types: List[NFType]
        """
        if allowed_nf_types is not None and len(allowed_nf_types) < 1:
            raise ValueError("Invalid value for `allowed_nf_types`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._allowed_nf_types = allowed_nf_types

    @property
    def allowed_nf_domains(self):
        """Gets the allowed_nf_domains of this NFProfile.


        :return: The allowed_nf_domains of this NFProfile.
        :rtype: List[str]
        """
        return self._allowed_nf_domains

    @allowed_nf_domains.setter
    def allowed_nf_domains(self, allowed_nf_domains):
        """Sets the allowed_nf_domains of this NFProfile.


        :param allowed_nf_domains: The allowed_nf_domains of this NFProfile.
        :type allowed_nf_domains: List[str]
        """
        if allowed_nf_domains is not None and len(allowed_nf_domains) < 1:
            raise ValueError("Invalid value for `allowed_nf_domains`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._allowed_nf_domains = allowed_nf_domains

    @property
    def allowed_nssais(self):
        """Gets the allowed_nssais of this NFProfile.


        :return: The allowed_nssais of this NFProfile.
        :rtype: List[ExtSnssai]
        """
        return self._allowed_nssais

    @allowed_nssais.setter
    def allowed_nssais(self, allowed_nssais):
        """Sets the allowed_nssais of this NFProfile.


        :param allowed_nssais: The allowed_nssais of this NFProfile.
        :type allowed_nssais: List[ExtSnssai]
        """
        if allowed_nssais is not None and len(allowed_nssais) < 1:
            raise ValueError("Invalid value for `allowed_nssais`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._allowed_nssais = allowed_nssais

    @property
    def priority(self):
        """Gets the priority of this NFProfile.


        :return: The priority of this NFProfile.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this NFProfile.


        :param priority: The priority of this NFProfile.
        :type priority: int
        """
        if priority is not None and priority > 65535:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value less than or equal to `65535`")  # noqa: E501
        if priority is not None and priority < 0:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value greater than or equal to `0`")  # noqa: E501

        self._priority = priority

    @property
    def capacity(self):
        """Gets the capacity of this NFProfile.


        :return: The capacity of this NFProfile.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this NFProfile.


        :param capacity: The capacity of this NFProfile.
        :type capacity: int
        """
        if capacity is not None and capacity > 65535:  # noqa: E501
            raise ValueError("Invalid value for `capacity`, must be a value less than or equal to `65535`")  # noqa: E501
        if capacity is not None and capacity < 0:  # noqa: E501
            raise ValueError("Invalid value for `capacity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._capacity = capacity

    @property
    def load(self):
        """Gets the load of this NFProfile.


        :return: The load of this NFProfile.
        :rtype: int
        """
        return self._load

    @load.setter
    def load(self, load):
        """Sets the load of this NFProfile.


        :param load: The load of this NFProfile.
        :type load: int
        """
        if load is not None and load > 100:  # noqa: E501
            raise ValueError("Invalid value for `load`, must be a value less than or equal to `100`")  # noqa: E501
        if load is not None and load < 0:  # noqa: E501
            raise ValueError("Invalid value for `load`, must be a value greater than or equal to `0`")  # noqa: E501

        self._load = load

    @property
    def load_time_stamp(self):
        """Gets the load_time_stamp of this NFProfile.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :return: The load_time_stamp of this NFProfile.
        :rtype: datetime
        """
        return self._load_time_stamp

    @load_time_stamp.setter
    def load_time_stamp(self, load_time_stamp):
        """Sets the load_time_stamp of this NFProfile.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :param load_time_stamp: The load_time_stamp of this NFProfile.
        :type load_time_stamp: datetime
        """

        self._load_time_stamp = load_time_stamp

    @property
    def locality(self):
        """Gets the locality of this NFProfile.


        :return: The locality of this NFProfile.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this NFProfile.


        :param locality: The locality of this NFProfile.
        :type locality: str
        """

        self._locality = locality

    @property
    def ext_locality(self):
        """Gets the ext_locality of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key representing a type of locality   # noqa: E501

        :return: The ext_locality of this NFProfile.
        :rtype: Dict[str, str]
        """
        return self._ext_locality

    @ext_locality.setter
    def ext_locality(self, ext_locality):
        """Sets the ext_locality of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key representing a type of locality   # noqa: E501

        :param ext_locality: The ext_locality of this NFProfile.
        :type ext_locality: Dict[str, str]
        """
        if ext_locality is not None and len(ext_locality) < 1:
            raise ValueError("Invalid value for `ext_locality`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ext_locality = ext_locality

    @property
    def udr_info(self):
        """Gets the udr_info of this NFProfile.


        :return: The udr_info of this NFProfile.
        :rtype: UdrInfo
        """
        return self._udr_info

    @udr_info.setter
    def udr_info(self, udr_info):
        """Sets the udr_info of this NFProfile.


        :param udr_info: The udr_info of this NFProfile.
        :type udr_info: UdrInfo
        """

        self._udr_info = udr_info

    @property
    def udr_info_list(self):
        """Gets the udr_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of UdrInfo   # noqa: E501

        :return: The udr_info_list of this NFProfile.
        :rtype: Dict[str, UdrInfo]
        """
        return self._udr_info_list

    @udr_info_list.setter
    def udr_info_list(self, udr_info_list):
        """Sets the udr_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of UdrInfo   # noqa: E501

        :param udr_info_list: The udr_info_list of this NFProfile.
        :type udr_info_list: Dict[str, UdrInfo]
        """
        if udr_info_list is not None and len(udr_info_list) < 1:
            raise ValueError("Invalid value for `udr_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._udr_info_list = udr_info_list

    @property
    def udm_info(self):
        """Gets the udm_info of this NFProfile.


        :return: The udm_info of this NFProfile.
        :rtype: UdmInfo
        """
        return self._udm_info

    @udm_info.setter
    def udm_info(self, udm_info):
        """Sets the udm_info of this NFProfile.


        :param udm_info: The udm_info of this NFProfile.
        :type udm_info: UdmInfo
        """

        self._udm_info = udm_info

    @property
    def udm_info_list(self):
        """Gets the udm_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of UdmInfo   # noqa: E501

        :return: The udm_info_list of this NFProfile.
        :rtype: Dict[str, UdmInfo]
        """
        return self._udm_info_list

    @udm_info_list.setter
    def udm_info_list(self, udm_info_list):
        """Sets the udm_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of UdmInfo   # noqa: E501

        :param udm_info_list: The udm_info_list of this NFProfile.
        :type udm_info_list: Dict[str, UdmInfo]
        """
        if udm_info_list is not None and len(udm_info_list) < 1:
            raise ValueError("Invalid value for `udm_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._udm_info_list = udm_info_list

    @property
    def ausf_info(self):
        """Gets the ausf_info of this NFProfile.


        :return: The ausf_info of this NFProfile.
        :rtype: AusfInfo
        """
        return self._ausf_info

    @ausf_info.setter
    def ausf_info(self, ausf_info):
        """Sets the ausf_info of this NFProfile.


        :param ausf_info: The ausf_info of this NFProfile.
        :type ausf_info: AusfInfo
        """

        self._ausf_info = ausf_info

    @property
    def ausf_info_list(self):
        """Gets the ausf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of AusfInfo   # noqa: E501

        :return: The ausf_info_list of this NFProfile.
        :rtype: Dict[str, AusfInfo]
        """
        return self._ausf_info_list

    @ausf_info_list.setter
    def ausf_info_list(self, ausf_info_list):
        """Sets the ausf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of AusfInfo   # noqa: E501

        :param ausf_info_list: The ausf_info_list of this NFProfile.
        :type ausf_info_list: Dict[str, AusfInfo]
        """
        if ausf_info_list is not None and len(ausf_info_list) < 1:
            raise ValueError("Invalid value for `ausf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ausf_info_list = ausf_info_list

    @property
    def amf_info(self):
        """Gets the amf_info of this NFProfile.


        :return: The amf_info of this NFProfile.
        :rtype: AmfInfo
        """
        return self._amf_info

    @amf_info.setter
    def amf_info(self, amf_info):
        """Sets the amf_info of this NFProfile.


        :param amf_info: The amf_info of this NFProfile.
        :type amf_info: AmfInfo
        """

        self._amf_info = amf_info

    @property
    def amf_info_list(self):
        """Gets the amf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of AmfInfo   # noqa: E501

        :return: The amf_info_list of this NFProfile.
        :rtype: Dict[str, AmfInfo]
        """
        return self._amf_info_list

    @amf_info_list.setter
    def amf_info_list(self, amf_info_list):
        """Sets the amf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of AmfInfo   # noqa: E501

        :param amf_info_list: The amf_info_list of this NFProfile.
        :type amf_info_list: Dict[str, AmfInfo]
        """
        if amf_info_list is not None and len(amf_info_list) < 1:
            raise ValueError("Invalid value for `amf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._amf_info_list = amf_info_list

    @property
    def smf_info(self):
        """Gets the smf_info of this NFProfile.


        :return: The smf_info of this NFProfile.
        :rtype: SmfInfo
        """
        return self._smf_info

    @smf_info.setter
    def smf_info(self, smf_info):
        """Sets the smf_info of this NFProfile.


        :param smf_info: The smf_info of this NFProfile.
        :type smf_info: SmfInfo
        """

        self._smf_info = smf_info

    @property
    def smf_info_list(self):
        """Gets the smf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of SmfInfo   # noqa: E501

        :return: The smf_info_list of this NFProfile.
        :rtype: Dict[str, SmfInfo]
        """
        return self._smf_info_list

    @smf_info_list.setter
    def smf_info_list(self, smf_info_list):
        """Sets the smf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of SmfInfo   # noqa: E501

        :param smf_info_list: The smf_info_list of this NFProfile.
        :type smf_info_list: Dict[str, SmfInfo]
        """
        if smf_info_list is not None and len(smf_info_list) < 1:
            raise ValueError("Invalid value for `smf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._smf_info_list = smf_info_list

    @property
    def upf_info(self):
        """Gets the upf_info of this NFProfile.


        :return: The upf_info of this NFProfile.
        :rtype: UpfInfo
        """
        return self._upf_info

    @upf_info.setter
    def upf_info(self, upf_info):
        """Sets the upf_info of this NFProfile.


        :param upf_info: The upf_info of this NFProfile.
        :type upf_info: UpfInfo
        """

        self._upf_info = upf_info

    @property
    def upf_info_list(self):
        """Gets the upf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of UpfInfo   # noqa: E501

        :return: The upf_info_list of this NFProfile.
        :rtype: Dict[str, UpfInfo]
        """
        return self._upf_info_list

    @upf_info_list.setter
    def upf_info_list(self, upf_info_list):
        """Sets the upf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of UpfInfo   # noqa: E501

        :param upf_info_list: The upf_info_list of this NFProfile.
        :type upf_info_list: Dict[str, UpfInfo]
        """
        if upf_info_list is not None and len(upf_info_list) < 1:
            raise ValueError("Invalid value for `upf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._upf_info_list = upf_info_list

    @property
    def pcf_info(self):
        """Gets the pcf_info of this NFProfile.


        :return: The pcf_info of this NFProfile.
        :rtype: PcfInfo
        """
        return self._pcf_info

    @pcf_info.setter
    def pcf_info(self, pcf_info):
        """Sets the pcf_info of this NFProfile.


        :param pcf_info: The pcf_info of this NFProfile.
        :type pcf_info: PcfInfo
        """

        self._pcf_info = pcf_info

    @property
    def pcf_info_list(self):
        """Gets the pcf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of PcfInfo   # noqa: E501

        :return: The pcf_info_list of this NFProfile.
        :rtype: Dict[str, PcfInfo]
        """
        return self._pcf_info_list

    @pcf_info_list.setter
    def pcf_info_list(self, pcf_info_list):
        """Sets the pcf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of PcfInfo   # noqa: E501

        :param pcf_info_list: The pcf_info_list of this NFProfile.
        :type pcf_info_list: Dict[str, PcfInfo]
        """
        if pcf_info_list is not None and len(pcf_info_list) < 1:
            raise ValueError("Invalid value for `pcf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._pcf_info_list = pcf_info_list

    @property
    def bsf_info(self):
        """Gets the bsf_info of this NFProfile.


        :return: The bsf_info of this NFProfile.
        :rtype: BsfInfo
        """
        return self._bsf_info

    @bsf_info.setter
    def bsf_info(self, bsf_info):
        """Sets the bsf_info of this NFProfile.


        :param bsf_info: The bsf_info of this NFProfile.
        :type bsf_info: BsfInfo
        """

        self._bsf_info = bsf_info

    @property
    def bsf_info_list(self):
        """Gets the bsf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of BsfInfo   # noqa: E501

        :return: The bsf_info_list of this NFProfile.
        :rtype: Dict[str, BsfInfo]
        """
        return self._bsf_info_list

    @bsf_info_list.setter
    def bsf_info_list(self, bsf_info_list):
        """Sets the bsf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of BsfInfo   # noqa: E501

        :param bsf_info_list: The bsf_info_list of this NFProfile.
        :type bsf_info_list: Dict[str, BsfInfo]
        """
        if bsf_info_list is not None and len(bsf_info_list) < 1:
            raise ValueError("Invalid value for `bsf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._bsf_info_list = bsf_info_list

    @property
    def chf_info(self):
        """Gets the chf_info of this NFProfile.


        :return: The chf_info of this NFProfile.
        :rtype: ChfInfo
        """
        return self._chf_info

    @chf_info.setter
    def chf_info(self, chf_info):
        """Sets the chf_info of this NFProfile.


        :param chf_info: The chf_info of this NFProfile.
        :type chf_info: ChfInfo
        """

        self._chf_info = chf_info

    @property
    def chf_info_list(self):
        """Gets the chf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of ChfInfo   # noqa: E501

        :return: The chf_info_list of this NFProfile.
        :rtype: Dict[str, ChfInfo]
        """
        return self._chf_info_list

    @chf_info_list.setter
    def chf_info_list(self, chf_info_list):
        """Sets the chf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of ChfInfo   # noqa: E501

        :param chf_info_list: The chf_info_list of this NFProfile.
        :type chf_info_list: Dict[str, ChfInfo]
        """
        if chf_info_list is not None and len(chf_info_list) < 1:
            raise ValueError("Invalid value for `chf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._chf_info_list = chf_info_list

    @property
    def nef_info(self):
        """Gets the nef_info of this NFProfile.


        :return: The nef_info of this NFProfile.
        :rtype: NefInfo
        """
        return self._nef_info

    @nef_info.setter
    def nef_info(self, nef_info):
        """Sets the nef_info of this NFProfile.


        :param nef_info: The nef_info of this NFProfile.
        :type nef_info: NefInfo
        """

        self._nef_info = nef_info

    @property
    def nrf_info(self):
        """Gets the nrf_info of this NFProfile.


        :return: The nrf_info of this NFProfile.
        :rtype: NrfInfo
        """
        return self._nrf_info

    @nrf_info.setter
    def nrf_info(self, nrf_info):
        """Sets the nrf_info of this NFProfile.


        :param nrf_info: The nrf_info of this NFProfile.
        :type nrf_info: NrfInfo
        """

        self._nrf_info = nrf_info

    @property
    def udsf_info(self):
        """Gets the udsf_info of this NFProfile.


        :return: The udsf_info of this NFProfile.
        :rtype: UdsfInfo
        """
        return self._udsf_info

    @udsf_info.setter
    def udsf_info(self, udsf_info):
        """Sets the udsf_info of this NFProfile.


        :param udsf_info: The udsf_info of this NFProfile.
        :type udsf_info: UdsfInfo
        """

        self._udsf_info = udsf_info

    @property
    def udsf_info_list(self):
        """Gets the udsf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of UdsfInfo   # noqa: E501

        :return: The udsf_info_list of this NFProfile.
        :rtype: Dict[str, UdsfInfo]
        """
        return self._udsf_info_list

    @udsf_info_list.setter
    def udsf_info_list(self, udsf_info_list):
        """Sets the udsf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of UdsfInfo   # noqa: E501

        :param udsf_info_list: The udsf_info_list of this NFProfile.
        :type udsf_info_list: Dict[str, UdsfInfo]
        """
        if udsf_info_list is not None and len(udsf_info_list) < 1:
            raise ValueError("Invalid value for `udsf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._udsf_info_list = udsf_info_list

    @property
    def nwdaf_info(self):
        """Gets the nwdaf_info of this NFProfile.


        :return: The nwdaf_info of this NFProfile.
        :rtype: NwdafInfo
        """
        return self._nwdaf_info

    @nwdaf_info.setter
    def nwdaf_info(self, nwdaf_info):
        """Sets the nwdaf_info of this NFProfile.


        :param nwdaf_info: The nwdaf_info of this NFProfile.
        :type nwdaf_info: NwdafInfo
        """

        self._nwdaf_info = nwdaf_info

    @property
    def nwdaf_info_list(self):
        """Gets the nwdaf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of NwdafInfo   # noqa: E501

        :return: The nwdaf_info_list of this NFProfile.
        :rtype: Dict[str, NwdafInfo]
        """
        return self._nwdaf_info_list

    @nwdaf_info_list.setter
    def nwdaf_info_list(self, nwdaf_info_list):
        """Sets the nwdaf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of NwdafInfo   # noqa: E501

        :param nwdaf_info_list: The nwdaf_info_list of this NFProfile.
        :type nwdaf_info_list: Dict[str, NwdafInfo]
        """
        if nwdaf_info_list is not None and len(nwdaf_info_list) < 1:
            raise ValueError("Invalid value for `nwdaf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._nwdaf_info_list = nwdaf_info_list

    @property
    def pcscf_info_list(self):
        """Gets the pcscf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of PcscfInfo   # noqa: E501

        :return: The pcscf_info_list of this NFProfile.
        :rtype: Dict[str, PcscfInfo]
        """
        return self._pcscf_info_list

    @pcscf_info_list.setter
    def pcscf_info_list(self, pcscf_info_list):
        """Sets the pcscf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of PcscfInfo   # noqa: E501

        :param pcscf_info_list: The pcscf_info_list of this NFProfile.
        :type pcscf_info_list: Dict[str, PcscfInfo]
        """
        if pcscf_info_list is not None and len(pcscf_info_list) < 1:
            raise ValueError("Invalid value for `pcscf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._pcscf_info_list = pcscf_info_list

    @property
    def hss_info_list(self):
        """Gets the hss_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of HssInfo   # noqa: E501

        :return: The hss_info_list of this NFProfile.
        :rtype: Dict[str, HssInfo]
        """
        return self._hss_info_list

    @hss_info_list.setter
    def hss_info_list(self, hss_info_list):
        """Sets the hss_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of HssInfo   # noqa: E501

        :param hss_info_list: The hss_info_list of this NFProfile.
        :type hss_info_list: Dict[str, HssInfo]
        """
        if hss_info_list is not None and len(hss_info_list) < 1:
            raise ValueError("Invalid value for `hss_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._hss_info_list = hss_info_list

    @property
    def custom_info(self):
        """Gets the custom_info of this NFProfile.


        :return: The custom_info of this NFProfile.
        :rtype: object
        """
        return self._custom_info

    @custom_info.setter
    def custom_info(self, custom_info):
        """Sets the custom_info of this NFProfile.


        :param custom_info: The custom_info of this NFProfile.
        :type custom_info: object
        """

        self._custom_info = custom_info

    @property
    def recovery_time(self):
        """Gets the recovery_time of this NFProfile.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :return: The recovery_time of this NFProfile.
        :rtype: datetime
        """
        return self._recovery_time

    @recovery_time.setter
    def recovery_time(self, recovery_time):
        """Sets the recovery_time of this NFProfile.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :param recovery_time: The recovery_time of this NFProfile.
        :type recovery_time: datetime
        """

        self._recovery_time = recovery_time

    @property
    def nf_service_persistence(self):
        """Gets the nf_service_persistence of this NFProfile.


        :return: The nf_service_persistence of this NFProfile.
        :rtype: bool
        """
        return self._nf_service_persistence

    @nf_service_persistence.setter
    def nf_service_persistence(self, nf_service_persistence):
        """Sets the nf_service_persistence of this NFProfile.


        :param nf_service_persistence: The nf_service_persistence of this NFProfile.
        :type nf_service_persistence: bool
        """

        self._nf_service_persistence = nf_service_persistence

    @property
    def nf_services(self):
        """Gets the nf_services of this NFProfile.


        :return: The nf_services of this NFProfile.
        :rtype: List[NFService]
        """
        return self._nf_services

    @nf_services.setter
    def nf_services(self, nf_services):
        """Sets the nf_services of this NFProfile.


        :param nf_services: The nf_services of this NFProfile.
        :type nf_services: List[NFService]
        """
        if nf_services is not None and len(nf_services) < 1:
            raise ValueError("Invalid value for `nf_services`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._nf_services = nf_services

    @property
    def nf_service_list(self):
        """Gets the nf_service_list of this NFProfile.

        A map (list of key-value pairs) where serviceInstanceId serves as key of NFService   # noqa: E501

        :return: The nf_service_list of this NFProfile.
        :rtype: Dict[str, NFService]
        """
        return self._nf_service_list

    @nf_service_list.setter
    def nf_service_list(self, nf_service_list):
        """Sets the nf_service_list of this NFProfile.

        A map (list of key-value pairs) where serviceInstanceId serves as key of NFService   # noqa: E501

        :param nf_service_list: The nf_service_list of this NFProfile.
        :type nf_service_list: Dict[str, NFService]
        """
        if nf_service_list is not None and len(nf_service_list) < 1:
            raise ValueError("Invalid value for `nf_service_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._nf_service_list = nf_service_list

    @property
    def nf_profile_changes_support_ind(self):
        """Gets the nf_profile_changes_support_ind of this NFProfile.


        :return: The nf_profile_changes_support_ind of this NFProfile.
        :rtype: bool
        """
        return self._nf_profile_changes_support_ind

    @nf_profile_changes_support_ind.setter
    def nf_profile_changes_support_ind(self, nf_profile_changes_support_ind):
        """Sets the nf_profile_changes_support_ind of this NFProfile.


        :param nf_profile_changes_support_ind: The nf_profile_changes_support_ind of this NFProfile.
        :type nf_profile_changes_support_ind: bool
        """

        self._nf_profile_changes_support_ind = nf_profile_changes_support_ind

    @property
    def nf_profile_changes_ind(self):
        """Gets the nf_profile_changes_ind of this NFProfile.


        :return: The nf_profile_changes_ind of this NFProfile.
        :rtype: bool
        """
        return self._nf_profile_changes_ind

    @nf_profile_changes_ind.setter
    def nf_profile_changes_ind(self, nf_profile_changes_ind):
        """Sets the nf_profile_changes_ind of this NFProfile.


        :param nf_profile_changes_ind: The nf_profile_changes_ind of this NFProfile.
        :type nf_profile_changes_ind: bool
        """

        self._nf_profile_changes_ind = nf_profile_changes_ind

    @property
    def default_notification_subscriptions(self):
        """Gets the default_notification_subscriptions of this NFProfile.


        :return: The default_notification_subscriptions of this NFProfile.
        :rtype: List[DefaultNotificationSubscription]
        """
        return self._default_notification_subscriptions

    @default_notification_subscriptions.setter
    def default_notification_subscriptions(self, default_notification_subscriptions):
        """Sets the default_notification_subscriptions of this NFProfile.


        :param default_notification_subscriptions: The default_notification_subscriptions of this NFProfile.
        :type default_notification_subscriptions: List[DefaultNotificationSubscription]
        """

        self._default_notification_subscriptions = default_notification_subscriptions

    @property
    def lmf_info(self):
        """Gets the lmf_info of this NFProfile.


        :return: The lmf_info of this NFProfile.
        :rtype: LmfInfo
        """
        return self._lmf_info

    @lmf_info.setter
    def lmf_info(self, lmf_info):
        """Sets the lmf_info of this NFProfile.


        :param lmf_info: The lmf_info of this NFProfile.
        :type lmf_info: LmfInfo
        """

        self._lmf_info = lmf_info

    @property
    def gmlc_info(self):
        """Gets the gmlc_info of this NFProfile.


        :return: The gmlc_info of this NFProfile.
        :rtype: GmlcInfo
        """
        return self._gmlc_info

    @gmlc_info.setter
    def gmlc_info(self, gmlc_info):
        """Sets the gmlc_info of this NFProfile.


        :param gmlc_info: The gmlc_info of this NFProfile.
        :type gmlc_info: GmlcInfo
        """

        self._gmlc_info = gmlc_info

    @property
    def nf_set_id_list(self):
        """Gets the nf_set_id_list of this NFProfile.


        :return: The nf_set_id_list of this NFProfile.
        :rtype: List[str]
        """
        return self._nf_set_id_list

    @nf_set_id_list.setter
    def nf_set_id_list(self, nf_set_id_list):
        """Sets the nf_set_id_list of this NFProfile.


        :param nf_set_id_list: The nf_set_id_list of this NFProfile.
        :type nf_set_id_list: List[str]
        """
        if nf_set_id_list is not None and len(nf_set_id_list) < 1:
            raise ValueError("Invalid value for `nf_set_id_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._nf_set_id_list = nf_set_id_list

    @property
    def serving_scope(self):
        """Gets the serving_scope of this NFProfile.


        :return: The serving_scope of this NFProfile.
        :rtype: List[str]
        """
        return self._serving_scope

    @serving_scope.setter
    def serving_scope(self, serving_scope):
        """Sets the serving_scope of this NFProfile.


        :param serving_scope: The serving_scope of this NFProfile.
        :type serving_scope: List[str]
        """
        if serving_scope is not None and len(serving_scope) < 1:
            raise ValueError("Invalid value for `serving_scope`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._serving_scope = serving_scope

    @property
    def lc_h_support_ind(self):
        """Gets the lc_h_support_ind of this NFProfile.


        :return: The lc_h_support_ind of this NFProfile.
        :rtype: bool
        """
        return self._lc_h_support_ind

    @lc_h_support_ind.setter
    def lc_h_support_ind(self, lc_h_support_ind):
        """Sets the lc_h_support_ind of this NFProfile.


        :param lc_h_support_ind: The lc_h_support_ind of this NFProfile.
        :type lc_h_support_ind: bool
        """

        self._lc_h_support_ind = lc_h_support_ind

    @property
    def olc_h_support_ind(self):
        """Gets the olc_h_support_ind of this NFProfile.


        :return: The olc_h_support_ind of this NFProfile.
        :rtype: bool
        """
        return self._olc_h_support_ind

    @olc_h_support_ind.setter
    def olc_h_support_ind(self, olc_h_support_ind):
        """Sets the olc_h_support_ind of this NFProfile.


        :param olc_h_support_ind: The olc_h_support_ind of this NFProfile.
        :type olc_h_support_ind: bool
        """

        self._olc_h_support_ind = olc_h_support_ind

    @property
    def nf_set_recovery_time_list(self):
        """Gets the nf_set_recovery_time_list of this NFProfile.

        A map (list of key-value pairs) where NfSetId serves as key of DateTime  # noqa: E501

        :return: The nf_set_recovery_time_list of this NFProfile.
        :rtype: Dict[str, datetime]
        """
        return self._nf_set_recovery_time_list

    @nf_set_recovery_time_list.setter
    def nf_set_recovery_time_list(self, nf_set_recovery_time_list):
        """Sets the nf_set_recovery_time_list of this NFProfile.

        A map (list of key-value pairs) where NfSetId serves as key of DateTime  # noqa: E501

        :param nf_set_recovery_time_list: The nf_set_recovery_time_list of this NFProfile.
        :type nf_set_recovery_time_list: Dict[str, datetime]
        """
        if nf_set_recovery_time_list is not None and len(nf_set_recovery_time_list) < 1:
            raise ValueError("Invalid value for `nf_set_recovery_time_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._nf_set_recovery_time_list = nf_set_recovery_time_list

    @property
    def service_set_recovery_time_list(self):
        """Gets the service_set_recovery_time_list of this NFProfile.

        A map (list of key-value pairs) where NfServiceSetId serves as key of DateTime   # noqa: E501

        :return: The service_set_recovery_time_list of this NFProfile.
        :rtype: Dict[str, datetime]
        """
        return self._service_set_recovery_time_list

    @service_set_recovery_time_list.setter
    def service_set_recovery_time_list(self, service_set_recovery_time_list):
        """Sets the service_set_recovery_time_list of this NFProfile.

        A map (list of key-value pairs) where NfServiceSetId serves as key of DateTime   # noqa: E501

        :param service_set_recovery_time_list: The service_set_recovery_time_list of this NFProfile.
        :type service_set_recovery_time_list: Dict[str, datetime]
        """
        if service_set_recovery_time_list is not None and len(service_set_recovery_time_list) < 1:
            raise ValueError("Invalid value for `service_set_recovery_time_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._service_set_recovery_time_list = service_set_recovery_time_list

    @property
    def scp_domains(self):
        """Gets the scp_domains of this NFProfile.


        :return: The scp_domains of this NFProfile.
        :rtype: List[str]
        """
        return self._scp_domains

    @scp_domains.setter
    def scp_domains(self, scp_domains):
        """Sets the scp_domains of this NFProfile.


        :param scp_domains: The scp_domains of this NFProfile.
        :type scp_domains: List[str]
        """
        if scp_domains is not None and len(scp_domains) < 1:
            raise ValueError("Invalid value for `scp_domains`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._scp_domains = scp_domains

    @property
    def scp_info(self):
        """Gets the scp_info of this NFProfile.


        :return: The scp_info of this NFProfile.
        :rtype: ScpInfo
        """
        return self._scp_info

    @scp_info.setter
    def scp_info(self, scp_info):
        """Sets the scp_info of this NFProfile.


        :param scp_info: The scp_info of this NFProfile.
        :type scp_info: ScpInfo
        """

        self._scp_info = scp_info

    @property
    def sepp_info(self):
        """Gets the sepp_info of this NFProfile.


        :return: The sepp_info of this NFProfile.
        :rtype: SeppInfo
        """
        return self._sepp_info

    @sepp_info.setter
    def sepp_info(self, sepp_info):
        """Sets the sepp_info of this NFProfile.


        :param sepp_info: The sepp_info of this NFProfile.
        :type sepp_info: SeppInfo
        """

        self._sepp_info = sepp_info

    @property
    def vendor_id(self):
        """Gets the vendor_id of this NFProfile.

        Vendor ID of the NF Service instance (Private Enterprise Number assigned by IANA)  # noqa: E501

        :return: The vendor_id of this NFProfile.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """Sets the vendor_id of this NFProfile.

        Vendor ID of the NF Service instance (Private Enterprise Number assigned by IANA)  # noqa: E501

        :param vendor_id: The vendor_id of this NFProfile.
        :type vendor_id: str
        """
        if vendor_id is not None and not re.search(r'^[0-9]{6}$', vendor_id):  # noqa: E501
            raise ValueError("Invalid value for `vendor_id`, must be a follow pattern or equal to `/^[0-9]{6}$/`")  # noqa: E501

        self._vendor_id = vendor_id

    @property
    def supported_vendor_specific_features(self):
        """Gets the supported_vendor_specific_features of this NFProfile.

        The key of the map is the IANA-assigned SMI Network Management Private Enterprise Codes   # noqa: E501

        :return: The supported_vendor_specific_features of this NFProfile.
        :rtype: Dict[str, List[VendorSpecificFeature]]
        """
        return self._supported_vendor_specific_features

    @supported_vendor_specific_features.setter
    def supported_vendor_specific_features(self, supported_vendor_specific_features):
        """Sets the supported_vendor_specific_features of this NFProfile.

        The key of the map is the IANA-assigned SMI Network Management Private Enterprise Codes   # noqa: E501

        :param supported_vendor_specific_features: The supported_vendor_specific_features of this NFProfile.
        :type supported_vendor_specific_features: Dict[str, List[VendorSpecificFeature]]
        """
        if supported_vendor_specific_features is not None and len(supported_vendor_specific_features) < 1:
            raise ValueError("Invalid value for `supported_vendor_specific_features`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._supported_vendor_specific_features = supported_vendor_specific_features

    @property
    def aanf_info_list(self):
        """Gets the aanf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of AanfInfo   # noqa: E501

        :return: The aanf_info_list of this NFProfile.
        :rtype: Dict[str, AanfInfo]
        """
        return self._aanf_info_list

    @aanf_info_list.setter
    def aanf_info_list(self, aanf_info_list):
        """Sets the aanf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of AanfInfo   # noqa: E501

        :param aanf_info_list: The aanf_info_list of this NFProfile.
        :type aanf_info_list: Dict[str, AanfInfo]
        """
        if aanf_info_list is not None and len(aanf_info_list) < 1:
            raise ValueError("Invalid value for `aanf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._aanf_info_list = aanf_info_list

    @property
    def _5g_ddnmf_info(self):
        """Gets the _5g_ddnmf_info of this NFProfile.


        :return: The _5g_ddnmf_info of this NFProfile.
        :rtype: Model5GDdnmfInfo
        """
        return self.__5g_ddnmf_info

    @_5g_ddnmf_info.setter
    def _5g_ddnmf_info(self, _5g_ddnmf_info):
        """Sets the _5g_ddnmf_info of this NFProfile.


        :param _5g_ddnmf_info: The _5g_ddnmf_info of this NFProfile.
        :type _5g_ddnmf_info: Model5GDdnmfInfo
        """

        self.__5g_ddnmf_info = _5g_ddnmf_info

    @property
    def mfaf_info(self):
        """Gets the mfaf_info of this NFProfile.


        :return: The mfaf_info of this NFProfile.
        :rtype: MfafInfo
        """
        return self._mfaf_info

    @mfaf_info.setter
    def mfaf_info(self, mfaf_info):
        """Sets the mfaf_info of this NFProfile.


        :param mfaf_info: The mfaf_info of this NFProfile.
        :type mfaf_info: MfafInfo
        """

        self._mfaf_info = mfaf_info

    @property
    def easdf_info_list(self):
        """Gets the easdf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of EasdfInfo   # noqa: E501

        :return: The easdf_info_list of this NFProfile.
        :rtype: Dict[str, EasdfInfo]
        """
        return self._easdf_info_list

    @easdf_info_list.setter
    def easdf_info_list(self, easdf_info_list):
        """Sets the easdf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of EasdfInfo   # noqa: E501

        :param easdf_info_list: The easdf_info_list of this NFProfile.
        :type easdf_info_list: Dict[str, EasdfInfo]
        """
        if easdf_info_list is not None and len(easdf_info_list) < 1:
            raise ValueError("Invalid value for `easdf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._easdf_info_list = easdf_info_list

    @property
    def dccf_info(self):
        """Gets the dccf_info of this NFProfile.


        :return: The dccf_info of this NFProfile.
        :rtype: DccfInfo
        """
        return self._dccf_info

    @dccf_info.setter
    def dccf_info(self, dccf_info):
        """Sets the dccf_info of this NFProfile.


        :param dccf_info: The dccf_info of this NFProfile.
        :type dccf_info: DccfInfo
        """

        self._dccf_info = dccf_info

    @property
    def nsacf_info_list(self):
        """Gets the nsacf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of NsacfInfo   # noqa: E501

        :return: The nsacf_info_list of this NFProfile.
        :rtype: Dict[str, NsacfInfo]
        """
        return self._nsacf_info_list

    @nsacf_info_list.setter
    def nsacf_info_list(self, nsacf_info_list):
        """Sets the nsacf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of NsacfInfo   # noqa: E501

        :param nsacf_info_list: The nsacf_info_list of this NFProfile.
        :type nsacf_info_list: Dict[str, NsacfInfo]
        """
        if nsacf_info_list is not None and len(nsacf_info_list) < 1:
            raise ValueError("Invalid value for `nsacf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._nsacf_info_list = nsacf_info_list

    @property
    def mb_smf_info_list(self):
        """Gets the mb_smf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of MbSmfInfo   # noqa: E501

        :return: The mb_smf_info_list of this NFProfile.
        :rtype: Dict[str, MbSmfInfo]
        """
        return self._mb_smf_info_list

    @mb_smf_info_list.setter
    def mb_smf_info_list(self, mb_smf_info_list):
        """Sets the mb_smf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of MbSmfInfo   # noqa: E501

        :param mb_smf_info_list: The mb_smf_info_list of this NFProfile.
        :type mb_smf_info_list: Dict[str, MbSmfInfo]
        """
        if mb_smf_info_list is not None and len(mb_smf_info_list) < 1:
            raise ValueError("Invalid value for `mb_smf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._mb_smf_info_list = mb_smf_info_list

    @property
    def tsctsf_info_list(self):
        """Gets the tsctsf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of TsctsfInfo   # noqa: E501

        :return: The tsctsf_info_list of this NFProfile.
        :rtype: Dict[str, TsctsfInfo]
        """
        return self._tsctsf_info_list

    @tsctsf_info_list.setter
    def tsctsf_info_list(self, tsctsf_info_list):
        """Sets the tsctsf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of TsctsfInfo   # noqa: E501

        :param tsctsf_info_list: The tsctsf_info_list of this NFProfile.
        :type tsctsf_info_list: Dict[str, TsctsfInfo]
        """
        if tsctsf_info_list is not None and len(tsctsf_info_list) < 1:
            raise ValueError("Invalid value for `tsctsf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._tsctsf_info_list = tsctsf_info_list

    @property
    def mb_upf_info_list(self):
        """Gets the mb_upf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of MbUpfInfo   # noqa: E501

        :return: The mb_upf_info_list of this NFProfile.
        :rtype: Dict[str, MbUpfInfo]
        """
        return self._mb_upf_info_list

    @mb_upf_info_list.setter
    def mb_upf_info_list(self, mb_upf_info_list):
        """Sets the mb_upf_info_list of this NFProfile.

        A map (list of key-value pairs) where a (unique) valid JSON string serves as key of MbUpfInfo   # noqa: E501

        :param mb_upf_info_list: The mb_upf_info_list of this NFProfile.
        :type mb_upf_info_list: Dict[str, MbUpfInfo]
        """
        if mb_upf_info_list is not None and len(mb_upf_info_list) < 1:
            raise ValueError("Invalid value for `mb_upf_info_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._mb_upf_info_list = mb_upf_info_list

    @property
    def trust_af_info(self):
        """Gets the trust_af_info of this NFProfile.


        :return: The trust_af_info of this NFProfile.
        :rtype: TrustAfInfo
        """
        return self._trust_af_info

    @trust_af_info.setter
    def trust_af_info(self, trust_af_info):
        """Sets the trust_af_info of this NFProfile.


        :param trust_af_info: The trust_af_info of this NFProfile.
        :type trust_af_info: TrustAfInfo
        """

        self._trust_af_info = trust_af_info

    @property
    def nssaaf_info(self):
        """Gets the nssaaf_info of this NFProfile.


        :return: The nssaaf_info of this NFProfile.
        :rtype: NssaafInfo
        """
        return self._nssaaf_info

    @nssaaf_info.setter
    def nssaaf_info(self, nssaaf_info):
        """Sets the nssaaf_info of this NFProfile.


        :param nssaaf_info: The nssaaf_info of this NFProfile.
        :type nssaaf_info: NssaafInfo
        """

        self._nssaaf_info = nssaaf_info

    @property
    def hni_list(self):
        """Gets the hni_list of this NFProfile.


        :return: The hni_list of this NFProfile.
        :rtype: List[str]
        """
        return self._hni_list

    @hni_list.setter
    def hni_list(self, hni_list):
        """Sets the hni_list of this NFProfile.


        :param hni_list: The hni_list of this NFProfile.
        :type hni_list: List[str]
        """
        if hni_list is not None and len(hni_list) < 1:
            raise ValueError("Invalid value for `hni_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._hni_list = hni_list

    @property
    def iwmsc_info(self):
        """Gets the iwmsc_info of this NFProfile.


        :return: The iwmsc_info of this NFProfile.
        :rtype: IwmscInfo
        """
        return self._iwmsc_info

    @iwmsc_info.setter
    def iwmsc_info(self, iwmsc_info):
        """Sets the iwmsc_info of this NFProfile.


        :param iwmsc_info: The iwmsc_info of this NFProfile.
        :type iwmsc_info: IwmscInfo
        """

        self._iwmsc_info = iwmsc_info

    @property
    def mnpf_info(self):
        """Gets the mnpf_info of this NFProfile.


        :return: The mnpf_info of this NFProfile.
        :rtype: MnpfInfo
        """
        return self._mnpf_info

    @mnpf_info.setter
    def mnpf_info(self, mnpf_info):
        """Sets the mnpf_info of this NFProfile.


        :param mnpf_info: The mnpf_info of this NFProfile.
        :type mnpf_info: MnpfInfo
        """

        self._mnpf_info = mnpf_info

    @property
    def smsf_info(self):
        """Gets the smsf_info of this NFProfile.


        :return: The smsf_info of this NFProfile.
        :rtype: SmsfInfo
        """
        return self._smsf_info

    @smsf_info.setter
    def smsf_info(self, smsf_info):
        """Sets the smsf_info of this NFProfile.


        :param smsf_info: The smsf_info of this NFProfile.
        :type smsf_info: SmsfInfo
        """

        self._smsf_info = smsf_info

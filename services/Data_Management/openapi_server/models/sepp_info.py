# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.n32_purpose import N32Purpose
from openapi_server.models.plmn_id import PlmnId
from openapi_server.models.plmn_id_nid import PlmnIdNid
from openapi_server import util

from openapi_server.models.n32_purpose import N32Purpose  # noqa: E501
from openapi_server.models.plmn_id import PlmnId  # noqa: E501
from openapi_server.models.plmn_id_nid import PlmnIdNid  # noqa: E501

class SeppInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sepp_prefix=None, sepp_ports=None, remote_plmn_list=None, remote_snpn_list=None, n32_purposes=None):  # noqa: E501
        """SeppInfo - a model defined in OpenAPI

        :param sepp_prefix: The sepp_prefix of this SeppInfo.  # noqa: E501
        :type sepp_prefix: str
        :param sepp_ports: The sepp_ports of this SeppInfo.  # noqa: E501
        :type sepp_ports: Dict[str, int]
        :param remote_plmn_list: The remote_plmn_list of this SeppInfo.  # noqa: E501
        :type remote_plmn_list: List[PlmnId]
        :param remote_snpn_list: The remote_snpn_list of this SeppInfo.  # noqa: E501
        :type remote_snpn_list: List[PlmnIdNid]
        :param n32_purposes: The n32_purposes of this SeppInfo.  # noqa: E501
        :type n32_purposes: List[N32Purpose]
        """
        self.openapi_types = {
            'sepp_prefix': str,
            'sepp_ports': Dict[str, int],
            'remote_plmn_list': List[PlmnId],
            'remote_snpn_list': List[PlmnIdNid],
            'n32_purposes': List[N32Purpose]
        }

        self.attribute_map = {
            'sepp_prefix': 'seppPrefix',
            'sepp_ports': 'seppPorts',
            'remote_plmn_list': 'remotePlmnList',
            'remote_snpn_list': 'remoteSnpnList',
            'n32_purposes': 'n32Purposes'
        }

        self._sepp_prefix = sepp_prefix
        self._sepp_ports = sepp_ports
        self._remote_plmn_list = remote_plmn_list
        self._remote_snpn_list = remote_snpn_list
        self._n32_purposes = n32_purposes

    @classmethod
    def from_dict(cls, dikt) -> 'SeppInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SeppInfo of this SeppInfo.  # noqa: E501
        :rtype: SeppInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sepp_prefix(self):
        """Gets the sepp_prefix of this SeppInfo.


        :return: The sepp_prefix of this SeppInfo.
        :rtype: str
        """
        return self._sepp_prefix

    @sepp_prefix.setter
    def sepp_prefix(self, sepp_prefix):
        """Sets the sepp_prefix of this SeppInfo.


        :param sepp_prefix: The sepp_prefix of this SeppInfo.
        :type sepp_prefix: str
        """

        self._sepp_prefix = sepp_prefix

    @property
    def sepp_ports(self):
        """Gets the sepp_ports of this SeppInfo.

        Port numbers for HTTP and HTTPS. The key of the map shall be \"http\" or \"https\".   # noqa: E501

        :return: The sepp_ports of this SeppInfo.
        :rtype: Dict[str, int]
        """
        return self._sepp_ports

    @sepp_ports.setter
    def sepp_ports(self, sepp_ports):
        """Sets the sepp_ports of this SeppInfo.

        Port numbers for HTTP and HTTPS. The key of the map shall be \"http\" or \"https\".   # noqa: E501

        :param sepp_ports: The sepp_ports of this SeppInfo.
        :type sepp_ports: Dict[str, int]
        """
        if sepp_ports is not None and len(sepp_ports) < 1:
            raise ValueError("Invalid value for `sepp_ports`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._sepp_ports = sepp_ports

    @property
    def remote_plmn_list(self):
        """Gets the remote_plmn_list of this SeppInfo.


        :return: The remote_plmn_list of this SeppInfo.
        :rtype: List[PlmnId]
        """
        return self._remote_plmn_list

    @remote_plmn_list.setter
    def remote_plmn_list(self, remote_plmn_list):
        """Sets the remote_plmn_list of this SeppInfo.


        :param remote_plmn_list: The remote_plmn_list of this SeppInfo.
        :type remote_plmn_list: List[PlmnId]
        """
        if remote_plmn_list is not None and len(remote_plmn_list) < 1:
            raise ValueError("Invalid value for `remote_plmn_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._remote_plmn_list = remote_plmn_list

    @property
    def remote_snpn_list(self):
        """Gets the remote_snpn_list of this SeppInfo.


        :return: The remote_snpn_list of this SeppInfo.
        :rtype: List[PlmnIdNid]
        """
        return self._remote_snpn_list

    @remote_snpn_list.setter
    def remote_snpn_list(self, remote_snpn_list):
        """Sets the remote_snpn_list of this SeppInfo.


        :param remote_snpn_list: The remote_snpn_list of this SeppInfo.
        :type remote_snpn_list: List[PlmnIdNid]
        """
        if remote_snpn_list is not None and len(remote_snpn_list) < 1:
            raise ValueError("Invalid value for `remote_snpn_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._remote_snpn_list = remote_snpn_list

    @property
    def n32_purposes(self):
        """Gets the n32_purposes of this SeppInfo.

        N32 purposes supported by the SEPP  # noqa: E501

        :return: The n32_purposes of this SeppInfo.
        :rtype: List[N32Purpose]
        """
        return self._n32_purposes

    @n32_purposes.setter
    def n32_purposes(self, n32_purposes):
        """Sets the n32_purposes of this SeppInfo.

        N32 purposes supported by the SEPP  # noqa: E501

        :param n32_purposes: The n32_purposes of this SeppInfo.
        :type n32_purposes: List[N32Purpose]
        """
        if n32_purposes is not None and len(n32_purposes) < 1:
            raise ValueError("Invalid value for `n32_purposes`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._n32_purposes = n32_purposes

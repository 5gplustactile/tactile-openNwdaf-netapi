# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ue_trajectory_info import UeTrajectoryInfo
import re
from openapi_server import util

from openapi_server.models.ue_trajectory_info import UeTrajectoryInfo  # noqa: E501
import re  # noqa: E501

class UeMobilityInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, supi=None, app_id=None, ue_trajs=None):  # noqa: E501
        """UeMobilityInfo - a model defined in OpenAPI

        :param supi: The supi of this UeMobilityInfo.  # noqa: E501
        :type supi: str
        :param app_id: The app_id of this UeMobilityInfo.  # noqa: E501
        :type app_id: str
        :param ue_trajs: The ue_trajs of this UeMobilityInfo.  # noqa: E501
        :type ue_trajs: List[UeTrajectoryInfo]
        """
        self.openapi_types = {
            'supi': str,
            'app_id': str,
            'ue_trajs': List[UeTrajectoryInfo]
        }

        self.attribute_map = {
            'supi': 'supi',
            'app_id': 'appId',
            'ue_trajs': 'ueTrajs'
        }

        self._supi = supi
        self._app_id = app_id
        self._ue_trajs = ue_trajs

    @classmethod
    def from_dict(cls, dikt) -> 'UeMobilityInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UeMobilityInfo of this UeMobilityInfo.  # noqa: E501
        :rtype: UeMobilityInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def supi(self):
        """Gets the supi of this UeMobilityInfo.

        String identifying a Supi that shall contain either an IMSI, a network specific identifier, a Global Cable Identifier (GCI) or a Global Line Identifier (GLI) as specified in clause  2.2A of 3GPP TS 23.003. It shall be formatted as follows  - for an IMSI \"imsi-<imsi>\", where <imsi> shall be formatted according to clause 2.2    of 3GPP TS 23.003 that describes an IMSI.  - for a network specific identifier \"nai-<nai>, where <nai> shall be formatted    according to clause 28.7.2 of 3GPP TS 23.003 that describes an NAI.  - for a GCI \"gci-<gci>\", where <gci> shall be formatted according to clause 28.15.2    of 3GPP TS 23.003.  - for a GLI \"gli-<gli>\", where <gli> shall be formatted according to clause 28.16.2 of    3GPP TS 23.003.To enable that the value is used as part of an URI, the string shall    only contain characters allowed according to the \"lower-with-hyphen\" naming convention    defined in 3GPP TS 29.501.   # noqa: E501

        :return: The supi of this UeMobilityInfo.
        :rtype: str
        """
        return self._supi

    @supi.setter
    def supi(self, supi):
        """Sets the supi of this UeMobilityInfo.

        String identifying a Supi that shall contain either an IMSI, a network specific identifier, a Global Cable Identifier (GCI) or a Global Line Identifier (GLI) as specified in clause  2.2A of 3GPP TS 23.003. It shall be formatted as follows  - for an IMSI \"imsi-<imsi>\", where <imsi> shall be formatted according to clause 2.2    of 3GPP TS 23.003 that describes an IMSI.  - for a network specific identifier \"nai-<nai>, where <nai> shall be formatted    according to clause 28.7.2 of 3GPP TS 23.003 that describes an NAI.  - for a GCI \"gci-<gci>\", where <gci> shall be formatted according to clause 28.15.2    of 3GPP TS 23.003.  - for a GLI \"gli-<gli>\", where <gli> shall be formatted according to clause 28.16.2 of    3GPP TS 23.003.To enable that the value is used as part of an URI, the string shall    only contain characters allowed according to the \"lower-with-hyphen\" naming convention    defined in 3GPP TS 29.501.   # noqa: E501

        :param supi: The supi of this UeMobilityInfo.
        :type supi: str
        """
        if supi is None:
            raise ValueError("Invalid value for `supi`, must not be `None`")  # noqa: E501
        if supi is not None and not re.search(r'^(imsi-[0-9]{5,15}|nai-.+|gci-.+|gli-.+|.+)$', supi):  # noqa: E501
            raise ValueError("Invalid value for `supi`, must be a follow pattern or equal to `/^(imsi-[0-9]{5,15}|nai-.+|gci-.+|gli-.+|.+)$/`")  # noqa: E501

        self._supi = supi

    @property
    def app_id(self):
        """Gets the app_id of this UeMobilityInfo.

        String providing an application identifier.  # noqa: E501

        :return: The app_id of this UeMobilityInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this UeMobilityInfo.

        String providing an application identifier.  # noqa: E501

        :param app_id: The app_id of this UeMobilityInfo.
        :type app_id: str
        """

        self._app_id = app_id

    @property
    def ue_trajs(self):
        """Gets the ue_trajs of this UeMobilityInfo.


        :return: The ue_trajs of this UeMobilityInfo.
        :rtype: List[UeTrajectoryInfo]
        """
        return self._ue_trajs

    @ue_trajs.setter
    def ue_trajs(self, ue_trajs):
        """Sets the ue_trajs of this UeMobilityInfo.


        :param ue_trajs: The ue_trajs of this UeMobilityInfo.
        :type ue_trajs: List[UeTrajectoryInfo]
        """
        if ue_trajs is None:
            raise ValueError("Invalid value for `ue_trajs`, must not be `None`")  # noqa: E501
        if ue_trajs is not None and len(ue_trajs) < 1:
            raise ValueError("Invalid value for `ue_trajs`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ue_trajs = ue_trajs
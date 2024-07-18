# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class UEIdExt(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, supi=None, gpsi=None):  # noqa: E501
        """UEIdExt - a model defined in OpenAPI

        :param supi: The supi of this UEIdExt.  # noqa: E501
        :type supi: str
        :param gpsi: The gpsi of this UEIdExt.  # noqa: E501
        :type gpsi: str
        """
        self.openapi_types = {
            'supi': str,
            'gpsi': str
        }

        self.attribute_map = {
            'supi': 'supi',
            'gpsi': 'gpsi'
        }

        self._supi = supi
        self._gpsi = gpsi

    @classmethod
    def from_dict(cls, dikt) -> 'UEIdExt':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UEIdExt of this UEIdExt.  # noqa: E501
        :rtype: UEIdExt
        """
        return util.deserialize_model(dikt, cls)

    @property
    def supi(self):
        """Gets the supi of this UEIdExt.

        String identifying a Supi that shall contain either an IMSI, a network specific identifier, a Global Cable Identifier (GCI) or a Global Line Identifier (GLI) as specified in clause  2.2A of 3GPP TS 23.003. It shall be formatted as follows  - for an IMSI \"imsi-<imsi>\", where <imsi> shall be formatted according to clause 2.2    of 3GPP TS 23.003 that describes an IMSI.  - for a network specific identifier \"nai-<nai>, where <nai> shall be formatted    according to clause 28.7.2 of 3GPP TS 23.003 that describes an NAI.  - for a GCI \"gci-<gci>\", where <gci> shall be formatted according to clause 28.15.2    of 3GPP TS 23.003.  - for a GLI \"gli-<gli>\", where <gli> shall be formatted according to clause 28.16.2 of    3GPP TS 23.003.To enable that the value is used as part of an URI, the string shall    only contain characters allowed according to the \"lower-with-hyphen\" naming convention    defined in 3GPP TS 29.501.   # noqa: E501

        :return: The supi of this UEIdExt.
        :rtype: str
        """
        return self._supi

    @supi.setter
    def supi(self, supi):
        """Sets the supi of this UEIdExt.

        String identifying a Supi that shall contain either an IMSI, a network specific identifier, a Global Cable Identifier (GCI) or a Global Line Identifier (GLI) as specified in clause  2.2A of 3GPP TS 23.003. It shall be formatted as follows  - for an IMSI \"imsi-<imsi>\", where <imsi> shall be formatted according to clause 2.2    of 3GPP TS 23.003 that describes an IMSI.  - for a network specific identifier \"nai-<nai>, where <nai> shall be formatted    according to clause 28.7.2 of 3GPP TS 23.003 that describes an NAI.  - for a GCI \"gci-<gci>\", where <gci> shall be formatted according to clause 28.15.2    of 3GPP TS 23.003.  - for a GLI \"gli-<gli>\", where <gli> shall be formatted according to clause 28.16.2 of    3GPP TS 23.003.To enable that the value is used as part of an URI, the string shall    only contain characters allowed according to the \"lower-with-hyphen\" naming convention    defined in 3GPP TS 29.501.   # noqa: E501

        :param supi: The supi of this UEIdExt.
        :type supi: str
        """
        if supi is not None and not re.search(r'^(imsi-[0-9]{5,15}|nai-.+|gci-.+|gli-.+|.+)$', supi):  # noqa: E501
            raise ValueError("Invalid value for `supi`, must be a follow pattern or equal to `/^(imsi-[0-9]{5,15}|nai-.+|gci-.+|gli-.+|.+)$/`")  # noqa: E501

        self._supi = supi

    @property
    def gpsi(self):
        """Gets the gpsi of this UEIdExt.

        String identifying a Gpsi shall contain either an External Id or an MSISDN.  It shall be formatted as follows -External Identifier= \"extid-'extid', where 'extid'  shall be formatted according to clause 19.7.2 of 3GPP TS 23.003 that describes an  External Identifier.    # noqa: E501

        :return: The gpsi of this UEIdExt.
        :rtype: str
        """
        return self._gpsi

    @gpsi.setter
    def gpsi(self, gpsi):
        """Sets the gpsi of this UEIdExt.

        String identifying a Gpsi shall contain either an External Id or an MSISDN.  It shall be formatted as follows -External Identifier= \"extid-'extid', where 'extid'  shall be formatted according to clause 19.7.2 of 3GPP TS 23.003 that describes an  External Identifier.    # noqa: E501

        :param gpsi: The gpsi of this UEIdExt.
        :type gpsi: str
        """
        if gpsi is not None and not re.search(r'^(msisdn-[0-9]{5,15}|extid-[^@]+@[^@]+|.+)$', gpsi):  # noqa: E501
            raise ValueError("Invalid value for `gpsi`, must be a follow pattern or equal to `/^(msisdn-[0-9]{5,15}|extid-[^@]+@[^@]+|.+)$/`")  # noqa: E501

        self._gpsi = gpsi

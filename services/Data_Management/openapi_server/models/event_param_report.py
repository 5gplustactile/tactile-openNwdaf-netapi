# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.network_area_info import NetworkAreaInfo
from openapi_server.models.number_average import NumberAverage
import re
from openapi_server import util

from openapi_server.models.network_area_info import NetworkAreaInfo  # noqa: E501
from openapi_server.models.number_average import NumberAverage  # noqa: E501
import re  # noqa: E501

class EventParamReport(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, values=None, supi=None, area=None, spacing=None, duration=None, avg_and_var=None, most_freq_val=None, least_freq_val=None, count=None, min_value=None, max_value=None):  # noqa: E501
        """EventParamReport - a model defined in OpenAPI

        :param name: The name of this EventParamReport.  # noqa: E501
        :type name: str
        :param values: The values of this EventParamReport.  # noqa: E501
        :type values: List[object]
        :param supi: The supi of this EventParamReport.  # noqa: E501
        :type supi: str
        :param area: The area of this EventParamReport.  # noqa: E501
        :type area: NetworkAreaInfo
        :param spacing: The spacing of this EventParamReport.  # noqa: E501
        :type spacing: NumberAverage
        :param duration: The duration of this EventParamReport.  # noqa: E501
        :type duration: NumberAverage
        :param avg_and_var: The avg_and_var of this EventParamReport.  # noqa: E501
        :type avg_and_var: NumberAverage
        :param most_freq_val: The most_freq_val of this EventParamReport.  # noqa: E501
        :type most_freq_val: object
        :param least_freq_val: The least_freq_val of this EventParamReport.  # noqa: E501
        :type least_freq_val: object
        :param count: The count of this EventParamReport.  # noqa: E501
        :type count: int
        :param min_value: The min_value of this EventParamReport.  # noqa: E501
        :type min_value: str
        :param max_value: The max_value of this EventParamReport.  # noqa: E501
        :type max_value: str
        """
        self.openapi_types = {
            'name': str,
            'values': List[object],
            'supi': str,
            'area': NetworkAreaInfo,
            'spacing': NumberAverage,
            'duration': NumberAverage,
            'avg_and_var': NumberAverage,
            'most_freq_val': object,
            'least_freq_val': object,
            'count': int,
            'min_value': str,
            'max_value': str
        }

        self.attribute_map = {
            'name': 'name',
            'values': 'values',
            'supi': 'supi',
            'area': 'area',
            'spacing': 'spacing',
            'duration': 'duration',
            'avg_and_var': 'avgAndVar',
            'most_freq_val': 'mostFreqVal',
            'least_freq_val': 'leastFreqVal',
            'count': 'count',
            'min_value': 'minValue',
            'max_value': 'maxValue'
        }

        self._name = name
        self._values = values
        self._supi = supi
        self._area = area
        self._spacing = spacing
        self._duration = duration
        self._avg_and_var = avg_and_var
        self._most_freq_val = most_freq_val
        self._least_freq_val = least_freq_val
        self._count = count
        self._min_value = min_value
        self._max_value = max_value

    @classmethod
    def from_dict(cls, dikt) -> 'EventParamReport':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EventParamReport of this EventParamReport.  # noqa: E501
        :rtype: EventParamReport
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this EventParamReport.

        The name of the reported parameter.  # noqa: E501

        :return: The name of this EventParamReport.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventParamReport.

        The name of the reported parameter.  # noqa: E501

        :param name: The name of this EventParamReport.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def values(self):
        """Gets the values of this EventParamReport.

        The list of values of the reported parameter.  # noqa: E501

        :return: The values of this EventParamReport.
        :rtype: List[object]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this EventParamReport.

        The list of values of the reported parameter.  # noqa: E501

        :param values: The values of this EventParamReport.
        :type values: List[object]
        """
        if values is None:
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501
        if values is not None and len(values) < 1:
            raise ValueError("Invalid value for `values`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._values = values

    @property
    def supi(self):
        """Gets the supi of this EventParamReport.

        String identifying a Supi that shall contain either an IMSI, a network specific identifier, a Global Cable Identifier (GCI) or a Global Line Identifier (GLI) as specified in clause  2.2A of 3GPP TS 23.003. It shall be formatted as follows  - for an IMSI \"imsi-<imsi>\", where <imsi> shall be formatted according to clause 2.2    of 3GPP TS 23.003 that describes an IMSI.  - for a network specific identifier \"nai-<nai>, where <nai> shall be formatted    according to clause 28.7.2 of 3GPP TS 23.003 that describes an NAI.  - for a GCI \"gci-<gci>\", where <gci> shall be formatted according to clause 28.15.2    of 3GPP TS 23.003.  - for a GLI \"gli-<gli>\", where <gli> shall be formatted according to clause 28.16.2 of    3GPP TS 23.003.To enable that the value is used as part of an URI, the string shall    only contain characters allowed according to the \"lower-with-hyphen\" naming convention    defined in 3GPP TS 29.501.   # noqa: E501

        :return: The supi of this EventParamReport.
        :rtype: str
        """
        return self._supi

    @supi.setter
    def supi(self, supi):
        """Sets the supi of this EventParamReport.

        String identifying a Supi that shall contain either an IMSI, a network specific identifier, a Global Cable Identifier (GCI) or a Global Line Identifier (GLI) as specified in clause  2.2A of 3GPP TS 23.003. It shall be formatted as follows  - for an IMSI \"imsi-<imsi>\", where <imsi> shall be formatted according to clause 2.2    of 3GPP TS 23.003 that describes an IMSI.  - for a network specific identifier \"nai-<nai>, where <nai> shall be formatted    according to clause 28.7.2 of 3GPP TS 23.003 that describes an NAI.  - for a GCI \"gci-<gci>\", where <gci> shall be formatted according to clause 28.15.2    of 3GPP TS 23.003.  - for a GLI \"gli-<gli>\", where <gli> shall be formatted according to clause 28.16.2 of    3GPP TS 23.003.To enable that the value is used as part of an URI, the string shall    only contain characters allowed according to the \"lower-with-hyphen\" naming convention    defined in 3GPP TS 29.501.   # noqa: E501

        :param supi: The supi of this EventParamReport.
        :type supi: str
        """
        if supi is not None and not re.search(r'^(imsi-[0-9]{5,15}|nai-.+|gci-.+|gli-.+|.+)$', supi):  # noqa: E501
            raise ValueError("Invalid value for `supi`, must be a follow pattern or equal to `/^(imsi-[0-9]{5,15}|nai-.+|gci-.+|gli-.+|.+)$/`")  # noqa: E501

        self._supi = supi

    @property
    def area(self):
        """Gets the area of this EventParamReport.


        :return: The area of this EventParamReport.
        :rtype: NetworkAreaInfo
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this EventParamReport.


        :param area: The area of this EventParamReport.
        :type area: NetworkAreaInfo
        """

        self._area = area

    @property
    def spacing(self):
        """Gets the spacing of this EventParamReport.


        :return: The spacing of this EventParamReport.
        :rtype: NumberAverage
        """
        return self._spacing

    @spacing.setter
    def spacing(self, spacing):
        """Sets the spacing of this EventParamReport.


        :param spacing: The spacing of this EventParamReport.
        :type spacing: NumberAverage
        """

        self._spacing = spacing

    @property
    def duration(self):
        """Gets the duration of this EventParamReport.


        :return: The duration of this EventParamReport.
        :rtype: NumberAverage
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this EventParamReport.


        :param duration: The duration of this EventParamReport.
        :type duration: NumberAverage
        """

        self._duration = duration

    @property
    def avg_and_var(self):
        """Gets the avg_and_var of this EventParamReport.


        :return: The avg_and_var of this EventParamReport.
        :rtype: NumberAverage
        """
        return self._avg_and_var

    @avg_and_var.setter
    def avg_and_var(self, avg_and_var):
        """Sets the avg_and_var of this EventParamReport.


        :param avg_and_var: The avg_and_var of this EventParamReport.
        :type avg_and_var: NumberAverage
        """

        self._avg_and_var = avg_and_var

    @property
    def most_freq_val(self):
        """Gets the most_freq_val of this EventParamReport.


        :return: The most_freq_val of this EventParamReport.
        :rtype: object
        """
        return self._most_freq_val

    @most_freq_val.setter
    def most_freq_val(self, most_freq_val):
        """Sets the most_freq_val of this EventParamReport.


        :param most_freq_val: The most_freq_val of this EventParamReport.
        :type most_freq_val: object
        """

        self._most_freq_val = most_freq_val

    @property
    def least_freq_val(self):
        """Gets the least_freq_val of this EventParamReport.


        :return: The least_freq_val of this EventParamReport.
        :rtype: object
        """
        return self._least_freq_val

    @least_freq_val.setter
    def least_freq_val(self, least_freq_val):
        """Sets the least_freq_val of this EventParamReport.


        :param least_freq_val: The least_freq_val of this EventParamReport.
        :type least_freq_val: object
        """

        self._least_freq_val = least_freq_val

    @property
    def count(self):
        """Gets the count of this EventParamReport.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :return: The count of this EventParamReport.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this EventParamReport.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :param count: The count of this EventParamReport.
        :type count: int
        """
        if count is not None and count < 0:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._count = count

    @property
    def min_value(self):
        """Gets the min_value of this EventParamReport.

        The minimum value of the parameter.  # noqa: E501

        :return: The min_value of this EventParamReport.
        :rtype: str
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this EventParamReport.

        The minimum value of the parameter.  # noqa: E501

        :param min_value: The min_value of this EventParamReport.
        :type min_value: str
        """

        self._min_value = min_value

    @property
    def max_value(self):
        """Gets the max_value of this EventParamReport.

        The maximum value of the parameter.  # noqa: E501

        :return: The max_value of this EventParamReport.
        :rtype: str
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this EventParamReport.

        The maximum value of the parameter.  # noqa: E501

        :param max_value: The max_value of this EventParamReport.
        :type max_value: str
        """

        self._max_value = max_value

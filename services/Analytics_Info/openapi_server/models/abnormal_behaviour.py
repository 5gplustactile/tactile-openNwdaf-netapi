# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.additional_measurement import AdditionalMeasurement
from openapi_server.models.exception import Exception
from openapi_server.models.snssai import Snssai
from openapi_server import util

from openapi_server.models.additional_measurement import AdditionalMeasurement  # noqa: E501
from openapi_server.models.exception import Exception  # noqa: E501
from openapi_server.models.snssai import Snssai  # noqa: E501

class AbnormalBehaviour(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, supis=None, excep=None, dnn=None, snssai=None, ratio=None, confidence=None, addt_meas_info=None):  # noqa: E501
        """AbnormalBehaviour - a model defined in OpenAPI

        :param supis: The supis of this AbnormalBehaviour.  # noqa: E501
        :type supis: List[str]
        :param excep: The excep of this AbnormalBehaviour.  # noqa: E501
        :type excep: Exception
        :param dnn: The dnn of this AbnormalBehaviour.  # noqa: E501
        :type dnn: str
        :param snssai: The snssai of this AbnormalBehaviour.  # noqa: E501
        :type snssai: Snssai
        :param ratio: The ratio of this AbnormalBehaviour.  # noqa: E501
        :type ratio: int
        :param confidence: The confidence of this AbnormalBehaviour.  # noqa: E501
        :type confidence: int
        :param addt_meas_info: The addt_meas_info of this AbnormalBehaviour.  # noqa: E501
        :type addt_meas_info: AdditionalMeasurement
        """
        self.openapi_types = {
            'supis': List[str],
            'excep': Exception,
            'dnn': str,
            'snssai': Snssai,
            'ratio': int,
            'confidence': int,
            'addt_meas_info': AdditionalMeasurement
        }

        self.attribute_map = {
            'supis': 'supis',
            'excep': 'excep',
            'dnn': 'dnn',
            'snssai': 'snssai',
            'ratio': 'ratio',
            'confidence': 'confidence',
            'addt_meas_info': 'addtMeasInfo'
        }

        self._supis = supis
        self._excep = excep
        self._dnn = dnn
        self._snssai = snssai
        self._ratio = ratio
        self._confidence = confidence
        self._addt_meas_info = addt_meas_info

    @classmethod
    def from_dict(cls, dikt) -> 'AbnormalBehaviour':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AbnormalBehaviour of this AbnormalBehaviour.  # noqa: E501
        :rtype: AbnormalBehaviour
        """
        return util.deserialize_model(dikt, cls)

    @property
    def supis(self):
        """Gets the supis of this AbnormalBehaviour.


        :return: The supis of this AbnormalBehaviour.
        :rtype: List[str]
        """
        return self._supis

    @supis.setter
    def supis(self, supis):
        """Sets the supis of this AbnormalBehaviour.


        :param supis: The supis of this AbnormalBehaviour.
        :type supis: List[str]
        """
        if supis is not None and len(supis) < 1:
            raise ValueError("Invalid value for `supis`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._supis = supis

    @property
    def excep(self):
        """Gets the excep of this AbnormalBehaviour.


        :return: The excep of this AbnormalBehaviour.
        :rtype: Exception
        """
        return self._excep

    @excep.setter
    def excep(self, excep):
        """Sets the excep of this AbnormalBehaviour.


        :param excep: The excep of this AbnormalBehaviour.
        :type excep: Exception
        """
        if excep is None:
            raise ValueError("Invalid value for `excep`, must not be `None`")  # noqa: E501

        self._excep = excep

    @property
    def dnn(self):
        """Gets the dnn of this AbnormalBehaviour.

        String representing a Data Network as defined in clause 9A of 3GPP TS 23.003;  it shall contain either a DNN Network Identifier, or a full DNN with both the Network  Identifier and Operator Identifier, as specified in 3GPP TS 23.003 clause 9.1.1 and 9.1.2. It shall be coded as string in which the labels are separated by dots  (e.g. \"Label1.Label2.Label3\").   # noqa: E501

        :return: The dnn of this AbnormalBehaviour.
        :rtype: str
        """
        return self._dnn

    @dnn.setter
    def dnn(self, dnn):
        """Sets the dnn of this AbnormalBehaviour.

        String representing a Data Network as defined in clause 9A of 3GPP TS 23.003;  it shall contain either a DNN Network Identifier, or a full DNN with both the Network  Identifier and Operator Identifier, as specified in 3GPP TS 23.003 clause 9.1.1 and 9.1.2. It shall be coded as string in which the labels are separated by dots  (e.g. \"Label1.Label2.Label3\").   # noqa: E501

        :param dnn: The dnn of this AbnormalBehaviour.
        :type dnn: str
        """

        self._dnn = dnn

    @property
    def snssai(self):
        """Gets the snssai of this AbnormalBehaviour.


        :return: The snssai of this AbnormalBehaviour.
        :rtype: Snssai
        """
        return self._snssai

    @snssai.setter
    def snssai(self, snssai):
        """Sets the snssai of this AbnormalBehaviour.


        :param snssai: The snssai of this AbnormalBehaviour.
        :type snssai: Snssai
        """

        self._snssai = snssai

    @property
    def ratio(self):
        """Gets the ratio of this AbnormalBehaviour.

        Unsigned integer indicating Sampling Ratio (see clauses 4.15.1 of 3GPP TS 23.502), expressed in percent.    # noqa: E501

        :return: The ratio of this AbnormalBehaviour.
        :rtype: int
        """
        return self._ratio

    @ratio.setter
    def ratio(self, ratio):
        """Sets the ratio of this AbnormalBehaviour.

        Unsigned integer indicating Sampling Ratio (see clauses 4.15.1 of 3GPP TS 23.502), expressed in percent.    # noqa: E501

        :param ratio: The ratio of this AbnormalBehaviour.
        :type ratio: int
        """
        if ratio is not None and ratio > 100:  # noqa: E501
            raise ValueError("Invalid value for `ratio`, must be a value less than or equal to `100`")  # noqa: E501
        if ratio is not None and ratio < 1:  # noqa: E501
            raise ValueError("Invalid value for `ratio`, must be a value greater than or equal to `1`")  # noqa: E501

        self._ratio = ratio

    @property
    def confidence(self):
        """Gets the confidence of this AbnormalBehaviour.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :return: The confidence of this AbnormalBehaviour.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this AbnormalBehaviour.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :param confidence: The confidence of this AbnormalBehaviour.
        :type confidence: int
        """
        if confidence is not None and confidence < 0:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value greater than or equal to `0`")  # noqa: E501

        self._confidence = confidence

    @property
    def addt_meas_info(self):
        """Gets the addt_meas_info of this AbnormalBehaviour.


        :return: The addt_meas_info of this AbnormalBehaviour.
        :rtype: AdditionalMeasurement
        """
        return self._addt_meas_info

    @addt_meas_info.setter
    def addt_meas_info(self, addt_meas_info):
        """Sets the addt_meas_info of this AbnormalBehaviour.


        :param addt_meas_info: The addt_meas_info of this AbnormalBehaviour.
        :type addt_meas_info: AdditionalMeasurement
        """

        self._addt_meas_info = addt_meas_info

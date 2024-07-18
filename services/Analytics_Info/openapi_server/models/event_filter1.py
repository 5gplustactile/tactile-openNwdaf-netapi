# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.collective_behaviour_filter import CollectiveBehaviourFilter
from openapi_server.models.location_area5_g import LocationArea5G
from openapi_server import util

from openapi_server.models.collective_behaviour_filter import CollectiveBehaviourFilter  # noqa: E501
from openapi_server.models.location_area5_g import LocationArea5G  # noqa: E501

class EventFilter1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, gpsis=None, supis=None, exter_group_ids=None, inter_group_ids=None, any_ue_ind=None, app_ids=None, loc_area=None, coll_attrs=None):  # noqa: E501
        """EventFilter1 - a model defined in OpenAPI

        :param gpsis: The gpsis of this EventFilter1.  # noqa: E501
        :type gpsis: List[str]
        :param supis: The supis of this EventFilter1.  # noqa: E501
        :type supis: List[str]
        :param exter_group_ids: The exter_group_ids of this EventFilter1.  # noqa: E501
        :type exter_group_ids: List[str]
        :param inter_group_ids: The inter_group_ids of this EventFilter1.  # noqa: E501
        :type inter_group_ids: List[str]
        :param any_ue_ind: The any_ue_ind of this EventFilter1.  # noqa: E501
        :type any_ue_ind: bool
        :param app_ids: The app_ids of this EventFilter1.  # noqa: E501
        :type app_ids: List[str]
        :param loc_area: The loc_area of this EventFilter1.  # noqa: E501
        :type loc_area: LocationArea5G
        :param coll_attrs: The coll_attrs of this EventFilter1.  # noqa: E501
        :type coll_attrs: List[CollectiveBehaviourFilter]
        """
        self.openapi_types = {
            'gpsis': List[str],
            'supis': List[str],
            'exter_group_ids': List[str],
            'inter_group_ids': List[str],
            'any_ue_ind': bool,
            'app_ids': List[str],
            'loc_area': LocationArea5G,
            'coll_attrs': List[CollectiveBehaviourFilter]
        }

        self.attribute_map = {
            'gpsis': 'gpsis',
            'supis': 'supis',
            'exter_group_ids': 'exterGroupIds',
            'inter_group_ids': 'interGroupIds',
            'any_ue_ind': 'anyUeInd',
            'app_ids': 'appIds',
            'loc_area': 'locArea',
            'coll_attrs': 'collAttrs'
        }

        self._gpsis = gpsis
        self._supis = supis
        self._exter_group_ids = exter_group_ids
        self._inter_group_ids = inter_group_ids
        self._any_ue_ind = any_ue_ind
        self._app_ids = app_ids
        self._loc_area = loc_area
        self._coll_attrs = coll_attrs

    @classmethod
    def from_dict(cls, dikt) -> 'EventFilter1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EventFilter_1 of this EventFilter1.  # noqa: E501
        :rtype: EventFilter1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def gpsis(self):
        """Gets the gpsis of this EventFilter1.


        :return: The gpsis of this EventFilter1.
        :rtype: List[str]
        """
        return self._gpsis

    @gpsis.setter
    def gpsis(self, gpsis):
        """Sets the gpsis of this EventFilter1.


        :param gpsis: The gpsis of this EventFilter1.
        :type gpsis: List[str]
        """
        if gpsis is not None and len(gpsis) < 1:
            raise ValueError("Invalid value for `gpsis`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._gpsis = gpsis

    @property
    def supis(self):
        """Gets the supis of this EventFilter1.


        :return: The supis of this EventFilter1.
        :rtype: List[str]
        """
        return self._supis

    @supis.setter
    def supis(self, supis):
        """Sets the supis of this EventFilter1.


        :param supis: The supis of this EventFilter1.
        :type supis: List[str]
        """
        if supis is not None and len(supis) < 1:
            raise ValueError("Invalid value for `supis`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._supis = supis

    @property
    def exter_group_ids(self):
        """Gets the exter_group_ids of this EventFilter1.


        :return: The exter_group_ids of this EventFilter1.
        :rtype: List[str]
        """
        return self._exter_group_ids

    @exter_group_ids.setter
    def exter_group_ids(self, exter_group_ids):
        """Sets the exter_group_ids of this EventFilter1.


        :param exter_group_ids: The exter_group_ids of this EventFilter1.
        :type exter_group_ids: List[str]
        """
        if exter_group_ids is not None and len(exter_group_ids) < 1:
            raise ValueError("Invalid value for `exter_group_ids`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._exter_group_ids = exter_group_ids

    @property
    def inter_group_ids(self):
        """Gets the inter_group_ids of this EventFilter1.


        :return: The inter_group_ids of this EventFilter1.
        :rtype: List[str]
        """
        return self._inter_group_ids

    @inter_group_ids.setter
    def inter_group_ids(self, inter_group_ids):
        """Sets the inter_group_ids of this EventFilter1.


        :param inter_group_ids: The inter_group_ids of this EventFilter1.
        :type inter_group_ids: List[str]
        """

        self._inter_group_ids = inter_group_ids

    @property
    def any_ue_ind(self):
        """Gets the any_ue_ind of this EventFilter1.


        :return: The any_ue_ind of this EventFilter1.
        :rtype: bool
        """
        return self._any_ue_ind

    @any_ue_ind.setter
    def any_ue_ind(self, any_ue_ind):
        """Sets the any_ue_ind of this EventFilter1.


        :param any_ue_ind: The any_ue_ind of this EventFilter1.
        :type any_ue_ind: bool
        """

        self._any_ue_ind = any_ue_ind

    @property
    def app_ids(self):
        """Gets the app_ids of this EventFilter1.


        :return: The app_ids of this EventFilter1.
        :rtype: List[str]
        """
        return self._app_ids

    @app_ids.setter
    def app_ids(self, app_ids):
        """Sets the app_ids of this EventFilter1.


        :param app_ids: The app_ids of this EventFilter1.
        :type app_ids: List[str]
        """
        if app_ids is not None and len(app_ids) < 1:
            raise ValueError("Invalid value for `app_ids`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._app_ids = app_ids

    @property
    def loc_area(self):
        """Gets the loc_area of this EventFilter1.


        :return: The loc_area of this EventFilter1.
        :rtype: LocationArea5G
        """
        return self._loc_area

    @loc_area.setter
    def loc_area(self, loc_area):
        """Sets the loc_area of this EventFilter1.


        :param loc_area: The loc_area of this EventFilter1.
        :type loc_area: LocationArea5G
        """

        self._loc_area = loc_area

    @property
    def coll_attrs(self):
        """Gets the coll_attrs of this EventFilter1.


        :return: The coll_attrs of this EventFilter1.
        :rtype: List[CollectiveBehaviourFilter]
        """
        return self._coll_attrs

    @coll_attrs.setter
    def coll_attrs(self, coll_attrs):
        """Sets the coll_attrs of this EventFilter1.


        :param coll_attrs: The coll_attrs of this EventFilter1.
        :type coll_attrs: List[CollectiveBehaviourFilter]
        """
        if coll_attrs is not None and len(coll_attrs) < 1:
            raise ValueError("Invalid value for `coll_attrs`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._coll_attrs = coll_attrs

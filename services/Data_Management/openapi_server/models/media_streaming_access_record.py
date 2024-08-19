# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.cache_status import CacheStatus
from openapi_server.models.endpoint_address import EndpointAddress
from openapi_server.models.media_streaming_access_record_all_of_connection_metrics import MediaStreamingAccessRecordAllOfConnectionMetrics
from openapi_server.models.media_streaming_access_record_all_of_request_message import MediaStreamingAccessRecordAllOfRequestMessage
from openapi_server.models.media_streaming_access_record_all_of_response_message import MediaStreamingAccessRecordAllOfResponseMessage
from openapi_server import util

from openapi_server.models.cache_status import CacheStatus  # noqa: E501
from openapi_server.models.endpoint_address import EndpointAddress  # noqa: E501
from openapi_server.models.media_streaming_access_record_all_of_connection_metrics import MediaStreamingAccessRecordAllOfConnectionMetrics  # noqa: E501
from openapi_server.models.media_streaming_access_record_all_of_request_message import MediaStreamingAccessRecordAllOfRequestMessage  # noqa: E501
from openapi_server.models.media_streaming_access_record_all_of_response_message import MediaStreamingAccessRecordAllOfResponseMessage  # noqa: E501

class MediaStreamingAccessRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, timestamp=None, media_stream_handler_endpoint_address=None, application_server_endpoint_address=None, session_identifier=None, request_message=None, cache_status=None, response_message=None, processing_latency=None, connection_metrics=None):  # noqa: E501
        """MediaStreamingAccessRecord - a model defined in OpenAPI

        :param timestamp: The timestamp of this MediaStreamingAccessRecord.  # noqa: E501
        :type timestamp: datetime
        :param media_stream_handler_endpoint_address: The media_stream_handler_endpoint_address of this MediaStreamingAccessRecord.  # noqa: E501
        :type media_stream_handler_endpoint_address: EndpointAddress
        :param application_server_endpoint_address: The application_server_endpoint_address of this MediaStreamingAccessRecord.  # noqa: E501
        :type application_server_endpoint_address: EndpointAddress
        :param session_identifier: The session_identifier of this MediaStreamingAccessRecord.  # noqa: E501
        :type session_identifier: str
        :param request_message: The request_message of this MediaStreamingAccessRecord.  # noqa: E501
        :type request_message: MediaStreamingAccessRecordAllOfRequestMessage
        :param cache_status: The cache_status of this MediaStreamingAccessRecord.  # noqa: E501
        :type cache_status: CacheStatus
        :param response_message: The response_message of this MediaStreamingAccessRecord.  # noqa: E501
        :type response_message: MediaStreamingAccessRecordAllOfResponseMessage
        :param processing_latency: The processing_latency of this MediaStreamingAccessRecord.  # noqa: E501
        :type processing_latency: float
        :param connection_metrics: The connection_metrics of this MediaStreamingAccessRecord.  # noqa: E501
        :type connection_metrics: MediaStreamingAccessRecordAllOfConnectionMetrics
        """
        self.openapi_types = {
            'timestamp': datetime,
            'media_stream_handler_endpoint_address': EndpointAddress,
            'application_server_endpoint_address': EndpointAddress,
            'session_identifier': str,
            'request_message': MediaStreamingAccessRecordAllOfRequestMessage,
            'cache_status': CacheStatus,
            'response_message': MediaStreamingAccessRecordAllOfResponseMessage,
            'processing_latency': float,
            'connection_metrics': MediaStreamingAccessRecordAllOfConnectionMetrics
        }

        self.attribute_map = {
            'timestamp': 'timestamp',
            'media_stream_handler_endpoint_address': 'mediaStreamHandlerEndpointAddress',
            'application_server_endpoint_address': 'applicationServerEndpointAddress',
            'session_identifier': 'sessionIdentifier',
            'request_message': 'requestMessage',
            'cache_status': 'cacheStatus',
            'response_message': 'responseMessage',
            'processing_latency': 'processingLatency',
            'connection_metrics': 'connectionMetrics'
        }

        self._timestamp = timestamp
        self._media_stream_handler_endpoint_address = media_stream_handler_endpoint_address
        self._application_server_endpoint_address = application_server_endpoint_address
        self._session_identifier = session_identifier
        self._request_message = request_message
        self._cache_status = cache_status
        self._response_message = response_message
        self._processing_latency = processing_latency
        self._connection_metrics = connection_metrics

    @classmethod
    def from_dict(cls, dikt) -> 'MediaStreamingAccessRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MediaStreamingAccessRecord of this MediaStreamingAccessRecord.  # noqa: E501
        :rtype: MediaStreamingAccessRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def timestamp(self):
        """Gets the timestamp of this MediaStreamingAccessRecord.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :return: The timestamp of this MediaStreamingAccessRecord.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this MediaStreamingAccessRecord.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :param timestamp: The timestamp of this MediaStreamingAccessRecord.
        :type timestamp: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def media_stream_handler_endpoint_address(self):
        """Gets the media_stream_handler_endpoint_address of this MediaStreamingAccessRecord.


        :return: The media_stream_handler_endpoint_address of this MediaStreamingAccessRecord.
        :rtype: EndpointAddress
        """
        return self._media_stream_handler_endpoint_address

    @media_stream_handler_endpoint_address.setter
    def media_stream_handler_endpoint_address(self, media_stream_handler_endpoint_address):
        """Sets the media_stream_handler_endpoint_address of this MediaStreamingAccessRecord.


        :param media_stream_handler_endpoint_address: The media_stream_handler_endpoint_address of this MediaStreamingAccessRecord.
        :type media_stream_handler_endpoint_address: EndpointAddress
        """
        if media_stream_handler_endpoint_address is None:
            raise ValueError("Invalid value for `media_stream_handler_endpoint_address`, must not be `None`")  # noqa: E501

        self._media_stream_handler_endpoint_address = media_stream_handler_endpoint_address

    @property
    def application_server_endpoint_address(self):
        """Gets the application_server_endpoint_address of this MediaStreamingAccessRecord.


        :return: The application_server_endpoint_address of this MediaStreamingAccessRecord.
        :rtype: EndpointAddress
        """
        return self._application_server_endpoint_address

    @application_server_endpoint_address.setter
    def application_server_endpoint_address(self, application_server_endpoint_address):
        """Sets the application_server_endpoint_address of this MediaStreamingAccessRecord.


        :param application_server_endpoint_address: The application_server_endpoint_address of this MediaStreamingAccessRecord.
        :type application_server_endpoint_address: EndpointAddress
        """
        if application_server_endpoint_address is None:
            raise ValueError("Invalid value for `application_server_endpoint_address`, must not be `None`")  # noqa: E501

        self._application_server_endpoint_address = application_server_endpoint_address

    @property
    def session_identifier(self):
        """Gets the session_identifier of this MediaStreamingAccessRecord.


        :return: The session_identifier of this MediaStreamingAccessRecord.
        :rtype: str
        """
        return self._session_identifier

    @session_identifier.setter
    def session_identifier(self, session_identifier):
        """Sets the session_identifier of this MediaStreamingAccessRecord.


        :param session_identifier: The session_identifier of this MediaStreamingAccessRecord.
        :type session_identifier: str
        """

        self._session_identifier = session_identifier

    @property
    def request_message(self):
        """Gets the request_message of this MediaStreamingAccessRecord.


        :return: The request_message of this MediaStreamingAccessRecord.
        :rtype: MediaStreamingAccessRecordAllOfRequestMessage
        """
        return self._request_message

    @request_message.setter
    def request_message(self, request_message):
        """Sets the request_message of this MediaStreamingAccessRecord.


        :param request_message: The request_message of this MediaStreamingAccessRecord.
        :type request_message: MediaStreamingAccessRecordAllOfRequestMessage
        """
        if request_message is None:
            raise ValueError("Invalid value for `request_message`, must not be `None`")  # noqa: E501

        self._request_message = request_message

    @property
    def cache_status(self):
        """Gets the cache_status of this MediaStreamingAccessRecord.


        :return: The cache_status of this MediaStreamingAccessRecord.
        :rtype: CacheStatus
        """
        return self._cache_status

    @cache_status.setter
    def cache_status(self, cache_status):
        """Sets the cache_status of this MediaStreamingAccessRecord.


        :param cache_status: The cache_status of this MediaStreamingAccessRecord.
        :type cache_status: CacheStatus
        """

        self._cache_status = cache_status

    @property
    def response_message(self):
        """Gets the response_message of this MediaStreamingAccessRecord.


        :return: The response_message of this MediaStreamingAccessRecord.
        :rtype: MediaStreamingAccessRecordAllOfResponseMessage
        """
        return self._response_message

    @response_message.setter
    def response_message(self, response_message):
        """Sets the response_message of this MediaStreamingAccessRecord.


        :param response_message: The response_message of this MediaStreamingAccessRecord.
        :type response_message: MediaStreamingAccessRecordAllOfResponseMessage
        """
        if response_message is None:
            raise ValueError("Invalid value for `response_message`, must not be `None`")  # noqa: E501

        self._response_message = response_message

    @property
    def processing_latency(self):
        """Gets the processing_latency of this MediaStreamingAccessRecord.

        string with format 'float' as defined in OpenAPI.  # noqa: E501

        :return: The processing_latency of this MediaStreamingAccessRecord.
        :rtype: float
        """
        return self._processing_latency

    @processing_latency.setter
    def processing_latency(self, processing_latency):
        """Sets the processing_latency of this MediaStreamingAccessRecord.

        string with format 'float' as defined in OpenAPI.  # noqa: E501

        :param processing_latency: The processing_latency of this MediaStreamingAccessRecord.
        :type processing_latency: float
        """
        if processing_latency is None:
            raise ValueError("Invalid value for `processing_latency`, must not be `None`")  # noqa: E501

        self._processing_latency = processing_latency

    @property
    def connection_metrics(self):
        """Gets the connection_metrics of this MediaStreamingAccessRecord.


        :return: The connection_metrics of this MediaStreamingAccessRecord.
        :rtype: MediaStreamingAccessRecordAllOfConnectionMetrics
        """
        return self._connection_metrics

    @connection_metrics.setter
    def connection_metrics(self, connection_metrics):
        """Sets the connection_metrics of this MediaStreamingAccessRecord.


        :param connection_metrics: The connection_metrics of this MediaStreamingAccessRecord.
        :type connection_metrics: MediaStreamingAccessRecordAllOfConnectionMetrics
        """

        self._connection_metrics = connection_metrics
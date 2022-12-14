# coding: utf-8

"""
    Public Transit API

    Public Transit is a set of three REST APIs that provides public transit routing information and public transit stations information available within an area or for a given station.   # noqa: E501

    OpenAPI spec version: 8.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from here_public_transit_api.api_client import ApiClient


class StationSearchApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_health(self, **kwargs):  # noqa: E501
        """Health  # noqa: E501

        Returns the health status of the service  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_health(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: HealthResponseOKSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_health_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_health_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_health_with_http_info(self, **kwargs):  # noqa: E501
        """Health  # noqa: E501

        Returns the health status of the service  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_health_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: HealthResponseOKSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_health" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/health', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HealthResponseOKSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stations(self, **kwargs):  # noqa: E501
        """Stations  # noqa: E501

        Lists public transit stations. Discovers stations using structured or topological queries. The service accepts three types of queries as shown in the table below:  | Query | Parameter | Description | |-------|-----------|-------------| | Stations by IDs | `ids` | Takes a comma-separated list of station/stop identifiers. | | Stations by location | `in` | Takes a pair of coordinates to define the center and a radius to define the extent of a circular area where to search for departures. | | Stations by name and location | `name` and `in` | Takes the station name or part of the name to search for. It is composed of one or more space-separated words and does not support stopwords. |  Select a query from `one of` the options above to visualize the request parameters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StationOptions station_options: Station filter
        :param PlacesReturn _return: Defines which place attributes are included.   * `address` - The place's address.  * `transport` - List of transports.  * `accessPoints` - List of access points. 
        :return: StationsInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_stations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_stations_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_stations_with_http_info(self, **kwargs):  # noqa: E501
        """Stations  # noqa: E501

        Lists public transit stations. Discovers stations using structured or topological queries. The service accepts three types of queries as shown in the table below:  | Query | Parameter | Description | |-------|-----------|-------------| | Stations by IDs | `ids` | Takes a comma-separated list of station/stop identifiers. | | Stations by location | `in` | Takes a pair of coordinates to define the center and a radius to define the extent of a circular area where to search for departures. | | Stations by name and location | `name` and `in` | Takes the station name or part of the name to search for. It is composed of one or more space-separated words and does not support stopwords. |  Select a query from `one of` the options above to visualize the request parameters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StationOptions station_options: Station filter
        :param PlacesReturn _return: Defines which place attributes are included.   * `address` - The place's address.  * `transport` - List of transports.  * `accessPoints` - List of access points. 
        :return: StationsInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['station_options', '_return']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stations" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'station_options' in params:
            query_params.append(('stationOptions', params['station_options']))  # noqa: E501
        if '_return' in params:
            query_params.append(('return', params['_return']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/stations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StationsInfoResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_version(self, **kwargs):  # noqa: E501
        """Version  # noqa: E501

        Returns the version of the service  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_version(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_version_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_version_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_version_with_http_info(self, **kwargs):  # noqa: E501
        """Version  # noqa: E501

        Returns the version of the service  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_version_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_version" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/version', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

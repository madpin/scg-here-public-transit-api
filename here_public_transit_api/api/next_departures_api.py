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


class NextDeparturesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_departures(self, **kwargs):  # noqa: E501
        """Departures  # noqa: E501

        Lists public transit departures. Discovers subsequent departures using structured or topological queries. The service accepts two types of queries as shown in the table below:  | Query | Parameter | Description | |-------|-----------|-------------| | Departures by IDs | `ids` | takes a comma-separated list of station/stop identifiers | | Departures by Location | `in` | takes a pair of coordinates to define the center and a radius to define the extent of a circular area where to search for departures |  Select a query from `one of` the options above to visualize the request parameters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_departures(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BoardOptions board_options: Board options
        :param Time time: Specifies the time of earliest departure in `RFC 3339`, section 5.6 as defined by either `date-time` or `full-date` \"T\" `partial-time` (for example, `2019-06-24T01:23:45`). The requested time is converted to local time at each location. When the optional timezone offset is not specified, time is assumed to be local. If `time` is not specified, current time at departure place will be used. All `Time` values in the response are returned in the timezone of each location. 
        :param TransitModesFilter modes: Transit mode filter used to determine which modes of transit to include in the response. By default, all supported transit modes are permitted.  Supported modes: `highSpeedTrain` `intercityTrain` `interRegionalTrain` `regionalTrain` `cityTrain` `bus` `ferry` `subway` `lightRail` `privateBus` `inclined` `aerial` `busRapid` `monorail` `flight` `spaceship`  This parameter also support an exclusion list: It's sufficient to specify each mode to exclude by prefixing it with `-`. Mixing of inclusive and exclusive transit modes is not allowed.  examples:   * `subway,bus`. Returns only subways and busses.   * `-subway,-bus`. Returns all modes except subways and busses. 
        :param int max_per_board: The maximum number of subsequent departures per station board the response is to include.
        :param int max_per_transport: The maximum number of subsequent departures per transport returned in the response. A transport is identified by its name, direction and mode. When not set, all departures are returned, otherwise the first `maxPerTransport` departures for each transport in chronological order are returned. 
        :param str sort: Define how the departures are sorted. By default, the departures are returned sorted by scheduled time. When `sort=transport`, the departures are sorted first by transport and then by scheduled time.  * `sort=time`: means sorted by time. * `sort=transport`: means that we sort by `name`, `headsign`, `mode` and `time` in this order. 
        :param Timespan timespan: Limit the subsequent departures to the defined time window and starting from the time provided in the request. When not set, this filter is not applied and a maximum of 24 hours of departures can be returned. The filter will remove all departures outside the interval defined by time and time span. 
        :param str lang: Specifies the preferred language of the response. The value should comply with the [IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). 
        :return: StationBoardResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_departures_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_departures_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_departures_with_http_info(self, **kwargs):  # noqa: E501
        """Departures  # noqa: E501

        Lists public transit departures. Discovers subsequent departures using structured or topological queries. The service accepts two types of queries as shown in the table below:  | Query | Parameter | Description | |-------|-----------|-------------| | Departures by IDs | `ids` | takes a comma-separated list of station/stop identifiers | | Departures by Location | `in` | takes a pair of coordinates to define the center and a radius to define the extent of a circular area where to search for departures |  Select a query from `one of` the options above to visualize the request parameters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_departures_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BoardOptions board_options: Board options
        :param Time time: Specifies the time of earliest departure in `RFC 3339`, section 5.6 as defined by either `date-time` or `full-date` \"T\" `partial-time` (for example, `2019-06-24T01:23:45`). The requested time is converted to local time at each location. When the optional timezone offset is not specified, time is assumed to be local. If `time` is not specified, current time at departure place will be used. All `Time` values in the response are returned in the timezone of each location. 
        :param TransitModesFilter modes: Transit mode filter used to determine which modes of transit to include in the response. By default, all supported transit modes are permitted.  Supported modes: `highSpeedTrain` `intercityTrain` `interRegionalTrain` `regionalTrain` `cityTrain` `bus` `ferry` `subway` `lightRail` `privateBus` `inclined` `aerial` `busRapid` `monorail` `flight` `spaceship`  This parameter also support an exclusion list: It's sufficient to specify each mode to exclude by prefixing it with `-`. Mixing of inclusive and exclusive transit modes is not allowed.  examples:   * `subway,bus`. Returns only subways and busses.   * `-subway,-bus`. Returns all modes except subways and busses. 
        :param int max_per_board: The maximum number of subsequent departures per station board the response is to include.
        :param int max_per_transport: The maximum number of subsequent departures per transport returned in the response. A transport is identified by its name, direction and mode. When not set, all departures are returned, otherwise the first `maxPerTransport` departures for each transport in chronological order are returned. 
        :param str sort: Define how the departures are sorted. By default, the departures are returned sorted by scheduled time. When `sort=transport`, the departures are sorted first by transport and then by scheduled time.  * `sort=time`: means sorted by time. * `sort=transport`: means that we sort by `name`, `headsign`, `mode` and `time` in this order. 
        :param Timespan timespan: Limit the subsequent departures to the defined time window and starting from the time provided in the request. When not set, this filter is not applied and a maximum of 24 hours of departures can be returned. The filter will remove all departures outside the interval defined by time and time span. 
        :param str lang: Specifies the preferred language of the response. The value should comply with the [IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). 
        :return: StationBoardResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['board_options', 'time', 'modes', 'max_per_board', 'max_per_transport', 'sort', 'timespan', 'lang']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_departures" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'board_options' in params:
            query_params.append(('boardOptions', params['board_options']))  # noqa: E501
        if 'time' in params:
            query_params.append(('time', params['time']))  # noqa: E501
        if 'modes' in params:
            query_params.append(('modes', params['modes']))  # noqa: E501
        if 'max_per_board' in params:
            query_params.append(('maxPerBoard', params['max_per_board']))  # noqa: E501
        if 'max_per_transport' in params:
            query_params.append(('maxPerTransport', params['max_per_transport']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'timespan' in params:
            query_params.append(('timespan', params['timespan']))  # noqa: E501
        if 'lang' in params:
            query_params.append(('lang', params['lang']))  # noqa: E501

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
            '/departures', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StationBoardResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

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
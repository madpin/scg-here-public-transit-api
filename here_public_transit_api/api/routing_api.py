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


class RoutingApi(object):
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

    def get_routes(self, origin, destination, **kwargs):  # noqa: E501
        """Routes  # noqa: E501

        Lists public transit routes. The service supports several use cases as follows:    * define routes based on arrival or departure times.   * filter specific transit modes, such as rail and metro only.   * plan routes hours or days in advance.   * set a maximum distance for the walk to the nearest transit stop/station or the speed of the walk.   * define how many changes or transfers the journey may include.   * request turn-by-turn navigation.   * request route polyline in order to view the route over a map.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_routes(origin, destination, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LocationString origin: Trip origin WGS-84 compliant coordinates.  Format: `{lat},{lng}[;placeName={name}]`  The optional `placeName` parameter can be used to customize   the name of the origin place and will affect the generated actions descriptions.   (required)
        :param LocationString destination: Trip destination WGS-84 compliant coordinates.  Format: `{lat},{lng}[;placeName={name}]`  The optional `placeName` parameter can be used to customize the   name of the destination place and will affect the generated actions descriptions.   (required)
        :param str lang: Specifies the preferred language of the response. The value should comply with the [IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). 
        :param Units units: Units of measurement used, for example, in guidance instructions. The default is `metric`.
        :param Time departure_time: Specifies the time of departure as defined by either `date-time` or `full-date` `T` `partial-time` in `RFC 3339`, section 5.6 (for example, `2019-06-24T01:23:45`). The requested time is converted to the local time at origin. When the optional timezone offset is not specified, time is assumed to be local. If neither `departureTime` or `arrivalTime` are specified, current time at departure location will be used. All `Time` values in the response are returned in the timezone of each location. 
        :param Time arrival_time: Specifies the time of arrival as defined by either `date-time` or `full-date` `T` `partial-time` in `RFC 3339`, section 5.6 (for example, `2019-06-24T01:23:45`). The requested time is converted to the local time at destination. When the optional timezone offset is not specified, time is assumed to be local. All `Time` values in the response are returned in the timezone of each location.  Note : The following features do not support the arrivalTime parameter: * EV Routing * Route Handle * Route Import 
        :param int alternatives: Number of alternative routes to return aside from the optimal route.
        :param int changes: Maximum number of changes or transfers allowed in a route. Unlimited number of changes is permitted when not set. 
        :param TransitModesFilter modes: Transit mode filter used to determine which modes of transit to include in the response. By default, all supported transit modes are permitted.  Supported modes: `highSpeedTrain` `intercityTrain` `interRegionalTrain` `regionalTrain` `cityTrain` `bus` `ferry` `subway` `lightRail` `privateBus` `inclined` `aerial` `busRapid` `monorail` `flight` `spaceship`  This parameter also support an exclusion list: It's sufficient to specify each mode to exclude by prefixing it with `-`. Mixing of inclusive and exclusive transit modes is not allowed.  examples:   * `subway,bus`. Returns only subways and busses.   * `-subway,-bus`. Returns all modes except subways and busses. 
        :param PedestrianSpeed pedestrian_speed: Walking speed in meters per second. Influences the duration of walking segments from origin to a station, from a station to destination and in-between the stations (e.g. if transfer is needed). 
        :param int pedestrian_max_distance: Maximum allowed walking distance in meters (e.g. when looking for nearest stations).
        :param list[str] _return: Defines which section attributes are included.   * `intermediate` - List of intermediate stops within a section of the route. If    enabled, the response includes `intermediateStops` attribute. Each intermediate stop includes    stop/station names, WGS-84 geocoordinates, and the departure times at the stops.  * `fares` - List of fares/tickets to cover a section of the route.  * `polyline` - Polyline for the route in    [Flexible Polyline](https://github.com/heremaps/flexible-polyline/blob/master/README.md)    Encoding.  * `actions` - Actions (such as maneuvers or tasks) that must be taken to complete the section.  * `travelSummary` - Include summary for the travel portion of the section.  * `incidents` - Include a list of all incidents applicable to each section.  * `bookingLinks` - Include a list of links to book a ride for a section of the route. 
        :return: TransitRouteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_routes_with_http_info(origin, destination, **kwargs)  # noqa: E501
        else:
            (data) = self.get_routes_with_http_info(origin, destination, **kwargs)  # noqa: E501
            return data

    def get_routes_with_http_info(self, origin, destination, **kwargs):  # noqa: E501
        """Routes  # noqa: E501

        Lists public transit routes. The service supports several use cases as follows:    * define routes based on arrival or departure times.   * filter specific transit modes, such as rail and metro only.   * plan routes hours or days in advance.   * set a maximum distance for the walk to the nearest transit stop/station or the speed of the walk.   * define how many changes or transfers the journey may include.   * request turn-by-turn navigation.   * request route polyline in order to view the route over a map.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_routes_with_http_info(origin, destination, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LocationString origin: Trip origin WGS-84 compliant coordinates.  Format: `{lat},{lng}[;placeName={name}]`  The optional `placeName` parameter can be used to customize   the name of the origin place and will affect the generated actions descriptions.   (required)
        :param LocationString destination: Trip destination WGS-84 compliant coordinates.  Format: `{lat},{lng}[;placeName={name}]`  The optional `placeName` parameter can be used to customize the   name of the destination place and will affect the generated actions descriptions.   (required)
        :param str lang: Specifies the preferred language of the response. The value should comply with the [IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). 
        :param Units units: Units of measurement used, for example, in guidance instructions. The default is `metric`.
        :param Time departure_time: Specifies the time of departure as defined by either `date-time` or `full-date` `T` `partial-time` in `RFC 3339`, section 5.6 (for example, `2019-06-24T01:23:45`). The requested time is converted to the local time at origin. When the optional timezone offset is not specified, time is assumed to be local. If neither `departureTime` or `arrivalTime` are specified, current time at departure location will be used. All `Time` values in the response are returned in the timezone of each location. 
        :param Time arrival_time: Specifies the time of arrival as defined by either `date-time` or `full-date` `T` `partial-time` in `RFC 3339`, section 5.6 (for example, `2019-06-24T01:23:45`). The requested time is converted to the local time at destination. When the optional timezone offset is not specified, time is assumed to be local. All `Time` values in the response are returned in the timezone of each location.  Note : The following features do not support the arrivalTime parameter: * EV Routing * Route Handle * Route Import 
        :param int alternatives: Number of alternative routes to return aside from the optimal route.
        :param int changes: Maximum number of changes or transfers allowed in a route. Unlimited number of changes is permitted when not set. 
        :param TransitModesFilter modes: Transit mode filter used to determine which modes of transit to include in the response. By default, all supported transit modes are permitted.  Supported modes: `highSpeedTrain` `intercityTrain` `interRegionalTrain` `regionalTrain` `cityTrain` `bus` `ferry` `subway` `lightRail` `privateBus` `inclined` `aerial` `busRapid` `monorail` `flight` `spaceship`  This parameter also support an exclusion list: It's sufficient to specify each mode to exclude by prefixing it with `-`. Mixing of inclusive and exclusive transit modes is not allowed.  examples:   * `subway,bus`. Returns only subways and busses.   * `-subway,-bus`. Returns all modes except subways and busses. 
        :param PedestrianSpeed pedestrian_speed: Walking speed in meters per second. Influences the duration of walking segments from origin to a station, from a station to destination and in-between the stations (e.g. if transfer is needed). 
        :param int pedestrian_max_distance: Maximum allowed walking distance in meters (e.g. when looking for nearest stations).
        :param list[str] _return: Defines which section attributes are included.   * `intermediate` - List of intermediate stops within a section of the route. If    enabled, the response includes `intermediateStops` attribute. Each intermediate stop includes    stop/station names, WGS-84 geocoordinates, and the departure times at the stops.  * `fares` - List of fares/tickets to cover a section of the route.  * `polyline` - Polyline for the route in    [Flexible Polyline](https://github.com/heremaps/flexible-polyline/blob/master/README.md)    Encoding.  * `actions` - Actions (such as maneuvers or tasks) that must be taken to complete the section.  * `travelSummary` - Include summary for the travel portion of the section.  * `incidents` - Include a list of all incidents applicable to each section.  * `bookingLinks` - Include a list of links to book a ride for a section of the route. 
        :return: TransitRouteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['origin', 'destination', 'lang', 'units', 'departure_time', 'arrival_time', 'alternatives', 'changes', 'modes', 'pedestrian_speed', 'pedestrian_max_distance', '_return']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'origin' is set
        if ('origin' not in params or
                params['origin'] is None):
            raise ValueError("Missing the required parameter `origin` when calling `get_routes`")  # noqa: E501
        # verify the required parameter 'destination' is set
        if ('destination' not in params or
                params['destination'] is None):
            raise ValueError("Missing the required parameter `destination` when calling `get_routes`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'origin' in params:
            query_params.append(('origin', params['origin']))  # noqa: E501
        if 'destination' in params:
            query_params.append(('destination', params['destination']))  # noqa: E501
        if 'lang' in params:
            query_params.append(('lang', params['lang']))  # noqa: E501
        if 'units' in params:
            query_params.append(('units', params['units']))  # noqa: E501
        if 'departure_time' in params:
            query_params.append(('departureTime', params['departure_time']))  # noqa: E501
        if 'arrival_time' in params:
            query_params.append(('arrivalTime', params['arrival_time']))  # noqa: E501
        if 'alternatives' in params:
            query_params.append(('alternatives', params['alternatives']))  # noqa: E501
        if 'changes' in params:
            query_params.append(('changes', params['changes']))  # noqa: E501
        if 'modes' in params:
            query_params.append(('modes', params['modes']))  # noqa: E501
        if 'pedestrian_speed' in params:
            query_params.append(('pedestrian[speed]', params['pedestrian_speed']))  # noqa: E501
        if 'pedestrian_max_distance' in params:
            query_params.append(('pedestrian[maxDistance]', params['pedestrian_max_distance']))  # noqa: E501
        if '_return' in params:
            query_params.append(('return', params['_return']))  # noqa: E501
            collection_formats['return'] = 'csv'  # noqa: E501

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
            '/routes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransitRouteResponse',  # noqa: E501
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
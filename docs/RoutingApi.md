# here_public_transit_api.RoutingApi

All URIs are relative to *https://transit.hereapi.com/v8*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health**](RoutingApi.md#get_health) | **GET** /health | Health
[**get_routes**](RoutingApi.md#get_routes) | **GET** /routes | Routes
[**get_version**](RoutingApi.md#get_version) | **GET** /version | Version

# **get_health**
> HealthResponseOKSchema get_health()

Health

Returns the health status of the service

### Example
```python
from __future__ import print_function
import time
import here_public_transit_api
from here_public_transit_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = here_public_transit_api.RoutingApi()

try:
    # Health
    api_response = api_instance.get_health()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthResponseOKSchema**](HealthResponseOKSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routes**
> TransitRouteResponse get_routes(origin, destination, lang=lang, units=units, departure_time=departure_time, arrival_time=arrival_time, alternatives=alternatives, changes=changes, modes=modes, pedestrian_speed=pedestrian_speed, pedestrian_max_distance=pedestrian_max_distance, _return=_return)

Routes

Lists public transit routes. The service supports several use cases as follows:    * define routes based on arrival or departure times.   * filter specific transit modes, such as rail and metro only.   * plan routes hours or days in advance.   * set a maximum distance for the walk to the nearest transit stop/station or the speed of the walk.   * define how many changes or transfers the journey may include.   * request turn-by-turn navigation.   * request route polyline in order to view the route over a map. 

### Example
```python
from __future__ import print_function
import time
import here_public_transit_api
from here_public_transit_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = here_public_transit_api.Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = here_public_transit_api.RoutingApi(here_public_transit_api.ApiClient(configuration))
origin = here_public_transit_api.LocationString() # LocationString | Trip origin WGS-84 compliant coordinates.  Format: `{lat},{lng}[;placeName={name}]`  The optional `placeName` parameter can be used to customize   the name of the origin place and will affect the generated actions descriptions.  
destination = here_public_transit_api.LocationString() # LocationString | Trip destination WGS-84 compliant coordinates.  Format: `{lat},{lng}[;placeName={name}]`  The optional `placeName` parameter can be used to customize the   name of the destination place and will affect the generated actions descriptions.  
lang = 'en-US' # str | Specifies the preferred language of the response. The value should comply with the [IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt).  (optional) (default to en-US)
units = here_public_transit_api.Units() # Units | Units of measurement used, for example, in guidance instructions. The default is `metric`. (optional)
departure_time = here_public_transit_api.Time() # Time | Specifies the time of departure as defined by either `date-time` or `full-date` `T` `partial-time` in `RFC 3339`, section 5.6 (for example, `2019-06-24T01:23:45`). The requested time is converted to the local time at origin. When the optional timezone offset is not specified, time is assumed to be local. If neither `departureTime` or `arrivalTime` are specified, current time at departure location will be used. All `Time` values in the response are returned in the timezone of each location.  (optional)
arrival_time = here_public_transit_api.Time() # Time | Specifies the time of arrival as defined by either `date-time` or `full-date` `T` `partial-time` in `RFC 3339`, section 5.6 (for example, `2019-06-24T01:23:45`). The requested time is converted to the local time at destination. When the optional timezone offset is not specified, time is assumed to be local. All `Time` values in the response are returned in the timezone of each location.  Note : The following features do not support the arrivalTime parameter: * EV Routing * Route Handle * Route Import  (optional)
alternatives = 0 # int | Number of alternative routes to return aside from the optimal route. (optional) (default to 0)
changes = 56 # int | Maximum number of changes or transfers allowed in a route. Unlimited number of changes is permitted when not set.  (optional)
modes = here_public_transit_api.TransitModesFilter() # TransitModesFilter | Transit mode filter used to determine which modes of transit to include in the response. By default, all supported transit modes are permitted.  Supported modes: `highSpeedTrain` `intercityTrain` `interRegionalTrain` `regionalTrain` `cityTrain` `bus` `ferry` `subway` `lightRail` `privateBus` `inclined` `aerial` `busRapid` `monorail` `flight` `spaceship`  This parameter also support an exclusion list: It's sufficient to specify each mode to exclude by prefixing it with `-`. Mixing of inclusive and exclusive transit modes is not allowed.  examples:   * `subway,bus`. Returns only subways and busses.   * `-subway,-bus`. Returns all modes except subways and busses.  (optional)
pedestrian_speed = here_public_transit_api.PedestrianSpeed() # PedestrianSpeed | Walking speed in meters per second. Influences the duration of walking segments from origin to a station, from a station to destination and in-between the stations (e.g. if transfer is needed).  (optional)
pedestrian_max_distance = 2000 # int | Maximum allowed walking distance in meters (e.g. when looking for nearest stations). (optional) (default to 2000)
_return = ['_return_example'] # list[str] | Defines which section attributes are included.   * `intermediate` - List of intermediate stops within a section of the route. If    enabled, the response includes `intermediateStops` attribute. Each intermediate stop includes    stop/station names, WGS-84 geocoordinates, and the departure times at the stops.  * `fares` - List of fares/tickets to cover a section of the route.  * `polyline` - Polyline for the route in    [Flexible Polyline](https://github.com/heremaps/flexible-polyline/blob/master/README.md)    Encoding.  * `actions` - Actions (such as maneuvers or tasks) that must be taken to complete the section.  * `travelSummary` - Include summary for the travel portion of the section.  * `incidents` - Include a list of all incidents applicable to each section.  * `bookingLinks` - Include a list of links to book a ride for a section of the route.  (optional)

try:
    # Routes
    api_response = api_instance.get_routes(origin, destination, lang=lang, units=units, departure_time=departure_time, arrival_time=arrival_time, alternatives=alternatives, changes=changes, modes=modes, pedestrian_speed=pedestrian_speed, pedestrian_max_distance=pedestrian_max_distance, _return=_return)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | [**LocationString**](.md)| Trip origin WGS-84 compliant coordinates.  Format: &#x60;{lat},{lng}[;placeName&#x3D;{name}]&#x60;  The optional &#x60;placeName&#x60; parameter can be used to customize   the name of the origin place and will affect the generated actions descriptions.   | 
 **destination** | [**LocationString**](.md)| Trip destination WGS-84 compliant coordinates.  Format: &#x60;{lat},{lng}[;placeName&#x3D;{name}]&#x60;  The optional &#x60;placeName&#x60; parameter can be used to customize the   name of the destination place and will affect the generated actions descriptions.   | 
 **lang** | **str**| Specifies the preferred language of the response. The value should comply with the [IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt).  | [optional] [default to en-US]
 **units** | [**Units**](.md)| Units of measurement used, for example, in guidance instructions. The default is &#x60;metric&#x60;. | [optional] 
 **departure_time** | [**Time**](.md)| Specifies the time of departure as defined by either &#x60;date-time&#x60; or &#x60;full-date&#x60; &#x60;T&#x60; &#x60;partial-time&#x60; in &#x60;RFC 3339&#x60;, section 5.6 (for example, &#x60;2019-06-24T01:23:45&#x60;). The requested time is converted to the local time at origin. When the optional timezone offset is not specified, time is assumed to be local. If neither &#x60;departureTime&#x60; or &#x60;arrivalTime&#x60; are specified, current time at departure location will be used. All &#x60;Time&#x60; values in the response are returned in the timezone of each location.  | [optional] 
 **arrival_time** | [**Time**](.md)| Specifies the time of arrival as defined by either &#x60;date-time&#x60; or &#x60;full-date&#x60; &#x60;T&#x60; &#x60;partial-time&#x60; in &#x60;RFC 3339&#x60;, section 5.6 (for example, &#x60;2019-06-24T01:23:45&#x60;). The requested time is converted to the local time at destination. When the optional timezone offset is not specified, time is assumed to be local. All &#x60;Time&#x60; values in the response are returned in the timezone of each location.  Note : The following features do not support the arrivalTime parameter: * EV Routing * Route Handle * Route Import  | [optional] 
 **alternatives** | **int**| Number of alternative routes to return aside from the optimal route. | [optional] [default to 0]
 **changes** | **int**| Maximum number of changes or transfers allowed in a route. Unlimited number of changes is permitted when not set.  | [optional] 
 **modes** | [**TransitModesFilter**](.md)| Transit mode filter used to determine which modes of transit to include in the response. By default, all supported transit modes are permitted.  Supported modes: &#x60;highSpeedTrain&#x60; &#x60;intercityTrain&#x60; &#x60;interRegionalTrain&#x60; &#x60;regionalTrain&#x60; &#x60;cityTrain&#x60; &#x60;bus&#x60; &#x60;ferry&#x60; &#x60;subway&#x60; &#x60;lightRail&#x60; &#x60;privateBus&#x60; &#x60;inclined&#x60; &#x60;aerial&#x60; &#x60;busRapid&#x60; &#x60;monorail&#x60; &#x60;flight&#x60; &#x60;spaceship&#x60;  This parameter also support an exclusion list: It&#x27;s sufficient to specify each mode to exclude by prefixing it with &#x60;-&#x60;. Mixing of inclusive and exclusive transit modes is not allowed.  examples:   * &#x60;subway,bus&#x60;. Returns only subways and busses.   * &#x60;-subway,-bus&#x60;. Returns all modes except subways and busses.  | [optional] 
 **pedestrian_speed** | [**PedestrianSpeed**](.md)| Walking speed in meters per second. Influences the duration of walking segments from origin to a station, from a station to destination and in-between the stations (e.g. if transfer is needed).  | [optional] 
 **pedestrian_max_distance** | **int**| Maximum allowed walking distance in meters (e.g. when looking for nearest stations). | [optional] [default to 2000]
 **_return** | [**list[str]**](str.md)| Defines which section attributes are included.   * &#x60;intermediate&#x60; - List of intermediate stops within a section of the route. If    enabled, the response includes &#x60;intermediateStops&#x60; attribute. Each intermediate stop includes    stop/station names, WGS-84 geocoordinates, and the departure times at the stops.  * &#x60;fares&#x60; - List of fares/tickets to cover a section of the route.  * &#x60;polyline&#x60; - Polyline for the route in    [Flexible Polyline](https://github.com/heremaps/flexible-polyline/blob/master/README.md)    Encoding.  * &#x60;actions&#x60; - Actions (such as maneuvers or tasks) that must be taken to complete the section.  * &#x60;travelSummary&#x60; - Include summary for the travel portion of the section.  * &#x60;incidents&#x60; - Include a list of all incidents applicable to each section.  * &#x60;bookingLinks&#x60; - Include a list of links to book a ride for a section of the route.  | [optional] 

### Return type

[**TransitRouteResponse**](TransitRouteResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> InlineResponse200 get_version()

Version

Returns the version of the service

### Example
```python
from __future__ import print_function
import time
import here_public_transit_api
from here_public_transit_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = here_public_transit_api.RoutingApi()

try:
    # Version
    api_response = api_instance.get_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


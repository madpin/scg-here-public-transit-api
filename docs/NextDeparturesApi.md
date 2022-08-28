# here_public_transit_api.NextDeparturesApi

All URIs are relative to *https://transit.hereapi.com/v8*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_departures**](NextDeparturesApi.md#get_departures) | **GET** /departures | Departures
[**get_health**](NextDeparturesApi.md#get_health) | **GET** /health | Health
[**get_version**](NextDeparturesApi.md#get_version) | **GET** /version | Version

# **get_departures**
> StationBoardResponse get_departures(board_options=board_options, time=time, modes=modes, max_per_board=max_per_board, max_per_transport=max_per_transport, sort=sort, timespan=timespan, lang=lang)

Departures

Lists public transit departures. Discovers subsequent departures using structured or topological queries. The service accepts two types of queries as shown in the table below:  | Query | Parameter | Description | |-------|-----------|-------------| | Departures by IDs | `ids` | takes a comma-separated list of station/stop identifiers | | Departures by Location | `in` | takes a pair of coordinates to define the center and a radius to define the extent of a circular area where to search for departures |  Select a query from `one of` the options above to visualize the request parameters. 

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
api_instance = here_public_transit_api.NextDeparturesApi(here_public_transit_api.ApiClient(configuration))
board_options = here_public_transit_api.BoardOptions() # BoardOptions | Board options (optional)
time = here_public_transit_api.Time() # Time | Specifies the time of earliest departure in `RFC 3339`, section 5.6 as defined by either `date-time` or `full-date` \"T\" `partial-time` (for example, `2019-06-24T01:23:45`). The requested time is converted to local time at each location. When the optional timezone offset is not specified, time is assumed to be local. If `time` is not specified, current time at departure place will be used. All `Time` values in the response are returned in the timezone of each location.  (optional)
modes = here_public_transit_api.TransitModesFilter() # TransitModesFilter | Transit mode filter used to determine which modes of transit to include in the response. By default, all supported transit modes are permitted.  Supported modes: `highSpeedTrain` `intercityTrain` `interRegionalTrain` `regionalTrain` `cityTrain` `bus` `ferry` `subway` `lightRail` `privateBus` `inclined` `aerial` `busRapid` `monorail` `flight` `spaceship`  This parameter also support an exclusion list: It's sufficient to specify each mode to exclude by prefixing it with `-`. Mixing of inclusive and exclusive transit modes is not allowed.  examples:   * `subway,bus`. Returns only subways and busses.   * `-subway,-bus`. Returns all modes except subways and busses.  (optional)
max_per_board = 5 # int | The maximum number of subsequent departures per station board the response is to include. (optional) (default to 5)
max_per_transport = 56 # int | The maximum number of subsequent departures per transport returned in the response. A transport is identified by its name, direction and mode. When not set, all departures are returned, otherwise the first `maxPerTransport` departures for each transport in chronological order are returned.  (optional)
sort = 'time' # str | Define how the departures are sorted. By default, the departures are returned sorted by scheduled time. When `sort=transport`, the departures are sorted first by transport and then by scheduled time.  * `sort=time`: means sorted by time. * `sort=transport`: means that we sort by `name`, `headsign`, `mode` and `time` in this order.  (optional) (default to time)
timespan = here_public_transit_api.Timespan() # Timespan | Limit the subsequent departures to the defined time window and starting from the time provided in the request. When not set, this filter is not applied and a maximum of 24 hours of departures can be returned. The filter will remove all departures outside the interval defined by time and time span.  (optional)
lang = 'en-US' # str | Specifies the preferred language of the response. The value should comply with the [IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt).  (optional) (default to en-US)

try:
    # Departures
    api_response = api_instance.get_departures(board_options=board_options, time=time, modes=modes, max_per_board=max_per_board, max_per_transport=max_per_transport, sort=sort, timespan=timespan, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NextDeparturesApi->get_departures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_options** | [**BoardOptions**](.md)| Board options | [optional] 
 **time** | [**Time**](.md)| Specifies the time of earliest departure in &#x60;RFC 3339&#x60;, section 5.6 as defined by either &#x60;date-time&#x60; or &#x60;full-date&#x60; \&quot;T\&quot; &#x60;partial-time&#x60; (for example, &#x60;2019-06-24T01:23:45&#x60;). The requested time is converted to local time at each location. When the optional timezone offset is not specified, time is assumed to be local. If &#x60;time&#x60; is not specified, current time at departure place will be used. All &#x60;Time&#x60; values in the response are returned in the timezone of each location.  | [optional] 
 **modes** | [**TransitModesFilter**](.md)| Transit mode filter used to determine which modes of transit to include in the response. By default, all supported transit modes are permitted.  Supported modes: &#x60;highSpeedTrain&#x60; &#x60;intercityTrain&#x60; &#x60;interRegionalTrain&#x60; &#x60;regionalTrain&#x60; &#x60;cityTrain&#x60; &#x60;bus&#x60; &#x60;ferry&#x60; &#x60;subway&#x60; &#x60;lightRail&#x60; &#x60;privateBus&#x60; &#x60;inclined&#x60; &#x60;aerial&#x60; &#x60;busRapid&#x60; &#x60;monorail&#x60; &#x60;flight&#x60; &#x60;spaceship&#x60;  This parameter also support an exclusion list: It&#x27;s sufficient to specify each mode to exclude by prefixing it with &#x60;-&#x60;. Mixing of inclusive and exclusive transit modes is not allowed.  examples:   * &#x60;subway,bus&#x60;. Returns only subways and busses.   * &#x60;-subway,-bus&#x60;. Returns all modes except subways and busses.  | [optional] 
 **max_per_board** | **int**| The maximum number of subsequent departures per station board the response is to include. | [optional] [default to 5]
 **max_per_transport** | **int**| The maximum number of subsequent departures per transport returned in the response. A transport is identified by its name, direction and mode. When not set, all departures are returned, otherwise the first &#x60;maxPerTransport&#x60; departures for each transport in chronological order are returned.  | [optional] 
 **sort** | **str**| Define how the departures are sorted. By default, the departures are returned sorted by scheduled time. When &#x60;sort&#x3D;transport&#x60;, the departures are sorted first by transport and then by scheduled time.  * &#x60;sort&#x3D;time&#x60;: means sorted by time. * &#x60;sort&#x3D;transport&#x60;: means that we sort by &#x60;name&#x60;, &#x60;headsign&#x60;, &#x60;mode&#x60; and &#x60;time&#x60; in this order.  | [optional] [default to time]
 **timespan** | [**Timespan**](.md)| Limit the subsequent departures to the defined time window and starting from the time provided in the request. When not set, this filter is not applied and a maximum of 24 hours of departures can be returned. The filter will remove all departures outside the interval defined by time and time span.  | [optional] 
 **lang** | **str**| Specifies the preferred language of the response. The value should comply with the [IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt).  | [optional] [default to en-US]

### Return type

[**StationBoardResponse**](StationBoardResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = here_public_transit_api.NextDeparturesApi()

try:
    # Health
    api_response = api_instance.get_health()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NextDeparturesApi->get_health: %s\n" % e)
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
api_instance = here_public_transit_api.NextDeparturesApi()

try:
    # Version
    api_response = api_instance.get_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NextDeparturesApi->get_version: %s\n" % e)
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


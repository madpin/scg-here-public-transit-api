# here_public_transit_api.StationSearchApi

All URIs are relative to *https://transit.hereapi.com/v8*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health**](StationSearchApi.md#get_health) | **GET** /health | Health
[**get_stations**](StationSearchApi.md#get_stations) | **GET** /stations | Stations
[**get_version**](StationSearchApi.md#get_version) | **GET** /version | Version

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
api_instance = here_public_transit_api.StationSearchApi()

try:
    # Health
    api_response = api_instance.get_health()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StationSearchApi->get_health: %s\n" % e)
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

# **get_stations**
> StationsInfoResponse get_stations(station_options=station_options, _return=_return)

Stations

Lists public transit stations. Discovers stations using structured or topological queries. The service accepts three types of queries as shown in the table below:  | Query | Parameter | Description | |-------|-----------|-------------| | Stations by IDs | `ids` | Takes a comma-separated list of station/stop identifiers. | | Stations by location | `in` | Takes a pair of coordinates to define the center and a radius to define the extent of a circular area where to search for departures. | | Stations by name and location | `name` and `in` | Takes the station name or part of the name to search for. It is composed of one or more space-separated words and does not support stopwords. |  Select a query from `one of` the options above to visualize the request parameters. 

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
api_instance = here_public_transit_api.StationSearchApi(here_public_transit_api.ApiClient(configuration))
station_options = here_public_transit_api.StationOptions() # StationOptions | Station filter (optional)
_return = here_public_transit_api.PlacesReturn() # PlacesReturn | Defines which place attributes are included.   * `address` - The place's address.  * `transport` - List of transports.  * `accessPoints` - List of access points.  (optional)

try:
    # Stations
    api_response = api_instance.get_stations(station_options=station_options, _return=_return)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StationSearchApi->get_stations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_options** | [**StationOptions**](.md)| Station filter | [optional] 
 **_return** | [**PlacesReturn**](.md)| Defines which place attributes are included.   * &#x60;address&#x60; - The place&#x27;s address.  * &#x60;transport&#x60; - List of transports.  * &#x60;accessPoints&#x60; - List of access points.  | [optional] 

### Return type

[**StationsInfoResponse**](StationsInfoResponse.md)

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
api_instance = here_public_transit_api.StationSearchApi()

try:
    # Version
    api_response = api_instance.get_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StationSearchApi->get_version: %s\n" % e)
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


# here_public_transit_api.CommonApi

All URIs are relative to *https://router.hereapi.com/v8*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health**](CommonApi.md#get_health) | **GET** /health | Health status of the service
[**get_version**](CommonApi.md#get_version) | **GET** /version | Full version of the API

# **get_health**
> HealthResponseOKSchema get_health(x_request_id=x_request_id)

Health status of the service

Returns the health of the service

### Example
```python
from __future__ import print_function
import time
import here_public_transit_api
from here_public_transit_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = here_public_transit_api.CommonApi()
x_request_id = 'x_request_id_example' # str | User-provided token that can be used to trace a request or a group of requests sent to the service. (optional)

try:
    # Health status of the service
    api_response = api_instance.get_health(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->get_health: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| User-provided token that can be used to trace a request or a group of requests sent to the service. | [optional] 

### Return type

[**HealthResponseOKSchema**](HealthResponseOKSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> VersionResponse get_version(x_request_id=x_request_id)

Full version of the API

Returns the version of the service

### Example
```python
from __future__ import print_function
import time
import here_public_transit_api
from here_public_transit_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = here_public_transit_api.CommonApi()
x_request_id = 'x_request_id_example' # str | User-provided token that can be used to trace a request or a group of requests sent to the service. (optional)

try:
    # Full version of the API
    api_response = api_instance.get_version(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->get_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| User-provided token that can be used to trace a request or a group of requests sent to the service. | [optional] 

### Return type

[**VersionResponse**](VersionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


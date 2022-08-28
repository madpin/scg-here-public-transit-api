# RouterRoute

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the route | 
**notices** | [**list[Notice]**](Notice.md) | Contains a list of issues encountered during the processing of this response. | [optional] 
**sections** | [**list[RouterSection]**](RouterSection.md) | An ordered list of vehicle, transit, and pedestrian sections making up the route.  | 
**route_handle** | **str** | Opaque handle of the calculated route.  A handle encodes the calculated route. The route can be decoded from a handle at a later point in time as long as the service uses the same map data which was used during encoding.  To request a handle set the &#x60;routeHandle&#x60; flag in &#x60;return&#x60; parameter. If a handle is requested, but fails to be calculated for any reason, then the &#x60;routeHandle&#x60; property is not available in the response. The rest of the route is intact.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


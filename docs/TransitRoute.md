# TransitRoute

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the route | 
**notices** | [**list[Notice]**](Notice.md) | Contains a list of issues related to this route.  Follows a list of possible notice codes:  * &#x60;excessiveWaitingTime&#x60;: Commuter has to wait at a station much longer than usual. * &#x60;changeOptionViolated&#x60;: This route contains more changes than specified by the &#x60;changes&#x60; parameter. * &#x60;nonviableRoute&#x60;: Based on the real-time situation, one or more changes on the route   are not possible. This can happen if real-time re-routing is not available on this area.  | [optional] 
**sections** | [**list[TransitRouteSection]**](TransitRouteSection.md) | A list of transit and pedestrian sections of the route. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


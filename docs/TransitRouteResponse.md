# TransitRouteResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notices** | [**list[Notice]**](Notice.md) | Contains a list of issues related to this response. Follows a list of possible notice codes:  * &#x60;noRouteFound&#x60;: Routing between origin and destination is not possible given current input parameters. * &#x60;noRoutesFound&#x60;: (Deprecated) For more information, see noRouteFound. * &#x60;noTransitRouteFound&#x60;: Transit routing between origin and destination is not possible given current input parameters (other types of routes are available). * &#x60;noCoverage&#x60;: Routing is not possible due to missing transit information at this time. * &#x60;noStationsFound&#x60;: Routing is not possible due to missing stations in a given range. * &#x60;noAllowedTransitModes&#x60;: All transit modes are excluded in the request.  | [optional] 
**routes** | [**list[TransitRoute]**](TransitRoute.md) | List of possible routes. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


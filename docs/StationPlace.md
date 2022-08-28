# StationPlace

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Location name | [optional] 
**waypoint** | **int** | If present, this place corresponds to the waypoint in the request with the same index. | [optional] 
**type** | **str** | Place type. Each place type can have extra attributes.  **NOTE:** The list of possible place types could be extended in the future. The client application is expected to handle such a case gracefully.  | 
**location** | **AllOfStationPlaceLocation** | The position of this location  This position was used in route calculation. It may be different to the original position provided in the request.  | 
**original_location** | **AllOfStationPlaceOriginalLocation** | If present, the original position of this location provided in the request. | [optional] 
**id** | **str** | Identifier of this station | [optional] 
**platform** | **str** | Platform name or number for the departure. | [optional] 
**code** | **str** | Short text or a number that identifies the place for riders. | [optional] 
**wheelchair_accessible** | **AllOfStationPlaceWheelchairAccessible** | Information about accessibility for people with a disability and who use a wheelchair.  * &#x60;unknown&#x60; - Accessibility information is not available. * &#x60;yes&#x60; - There exists some accessible path from outside the station to the specific stop/platform. * &#x60;limited&#x60; - Accessibility is limited or assistance is required. * &#x60;no&#x60; - There exists no accessible path from outside the station to the specific stop/platform.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# AccessPointPlace

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Location name | [optional] 
**waypoint** | **int** | If present, this place corresponds to the waypoint in the request with the same index. | [optional] 
**type** | **str** | Place type. Each place type can have extra attributes.  **NOTE:** The list of possible place types could be extended in the future. The client application is expected to handle such a case gracefully.  | 
**location** | **AllOfAccessPointPlaceLocation** | The position of this location  This position was used in route calculation. It may be different to the original position provided in the request.  | 
**original_location** | **AllOfAccessPointPlaceOriginalLocation** | If present, the original position of this location provided in the request. | [optional] 
**wheelchair_accessible** | **AllOfAccessPointPlaceWheelchairAccessible** | Information about accessibility for people with a disability and who use a wheelchair.  * &#x60;unknown&#x60; - Accessibility information is not available. * &#x60;yes&#x60; - Access point is wheelchair accessible. * &#x60;limited&#x60; - Accessibility is limited or assistance is required. * &#x60;no&#x60; - No accessible path from the access point to platforms.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


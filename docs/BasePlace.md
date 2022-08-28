# BasePlace

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Location name | [optional] 
**waypoint** | **int** | If present, this place corresponds to the waypoint in the request with the same index. | [optional] 
**type** | **str** | Place type. Each place type can have extra attributes.  **NOTE:** The list of possible place types could be extended in the future. The client application is expected to handle such a case gracefully.  | 
**location** | **AllOfBasePlaceLocation** | The position of this location  This position was used in route calculation. It may be different to the original position provided in the request.  | 
**original_location** | **AllOfBasePlaceOriginalLocation** | If present, the original position of this location provided in the request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


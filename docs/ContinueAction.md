# ContinueAction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The type of the action.  **NOTE:** The list of possible actions may be extended in the future. The client application should handle such a case gracefully.  | 
**duration** | **AllOfContinueActionDuration** | Estimated duration of this action (in seconds). Actions last until the next action, or the end of the route in case of the last one. | 
**instruction** | **str** | Description of the action (e.g. Turn left onto Minna St.). | [optional] 
**offset** | **int** | Offset of a coordinate in the section&#x27;s polyline. | [optional] 
**length** | **AllOfContinueActionLength** | Estimated length of this action (in meters). Actions extend until the next action, or the end of the route in case of the last one. | [optional] 
**current_road** | **AllOfContinueActionCurrentRoad** | Attributes of the current road | [optional] 
**next_road** | **AllOfContinueActionNextRoad** | Attributes of the next road | [optional] 
**exit_sign** | **AllOfContinueActionExitSign** | Attributes of the road exit | [optional] 
**intersection_name** | [**list[LocalizedString]**](LocalizedString.md) | Name of the intersection where the turn takes place, if available. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


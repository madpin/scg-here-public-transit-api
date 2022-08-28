# ChargingAction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The type of the action.  **NOTE:** The list of possible actions may be extended in the future. The client application should handle such a case gracefully.  | 
**duration** | **AllOfChargingActionDuration** | Estimated duration of this action (in seconds). Actions last until the next action, or the end of the route in case of the last one. | 
**instruction** | **str** | Description of the action (e.g. Turn left onto Minna St.). | [optional] 
**consumable_power** | **float** | Maximum charging power (in kW) available to the vehicle, based on the properties of the charging station and the vehicle.  | [optional] 
**arrival_charge** | **float** | Estimated vehicle battery charge before this action (in kWh).  | [optional] 
**target_charge** | **float** | Level to which vehicle battery should be charged by this action (in kWh).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


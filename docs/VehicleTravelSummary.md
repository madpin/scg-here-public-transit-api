# VehicleTravelSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | [**Duration**](Duration.md) |  | 
**length** | [**Distance**](Distance.md) |  | 
**consumption** | [**Energy**](Energy.md) |  | [optional] 
**base_duration** | **AllOfVehicleTravelSummaryBaseDuration** | Duration (in seconds) ignoring time-aware information.  In particular, dynamic traffic information is not taken into account. Only average free-flow speeds based on historical traffic are used to calculate this duration.  The &#x60;baseDuration&#x60; can also be understood as the best possible duration.  | [optional] 
**typical_duration** | **AllOfVehicleTravelSummaryTypicalDuration** | Duration (in seconds) under typical traffic conditions.  In particular, dynamic traffic information is not taken into account. Instead, speeds that are typical for the given time of day/day of week based on historical traffic are used to calculate this duration.  | [optional] 
**ml_duration** | **AllOfVehicleTravelSummaryMlDuration** | Duration (in seconds) based on the region-specific machine learning model.  &#x60;mlDuration&#x60; is calculated for each route section of the route. If a section of the route is not supported, &#x60;mlDuration&#x60; is not present in the summary of that section and a notice with the reason is provided. &#x60;mlDuration&#x60; is only calculated for the entire section. The sum of span durations is not equivalent to &#x60;mlDuration&#x60;.  | [optional] 
**tolls** | [**TollSummary**](TollSummary.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


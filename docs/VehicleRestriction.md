# VehicleRestriction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Detail title | [optional] 
**cause** | **str** | Cause of the notice | [optional] 
**type** | **str** | Detail type. Each type of detail might contain extra attributes.  **NOTE:** The list of possible detail types may be extended in the future. The client application is expected to handle such a case gracefully.  | 
**forbidden_hazardous_goods** | [**list[HazardousGoodsRestriction]**](HazardousGoodsRestriction.md) | Hazardous goods restrictions applied during the trip.  This condition is met when the vehicle&#x27;s shippedHazardousGoods contains any of the items in this array.  | [optional] 
**max_gross_weight** | **int** | Contains max permitted gross weight, in kilograms.  This condition is met when the vehicle&#x27;s &#x60;grossWeight&#x60; exceeds this value.  | [optional] 
**max_weight_per_axle** | **int** | Contains max permitted weight per axle, in kilograms.  This condition is met when the vehicle&#x27;s &#x60;weightPerAxle&#x60; exceeds this value.  | [optional] 
**max_height** | **int** | Contains max permitted height, in centimeters.  This condition is met when the vehicle&#x27;s &#x60;height&#x60; exceeds this value.  | [optional] 
**max_width** | **int** | Contains max permitted width, in centimeters.  This condition is met when the vehicle&#x27;s &#x60;width&#x60; exceeds this value.  | [optional] 
**max_length** | **int** | Contains max permitted length, in centimeters.  This condition is met when the vehicle&#x27;s &#x60;length&#x60; exceeds this value.  | [optional] 
**axle_count** | **AllOfVehicleRestrictionAxleCount** | Constrains the restriction to trucks with number of axles within specified range.  This condition is met when the vehicle&#x27;s &#x60;axleCount&#x60; is within the range specified.  | [optional] 
**tunnel_category** | **AllOfVehicleRestrictionTunnelCategory** | Specifies the tunnel category used to restrict transport of specific goods.  This condition is met when the value exceeds the tunnel category specified by the vehicle&#x27;s &#x60;tunnelCategory&#x60;  | [optional] 
**time_dependent** | **bool** | Indicates that restriction depends on time.  | [optional] 
**truck_type** | **AllOfVehicleRestrictionTruckType** | Constrains the restriction to a specific type of vehicle.  This condition is met if the &#x60;vehicle[type]&#x60; request parameter matches this value.  | [optional] 
**vehicle_type** | **AllOfVehicleRestrictionVehicleType** | Constrains the restriction to a specific type of vehicle.  This condition is met if the &#x60;vehicle[type]&#x60; request parameter matches this value.  | [optional] 
**trailer_count** | **AllOfVehicleRestrictionTrailerCount** | Constrains the restriction to trucks with number of axles within specified range.  This condition is met when the vehicle&#x27;s &#x60;trailerCount&#x60; is within the range specified.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


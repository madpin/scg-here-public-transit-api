# StationInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notices** | [**list[Notice]**](Notice.md) | Contains a list of issues related to this station.  Follows a list of possible notice codes:  * &#x60;noDepartureInfo&#x60;: Departure information is unavailable or inaccurate for this station/stop.  | [optional] 
**place** | **AllOfStationInfoPlace** | Information about a station or stop. | 
**transports** | [**list[TransitTransport]**](TransitTransport.md) | A list of transit services. | [optional] 
**access_points** | [**list[AccessPointPlace]**](AccessPointPlace.md) | A list of access points | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


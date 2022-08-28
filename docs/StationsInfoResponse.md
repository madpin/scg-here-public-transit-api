# StationsInfoResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notices** | [**list[Notice]**](Notice.md) | Contains a list of issues related to this response.  Follows a list of possible notice codes:  * &#x60;unknownStations&#x60;: The response is incomplete as one or more of the given station IDs were not found. * &#x60;noStationsFound&#x60;: No stations information is available given current input parameters  | [optional] 
**stations** | [**list[StationInfo]**](StationInfo.md) | A list of stations. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


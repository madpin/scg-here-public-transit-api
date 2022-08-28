# TollCost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**toll_system** | **str** | Name of the toll system collecting the toll.  | 
**toll_system_ref** | **int** | Reference index of the affected toll system in the &#x60;tollSystems&#x60; array.  | 
**country_code** | [**CountryCode**](CountryCode.md) |  | [optional] 
**toll_collection_locations** | [**list[TollCollectionLocation]**](TollCollectionLocation.md) | Information about the location(s) of the toll places where the fare is collected. In case of entry/exit tolls measured by distance, both entry and exit toll locations are returned. Note that since payment is at only one of these places (normally the exit), the other place *may* be in an unrelated section.  | [optional] 
**fares** | [**list[Fare]**](Fare.md) | List of possible &#x60;Fare&#x60;s to pay, which may depend on time of day, payment method, vehicle characteristics, etc.  **Note**: The router presents only options relevant to the original query, on a best effort basis. Note that a &#x60;Fare&#x60; for tolls is always a &#x60;SinglePrice&#x60;.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


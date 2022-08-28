# RoadInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RoadInfoType**](RoadInfoType.md) |  | [optional] 
**name** | [**list[LocalizedString]**](LocalizedString.md) | Name of the road  If the road has multiple names, each name will be a separate entry in the array. The road names can be in multiple languages. If a preferred language was provided, and names in that language are available, they will be prioritized in the array. Otherwise the default name of the street is prioritized.  | [optional] 
**number** | [**list[LocalizedString]**](LocalizedString.md) | Route name or number (e.g. &#x27;M25&#x27;) | [optional] 
**toward** | [**list[LocalizedString]**](LocalizedString.md) | Names of destinations on sign which can be reached when going in that direction | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


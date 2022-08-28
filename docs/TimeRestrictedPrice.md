# TimeRestrictedPrice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of price represented by this object. The API customer is responsible for correctly visualizing the pricing model. As it is possible to extend the supported price types in the future, the price information should be hidden when an unknown type is encountered.  Available price types are:    * &#x60;restricted&#x60; - A single price value valid for a specific time or duration  | 
**estimated** | **bool** | Attribute value is &#x60;true&#x60; if the fare price is estimated, &#x60;false&#x60; if it is an exact value. | [optional] [default to False]
**currency** | **str** | Local currency of the price compliant to ISO 4217 | 
**unit** | **AllOfTimeRestrictedPriceUnit** | When set, the price is paid for a specific duration.  Examples:   * &#x60;\&quot;unit\&quot;: 3600&#x60; - price for one hour   * &#x60;\&quot;unit\&quot;: 28800&#x60; - price for 8 hours   * &#x60;\&quot;unit\&quot;: 86400&#x60; - price for one day  | [optional] 
**value** | **float** | The price value | 
**days** | [**list[TimeRestrictedWeekdays]**](TimeRestrictedWeekdays.md) | This price applies only for the selected days | [optional] 
**min_duration** | **AllOfTimeRestrictedPriceMinDuration** | The price applies if the duration is more or equal to &#x60;minDuration&#x60; | [optional] 
**max_duration** | **AllOfTimeRestrictedPriceMaxDuration** | The price applies if the duration is less or equal to &#x60;maxDuration&#x60; | [optional] 
**from_time** | **AllOfTimeRestrictedPriceFromTime** | The price applies from this time of the day | [optional] 
**to_time** | **AllOfTimeRestrictedPriceToTime** | The price applies until this time of the day | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


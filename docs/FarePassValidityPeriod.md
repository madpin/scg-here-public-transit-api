# FarePassValidityPeriod

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **str** | Extensible enum: &#x60;annual&#x60; &#x60;extendedAnnual&#x60; &#x60;minutes&#x60; &#x60;days&#x60; &#x60;months&#x60; &#x60;...&#x60;   Specifies one of the following validity periods:   - &#x60;annual&#x60;: pass is valid from Jan 1 to Dec 31   - &#x60;extendedAnnual&#x60;: pass is valid from Jan 1 to Jan 31 of the following year   - &#x60;minutes&#x60;: pass is valid for a specified number of minutes See &#x60;unit&#x60;.   - &#x60;days&#x60;: pass is valid for a specified number of days. See &#x60;unit&#x60;.   - &#x60;months&#x60;: pass is valid for a specified number of months. See &#x60;unit&#x60;.  | 
**count** | **int** | Required if period is &#x60;minutes&#x60;, days&#x60; or &#x60;months&#x60;, it specifies how many of these units are covered by the pass. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


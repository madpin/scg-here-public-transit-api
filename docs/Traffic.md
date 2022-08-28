# Traffic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**override_flow_duration** | **int** | Duration in seconds for which flow traffic event would be considered valid. While flow traffic event is valid it will be used over the historical traffic data.  **Note**: Flow traffic represents congestion not caused by any long-term incidents. State of the flow traffic often changes fast. The farther away from the current time we move, the less precise current flow traffic data will be and the more precise historical traffic data becomes. That&#x27;s why it&#x27;s advised not to use this parameter unless you know what you want to achieve and use the default behavior which is almost always better.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


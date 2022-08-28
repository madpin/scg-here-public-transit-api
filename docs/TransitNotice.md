# TransitNotice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Human-readable notice description. | [optional] 
**code** | **str** | Extensible enum: &#x60;noSchedule&#x60; &#x60;noIntermediate&#x60; &#x60;unwantedMode&#x60; &#x60;scheduledTimes&#x60; &#x60;simplePolyline&#x60; &#x60;violatedAvoidFerry&#x60; &#x60;violatedAvoidTrainFerry&#x60; &#x60;...&#x60;   Currently known codes (non-exhaustive: this list could be extended for new situations):  | Code      | Description  | Severity | | ------            | ------- | ------- | | noSchedule | A timetable schedule is not available for the transit line in this section, and only the run frequency is available. As a result, departure/arrival times are approximated | info | | noIntermediate | Information about intermediate stops is not available for this transit line | info | | unwantedMode | This section contains a transport mode that was explicitly disabled. Mode filtering is not available in this area | info | | scheduledTimes | The times returned on this section are the scheduled times even though delay information are available | info | | simplePolyline | An accurate polyline is not available for this section. The returned polyline has been generated from departure and arrival places | info | | violatedAvoidFerry | Route did not manage to avoid user preference | critical | | violatedAvoidTrainFerry | Route did not manage to avoid user preference | critical |  | 
**severity** | [**NoticeSeverity**](NoticeSeverity.md) |  | [optional] 
**details** | [**list[BaseNoticeDetail]**](BaseNoticeDetail.md) | Additional details about the notice | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


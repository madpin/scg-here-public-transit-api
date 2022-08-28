# PedestrianNotice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Human-readable notice description. | [optional] 
**code** | **str** | Extensible enum: &#x60;simplePolyline&#x60; &#x60;pedestrianOptionViolated&#x60; &#x60;violatedAvoidTunnel&#x60; &#x60;violatedAvoidDirtRoad&#x60; &#x60;...&#x60;   Currently known codes (non-exhaustive: this list could be extended for new situations):  | Code      | Description  | Severity | | --------- | ------- | ----            | | simplePolyline | An accurate polyline is not available for this section. The returned polyline has been generated from departure and arrival places | info | | pedestrianOptionViolated | This section violates the parameter &#x60;pedestrian[speed]&#x60; or &#x60;pedestrian[maxDistance]&#x60; | critical | | violatedAvoidTunnel | Route did not manage to avoid user preference | critical | | violatedAvoidDirtRoad | Route did not manage to avoid user preference | critical |  | 
**severity** | [**NoticeSeverity**](NoticeSeverity.md) |  | [optional] 
**details** | [**list[BaseNoticeDetail]**](BaseNoticeDetail.md) | Additional details about the notice | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


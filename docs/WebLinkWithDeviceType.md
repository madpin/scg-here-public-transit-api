# WebLinkWithDeviceType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the web link. It is used to deduplicate links defined in multiple sections. | 
**href** | [**Uri**](Uri.md) |  | [optional] 
**text** | **str** | Text describing the url address (e.g. The example website). | 
**href_text** | **str** | The interactive (or clickable) portion of the text. If not present (default), the entire content of the text attribute will be considered.  | [optional] 
**device_type** | **str** | Extensible enum: &#x60;web&#x60; &#x60;ios&#x60; &#x60;android&#x60; &#x60;...&#x60;   Device type for which the link is intended  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


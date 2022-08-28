# AvoidPost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segments** | **list[str]** | An array of segment identifiers that routes will avoid going through.  Each entry has the following structure: &#x60;{segmentId}(#{direction})?&#x60;  The individual parts are: * segmentId: The identifier of the referenced topology segment inside the catalog, example: &#x60;here:cm:segment:207551710&#x60; * direction (optional): Either &#x27;*&#x27; for bidirectional (default), &#x27;+&#x27; for positive direction, or &#x27;-&#x27; for negative direction  Example of a parameter value excluding two segments: &#x60;[\&quot;here:cm:segment:207551710#+\&quot;, \&quot;here:cm:segment:76771992#*\&quot;]&#x60;  **Note**: Maximum amount of penalized segments in one request should not be grater than 250.           A \&quot;penalized segments\&quot; refers to segments that have a restrictions on maximum baseSpeed with &#x60;maxSpeedOnSegment&#x60;           or avoided with &#x60;avoid[segments]&#x60;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


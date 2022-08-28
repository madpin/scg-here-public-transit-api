# RoutingZone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** | A reference to a routing zone in HMC.  The standard representation of a routing zone reference has the following structure: &#x60;{catalogHrn}:{catalogVersion}:({layerId})?:{tileId}:{zoneId}&#x60;  The individual parts are: * &#x60;catalogHrn&#x60;: The HERE Resource Name that identifies the source catalog of the routing zone, example: &#x60;hrn:here:data::olp-here:rib-2&#x60; * &#x60;catalogVersion&#x60;: The catalog version * &#x60;layerId&#x60; (optional): The layer inside the catalog where the routing zone is located, example: &#x60;environmental-zones&#x60; * &#x60;tileId&#x60;: The HERE tile key of the partition/tile where the routing zone is located in the given version of the catalog * &#x60;zoneId&#x60;: The identifier of the referenced routing zone within the catalog, example: &#x60;here:cm:envzone:3455277&#x60;  Example of a reference to an environmental zone in standard form: &#x60;hrn:here:data::olp-here:rib-2:1557:environmental-zones:all:here:cm:envzone:3455277&#x60;  In order to reduce reponse size, routing zone references can also be provided in a compact representation. In compact form, parts of a reference are replaced by placeholders, which can be resolved using the &#x60;refReplacements&#x60; dictionary in the parent section. The placeholder format is &#x60;\\$\\d+&#x60; and needs to be surrounded by columns or string start/end. It can be captured with the following regular expression: &#x60;(^|:)\\$\\d+(:|$)&#x60;  Example of the aforementioned environmental zone reference in compact form: &#x60;$0:$1:3455277&#x60; With the corresponding &#x60;refReplacements&#x60;: &#x60;&#x60;&#x60; \&quot;refReplacements\&quot;: {   \&quot;0\&quot;: \&quot;hrn:here:data::olp-here:rib-2:1557\&quot;,   \&quot;1\&quot;: \&quot;environmental-zones:all:here:cm:envzone\&quot; } &#x60;&#x60;&#x60;  | [optional] 
**type** | **str** | Extensible enum: &#x60;environmental&#x60; &#x60;vignette&#x60; &#x60;...&#x60;   The type of a routing zone.  | [optional] 
**name** | **str** | The routing zone&#x27;s name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

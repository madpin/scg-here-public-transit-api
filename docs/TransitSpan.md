# TransitSpan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | Offset of a coordinate in the section&#x27;s polyline.  | [optional] 
**length** | [**Distance**](Distance.md) |  | [optional] 
**duration** | [**Duration**](Duration.md) |  | [optional] 
**country_code** | [**CountryCode**](CountryCode.md) |  | [optional] 
**names** | [**list[LocalizedString]**](LocalizedString.md) | Designated name for the span (e.g. a street name or a transport name) | [optional] 
**segment_id** | **str** | **Disclaimer: This property is currently in beta release, and is therefore subject to breaking changes.**  The directed topology segment id including prefix (e.g &#x27;+here:cm:segment:&#x27;).  The id consists of two parts. * The direction (&#x27;+&#x27; or &#x27;-&#x27;) * followed by the topology segment id (a unique identifier within the HERE platform catalogs).  The direction specifies whether the route is using the segment in its canonical direction (&#x27;+&#x27; aka traveling along the geometry&#x27;s direction), or against it (&#x27;-&#x27; aka traveling against the geometry&#x27;s direction).  This attribute will not appear for HERE Public Transit v8 and HERE Intermodal Routing v8 requests  | [optional] 
**segment_ref** | **str** | A reference to the HMC topology segment used in this span.  The standard representation of a segment reference has the following structure: {catalogHrn}:{catalogVersion}:({layerId})?:{tileId}:{segmentId}(#{direction}({startOffset}..{endOffset})?)?  The individual parts are: * catalogHrn: The HERE Resource Name that identifies the source catalog of the segment, example: hrn:here:data::olp-here:rib-2 * catalogVersion: The catalog version * layerId (optional): The layer inside the catalog where the segment can be found, example: topology-geometry * tileId: The HERE tile key of the partition/tile where the segment is located in the given version of the catalog. This can be on a lower level than the actual segment is stored at (for example, the provided tile ID can be on level 14, despite topology-geometry partitions being tiled at level 12). The level of a HERE tile key is indicated by the position of the highest set bit in binary representation. Since the HERE tile key represents a morton code of the x and y portion of the Tile ID, the level 12 tile ID can be retrieved from the level 14 tile ID by removing the 4 least significant bits (or 2 bits per level) or 1 hexidecimal digit. For example, the level 14 tile 377894441 is included in the level 12 tile 23618402 (377894441&lt;sub&gt;10&lt;/sub&gt; &#x3D; 16863629&lt;sub&gt;16&lt;/sub&gt; &amp;rightarrow; 1686362&lt;sub&gt;16&lt;/sub&gt; &#x3D; 23618402&lt;sub&gt;10&lt;/sub&gt;) * segmentId: The identifier of the referenced topology segment inside the catalog, example: here:cm:segment:84905195 * direction (optional): Either &#x27;*&#x27; for undirected or bidirectional, &#x27;+&#x27; for positive direction, &#x27;-&#x27; for negative direction, or &#x27;?&#x27; for unknown direction (not used by the routing service) * startOffset/endOffset (optional): The start- and end offset are non-negative numbers between 0 and 1, representing the start and end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments). Example: 0.7..1  This attribute will not appear for HERE Public Transit v8 and HERE Intermodal Routing v8 requests  Example of a segment reference in standard representation: hrn:here:data::olp-here:rib-2:1363::377894441:here:cm:segment:84905195#+0.7..1  The segment references can also be provided in a compact representation, to reduce the response size. In the compact representation, some parts are replaced by placeholders, which can be resolved using the refReplacements dictionary in the parent section. The placeholder format is \\$\\d+ and need to be surrounded by columns or string start/end. It can be captured with the following regular expression: (^|:)\\$\\d+(:|$)  Example of the segment reference previously mentioned in compact representation: $0:377894441:$1:84905195#+0.7..1 With the corresponding refReplacements: \&quot;refReplacements\&quot;: {   \&quot;0\&quot;: \&quot;hrn:here:data::olp-here:rib-2:1363:\&quot;,   \&quot;1\&quot;: \&quot;here:cm:segment\&quot; }  | [optional] 
**ref_replacements** | **dict(str, str)** | Dictionary of placeholders to replacement strings for the compact representation of map entity references.  This attribute will not appear for HERE Public Transit v8 and HERE Intermodal Routing v8 requests  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

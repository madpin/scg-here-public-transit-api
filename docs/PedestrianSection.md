# PedestrianSection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the section | 
**type** | **str** | Section type used by the client to identify what extension to the BaseSection are available. | 
**pre_actions** | [**list[BaseAction]**](BaseAction.md) | Actions that must be done prior to &#x60;departure&#x60;. | [optional] 
**actions** | [**list[PedestrianAction]**](PedestrianAction.md) | Actions to be performed at or during a specific portion of a section.  Action offsets are the coordinate index in the polyline.  *NOTE:* currentRoad and nextRoad are not populated for actions.  | [optional] 
**language** | **str** | Language of the localized strings in the section, if any, in BCP47 format. | [optional] 
**post_actions** | [**list[PedestrianPostAction]**](PedestrianPostAction.md) | Actions that must be done after &#x60;arrival&#x60;. | [optional] 
**turn_by_turn_actions** | [**list[OffsetAction]**](OffsetAction.md) | Actions for turn by turn guidance during the travel portion of the section, i.e., between &#x60;departure&#x60; and &#x60;arrival&#x60;. | [optional] 
**departure** | [**PedestrianDeparture**](PedestrianDeparture.md) |  | 
**arrival** | [**PedestrianDeparture**](PedestrianDeparture.md) |  | 
**passthrough** | [**list[Passthrough]**](Passthrough.md) | List of via waypoints this section is passing through.  Each via waypoint of the request that is a &#x60;passThrough&#x3D;true&#x60; waypoint, appears as a &#x60;Passthrough&#x60; in the response. It appears in the section that starts with the closest non-passthrough via specified before it or origin.  The passthrough vias appear in this list in the order they are traversed. They are traversed in the order they are specified in the request.  | [optional] 
**summary** | **AllOfPedestrianSectionSummary** | Total value of key attributes (e.g. duration, length) summed up for the entire section, including &#x60;preActions&#x60;, &#x60;postActions&#x60;, and the travel portion of the section.  | [optional] 
**travel_summary** | **AllOfPedestrianSectionTravelSummary** | Total value of key attributes (e.g., duration, length) summed up for just the travel portion of the section, between &#x60;departure&#x60; and &#x60;arrival&#x60;. &#x60;preActions&#x60; and &#x60;postActions&#x60; are excluded.  | [optional] 
**polyline** | [**Polyline**](Polyline.md) |  | [optional] 
**notices** | [**list[PedestrianNotice]**](PedestrianNotice.md) | Contains a list of issues related to this section of the route.  | [optional] 
**transport** | [**PedestrianTransport**](PedestrianTransport.md) |  | 
**spans** | [**list[PedestrianSpan]**](PedestrianSpan.md) | Spans attached to a &#x60;Section&#x60; describing pedestrian content.  | [optional] 
**ref_replacements** | **dict(str, str)** | Dictionary of placeholders to replacement strings for the compact representation of map entity references.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


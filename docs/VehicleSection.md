# VehicleSection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the section | 
**type** | **str** | Section type used by the client to identify what extension to the BaseSection are available. | 
**pre_actions** | [**list[BaseAction]**](BaseAction.md) | Actions that must be done prior to &#x60;departure&#x60;. | [optional] 
**actions** | [**list[VehicleAction]**](VehicleAction.md) | Actions to be performed at or during a specific portion of a section.  Action offsets are the coordinate index in the polyline.  *NOTE:* currentRoad and nextRoad are not populated for actions.  | [optional] 
**language** | **str** | Language of the localized strings in the section, if any, in BCP47 format. | [optional] 
**post_actions** | [**list[VehiclePostAction]**](VehiclePostAction.md) | Actions that must be done after &#x60;arrival&#x60;. | [optional] 
**turn_by_turn_actions** | [**list[VehicleAction]**](VehicleAction.md) | Actions for turn by turn guidance.  Action offsets are the coordinate index in the polyline.  | [optional] 
**departure** | [**VehicleDeparture**](VehicleDeparture.md) |  | 
**arrival** | [**VehicleDeparture**](VehicleDeparture.md) |  | 
**passthrough** | [**list[Passthrough]**](Passthrough.md) | List of via waypoints this section is passing through.  Each via waypoint of the request that is a &#x60;passThrough&#x3D;true&#x60; waypoint, appears as a &#x60;Passthrough&#x60; in the response. It appears in the section that starts with the closest non-passthrough via specified before it or origin.  The passthrough vias appear in this list in the order they are traversed. They are traversed in the order they are specified in the request.  | [optional] 
**summary** | **AllOfVehicleSectionSummary** | Total value of key attributes (e.g., duration, length, consumption) summed up for the entire section, including &#x60;preActions&#x60;, &#x60;postActions&#x60;, and the travel portion of the section.  | [optional] 
**travel_summary** | **AllOfVehicleSectionTravelSummary** | Total value of key attributes (e.g., duration, length, consumption) summed up for just the travel portion of the section, between &#x60;departure&#x60; and &#x60;arrival&#x60;. &#x60;preActions&#x60; and &#x60;postActions&#x60; are excluded.  | [optional] 
**polyline** | [**Polyline**](Polyline.md) |  | [optional] 
**notices** | [**list[VehicleNotice]**](VehicleNotice.md) | Contains a list of issues related to this section of the route.  Notices must be carefully evaluated and the route section should be discarded if appropriate. In particular, the user should be aware that new notice codes may be added at any time. If an unrecognized notice code appears with a &#x60;critical&#x60; severity level, the route section must be discarded. Please refer to the &#x60;code&#x60; attribute for possible values.  | [optional] 
**spans** | [**list[VehicleSpan]**](VehicleSpan.md) | Spans attached to a &#x60;Section&#x60; describing vehicle content.  | [optional] 
**routing_zones** | [**list[RoutingZone]**](RoutingZone.md) | A list of routing zones that are applicable to the section.  Elements of this list will be referenced by indices within the &#x60;span&#x60; attribute of the section.  | [optional] 
**truck_road_types** | **list[str]** | A list of truck road types that are applicable to the section.  Elements of this list will be referenced by indices within the &#x60;span&#x60; attribute of the section.  A truck road type is an identifier associated with roads that have additional regulations applied by local administration for traversal by heavy vehicles like trucks. For example, the BK Bearing Class regulations in Sweden, and ET categories in Mexico. The identifiers of supported truck road types are specified at HERE Map Content [TruckRoadType](https://developer.here.com/documentation/here-map-content/dev_guide/topics_schema/truckroadtypeattribute.truckroadtype.html).  These names should be provided when avoiding a certain truck road type.  | [optional] 
**incidents** | [**list[TrafficIncident]**](TrafficIncident.md) | A list of all incidents that apply to the section. | [optional] 
**ref_replacements** | **dict(str, str)** | Dictionary of placeholders to replacement strings for the compact representation of map entity references.  | [optional] 
**toll_systems** | [**list[TollSystem]**](TollSystem.md) | An array of toll authorities that collect payments for the use of (part of) this section of the route.  | [optional] 
**tolls** | [**list[TollCost]**](TollCost.md) | Detail of tolls to be paid for traversing this section.  | [optional] 
**transport** | [**VehicleTransport**](VehicleTransport.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


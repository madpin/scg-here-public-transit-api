# TransitSection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the section | 
**type** | **str** | Section type used by the client to identify what extension to the BaseSection are available. | 
**pre_actions** | [**list[TransitPreAction]**](TransitPreAction.md) | Actions that must be done prior to &#x60;departure&#x60;. | [optional] 
**actions** | [**list[OffsetAction]**](OffsetAction.md) | Actions that must be done during the travel portion of the section, i.e., between &#x60;departure&#x60; and &#x60;arrival&#x60;.  *NOTE:* currentRoad and nextRoad are not populated for actions.  | [optional] 
**language** | **str** | Language of the localized strings in the section, if any, in BCP47 format. | [optional] 
**post_actions** | [**list[TransitPostAction]**](TransitPostAction.md) | Actions that must be done after &#x60;arrival&#x60;. | [optional] 
**turn_by_turn_actions** | [**list[OffsetAction]**](OffsetAction.md) | Actions for turn by turn guidance during the travel portion of the section, i.e., between &#x60;departure&#x60; and &#x60;arrival&#x60;. | [optional] 
**departure** | [**TransitDeparture**](TransitDeparture.md) |  | 
**arrival** | [**TransitDeparture**](TransitDeparture.md) |  | 
**passthrough** | [**list[Passthrough]**](Passthrough.md) | List of via waypoints this section is passing through.  Each via waypoint of the request that is a &#x60;passThrough&#x3D;true&#x60; waypoint, appears as a &#x60;Passthrough&#x60; in the response. It appears in the section that starts with the closest non-passthrough via specified before it or origin.  The passthrough vias appear in this list in the order they are traversed. They are traversed in the order they are specified in the request.  | [optional] 
**summary** | **AllOfTransitSectionSummary** | Total value of key attributes (e.g., duration, length) summed up for the entire section, including &#x60;preActions&#x60;, &#x60;postActions&#x60;, and the travel portion of the section.  | [optional] 
**travel_summary** | **AllOfTransitSectionTravelSummary** | Total value of key attributes (e.g., duration, length) summed up for just the travel portion of the section, between &#x60;departure&#x60; and &#x60;arrival&#x60;. &#x60;preActions&#x60; and &#x60;postActions&#x60; are excluded.  | [optional] 
**polyline** | [**Polyline**](Polyline.md) |  | [optional] 
**notices** | [**list[TransitNotice]**](TransitNotice.md) | Contains a list of issues related to this section of the route.  | [optional] 
**booking_links** | [**list[WebLinkWithDeviceType]**](WebLinkWithDeviceType.md) | Links to external ticket booking services | [optional] 
**transport** | [**TransitTransport**](TransitTransport.md) |  | [optional] 
**intermediate_stops** | [**list[TransitStop]**](TransitStop.md) | Intermediate stops between departure and destination of the transit line. It can be missing if this information is not available or not requested.  | [optional] 
**agency** | [**Agency**](Agency.md) |  | [optional] 
**attributions** | [**list[Attribution]**](Attribution.md) | List of required attributions to display. | [optional] 
**fares** | [**list[Fare]**](Fare.md) | List of tickets to pay for this section of the route | [optional] 
**booking** | [**WebLink**](WebLink.md) |  | [optional] 
**spans** | [**list[TransitSpan]**](TransitSpan.md) | Span attached to a &#x60;Section&#x60; describing transit content.  | [optional] 
**incidents** | [**list[TransitIncident]**](TransitIncident.md) | A list of all incidents that apply to the section. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


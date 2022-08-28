# here_public_transit_api.RoutingApi

All URIs are relative to *https://router.hereapi.com/v8*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_routes**](RoutingApi.md#calculate_routes) | **GET** /routes | Calculate routes via GET
[**calculate_routes_post**](RoutingApi.md#calculate_routes_post) | **POST** /routes | Calculate routes via POST
[**get_routes_by_handle**](RoutingApi.md#get_routes_by_handle) | **GET** /routes/{routeHandle} | Get route by handle via GET
[**get_routes_by_handle_post**](RoutingApi.md#get_routes_by_handle_post) | **POST** /routes/{routeHandle} | Get route by handle via POST
[**import_route**](RoutingApi.md#import_route) | **POST** /import | Calculate a route from a sequence of trace points

# **calculate_routes**
> RouterRouteResponse calculate_routes(transport_mode, origin, destination, ev_free_flow_speed_table, via=via, departure_time=departure_time, arrival_time=arrival_time, routing_mode=routing_mode, alternatives=alternatives, avoid_features=avoid_features, avoid_areas=avoid_areas, avoid_segments=avoid_segments, avoid_zone_categories=avoid_zone_categories, avoid_zone_identifiers=avoid_zone_identifiers, avoid_truck_road_types=avoid_truck_road_types, avoid_toll_transponders=avoid_toll_transponders, exclude_countries=exclude_countries, units=units, lang=lang, _return=_return, spans=spans, truck_shipped_hazardous_goods=truck_shipped_hazardous_goods, truck_gross_weight=truck_gross_weight, truck_weight_per_axle=truck_weight_per_axle, truck_weight_per_axle_group=truck_weight_per_axle_group, truck_height=truck_height, truck_width=truck_width, truck_length=truck_length, truck_tunnel_category=truck_tunnel_category, truck_axle_count=truck_axle_count, truck_trailer_axle_count=truck_trailer_axle_count, truck_tires_count=truck_tires_count, truck_category=truck_category, truck_trailer_count=truck_trailer_count, truck_hov_occupancy=truck_hov_occupancy, truck_license_plate=truck_license_plate, truck_speed_cap=truck_speed_cap, truck_type=truck_type, vehicle_shipped_hazardous_goods=vehicle_shipped_hazardous_goods, vehicle_gross_weight=vehicle_gross_weight, vehicle_weight_per_axle=vehicle_weight_per_axle, vehicle_weight_per_axle_group=vehicle_weight_per_axle_group, vehicle_height=vehicle_height, vehicle_width=vehicle_width, vehicle_length=vehicle_length, vehicle_tunnel_category=vehicle_tunnel_category, vehicle_axle_count=vehicle_axle_count, vehicle_trailer_axle_count=vehicle_trailer_axle_count, vehicle_tires_count=vehicle_tires_count, vehicle_category=vehicle_category, vehicle_trailer_count=vehicle_trailer_count, vehicle_hov_occupancy=vehicle_hov_occupancy, vehicle_license_plate=vehicle_license_plate, vehicle_speed_cap=vehicle_speed_cap, vehicle_type=vehicle_type, ev_traffic_speed_table=ev_traffic_speed_table, ev_ascent=ev_ascent, ev_descent=ev_descent, ev_auxiliary_consumption=ev_auxiliary_consumption, ev_initial_charge=ev_initial_charge, ev_max_charge=ev_max_charge, ev_charging_curve=ev_charging_curve, ev_max_charging_voltage=ev_max_charging_voltage, ev_max_charging_current=ev_max_charging_current, ev_max_charge_after_charging_station=ev_max_charge_after_charging_station, ev_min_charge_at_charging_station=ev_min_charge_at_charging_station, ev_min_charge_at_first_charging_station=ev_min_charge_at_first_charging_station, ev_min_charge_at_destination=ev_min_charge_at_destination, ev_charging_setup_duration=ev_charging_setup_duration, ev_connector_types=ev_connector_types, ev_make_reachable=ev_make_reachable, ev_preferred_brands=ev_preferred_brands, pedestrian_speed=pedestrian_speed, x_request_id=x_request_id, scooter_allow_highway=scooter_allow_highway, currency=currency, customizations=customizations, taxi_allow_drive_through_taxi_roads=taxi_allow_drive_through_taxi_roads, tolls_transponders=tolls_transponders, tolls_vignettes=tolls_vignettes, tolls_summaries=tolls_summaries, tolls_vehicle_category=tolls_vehicle_category, tolls_emission_type=tolls_emission_type, max_speed_on_segment=max_speed_on_segment, traffic_override_flow_duration=traffic_override_flow_duration)

Calculate routes via GET

Calculates a route using a generic vehicle/pedestrian mode, e.g. car, truck, pedestrian, etc...

### Example
```python
from __future__ import print_function
import time
import here_public_transit_api
from here_public_transit_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = here_public_transit_api.Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = here_public_transit_api.RoutingApi(here_public_transit_api.ApiClient(configuration))
transport_mode = here_public_transit_api.RouterMode() # RouterMode | Mode of transport to be used for the calculation of the route.  Note: `bus`, `privateBus`, and `taxi` modes are currently provided as Beta, with limited functionality. The API and behaviour may change drastically, or even become unsupported, without warning. Please refer to the developers' guide for more details. 
origin = here_public_transit_api.Waypoint() # Waypoint | A location defining the origin of the trip.  ## Format  Format: `Place[WaypointOptions]`  * Place: `{lat},{lng}[PlaceOptions]` * PlaceOptions: `;option1=value1;option2=value2...` * WaypointOptions: `!option1=value1!option2=value2...`  A waypoint consists of:  * Exactly one place * Optional settings for the place * Optional settings for the waypoint itself  Supported place options:  * `course`: int, degrees clock-wise from north. Indicating desired direction at the place.   E.g. `90` indicating `east`. Often combined with `radius` and/or `minCourseDistance` * `sideOfStreetHint`: `{lat},{lng}`. Indicating the side of the street that should be   used. E.g. if the location is to the left of the street, the router will prefer using   that side in case the street has dividers. E.g.   `52.511496,13.304140;sideOfStreetHint=52.512149,13.304076` indicates that the `north`   side of the street should be preferred. This option is required, if `matchSideOfStreet`   is set to `always`. * `matchSideOfStreet`: enum `[always, onlyIfDivided]`. Specifies how the location set by   `sideOfStreetHint` should be handled. Requires `sideOfStreetHint` to be specified as   well.   + `always` : Always prefer the given side of street.   + `onlyIfDivided`: Only prefer using side of street set by `sideOfStreetHint` in case     the street has dividers. This is the default behavior. * `nameHint`: string. Causes the router to look for the place with the most similar name.   This can e.g. include things like: `North` being used to differentiate between   interstates `I66 North` and `I66 South`, `Downtown Avenue` being used to correctly   select a residental street. * `radius`: int, meters. Asks the router to consider all places within the given radius as   potential candidates for route calculation. This can be either because it is not   important which place is used, or because it is unknown. Radius more than 200meter are   not supported. * `minCourseDistance`: int, meters. Instructs the routing service to try to find a route that avoids actions for the indicated distance.   For example, if the origin is determined by a moving vehicle, the user might not have time to react to early actions. * `customizationIndex`: int. Specifies the zero-based index into the list of customizations   specified in the `customizations` parameter. The customization at that index must be an   Extension Map.   Providing a `customizationIndex` indicates the this waypoint is located within that   Extension Map.   **Alpha**: This customization API parameter is in development. It may not be stable and is subject to change. * `segmentIdHint`: string. Causes the router to try and match to the specified segment.   Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint   This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one. * `onRoadThreshold`: int, meters. allows specifying a distance within which   the waypoint could be considered as being on a highway/bridge/tunnel/sliproad.   Within this threshold, the attributes of the segments do not impact the matching.   Outside the threshold only segments which aren't one of highway/bridge/tunnel/sliproad can be matched.  Notes:  * `stopDuration` option is not supported for `origin`, contrary to `destination` and   `via` waypoints. * `passThrough`: option is not supported for 'origin'. * Non-structural reserved characters in options' values need to be properly percent-encoded.   Please refer to the developers' guide for more details. 
destination = here_public_transit_api.Waypoint() # Waypoint | A location defining the destination of the trip.  ## Format  Format: `Place[WaypointOptions]`  * Place: `{lat},{lng}[PlaceOptions]` * PlaceOptions: `;option1=value1;option2=value2...` * WaypointOptions: `!option1=value1!option2=value2...`  A waypoint consists of:  * Exactly one place * Optional settings for the place * Optional settings for the waypoint itself  Supported place options:  * `course`: int, degrees clock-wise from north. Indicating desired direction at the place.   E.g. `90` indicating `east`. Often combined with `radius` and/or `minCourseDistance` * `sideOfStreetHint`: `{lat},{lng}`. Indicating the side of the street that should be   used. E.g. if the location is to the left of the street, the router will prefer using   that side in case the street has dividers. E.g.   `52.511496,13.304140;sideOfStreetHint=52.512149,13.304076` indicates that the `north`   side of the street should be preferred. This option is required, if `matchSideOfStreet`   is set to `always`. * `matchSideOfStreet`: enum `[always, onlyIfDivided]`. Specifies how the location set by   `sideOfStreetHint` should be handled. Requires `sideOfStreetHint` to be specified as   well.   + `always` : Always prefer the given side of street.   + `onlyIfDivided`: Only prefer using side of street set by `sideOfStreetHint` in case     the street has dividers. This is the default behavior. * `nameHint`: string. Causes the router to look for the place with the most similar name.   This can e.g. include things like: `North` being used to differentiate between   interstates `I66 North` and `I66 South`, `Downtown Avenue` being used to correctly   select a residental street. * `radius`: int, meters. Asks the router to consider all places within the given radius as   potential candidates for route calculation. This can be either because it is not   important which place is used, or because it is unknown. Radius more than 200meter are   not supported. * `minCourseDistance`: int, meters. Instructs the routing service to try to find a route that avoids actions for the indicated distance.   For example, if the origin is determined by a moving vehicle, the user might not have time to react to early actions. * `customizationIndex`: int. Specifies the zero-based index into the list of customizations   specified in the `customizations` parameter. The customization at that index must be an   Extension Map.   Providing a `customizationIndex` indicates the this waypoint is located within that   Extension Map.   **Alpha**: This customization API parameter is in development. It may not be stable and is subject to change. * `segmentIdHint`: string. Causes the router to try and match to the specified segment.   Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint   This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one. * `onRoadThreshold`: int, meters. allows specifying a distance within which   the waypoint could be considered as being on a highway/bridge/tunnel/sliproad.   Within this threshold, the attributes of the segments do not impact the matching.   Outside the threshold only segments which aren't one of highway/bridge/tunnel/sliproad can be matched.  Supported waypoint options:  * `stopDuration`: desired duration for the stop, in seconds. The section arriving at this   via waypoint will have a `wait` post action reflecting the stopping time. The   consecutive section will start at the arrival time of the former section + stop   duration. * `passThrough`: option is not supported for 'destination'.  Notes:  * Non-structural reserved characters in options' values need to be properly percent-encoded.   Please refer to the developers' guide for more details. 
ev_free_flow_speed_table = NULL # object | 
via = [here_public_transit_api.Waypoint()] # list[Waypoint] | A location defining a via waypoint.  A via waypoint is a location between origin and destination. The route will do a stop at the via waypoint.  Multiple waypoints can also be specified using multiple via parameters like `via=...&via=...`, in which case the route will traverse these waypoints sequentially in the order specified in the request.  ## Format  Format: `Place[WaypointOptions]`  * Place: `{lat},{lng}[PlaceOptions]` * PlaceOptions: `;option1=value1;option2=value2...` * WaypointOptions: `!option1=value1!option2=value2...`  A waypoint consists of:  * Exactly one place * Optional settings for the place * Optional settings for the waypoint itself  Supported place options:  * `course`: int, degrees clock-wise from north. Indicating desired direction at the place.   E.g. `90` indicating `east`. Often combined with `radius` and/or `minCourseDistance` * `sideOfStreetHint`: `{lat},{lng}`. Indicating the side of the street that should be   used. E.g. if the location is to the left of the street, the router will prefer using   that side in case the street has dividers. E.g.   `52.511496,13.304140;sideOfStreetHint=52.512149,13.304076` indicates that the `north`   side of the street should be preferred. This option is required, if `matchSideOfStreet`   is set to `always`. * `matchSideOfStreet`: enum `[always, onlyIfDivided]`. Specifies how the location set by   `sideOfStreetHint` should be handled. Requires `sideOfStreetHint` to be specified as   well.   + `always` : Always prefer the given side of street.   + `onlyIfDivided`: Only prefer using side of street set by `sideOfStreetHint` in case     the street has dividers. This is the default behavior. * `nameHint`: string. Causes the router to look for the place with the most similar name.   This can e.g. include things like: `North` being used to differentiate between   interstates `I66 North` and `I66 South`, `Downtown Avenue` being used to correctly   select a residental street. * `radius`: int, meters. Asks the router to consider all places within the given radius as   potential candidates for route calculation. This can be either because it is not   important which place is used, or because it is unknown. Radius more than 200meter are   not supported. * `minCourseDistance`: int, meters. Instructs the routing service to try to find a route that avoids actions for the indicated distance.   For example, if the origin is determined by a moving vehicle, the user might not have time to react to early actions. * `customizationIndex`: int. Specifies the zero-based index into the list of customizations   specified in the `customizations` parameter. The customization at that index must be an   Extension Map.   Providing a `customizationIndex` indicates the this waypoint is located within that   Extension Map.   **Alpha**: This customization API parameter is in development. It may not be stable and is subject to change. * `segmentIdHint`: string. Causes the router to try and match to the specified segment.   Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint   This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one. * `onRoadThreshold`: int, meters. allows specifying a distance within which   the waypoint could be considered as being on a highway/bridge/tunnel/sliproad.   Within this threshold, the attributes of the segments do not impact the matching.   Outside the threshold only segments which aren't one of highway/bridge/tunnel/sliproad can be matched.  Supported waypoint options: * `stopDuration`: desired duration for the stop, in seconds. * `passThrough`: boolean. Asks the router to avoid the following during route calculation:   + Introducing a stop at the waypoint.   + Splitting the route into sections.   + Changing the direction of travel.    Following scenarios are not supported for `passThrough` parameter:   + Setting both `stopDuration` to a value greater than 0 and `passThrough=true`.   + Setting `passThrough=true` for `origin` or `destination` of a route.   The default value is `false`.  Notes:  * Non-structural reserved characters in options' values need to be properly percent-encoded.   Please refer to the developers' guide for more details.  (optional)
departure_time = here_public_transit_api.TimeWithAny() # TimeWithAny | Specifies the time of departure as defined by either `date-time` or `full-date` `T` `partial-time` in `RFC 3339`, section 5.6 (for example, `2019-06-24T01:23:45`).  The requested time is converted to local time at origin. When the optional timezone offset is not specified, time is assumed to be local. The special value `any` can be used to indicate that time should not be taken into account during routing. If neither `departureTime` or `arrivalTime` are specified, current time at departure place will be used. All time values in the response are returned in the timezone of each location.  (optional)
arrival_time = here_public_transit_api.Time() # Time | Specifies the time of arrival as defined by either `date-time` or `full-date` `T` `partial-time` in `RFC 3339`, section 5.6 (for example, `2019-06-24T01:23:45`). The requested time is converted to the local time at destination. When the optional timezone offset is not specified, time is assumed to be local. All `Time` values in the response are returned in the timezone of each location.  Note : The following features do not support the arrivalTime parameter: * EV Routing * Route Handle * Route Import  (optional)
routing_mode = here_public_transit_api.RoutingMode() # RoutingMode | Specifies which optimization is applied during route calculation.  * `fast`: Route calculation from start to destination optimized by travel time. In many   cases, the route returned by the `fast` mode may not be the route with the fastest   possible travel time. For example, the routing service may favor a route that remains on   a highway, even if a faster travel time can be achieved by taking a detour or shortcut   through an inconvenient side road. * `short`: Route calculation from start to destination disregarding any speed information.   In this mode, the distance of the route is minimized, while keeping the route sensible.   This includes, for example, penalizing turns. Because of that, the resulting route will   not necessarily be the one with minimal distance.  Notes: * The following Transport modes only support `fast` routingMode   - `bicycle`   - `bus`   - `pedestrian`   - `privateBus`   - `scooter`   - `taxi`  (optional)
alternatives = 0 # int | Number of alternative routes to return aside from the optimal route. (optional) (default to 0)
avoid_features = 'avoid_features_example' # str |  (optional)
avoid_areas = 'avoid_areas_example' # str |  (optional)
avoid_segments = 'avoid_segments_example' # str |  (optional)
avoid_zone_categories = 'avoid_zone_categories_example' # str |  (optional)
avoid_zone_identifiers = 'avoid_zone_identifiers_example' # str |  (optional)
avoid_truck_road_types = 'avoid_truck_road_types_example' # str |  (optional)
avoid_toll_transponders = 'avoid_toll_transponders_example' # str |  (optional)
exclude_countries = 'exclude_countries_example' # str |  (optional)
units = here_public_transit_api.Units() # Units | Units of measurement used in guidance instructions. The default is `metric`.  (optional)
lang = ['[\"en-US\"]'] # list[str] | Specifies the list of preferred languages of the response. The first supported language from the list will be used for for the response. The value should comply with the [IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). A list of supported languages for the routing service can be found in the dev guide https://developer.here.com/documentation/routing-api/dev_guide/topics/languages.html.  Note: If the first language in the list is not supported, an info notification will be generated with code `mainLanguageNotFound`.  (optional) (default to ["en-US"])
_return = [here_public_transit_api.ModelReturn()] # list[ModelReturn] |  (optional)
spans = [here_public_transit_api.Spans()] # list[Spans] | Defines which map content attributes are included in the response spans. For example, `attributes,length` will enable the fields `attributes` and `length` in the route response. For more information about the `countryCode` field, see https://www.iso.org/obp/ui/#search.  This parameter also requires that the `polyline` option is set within the `return` parameter.  (optional)
truck_shipped_hazardous_goods = 'truck_shipped_hazardous_goods_example' # str |  (optional)
truck_gross_weight = 56 # int |  (optional)
truck_weight_per_axle = 56 # int |  (optional)
truck_weight_per_axle_group = 'truck_weight_per_axle_group_example' # str |  (optional)
truck_height = 56 # int |  (optional)
truck_width = 56 # int |  (optional)
truck_length = 56 # int |  (optional)
truck_tunnel_category = 'truck_tunnel_category_example' # str |  (optional)
truck_axle_count = 56 # int |  (optional)
truck_trailer_axle_count = 56 # int |  (optional)
truck_tires_count = 56 # int |  (optional)
truck_category = 'undefined' # str |  (optional) (default to undefined)
truck_trailer_count = 0 # int |  (optional) (default to 0)
truck_hov_occupancy = 1 # int |  (optional) (default to 1)
truck_license_plate = 'truck_license_plate_example' # str |  (optional)
truck_speed_cap = 1.2 # float |  (optional)
truck_type = 'straight' # str |  (optional) (default to straight)
vehicle_shipped_hazardous_goods = 'vehicle_shipped_hazardous_goods_example' # str |  (optional)
vehicle_gross_weight = 56 # int |  (optional)
vehicle_weight_per_axle = 56 # int |  (optional)
vehicle_weight_per_axle_group = 'vehicle_weight_per_axle_group_example' # str |  (optional)
vehicle_height = 56 # int |  (optional)
vehicle_width = 56 # int |  (optional)
vehicle_length = 56 # int |  (optional)
vehicle_tunnel_category = 'vehicle_tunnel_category_example' # str |  (optional)
vehicle_axle_count = 56 # int |  (optional)
vehicle_trailer_axle_count = 56 # int |  (optional)
vehicle_tires_count = 56 # int |  (optional)
vehicle_category = 'undefined' # str |  (optional) (default to undefined)
vehicle_trailer_count = 0 # int |  (optional) (default to 0)
vehicle_hov_occupancy = 1 # int |  (optional) (default to 1)
vehicle_license_plate = 'vehicle_license_plate_example' # str |  (optional)
vehicle_speed_cap = 1.2 # float |  (optional)
vehicle_type = 'vehicle_type_example' # str |  (optional)
ev_traffic_speed_table = NULL # object |  (optional)
ev_ascent = 1.2 # float |  (optional)
ev_descent = 1.2 # float |  (optional)
ev_auxiliary_consumption = 1.2 # float |  (optional)
ev_initial_charge = 1.2 # float |  (optional)
ev_max_charge = 1.2 # float |  (optional)
ev_charging_curve = 'ev_charging_curve_example' # str |  (optional)
ev_max_charging_voltage = 1.2 # float |  (optional)
ev_max_charging_current = 1.2 # float |  (optional)
ev_max_charge_after_charging_station = 1.2 # float |  (optional)
ev_min_charge_at_charging_station = 1.2 # float |  (optional)
ev_min_charge_at_first_charging_station = 1.2 # float |  (optional)
ev_min_charge_at_destination = 1.2 # float |  (optional)
ev_charging_setup_duration = 56 # int |  (optional)
ev_connector_types = 'ev_connector_types_example' # str |  (optional)
ev_make_reachable = true # bool |  (optional)
ev_preferred_brands = 'ev_preferred_brands_example' # str |  (optional)
pedestrian_speed = here_public_transit_api.PedestrianSpeed() # PedestrianSpeed | **Disclaimer: This parameter is currently in beta release, and is therefore subject to breaking changes. The parameter could be extracted to a separate API if speed capping for cars/trucks is introduced** Walking speed in meters per second. Influences the duration of walking segments along the route.  (optional)
x_request_id = 'x_request_id_example' # str | User-provided token that can be used to trace a request or a group of requests sent to the service. (optional)
scooter_allow_highway = false # bool |  (optional) (default to false)
currency = 'currency_example' # str | Currency code compliant to ISO 4217. Costs for the calculated route will be returned using this currency.  If not provided, the router will specify it. On a best-effort basis, the router will try to specify the costs in the local currency.  (optional)
customizations = [here_public_transit_api.CustomizationHRN()] # list[CustomizationHRN] | Specifies a list of customizations to be used. The data provided by these customizations either replaces or augments the standard HERE map data. The provided credentials must authorize access to all of the customizations specified.  **Alpha**: This API is in development. It may not be stable and is subject to change.  (optional)
taxi_allow_drive_through_taxi_roads = true # bool |  (optional) (default to true)
tolls_transponders = 'tolls_transponders_example' # str |  (optional)
tolls_vignettes = 'tolls_vignettes_example' # str |  (optional)
tolls_summaries = ['tolls_summaries_example'] # list[str] |  (optional)
tolls_vehicle_category = 'tolls_vehicle_category_example' # str |  (optional)
tolls_emission_type = 'tolls_emission_type_example' # str |  (optional)
max_speed_on_segment = here_public_transit_api.MaxSpeedOnSegment() # MaxSpeedOnSegment | Specify new base speed for segment by value. Affects route selection and the ETA. Cannot increase base speed on segment.  (optional)
traffic_override_flow_duration = 56 # int |  (optional)

try:
    # Calculate routes via GET
    api_response = api_instance.calculate_routes(transport_mode, origin, destination, ev_free_flow_speed_table, via=via, departure_time=departure_time, arrival_time=arrival_time, routing_mode=routing_mode, alternatives=alternatives, avoid_features=avoid_features, avoid_areas=avoid_areas, avoid_segments=avoid_segments, avoid_zone_categories=avoid_zone_categories, avoid_zone_identifiers=avoid_zone_identifiers, avoid_truck_road_types=avoid_truck_road_types, avoid_toll_transponders=avoid_toll_transponders, exclude_countries=exclude_countries, units=units, lang=lang, _return=_return, spans=spans, truck_shipped_hazardous_goods=truck_shipped_hazardous_goods, truck_gross_weight=truck_gross_weight, truck_weight_per_axle=truck_weight_per_axle, truck_weight_per_axle_group=truck_weight_per_axle_group, truck_height=truck_height, truck_width=truck_width, truck_length=truck_length, truck_tunnel_category=truck_tunnel_category, truck_axle_count=truck_axle_count, truck_trailer_axle_count=truck_trailer_axle_count, truck_tires_count=truck_tires_count, truck_category=truck_category, truck_trailer_count=truck_trailer_count, truck_hov_occupancy=truck_hov_occupancy, truck_license_plate=truck_license_plate, truck_speed_cap=truck_speed_cap, truck_type=truck_type, vehicle_shipped_hazardous_goods=vehicle_shipped_hazardous_goods, vehicle_gross_weight=vehicle_gross_weight, vehicle_weight_per_axle=vehicle_weight_per_axle, vehicle_weight_per_axle_group=vehicle_weight_per_axle_group, vehicle_height=vehicle_height, vehicle_width=vehicle_width, vehicle_length=vehicle_length, vehicle_tunnel_category=vehicle_tunnel_category, vehicle_axle_count=vehicle_axle_count, vehicle_trailer_axle_count=vehicle_trailer_axle_count, vehicle_tires_count=vehicle_tires_count, vehicle_category=vehicle_category, vehicle_trailer_count=vehicle_trailer_count, vehicle_hov_occupancy=vehicle_hov_occupancy, vehicle_license_plate=vehicle_license_plate, vehicle_speed_cap=vehicle_speed_cap, vehicle_type=vehicle_type, ev_traffic_speed_table=ev_traffic_speed_table, ev_ascent=ev_ascent, ev_descent=ev_descent, ev_auxiliary_consumption=ev_auxiliary_consumption, ev_initial_charge=ev_initial_charge, ev_max_charge=ev_max_charge, ev_charging_curve=ev_charging_curve, ev_max_charging_voltage=ev_max_charging_voltage, ev_max_charging_current=ev_max_charging_current, ev_max_charge_after_charging_station=ev_max_charge_after_charging_station, ev_min_charge_at_charging_station=ev_min_charge_at_charging_station, ev_min_charge_at_first_charging_station=ev_min_charge_at_first_charging_station, ev_min_charge_at_destination=ev_min_charge_at_destination, ev_charging_setup_duration=ev_charging_setup_duration, ev_connector_types=ev_connector_types, ev_make_reachable=ev_make_reachable, ev_preferred_brands=ev_preferred_brands, pedestrian_speed=pedestrian_speed, x_request_id=x_request_id, scooter_allow_highway=scooter_allow_highway, currency=currency, customizations=customizations, taxi_allow_drive_through_taxi_roads=taxi_allow_drive_through_taxi_roads, tolls_transponders=tolls_transponders, tolls_vignettes=tolls_vignettes, tolls_summaries=tolls_summaries, tolls_vehicle_category=tolls_vehicle_category, tolls_emission_type=tolls_emission_type, max_speed_on_segment=max_speed_on_segment, traffic_override_flow_duration=traffic_override_flow_duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->calculate_routes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_mode** | [**RouterMode**](.md)| Mode of transport to be used for the calculation of the route.  Note: &#x60;bus&#x60;, &#x60;privateBus&#x60;, and &#x60;taxi&#x60; modes are currently provided as Beta, with limited functionality. The API and behaviour may change drastically, or even become unsupported, without warning. Please refer to the developers&#x27; guide for more details.  | 
 **origin** | [**Waypoint**](.md)| A location defining the origin of the trip.  ## Format  Format: &#x60;Place[WaypointOptions]&#x60;  * Place: &#x60;{lat},{lng}[PlaceOptions]&#x60; * PlaceOptions: &#x60;;option1&#x3D;value1;option2&#x3D;value2...&#x60; * WaypointOptions: &#x60;!option1&#x3D;value1!option2&#x3D;value2...&#x60;  A waypoint consists of:  * Exactly one place * Optional settings for the place * Optional settings for the waypoint itself  Supported place options:  * &#x60;course&#x60;: int, degrees clock-wise from north. Indicating desired direction at the place.   E.g. &#x60;90&#x60; indicating &#x60;east&#x60;. Often combined with &#x60;radius&#x60; and/or &#x60;minCourseDistance&#x60; * &#x60;sideOfStreetHint&#x60;: &#x60;{lat},{lng}&#x60;. Indicating the side of the street that should be   used. E.g. if the location is to the left of the street, the router will prefer using   that side in case the street has dividers. E.g.   &#x60;52.511496,13.304140;sideOfStreetHint&#x3D;52.512149,13.304076&#x60; indicates that the &#x60;north&#x60;   side of the street should be preferred. This option is required, if &#x60;matchSideOfStreet&#x60;   is set to &#x60;always&#x60;. * &#x60;matchSideOfStreet&#x60;: enum &#x60;[always, onlyIfDivided]&#x60;. Specifies how the location set by   &#x60;sideOfStreetHint&#x60; should be handled. Requires &#x60;sideOfStreetHint&#x60; to be specified as   well.   + &#x60;always&#x60; : Always prefer the given side of street.   + &#x60;onlyIfDivided&#x60;: Only prefer using side of street set by &#x60;sideOfStreetHint&#x60; in case     the street has dividers. This is the default behavior. * &#x60;nameHint&#x60;: string. Causes the router to look for the place with the most similar name.   This can e.g. include things like: &#x60;North&#x60; being used to differentiate between   interstates &#x60;I66 North&#x60; and &#x60;I66 South&#x60;, &#x60;Downtown Avenue&#x60; being used to correctly   select a residental street. * &#x60;radius&#x60;: int, meters. Asks the router to consider all places within the given radius as   potential candidates for route calculation. This can be either because it is not   important which place is used, or because it is unknown. Radius more than 200meter are   not supported. * &#x60;minCourseDistance&#x60;: int, meters. Instructs the routing service to try to find a route that avoids actions for the indicated distance.   For example, if the origin is determined by a moving vehicle, the user might not have time to react to early actions. * &#x60;customizationIndex&#x60;: int. Specifies the zero-based index into the list of customizations   specified in the &#x60;customizations&#x60; parameter. The customization at that index must be an   Extension Map.   Providing a &#x60;customizationIndex&#x60; indicates the this waypoint is located within that   Extension Map.   **Alpha**: This customization API parameter is in development. It may not be stable and is subject to change. * &#x60;segmentIdHint&#x60;: string. Causes the router to try and match to the specified segment.   Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint   This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one. * &#x60;onRoadThreshold&#x60;: int, meters. allows specifying a distance within which   the waypoint could be considered as being on a highway/bridge/tunnel/sliproad.   Within this threshold, the attributes of the segments do not impact the matching.   Outside the threshold only segments which aren&#x27;t one of highway/bridge/tunnel/sliproad can be matched.  Notes:  * &#x60;stopDuration&#x60; option is not supported for &#x60;origin&#x60;, contrary to &#x60;destination&#x60; and   &#x60;via&#x60; waypoints. * &#x60;passThrough&#x60;: option is not supported for &#x27;origin&#x27;. * Non-structural reserved characters in options&#x27; values need to be properly percent-encoded.   Please refer to the developers&#x27; guide for more details.  | 
 **destination** | [**Waypoint**](.md)| A location defining the destination of the trip.  ## Format  Format: &#x60;Place[WaypointOptions]&#x60;  * Place: &#x60;{lat},{lng}[PlaceOptions]&#x60; * PlaceOptions: &#x60;;option1&#x3D;value1;option2&#x3D;value2...&#x60; * WaypointOptions: &#x60;!option1&#x3D;value1!option2&#x3D;value2...&#x60;  A waypoint consists of:  * Exactly one place * Optional settings for the place * Optional settings for the waypoint itself  Supported place options:  * &#x60;course&#x60;: int, degrees clock-wise from north. Indicating desired direction at the place.   E.g. &#x60;90&#x60; indicating &#x60;east&#x60;. Often combined with &#x60;radius&#x60; and/or &#x60;minCourseDistance&#x60; * &#x60;sideOfStreetHint&#x60;: &#x60;{lat},{lng}&#x60;. Indicating the side of the street that should be   used. E.g. if the location is to the left of the street, the router will prefer using   that side in case the street has dividers. E.g.   &#x60;52.511496,13.304140;sideOfStreetHint&#x3D;52.512149,13.304076&#x60; indicates that the &#x60;north&#x60;   side of the street should be preferred. This option is required, if &#x60;matchSideOfStreet&#x60;   is set to &#x60;always&#x60;. * &#x60;matchSideOfStreet&#x60;: enum &#x60;[always, onlyIfDivided]&#x60;. Specifies how the location set by   &#x60;sideOfStreetHint&#x60; should be handled. Requires &#x60;sideOfStreetHint&#x60; to be specified as   well.   + &#x60;always&#x60; : Always prefer the given side of street.   + &#x60;onlyIfDivided&#x60;: Only prefer using side of street set by &#x60;sideOfStreetHint&#x60; in case     the street has dividers. This is the default behavior. * &#x60;nameHint&#x60;: string. Causes the router to look for the place with the most similar name.   This can e.g. include things like: &#x60;North&#x60; being used to differentiate between   interstates &#x60;I66 North&#x60; and &#x60;I66 South&#x60;, &#x60;Downtown Avenue&#x60; being used to correctly   select a residental street. * &#x60;radius&#x60;: int, meters. Asks the router to consider all places within the given radius as   potential candidates for route calculation. This can be either because it is not   important which place is used, or because it is unknown. Radius more than 200meter are   not supported. * &#x60;minCourseDistance&#x60;: int, meters. Instructs the routing service to try to find a route that avoids actions for the indicated distance.   For example, if the origin is determined by a moving vehicle, the user might not have time to react to early actions. * &#x60;customizationIndex&#x60;: int. Specifies the zero-based index into the list of customizations   specified in the &#x60;customizations&#x60; parameter. The customization at that index must be an   Extension Map.   Providing a &#x60;customizationIndex&#x60; indicates the this waypoint is located within that   Extension Map.   **Alpha**: This customization API parameter is in development. It may not be stable and is subject to change. * &#x60;segmentIdHint&#x60;: string. Causes the router to try and match to the specified segment.   Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint   This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one. * &#x60;onRoadThreshold&#x60;: int, meters. allows specifying a distance within which   the waypoint could be considered as being on a highway/bridge/tunnel/sliproad.   Within this threshold, the attributes of the segments do not impact the matching.   Outside the threshold only segments which aren&#x27;t one of highway/bridge/tunnel/sliproad can be matched.  Supported waypoint options:  * &#x60;stopDuration&#x60;: desired duration for the stop, in seconds. The section arriving at this   via waypoint will have a &#x60;wait&#x60; post action reflecting the stopping time. The   consecutive section will start at the arrival time of the former section + stop   duration. * &#x60;passThrough&#x60;: option is not supported for &#x27;destination&#x27;.  Notes:  * Non-structural reserved characters in options&#x27; values need to be properly percent-encoded.   Please refer to the developers&#x27; guide for more details.  | 
 **ev_free_flow_speed_table** | [**object**](.md)|  | 
 **via** | [**list[Waypoint]**](Waypoint.md)| A location defining a via waypoint.  A via waypoint is a location between origin and destination. The route will do a stop at the via waypoint.  Multiple waypoints can also be specified using multiple via parameters like &#x60;via&#x3D;...&amp;via&#x3D;...&#x60;, in which case the route will traverse these waypoints sequentially in the order specified in the request.  ## Format  Format: &#x60;Place[WaypointOptions]&#x60;  * Place: &#x60;{lat},{lng}[PlaceOptions]&#x60; * PlaceOptions: &#x60;;option1&#x3D;value1;option2&#x3D;value2...&#x60; * WaypointOptions: &#x60;!option1&#x3D;value1!option2&#x3D;value2...&#x60;  A waypoint consists of:  * Exactly one place * Optional settings for the place * Optional settings for the waypoint itself  Supported place options:  * &#x60;course&#x60;: int, degrees clock-wise from north. Indicating desired direction at the place.   E.g. &#x60;90&#x60; indicating &#x60;east&#x60;. Often combined with &#x60;radius&#x60; and/or &#x60;minCourseDistance&#x60; * &#x60;sideOfStreetHint&#x60;: &#x60;{lat},{lng}&#x60;. Indicating the side of the street that should be   used. E.g. if the location is to the left of the street, the router will prefer using   that side in case the street has dividers. E.g.   &#x60;52.511496,13.304140;sideOfStreetHint&#x3D;52.512149,13.304076&#x60; indicates that the &#x60;north&#x60;   side of the street should be preferred. This option is required, if &#x60;matchSideOfStreet&#x60;   is set to &#x60;always&#x60;. * &#x60;matchSideOfStreet&#x60;: enum &#x60;[always, onlyIfDivided]&#x60;. Specifies how the location set by   &#x60;sideOfStreetHint&#x60; should be handled. Requires &#x60;sideOfStreetHint&#x60; to be specified as   well.   + &#x60;always&#x60; : Always prefer the given side of street.   + &#x60;onlyIfDivided&#x60;: Only prefer using side of street set by &#x60;sideOfStreetHint&#x60; in case     the street has dividers. This is the default behavior. * &#x60;nameHint&#x60;: string. Causes the router to look for the place with the most similar name.   This can e.g. include things like: &#x60;North&#x60; being used to differentiate between   interstates &#x60;I66 North&#x60; and &#x60;I66 South&#x60;, &#x60;Downtown Avenue&#x60; being used to correctly   select a residental street. * &#x60;radius&#x60;: int, meters. Asks the router to consider all places within the given radius as   potential candidates for route calculation. This can be either because it is not   important which place is used, or because it is unknown. Radius more than 200meter are   not supported. * &#x60;minCourseDistance&#x60;: int, meters. Instructs the routing service to try to find a route that avoids actions for the indicated distance.   For example, if the origin is determined by a moving vehicle, the user might not have time to react to early actions. * &#x60;customizationIndex&#x60;: int. Specifies the zero-based index into the list of customizations   specified in the &#x60;customizations&#x60; parameter. The customization at that index must be an   Extension Map.   Providing a &#x60;customizationIndex&#x60; indicates the this waypoint is located within that   Extension Map.   **Alpha**: This customization API parameter is in development. It may not be stable and is subject to change. * &#x60;segmentIdHint&#x60;: string. Causes the router to try and match to the specified segment.   Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint   This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one. * &#x60;onRoadThreshold&#x60;: int, meters. allows specifying a distance within which   the waypoint could be considered as being on a highway/bridge/tunnel/sliproad.   Within this threshold, the attributes of the segments do not impact the matching.   Outside the threshold only segments which aren&#x27;t one of highway/bridge/tunnel/sliproad can be matched.  Supported waypoint options: * &#x60;stopDuration&#x60;: desired duration for the stop, in seconds. * &#x60;passThrough&#x60;: boolean. Asks the router to avoid the following during route calculation:   + Introducing a stop at the waypoint.   + Splitting the route into sections.   + Changing the direction of travel.    Following scenarios are not supported for &#x60;passThrough&#x60; parameter:   + Setting both &#x60;stopDuration&#x60; to a value greater than 0 and &#x60;passThrough&#x3D;true&#x60;.   + Setting &#x60;passThrough&#x3D;true&#x60; for &#x60;origin&#x60; or &#x60;destination&#x60; of a route.   The default value is &#x60;false&#x60;.  Notes:  * Non-structural reserved characters in options&#x27; values need to be properly percent-encoded.   Please refer to the developers&#x27; guide for more details.  | [optional] 
 **departure_time** | [**TimeWithAny**](.md)| Specifies the time of departure as defined by either &#x60;date-time&#x60; or &#x60;full-date&#x60; &#x60;T&#x60; &#x60;partial-time&#x60; in &#x60;RFC 3339&#x60;, section 5.6 (for example, &#x60;2019-06-24T01:23:45&#x60;).  The requested time is converted to local time at origin. When the optional timezone offset is not specified, time is assumed to be local. The special value &#x60;any&#x60; can be used to indicate that time should not be taken into account during routing. If neither &#x60;departureTime&#x60; or &#x60;arrivalTime&#x60; are specified, current time at departure place will be used. All time values in the response are returned in the timezone of each location.  | [optional] 
 **arrival_time** | [**Time**](.md)| Specifies the time of arrival as defined by either &#x60;date-time&#x60; or &#x60;full-date&#x60; &#x60;T&#x60; &#x60;partial-time&#x60; in &#x60;RFC 3339&#x60;, section 5.6 (for example, &#x60;2019-06-24T01:23:45&#x60;). The requested time is converted to the local time at destination. When the optional timezone offset is not specified, time is assumed to be local. All &#x60;Time&#x60; values in the response are returned in the timezone of each location.  Note : The following features do not support the arrivalTime parameter: * EV Routing * Route Handle * Route Import  | [optional] 
 **routing_mode** | [**RoutingMode**](.md)| Specifies which optimization is applied during route calculation.  * &#x60;fast&#x60;: Route calculation from start to destination optimized by travel time. In many   cases, the route returned by the &#x60;fast&#x60; mode may not be the route with the fastest   possible travel time. For example, the routing service may favor a route that remains on   a highway, even if a faster travel time can be achieved by taking a detour or shortcut   through an inconvenient side road. * &#x60;short&#x60;: Route calculation from start to destination disregarding any speed information.   In this mode, the distance of the route is minimized, while keeping the route sensible.   This includes, for example, penalizing turns. Because of that, the resulting route will   not necessarily be the one with minimal distance.  Notes: * The following Transport modes only support &#x60;fast&#x60; routingMode   - &#x60;bicycle&#x60;   - &#x60;bus&#x60;   - &#x60;pedestrian&#x60;   - &#x60;privateBus&#x60;   - &#x60;scooter&#x60;   - &#x60;taxi&#x60;  | [optional] 
 **alternatives** | **int**| Number of alternative routes to return aside from the optimal route. | [optional] [default to 0]
 **avoid_features** | **str**|  | [optional] 
 **avoid_areas** | **str**|  | [optional] 
 **avoid_segments** | **str**|  | [optional] 
 **avoid_zone_categories** | **str**|  | [optional] 
 **avoid_zone_identifiers** | **str**|  | [optional] 
 **avoid_truck_road_types** | **str**|  | [optional] 
 **avoid_toll_transponders** | **str**|  | [optional] 
 **exclude_countries** | **str**|  | [optional] 
 **units** | [**Units**](.md)| Units of measurement used in guidance instructions. The default is &#x60;metric&#x60;.  | [optional] 
 **lang** | [**list[str]**](str.md)| Specifies the list of preferred languages of the response. The first supported language from the list will be used for for the response. The value should comply with the [IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). A list of supported languages for the routing service can be found in the dev guide https://developer.here.com/documentation/routing-api/dev_guide/topics/languages.html.  Note: If the first language in the list is not supported, an info notification will be generated with code &#x60;mainLanguageNotFound&#x60;.  | [optional] [default to [&quot;en-US&quot;]]
 **_return** | [**list[ModelReturn]**](ModelReturn.md)|  | [optional] 
 **spans** | [**list[Spans]**](Spans.md)| Defines which map content attributes are included in the response spans. For example, &#x60;attributes,length&#x60; will enable the fields &#x60;attributes&#x60; and &#x60;length&#x60; in the route response. For more information about the &#x60;countryCode&#x60; field, see https://www.iso.org/obp/ui/#search.  This parameter also requires that the &#x60;polyline&#x60; option is set within the &#x60;return&#x60; parameter.  | [optional] 
 **truck_shipped_hazardous_goods** | **str**|  | [optional] 
 **truck_gross_weight** | **int**|  | [optional] 
 **truck_weight_per_axle** | **int**|  | [optional] 
 **truck_weight_per_axle_group** | **str**|  | [optional] 
 **truck_height** | **int**|  | [optional] 
 **truck_width** | **int**|  | [optional] 
 **truck_length** | **int**|  | [optional] 
 **truck_tunnel_category** | **str**|  | [optional] 
 **truck_axle_count** | **int**|  | [optional] 
 **truck_trailer_axle_count** | **int**|  | [optional] 
 **truck_tires_count** | **int**|  | [optional] 
 **truck_category** | **str**|  | [optional] [default to undefined]
 **truck_trailer_count** | **int**|  | [optional] [default to 0]
 **truck_hov_occupancy** | **int**|  | [optional] [default to 1]
 **truck_license_plate** | **str**|  | [optional] 
 **truck_speed_cap** | **float**|  | [optional] 
 **truck_type** | **str**|  | [optional] [default to straight]
 **vehicle_shipped_hazardous_goods** | **str**|  | [optional] 
 **vehicle_gross_weight** | **int**|  | [optional] 
 **vehicle_weight_per_axle** | **int**|  | [optional] 
 **vehicle_weight_per_axle_group** | **str**|  | [optional] 
 **vehicle_height** | **int**|  | [optional] 
 **vehicle_width** | **int**|  | [optional] 
 **vehicle_length** | **int**|  | [optional] 
 **vehicle_tunnel_category** | **str**|  | [optional] 
 **vehicle_axle_count** | **int**|  | [optional] 
 **vehicle_trailer_axle_count** | **int**|  | [optional] 
 **vehicle_tires_count** | **int**|  | [optional] 
 **vehicle_category** | **str**|  | [optional] [default to undefined]
 **vehicle_trailer_count** | **int**|  | [optional] [default to 0]
 **vehicle_hov_occupancy** | **int**|  | [optional] [default to 1]
 **vehicle_license_plate** | **str**|  | [optional] 
 **vehicle_speed_cap** | **float**|  | [optional] 
 **vehicle_type** | **str**|  | [optional] 
 **ev_traffic_speed_table** | [**object**](.md)|  | [optional] 
 **ev_ascent** | **float**|  | [optional] 
 **ev_descent** | **float**|  | [optional] 
 **ev_auxiliary_consumption** | **float**|  | [optional] 
 **ev_initial_charge** | **float**|  | [optional] 
 **ev_max_charge** | **float**|  | [optional] 
 **ev_charging_curve** | **str**|  | [optional] 
 **ev_max_charging_voltage** | **float**|  | [optional] 
 **ev_max_charging_current** | **float**|  | [optional] 
 **ev_max_charge_after_charging_station** | **float**|  | [optional] 
 **ev_min_charge_at_charging_station** | **float**|  | [optional] 
 **ev_min_charge_at_first_charging_station** | **float**|  | [optional] 
 **ev_min_charge_at_destination** | **float**|  | [optional] 
 **ev_charging_setup_duration** | **int**|  | [optional] 
 **ev_connector_types** | **str**|  | [optional] 
 **ev_make_reachable** | **bool**|  | [optional] 
 **ev_preferred_brands** | **str**|  | [optional] 
 **pedestrian_speed** | [**PedestrianSpeed**](.md)| **Disclaimer: This parameter is currently in beta release, and is therefore subject to breaking changes. The parameter could be extracted to a separate API if speed capping for cars/trucks is introduced** Walking speed in meters per second. Influences the duration of walking segments along the route.  | [optional] 
 **x_request_id** | **str**| User-provided token that can be used to trace a request or a group of requests sent to the service. | [optional] 
 **scooter_allow_highway** | **bool**|  | [optional] [default to false]
 **currency** | **str**| Currency code compliant to ISO 4217. Costs for the calculated route will be returned using this currency.  If not provided, the router will specify it. On a best-effort basis, the router will try to specify the costs in the local currency.  | [optional] 
 **customizations** | [**list[CustomizationHRN]**](CustomizationHRN.md)| Specifies a list of customizations to be used. The data provided by these customizations either replaces or augments the standard HERE map data. The provided credentials must authorize access to all of the customizations specified.  **Alpha**: This API is in development. It may not be stable and is subject to change.  | [optional] 
 **taxi_allow_drive_through_taxi_roads** | **bool**|  | [optional] [default to true]
 **tolls_transponders** | **str**|  | [optional] 
 **tolls_vignettes** | **str**|  | [optional] 
 **tolls_summaries** | [**list[str]**](str.md)|  | [optional] 
 **tolls_vehicle_category** | **str**|  | [optional] 
 **tolls_emission_type** | **str**|  | [optional] 
 **max_speed_on_segment** | [**MaxSpeedOnSegment**](.md)| Specify new base speed for segment by value. Affects route selection and the ETA. Cannot increase base speed on segment.  | [optional] 
 **traffic_override_flow_duration** | **int**|  | [optional] 

### Return type

[**RouterRouteResponse**](RouterRouteResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_routes_post**
> RouterRouteResponse calculate_routes_post(transport_mode, origin, destination, ev_free_flow_speed_table, body=body, x_request_id=x_request_id, via=via, departure_time=departure_time, arrival_time=arrival_time, routing_mode=routing_mode, alternatives=alternatives, avoid_features=avoid_features, avoid_areas=avoid_areas, avoid_segments=avoid_segments, avoid_zone_categories=avoid_zone_categories, avoid_zone_identifiers=avoid_zone_identifiers, avoid_truck_road_types=avoid_truck_road_types, avoid_toll_transponders=avoid_toll_transponders, exclude_countries=exclude_countries, units=units, lang=lang, _return=_return, spans=spans, truck_shipped_hazardous_goods=truck_shipped_hazardous_goods, truck_gross_weight=truck_gross_weight, truck_weight_per_axle=truck_weight_per_axle, truck_weight_per_axle_group=truck_weight_per_axle_group, truck_height=truck_height, truck_width=truck_width, truck_length=truck_length, truck_tunnel_category=truck_tunnel_category, truck_axle_count=truck_axle_count, truck_trailer_axle_count=truck_trailer_axle_count, truck_tires_count=truck_tires_count, truck_category=truck_category, truck_trailer_count=truck_trailer_count, truck_hov_occupancy=truck_hov_occupancy, truck_license_plate=truck_license_plate, truck_speed_cap=truck_speed_cap, truck_type=truck_type, vehicle_shipped_hazardous_goods=vehicle_shipped_hazardous_goods, vehicle_gross_weight=vehicle_gross_weight, vehicle_weight_per_axle=vehicle_weight_per_axle, vehicle_weight_per_axle_group=vehicle_weight_per_axle_group, vehicle_height=vehicle_height, vehicle_width=vehicle_width, vehicle_length=vehicle_length, vehicle_tunnel_category=vehicle_tunnel_category, vehicle_axle_count=vehicle_axle_count, vehicle_trailer_axle_count=vehicle_trailer_axle_count, vehicle_tires_count=vehicle_tires_count, vehicle_category=vehicle_category, vehicle_trailer_count=vehicle_trailer_count, vehicle_hov_occupancy=vehicle_hov_occupancy, vehicle_license_plate=vehicle_license_plate, vehicle_speed_cap=vehicle_speed_cap, vehicle_type=vehicle_type, ev_traffic_speed_table=ev_traffic_speed_table, ev_ascent=ev_ascent, ev_descent=ev_descent, ev_auxiliary_consumption=ev_auxiliary_consumption, ev_initial_charge=ev_initial_charge, ev_max_charge=ev_max_charge, ev_charging_curve=ev_charging_curve, ev_max_charging_voltage=ev_max_charging_voltage, ev_max_charging_current=ev_max_charging_current, ev_max_charge_after_charging_station=ev_max_charge_after_charging_station, ev_min_charge_at_charging_station=ev_min_charge_at_charging_station, ev_min_charge_at_first_charging_station=ev_min_charge_at_first_charging_station, ev_min_charge_at_destination=ev_min_charge_at_destination, ev_charging_setup_duration=ev_charging_setup_duration, ev_connector_types=ev_connector_types, ev_make_reachable=ev_make_reachable, ev_preferred_brands=ev_preferred_brands, pedestrian_speed=pedestrian_speed, scooter_allow_highway=scooter_allow_highway, currency=currency, customizations=customizations, taxi_allow_drive_through_taxi_roads=taxi_allow_drive_through_taxi_roads, tolls_transponders=tolls_transponders, tolls_vignettes=tolls_vignettes, tolls_summaries=tolls_summaries, tolls_vehicle_category=tolls_vehicle_category, tolls_emission_type=tolls_emission_type, max_speed_on_segment=max_speed_on_segment, traffic_override_flow_duration=traffic_override_flow_duration)

Calculate routes via POST

Calculates a route using a generic vehicle/pedestrian mode, e.g. car, truck, pedestrian, etc...  At the moment, only select parameters are permitted in the POST payload. In particular, those parameters that due to request size may be limited in the query string. See the request body section below. These parameters can be provided either in the query string or in the POST body. However, if a parameter is provided in both, the request will fail. All other parameters can only be provided in the query string at the moment.  Post body size limit is 10MiB. 

### Example
```python
from __future__ import print_function
import time
import here_public_transit_api
from here_public_transit_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = here_public_transit_api.Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = here_public_transit_api.RoutingApi(here_public_transit_api.ApiClient(configuration))
transport_mode = here_public_transit_api.RouterMode() # RouterMode | Mode of transport to be used for the calculation of the route.  Note: `bus`, `privateBus`, and `taxi` modes are currently provided as Beta, with limited functionality. The API and behaviour may change drastically, or even become unsupported, without warning. Please refer to the developers' guide for more details. 
origin = here_public_transit_api.Waypoint() # Waypoint | A location defining the origin of the trip.  ## Format  Format: `Place[WaypointOptions]`  * Place: `{lat},{lng}[PlaceOptions]` * PlaceOptions: `;option1=value1;option2=value2...` * WaypointOptions: `!option1=value1!option2=value2...`  A waypoint consists of:  * Exactly one place * Optional settings for the place * Optional settings for the waypoint itself  Supported place options:  * `course`: int, degrees clock-wise from north. Indicating desired direction at the place.   E.g. `90` indicating `east`. Often combined with `radius` and/or `minCourseDistance` * `sideOfStreetHint`: `{lat},{lng}`. Indicating the side of the street that should be   used. E.g. if the location is to the left of the street, the router will prefer using   that side in case the street has dividers. E.g.   `52.511496,13.304140;sideOfStreetHint=52.512149,13.304076` indicates that the `north`   side of the street should be preferred. This option is required, if `matchSideOfStreet`   is set to `always`. * `matchSideOfStreet`: enum `[always, onlyIfDivided]`. Specifies how the location set by   `sideOfStreetHint` should be handled. Requires `sideOfStreetHint` to be specified as   well.   + `always` : Always prefer the given side of street.   + `onlyIfDivided`: Only prefer using side of street set by `sideOfStreetHint` in case     the street has dividers. This is the default behavior. * `nameHint`: string. Causes the router to look for the place with the most similar name.   This can e.g. include things like: `North` being used to differentiate between   interstates `I66 North` and `I66 South`, `Downtown Avenue` being used to correctly   select a residental street. * `radius`: int, meters. Asks the router to consider all places within the given radius as   potential candidates for route calculation. This can be either because it is not   important which place is used, or because it is unknown. Radius more than 200meter are   not supported. * `minCourseDistance`: int, meters. Instructs the routing service to try to find a route that avoids actions for the indicated distance.   For example, if the origin is determined by a moving vehicle, the user might not have time to react to early actions. * `customizationIndex`: int. Specifies the zero-based index into the list of customizations   specified in the `customizations` parameter. The customization at that index must be an   Extension Map.   Providing a `customizationIndex` indicates the this waypoint is located within that   Extension Map.   **Alpha**: This customization API parameter is in development. It may not be stable and is subject to change. * `segmentIdHint`: string. Causes the router to try and match to the specified segment.   Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint   This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one. * `onRoadThreshold`: int, meters. allows specifying a distance within which   the waypoint could be considered as being on a highway/bridge/tunnel/sliproad.   Within this threshold, the attributes of the segments do not impact the matching.   Outside the threshold only segments which aren't one of highway/bridge/tunnel/sliproad can be matched.  Notes:  * `stopDuration` option is not supported for `origin`, contrary to `destination` and   `via` waypoints. * `passThrough`: option is not supported for 'origin'. * Non-structural reserved characters in options' values need to be properly percent-encoded.   Please refer to the developers' guide for more details. 
destination = here_public_transit_api.Waypoint() # Waypoint | A location defining the destination of the trip.  ## Format  Format: `Place[WaypointOptions]`  * Place: `{lat},{lng}[PlaceOptions]` * PlaceOptions: `;option1=value1;option2=value2...` * WaypointOptions: `!option1=value1!option2=value2...`  A waypoint consists of:  * Exactly one place * Optional settings for the place * Optional settings for the waypoint itself  Supported place options:  * `course`: int, degrees clock-wise from north. Indicating desired direction at the place.   E.g. `90` indicating `east`. Often combined with `radius` and/or `minCourseDistance` * `sideOfStreetHint`: `{lat},{lng}`. Indicating the side of the street that should be   used. E.g. if the location is to the left of the street, the router will prefer using   that side in case the street has dividers. E.g.   `52.511496,13.304140;sideOfStreetHint=52.512149,13.304076` indicates that the `north`   side of the street should be preferred. This option is required, if `matchSideOfStreet`   is set to `always`. * `matchSideOfStreet`: enum `[always, onlyIfDivided]`. Specifies how the location set by   `sideOfStreetHint` should be handled. Requires `sideOfStreetHint` to be specified as   well.   + `always` : Always prefer the given side of street.   + `onlyIfDivided`: Only prefer using side of street set by `sideOfStreetHint` in case     the street has dividers. This is the default behavior. * `nameHint`: string. Causes the router to look for the place with the most similar name.   This can e.g. include things like: `North` being used to differentiate between   interstates `I66 North` and `I66 South`, `Downtown Avenue` being used to correctly   select a residental street. * `radius`: int, meters. Asks the router to consider all places within the given radius as   potential candidates for route calculation. This can be either because it is not   important which place is used, or because it is unknown. Radius more than 200meter are   not supported. * `minCourseDistance`: int, meters. Instructs the routing service to try to find a route that avoids actions for the indicated distance.   For example, if the origin is determined by a moving vehicle, the user might not have time to react to early actions. * `customizationIndex`: int. Specifies the zero-based index into the list of customizations   specified in the `customizations` parameter. The customization at that index must be an   Extension Map.   Providing a `customizationIndex` indicates the this waypoint is located within that   Extension Map.   **Alpha**: This customization API parameter is in development. It may not be stable and is subject to change. * `segmentIdHint`: string. Causes the router to try and match to the specified segment.   Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint   This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one. * `onRoadThreshold`: int, meters. allows specifying a distance within which   the waypoint could be considered as being on a highway/bridge/tunnel/sliproad.   Within this threshold, the attributes of the segments do not impact the matching.   Outside the threshold only segments which aren't one of highway/bridge/tunnel/sliproad can be matched.  Supported waypoint options:  * `stopDuration`: desired duration for the stop, in seconds. The section arriving at this   via waypoint will have a `wait` post action reflecting the stopping time. The   consecutive section will start at the arrival time of the former section + stop   duration. * `passThrough`: option is not supported for 'destination'.  Notes:  * Non-structural reserved characters in options' values need to be properly percent-encoded.   Please refer to the developers' guide for more details. 
ev_free_flow_speed_table = NULL # object | 
body = here_public_transit_api.CalculateRoutesPostParameters() # CalculateRoutesPostParameters |  (optional)
x_request_id = 'x_request_id_example' # str | User-provided token that can be used to trace a request or a group of requests sent to the service. (optional)
via = [here_public_transit_api.Waypoint()] # list[Waypoint] | A location defining a via waypoint.  A via waypoint is a location between origin and destination. The route will do a stop at the via waypoint.  Multiple waypoints can also be specified using multiple via parameters like `via=...&via=...`, in which case the route will traverse these waypoints sequentially in the order specified in the request.  ## Format  Format: `Place[WaypointOptions]`  * Place: `{lat},{lng}[PlaceOptions]` * PlaceOptions: `;option1=value1;option2=value2...` * WaypointOptions: `!option1=value1!option2=value2...`  A waypoint consists of:  * Exactly one place * Optional settings for the place * Optional settings for the waypoint itself  Supported place options:  * `course`: int, degrees clock-wise from north. Indicating desired direction at the place.   E.g. `90` indicating `east`. Often combined with `radius` and/or `minCourseDistance` * `sideOfStreetHint`: `{lat},{lng}`. Indicating the side of the street that should be   used. E.g. if the location is to the left of the street, the router will prefer using   that side in case the street has dividers. E.g.   `52.511496,13.304140;sideOfStreetHint=52.512149,13.304076` indicates that the `north`   side of the street should be preferred. This option is required, if `matchSideOfStreet`   is set to `always`. * `matchSideOfStreet`: enum `[always, onlyIfDivided]`. Specifies how the location set by   `sideOfStreetHint` should be handled. Requires `sideOfStreetHint` to be specified as   well.   + `always` : Always prefer the given side of street.   + `onlyIfDivided`: Only prefer using side of street set by `sideOfStreetHint` in case     the street has dividers. This is the default behavior. * `nameHint`: string. Causes the router to look for the place with the most similar name.   This can e.g. include things like: `North` being used to differentiate between   interstates `I66 North` and `I66 South`, `Downtown Avenue` being used to correctly   select a residental street. * `radius`: int, meters. Asks the router to consider all places within the given radius as   potential candidates for route calculation. This can be either because it is not   important which place is used, or because it is unknown. Radius more than 200meter are   not supported. * `minCourseDistance`: int, meters. Instructs the routing service to try to find a route that avoids actions for the indicated distance.   For example, if the origin is determined by a moving vehicle, the user might not have time to react to early actions. * `customizationIndex`: int. Specifies the zero-based index into the list of customizations   specified in the `customizations` parameter. The customization at that index must be an   Extension Map.   Providing a `customizationIndex` indicates the this waypoint is located within that   Extension Map.   **Alpha**: This customization API parameter is in development. It may not be stable and is subject to change. * `segmentIdHint`: string. Causes the router to try and match to the specified segment.   Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint   This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one. * `onRoadThreshold`: int, meters. allows specifying a distance within which   the waypoint could be considered as being on a highway/bridge/tunnel/sliproad.   Within this threshold, the attributes of the segments do not impact the matching.   Outside the threshold only segments which aren't one of highway/bridge/tunnel/sliproad can be matched.  Supported waypoint options: * `stopDuration`: desired duration for the stop, in seconds. * `passThrough`: boolean. Asks the router to avoid the following during route calculation:   + Introducing a stop at the waypoint.   + Splitting the route into sections.   + Changing the direction of travel.    Following scenarios are not supported for `passThrough` parameter:   + Setting both `stopDuration` to a value greater than 0 and `passThrough=true`.   + Setting `passThrough=true` for `origin` or `destination` of a route.   The default value is `false`.  Notes:  * Non-structural reserved characters in options' values need to be properly percent-encoded.   Please refer to the developers' guide for more details.  (optional)
departure_time = here_public_transit_api.TimeWithAny() # TimeWithAny | Specifies the time of departure as defined by either `date-time` or `full-date` `T` `partial-time` in `RFC 3339`, section 5.6 (for example, `2019-06-24T01:23:45`).  The requested time is converted to local time at origin. When the optional timezone offset is not specified, time is assumed to be local. The special value `any` can be used to indicate that time should not be taken into account during routing. If neither `departureTime` or `arrivalTime` are specified, current time at departure place will be used. All time values in the response are returned in the timezone of each location.  (optional)
arrival_time = here_public_transit_api.Time() # Time | Specifies the time of arrival as defined by either `date-time` or `full-date` `T` `partial-time` in `RFC 3339`, section 5.6 (for example, `2019-06-24T01:23:45`). The requested time is converted to the local time at destination. When the optional timezone offset is not specified, time is assumed to be local. All `Time` values in the response are returned in the timezone of each location.  Note : The following features do not support the arrivalTime parameter: * EV Routing * Route Handle * Route Import  (optional)
routing_mode = here_public_transit_api.RoutingMode() # RoutingMode | Specifies which optimization is applied during route calculation.  * `fast`: Route calculation from start to destination optimized by travel time. In many   cases, the route returned by the `fast` mode may not be the route with the fastest   possible travel time. For example, the routing service may favor a route that remains on   a highway, even if a faster travel time can be achieved by taking a detour or shortcut   through an inconvenient side road. * `short`: Route calculation from start to destination disregarding any speed information.   In this mode, the distance of the route is minimized, while keeping the route sensible.   This includes, for example, penalizing turns. Because of that, the resulting route will   not necessarily be the one with minimal distance.  Notes: * The following Transport modes only support `fast` routingMode   - `bicycle`   - `bus`   - `pedestrian`   - `privateBus`   - `scooter`   - `taxi`  (optional)
alternatives = 0 # int | Number of alternative routes to return aside from the optimal route. (optional) (default to 0)
avoid_features = 'avoid_features_example' # str |  (optional)
avoid_areas = 'avoid_areas_example' # str |  (optional)
avoid_segments = 'avoid_segments_example' # str |  (optional)
avoid_zone_categories = 'avoid_zone_categories_example' # str |  (optional)
avoid_zone_identifiers = 'avoid_zone_identifiers_example' # str |  (optional)
avoid_truck_road_types = 'avoid_truck_road_types_example' # str |  (optional)
avoid_toll_transponders = 'avoid_toll_transponders_example' # str |  (optional)
exclude_countries = 'exclude_countries_example' # str |  (optional)
units = here_public_transit_api.Units() # Units | Units of measurement used in guidance instructions. The default is `metric`.  (optional)
lang = ['[\"en-US\"]'] # list[str] | Specifies the list of preferred languages of the response. The first supported language from the list will be used for for the response. The value should comply with the [IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). A list of supported languages for the routing service can be found in the dev guide https://developer.here.com/documentation/routing-api/dev_guide/topics/languages.html.  Note: If the first language in the list is not supported, an info notification will be generated with code `mainLanguageNotFound`.  (optional) (default to ["en-US"])
_return = [here_public_transit_api.ModelReturn()] # list[ModelReturn] |  (optional)
spans = [here_public_transit_api.Spans()] # list[Spans] | Defines which map content attributes are included in the response spans. For example, `attributes,length` will enable the fields `attributes` and `length` in the route response. For more information about the `countryCode` field, see https://www.iso.org/obp/ui/#search.  This parameter also requires that the `polyline` option is set within the `return` parameter.  (optional)
truck_shipped_hazardous_goods = 'truck_shipped_hazardous_goods_example' # str |  (optional)
truck_gross_weight = 56 # int |  (optional)
truck_weight_per_axle = 56 # int |  (optional)
truck_weight_per_axle_group = 'truck_weight_per_axle_group_example' # str |  (optional)
truck_height = 56 # int |  (optional)
truck_width = 56 # int |  (optional)
truck_length = 56 # int |  (optional)
truck_tunnel_category = 'truck_tunnel_category_example' # str |  (optional)
truck_axle_count = 56 # int |  (optional)
truck_trailer_axle_count = 56 # int |  (optional)
truck_tires_count = 56 # int |  (optional)
truck_category = 'undefined' # str |  (optional) (default to undefined)
truck_trailer_count = 0 # int |  (optional) (default to 0)
truck_hov_occupancy = 1 # int |  (optional) (default to 1)
truck_license_plate = 'truck_license_plate_example' # str |  (optional)
truck_speed_cap = 1.2 # float |  (optional)
truck_type = 'straight' # str |  (optional) (default to straight)
vehicle_shipped_hazardous_goods = 'vehicle_shipped_hazardous_goods_example' # str |  (optional)
vehicle_gross_weight = 56 # int |  (optional)
vehicle_weight_per_axle = 56 # int |  (optional)
vehicle_weight_per_axle_group = 'vehicle_weight_per_axle_group_example' # str |  (optional)
vehicle_height = 56 # int |  (optional)
vehicle_width = 56 # int |  (optional)
vehicle_length = 56 # int |  (optional)
vehicle_tunnel_category = 'vehicle_tunnel_category_example' # str |  (optional)
vehicle_axle_count = 56 # int |  (optional)
vehicle_trailer_axle_count = 56 # int |  (optional)
vehicle_tires_count = 56 # int |  (optional)
vehicle_category = 'undefined' # str |  (optional) (default to undefined)
vehicle_trailer_count = 0 # int |  (optional) (default to 0)
vehicle_hov_occupancy = 1 # int |  (optional) (default to 1)
vehicle_license_plate = 'vehicle_license_plate_example' # str |  (optional)
vehicle_speed_cap = 1.2 # float |  (optional)
vehicle_type = 'vehicle_type_example' # str |  (optional)
ev_traffic_speed_table = NULL # object |  (optional)
ev_ascent = 1.2 # float |  (optional)
ev_descent = 1.2 # float |  (optional)
ev_auxiliary_consumption = 1.2 # float |  (optional)
ev_initial_charge = 1.2 # float |  (optional)
ev_max_charge = 1.2 # float |  (optional)
ev_charging_curve = 'ev_charging_curve_example' # str |  (optional)
ev_max_charging_voltage = 1.2 # float |  (optional)
ev_max_charging_current = 1.2 # float |  (optional)
ev_max_charge_after_charging_station = 1.2 # float |  (optional)
ev_min_charge_at_charging_station = 1.2 # float |  (optional)
ev_min_charge_at_first_charging_station = 1.2 # float |  (optional)
ev_min_charge_at_destination = 1.2 # float |  (optional)
ev_charging_setup_duration = 56 # int |  (optional)
ev_connector_types = 'ev_connector_types_example' # str |  (optional)
ev_make_reachable = true # bool |  (optional)
ev_preferred_brands = 'ev_preferred_brands_example' # str |  (optional)
pedestrian_speed = here_public_transit_api.PedestrianSpeed() # PedestrianSpeed | **Disclaimer: This parameter is currently in beta release, and is therefore subject to breaking changes. The parameter could be extracted to a separate API if speed capping for cars/trucks is introduced** Walking speed in meters per second. Influences the duration of walking segments along the route.  (optional)
scooter_allow_highway = false # bool |  (optional) (default to false)
currency = 'currency_example' # str | Currency code compliant to ISO 4217. Costs for the calculated route will be returned using this currency.  If not provided, the router will specify it. On a best-effort basis, the router will try to specify the costs in the local currency.  (optional)
customizations = [here_public_transit_api.CustomizationHRN()] # list[CustomizationHRN] | Specifies a list of customizations to be used. The data provided by these customizations either replaces or augments the standard HERE map data. The provided credentials must authorize access to all of the customizations specified.  **Alpha**: This API is in development. It may not be stable and is subject to change.  (optional)
taxi_allow_drive_through_taxi_roads = true # bool |  (optional) (default to true)
tolls_transponders = 'tolls_transponders_example' # str |  (optional)
tolls_vignettes = 'tolls_vignettes_example' # str |  (optional)
tolls_summaries = ['tolls_summaries_example'] # list[str] |  (optional)
tolls_vehicle_category = 'tolls_vehicle_category_example' # str |  (optional)
tolls_emission_type = 'tolls_emission_type_example' # str |  (optional)
max_speed_on_segment = here_public_transit_api.MaxSpeedOnSegment() # MaxSpeedOnSegment | Specify new base speed for segment by value. Affects route selection and the ETA. Cannot increase base speed on segment.  (optional)
traffic_override_flow_duration = 56 # int |  (optional)

try:
    # Calculate routes via POST
    api_response = api_instance.calculate_routes_post(transport_mode, origin, destination, ev_free_flow_speed_table, body=body, x_request_id=x_request_id, via=via, departure_time=departure_time, arrival_time=arrival_time, routing_mode=routing_mode, alternatives=alternatives, avoid_features=avoid_features, avoid_areas=avoid_areas, avoid_segments=avoid_segments, avoid_zone_categories=avoid_zone_categories, avoid_zone_identifiers=avoid_zone_identifiers, avoid_truck_road_types=avoid_truck_road_types, avoid_toll_transponders=avoid_toll_transponders, exclude_countries=exclude_countries, units=units, lang=lang, _return=_return, spans=spans, truck_shipped_hazardous_goods=truck_shipped_hazardous_goods, truck_gross_weight=truck_gross_weight, truck_weight_per_axle=truck_weight_per_axle, truck_weight_per_axle_group=truck_weight_per_axle_group, truck_height=truck_height, truck_width=truck_width, truck_length=truck_length, truck_tunnel_category=truck_tunnel_category, truck_axle_count=truck_axle_count, truck_trailer_axle_count=truck_trailer_axle_count, truck_tires_count=truck_tires_count, truck_category=truck_category, truck_trailer_count=truck_trailer_count, truck_hov_occupancy=truck_hov_occupancy, truck_license_plate=truck_license_plate, truck_speed_cap=truck_speed_cap, truck_type=truck_type, vehicle_shipped_hazardous_goods=vehicle_shipped_hazardous_goods, vehicle_gross_weight=vehicle_gross_weight, vehicle_weight_per_axle=vehicle_weight_per_axle, vehicle_weight_per_axle_group=vehicle_weight_per_axle_group, vehicle_height=vehicle_height, vehicle_width=vehicle_width, vehicle_length=vehicle_length, vehicle_tunnel_category=vehicle_tunnel_category, vehicle_axle_count=vehicle_axle_count, vehicle_trailer_axle_count=vehicle_trailer_axle_count, vehicle_tires_count=vehicle_tires_count, vehicle_category=vehicle_category, vehicle_trailer_count=vehicle_trailer_count, vehicle_hov_occupancy=vehicle_hov_occupancy, vehicle_license_plate=vehicle_license_plate, vehicle_speed_cap=vehicle_speed_cap, vehicle_type=vehicle_type, ev_traffic_speed_table=ev_traffic_speed_table, ev_ascent=ev_ascent, ev_descent=ev_descent, ev_auxiliary_consumption=ev_auxiliary_consumption, ev_initial_charge=ev_initial_charge, ev_max_charge=ev_max_charge, ev_charging_curve=ev_charging_curve, ev_max_charging_voltage=ev_max_charging_voltage, ev_max_charging_current=ev_max_charging_current, ev_max_charge_after_charging_station=ev_max_charge_after_charging_station, ev_min_charge_at_charging_station=ev_min_charge_at_charging_station, ev_min_charge_at_first_charging_station=ev_min_charge_at_first_charging_station, ev_min_charge_at_destination=ev_min_charge_at_destination, ev_charging_setup_duration=ev_charging_setup_duration, ev_connector_types=ev_connector_types, ev_make_reachable=ev_make_reachable, ev_preferred_brands=ev_preferred_brands, pedestrian_speed=pedestrian_speed, scooter_allow_highway=scooter_allow_highway, currency=currency, customizations=customizations, taxi_allow_drive_through_taxi_roads=taxi_allow_drive_through_taxi_roads, tolls_transponders=tolls_transponders, tolls_vignettes=tolls_vignettes, tolls_summaries=tolls_summaries, tolls_vehicle_category=tolls_vehicle_category, tolls_emission_type=tolls_emission_type, max_speed_on_segment=max_speed_on_segment, traffic_override_flow_duration=traffic_override_flow_duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->calculate_routes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_mode** | [**RouterMode**](.md)| Mode of transport to be used for the calculation of the route.  Note: &#x60;bus&#x60;, &#x60;privateBus&#x60;, and &#x60;taxi&#x60; modes are currently provided as Beta, with limited functionality. The API and behaviour may change drastically, or even become unsupported, without warning. Please refer to the developers&#x27; guide for more details.  | 
 **origin** | [**Waypoint**](.md)| A location defining the origin of the trip.  ## Format  Format: &#x60;Place[WaypointOptions]&#x60;  * Place: &#x60;{lat},{lng}[PlaceOptions]&#x60; * PlaceOptions: &#x60;;option1&#x3D;value1;option2&#x3D;value2...&#x60; * WaypointOptions: &#x60;!option1&#x3D;value1!option2&#x3D;value2...&#x60;  A waypoint consists of:  * Exactly one place * Optional settings for the place * Optional settings for the waypoint itself  Supported place options:  * &#x60;course&#x60;: int, degrees clock-wise from north. Indicating desired direction at the place.   E.g. &#x60;90&#x60; indicating &#x60;east&#x60;. Often combined with &#x60;radius&#x60; and/or &#x60;minCourseDistance&#x60; * &#x60;sideOfStreetHint&#x60;: &#x60;{lat},{lng}&#x60;. Indicating the side of the street that should be   used. E.g. if the location is to the left of the street, the router will prefer using   that side in case the street has dividers. E.g.   &#x60;52.511496,13.304140;sideOfStreetHint&#x3D;52.512149,13.304076&#x60; indicates that the &#x60;north&#x60;   side of the street should be preferred. This option is required, if &#x60;matchSideOfStreet&#x60;   is set to &#x60;always&#x60;. * &#x60;matchSideOfStreet&#x60;: enum &#x60;[always, onlyIfDivided]&#x60;. Specifies how the location set by   &#x60;sideOfStreetHint&#x60; should be handled. Requires &#x60;sideOfStreetHint&#x60; to be specified as   well.   + &#x60;always&#x60; : Always prefer the given side of street.   + &#x60;onlyIfDivided&#x60;: Only prefer using side of street set by &#x60;sideOfStreetHint&#x60; in case     the street has dividers. This is the default behavior. * &#x60;nameHint&#x60;: string. Causes the router to look for the place with the most similar name.   This can e.g. include things like: &#x60;North&#x60; being used to differentiate between   interstates &#x60;I66 North&#x60; and &#x60;I66 South&#x60;, &#x60;Downtown Avenue&#x60; being used to correctly   select a residental street. * &#x60;radius&#x60;: int, meters. Asks the router to consider all places within the given radius as   potential candidates for route calculation. This can be either because it is not   important which place is used, or because it is unknown. Radius more than 200meter are   not supported. * &#x60;minCourseDistance&#x60;: int, meters. Instructs the routing service to try to find a route that avoids actions for the indicated distance.   For example, if the origin is determined by a moving vehicle, the user might not have time to react to early actions. * &#x60;customizationIndex&#x60;: int. Specifies the zero-based index into the list of customizations   specified in the &#x60;customizations&#x60; parameter. The customization at that index must be an   Extension Map.   Providing a &#x60;customizationIndex&#x60; indicates the this waypoint is located within that   Extension Map.   **Alpha**: This customization API parameter is in development. It may not be stable and is subject to change. * &#x60;segmentIdHint&#x60;: string. Causes the router to try and match to the specified segment.   Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint   This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one. * &#x60;onRoadThreshold&#x60;: int, meters. allows specifying a distance within which   the waypoint could be considered as being on a highway/bridge/tunnel/sliproad.   Within this threshold, the attributes of the segments do not impact the matching.   Outside the threshold only segments which aren&#x27;t one of highway/bridge/tunnel/sliproad can be matched.  Notes:  * &#x60;stopDuration&#x60; option is not supported for &#x60;origin&#x60;, contrary to &#x60;destination&#x60; and   &#x60;via&#x60; waypoints. * &#x60;passThrough&#x60;: option is not supported for &#x27;origin&#x27;. * Non-structural reserved characters in options&#x27; values need to be properly percent-encoded.   Please refer to the developers&#x27; guide for more details.  | 
 **destination** | [**Waypoint**](.md)| A location defining the destination of the trip.  ## Format  Format: &#x60;Place[WaypointOptions]&#x60;  * Place: &#x60;{lat},{lng}[PlaceOptions]&#x60; * PlaceOptions: &#x60;;option1&#x3D;value1;option2&#x3D;value2...&#x60; * WaypointOptions: &#x60;!option1&#x3D;value1!option2&#x3D;value2...&#x60;  A waypoint consists of:  * Exactly one place * Optional settings for the place * Optional settings for the waypoint itself  Supported place options:  * &#x60;course&#x60;: int, degrees clock-wise from north. Indicating desired direction at the place.   E.g. &#x60;90&#x60; indicating &#x60;east&#x60;. Often combined with &#x60;radius&#x60; and/or &#x60;minCourseDistance&#x60; * &#x60;sideOfStreetHint&#x60;: &#x60;{lat},{lng}&#x60;. Indicating the side of the street that should be   used. E.g. if the location is to the left of the street, the router will prefer using   that side in case the street has dividers. E.g.   &#x60;52.511496,13.304140;sideOfStreetHint&#x3D;52.512149,13.304076&#x60; indicates that the &#x60;north&#x60;   side of the street should be preferred. This option is required, if &#x60;matchSideOfStreet&#x60;   is set to &#x60;always&#x60;. * &#x60;matchSideOfStreet&#x60;: enum &#x60;[always, onlyIfDivided]&#x60;. Specifies how the location set by   &#x60;sideOfStreetHint&#x60; should be handled. Requires &#x60;sideOfStreetHint&#x60; to be specified as   well.   + &#x60;always&#x60; : Always prefer the given side of street.   + &#x60;onlyIfDivided&#x60;: Only prefer using side of street set by &#x60;sideOfStreetHint&#x60; in case     the street has dividers. This is the default behavior. * &#x60;nameHint&#x60;: string. Causes the router to look for the place with the most similar name.   This can e.g. include things like: &#x60;North&#x60; being used to differentiate between   interstates &#x60;I66 North&#x60; and &#x60;I66 South&#x60;, &#x60;Downtown Avenue&#x60; being used to correctly   select a residental street. * &#x60;radius&#x60;: int, meters. Asks the router to consider all places within the given radius as   potential candidates for route calculation. This can be either because it is not   important which place is used, or because it is unknown. Radius more than 200meter are   not supported. * &#x60;minCourseDistance&#x60;: int, meters. Instructs the routing service to try to find a route that avoids actions for the indicated distance.   For example, if the origin is determined by a moving vehicle, the user might not have time to react to early actions. * &#x60;customizationIndex&#x60;: int. Specifies the zero-based index into the list of customizations   specified in the &#x60;customizations&#x60; parameter. The customization at that index must be an   Extension Map.   Providing a &#x60;customizationIndex&#x60; indicates the this waypoint is located within that   Extension Map.   **Alpha**: This customization API parameter is in development. It may not be stable and is subject to change. * &#x60;segmentIdHint&#x60;: string. Causes the router to try and match to the specified segment.   Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint   This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one. * &#x60;onRoadThreshold&#x60;: int, meters. allows specifying a distance within which   the waypoint could be considered as being on a highway/bridge/tunnel/sliproad.   Within this threshold, the attributes of the segments do not impact the matching.   Outside the threshold only segments which aren&#x27;t one of highway/bridge/tunnel/sliproad can be matched.  Supported waypoint options:  * &#x60;stopDuration&#x60;: desired duration for the stop, in seconds. The section arriving at this   via waypoint will have a &#x60;wait&#x60; post action reflecting the stopping time. The   consecutive section will start at the arrival time of the former section + stop   duration. * &#x60;passThrough&#x60;: option is not supported for &#x27;destination&#x27;.  Notes:  * Non-structural reserved characters in options&#x27; values need to be properly percent-encoded.   Please refer to the developers&#x27; guide for more details.  | 
 **ev_free_flow_speed_table** | [**object**](.md)|  | 
 **body** | [**CalculateRoutesPostParameters**](CalculateRoutesPostParameters.md)|  | [optional] 
 **x_request_id** | **str**| User-provided token that can be used to trace a request or a group of requests sent to the service. | [optional] 
 **via** | [**list[Waypoint]**](Waypoint.md)| A location defining a via waypoint.  A via waypoint is a location between origin and destination. The route will do a stop at the via waypoint.  Multiple waypoints can also be specified using multiple via parameters like &#x60;via&#x3D;...&amp;via&#x3D;...&#x60;, in which case the route will traverse these waypoints sequentially in the order specified in the request.  ## Format  Format: &#x60;Place[WaypointOptions]&#x60;  * Place: &#x60;{lat},{lng}[PlaceOptions]&#x60; * PlaceOptions: &#x60;;option1&#x3D;value1;option2&#x3D;value2...&#x60; * WaypointOptions: &#x60;!option1&#x3D;value1!option2&#x3D;value2...&#x60;  A waypoint consists of:  * Exactly one place * Optional settings for the place * Optional settings for the waypoint itself  Supported place options:  * &#x60;course&#x60;: int, degrees clock-wise from north. Indicating desired direction at the place.   E.g. &#x60;90&#x60; indicating &#x60;east&#x60;. Often combined with &#x60;radius&#x60; and/or &#x60;minCourseDistance&#x60; * &#x60;sideOfStreetHint&#x60;: &#x60;{lat},{lng}&#x60;. Indicating the side of the street that should be   used. E.g. if the location is to the left of the street, the router will prefer using   that side in case the street has dividers. E.g.   &#x60;52.511496,13.304140;sideOfStreetHint&#x3D;52.512149,13.304076&#x60; indicates that the &#x60;north&#x60;   side of the street should be preferred. This option is required, if &#x60;matchSideOfStreet&#x60;   is set to &#x60;always&#x60;. * &#x60;matchSideOfStreet&#x60;: enum &#x60;[always, onlyIfDivided]&#x60;. Specifies how the location set by   &#x60;sideOfStreetHint&#x60; should be handled. Requires &#x60;sideOfStreetHint&#x60; to be specified as   well.   + &#x60;always&#x60; : Always prefer the given side of street.   + &#x60;onlyIfDivided&#x60;: Only prefer using side of street set by &#x60;sideOfStreetHint&#x60; in case     the street has dividers. This is the default behavior. * &#x60;nameHint&#x60;: string. Causes the router to look for the place with the most similar name.   This can e.g. include things like: &#x60;North&#x60; being used to differentiate between   interstates &#x60;I66 North&#x60; and &#x60;I66 South&#x60;, &#x60;Downtown Avenue&#x60; being used to correctly   select a residental street. * &#x60;radius&#x60;: int, meters. Asks the router to consider all places within the given radius as   potential candidates for route calculation. This can be either because it is not   important which place is used, or because it is unknown. Radius more than 200meter are   not supported. * &#x60;minCourseDistance&#x60;: int, meters. Instructs the routing service to try to find a route that avoids actions for the indicated distance.   For example, if the origin is determined by a moving vehicle, the user might not have time to react to early actions. * &#x60;customizationIndex&#x60;: int. Specifies the zero-based index into the list of customizations   specified in the &#x60;customizations&#x60; parameter. The customization at that index must be an   Extension Map.   Providing a &#x60;customizationIndex&#x60; indicates the this waypoint is located within that   Extension Map.   **Alpha**: This customization API parameter is in development. It may not be stable and is subject to change. * &#x60;segmentIdHint&#x60;: string. Causes the router to try and match to the specified segment.   Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint   This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one. * &#x60;onRoadThreshold&#x60;: int, meters. allows specifying a distance within which   the waypoint could be considered as being on a highway/bridge/tunnel/sliproad.   Within this threshold, the attributes of the segments do not impact the matching.   Outside the threshold only segments which aren&#x27;t one of highway/bridge/tunnel/sliproad can be matched.  Supported waypoint options: * &#x60;stopDuration&#x60;: desired duration for the stop, in seconds. * &#x60;passThrough&#x60;: boolean. Asks the router to avoid the following during route calculation:   + Introducing a stop at the waypoint.   + Splitting the route into sections.   + Changing the direction of travel.    Following scenarios are not supported for &#x60;passThrough&#x60; parameter:   + Setting both &#x60;stopDuration&#x60; to a value greater than 0 and &#x60;passThrough&#x3D;true&#x60;.   + Setting &#x60;passThrough&#x3D;true&#x60; for &#x60;origin&#x60; or &#x60;destination&#x60; of a route.   The default value is &#x60;false&#x60;.  Notes:  * Non-structural reserved characters in options&#x27; values need to be properly percent-encoded.   Please refer to the developers&#x27; guide for more details.  | [optional] 
 **departure_time** | [**TimeWithAny**](.md)| Specifies the time of departure as defined by either &#x60;date-time&#x60; or &#x60;full-date&#x60; &#x60;T&#x60; &#x60;partial-time&#x60; in &#x60;RFC 3339&#x60;, section 5.6 (for example, &#x60;2019-06-24T01:23:45&#x60;).  The requested time is converted to local time at origin. When the optional timezone offset is not specified, time is assumed to be local. The special value &#x60;any&#x60; can be used to indicate that time should not be taken into account during routing. If neither &#x60;departureTime&#x60; or &#x60;arrivalTime&#x60; are specified, current time at departure place will be used. All time values in the response are returned in the timezone of each location.  | [optional] 
 **arrival_time** | [**Time**](.md)| Specifies the time of arrival as defined by either &#x60;date-time&#x60; or &#x60;full-date&#x60; &#x60;T&#x60; &#x60;partial-time&#x60; in &#x60;RFC 3339&#x60;, section 5.6 (for example, &#x60;2019-06-24T01:23:45&#x60;). The requested time is converted to the local time at destination. When the optional timezone offset is not specified, time is assumed to be local. All &#x60;Time&#x60; values in the response are returned in the timezone of each location.  Note : The following features do not support the arrivalTime parameter: * EV Routing * Route Handle * Route Import  | [optional] 
 **routing_mode** | [**RoutingMode**](.md)| Specifies which optimization is applied during route calculation.  * &#x60;fast&#x60;: Route calculation from start to destination optimized by travel time. In many   cases, the route returned by the &#x60;fast&#x60; mode may not be the route with the fastest   possible travel time. For example, the routing service may favor a route that remains on   a highway, even if a faster travel time can be achieved by taking a detour or shortcut   through an inconvenient side road. * &#x60;short&#x60;: Route calculation from start to destination disregarding any speed information.   In this mode, the distance of the route is minimized, while keeping the route sensible.   This includes, for example, penalizing turns. Because of that, the resulting route will   not necessarily be the one with minimal distance.  Notes: * The following Transport modes only support &#x60;fast&#x60; routingMode   - &#x60;bicycle&#x60;   - &#x60;bus&#x60;   - &#x60;pedestrian&#x60;   - &#x60;privateBus&#x60;   - &#x60;scooter&#x60;   - &#x60;taxi&#x60;  | [optional] 
 **alternatives** | **int**| Number of alternative routes to return aside from the optimal route. | [optional] [default to 0]
 **avoid_features** | **str**|  | [optional] 
 **avoid_areas** | **str**|  | [optional] 
 **avoid_segments** | **str**|  | [optional] 
 **avoid_zone_categories** | **str**|  | [optional] 
 **avoid_zone_identifiers** | **str**|  | [optional] 
 **avoid_truck_road_types** | **str**|  | [optional] 
 **avoid_toll_transponders** | **str**|  | [optional] 
 **exclude_countries** | **str**|  | [optional] 
 **units** | [**Units**](.md)| Units of measurement used in guidance instructions. The default is &#x60;metric&#x60;.  | [optional] 
 **lang** | [**list[str]**](str.md)| Specifies the list of preferred languages of the response. The first supported language from the list will be used for for the response. The value should comply with the [IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). A list of supported languages for the routing service can be found in the dev guide https://developer.here.com/documentation/routing-api/dev_guide/topics/languages.html.  Note: If the first language in the list is not supported, an info notification will be generated with code &#x60;mainLanguageNotFound&#x60;.  | [optional] [default to [&quot;en-US&quot;]]
 **_return** | [**list[ModelReturn]**](ModelReturn.md)|  | [optional] 
 **spans** | [**list[Spans]**](Spans.md)| Defines which map content attributes are included in the response spans. For example, &#x60;attributes,length&#x60; will enable the fields &#x60;attributes&#x60; and &#x60;length&#x60; in the route response. For more information about the &#x60;countryCode&#x60; field, see https://www.iso.org/obp/ui/#search.  This parameter also requires that the &#x60;polyline&#x60; option is set within the &#x60;return&#x60; parameter.  | [optional] 
 **truck_shipped_hazardous_goods** | **str**|  | [optional] 
 **truck_gross_weight** | **int**|  | [optional] 
 **truck_weight_per_axle** | **int**|  | [optional] 
 **truck_weight_per_axle_group** | **str**|  | [optional] 
 **truck_height** | **int**|  | [optional] 
 **truck_width** | **int**|  | [optional] 
 **truck_length** | **int**|  | [optional] 
 **truck_tunnel_category** | **str**|  | [optional] 
 **truck_axle_count** | **int**|  | [optional] 
 **truck_trailer_axle_count** | **int**|  | [optional] 
 **truck_tires_count** | **int**|  | [optional] 
 **truck_category** | **str**|  | [optional] [default to undefined]
 **truck_trailer_count** | **int**|  | [optional] [default to 0]
 **truck_hov_occupancy** | **int**|  | [optional] [default to 1]
 **truck_license_plate** | **str**|  | [optional] 
 **truck_speed_cap** | **float**|  | [optional] 
 **truck_type** | **str**|  | [optional] [default to straight]
 **vehicle_shipped_hazardous_goods** | **str**|  | [optional] 
 **vehicle_gross_weight** | **int**|  | [optional] 
 **vehicle_weight_per_axle** | **int**|  | [optional] 
 **vehicle_weight_per_axle_group** | **str**|  | [optional] 
 **vehicle_height** | **int**|  | [optional] 
 **vehicle_width** | **int**|  | [optional] 
 **vehicle_length** | **int**|  | [optional] 
 **vehicle_tunnel_category** | **str**|  | [optional] 
 **vehicle_axle_count** | **int**|  | [optional] 
 **vehicle_trailer_axle_count** | **int**|  | [optional] 
 **vehicle_tires_count** | **int**|  | [optional] 
 **vehicle_category** | **str**|  | [optional] [default to undefined]
 **vehicle_trailer_count** | **int**|  | [optional] [default to 0]
 **vehicle_hov_occupancy** | **int**|  | [optional] [default to 1]
 **vehicle_license_plate** | **str**|  | [optional] 
 **vehicle_speed_cap** | **float**|  | [optional] 
 **vehicle_type** | **str**|  | [optional] 
 **ev_traffic_speed_table** | [**object**](.md)|  | [optional] 
 **ev_ascent** | **float**|  | [optional] 
 **ev_descent** | **float**|  | [optional] 
 **ev_auxiliary_consumption** | **float**|  | [optional] 
 **ev_initial_charge** | **float**|  | [optional] 
 **ev_max_charge** | **float**|  | [optional] 
 **ev_charging_curve** | **str**|  | [optional] 
 **ev_max_charging_voltage** | **float**|  | [optional] 
 **ev_max_charging_current** | **float**|  | [optional] 
 **ev_max_charge_after_charging_station** | **float**|  | [optional] 
 **ev_min_charge_at_charging_station** | **float**|  | [optional] 
 **ev_min_charge_at_first_charging_station** | **float**|  | [optional] 
 **ev_min_charge_at_destination** | **float**|  | [optional] 
 **ev_charging_setup_duration** | **int**|  | [optional] 
 **ev_connector_types** | **str**|  | [optional] 
 **ev_make_reachable** | **bool**|  | [optional] 
 **ev_preferred_brands** | **str**|  | [optional] 
 **pedestrian_speed** | [**PedestrianSpeed**](.md)| **Disclaimer: This parameter is currently in beta release, and is therefore subject to breaking changes. The parameter could be extracted to a separate API if speed capping for cars/trucks is introduced** Walking speed in meters per second. Influences the duration of walking segments along the route.  | [optional] 
 **scooter_allow_highway** | **bool**|  | [optional] [default to false]
 **currency** | **str**| Currency code compliant to ISO 4217. Costs for the calculated route will be returned using this currency.  If not provided, the router will specify it. On a best-effort basis, the router will try to specify the costs in the local currency.  | [optional] 
 **customizations** | [**list[CustomizationHRN]**](CustomizationHRN.md)| Specifies a list of customizations to be used. The data provided by these customizations either replaces or augments the standard HERE map data. The provided credentials must authorize access to all of the customizations specified.  **Alpha**: This API is in development. It may not be stable and is subject to change.  | [optional] 
 **taxi_allow_drive_through_taxi_roads** | **bool**|  | [optional] [default to true]
 **tolls_transponders** | **str**|  | [optional] 
 **tolls_vignettes** | **str**|  | [optional] 
 **tolls_summaries** | [**list[str]**](str.md)|  | [optional] 
 **tolls_vehicle_category** | **str**|  | [optional] 
 **tolls_emission_type** | **str**|  | [optional] 
 **max_speed_on_segment** | [**MaxSpeedOnSegment**](.md)| Specify new base speed for segment by value. Affects route selection and the ETA. Cannot increase base speed on segment.  | [optional] 
 **traffic_override_flow_duration** | **int**|  | [optional] 

### Return type

[**RouterRouteResponse**](RouterRouteResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routes_by_handle**
> RouterRouteResponse get_routes_by_handle(route_handle, transport_mode, ev_free_flow_speed_table, origin=origin, departure_time=departure_time, avoid_features=avoid_features, avoid_areas=avoid_areas, avoid_segments=avoid_segments, avoid_zone_categories=avoid_zone_categories, avoid_zone_identifiers=avoid_zone_identifiers, avoid_truck_road_types=avoid_truck_road_types, avoid_toll_transponders=avoid_toll_transponders, exclude_countries=exclude_countries, units=units, lang=lang, _return=_return, spans=spans, truck_shipped_hazardous_goods=truck_shipped_hazardous_goods, truck_gross_weight=truck_gross_weight, truck_weight_per_axle=truck_weight_per_axle, truck_weight_per_axle_group=truck_weight_per_axle_group, truck_height=truck_height, truck_width=truck_width, truck_length=truck_length, truck_tunnel_category=truck_tunnel_category, truck_axle_count=truck_axle_count, truck_trailer_axle_count=truck_trailer_axle_count, truck_tires_count=truck_tires_count, truck_category=truck_category, truck_trailer_count=truck_trailer_count, truck_hov_occupancy=truck_hov_occupancy, truck_license_plate=truck_license_plate, truck_speed_cap=truck_speed_cap, truck_type=truck_type, vehicle_shipped_hazardous_goods=vehicle_shipped_hazardous_goods, vehicle_gross_weight=vehicle_gross_weight, vehicle_weight_per_axle=vehicle_weight_per_axle, vehicle_weight_per_axle_group=vehicle_weight_per_axle_group, vehicle_height=vehicle_height, vehicle_width=vehicle_width, vehicle_length=vehicle_length, vehicle_tunnel_category=vehicle_tunnel_category, vehicle_axle_count=vehicle_axle_count, vehicle_trailer_axle_count=vehicle_trailer_axle_count, vehicle_tires_count=vehicle_tires_count, vehicle_category=vehicle_category, vehicle_trailer_count=vehicle_trailer_count, vehicle_hov_occupancy=vehicle_hov_occupancy, vehicle_license_plate=vehicle_license_plate, vehicle_speed_cap=vehicle_speed_cap, vehicle_type=vehicle_type, ev_traffic_speed_table=ev_traffic_speed_table, ev_ascent=ev_ascent, ev_descent=ev_descent, ev_auxiliary_consumption=ev_auxiliary_consumption, ev_initial_charge=ev_initial_charge, ev_max_charge=ev_max_charge, ev_charging_curve=ev_charging_curve, ev_max_charging_voltage=ev_max_charging_voltage, ev_max_charging_current=ev_max_charging_current, ev_max_charge_after_charging_station=ev_max_charge_after_charging_station, ev_min_charge_at_charging_station=ev_min_charge_at_charging_station, ev_min_charge_at_first_charging_station=ev_min_charge_at_first_charging_station, ev_min_charge_at_destination=ev_min_charge_at_destination, ev_charging_setup_duration=ev_charging_setup_duration, ev_connector_types=ev_connector_types, pedestrian_speed=pedestrian_speed, x_request_id=x_request_id, scooter_allow_highway=scooter_allow_highway, currency=currency, rerouting_mode=rerouting_mode, rerouting_last_traveled_section_index=rerouting_last_traveled_section_index, rerouting_traveled_distance_on_last_section=rerouting_traveled_distance_on_last_section, taxi_allow_drive_through_taxi_roads=taxi_allow_drive_through_taxi_roads, tolls_transponders=tolls_transponders, tolls_vignettes=tolls_vignettes, tolls_summaries=tolls_summaries, tolls_vehicle_category=tolls_vehicle_category, tolls_emission_type=tolls_emission_type, max_speed_on_segment=max_speed_on_segment, traffic_override_flow_duration=traffic_override_flow_duration)

Get route by handle via GET

Decodes and returns a route from a previously calculated route handle.  **Disclaimer: A route handle is not suitable for persistent route storage! It can be invalidated at any time.**  A route handle encodes a previously calculated route. A route can be decoded from a handle as long as the service uses the same map data and encoding that were used when retrieving the handle.  Thus it is suitable for caching routes compactly. It can be used to retrieve updated traffic information or other data along the route. However, a user should be prepared to recalculate the route when decoding the handle fails.  All parameters of the `/routes` endpoint are supported, except for `destination`, `via`, `alternatives` and `routingMode`. See also the `return` parameter of `/routes` endpoint.  The `origin` parameter can be provided to update the start of the previously calculated route.  The `transportMode` parameter does not have to match the transport mode previously used for route calculation. However, when using a different transport mode, the request may fail, e.g. when the route has road segments forbidden for the provided transport mode.  Please refer to the developers' guide for more information and examples. 

### Example
```python
from __future__ import print_function
import time
import here_public_transit_api
from here_public_transit_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = here_public_transit_api.Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = here_public_transit_api.RoutingApi(here_public_transit_api.ApiClient(configuration))
route_handle = 'route_handle_example' # str | Route handle returned from a previous route calculation.  See `return` parameter of `/routes` endpoint for more information. 
transport_mode = here_public_transit_api.RouterMode() # RouterMode | Mode of transport to be used for the calculation of the route.  Note: `bus`, `privateBus`, and `taxi` modes are currently provided as Beta, with limited functionality. The API and behaviour may change drastically, or even become unsupported, without warning. Please refer to the developers' guide for more details. 
ev_free_flow_speed_table = NULL # object | 
origin = here_public_transit_api.Waypoint() # Waypoint | A location defining the origin of the trip. The origin has to be located along the previously calculated route.  ## Format  Format: `Place[WaypointOptions]`  * Place: `{lat},{lng}[PlaceOptions]` * PlaceOptions: `;option1=value1;option2=value2...` * WaypointOptions: `!option1=value1!option2=value2...`  A waypoint consists of:  * Exactly one place * Optional settings for the place * Optional settings for the waypoint itself  Supported place options:  * `course`: int, degrees clock-wise from north. Indicating desired direction at the place.   E.g. `90` indicating `east`. Often combined with `radius` and/or `minCourseDistance` * `sideOfStreetHint`: `{lat},{lng}`. Indicating the side of the street that should be   used. E.g. if the location is to the left of the street, the router will prefer using   that side in case the street has dividers. E.g.   `52.511496,13.304140;sideOfStreetHint=52.512149,13.304076` indicates that the `north`   side of the street should be preferred. This option is required, if `matchSideOfStreet`   is set to `always`. * `matchSideOfStreet`: enum `[always, onlyIfDivided]`. Specifies how the location set by   `sideOfStreetHint` should be handled. Requires `sideOfStreetHint` to be specified as   well.   + `always` : Always prefer the given side of street.   + `onlyIfDivided`: Only prefer using side of street set by `sideOfStreetHint` in case     the street has dividers. This is the default behavior. * `nameHint`: string. Causes the router to look for the place with the most similar name.   This can e.g. include things like: `North` being used to differentiate between   interstates `I66 North` and `I66 South`, `Downtown Avenue` being used to correctly   select a residental street. * `radius`: int, meters. Asks the router to consider all places within the given radius as   potential candidates for route calculation. This can be either because it is not   important which place is used, or because it is unknown. Radius more than 200meter are   not supported.  Notes:  * `stopDuration` option is not supported for `origin`, contrary to `destination` and   `via` waypoints. * `passThrough`: option is not supported for 'origin'. * Non-structural reserved characters in options' values need to be properly percent-encoded.   Please refer to the developers' guide for more details. * `minCourseDistance`: While this parameter can be provided for compatibility reasons,   it will not affect the result of a getRoutesByHandle request.  (optional)
departure_time = here_public_transit_api.TimeWithAny() # TimeWithAny | Specifies the time of departure as defined by either `date-time` or `full-date` `T` `partial-time` in `RFC 3339`, section 5.6 (for example, `2019-06-24T01:23:45`).  The requested time is converted to local time at origin. When the optional timezone offset is not specified, time is assumed to be local. The special value `any` can be used to indicate that time should not be taken into account during routing. If neither `departureTime` or `arrivalTime` are specified, current time at departure place will be used. All time values in the response are returned in the timezone of each location.  (optional)
avoid_features = 'avoid_features_example' # str |  (optional)
avoid_areas = 'avoid_areas_example' # str |  (optional)
avoid_segments = 'avoid_segments_example' # str |  (optional)
avoid_zone_categories = 'avoid_zone_categories_example' # str |  (optional)
avoid_zone_identifiers = 'avoid_zone_identifiers_example' # str |  (optional)
avoid_truck_road_types = 'avoid_truck_road_types_example' # str |  (optional)
avoid_toll_transponders = 'avoid_toll_transponders_example' # str |  (optional)
exclude_countries = 'exclude_countries_example' # str |  (optional)
units = here_public_transit_api.Units() # Units | Units of measurement used in guidance instructions. The default is `metric`.  (optional)
lang = ['[\"en-US\"]'] # list[str] | Specifies the list of preferred languages of the response. The first supported language from the list will be used for for the response. The value should comply with the [IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). A list of supported languages for the routing service can be found in the dev guide https://developer.here.com/documentation/routing-api/dev_guide/topics/languages.html.  Note: If the first language in the list is not supported, an info notification will be generated with code `mainLanguageNotFound`.  (optional) (default to ["en-US"])
_return = [here_public_transit_api.ModelReturn()] # list[ModelReturn] |  (optional)
spans = [here_public_transit_api.Spans()] # list[Spans] | Defines which map content attributes are included in the response spans. For example, `attributes,length` will enable the fields `attributes` and `length` in the route response. For more information about the `countryCode` field, see https://www.iso.org/obp/ui/#search.  This parameter also requires that the `polyline` option is set within the `return` parameter.  (optional)
truck_shipped_hazardous_goods = 'truck_shipped_hazardous_goods_example' # str |  (optional)
truck_gross_weight = 56 # int |  (optional)
truck_weight_per_axle = 56 # int |  (optional)
truck_weight_per_axle_group = 'truck_weight_per_axle_group_example' # str |  (optional)
truck_height = 56 # int |  (optional)
truck_width = 56 # int |  (optional)
truck_length = 56 # int |  (optional)
truck_tunnel_category = 'truck_tunnel_category_example' # str |  (optional)
truck_axle_count = 56 # int |  (optional)
truck_trailer_axle_count = 56 # int |  (optional)
truck_tires_count = 56 # int |  (optional)
truck_category = 'undefined' # str |  (optional) (default to undefined)
truck_trailer_count = 0 # int |  (optional) (default to 0)
truck_hov_occupancy = 1 # int |  (optional) (default to 1)
truck_license_plate = 'truck_license_plate_example' # str |  (optional)
truck_speed_cap = 1.2 # float |  (optional)
truck_type = 'straight' # str |  (optional) (default to straight)
vehicle_shipped_hazardous_goods = 'vehicle_shipped_hazardous_goods_example' # str |  (optional)
vehicle_gross_weight = 56 # int |  (optional)
vehicle_weight_per_axle = 56 # int |  (optional)
vehicle_weight_per_axle_group = 'vehicle_weight_per_axle_group_example' # str |  (optional)
vehicle_height = 56 # int |  (optional)
vehicle_width = 56 # int |  (optional)
vehicle_length = 56 # int |  (optional)
vehicle_tunnel_category = 'vehicle_tunnel_category_example' # str |  (optional)
vehicle_axle_count = 56 # int |  (optional)
vehicle_trailer_axle_count = 56 # int |  (optional)
vehicle_tires_count = 56 # int |  (optional)
vehicle_category = 'undefined' # str |  (optional) (default to undefined)
vehicle_trailer_count = 0 # int |  (optional) (default to 0)
vehicle_hov_occupancy = 1 # int |  (optional) (default to 1)
vehicle_license_plate = 'vehicle_license_plate_example' # str |  (optional)
vehicle_speed_cap = 1.2 # float |  (optional)
vehicle_type = 'vehicle_type_example' # str |  (optional)
ev_traffic_speed_table = NULL # object |  (optional)
ev_ascent = 1.2 # float |  (optional)
ev_descent = 1.2 # float |  (optional)
ev_auxiliary_consumption = 1.2 # float |  (optional)
ev_initial_charge = 1.2 # float |  (optional)
ev_max_charge = 1.2 # float |  (optional)
ev_charging_curve = 'ev_charging_curve_example' # str |  (optional)
ev_max_charging_voltage = 1.2 # float |  (optional)
ev_max_charging_current = 1.2 # float |  (optional)
ev_max_charge_after_charging_station = 1.2 # float |  (optional)
ev_min_charge_at_charging_station = 1.2 # float |  (optional)
ev_min_charge_at_first_charging_station = 1.2 # float |  (optional)
ev_min_charge_at_destination = 1.2 # float |  (optional)
ev_charging_setup_duration = 56 # int |  (optional)
ev_connector_types = 'ev_connector_types_example' # str |  (optional)
pedestrian_speed = here_public_transit_api.PedestrianSpeed() # PedestrianSpeed | **Disclaimer: This parameter is currently in beta release, and is therefore subject to breaking changes. The parameter could be extracted to a separate API if speed capping for cars/trucks is introduced** Walking speed in meters per second. Influences the duration of walking segments along the route.  (optional)
x_request_id = 'x_request_id_example' # str | User-provided token that can be used to trace a request or a group of requests sent to the service. (optional)
scooter_allow_highway = false # bool |  (optional) (default to false)
currency = 'currency_example' # str | Currency code compliant to ISO 4217. Costs for the calculated route will be returned using this currency.  If not provided, the router will specify it. On a best-effort basis, the router will try to specify the costs in the local currency.  (optional)
rerouting_mode = 'rerouting_mode_example' # str |  (optional)
rerouting_last_traveled_section_index = 0 # int |  (optional) (default to 0)
rerouting_traveled_distance_on_last_section = 0 # int |  (optional) (default to 0)
taxi_allow_drive_through_taxi_roads = true # bool |  (optional) (default to true)
tolls_transponders = 'tolls_transponders_example' # str |  (optional)
tolls_vignettes = 'tolls_vignettes_example' # str |  (optional)
tolls_summaries = ['tolls_summaries_example'] # list[str] |  (optional)
tolls_vehicle_category = 'tolls_vehicle_category_example' # str |  (optional)
tolls_emission_type = 'tolls_emission_type_example' # str |  (optional)
max_speed_on_segment = here_public_transit_api.MaxSpeedOnSegment() # MaxSpeedOnSegment | Specify new base speed for segment by value. Affects route selection and the ETA. Cannot increase base speed on segment.  (optional)
traffic_override_flow_duration = 56 # int |  (optional)

try:
    # Get route by handle via GET
    api_response = api_instance.get_routes_by_handle(route_handle, transport_mode, ev_free_flow_speed_table, origin=origin, departure_time=departure_time, avoid_features=avoid_features, avoid_areas=avoid_areas, avoid_segments=avoid_segments, avoid_zone_categories=avoid_zone_categories, avoid_zone_identifiers=avoid_zone_identifiers, avoid_truck_road_types=avoid_truck_road_types, avoid_toll_transponders=avoid_toll_transponders, exclude_countries=exclude_countries, units=units, lang=lang, _return=_return, spans=spans, truck_shipped_hazardous_goods=truck_shipped_hazardous_goods, truck_gross_weight=truck_gross_weight, truck_weight_per_axle=truck_weight_per_axle, truck_weight_per_axle_group=truck_weight_per_axle_group, truck_height=truck_height, truck_width=truck_width, truck_length=truck_length, truck_tunnel_category=truck_tunnel_category, truck_axle_count=truck_axle_count, truck_trailer_axle_count=truck_trailer_axle_count, truck_tires_count=truck_tires_count, truck_category=truck_category, truck_trailer_count=truck_trailer_count, truck_hov_occupancy=truck_hov_occupancy, truck_license_plate=truck_license_plate, truck_speed_cap=truck_speed_cap, truck_type=truck_type, vehicle_shipped_hazardous_goods=vehicle_shipped_hazardous_goods, vehicle_gross_weight=vehicle_gross_weight, vehicle_weight_per_axle=vehicle_weight_per_axle, vehicle_weight_per_axle_group=vehicle_weight_per_axle_group, vehicle_height=vehicle_height, vehicle_width=vehicle_width, vehicle_length=vehicle_length, vehicle_tunnel_category=vehicle_tunnel_category, vehicle_axle_count=vehicle_axle_count, vehicle_trailer_axle_count=vehicle_trailer_axle_count, vehicle_tires_count=vehicle_tires_count, vehicle_category=vehicle_category, vehicle_trailer_count=vehicle_trailer_count, vehicle_hov_occupancy=vehicle_hov_occupancy, vehicle_license_plate=vehicle_license_plate, vehicle_speed_cap=vehicle_speed_cap, vehicle_type=vehicle_type, ev_traffic_speed_table=ev_traffic_speed_table, ev_ascent=ev_ascent, ev_descent=ev_descent, ev_auxiliary_consumption=ev_auxiliary_consumption, ev_initial_charge=ev_initial_charge, ev_max_charge=ev_max_charge, ev_charging_curve=ev_charging_curve, ev_max_charging_voltage=ev_max_charging_voltage, ev_max_charging_current=ev_max_charging_current, ev_max_charge_after_charging_station=ev_max_charge_after_charging_station, ev_min_charge_at_charging_station=ev_min_charge_at_charging_station, ev_min_charge_at_first_charging_station=ev_min_charge_at_first_charging_station, ev_min_charge_at_destination=ev_min_charge_at_destination, ev_charging_setup_duration=ev_charging_setup_duration, ev_connector_types=ev_connector_types, pedestrian_speed=pedestrian_speed, x_request_id=x_request_id, scooter_allow_highway=scooter_allow_highway, currency=currency, rerouting_mode=rerouting_mode, rerouting_last_traveled_section_index=rerouting_last_traveled_section_index, rerouting_traveled_distance_on_last_section=rerouting_traveled_distance_on_last_section, taxi_allow_drive_through_taxi_roads=taxi_allow_drive_through_taxi_roads, tolls_transponders=tolls_transponders, tolls_vignettes=tolls_vignettes, tolls_summaries=tolls_summaries, tolls_vehicle_category=tolls_vehicle_category, tolls_emission_type=tolls_emission_type, max_speed_on_segment=max_speed_on_segment, traffic_override_flow_duration=traffic_override_flow_duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routes_by_handle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_handle** | **str**| Route handle returned from a previous route calculation.  See &#x60;return&#x60; parameter of &#x60;/routes&#x60; endpoint for more information.  | 
 **transport_mode** | [**RouterMode**](.md)| Mode of transport to be used for the calculation of the route.  Note: &#x60;bus&#x60;, &#x60;privateBus&#x60;, and &#x60;taxi&#x60; modes are currently provided as Beta, with limited functionality. The API and behaviour may change drastically, or even become unsupported, without warning. Please refer to the developers&#x27; guide for more details.  | 
 **ev_free_flow_speed_table** | [**object**](.md)|  | 
 **origin** | [**Waypoint**](.md)| A location defining the origin of the trip. The origin has to be located along the previously calculated route.  ## Format  Format: &#x60;Place[WaypointOptions]&#x60;  * Place: &#x60;{lat},{lng}[PlaceOptions]&#x60; * PlaceOptions: &#x60;;option1&#x3D;value1;option2&#x3D;value2...&#x60; * WaypointOptions: &#x60;!option1&#x3D;value1!option2&#x3D;value2...&#x60;  A waypoint consists of:  * Exactly one place * Optional settings for the place * Optional settings for the waypoint itself  Supported place options:  * &#x60;course&#x60;: int, degrees clock-wise from north. Indicating desired direction at the place.   E.g. &#x60;90&#x60; indicating &#x60;east&#x60;. Often combined with &#x60;radius&#x60; and/or &#x60;minCourseDistance&#x60; * &#x60;sideOfStreetHint&#x60;: &#x60;{lat},{lng}&#x60;. Indicating the side of the street that should be   used. E.g. if the location is to the left of the street, the router will prefer using   that side in case the street has dividers. E.g.   &#x60;52.511496,13.304140;sideOfStreetHint&#x3D;52.512149,13.304076&#x60; indicates that the &#x60;north&#x60;   side of the street should be preferred. This option is required, if &#x60;matchSideOfStreet&#x60;   is set to &#x60;always&#x60;. * &#x60;matchSideOfStreet&#x60;: enum &#x60;[always, onlyIfDivided]&#x60;. Specifies how the location set by   &#x60;sideOfStreetHint&#x60; should be handled. Requires &#x60;sideOfStreetHint&#x60; to be specified as   well.   + &#x60;always&#x60; : Always prefer the given side of street.   + &#x60;onlyIfDivided&#x60;: Only prefer using side of street set by &#x60;sideOfStreetHint&#x60; in case     the street has dividers. This is the default behavior. * &#x60;nameHint&#x60;: string. Causes the router to look for the place with the most similar name.   This can e.g. include things like: &#x60;North&#x60; being used to differentiate between   interstates &#x60;I66 North&#x60; and &#x60;I66 South&#x60;, &#x60;Downtown Avenue&#x60; being used to correctly   select a residental street. * &#x60;radius&#x60;: int, meters. Asks the router to consider all places within the given radius as   potential candidates for route calculation. This can be either because it is not   important which place is used, or because it is unknown. Radius more than 200meter are   not supported.  Notes:  * &#x60;stopDuration&#x60; option is not supported for &#x60;origin&#x60;, contrary to &#x60;destination&#x60; and   &#x60;via&#x60; waypoints. * &#x60;passThrough&#x60;: option is not supported for &#x27;origin&#x27;. * Non-structural reserved characters in options&#x27; values need to be properly percent-encoded.   Please refer to the developers&#x27; guide for more details. * &#x60;minCourseDistance&#x60;: While this parameter can be provided for compatibility reasons,   it will not affect the result of a getRoutesByHandle request.  | [optional] 
 **departure_time** | [**TimeWithAny**](.md)| Specifies the time of departure as defined by either &#x60;date-time&#x60; or &#x60;full-date&#x60; &#x60;T&#x60; &#x60;partial-time&#x60; in &#x60;RFC 3339&#x60;, section 5.6 (for example, &#x60;2019-06-24T01:23:45&#x60;).  The requested time is converted to local time at origin. When the optional timezone offset is not specified, time is assumed to be local. The special value &#x60;any&#x60; can be used to indicate that time should not be taken into account during routing. If neither &#x60;departureTime&#x60; or &#x60;arrivalTime&#x60; are specified, current time at departure place will be used. All time values in the response are returned in the timezone of each location.  | [optional] 
 **avoid_features** | **str**|  | [optional] 
 **avoid_areas** | **str**|  | [optional] 
 **avoid_segments** | **str**|  | [optional] 
 **avoid_zone_categories** | **str**|  | [optional] 
 **avoid_zone_identifiers** | **str**|  | [optional] 
 **avoid_truck_road_types** | **str**|  | [optional] 
 **avoid_toll_transponders** | **str**|  | [optional] 
 **exclude_countries** | **str**|  | [optional] 
 **units** | [**Units**](.md)| Units of measurement used in guidance instructions. The default is &#x60;metric&#x60;.  | [optional] 
 **lang** | [**list[str]**](str.md)| Specifies the list of preferred languages of the response. The first supported language from the list will be used for for the response. The value should comply with the [IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). A list of supported languages for the routing service can be found in the dev guide https://developer.here.com/documentation/routing-api/dev_guide/topics/languages.html.  Note: If the first language in the list is not supported, an info notification will be generated with code &#x60;mainLanguageNotFound&#x60;.  | [optional] [default to [&quot;en-US&quot;]]
 **_return** | [**list[ModelReturn]**](ModelReturn.md)|  | [optional] 
 **spans** | [**list[Spans]**](Spans.md)| Defines which map content attributes are included in the response spans. For example, &#x60;attributes,length&#x60; will enable the fields &#x60;attributes&#x60; and &#x60;length&#x60; in the route response. For more information about the &#x60;countryCode&#x60; field, see https://www.iso.org/obp/ui/#search.  This parameter also requires that the &#x60;polyline&#x60; option is set within the &#x60;return&#x60; parameter.  | [optional] 
 **truck_shipped_hazardous_goods** | **str**|  | [optional] 
 **truck_gross_weight** | **int**|  | [optional] 
 **truck_weight_per_axle** | **int**|  | [optional] 
 **truck_weight_per_axle_group** | **str**|  | [optional] 
 **truck_height** | **int**|  | [optional] 
 **truck_width** | **int**|  | [optional] 
 **truck_length** | **int**|  | [optional] 
 **truck_tunnel_category** | **str**|  | [optional] 
 **truck_axle_count** | **int**|  | [optional] 
 **truck_trailer_axle_count** | **int**|  | [optional] 
 **truck_tires_count** | **int**|  | [optional] 
 **truck_category** | **str**|  | [optional] [default to undefined]
 **truck_trailer_count** | **int**|  | [optional] [default to 0]
 **truck_hov_occupancy** | **int**|  | [optional] [default to 1]
 **truck_license_plate** | **str**|  | [optional] 
 **truck_speed_cap** | **float**|  | [optional] 
 **truck_type** | **str**|  | [optional] [default to straight]
 **vehicle_shipped_hazardous_goods** | **str**|  | [optional] 
 **vehicle_gross_weight** | **int**|  | [optional] 
 **vehicle_weight_per_axle** | **int**|  | [optional] 
 **vehicle_weight_per_axle_group** | **str**|  | [optional] 
 **vehicle_height** | **int**|  | [optional] 
 **vehicle_width** | **int**|  | [optional] 
 **vehicle_length** | **int**|  | [optional] 
 **vehicle_tunnel_category** | **str**|  | [optional] 
 **vehicle_axle_count** | **int**|  | [optional] 
 **vehicle_trailer_axle_count** | **int**|  | [optional] 
 **vehicle_tires_count** | **int**|  | [optional] 
 **vehicle_category** | **str**|  | [optional] [default to undefined]
 **vehicle_trailer_count** | **int**|  | [optional] [default to 0]
 **vehicle_hov_occupancy** | **int**|  | [optional] [default to 1]
 **vehicle_license_plate** | **str**|  | [optional] 
 **vehicle_speed_cap** | **float**|  | [optional] 
 **vehicle_type** | **str**|  | [optional] 
 **ev_traffic_speed_table** | [**object**](.md)|  | [optional] 
 **ev_ascent** | **float**|  | [optional] 
 **ev_descent** | **float**|  | [optional] 
 **ev_auxiliary_consumption** | **float**|  | [optional] 
 **ev_initial_charge** | **float**|  | [optional] 
 **ev_max_charge** | **float**|  | [optional] 
 **ev_charging_curve** | **str**|  | [optional] 
 **ev_max_charging_voltage** | **float**|  | [optional] 
 **ev_max_charging_current** | **float**|  | [optional] 
 **ev_max_charge_after_charging_station** | **float**|  | [optional] 
 **ev_min_charge_at_charging_station** | **float**|  | [optional] 
 **ev_min_charge_at_first_charging_station** | **float**|  | [optional] 
 **ev_min_charge_at_destination** | **float**|  | [optional] 
 **ev_charging_setup_duration** | **int**|  | [optional] 
 **ev_connector_types** | **str**|  | [optional] 
 **pedestrian_speed** | [**PedestrianSpeed**](.md)| **Disclaimer: This parameter is currently in beta release, and is therefore subject to breaking changes. The parameter could be extracted to a separate API if speed capping for cars/trucks is introduced** Walking speed in meters per second. Influences the duration of walking segments along the route.  | [optional] 
 **x_request_id** | **str**| User-provided token that can be used to trace a request or a group of requests sent to the service. | [optional] 
 **scooter_allow_highway** | **bool**|  | [optional] [default to false]
 **currency** | **str**| Currency code compliant to ISO 4217. Costs for the calculated route will be returned using this currency.  If not provided, the router will specify it. On a best-effort basis, the router will try to specify the costs in the local currency.  | [optional] 
 **rerouting_mode** | **str**|  | [optional] 
 **rerouting_last_traveled_section_index** | **int**|  | [optional] [default to 0]
 **rerouting_traveled_distance_on_last_section** | **int**|  | [optional] [default to 0]
 **taxi_allow_drive_through_taxi_roads** | **bool**|  | [optional] [default to true]
 **tolls_transponders** | **str**|  | [optional] 
 **tolls_vignettes** | **str**|  | [optional] 
 **tolls_summaries** | [**list[str]**](str.md)|  | [optional] 
 **tolls_vehicle_category** | **str**|  | [optional] 
 **tolls_emission_type** | **str**|  | [optional] 
 **max_speed_on_segment** | [**MaxSpeedOnSegment**](.md)| Specify new base speed for segment by value. Affects route selection and the ETA. Cannot increase base speed on segment.  | [optional] 
 **traffic_override_flow_duration** | **int**|  | [optional] 

### Return type

[**RouterRouteResponse**](RouterRouteResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routes_by_handle_post**
> RouterRouteResponse get_routes_by_handle_post(transport_mode, ev_free_flow_speed_table, route_handle, body=body, x_request_id=x_request_id, origin=origin, departure_time=departure_time, avoid_features=avoid_features, avoid_areas=avoid_areas, avoid_segments=avoid_segments, avoid_zone_categories=avoid_zone_categories, avoid_zone_identifiers=avoid_zone_identifiers, avoid_truck_road_types=avoid_truck_road_types, avoid_toll_transponders=avoid_toll_transponders, exclude_countries=exclude_countries, units=units, lang=lang, _return=_return, spans=spans, truck_shipped_hazardous_goods=truck_shipped_hazardous_goods, truck_gross_weight=truck_gross_weight, truck_weight_per_axle=truck_weight_per_axle, truck_weight_per_axle_group=truck_weight_per_axle_group, truck_height=truck_height, truck_width=truck_width, truck_length=truck_length, truck_tunnel_category=truck_tunnel_category, truck_axle_count=truck_axle_count, truck_trailer_axle_count=truck_trailer_axle_count, truck_tires_count=truck_tires_count, truck_category=truck_category, truck_trailer_count=truck_trailer_count, truck_hov_occupancy=truck_hov_occupancy, truck_license_plate=truck_license_plate, truck_speed_cap=truck_speed_cap, truck_type=truck_type, vehicle_shipped_hazardous_goods=vehicle_shipped_hazardous_goods, vehicle_gross_weight=vehicle_gross_weight, vehicle_weight_per_axle=vehicle_weight_per_axle, vehicle_weight_per_axle_group=vehicle_weight_per_axle_group, vehicle_height=vehicle_height, vehicle_width=vehicle_width, vehicle_length=vehicle_length, vehicle_tunnel_category=vehicle_tunnel_category, vehicle_axle_count=vehicle_axle_count, vehicle_trailer_axle_count=vehicle_trailer_axle_count, vehicle_tires_count=vehicle_tires_count, vehicle_category=vehicle_category, vehicle_trailer_count=vehicle_trailer_count, vehicle_hov_occupancy=vehicle_hov_occupancy, vehicle_license_plate=vehicle_license_plate, vehicle_speed_cap=vehicle_speed_cap, vehicle_type=vehicle_type, ev_traffic_speed_table=ev_traffic_speed_table, ev_ascent=ev_ascent, ev_descent=ev_descent, ev_auxiliary_consumption=ev_auxiliary_consumption, ev_initial_charge=ev_initial_charge, ev_max_charge=ev_max_charge, ev_charging_curve=ev_charging_curve, ev_max_charging_voltage=ev_max_charging_voltage, ev_max_charging_current=ev_max_charging_current, ev_max_charge_after_charging_station=ev_max_charge_after_charging_station, ev_min_charge_at_charging_station=ev_min_charge_at_charging_station, ev_min_charge_at_first_charging_station=ev_min_charge_at_first_charging_station, ev_min_charge_at_destination=ev_min_charge_at_destination, ev_charging_setup_duration=ev_charging_setup_duration, ev_connector_types=ev_connector_types, pedestrian_speed=pedestrian_speed, scooter_allow_highway=scooter_allow_highway, currency=currency, rerouting_mode=rerouting_mode, rerouting_last_traveled_section_index=rerouting_last_traveled_section_index, rerouting_traveled_distance_on_last_section=rerouting_traveled_distance_on_last_section, taxi_allow_drive_through_taxi_roads=taxi_allow_drive_through_taxi_roads, tolls_transponders=tolls_transponders, tolls_vignettes=tolls_vignettes, tolls_summaries=tolls_summaries, tolls_vehicle_category=tolls_vehicle_category, tolls_emission_type=tolls_emission_type, max_speed_on_segment=max_speed_on_segment, traffic_override_flow_duration=traffic_override_flow_duration)

Get route by handle via POST

Decodes and returns a route from a previously calculated route handle.  **Disclaimer: A route handle is not suitable for persistent route storage! It can be invalidated at any time.**  A route handle encodes a previously calculated route. A route can be decoded from a handle as long as the service uses the same map data and encoding that were used when retrieving the handle.  Thus it is suitable for caching routes compactly. It can be used to retrieve updated traffic information or other data along the route. However, a user should be prepared to recalculate the route when decoding the handle fails.  All parameters of the `/routes` endpoint are supported, except for `destination`, `via`, `alternatives` and `routingMode`. See also the `return` parameter of `/routes` endpoint.  The `origin` parameter can be provided to update the start of the previously calculated route.  The `transportMode` parameter does not have to match the transport mode previously used for route calculation. However, when using a different transport mode, the request may fail, e.g. when the route has road segments forbidden for the provided transport mode.  Parameters can be provided either in the query string or some selected ones also in the POST body. If a parameter is provided in both, the request will fail.  Post body size limit is 10MiB.  Please refer to the developers' guide for more information and examples. 

### Example
```python
from __future__ import print_function
import time
import here_public_transit_api
from here_public_transit_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = here_public_transit_api.Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = here_public_transit_api.RoutingApi(here_public_transit_api.ApiClient(configuration))
transport_mode = here_public_transit_api.RouterMode() # RouterMode | Mode of transport to be used for the calculation of the route.  Note: `bus`, `privateBus`, and `taxi` modes are currently provided as Beta, with limited functionality. The API and behaviour may change drastically, or even become unsupported, without warning. Please refer to the developers' guide for more details. 
ev_free_flow_speed_table = NULL # object | 
route_handle = 'route_handle_example' # str | Route handle returned from a previous route calculation.  See `return` parameter of `/routes` endpoint for more information. 
body = here_public_transit_api.GetRoutesByHandlePostParameters() # GetRoutesByHandlePostParameters |  (optional)
x_request_id = 'x_request_id_example' # str | User-provided token that can be used to trace a request or a group of requests sent to the service. (optional)
origin = here_public_transit_api.Waypoint() # Waypoint | A location defining the origin of the trip. The origin has to be located along the previously calculated route.  ## Format  Format: `Place[WaypointOptions]`  * Place: `{lat},{lng}[PlaceOptions]` * PlaceOptions: `;option1=value1;option2=value2...` * WaypointOptions: `!option1=value1!option2=value2...`  A waypoint consists of:  * Exactly one place * Optional settings for the place * Optional settings for the waypoint itself  Supported place options:  * `course`: int, degrees clock-wise from north. Indicating desired direction at the place.   E.g. `90` indicating `east`. Often combined with `radius` and/or `minCourseDistance` * `sideOfStreetHint`: `{lat},{lng}`. Indicating the side of the street that should be   used. E.g. if the location is to the left of the street, the router will prefer using   that side in case the street has dividers. E.g.   `52.511496,13.304140;sideOfStreetHint=52.512149,13.304076` indicates that the `north`   side of the street should be preferred. This option is required, if `matchSideOfStreet`   is set to `always`. * `matchSideOfStreet`: enum `[always, onlyIfDivided]`. Specifies how the location set by   `sideOfStreetHint` should be handled. Requires `sideOfStreetHint` to be specified as   well.   + `always` : Always prefer the given side of street.   + `onlyIfDivided`: Only prefer using side of street set by `sideOfStreetHint` in case     the street has dividers. This is the default behavior. * `nameHint`: string. Causes the router to look for the place with the most similar name.   This can e.g. include things like: `North` being used to differentiate between   interstates `I66 North` and `I66 South`, `Downtown Avenue` being used to correctly   select a residental street. * `radius`: int, meters. Asks the router to consider all places within the given radius as   potential candidates for route calculation. This can be either because it is not   important which place is used, or because it is unknown. Radius more than 200meter are   not supported.  Notes:  * `stopDuration` option is not supported for `origin`, contrary to `destination` and   `via` waypoints. * `passThrough`: option is not supported for 'origin'. * Non-structural reserved characters in options' values need to be properly percent-encoded.   Please refer to the developers' guide for more details. * `minCourseDistance`: While this parameter can be provided for compatibility reasons,   it will not affect the result of a getRoutesByHandle request.  (optional)
departure_time = here_public_transit_api.TimeWithAny() # TimeWithAny | Specifies the time of departure as defined by either `date-time` or `full-date` `T` `partial-time` in `RFC 3339`, section 5.6 (for example, `2019-06-24T01:23:45`).  The requested time is converted to local time at origin. When the optional timezone offset is not specified, time is assumed to be local. The special value `any` can be used to indicate that time should not be taken into account during routing. If neither `departureTime` or `arrivalTime` are specified, current time at departure place will be used. All time values in the response are returned in the timezone of each location.  (optional)
avoid_features = 'avoid_features_example' # str |  (optional)
avoid_areas = 'avoid_areas_example' # str |  (optional)
avoid_segments = 'avoid_segments_example' # str |  (optional)
avoid_zone_categories = 'avoid_zone_categories_example' # str |  (optional)
avoid_zone_identifiers = 'avoid_zone_identifiers_example' # str |  (optional)
avoid_truck_road_types = 'avoid_truck_road_types_example' # str |  (optional)
avoid_toll_transponders = 'avoid_toll_transponders_example' # str |  (optional)
exclude_countries = 'exclude_countries_example' # str |  (optional)
units = here_public_transit_api.Units() # Units | Units of measurement used in guidance instructions. The default is `metric`.  (optional)
lang = ['[\"en-US\"]'] # list[str] | Specifies the list of preferred languages of the response. The first supported language from the list will be used for for the response. The value should comply with the [IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). A list of supported languages for the routing service can be found in the dev guide https://developer.here.com/documentation/routing-api/dev_guide/topics/languages.html.  Note: If the first language in the list is not supported, an info notification will be generated with code `mainLanguageNotFound`.  (optional) (default to ["en-US"])
_return = [here_public_transit_api.ModelReturn()] # list[ModelReturn] |  (optional)
spans = [here_public_transit_api.Spans()] # list[Spans] | Defines which map content attributes are included in the response spans. For example, `attributes,length` will enable the fields `attributes` and `length` in the route response. For more information about the `countryCode` field, see https://www.iso.org/obp/ui/#search.  This parameter also requires that the `polyline` option is set within the `return` parameter.  (optional)
truck_shipped_hazardous_goods = 'truck_shipped_hazardous_goods_example' # str |  (optional)
truck_gross_weight = 56 # int |  (optional)
truck_weight_per_axle = 56 # int |  (optional)
truck_weight_per_axle_group = 'truck_weight_per_axle_group_example' # str |  (optional)
truck_height = 56 # int |  (optional)
truck_width = 56 # int |  (optional)
truck_length = 56 # int |  (optional)
truck_tunnel_category = 'truck_tunnel_category_example' # str |  (optional)
truck_axle_count = 56 # int |  (optional)
truck_trailer_axle_count = 56 # int |  (optional)
truck_tires_count = 56 # int |  (optional)
truck_category = 'undefined' # str |  (optional) (default to undefined)
truck_trailer_count = 0 # int |  (optional) (default to 0)
truck_hov_occupancy = 1 # int |  (optional) (default to 1)
truck_license_plate = 'truck_license_plate_example' # str |  (optional)
truck_speed_cap = 1.2 # float |  (optional)
truck_type = 'straight' # str |  (optional) (default to straight)
vehicle_shipped_hazardous_goods = 'vehicle_shipped_hazardous_goods_example' # str |  (optional)
vehicle_gross_weight = 56 # int |  (optional)
vehicle_weight_per_axle = 56 # int |  (optional)
vehicle_weight_per_axle_group = 'vehicle_weight_per_axle_group_example' # str |  (optional)
vehicle_height = 56 # int |  (optional)
vehicle_width = 56 # int |  (optional)
vehicle_length = 56 # int |  (optional)
vehicle_tunnel_category = 'vehicle_tunnel_category_example' # str |  (optional)
vehicle_axle_count = 56 # int |  (optional)
vehicle_trailer_axle_count = 56 # int |  (optional)
vehicle_tires_count = 56 # int |  (optional)
vehicle_category = 'undefined' # str |  (optional) (default to undefined)
vehicle_trailer_count = 0 # int |  (optional) (default to 0)
vehicle_hov_occupancy = 1 # int |  (optional) (default to 1)
vehicle_license_plate = 'vehicle_license_plate_example' # str |  (optional)
vehicle_speed_cap = 1.2 # float |  (optional)
vehicle_type = 'vehicle_type_example' # str |  (optional)
ev_traffic_speed_table = NULL # object |  (optional)
ev_ascent = 1.2 # float |  (optional)
ev_descent = 1.2 # float |  (optional)
ev_auxiliary_consumption = 1.2 # float |  (optional)
ev_initial_charge = 1.2 # float |  (optional)
ev_max_charge = 1.2 # float |  (optional)
ev_charging_curve = 'ev_charging_curve_example' # str |  (optional)
ev_max_charging_voltage = 1.2 # float |  (optional)
ev_max_charging_current = 1.2 # float |  (optional)
ev_max_charge_after_charging_station = 1.2 # float |  (optional)
ev_min_charge_at_charging_station = 1.2 # float |  (optional)
ev_min_charge_at_first_charging_station = 1.2 # float |  (optional)
ev_min_charge_at_destination = 1.2 # float |  (optional)
ev_charging_setup_duration = 56 # int |  (optional)
ev_connector_types = 'ev_connector_types_example' # str |  (optional)
pedestrian_speed = here_public_transit_api.PedestrianSpeed() # PedestrianSpeed | **Disclaimer: This parameter is currently in beta release, and is therefore subject to breaking changes. The parameter could be extracted to a separate API if speed capping for cars/trucks is introduced** Walking speed in meters per second. Influences the duration of walking segments along the route.  (optional)
scooter_allow_highway = false # bool |  (optional) (default to false)
currency = 'currency_example' # str | Currency code compliant to ISO 4217. Costs for the calculated route will be returned using this currency.  If not provided, the router will specify it. On a best-effort basis, the router will try to specify the costs in the local currency.  (optional)
rerouting_mode = 'rerouting_mode_example' # str |  (optional)
rerouting_last_traveled_section_index = 0 # int |  (optional) (default to 0)
rerouting_traveled_distance_on_last_section = 0 # int |  (optional) (default to 0)
taxi_allow_drive_through_taxi_roads = true # bool |  (optional) (default to true)
tolls_transponders = 'tolls_transponders_example' # str |  (optional)
tolls_vignettes = 'tolls_vignettes_example' # str |  (optional)
tolls_summaries = ['tolls_summaries_example'] # list[str] |  (optional)
tolls_vehicle_category = 'tolls_vehicle_category_example' # str |  (optional)
tolls_emission_type = 'tolls_emission_type_example' # str |  (optional)
max_speed_on_segment = here_public_transit_api.MaxSpeedOnSegment() # MaxSpeedOnSegment | Specify new base speed for segment by value. Affects route selection and the ETA. Cannot increase base speed on segment.  (optional)
traffic_override_flow_duration = 56 # int |  (optional)

try:
    # Get route by handle via POST
    api_response = api_instance.get_routes_by_handle_post(transport_mode, ev_free_flow_speed_table, route_handle, body=body, x_request_id=x_request_id, origin=origin, departure_time=departure_time, avoid_features=avoid_features, avoid_areas=avoid_areas, avoid_segments=avoid_segments, avoid_zone_categories=avoid_zone_categories, avoid_zone_identifiers=avoid_zone_identifiers, avoid_truck_road_types=avoid_truck_road_types, avoid_toll_transponders=avoid_toll_transponders, exclude_countries=exclude_countries, units=units, lang=lang, _return=_return, spans=spans, truck_shipped_hazardous_goods=truck_shipped_hazardous_goods, truck_gross_weight=truck_gross_weight, truck_weight_per_axle=truck_weight_per_axle, truck_weight_per_axle_group=truck_weight_per_axle_group, truck_height=truck_height, truck_width=truck_width, truck_length=truck_length, truck_tunnel_category=truck_tunnel_category, truck_axle_count=truck_axle_count, truck_trailer_axle_count=truck_trailer_axle_count, truck_tires_count=truck_tires_count, truck_category=truck_category, truck_trailer_count=truck_trailer_count, truck_hov_occupancy=truck_hov_occupancy, truck_license_plate=truck_license_plate, truck_speed_cap=truck_speed_cap, truck_type=truck_type, vehicle_shipped_hazardous_goods=vehicle_shipped_hazardous_goods, vehicle_gross_weight=vehicle_gross_weight, vehicle_weight_per_axle=vehicle_weight_per_axle, vehicle_weight_per_axle_group=vehicle_weight_per_axle_group, vehicle_height=vehicle_height, vehicle_width=vehicle_width, vehicle_length=vehicle_length, vehicle_tunnel_category=vehicle_tunnel_category, vehicle_axle_count=vehicle_axle_count, vehicle_trailer_axle_count=vehicle_trailer_axle_count, vehicle_tires_count=vehicle_tires_count, vehicle_category=vehicle_category, vehicle_trailer_count=vehicle_trailer_count, vehicle_hov_occupancy=vehicle_hov_occupancy, vehicle_license_plate=vehicle_license_plate, vehicle_speed_cap=vehicle_speed_cap, vehicle_type=vehicle_type, ev_traffic_speed_table=ev_traffic_speed_table, ev_ascent=ev_ascent, ev_descent=ev_descent, ev_auxiliary_consumption=ev_auxiliary_consumption, ev_initial_charge=ev_initial_charge, ev_max_charge=ev_max_charge, ev_charging_curve=ev_charging_curve, ev_max_charging_voltage=ev_max_charging_voltage, ev_max_charging_current=ev_max_charging_current, ev_max_charge_after_charging_station=ev_max_charge_after_charging_station, ev_min_charge_at_charging_station=ev_min_charge_at_charging_station, ev_min_charge_at_first_charging_station=ev_min_charge_at_first_charging_station, ev_min_charge_at_destination=ev_min_charge_at_destination, ev_charging_setup_duration=ev_charging_setup_duration, ev_connector_types=ev_connector_types, pedestrian_speed=pedestrian_speed, scooter_allow_highway=scooter_allow_highway, currency=currency, rerouting_mode=rerouting_mode, rerouting_last_traveled_section_index=rerouting_last_traveled_section_index, rerouting_traveled_distance_on_last_section=rerouting_traveled_distance_on_last_section, taxi_allow_drive_through_taxi_roads=taxi_allow_drive_through_taxi_roads, tolls_transponders=tolls_transponders, tolls_vignettes=tolls_vignettes, tolls_summaries=tolls_summaries, tolls_vehicle_category=tolls_vehicle_category, tolls_emission_type=tolls_emission_type, max_speed_on_segment=max_speed_on_segment, traffic_override_flow_duration=traffic_override_flow_duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routes_by_handle_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_mode** | [**RouterMode**](.md)| Mode of transport to be used for the calculation of the route.  Note: &#x60;bus&#x60;, &#x60;privateBus&#x60;, and &#x60;taxi&#x60; modes are currently provided as Beta, with limited functionality. The API and behaviour may change drastically, or even become unsupported, without warning. Please refer to the developers&#x27; guide for more details.  | 
 **ev_free_flow_speed_table** | [**object**](.md)|  | 
 **route_handle** | **str**| Route handle returned from a previous route calculation.  See &#x60;return&#x60; parameter of &#x60;/routes&#x60; endpoint for more information.  | 
 **body** | [**GetRoutesByHandlePostParameters**](GetRoutesByHandlePostParameters.md)|  | [optional] 
 **x_request_id** | **str**| User-provided token that can be used to trace a request or a group of requests sent to the service. | [optional] 
 **origin** | [**Waypoint**](.md)| A location defining the origin of the trip. The origin has to be located along the previously calculated route.  ## Format  Format: &#x60;Place[WaypointOptions]&#x60;  * Place: &#x60;{lat},{lng}[PlaceOptions]&#x60; * PlaceOptions: &#x60;;option1&#x3D;value1;option2&#x3D;value2...&#x60; * WaypointOptions: &#x60;!option1&#x3D;value1!option2&#x3D;value2...&#x60;  A waypoint consists of:  * Exactly one place * Optional settings for the place * Optional settings for the waypoint itself  Supported place options:  * &#x60;course&#x60;: int, degrees clock-wise from north. Indicating desired direction at the place.   E.g. &#x60;90&#x60; indicating &#x60;east&#x60;. Often combined with &#x60;radius&#x60; and/or &#x60;minCourseDistance&#x60; * &#x60;sideOfStreetHint&#x60;: &#x60;{lat},{lng}&#x60;. Indicating the side of the street that should be   used. E.g. if the location is to the left of the street, the router will prefer using   that side in case the street has dividers. E.g.   &#x60;52.511496,13.304140;sideOfStreetHint&#x3D;52.512149,13.304076&#x60; indicates that the &#x60;north&#x60;   side of the street should be preferred. This option is required, if &#x60;matchSideOfStreet&#x60;   is set to &#x60;always&#x60;. * &#x60;matchSideOfStreet&#x60;: enum &#x60;[always, onlyIfDivided]&#x60;. Specifies how the location set by   &#x60;sideOfStreetHint&#x60; should be handled. Requires &#x60;sideOfStreetHint&#x60; to be specified as   well.   + &#x60;always&#x60; : Always prefer the given side of street.   + &#x60;onlyIfDivided&#x60;: Only prefer using side of street set by &#x60;sideOfStreetHint&#x60; in case     the street has dividers. This is the default behavior. * &#x60;nameHint&#x60;: string. Causes the router to look for the place with the most similar name.   This can e.g. include things like: &#x60;North&#x60; being used to differentiate between   interstates &#x60;I66 North&#x60; and &#x60;I66 South&#x60;, &#x60;Downtown Avenue&#x60; being used to correctly   select a residental street. * &#x60;radius&#x60;: int, meters. Asks the router to consider all places within the given radius as   potential candidates for route calculation. This can be either because it is not   important which place is used, or because it is unknown. Radius more than 200meter are   not supported.  Notes:  * &#x60;stopDuration&#x60; option is not supported for &#x60;origin&#x60;, contrary to &#x60;destination&#x60; and   &#x60;via&#x60; waypoints. * &#x60;passThrough&#x60;: option is not supported for &#x27;origin&#x27;. * Non-structural reserved characters in options&#x27; values need to be properly percent-encoded.   Please refer to the developers&#x27; guide for more details. * &#x60;minCourseDistance&#x60;: While this parameter can be provided for compatibility reasons,   it will not affect the result of a getRoutesByHandle request.  | [optional] 
 **departure_time** | [**TimeWithAny**](.md)| Specifies the time of departure as defined by either &#x60;date-time&#x60; or &#x60;full-date&#x60; &#x60;T&#x60; &#x60;partial-time&#x60; in &#x60;RFC 3339&#x60;, section 5.6 (for example, &#x60;2019-06-24T01:23:45&#x60;).  The requested time is converted to local time at origin. When the optional timezone offset is not specified, time is assumed to be local. The special value &#x60;any&#x60; can be used to indicate that time should not be taken into account during routing. If neither &#x60;departureTime&#x60; or &#x60;arrivalTime&#x60; are specified, current time at departure place will be used. All time values in the response are returned in the timezone of each location.  | [optional] 
 **avoid_features** | **str**|  | [optional] 
 **avoid_areas** | **str**|  | [optional] 
 **avoid_segments** | **str**|  | [optional] 
 **avoid_zone_categories** | **str**|  | [optional] 
 **avoid_zone_identifiers** | **str**|  | [optional] 
 **avoid_truck_road_types** | **str**|  | [optional] 
 **avoid_toll_transponders** | **str**|  | [optional] 
 **exclude_countries** | **str**|  | [optional] 
 **units** | [**Units**](.md)| Units of measurement used in guidance instructions. The default is &#x60;metric&#x60;.  | [optional] 
 **lang** | [**list[str]**](str.md)| Specifies the list of preferred languages of the response. The first supported language from the list will be used for for the response. The value should comply with the [IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). A list of supported languages for the routing service can be found in the dev guide https://developer.here.com/documentation/routing-api/dev_guide/topics/languages.html.  Note: If the first language in the list is not supported, an info notification will be generated with code &#x60;mainLanguageNotFound&#x60;.  | [optional] [default to [&quot;en-US&quot;]]
 **_return** | [**list[ModelReturn]**](ModelReturn.md)|  | [optional] 
 **spans** | [**list[Spans]**](Spans.md)| Defines which map content attributes are included in the response spans. For example, &#x60;attributes,length&#x60; will enable the fields &#x60;attributes&#x60; and &#x60;length&#x60; in the route response. For more information about the &#x60;countryCode&#x60; field, see https://www.iso.org/obp/ui/#search.  This parameter also requires that the &#x60;polyline&#x60; option is set within the &#x60;return&#x60; parameter.  | [optional] 
 **truck_shipped_hazardous_goods** | **str**|  | [optional] 
 **truck_gross_weight** | **int**|  | [optional] 
 **truck_weight_per_axle** | **int**|  | [optional] 
 **truck_weight_per_axle_group** | **str**|  | [optional] 
 **truck_height** | **int**|  | [optional] 
 **truck_width** | **int**|  | [optional] 
 **truck_length** | **int**|  | [optional] 
 **truck_tunnel_category** | **str**|  | [optional] 
 **truck_axle_count** | **int**|  | [optional] 
 **truck_trailer_axle_count** | **int**|  | [optional] 
 **truck_tires_count** | **int**|  | [optional] 
 **truck_category** | **str**|  | [optional] [default to undefined]
 **truck_trailer_count** | **int**|  | [optional] [default to 0]
 **truck_hov_occupancy** | **int**|  | [optional] [default to 1]
 **truck_license_plate** | **str**|  | [optional] 
 **truck_speed_cap** | **float**|  | [optional] 
 **truck_type** | **str**|  | [optional] [default to straight]
 **vehicle_shipped_hazardous_goods** | **str**|  | [optional] 
 **vehicle_gross_weight** | **int**|  | [optional] 
 **vehicle_weight_per_axle** | **int**|  | [optional] 
 **vehicle_weight_per_axle_group** | **str**|  | [optional] 
 **vehicle_height** | **int**|  | [optional] 
 **vehicle_width** | **int**|  | [optional] 
 **vehicle_length** | **int**|  | [optional] 
 **vehicle_tunnel_category** | **str**|  | [optional] 
 **vehicle_axle_count** | **int**|  | [optional] 
 **vehicle_trailer_axle_count** | **int**|  | [optional] 
 **vehicle_tires_count** | **int**|  | [optional] 
 **vehicle_category** | **str**|  | [optional] [default to undefined]
 **vehicle_trailer_count** | **int**|  | [optional] [default to 0]
 **vehicle_hov_occupancy** | **int**|  | [optional] [default to 1]
 **vehicle_license_plate** | **str**|  | [optional] 
 **vehicle_speed_cap** | **float**|  | [optional] 
 **vehicle_type** | **str**|  | [optional] 
 **ev_traffic_speed_table** | [**object**](.md)|  | [optional] 
 **ev_ascent** | **float**|  | [optional] 
 **ev_descent** | **float**|  | [optional] 
 **ev_auxiliary_consumption** | **float**|  | [optional] 
 **ev_initial_charge** | **float**|  | [optional] 
 **ev_max_charge** | **float**|  | [optional] 
 **ev_charging_curve** | **str**|  | [optional] 
 **ev_max_charging_voltage** | **float**|  | [optional] 
 **ev_max_charging_current** | **float**|  | [optional] 
 **ev_max_charge_after_charging_station** | **float**|  | [optional] 
 **ev_min_charge_at_charging_station** | **float**|  | [optional] 
 **ev_min_charge_at_first_charging_station** | **float**|  | [optional] 
 **ev_min_charge_at_destination** | **float**|  | [optional] 
 **ev_charging_setup_duration** | **int**|  | [optional] 
 **ev_connector_types** | **str**|  | [optional] 
 **pedestrian_speed** | [**PedestrianSpeed**](.md)| **Disclaimer: This parameter is currently in beta release, and is therefore subject to breaking changes. The parameter could be extracted to a separate API if speed capping for cars/trucks is introduced** Walking speed in meters per second. Influences the duration of walking segments along the route.  | [optional] 
 **scooter_allow_highway** | **bool**|  | [optional] [default to false]
 **currency** | **str**| Currency code compliant to ISO 4217. Costs for the calculated route will be returned using this currency.  If not provided, the router will specify it. On a best-effort basis, the router will try to specify the costs in the local currency.  | [optional] 
 **rerouting_mode** | **str**|  | [optional] 
 **rerouting_last_traveled_section_index** | **int**|  | [optional] [default to 0]
 **rerouting_traveled_distance_on_last_section** | **int**|  | [optional] [default to 0]
 **taxi_allow_drive_through_taxi_roads** | **bool**|  | [optional] [default to true]
 **tolls_transponders** | **str**|  | [optional] 
 **tolls_vignettes** | **str**|  | [optional] 
 **tolls_summaries** | [**list[str]**](str.md)|  | [optional] 
 **tolls_vehicle_category** | **str**|  | [optional] 
 **tolls_emission_type** | **str**|  | [optional] 
 **max_speed_on_segment** | [**MaxSpeedOnSegment**](.md)| Specify new base speed for segment by value. Affects route selection and the ETA. Cannot increase base speed on segment.  | [optional] 
 **traffic_override_flow_duration** | **int**|  | [optional] 

### Return type

[**RouterRouteResponse**](RouterRouteResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_route**
> RouterRouteResponse import_route(transport_mode, ev_free_flow_speed_table, body=body, x_request_id=x_request_id, departure_time=departure_time, avoid_features=avoid_features, avoid_areas=avoid_areas, avoid_segments=avoid_segments, avoid_zone_categories=avoid_zone_categories, avoid_zone_identifiers=avoid_zone_identifiers, avoid_truck_road_types=avoid_truck_road_types, avoid_toll_transponders=avoid_toll_transponders, exclude_countries=exclude_countries, units=units, lang=lang, _return=_return, spans=spans, truck_shipped_hazardous_goods=truck_shipped_hazardous_goods, truck_gross_weight=truck_gross_weight, truck_weight_per_axle=truck_weight_per_axle, truck_weight_per_axle_group=truck_weight_per_axle_group, truck_height=truck_height, truck_width=truck_width, truck_length=truck_length, truck_tunnel_category=truck_tunnel_category, truck_axle_count=truck_axle_count, truck_trailer_axle_count=truck_trailer_axle_count, truck_tires_count=truck_tires_count, truck_category=truck_category, truck_trailer_count=truck_trailer_count, truck_hov_occupancy=truck_hov_occupancy, truck_license_plate=truck_license_plate, truck_speed_cap=truck_speed_cap, truck_type=truck_type, vehicle_shipped_hazardous_goods=vehicle_shipped_hazardous_goods, vehicle_gross_weight=vehicle_gross_weight, vehicle_weight_per_axle=vehicle_weight_per_axle, vehicle_weight_per_axle_group=vehicle_weight_per_axle_group, vehicle_height=vehicle_height, vehicle_width=vehicle_width, vehicle_length=vehicle_length, vehicle_tunnel_category=vehicle_tunnel_category, vehicle_axle_count=vehicle_axle_count, vehicle_trailer_axle_count=vehicle_trailer_axle_count, vehicle_tires_count=vehicle_tires_count, vehicle_category=vehicle_category, vehicle_trailer_count=vehicle_trailer_count, vehicle_hov_occupancy=vehicle_hov_occupancy, vehicle_license_plate=vehicle_license_plate, vehicle_speed_cap=vehicle_speed_cap, vehicle_type=vehicle_type, ev_traffic_speed_table=ev_traffic_speed_table, ev_ascent=ev_ascent, ev_descent=ev_descent, ev_auxiliary_consumption=ev_auxiliary_consumption, ev_initial_charge=ev_initial_charge, ev_max_charge=ev_max_charge, ev_charging_curve=ev_charging_curve, ev_max_charging_voltage=ev_max_charging_voltage, ev_max_charging_current=ev_max_charging_current, ev_max_charge_after_charging_station=ev_max_charge_after_charging_station, ev_min_charge_at_charging_station=ev_min_charge_at_charging_station, ev_min_charge_at_first_charging_station=ev_min_charge_at_first_charging_station, ev_min_charge_at_destination=ev_min_charge_at_destination, ev_charging_setup_duration=ev_charging_setup_duration, ev_connector_types=ev_connector_types, scooter_allow_highway=scooter_allow_highway, taxi_allow_drive_through_taxi_roads=taxi_allow_drive_through_taxi_roads)

Calculate a route from a sequence of trace points

Creates a route from a sequence of trace points.  Post body size limit is 10MiB.  **Alpha**: This API is coming soon. It may not be stable and is subject to change. 

### Example
```python
from __future__ import print_function
import time
import here_public_transit_api
from here_public_transit_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = here_public_transit_api.Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = here_public_transit_api.RoutingApi(here_public_transit_api.ApiClient(configuration))
transport_mode = here_public_transit_api.RouterMode() # RouterMode | Mode of transport to be used for the calculation of the route.  Note: `bus`, `privateBus`, and `taxi` modes are currently provided as Beta, with limited functionality. The API and behaviour may change drastically, or even become unsupported, without warning. Please refer to the developers' guide for more details. 
ev_free_flow_speed_table = NULL # object | 
body = here_public_transit_api.MatchTrace() # MatchTrace |  (optional)
x_request_id = 'x_request_id_example' # str | User-provided token that can be used to trace a request or a group of requests sent to the service. (optional)
departure_time = here_public_transit_api.TimeWithAny() # TimeWithAny | Specifies the time of departure as defined by either `date-time` or `full-date` `T` `partial-time` in `RFC 3339`, section 5.6 (for example, `2019-06-24T01:23:45`).  The requested time is converted to local time at origin. When the optional timezone offset is not specified, time is assumed to be local. The special value `any` can be used to indicate that time should not be taken into account during routing. If neither `departureTime` or `arrivalTime` are specified, current time at departure place will be used. All time values in the response are returned in the timezone of each location.  (optional)
avoid_features = 'avoid_features_example' # str |  (optional)
avoid_areas = 'avoid_areas_example' # str |  (optional)
avoid_segments = 'avoid_segments_example' # str |  (optional)
avoid_zone_categories = 'avoid_zone_categories_example' # str |  (optional)
avoid_zone_identifiers = 'avoid_zone_identifiers_example' # str |  (optional)
avoid_truck_road_types = 'avoid_truck_road_types_example' # str |  (optional)
avoid_toll_transponders = 'avoid_toll_transponders_example' # str |  (optional)
exclude_countries = 'exclude_countries_example' # str |  (optional)
units = here_public_transit_api.Units() # Units | Units of measurement used in guidance instructions. The default is `metric`.  (optional)
lang = ['[\"en-US\"]'] # list[str] | Specifies the list of preferred languages of the response. The first supported language from the list will be used for for the response. The value should comply with the [IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). A list of supported languages for the routing service can be found in the dev guide https://developer.here.com/documentation/routing-api/dev_guide/topics/languages.html.  Note: If the first language in the list is not supported, an info notification will be generated with code `mainLanguageNotFound`.  (optional) (default to ["en-US"])
_return = [here_public_transit_api.ModelReturn()] # list[ModelReturn] |  (optional)
spans = [here_public_transit_api.Spans()] # list[Spans] | Defines which map content attributes are included in the response spans. For example, `attributes,length` will enable the fields `attributes` and `length` in the route response. For more information about the `countryCode` field, see https://www.iso.org/obp/ui/#search.  This parameter also requires that the `polyline` option is set within the `return` parameter.  (optional)
truck_shipped_hazardous_goods = 'truck_shipped_hazardous_goods_example' # str |  (optional)
truck_gross_weight = 56 # int |  (optional)
truck_weight_per_axle = 56 # int |  (optional)
truck_weight_per_axle_group = 'truck_weight_per_axle_group_example' # str |  (optional)
truck_height = 56 # int |  (optional)
truck_width = 56 # int |  (optional)
truck_length = 56 # int |  (optional)
truck_tunnel_category = 'truck_tunnel_category_example' # str |  (optional)
truck_axle_count = 56 # int |  (optional)
truck_trailer_axle_count = 56 # int |  (optional)
truck_tires_count = 56 # int |  (optional)
truck_category = 'undefined' # str |  (optional) (default to undefined)
truck_trailer_count = 0 # int |  (optional) (default to 0)
truck_hov_occupancy = 1 # int |  (optional) (default to 1)
truck_license_plate = 'truck_license_plate_example' # str |  (optional)
truck_speed_cap = 1.2 # float |  (optional)
truck_type = 'straight' # str |  (optional) (default to straight)
vehicle_shipped_hazardous_goods = 'vehicle_shipped_hazardous_goods_example' # str |  (optional)
vehicle_gross_weight = 56 # int |  (optional)
vehicle_weight_per_axle = 56 # int |  (optional)
vehicle_weight_per_axle_group = 'vehicle_weight_per_axle_group_example' # str |  (optional)
vehicle_height = 56 # int |  (optional)
vehicle_width = 56 # int |  (optional)
vehicle_length = 56 # int |  (optional)
vehicle_tunnel_category = 'vehicle_tunnel_category_example' # str |  (optional)
vehicle_axle_count = 56 # int |  (optional)
vehicle_trailer_axle_count = 56 # int |  (optional)
vehicle_tires_count = 56 # int |  (optional)
vehicle_category = 'undefined' # str |  (optional) (default to undefined)
vehicle_trailer_count = 0 # int |  (optional) (default to 0)
vehicle_hov_occupancy = 1 # int |  (optional) (default to 1)
vehicle_license_plate = 'vehicle_license_plate_example' # str |  (optional)
vehicle_speed_cap = 1.2 # float |  (optional)
vehicle_type = 'vehicle_type_example' # str |  (optional)
ev_traffic_speed_table = NULL # object |  (optional)
ev_ascent = 1.2 # float |  (optional)
ev_descent = 1.2 # float |  (optional)
ev_auxiliary_consumption = 1.2 # float |  (optional)
ev_initial_charge = 1.2 # float |  (optional)
ev_max_charge = 1.2 # float |  (optional)
ev_charging_curve = 'ev_charging_curve_example' # str |  (optional)
ev_max_charging_voltage = 1.2 # float |  (optional)
ev_max_charging_current = 1.2 # float |  (optional)
ev_max_charge_after_charging_station = 1.2 # float |  (optional)
ev_min_charge_at_charging_station = 1.2 # float |  (optional)
ev_min_charge_at_first_charging_station = 1.2 # float |  (optional)
ev_min_charge_at_destination = 1.2 # float |  (optional)
ev_charging_setup_duration = 56 # int |  (optional)
ev_connector_types = 'ev_connector_types_example' # str |  (optional)
scooter_allow_highway = false # bool |  (optional) (default to false)
taxi_allow_drive_through_taxi_roads = true # bool |  (optional) (default to true)

try:
    # Calculate a route from a sequence of trace points
    api_response = api_instance.import_route(transport_mode, ev_free_flow_speed_table, body=body, x_request_id=x_request_id, departure_time=departure_time, avoid_features=avoid_features, avoid_areas=avoid_areas, avoid_segments=avoid_segments, avoid_zone_categories=avoid_zone_categories, avoid_zone_identifiers=avoid_zone_identifiers, avoid_truck_road_types=avoid_truck_road_types, avoid_toll_transponders=avoid_toll_transponders, exclude_countries=exclude_countries, units=units, lang=lang, _return=_return, spans=spans, truck_shipped_hazardous_goods=truck_shipped_hazardous_goods, truck_gross_weight=truck_gross_weight, truck_weight_per_axle=truck_weight_per_axle, truck_weight_per_axle_group=truck_weight_per_axle_group, truck_height=truck_height, truck_width=truck_width, truck_length=truck_length, truck_tunnel_category=truck_tunnel_category, truck_axle_count=truck_axle_count, truck_trailer_axle_count=truck_trailer_axle_count, truck_tires_count=truck_tires_count, truck_category=truck_category, truck_trailer_count=truck_trailer_count, truck_hov_occupancy=truck_hov_occupancy, truck_license_plate=truck_license_plate, truck_speed_cap=truck_speed_cap, truck_type=truck_type, vehicle_shipped_hazardous_goods=vehicle_shipped_hazardous_goods, vehicle_gross_weight=vehicle_gross_weight, vehicle_weight_per_axle=vehicle_weight_per_axle, vehicle_weight_per_axle_group=vehicle_weight_per_axle_group, vehicle_height=vehicle_height, vehicle_width=vehicle_width, vehicle_length=vehicle_length, vehicle_tunnel_category=vehicle_tunnel_category, vehicle_axle_count=vehicle_axle_count, vehicle_trailer_axle_count=vehicle_trailer_axle_count, vehicle_tires_count=vehicle_tires_count, vehicle_category=vehicle_category, vehicle_trailer_count=vehicle_trailer_count, vehicle_hov_occupancy=vehicle_hov_occupancy, vehicle_license_plate=vehicle_license_plate, vehicle_speed_cap=vehicle_speed_cap, vehicle_type=vehicle_type, ev_traffic_speed_table=ev_traffic_speed_table, ev_ascent=ev_ascent, ev_descent=ev_descent, ev_auxiliary_consumption=ev_auxiliary_consumption, ev_initial_charge=ev_initial_charge, ev_max_charge=ev_max_charge, ev_charging_curve=ev_charging_curve, ev_max_charging_voltage=ev_max_charging_voltage, ev_max_charging_current=ev_max_charging_current, ev_max_charge_after_charging_station=ev_max_charge_after_charging_station, ev_min_charge_at_charging_station=ev_min_charge_at_charging_station, ev_min_charge_at_first_charging_station=ev_min_charge_at_first_charging_station, ev_min_charge_at_destination=ev_min_charge_at_destination, ev_charging_setup_duration=ev_charging_setup_duration, ev_connector_types=ev_connector_types, scooter_allow_highway=scooter_allow_highway, taxi_allow_drive_through_taxi_roads=taxi_allow_drive_through_taxi_roads)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->import_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_mode** | [**RouterMode**](.md)| Mode of transport to be used for the calculation of the route.  Note: &#x60;bus&#x60;, &#x60;privateBus&#x60;, and &#x60;taxi&#x60; modes are currently provided as Beta, with limited functionality. The API and behaviour may change drastically, or even become unsupported, without warning. Please refer to the developers&#x27; guide for more details.  | 
 **ev_free_flow_speed_table** | [**object**](.md)|  | 
 **body** | [**MatchTrace**](MatchTrace.md)|  | [optional] 
 **x_request_id** | **str**| User-provided token that can be used to trace a request or a group of requests sent to the service. | [optional] 
 **departure_time** | [**TimeWithAny**](.md)| Specifies the time of departure as defined by either &#x60;date-time&#x60; or &#x60;full-date&#x60; &#x60;T&#x60; &#x60;partial-time&#x60; in &#x60;RFC 3339&#x60;, section 5.6 (for example, &#x60;2019-06-24T01:23:45&#x60;).  The requested time is converted to local time at origin. When the optional timezone offset is not specified, time is assumed to be local. The special value &#x60;any&#x60; can be used to indicate that time should not be taken into account during routing. If neither &#x60;departureTime&#x60; or &#x60;arrivalTime&#x60; are specified, current time at departure place will be used. All time values in the response are returned in the timezone of each location.  | [optional] 
 **avoid_features** | **str**|  | [optional] 
 **avoid_areas** | **str**|  | [optional] 
 **avoid_segments** | **str**|  | [optional] 
 **avoid_zone_categories** | **str**|  | [optional] 
 **avoid_zone_identifiers** | **str**|  | [optional] 
 **avoid_truck_road_types** | **str**|  | [optional] 
 **avoid_toll_transponders** | **str**|  | [optional] 
 **exclude_countries** | **str**|  | [optional] 
 **units** | [**Units**](.md)| Units of measurement used in guidance instructions. The default is &#x60;metric&#x60;.  | [optional] 
 **lang** | [**list[str]**](str.md)| Specifies the list of preferred languages of the response. The first supported language from the list will be used for for the response. The value should comply with the [IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). A list of supported languages for the routing service can be found in the dev guide https://developer.here.com/documentation/routing-api/dev_guide/topics/languages.html.  Note: If the first language in the list is not supported, an info notification will be generated with code &#x60;mainLanguageNotFound&#x60;.  | [optional] [default to [&quot;en-US&quot;]]
 **_return** | [**list[ModelReturn]**](ModelReturn.md)|  | [optional] 
 **spans** | [**list[Spans]**](Spans.md)| Defines which map content attributes are included in the response spans. For example, &#x60;attributes,length&#x60; will enable the fields &#x60;attributes&#x60; and &#x60;length&#x60; in the route response. For more information about the &#x60;countryCode&#x60; field, see https://www.iso.org/obp/ui/#search.  This parameter also requires that the &#x60;polyline&#x60; option is set within the &#x60;return&#x60; parameter.  | [optional] 
 **truck_shipped_hazardous_goods** | **str**|  | [optional] 
 **truck_gross_weight** | **int**|  | [optional] 
 **truck_weight_per_axle** | **int**|  | [optional] 
 **truck_weight_per_axle_group** | **str**|  | [optional] 
 **truck_height** | **int**|  | [optional] 
 **truck_width** | **int**|  | [optional] 
 **truck_length** | **int**|  | [optional] 
 **truck_tunnel_category** | **str**|  | [optional] 
 **truck_axle_count** | **int**|  | [optional] 
 **truck_trailer_axle_count** | **int**|  | [optional] 
 **truck_tires_count** | **int**|  | [optional] 
 **truck_category** | **str**|  | [optional] [default to undefined]
 **truck_trailer_count** | **int**|  | [optional] [default to 0]
 **truck_hov_occupancy** | **int**|  | [optional] [default to 1]
 **truck_license_plate** | **str**|  | [optional] 
 **truck_speed_cap** | **float**|  | [optional] 
 **truck_type** | **str**|  | [optional] [default to straight]
 **vehicle_shipped_hazardous_goods** | **str**|  | [optional] 
 **vehicle_gross_weight** | **int**|  | [optional] 
 **vehicle_weight_per_axle** | **int**|  | [optional] 
 **vehicle_weight_per_axle_group** | **str**|  | [optional] 
 **vehicle_height** | **int**|  | [optional] 
 **vehicle_width** | **int**|  | [optional] 
 **vehicle_length** | **int**|  | [optional] 
 **vehicle_tunnel_category** | **str**|  | [optional] 
 **vehicle_axle_count** | **int**|  | [optional] 
 **vehicle_trailer_axle_count** | **int**|  | [optional] 
 **vehicle_tires_count** | **int**|  | [optional] 
 **vehicle_category** | **str**|  | [optional] [default to undefined]
 **vehicle_trailer_count** | **int**|  | [optional] [default to 0]
 **vehicle_hov_occupancy** | **int**|  | [optional] [default to 1]
 **vehicle_license_plate** | **str**|  | [optional] 
 **vehicle_speed_cap** | **float**|  | [optional] 
 **vehicle_type** | **str**|  | [optional] 
 **ev_traffic_speed_table** | [**object**](.md)|  | [optional] 
 **ev_ascent** | **float**|  | [optional] 
 **ev_descent** | **float**|  | [optional] 
 **ev_auxiliary_consumption** | **float**|  | [optional] 
 **ev_initial_charge** | **float**|  | [optional] 
 **ev_max_charge** | **float**|  | [optional] 
 **ev_charging_curve** | **str**|  | [optional] 
 **ev_max_charging_voltage** | **float**|  | [optional] 
 **ev_max_charging_current** | **float**|  | [optional] 
 **ev_max_charge_after_charging_station** | **float**|  | [optional] 
 **ev_min_charge_at_charging_station** | **float**|  | [optional] 
 **ev_min_charge_at_first_charging_station** | **float**|  | [optional] 
 **ev_min_charge_at_destination** | **float**|  | [optional] 
 **ev_charging_setup_duration** | **int**|  | [optional] 
 **ev_connector_types** | **str**|  | [optional] 
 **scooter_allow_highway** | **bool**|  | [optional] [default to false]
 **taxi_allow_drive_through_taxi_roads** | **bool**|  | [optional] [default to true]

### Return type

[**RouterRouteResponse**](RouterRouteResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/geo+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


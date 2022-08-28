# PlacesByName

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The station name or part of the name to search for. It is composed of one or more space separated words.  | 
**method** | **str** | Specifies if the match is &#x60;fuzzy&#x60; or &#x60;strict&#x60;. The default value is fuzzy.  &#x60;fuzzy&#x60; - search for a station with the name similar to one of the names requested &#x60;strict&#x60; - search for a station with the name exactly matching one of the names requested or containing it as a part  For example, if the station name in the request is \&quot;maurer\&quot;, then if the method is &#x60;fuzzy&#x60; the response contains \&quot;AMBOY AVE AT MAURER RD\&quot; and \&quot;LAUREL HILL BL/48 ST\&quot;. If the method is &#x60;strict&#x60; the response contains \&quot;AMBOY AVE AT MAURER RD\&quot; but not \&quot;LAUREL HILL BL/48 ST\&quot;.  | [optional] 
**max_places** | **int** | The maximum number of stations/stops included in the response. | [optional] [default to 5]
**_in** | [**InCircle**](InCircle.md) |  | 
**modes_in_place** | **str** | Format: &#x60;mode1,mode2,...&#x60;  Filter the list of stations returned in the response depending on the Transit modes available.  Stations where at least one of the specified modes exists will get returned. By default, all supported transit modes are permitted.  Supported modes: &#x60;highSpeedTrain&#x60; &#x60;intercityTrain&#x60; &#x60;interRegionalTrain&#x60; &#x60;regionalTrain&#x60; &#x60;cityTrain&#x60; &#x60;bus&#x60; &#x60;ferry&#x60; &#x60;subway&#x60; &#x60;lightRail&#x60; &#x60;privateBus&#x60; &#x60;inclined&#x60; &#x60;aerial&#x60; &#x60;busRapid&#x60; &#x60;monorail&#x60; &#x60;flight&#x60; &#x60;spaceship&#x60;  This parameter also support an exclusion list: It&#x27;s sufficient to specify each mode to exclude by prefixing it with &#x60;-&#x60;. Mixing of inclusive and exclusive transit modes is not allowed.  examples:   * &#x60;subway,bus&#x60;. Returns only stations having subways and busses.   * &#x60;-subway,-bus&#x60;. Returns all stations except the one having just subways or busses.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


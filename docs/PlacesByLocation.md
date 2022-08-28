# PlacesByLocation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_in** | [**InCircle**](InCircle.md) |  | 
**max_places** | **int** | The maximum number of stations/stops included in the response. | [optional] [default to 5]
**modes_in_place** | **str** | Format: &#x60;mode1,mode2,...&#x60;  Filter the list of stations returned in the response depending on the Transit modes available.  Stations where at least one of the specified modes exists will get returned. By default, all supported transit modes are permitted.  Supported modes: &#x60;highSpeedTrain&#x60; &#x60;intercityTrain&#x60; &#x60;interRegionalTrain&#x60; &#x60;regionalTrain&#x60; &#x60;cityTrain&#x60; &#x60;bus&#x60; &#x60;ferry&#x60; &#x60;subway&#x60; &#x60;lightRail&#x60; &#x60;privateBus&#x60; &#x60;inclined&#x60; &#x60;aerial&#x60; &#x60;busRapid&#x60; &#x60;monorail&#x60; &#x60;flight&#x60; &#x60;spaceship&#x60;  This parameter also support an exclusion list: It&#x27;s sufficient to specify each mode to exclude by prefixing it with &#x60;-&#x60;. Mixing of inclusive and exclusive transit modes is not allowed.  examples:   * &#x60;subway,bus&#x60;. Returns only stations having subways and busses.   * &#x60;-subway,-bus&#x60;. Returns all stations except the one having just subways or busses.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


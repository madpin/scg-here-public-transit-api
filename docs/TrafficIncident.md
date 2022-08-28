# TrafficIncident

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A human readable description of the incident | [optional] 
**type** | [**TrafficIncidentType**](TrafficIncidentType.md) |  | [optional] 
**criticality** | [**TrafficIncidentCriticality**](TrafficIncidentCriticality.md) |  | [optional] 
**valid_from** | [**Time**](Time.md) |  | [optional] 
**valid_until** | [**Time**](Time.md) |  | [optional] 
**id** | **str** | Traffic Incident unique identifier,  Example of a incident identifier in standard representation: here:traffic:incident:1000155780078589348  Id usage: An incident details can be queried from traffic service later, see https://developer.here.com/documentation/traffic-api/dev_guide/topics/use-cases/incidents-by-id.html  **Notice**: In most cases, the ID comes from a third party incident supplier. This means that once an incident has expired, the ID might be reused  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


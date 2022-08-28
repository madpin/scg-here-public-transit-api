# Fare

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique Fare id. Used to deduplicate fares that apply to multiple sections | 
**name** | **str** | Name of a fare | 
**price** | [**FarePrice**](FarePrice.md) |  | 
**converted_price** | [**FarePrice**](FarePrice.md) |  | [optional] 
**reason** | [**FareReason**](FareReason.md) |  | [optional] 
**payment_methods** | [**list[PaymentMethod]**](PaymentMethod.md) | Specifies the payment methods for which this fare is valid.  | [optional] 
**_pass** | [**FarePass**](FarePass.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# coding: utf-8

"""
    Routing API v8

    A location service providing customizable route calculations for a variety of vehicle types as well as pedestrian modes.  # noqa: E501

    OpenAPI spec version: 8.52.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from here_public_transit_api.models.charging_supply_type import ChargingSupplyType  # noqa: F401,E501

class AllOfChargingConnectorAttributesSupplyType(ChargingSupplyType):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }
    if hasattr(ChargingSupplyType, "swagger_types"):
        swagger_types.update(ChargingSupplyType.swagger_types)

    attribute_map = {
    }
    if hasattr(ChargingSupplyType, "attribute_map"):
        attribute_map.update(ChargingSupplyType.attribute_map)

    def __init__(self, *args, **kwargs):  # noqa: E501
        """AllOfChargingConnectorAttributesSupplyType - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None
        ChargingSupplyType.__init__(self, *args, **kwargs)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AllOfChargingConnectorAttributesSupplyType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AllOfChargingConnectorAttributesSupplyType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
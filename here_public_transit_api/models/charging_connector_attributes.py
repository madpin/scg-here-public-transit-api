# coding: utf-8

"""
    Public Transit API

    Public Transit is a set of three REST APIs that provides public transit routing information and public transit stations information available within an area or for a given station.   # noqa: E501

    OpenAPI spec version: 8.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ChargingConnectorAttributes(object):
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
        'power': 'float',
        'current': 'float',
        'voltage': 'float',
        'supply_type': 'AllOfChargingConnectorAttributesSupplyType',
        'connector_type': 'AllOfChargingConnectorAttributesConnectorType'
    }

    attribute_map = {
        'power': 'power',
        'current': 'current',
        'voltage': 'voltage',
        'supply_type': 'supplyType',
        'connector_type': 'connectorType'
    }

    def __init__(self, power=None, current=None, voltage=None, supply_type=None, connector_type=None):  # noqa: E501
        """ChargingConnectorAttributes - a model defined in Swagger"""  # noqa: E501
        self._power = None
        self._current = None
        self._voltage = None
        self._supply_type = None
        self._connector_type = None
        self.discriminator = None
        self.power = power
        if current is not None:
            self.current = current
        if voltage is not None:
            self.voltage = voltage
        self.supply_type = supply_type
        self.connector_type = connector_type

    @property
    def power(self):
        """Gets the power of this ChargingConnectorAttributes.  # noqa: E501

        Power supplied by the suggested connector in kW.  # noqa: E501

        :return: The power of this ChargingConnectorAttributes.  # noqa: E501
        :rtype: float
        """
        return self._power

    @power.setter
    def power(self, power):
        """Sets the power of this ChargingConnectorAttributes.

        Power supplied by the suggested connector in kW.  # noqa: E501

        :param power: The power of this ChargingConnectorAttributes.  # noqa: E501
        :type: float
        """
        if power is None:
            raise ValueError("Invalid value for `power`, must not be `None`")  # noqa: E501

        self._power = power

    @property
    def current(self):
        """Gets the current of this ChargingConnectorAttributes.  # noqa: E501

        Current of the suggested connector in Amperes.  # noqa: E501

        :return: The current of this ChargingConnectorAttributes.  # noqa: E501
        :rtype: float
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this ChargingConnectorAttributes.

        Current of the suggested connector in Amperes.  # noqa: E501

        :param current: The current of this ChargingConnectorAttributes.  # noqa: E501
        :type: float
        """

        self._current = current

    @property
    def voltage(self):
        """Gets the voltage of this ChargingConnectorAttributes.  # noqa: E501

        Voltage of the suggested connector in Volts.  # noqa: E501

        :return: The voltage of this ChargingConnectorAttributes.  # noqa: E501
        :rtype: float
        """
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        """Sets the voltage of this ChargingConnectorAttributes.

        Voltage of the suggested connector in Volts.  # noqa: E501

        :param voltage: The voltage of this ChargingConnectorAttributes.  # noqa: E501
        :type: float
        """

        self._voltage = voltage

    @property
    def supply_type(self):
        """Gets the supply_type of this ChargingConnectorAttributes.  # noqa: E501

        Supply type of the suggested connector.   # noqa: E501

        :return: The supply_type of this ChargingConnectorAttributes.  # noqa: E501
        :rtype: AllOfChargingConnectorAttributesSupplyType
        """
        return self._supply_type

    @supply_type.setter
    def supply_type(self, supply_type):
        """Sets the supply_type of this ChargingConnectorAttributes.

        Supply type of the suggested connector.   # noqa: E501

        :param supply_type: The supply_type of this ChargingConnectorAttributes.  # noqa: E501
        :type: AllOfChargingConnectorAttributesSupplyType
        """
        if supply_type is None:
            raise ValueError("Invalid value for `supply_type`, must not be `None`")  # noqa: E501

        self._supply_type = supply_type

    @property
    def connector_type(self):
        """Gets the connector_type of this ChargingConnectorAttributes.  # noqa: E501

        Suggested connector for charging at this station  # noqa: E501

        :return: The connector_type of this ChargingConnectorAttributes.  # noqa: E501
        :rtype: AllOfChargingConnectorAttributesConnectorType
        """
        return self._connector_type

    @connector_type.setter
    def connector_type(self, connector_type):
        """Sets the connector_type of this ChargingConnectorAttributes.

        Suggested connector for charging at this station  # noqa: E501

        :param connector_type: The connector_type of this ChargingConnectorAttributes.  # noqa: E501
        :type: AllOfChargingConnectorAttributesConnectorType
        """
        if connector_type is None:
            raise ValueError("Invalid value for `connector_type`, must not be `None`")  # noqa: E501

        self._connector_type = connector_type

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
        if issubclass(ChargingConnectorAttributes, dict):
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
        if not isinstance(other, ChargingConnectorAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

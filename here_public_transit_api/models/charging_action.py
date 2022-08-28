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

class ChargingAction(object):
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
        'action': 'str',
        'duration': 'AllOfChargingActionDuration',
        'instruction': 'str',
        'consumable_power': 'float',
        'arrival_charge': 'float',
        'target_charge': 'float'
    }

    attribute_map = {
        'action': 'action',
        'duration': 'duration',
        'instruction': 'instruction',
        'consumable_power': 'consumablePower',
        'arrival_charge': 'arrivalCharge',
        'target_charge': 'targetCharge'
    }

    def __init__(self, action=None, duration=None, instruction=None, consumable_power=None, arrival_charge=None, target_charge=None):  # noqa: E501
        """ChargingAction - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._duration = None
        self._instruction = None
        self._consumable_power = None
        self._arrival_charge = None
        self._target_charge = None
        self.discriminator = None
        self.action = action
        self.duration = duration
        if instruction is not None:
            self.instruction = instruction
        if consumable_power is not None:
            self.consumable_power = consumable_power
        if arrival_charge is not None:
            self.arrival_charge = arrival_charge
        if target_charge is not None:
            self.target_charge = target_charge

    @property
    def action(self):
        """Gets the action of this ChargingAction.  # noqa: E501

        The type of the action.  **NOTE:** The list of possible actions may be extended in the future. The client application should handle such a case gracefully.   # noqa: E501

        :return: The action of this ChargingAction.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ChargingAction.

        The type of the action.  **NOTE:** The list of possible actions may be extended in the future. The client application should handle such a case gracefully.   # noqa: E501

        :param action: The action of this ChargingAction.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def duration(self):
        """Gets the duration of this ChargingAction.  # noqa: E501

        Estimated duration of this action (in seconds). Actions last until the next action, or the end of the route in case of the last one.  # noqa: E501

        :return: The duration of this ChargingAction.  # noqa: E501
        :rtype: AllOfChargingActionDuration
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ChargingAction.

        Estimated duration of this action (in seconds). Actions last until the next action, or the end of the route in case of the last one.  # noqa: E501

        :param duration: The duration of this ChargingAction.  # noqa: E501
        :type: AllOfChargingActionDuration
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def instruction(self):
        """Gets the instruction of this ChargingAction.  # noqa: E501

        Description of the action (e.g. Turn left onto Minna St.).  # noqa: E501

        :return: The instruction of this ChargingAction.  # noqa: E501
        :rtype: str
        """
        return self._instruction

    @instruction.setter
    def instruction(self, instruction):
        """Sets the instruction of this ChargingAction.

        Description of the action (e.g. Turn left onto Minna St.).  # noqa: E501

        :param instruction: The instruction of this ChargingAction.  # noqa: E501
        :type: str
        """

        self._instruction = instruction

    @property
    def consumable_power(self):
        """Gets the consumable_power of this ChargingAction.  # noqa: E501

        Maximum charging power (in kW) available to the vehicle, based on the properties of the charging station and the vehicle.   # noqa: E501

        :return: The consumable_power of this ChargingAction.  # noqa: E501
        :rtype: float
        """
        return self._consumable_power

    @consumable_power.setter
    def consumable_power(self, consumable_power):
        """Sets the consumable_power of this ChargingAction.

        Maximum charging power (in kW) available to the vehicle, based on the properties of the charging station and the vehicle.   # noqa: E501

        :param consumable_power: The consumable_power of this ChargingAction.  # noqa: E501
        :type: float
        """

        self._consumable_power = consumable_power

    @property
    def arrival_charge(self):
        """Gets the arrival_charge of this ChargingAction.  # noqa: E501

        Estimated vehicle battery charge before this action (in kWh).   # noqa: E501

        :return: The arrival_charge of this ChargingAction.  # noqa: E501
        :rtype: float
        """
        return self._arrival_charge

    @arrival_charge.setter
    def arrival_charge(self, arrival_charge):
        """Sets the arrival_charge of this ChargingAction.

        Estimated vehicle battery charge before this action (in kWh).   # noqa: E501

        :param arrival_charge: The arrival_charge of this ChargingAction.  # noqa: E501
        :type: float
        """

        self._arrival_charge = arrival_charge

    @property
    def target_charge(self):
        """Gets the target_charge of this ChargingAction.  # noqa: E501

        Level to which vehicle battery should be charged by this action (in kWh).   # noqa: E501

        :return: The target_charge of this ChargingAction.  # noqa: E501
        :rtype: float
        """
        return self._target_charge

    @target_charge.setter
    def target_charge(self, target_charge):
        """Sets the target_charge of this ChargingAction.

        Level to which vehicle battery should be charged by this action (in kWh).   # noqa: E501

        :param target_charge: The target_charge of this ChargingAction.  # noqa: E501
        :type: float
        """

        self._target_charge = target_charge

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
        if issubclass(ChargingAction, dict):
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
        if not isinstance(other, ChargingAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
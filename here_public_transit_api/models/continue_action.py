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

class ContinueAction(object):
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
        'duration': 'AllOfContinueActionDuration',
        'instruction': 'str',
        'offset': 'int',
        'length': 'AllOfContinueActionLength',
        'current_road': 'AllOfContinueActionCurrentRoad',
        'next_road': 'AllOfContinueActionNextRoad',
        'exit_sign': 'AllOfContinueActionExitSign',
        'intersection_name': 'list[LocalizedString]'
    }

    attribute_map = {
        'action': 'action',
        'duration': 'duration',
        'instruction': 'instruction',
        'offset': 'offset',
        'length': 'length',
        'current_road': 'currentRoad',
        'next_road': 'nextRoad',
        'exit_sign': 'exitSign',
        'intersection_name': 'intersectionName'
    }

    def __init__(self, action=None, duration=None, instruction=None, offset=None, length=None, current_road=None, next_road=None, exit_sign=None, intersection_name=None):  # noqa: E501
        """ContinueAction - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._duration = None
        self._instruction = None
        self._offset = None
        self._length = None
        self._current_road = None
        self._next_road = None
        self._exit_sign = None
        self._intersection_name = None
        self.discriminator = None
        self.action = action
        self.duration = duration
        if instruction is not None:
            self.instruction = instruction
        if offset is not None:
            self.offset = offset
        if length is not None:
            self.length = length
        if current_road is not None:
            self.current_road = current_road
        if next_road is not None:
            self.next_road = next_road
        if exit_sign is not None:
            self.exit_sign = exit_sign
        if intersection_name is not None:
            self.intersection_name = intersection_name

    @property
    def action(self):
        """Gets the action of this ContinueAction.  # noqa: E501

        The type of the action.  **NOTE:** The list of possible actions may be extended in the future. The client application should handle such a case gracefully.   # noqa: E501

        :return: The action of this ContinueAction.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ContinueAction.

        The type of the action.  **NOTE:** The list of possible actions may be extended in the future. The client application should handle such a case gracefully.   # noqa: E501

        :param action: The action of this ContinueAction.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def duration(self):
        """Gets the duration of this ContinueAction.  # noqa: E501

        Estimated duration of this action (in seconds). Actions last until the next action, or the end of the route in case of the last one.  # noqa: E501

        :return: The duration of this ContinueAction.  # noqa: E501
        :rtype: AllOfContinueActionDuration
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ContinueAction.

        Estimated duration of this action (in seconds). Actions last until the next action, or the end of the route in case of the last one.  # noqa: E501

        :param duration: The duration of this ContinueAction.  # noqa: E501
        :type: AllOfContinueActionDuration
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def instruction(self):
        """Gets the instruction of this ContinueAction.  # noqa: E501

        Description of the action (e.g. Turn left onto Minna St.).  # noqa: E501

        :return: The instruction of this ContinueAction.  # noqa: E501
        :rtype: str
        """
        return self._instruction

    @instruction.setter
    def instruction(self, instruction):
        """Sets the instruction of this ContinueAction.

        Description of the action (e.g. Turn left onto Minna St.).  # noqa: E501

        :param instruction: The instruction of this ContinueAction.  # noqa: E501
        :type: str
        """

        self._instruction = instruction

    @property
    def offset(self):
        """Gets the offset of this ContinueAction.  # noqa: E501

        Offset of a coordinate in the section's polyline.  # noqa: E501

        :return: The offset of this ContinueAction.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ContinueAction.

        Offset of a coordinate in the section's polyline.  # noqa: E501

        :param offset: The offset of this ContinueAction.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def length(self):
        """Gets the length of this ContinueAction.  # noqa: E501

        Estimated length of this action (in meters). Actions extend until the next action, or the end of the route in case of the last one.  # noqa: E501

        :return: The length of this ContinueAction.  # noqa: E501
        :rtype: AllOfContinueActionLength
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this ContinueAction.

        Estimated length of this action (in meters). Actions extend until the next action, or the end of the route in case of the last one.  # noqa: E501

        :param length: The length of this ContinueAction.  # noqa: E501
        :type: AllOfContinueActionLength
        """

        self._length = length

    @property
    def current_road(self):
        """Gets the current_road of this ContinueAction.  # noqa: E501

        Attributes of the current road  # noqa: E501

        :return: The current_road of this ContinueAction.  # noqa: E501
        :rtype: AllOfContinueActionCurrentRoad
        """
        return self._current_road

    @current_road.setter
    def current_road(self, current_road):
        """Sets the current_road of this ContinueAction.

        Attributes of the current road  # noqa: E501

        :param current_road: The current_road of this ContinueAction.  # noqa: E501
        :type: AllOfContinueActionCurrentRoad
        """

        self._current_road = current_road

    @property
    def next_road(self):
        """Gets the next_road of this ContinueAction.  # noqa: E501

        Attributes of the next road  # noqa: E501

        :return: The next_road of this ContinueAction.  # noqa: E501
        :rtype: AllOfContinueActionNextRoad
        """
        return self._next_road

    @next_road.setter
    def next_road(self, next_road):
        """Sets the next_road of this ContinueAction.

        Attributes of the next road  # noqa: E501

        :param next_road: The next_road of this ContinueAction.  # noqa: E501
        :type: AllOfContinueActionNextRoad
        """

        self._next_road = next_road

    @property
    def exit_sign(self):
        """Gets the exit_sign of this ContinueAction.  # noqa: E501

        Attributes of the road exit  # noqa: E501

        :return: The exit_sign of this ContinueAction.  # noqa: E501
        :rtype: AllOfContinueActionExitSign
        """
        return self._exit_sign

    @exit_sign.setter
    def exit_sign(self, exit_sign):
        """Sets the exit_sign of this ContinueAction.

        Attributes of the road exit  # noqa: E501

        :param exit_sign: The exit_sign of this ContinueAction.  # noqa: E501
        :type: AllOfContinueActionExitSign
        """

        self._exit_sign = exit_sign

    @property
    def intersection_name(self):
        """Gets the intersection_name of this ContinueAction.  # noqa: E501

        Name of the intersection where the turn takes place, if available.  # noqa: E501

        :return: The intersection_name of this ContinueAction.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._intersection_name

    @intersection_name.setter
    def intersection_name(self, intersection_name):
        """Sets the intersection_name of this ContinueAction.

        Name of the intersection where the turn takes place, if available.  # noqa: E501

        :param intersection_name: The intersection_name of this ContinueAction.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._intersection_name = intersection_name

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
        if issubclass(ContinueAction, dict):
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
        if not isinstance(other, ContinueAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

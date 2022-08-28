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

class DynamicSpeedInfo(object):
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
        'traffic_speed': 'AllOfDynamicSpeedInfoTrafficSpeed',
        'base_speed': 'AllOfDynamicSpeedInfoBaseSpeed',
        'turn_time': 'AllOfDynamicSpeedInfoTurnTime'
    }

    attribute_map = {
        'traffic_speed': 'trafficSpeed',
        'base_speed': 'baseSpeed',
        'turn_time': 'turnTime'
    }

    def __init__(self, traffic_speed=None, base_speed=None, turn_time=None):  # noqa: E501
        """DynamicSpeedInfo - a model defined in Swagger"""  # noqa: E501
        self._traffic_speed = None
        self._base_speed = None
        self._turn_time = None
        self.discriminator = None
        self.traffic_speed = traffic_speed
        self.base_speed = base_speed
        self.turn_time = turn_time

    @property
    def traffic_speed(self):
        """Gets the traffic_speed of this DynamicSpeedInfo.  # noqa: E501

        Traffic-enabled speed, which is the estimated speed considering traffic-relevant constraints.   # noqa: E501

        :return: The traffic_speed of this DynamicSpeedInfo.  # noqa: E501
        :rtype: AllOfDynamicSpeedInfoTrafficSpeed
        """
        return self._traffic_speed

    @traffic_speed.setter
    def traffic_speed(self, traffic_speed):
        """Sets the traffic_speed of this DynamicSpeedInfo.

        Traffic-enabled speed, which is the estimated speed considering traffic-relevant constraints.   # noqa: E501

        :param traffic_speed: The traffic_speed of this DynamicSpeedInfo.  # noqa: E501
        :type: AllOfDynamicSpeedInfoTrafficSpeed
        """
        if traffic_speed is None:
            raise ValueError("Invalid value for `traffic_speed`, must not be `None`")  # noqa: E501

        self._traffic_speed = traffic_speed

    @property
    def base_speed(self):
        """Gets the base_speed of this DynamicSpeedInfo.  # noqa: E501

        Estimated speed without considering any traffic-related constraints.  # noqa: E501

        :return: The base_speed of this DynamicSpeedInfo.  # noqa: E501
        :rtype: AllOfDynamicSpeedInfoBaseSpeed
        """
        return self._base_speed

    @base_speed.setter
    def base_speed(self, base_speed):
        """Sets the base_speed of this DynamicSpeedInfo.

        Estimated speed without considering any traffic-related constraints.  # noqa: E501

        :param base_speed: The base_speed of this DynamicSpeedInfo.  # noqa: E501
        :type: AllOfDynamicSpeedInfoBaseSpeed
        """
        if base_speed is None:
            raise ValueError("Invalid value for `base_speed`, must not be `None`")  # noqa: E501

        self._base_speed = base_speed

    @property
    def turn_time(self):
        """Gets the turn_time of this DynamicSpeedInfo.  # noqa: E501

        Turn time estimate considering traffic and transport mode needed for turning from this segment into the next.   # noqa: E501

        :return: The turn_time of this DynamicSpeedInfo.  # noqa: E501
        :rtype: AllOfDynamicSpeedInfoTurnTime
        """
        return self._turn_time

    @turn_time.setter
    def turn_time(self, turn_time):
        """Sets the turn_time of this DynamicSpeedInfo.

        Turn time estimate considering traffic and transport mode needed for turning from this segment into the next.   # noqa: E501

        :param turn_time: The turn_time of this DynamicSpeedInfo.  # noqa: E501
        :type: AllOfDynamicSpeedInfoTurnTime
        """
        if turn_time is None:
            raise ValueError("Invalid value for `turn_time`, must not be `None`")  # noqa: E501

        self._turn_time = turn_time

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
        if issubclass(DynamicSpeedInfo, dict):
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
        if not isinstance(other, DynamicSpeedInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

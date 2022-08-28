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

class Traffic(object):
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
        'override_flow_duration': 'int'
    }

    attribute_map = {
        'override_flow_duration': 'overrideFlowDuration'
    }

    def __init__(self, override_flow_duration=None):  # noqa: E501
        """Traffic - a model defined in Swagger"""  # noqa: E501
        self._override_flow_duration = None
        self.discriminator = None
        if override_flow_duration is not None:
            self.override_flow_duration = override_flow_duration

    @property
    def override_flow_duration(self):
        """Gets the override_flow_duration of this Traffic.  # noqa: E501

        Duration in seconds for which flow traffic event would be considered valid. While flow traffic event is valid it will be used over the historical traffic data.  **Note**: Flow traffic represents congestion not caused by any long-term incidents. State of the flow traffic often changes fast. The farther away from the current time we move, the less precise current flow traffic data will be and the more precise historical traffic data becomes. That's why it's advised not to use this parameter unless you know what you want to achieve and use the default behavior which is almost always better.   # noqa: E501

        :return: The override_flow_duration of this Traffic.  # noqa: E501
        :rtype: int
        """
        return self._override_flow_duration

    @override_flow_duration.setter
    def override_flow_duration(self, override_flow_duration):
        """Sets the override_flow_duration of this Traffic.

        Duration in seconds for which flow traffic event would be considered valid. While flow traffic event is valid it will be used over the historical traffic data.  **Note**: Flow traffic represents congestion not caused by any long-term incidents. State of the flow traffic often changes fast. The farther away from the current time we move, the less precise current flow traffic data will be and the more precise historical traffic data becomes. That's why it's advised not to use this parameter unless you know what you want to achieve and use the default behavior which is almost always better.   # noqa: E501

        :param override_flow_duration: The override_flow_duration of this Traffic.  # noqa: E501
        :type: int
        """

        self._override_flow_duration = override_flow_duration

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
        if issubclass(Traffic, dict):
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
        if not isinstance(other, Traffic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

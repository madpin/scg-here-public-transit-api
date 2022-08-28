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

class MatchTracePoint(object):
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
        'lat': 'float',
        'lng': 'float'
    }

    attribute_map = {
        'lat': 'lat',
        'lng': 'lng'
    }

    def __init__(self, lat=None, lng=None):  # noqa: E501
        """MatchTracePoint - a model defined in Swagger"""  # noqa: E501
        self._lat = None
        self._lng = None
        self.discriminator = None
        self.lat = lat
        self.lng = lng

    @property
    def lat(self):
        """Gets the lat of this MatchTracePoint.  # noqa: E501

        Latitude in degrees  # noqa: E501

        :return: The lat of this MatchTracePoint.  # noqa: E501
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this MatchTracePoint.

        Latitude in degrees  # noqa: E501

        :param lat: The lat of this MatchTracePoint.  # noqa: E501
        :type: float
        """
        if lat is None:
            raise ValueError("Invalid value for `lat`, must not be `None`")  # noqa: E501

        self._lat = lat

    @property
    def lng(self):
        """Gets the lng of this MatchTracePoint.  # noqa: E501

        Longitude in degrees  # noqa: E501

        :return: The lng of this MatchTracePoint.  # noqa: E501
        :rtype: float
        """
        return self._lng

    @lng.setter
    def lng(self, lng):
        """Sets the lng of this MatchTracePoint.

        Longitude in degrees  # noqa: E501

        :param lng: The lng of this MatchTracePoint.  # noqa: E501
        :type: float
        """
        if lng is None:
            raise ValueError("Invalid value for `lng`, must not be `None`")  # noqa: E501

        self._lng = lng

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
        if issubclass(MatchTracePoint, dict):
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
        if not isinstance(other, MatchTracePoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
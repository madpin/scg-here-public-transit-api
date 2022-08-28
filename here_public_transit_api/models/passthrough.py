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

class Passthrough(object):
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
        'place': 'Place',
        'offset': 'float'
    }

    attribute_map = {
        'place': 'place',
        'offset': 'offset'
    }

    def __init__(self, place=None, offset=None):  # noqa: E501
        """Passthrough - a model defined in Swagger"""  # noqa: E501
        self._place = None
        self._offset = None
        self.discriminator = None
        self.place = place
        if offset is not None:
            self.offset = offset

    @property
    def place(self):
        """Gets the place of this Passthrough.  # noqa: E501


        :return: The place of this Passthrough.  # noqa: E501
        :rtype: Place
        """
        return self._place

    @place.setter
    def place(self, place):
        """Sets the place of this Passthrough.


        :param place: The place of this Passthrough.  # noqa: E501
        :type: Place
        """
        if place is None:
            raise ValueError("Invalid value for `place`, must not be `None`")  # noqa: E501

        self._place = place

    @property
    def offset(self):
        """Gets the offset of this Passthrough.  # noqa: E501

        Passthrough offsets are the coordinate index in the polyline.  # noqa: E501

        :return: The offset of this Passthrough.  # noqa: E501
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this Passthrough.

        Passthrough offsets are the coordinate index in the polyline.  # noqa: E501

        :param offset: The offset of this Passthrough.  # noqa: E501
        :type: float
        """

        self._offset = offset

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
        if issubclass(Passthrough, dict):
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
        if not isinstance(other, Passthrough):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
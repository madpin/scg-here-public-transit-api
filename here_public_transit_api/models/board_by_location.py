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

class BoardByLocation(object):
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
        '_in': 'InCircle',
        'max_places': 'int'
    }

    attribute_map = {
        '_in': 'in',
        'max_places': 'maxPlaces'
    }

    def __init__(self, _in=None, max_places=5):  # noqa: E501
        """BoardByLocation - a model defined in Swagger"""  # noqa: E501
        self.__in = None
        self._max_places = None
        self.discriminator = None
        self._in = _in
        if max_places is not None:
            self.max_places = max_places

    @property
    def _in(self):
        """Gets the _in of this BoardByLocation.  # noqa: E501


        :return: The _in of this BoardByLocation.  # noqa: E501
        :rtype: InCircle
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """Sets the _in of this BoardByLocation.


        :param _in: The _in of this BoardByLocation.  # noqa: E501
        :type: InCircle
        """
        if _in is None:
            raise ValueError("Invalid value for `_in`, must not be `None`")  # noqa: E501

        self.__in = _in

    @property
    def max_places(self):
        """Gets the max_places of this BoardByLocation.  # noqa: E501

        The maximum number of stations the response should include.  # noqa: E501

        :return: The max_places of this BoardByLocation.  # noqa: E501
        :rtype: int
        """
        return self._max_places

    @max_places.setter
    def max_places(self, max_places):
        """Sets the max_places of this BoardByLocation.

        The maximum number of stations the response should include.  # noqa: E501

        :param max_places: The max_places of this BoardByLocation.  # noqa: E501
        :type: int
        """

        self._max_places = max_places

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
        if issubclass(BoardByLocation, dict):
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
        if not isinstance(other, BoardByLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

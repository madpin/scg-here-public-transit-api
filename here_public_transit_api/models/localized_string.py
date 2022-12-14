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

class LocalizedString(object):
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
        'value': 'str',
        'language': 'str'
    }

    attribute_map = {
        'value': 'value',
        'language': 'language'
    }

    def __init__(self, value=None, language=None):  # noqa: E501
        """LocalizedString - a model defined in Swagger"""  # noqa: E501
        self._value = None
        self._language = None
        self.discriminator = None
        self.value = value
        if language is not None:
            self.language = language

    @property
    def value(self):
        """Gets the value of this LocalizedString.  # noqa: E501

        String written in the language specified in the language property.  # noqa: E501

        :return: The value of this LocalizedString.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this LocalizedString.

        String written in the language specified in the language property.  # noqa: E501

        :param value: The value of this LocalizedString.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def language(self):
        """Gets the language of this LocalizedString.  # noqa: E501

        Language in BCP47 format  # noqa: E501

        :return: The language of this LocalizedString.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this LocalizedString.

        Language in BCP47 format  # noqa: E501

        :param language: The language of this LocalizedString.  # noqa: E501
        :type: str
        """

        self._language = language

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
        if issubclass(LocalizedString, dict):
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
        if not isinstance(other, LocalizedString):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

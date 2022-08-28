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

class AuthErrorResponseSchema(object):
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
        'error': 'str',
        'error_description': 'str'
    }

    attribute_map = {
        'error': 'error',
        'error_description': 'error_description'
    }

    def __init__(self, error=None, error_description=None):  # noqa: E501
        """AuthErrorResponseSchema - a model defined in Swagger"""  # noqa: E501
        self._error = None
        self._error_description = None
        self.discriminator = None
        if error is not None:
            self.error = error
        if error_description is not None:
            self.error_description = error_description

    @property
    def error(self):
        """Gets the error of this AuthErrorResponseSchema.  # noqa: E501

        Human-readable error  # noqa: E501

        :return: The error of this AuthErrorResponseSchema.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this AuthErrorResponseSchema.

        Human-readable error  # noqa: E501

        :param error: The error of this AuthErrorResponseSchema.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def error_description(self):
        """Gets the error_description of this AuthErrorResponseSchema.  # noqa: E501

        Human-readable error description  # noqa: E501

        :return: The error_description of this AuthErrorResponseSchema.  # noqa: E501
        :rtype: str
        """
        return self._error_description

    @error_description.setter
    def error_description(self, error_description):
        """Sets the error_description of this AuthErrorResponseSchema.

        Human-readable error description  # noqa: E501

        :param error_description: The error_description of this AuthErrorResponseSchema.  # noqa: E501
        :type: str
        """

        self._error_description = error_description

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
        if issubclass(AuthErrorResponseSchema, dict):
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
        if not isinstance(other, AuthErrorResponseSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

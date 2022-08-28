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

class FarePassValidityPeriod(object):
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
        'period': 'str',
        'count': 'int'
    }

    attribute_map = {
        'period': 'period',
        'count': 'count'
    }

    def __init__(self, period=None, count=None):  # noqa: E501
        """FarePassValidityPeriod - a model defined in Swagger"""  # noqa: E501
        self._period = None
        self._count = None
        self.discriminator = None
        self.period = period
        if count is not None:
            self.count = count

    @property
    def period(self):
        """Gets the period of this FarePassValidityPeriod.  # noqa: E501

        Extensible enum: `annual` `extendedAnnual` `minutes` `days` `months` `...`   Specifies one of the following validity periods:   - `annual`: pass is valid from Jan 1 to Dec 31   - `extendedAnnual`: pass is valid from Jan 1 to Jan 31 of the following year   - `minutes`: pass is valid for a specified number of minutes See `unit`.   - `days`: pass is valid for a specified number of days. See `unit`.   - `months`: pass is valid for a specified number of months. See `unit`.   # noqa: E501

        :return: The period of this FarePassValidityPeriod.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this FarePassValidityPeriod.

        Extensible enum: `annual` `extendedAnnual` `minutes` `days` `months` `...`   Specifies one of the following validity periods:   - `annual`: pass is valid from Jan 1 to Dec 31   - `extendedAnnual`: pass is valid from Jan 1 to Jan 31 of the following year   - `minutes`: pass is valid for a specified number of minutes See `unit`.   - `days`: pass is valid for a specified number of days. See `unit`.   - `months`: pass is valid for a specified number of months. See `unit`.   # noqa: E501

        :param period: The period of this FarePassValidityPeriod.  # noqa: E501
        :type: str
        """
        if period is None:
            raise ValueError("Invalid value for `period`, must not be `None`")  # noqa: E501

        self._period = period

    @property
    def count(self):
        """Gets the count of this FarePassValidityPeriod.  # noqa: E501

        Required if period is `minutes`, days` or `months`, it specifies how many of these units are covered by the pass.  # noqa: E501

        :return: The count of this FarePassValidityPeriod.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this FarePassValidityPeriod.

        Required if period is `minutes`, days` or `months`, it specifies how many of these units are covered by the pass.  # noqa: E501

        :param count: The count of this FarePassValidityPeriod.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if issubclass(FarePassValidityPeriod, dict):
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
        if not isinstance(other, FarePassValidityPeriod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

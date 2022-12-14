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

class TimeRestrictedPrice(object):
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
        'type': 'str',
        'estimated': 'bool',
        'currency': 'str',
        'unit': 'AllOfTimeRestrictedPriceUnit',
        'value': 'float',
        'days': 'list[TimeRestrictedWeekdays]',
        'min_duration': 'AllOfTimeRestrictedPriceMinDuration',
        'max_duration': 'AllOfTimeRestrictedPriceMaxDuration',
        'from_time': 'AllOfTimeRestrictedPriceFromTime',
        'to_time': 'AllOfTimeRestrictedPriceToTime'
    }

    attribute_map = {
        'type': 'type',
        'estimated': 'estimated',
        'currency': 'currency',
        'unit': 'unit',
        'value': 'value',
        'days': 'days',
        'min_duration': 'minDuration',
        'max_duration': 'maxDuration',
        'from_time': 'fromTime',
        'to_time': 'toTime'
    }

    def __init__(self, type=None, estimated=False, currency=None, unit=None, value=None, days=None, min_duration=None, max_duration=None, from_time=None, to_time=None):  # noqa: E501
        """TimeRestrictedPrice - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._estimated = None
        self._currency = None
        self._unit = None
        self._value = None
        self._days = None
        self._min_duration = None
        self._max_duration = None
        self._from_time = None
        self._to_time = None
        self.discriminator = None
        self.type = type
        if estimated is not None:
            self.estimated = estimated
        self.currency = currency
        if unit is not None:
            self.unit = unit
        self.value = value
        if days is not None:
            self.days = days
        if min_duration is not None:
            self.min_duration = min_duration
        if max_duration is not None:
            self.max_duration = max_duration
        if from_time is not None:
            self.from_time = from_time
        if to_time is not None:
            self.to_time = to_time

    @property
    def type(self):
        """Gets the type of this TimeRestrictedPrice.  # noqa: E501

        Type of price represented by this object. The API customer is responsible for correctly visualizing the pricing model. As it is possible to extend the supported price types in the future, the price information should be hidden when an unknown type is encountered.  Available price types are:    * `restricted` - A single price value valid for a specific time or duration   # noqa: E501

        :return: The type of this TimeRestrictedPrice.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TimeRestrictedPrice.

        Type of price represented by this object. The API customer is responsible for correctly visualizing the pricing model. As it is possible to extend the supported price types in the future, the price information should be hidden when an unknown type is encountered.  Available price types are:    * `restricted` - A single price value valid for a specific time or duration   # noqa: E501

        :param type: The type of this TimeRestrictedPrice.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def estimated(self):
        """Gets the estimated of this TimeRestrictedPrice.  # noqa: E501

        Attribute value is `true` if the fare price is estimated, `false` if it is an exact value.  # noqa: E501

        :return: The estimated of this TimeRestrictedPrice.  # noqa: E501
        :rtype: bool
        """
        return self._estimated

    @estimated.setter
    def estimated(self, estimated):
        """Sets the estimated of this TimeRestrictedPrice.

        Attribute value is `true` if the fare price is estimated, `false` if it is an exact value.  # noqa: E501

        :param estimated: The estimated of this TimeRestrictedPrice.  # noqa: E501
        :type: bool
        """

        self._estimated = estimated

    @property
    def currency(self):
        """Gets the currency of this TimeRestrictedPrice.  # noqa: E501

        Local currency of the price compliant to ISO 4217  # noqa: E501

        :return: The currency of this TimeRestrictedPrice.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this TimeRestrictedPrice.

        Local currency of the price compliant to ISO 4217  # noqa: E501

        :param currency: The currency of this TimeRestrictedPrice.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def unit(self):
        """Gets the unit of this TimeRestrictedPrice.  # noqa: E501

        When set, the price is paid for a specific duration.  Examples:   * `\"unit\": 3600` - price for one hour   * `\"unit\": 28800` - price for 8 hours   * `\"unit\": 86400` - price for one day   # noqa: E501

        :return: The unit of this TimeRestrictedPrice.  # noqa: E501
        :rtype: AllOfTimeRestrictedPriceUnit
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this TimeRestrictedPrice.

        When set, the price is paid for a specific duration.  Examples:   * `\"unit\": 3600` - price for one hour   * `\"unit\": 28800` - price for 8 hours   * `\"unit\": 86400` - price for one day   # noqa: E501

        :param unit: The unit of this TimeRestrictedPrice.  # noqa: E501
        :type: AllOfTimeRestrictedPriceUnit
        """

        self._unit = unit

    @property
    def value(self):
        """Gets the value of this TimeRestrictedPrice.  # noqa: E501

        The price value  # noqa: E501

        :return: The value of this TimeRestrictedPrice.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TimeRestrictedPrice.

        The price value  # noqa: E501

        :param value: The value of this TimeRestrictedPrice.  # noqa: E501
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def days(self):
        """Gets the days of this TimeRestrictedPrice.  # noqa: E501

        This price applies only for the selected days  # noqa: E501

        :return: The days of this TimeRestrictedPrice.  # noqa: E501
        :rtype: list[TimeRestrictedWeekdays]
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this TimeRestrictedPrice.

        This price applies only for the selected days  # noqa: E501

        :param days: The days of this TimeRestrictedPrice.  # noqa: E501
        :type: list[TimeRestrictedWeekdays]
        """

        self._days = days

    @property
    def min_duration(self):
        """Gets the min_duration of this TimeRestrictedPrice.  # noqa: E501

        The price applies if the duration is more or equal to `minDuration`  # noqa: E501

        :return: The min_duration of this TimeRestrictedPrice.  # noqa: E501
        :rtype: AllOfTimeRestrictedPriceMinDuration
        """
        return self._min_duration

    @min_duration.setter
    def min_duration(self, min_duration):
        """Sets the min_duration of this TimeRestrictedPrice.

        The price applies if the duration is more or equal to `minDuration`  # noqa: E501

        :param min_duration: The min_duration of this TimeRestrictedPrice.  # noqa: E501
        :type: AllOfTimeRestrictedPriceMinDuration
        """

        self._min_duration = min_duration

    @property
    def max_duration(self):
        """Gets the max_duration of this TimeRestrictedPrice.  # noqa: E501

        The price applies if the duration is less or equal to `maxDuration`  # noqa: E501

        :return: The max_duration of this TimeRestrictedPrice.  # noqa: E501
        :rtype: AllOfTimeRestrictedPriceMaxDuration
        """
        return self._max_duration

    @max_duration.setter
    def max_duration(self, max_duration):
        """Sets the max_duration of this TimeRestrictedPrice.

        The price applies if the duration is less or equal to `maxDuration`  # noqa: E501

        :param max_duration: The max_duration of this TimeRestrictedPrice.  # noqa: E501
        :type: AllOfTimeRestrictedPriceMaxDuration
        """

        self._max_duration = max_duration

    @property
    def from_time(self):
        """Gets the from_time of this TimeRestrictedPrice.  # noqa: E501

        The price applies from this time of the day  # noqa: E501

        :return: The from_time of this TimeRestrictedPrice.  # noqa: E501
        :rtype: AllOfTimeRestrictedPriceFromTime
        """
        return self._from_time

    @from_time.setter
    def from_time(self, from_time):
        """Sets the from_time of this TimeRestrictedPrice.

        The price applies from this time of the day  # noqa: E501

        :param from_time: The from_time of this TimeRestrictedPrice.  # noqa: E501
        :type: AllOfTimeRestrictedPriceFromTime
        """

        self._from_time = from_time

    @property
    def to_time(self):
        """Gets the to_time of this TimeRestrictedPrice.  # noqa: E501

        The price applies until this time of the day  # noqa: E501

        :return: The to_time of this TimeRestrictedPrice.  # noqa: E501
        :rtype: AllOfTimeRestrictedPriceToTime
        """
        return self._to_time

    @to_time.setter
    def to_time(self, to_time):
        """Sets the to_time of this TimeRestrictedPrice.

        The price applies until this time of the day  # noqa: E501

        :param to_time: The to_time of this TimeRestrictedPrice.  # noqa: E501
        :type: AllOfTimeRestrictedPriceToTime
        """

        self._to_time = to_time

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
        if issubclass(TimeRestrictedPrice, dict):
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
        if not isinstance(other, TimeRestrictedPrice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

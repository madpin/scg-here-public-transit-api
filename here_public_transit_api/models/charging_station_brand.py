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

class ChargingStationBrand(object):
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
        'name': 'str',
        'hrn': 'str'
    }

    attribute_map = {
        'name': 'name',
        'hrn': 'hrn'
    }

    def __init__(self, name=None, hrn=None):  # noqa: E501
        """ChargingStationBrand - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._hrn = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if hrn is not None:
            self.hrn = hrn

    @property
    def name(self):
        """Gets the name of this ChargingStationBrand.  # noqa: E501

        Charging station brand name  # noqa: E501

        :return: The name of this ChargingStationBrand.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChargingStationBrand.

        Charging station brand name  # noqa: E501

        :param name: The name of this ChargingStationBrand.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def hrn(self):
        """Gets the hrn of this ChargingStationBrand.  # noqa: E501

        Charging station brand unique ID. If specified in `ev[preferredBrands]` parameter then it would apply preference to adding stations of the given brand.  **NOTE:** As of now it is generated as a brand name hash. It will be changed to HRN (HERE Resource Name) in the future.   # noqa: E501

        :return: The hrn of this ChargingStationBrand.  # noqa: E501
        :rtype: str
        """
        return self._hrn

    @hrn.setter
    def hrn(self, hrn):
        """Sets the hrn of this ChargingStationBrand.

        Charging station brand unique ID. If specified in `ev[preferredBrands]` parameter then it would apply preference to adding stations of the given brand.  **NOTE:** As of now it is generated as a brand name hash. It will be changed to HRN (HERE Resource Name) in the future.   # noqa: E501

        :param hrn: The hrn of this ChargingStationBrand.  # noqa: E501
        :type: str
        """

        self._hrn = hrn

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
        if issubclass(ChargingStationBrand, dict):
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
        if not isinstance(other, ChargingStationBrand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

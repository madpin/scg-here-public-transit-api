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

class StationsInfoResponse(object):
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
        'notices': 'list[Notice]',
        'stations': 'list[StationInfo]'
    }

    attribute_map = {
        'notices': 'notices',
        'stations': 'stations'
    }

    def __init__(self, notices=None, stations=None):  # noqa: E501
        """StationsInfoResponse - a model defined in Swagger"""  # noqa: E501
        self._notices = None
        self._stations = None
        self.discriminator = None
        if notices is not None:
            self.notices = notices
        self.stations = stations

    @property
    def notices(self):
        """Gets the notices of this StationsInfoResponse.  # noqa: E501

        Contains a list of issues related to this response.  Follows a list of possible notice codes:  * `unknownStations`: The response is incomplete as one or more of the given station IDs were not found. * `noStationsFound`: No stations information is available given current input parameters   # noqa: E501

        :return: The notices of this StationsInfoResponse.  # noqa: E501
        :rtype: list[Notice]
        """
        return self._notices

    @notices.setter
    def notices(self, notices):
        """Sets the notices of this StationsInfoResponse.

        Contains a list of issues related to this response.  Follows a list of possible notice codes:  * `unknownStations`: The response is incomplete as one or more of the given station IDs were not found. * `noStationsFound`: No stations information is available given current input parameters   # noqa: E501

        :param notices: The notices of this StationsInfoResponse.  # noqa: E501
        :type: list[Notice]
        """

        self._notices = notices

    @property
    def stations(self):
        """Gets the stations of this StationsInfoResponse.  # noqa: E501

        A list of stations.  # noqa: E501

        :return: The stations of this StationsInfoResponse.  # noqa: E501
        :rtype: list[StationInfo]
        """
        return self._stations

    @stations.setter
    def stations(self, stations):
        """Sets the stations of this StationsInfoResponse.

        A list of stations.  # noqa: E501

        :param stations: The stations of this StationsInfoResponse.  # noqa: E501
        :type: list[StationInfo]
        """
        if stations is None:
            raise ValueError("Invalid value for `stations`, must not be `None`")  # noqa: E501

        self._stations = stations

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
        if issubclass(StationsInfoResponse, dict):
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
        if not isinstance(other, StationsInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

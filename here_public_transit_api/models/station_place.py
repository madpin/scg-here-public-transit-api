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

class StationPlace(object):
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
        'waypoint': 'int',
        'type': 'str',
        'location': 'AllOfStationPlaceLocation',
        'original_location': 'AllOfStationPlaceOriginalLocation',
        'id': 'str',
        'platform': 'str',
        'code': 'str',
        'wheelchair_accessible': 'AllOfStationPlaceWheelchairAccessible'
    }

    attribute_map = {
        'name': 'name',
        'waypoint': 'waypoint',
        'type': 'type',
        'location': 'location',
        'original_location': 'originalLocation',
        'id': 'id',
        'platform': 'platform',
        'code': 'code',
        'wheelchair_accessible': 'wheelchairAccessible'
    }

    def __init__(self, name=None, waypoint=None, type=None, location=None, original_location=None, id=None, platform=None, code=None, wheelchair_accessible=None):  # noqa: E501
        """StationPlace - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._waypoint = None
        self._type = None
        self._location = None
        self._original_location = None
        self._id = None
        self._platform = None
        self._code = None
        self._wheelchair_accessible = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if waypoint is not None:
            self.waypoint = waypoint
        self.type = type
        self.location = location
        if original_location is not None:
            self.original_location = original_location
        if id is not None:
            self.id = id
        if platform is not None:
            self.platform = platform
        if code is not None:
            self.code = code
        if wheelchair_accessible is not None:
            self.wheelchair_accessible = wheelchair_accessible

    @property
    def name(self):
        """Gets the name of this StationPlace.  # noqa: E501

        Location name  # noqa: E501

        :return: The name of this StationPlace.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StationPlace.

        Location name  # noqa: E501

        :param name: The name of this StationPlace.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def waypoint(self):
        """Gets the waypoint of this StationPlace.  # noqa: E501

        If present, this place corresponds to the waypoint in the request with the same index.  # noqa: E501

        :return: The waypoint of this StationPlace.  # noqa: E501
        :rtype: int
        """
        return self._waypoint

    @waypoint.setter
    def waypoint(self, waypoint):
        """Sets the waypoint of this StationPlace.

        If present, this place corresponds to the waypoint in the request with the same index.  # noqa: E501

        :param waypoint: The waypoint of this StationPlace.  # noqa: E501
        :type: int
        """

        self._waypoint = waypoint

    @property
    def type(self):
        """Gets the type of this StationPlace.  # noqa: E501

        Place type. Each place type can have extra attributes.  **NOTE:** The list of possible place types could be extended in the future. The client application is expected to handle such a case gracefully.   # noqa: E501

        :return: The type of this StationPlace.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StationPlace.

        Place type. Each place type can have extra attributes.  **NOTE:** The list of possible place types could be extended in the future. The client application is expected to handle such a case gracefully.   # noqa: E501

        :param type: The type of this StationPlace.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def location(self):
        """Gets the location of this StationPlace.  # noqa: E501

        The position of this location  This position was used in route calculation. It may be different to the original position provided in the request.   # noqa: E501

        :return: The location of this StationPlace.  # noqa: E501
        :rtype: AllOfStationPlaceLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this StationPlace.

        The position of this location  This position was used in route calculation. It may be different to the original position provided in the request.   # noqa: E501

        :param location: The location of this StationPlace.  # noqa: E501
        :type: AllOfStationPlaceLocation
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def original_location(self):
        """Gets the original_location of this StationPlace.  # noqa: E501

        If present, the original position of this location provided in the request.  # noqa: E501

        :return: The original_location of this StationPlace.  # noqa: E501
        :rtype: AllOfStationPlaceOriginalLocation
        """
        return self._original_location

    @original_location.setter
    def original_location(self, original_location):
        """Sets the original_location of this StationPlace.

        If present, the original position of this location provided in the request.  # noqa: E501

        :param original_location: The original_location of this StationPlace.  # noqa: E501
        :type: AllOfStationPlaceOriginalLocation
        """

        self._original_location = original_location

    @property
    def id(self):
        """Gets the id of this StationPlace.  # noqa: E501

        Identifier of this station  # noqa: E501

        :return: The id of this StationPlace.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StationPlace.

        Identifier of this station  # noqa: E501

        :param id: The id of this StationPlace.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def platform(self):
        """Gets the platform of this StationPlace.  # noqa: E501

        Platform name or number for the departure.  # noqa: E501

        :return: The platform of this StationPlace.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this StationPlace.

        Platform name or number for the departure.  # noqa: E501

        :param platform: The platform of this StationPlace.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def code(self):
        """Gets the code of this StationPlace.  # noqa: E501

        Short text or a number that identifies the place for riders.  # noqa: E501

        :return: The code of this StationPlace.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this StationPlace.

        Short text or a number that identifies the place for riders.  # noqa: E501

        :param code: The code of this StationPlace.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def wheelchair_accessible(self):
        """Gets the wheelchair_accessible of this StationPlace.  # noqa: E501

        Information about accessibility for people with a disability and who use a wheelchair.  * `unknown` - Accessibility information is not available. * `yes` - There exists some accessible path from outside the station to the specific stop/platform. * `limited` - Accessibility is limited or assistance is required. * `no` - There exists no accessible path from outside the station to the specific stop/platform.   # noqa: E501

        :return: The wheelchair_accessible of this StationPlace.  # noqa: E501
        :rtype: AllOfStationPlaceWheelchairAccessible
        """
        return self._wheelchair_accessible

    @wheelchair_accessible.setter
    def wheelchair_accessible(self, wheelchair_accessible):
        """Sets the wheelchair_accessible of this StationPlace.

        Information about accessibility for people with a disability and who use a wheelchair.  * `unknown` - Accessibility information is not available. * `yes` - There exists some accessible path from outside the station to the specific stop/platform. * `limited` - Accessibility is limited or assistance is required. * `no` - There exists no accessible path from outside the station to the specific stop/platform.   # noqa: E501

        :param wheelchair_accessible: The wheelchair_accessible of this StationPlace.  # noqa: E501
        :type: AllOfStationPlaceWheelchairAccessible
        """

        self._wheelchair_accessible = wheelchair_accessible

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
        if issubclass(StationPlace, dict):
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
        if not isinstance(other, StationPlace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

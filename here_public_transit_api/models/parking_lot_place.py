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

class ParkingLotPlace(object):
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
        'location': 'AllOfParkingLotPlaceLocation',
        'original_location': 'AllOfParkingLotPlaceOriginalLocation',
        'id': 'str',
        'attributes': 'list[ParkingLotPlaceType]',
        'rates': 'list[TimeRestrictedPrice]'
    }

    attribute_map = {
        'name': 'name',
        'waypoint': 'waypoint',
        'type': 'type',
        'location': 'location',
        'original_location': 'originalLocation',
        'id': 'id',
        'attributes': 'attributes',
        'rates': 'rates'
    }

    def __init__(self, name=None, waypoint=None, type=None, location=None, original_location=None, id=None, attributes=None, rates=None):  # noqa: E501
        """ParkingLotPlace - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._waypoint = None
        self._type = None
        self._location = None
        self._original_location = None
        self._id = None
        self._attributes = None
        self._rates = None
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
        if attributes is not None:
            self.attributes = attributes
        if rates is not None:
            self.rates = rates

    @property
    def name(self):
        """Gets the name of this ParkingLotPlace.  # noqa: E501

        Location name  # noqa: E501

        :return: The name of this ParkingLotPlace.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ParkingLotPlace.

        Location name  # noqa: E501

        :param name: The name of this ParkingLotPlace.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def waypoint(self):
        """Gets the waypoint of this ParkingLotPlace.  # noqa: E501

        If present, this place corresponds to the waypoint in the request with the same index.  # noqa: E501

        :return: The waypoint of this ParkingLotPlace.  # noqa: E501
        :rtype: int
        """
        return self._waypoint

    @waypoint.setter
    def waypoint(self, waypoint):
        """Sets the waypoint of this ParkingLotPlace.

        If present, this place corresponds to the waypoint in the request with the same index.  # noqa: E501

        :param waypoint: The waypoint of this ParkingLotPlace.  # noqa: E501
        :type: int
        """

        self._waypoint = waypoint

    @property
    def type(self):
        """Gets the type of this ParkingLotPlace.  # noqa: E501

        Place type. Each place type can have extra attributes.  **NOTE:** The list of possible place types could be extended in the future. The client application is expected to handle such a case gracefully.   # noqa: E501

        :return: The type of this ParkingLotPlace.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ParkingLotPlace.

        Place type. Each place type can have extra attributes.  **NOTE:** The list of possible place types could be extended in the future. The client application is expected to handle such a case gracefully.   # noqa: E501

        :param type: The type of this ParkingLotPlace.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def location(self):
        """Gets the location of this ParkingLotPlace.  # noqa: E501

        The position of this location  This position was used in route calculation. It may be different to the original position provided in the request.   # noqa: E501

        :return: The location of this ParkingLotPlace.  # noqa: E501
        :rtype: AllOfParkingLotPlaceLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ParkingLotPlace.

        The position of this location  This position was used in route calculation. It may be different to the original position provided in the request.   # noqa: E501

        :param location: The location of this ParkingLotPlace.  # noqa: E501
        :type: AllOfParkingLotPlaceLocation
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def original_location(self):
        """Gets the original_location of this ParkingLotPlace.  # noqa: E501

        If present, the original position of this location provided in the request.  # noqa: E501

        :return: The original_location of this ParkingLotPlace.  # noqa: E501
        :rtype: AllOfParkingLotPlaceOriginalLocation
        """
        return self._original_location

    @original_location.setter
    def original_location(self, original_location):
        """Sets the original_location of this ParkingLotPlace.

        If present, the original position of this location provided in the request.  # noqa: E501

        :param original_location: The original_location of this ParkingLotPlace.  # noqa: E501
        :type: AllOfParkingLotPlaceOriginalLocation
        """

        self._original_location = original_location

    @property
    def id(self):
        """Gets the id of this ParkingLotPlace.  # noqa: E501

        Identifier of this parking lot  # noqa: E501

        :return: The id of this ParkingLotPlace.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ParkingLotPlace.

        Identifier of this parking lot  # noqa: E501

        :param id: The id of this ParkingLotPlace.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def attributes(self):
        """Gets the attributes of this ParkingLotPlace.  # noqa: E501

        Attributes of a parking lot.  # noqa: E501

        :return: The attributes of this ParkingLotPlace.  # noqa: E501
        :rtype: list[ParkingLotPlaceType]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ParkingLotPlace.

        Attributes of a parking lot.  # noqa: E501

        :param attributes: The attributes of this ParkingLotPlace.  # noqa: E501
        :type: list[ParkingLotPlaceType]
        """

        self._attributes = attributes

    @property
    def rates(self):
        """Gets the rates of this ParkingLotPlace.  # noqa: E501

        List of possible parking rates for this facility. Different rates can apply depending on the day, time of the day or parking duration.   # noqa: E501

        :return: The rates of this ParkingLotPlace.  # noqa: E501
        :rtype: list[TimeRestrictedPrice]
        """
        return self._rates

    @rates.setter
    def rates(self, rates):
        """Sets the rates of this ParkingLotPlace.

        List of possible parking rates for this facility. Different rates can apply depending on the day, time of the day or parking duration.   # noqa: E501

        :param rates: The rates of this ParkingLotPlace.  # noqa: E501
        :type: list[TimeRestrictedPrice]
        """

        self._rates = rates

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
        if issubclass(ParkingLotPlace, dict):
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
        if not isinstance(other, ParkingLotPlace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

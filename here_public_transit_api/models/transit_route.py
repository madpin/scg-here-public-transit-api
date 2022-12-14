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

class TransitRoute(object):
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
        'id': 'str',
        'notices': 'list[Notice]',
        'sections': 'list[TransitRouteSection]',
        'route_labels': 'list[RouteLabel]'
    }

    attribute_map = {
        'id': 'id',
        'notices': 'notices',
        'sections': 'sections',
        'route_labels': 'routeLabels'
    }

    def __init__(self, id=None, notices=None, sections=None, route_labels=None):  # noqa: E501
        """TransitRoute - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._notices = None
        self._sections = None
        self._route_labels = None
        self.discriminator = None
        self.id = id
        if notices is not None:
            self.notices = notices
        self.sections = sections
        if route_labels is not None:
            self.route_labels = route_labels

    @property
    def id(self):
        """Gets the id of this TransitRoute.  # noqa: E501

        Unique identifier of the route  # noqa: E501

        :return: The id of this TransitRoute.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransitRoute.

        Unique identifier of the route  # noqa: E501

        :param id: The id of this TransitRoute.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def notices(self):
        """Gets the notices of this TransitRoute.  # noqa: E501

        Contains a list of issues related to this route.  Follows a list of possible notice codes:  * `excessiveWaitingTime`: Commuter has to wait at a station much longer than usual. * `changeOptionViolated`: This route contains more changes than specified by the `changes` parameter. * `nonviableRoute`: Based on the real-time situation, one or more changes on the route   are not possible. This can happen if real-time re-routing is not available on this area.   # noqa: E501

        :return: The notices of this TransitRoute.  # noqa: E501
        :rtype: list[Notice]
        """
        return self._notices

    @notices.setter
    def notices(self, notices):
        """Sets the notices of this TransitRoute.

        Contains a list of issues related to this route.  Follows a list of possible notice codes:  * `excessiveWaitingTime`: Commuter has to wait at a station much longer than usual. * `changeOptionViolated`: This route contains more changes than specified by the `changes` parameter. * `nonviableRoute`: Based on the real-time situation, one or more changes on the route   are not possible. This can happen if real-time re-routing is not available on this area.   # noqa: E501

        :param notices: The notices of this TransitRoute.  # noqa: E501
        :type: list[Notice]
        """

        self._notices = notices

    @property
    def sections(self):
        """Gets the sections of this TransitRoute.  # noqa: E501

        A list of transit and pedestrian sections of the route.  # noqa: E501

        :return: The sections of this TransitRoute.  # noqa: E501
        :rtype: list[TransitRouteSection]
        """
        return self._sections

    @sections.setter
    def sections(self, sections):
        """Sets the sections of this TransitRoute.

        A list of transit and pedestrian sections of the route.  # noqa: E501

        :param sections: The sections of this TransitRoute.  # noqa: E501
        :type: list[TransitRouteSection]
        """
        if sections is None:
            raise ValueError("Invalid value for `sections`, must not be `None`")  # noqa: E501

        self._sections = sections

    @property
    def route_labels(self):
        """Gets the route_labels of this TransitRoute.  # noqa: E501

        Contains a list of the most important names and route numbers on this route that differentiate it from other alternatives. These names are used to make labels for the main and alternative routes, like \"route1 via A4,D10\", \"route2 via D11,5\" The generated list is expected to be unique for each route in response (but it's not guaranteed)   # noqa: E501

        :return: The route_labels of this TransitRoute.  # noqa: E501
        :rtype: list[RouteLabel]
        """
        return self._route_labels

    @route_labels.setter
    def route_labels(self, route_labels):
        """Sets the route_labels of this TransitRoute.

        Contains a list of the most important names and route numbers on this route that differentiate it from other alternatives. These names are used to make labels for the main and alternative routes, like \"route1 via A4,D10\", \"route2 via D11,5\" The generated list is expected to be unique for each route in response (but it's not guaranteed)   # noqa: E501

        :param route_labels: The route_labels of this TransitRoute.  # noqa: E501
        :type: list[RouteLabel]
        """

        self._route_labels = route_labels

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
        if issubclass(TransitRoute, dict):
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
        if not isinstance(other, TransitRoute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

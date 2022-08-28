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

class RouterRouteResponse(object):
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
        'notices': 'list[RouteResponseNotice]',
        'routes': 'list[RouterRoute]'
    }

    attribute_map = {
        'notices': 'notices',
        'routes': 'routes'
    }

    def __init__(self, notices=None, routes=None):  # noqa: E501
        """RouterRouteResponse - a model defined in Swagger"""  # noqa: E501
        self._notices = None
        self._routes = None
        self.discriminator = None
        if notices is not None:
            self.notices = notices
        self.routes = routes

    @property
    def notices(self):
        """Gets the notices of this RouterRouteResponse.  # noqa: E501

        Contains a list of issues related to this route calculation. Please refer to the `code` attribute for possible values.   # noqa: E501

        :return: The notices of this RouterRouteResponse.  # noqa: E501
        :rtype: list[RouteResponseNotice]
        """
        return self._notices

    @notices.setter
    def notices(self, notices):
        """Sets the notices of this RouterRouteResponse.

        Contains a list of issues related to this route calculation. Please refer to the `code` attribute for possible values.   # noqa: E501

        :param notices: The notices of this RouterRouteResponse.  # noqa: E501
        :type: list[RouteResponseNotice]
        """

        self._notices = notices

    @property
    def routes(self):
        """Gets the routes of this RouterRouteResponse.  # noqa: E501

        List of possible routes  # noqa: E501

        :return: The routes of this RouterRouteResponse.  # noqa: E501
        :rtype: list[RouterRoute]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this RouterRouteResponse.

        List of possible routes  # noqa: E501

        :param routes: The routes of this RouterRouteResponse.  # noqa: E501
        :type: list[RouterRoute]
        """
        if routes is None:
            raise ValueError("Invalid value for `routes`, must not be `None`")  # noqa: E501

        self._routes = routes

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
        if issubclass(RouterRouteResponse, dict):
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
        if not isinstance(other, RouterRouteResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

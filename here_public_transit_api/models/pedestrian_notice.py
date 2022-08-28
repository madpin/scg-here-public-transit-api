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

class PedestrianNotice(object):
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
        'title': 'str',
        'code': 'str',
        'severity': 'NoticeSeverity',
        'details': 'list[BaseNoticeDetail]'
    }

    attribute_map = {
        'title': 'title',
        'code': 'code',
        'severity': 'severity',
        'details': 'details'
    }

    def __init__(self, title=None, code=None, severity=None, details=None):  # noqa: E501
        """PedestrianNotice - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._code = None
        self._severity = None
        self._details = None
        self.discriminator = None
        if title is not None:
            self.title = title
        self.code = code
        if severity is not None:
            self.severity = severity
        if details is not None:
            self.details = details

    @property
    def title(self):
        """Gets the title of this PedestrianNotice.  # noqa: E501

        Human-readable notice description.  # noqa: E501

        :return: The title of this PedestrianNotice.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PedestrianNotice.

        Human-readable notice description.  # noqa: E501

        :param title: The title of this PedestrianNotice.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def code(self):
        """Gets the code of this PedestrianNotice.  # noqa: E501

        Extensible enum: `simplePolyline` `pedestrianOptionViolated` `violatedAvoidTunnel` `violatedAvoidDirtRoad` `...`   Currently known codes (non-exhaustive: this list could be extended for new situations):  | Code      | Description  | Severity | | --------- | ------- | ----            | | simplePolyline | An accurate polyline is not available for this section. The returned polyline has been generated from departure and arrival places | info | | pedestrianOptionViolated | This section violates the parameter `pedestrian[speed]` or `pedestrian[maxDistance]` | critical | | violatedAvoidTunnel | Route did not manage to avoid user preference | critical | | violatedAvoidDirtRoad | Route did not manage to avoid user preference | critical |   # noqa: E501

        :return: The code of this PedestrianNotice.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this PedestrianNotice.

        Extensible enum: `simplePolyline` `pedestrianOptionViolated` `violatedAvoidTunnel` `violatedAvoidDirtRoad` `...`   Currently known codes (non-exhaustive: this list could be extended for new situations):  | Code      | Description  | Severity | | --------- | ------- | ----            | | simplePolyline | An accurate polyline is not available for this section. The returned polyline has been generated from departure and arrival places | info | | pedestrianOptionViolated | This section violates the parameter `pedestrian[speed]` or `pedestrian[maxDistance]` | critical | | violatedAvoidTunnel | Route did not manage to avoid user preference | critical | | violatedAvoidDirtRoad | Route did not manage to avoid user preference | critical |   # noqa: E501

        :param code: The code of this PedestrianNotice.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def severity(self):
        """Gets the severity of this PedestrianNotice.  # noqa: E501


        :return: The severity of this PedestrianNotice.  # noqa: E501
        :rtype: NoticeSeverity
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this PedestrianNotice.


        :param severity: The severity of this PedestrianNotice.  # noqa: E501
        :type: NoticeSeverity
        """

        self._severity = severity

    @property
    def details(self):
        """Gets the details of this PedestrianNotice.  # noqa: E501

        Additional details about the notice  # noqa: E501

        :return: The details of this PedestrianNotice.  # noqa: E501
        :rtype: list[BaseNoticeDetail]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this PedestrianNotice.

        Additional details about the notice  # noqa: E501

        :param details: The details of this PedestrianNotice.  # noqa: E501
        :type: list[BaseNoticeDetail]
        """

        self._details = details

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
        if issubclass(PedestrianNotice, dict):
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
        if not isinstance(other, PedestrianNotice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

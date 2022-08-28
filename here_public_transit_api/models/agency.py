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

class Agency(object):
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
        'name': 'str',
        'website': 'AllOfAgencyWebsite'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'website': 'website'
    }

    def __init__(self, id=None, name=None, website=None):  # noqa: E501
        """Agency - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._website = None
        self.discriminator = None
        self.id = id
        self.name = name
        if website is not None:
            self.website = website

    @property
    def id(self):
        """Gets the id of this Agency.  # noqa: E501

        Unique code of the agency. Specifies if the same agency is used on different sections of the same route.  # noqa: E501

        :return: The id of this Agency.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Agency.

        Unique code of the agency. Specifies if the same agency is used on different sections of the same route.  # noqa: E501

        :param id: The id of this Agency.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Agency.  # noqa: E501

        Human readable name of the owner of the transport service.  # noqa: E501

        :return: The name of this Agency.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Agency.

        Human readable name of the owner of the transport service.  # noqa: E501

        :param name: The name of this Agency.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def website(self):
        """Gets the website of this Agency.  # noqa: E501

        Link to the agency's website.  # noqa: E501

        :return: The website of this Agency.  # noqa: E501
        :rtype: AllOfAgencyWebsite
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this Agency.

        Link to the agency's website.  # noqa: E501

        :param website: The website of this Agency.  # noqa: E501
        :type: AllOfAgencyWebsite
        """

        self._website = website

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
        if issubclass(Agency, dict):
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
        if not isinstance(other, Agency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

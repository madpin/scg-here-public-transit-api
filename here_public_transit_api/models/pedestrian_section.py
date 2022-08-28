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

class PedestrianSection(object):
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
        'type': 'str',
        'pre_actions': 'list[BaseAction]',
        'actions': 'list[PedestrianAction]',
        'language': 'str',
        'post_actions': 'list[PedestrianPostAction]',
        'turn_by_turn_actions': 'list[OffsetAction]',
        'departure': 'PedestrianDeparture',
        'arrival': 'PedestrianDeparture',
        'passthrough': 'list[Passthrough]',
        'summary': 'AllOfPedestrianSectionSummary',
        'travel_summary': 'AllOfPedestrianSectionTravelSummary',
        'polyline': 'Polyline',
        'notices': 'list[PedestrianNotice]',
        'transport': 'PedestrianTransport',
        'spans': 'list[PedestrianSpan]',
        'ref_replacements': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'pre_actions': 'preActions',
        'actions': 'actions',
        'language': 'language',
        'post_actions': 'postActions',
        'turn_by_turn_actions': 'turnByTurnActions',
        'departure': 'departure',
        'arrival': 'arrival',
        'passthrough': 'passthrough',
        'summary': 'summary',
        'travel_summary': 'travelSummary',
        'polyline': 'polyline',
        'notices': 'notices',
        'transport': 'transport',
        'spans': 'spans',
        'ref_replacements': 'refReplacements'
    }

    def __init__(self, id=None, type=None, pre_actions=None, actions=None, language=None, post_actions=None, turn_by_turn_actions=None, departure=None, arrival=None, passthrough=None, summary=None, travel_summary=None, polyline=None, notices=None, transport=None, spans=None, ref_replacements=None):  # noqa: E501
        """PedestrianSection - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._pre_actions = None
        self._actions = None
        self._language = None
        self._post_actions = None
        self._turn_by_turn_actions = None
        self._departure = None
        self._arrival = None
        self._passthrough = None
        self._summary = None
        self._travel_summary = None
        self._polyline = None
        self._notices = None
        self._transport = None
        self._spans = None
        self._ref_replacements = None
        self.discriminator = None
        self.id = id
        self.type = type
        if pre_actions is not None:
            self.pre_actions = pre_actions
        if actions is not None:
            self.actions = actions
        if language is not None:
            self.language = language
        if post_actions is not None:
            self.post_actions = post_actions
        if turn_by_turn_actions is not None:
            self.turn_by_turn_actions = turn_by_turn_actions
        self.departure = departure
        self.arrival = arrival
        if passthrough is not None:
            self.passthrough = passthrough
        if summary is not None:
            self.summary = summary
        if travel_summary is not None:
            self.travel_summary = travel_summary
        if polyline is not None:
            self.polyline = polyline
        if notices is not None:
            self.notices = notices
        self.transport = transport
        if spans is not None:
            self.spans = spans
        if ref_replacements is not None:
            self.ref_replacements = ref_replacements

    @property
    def id(self):
        """Gets the id of this PedestrianSection.  # noqa: E501

        Unique identifier of the section  # noqa: E501

        :return: The id of this PedestrianSection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PedestrianSection.

        Unique identifier of the section  # noqa: E501

        :param id: The id of this PedestrianSection.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this PedestrianSection.  # noqa: E501

        Section type used by the client to identify what extension to the BaseSection are available.  # noqa: E501

        :return: The type of this PedestrianSection.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PedestrianSection.

        Section type used by the client to identify what extension to the BaseSection are available.  # noqa: E501

        :param type: The type of this PedestrianSection.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def pre_actions(self):
        """Gets the pre_actions of this PedestrianSection.  # noqa: E501

        Actions that must be done prior to `departure`.  # noqa: E501

        :return: The pre_actions of this PedestrianSection.  # noqa: E501
        :rtype: list[BaseAction]
        """
        return self._pre_actions

    @pre_actions.setter
    def pre_actions(self, pre_actions):
        """Sets the pre_actions of this PedestrianSection.

        Actions that must be done prior to `departure`.  # noqa: E501

        :param pre_actions: The pre_actions of this PedestrianSection.  # noqa: E501
        :type: list[BaseAction]
        """

        self._pre_actions = pre_actions

    @property
    def actions(self):
        """Gets the actions of this PedestrianSection.  # noqa: E501

        Actions to be performed at or during a specific portion of a section.  Action offsets are the coordinate index in the polyline.  *NOTE:* currentRoad and nextRoad are not populated for actions.   # noqa: E501

        :return: The actions of this PedestrianSection.  # noqa: E501
        :rtype: list[PedestrianAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this PedestrianSection.

        Actions to be performed at or during a specific portion of a section.  Action offsets are the coordinate index in the polyline.  *NOTE:* currentRoad and nextRoad are not populated for actions.   # noqa: E501

        :param actions: The actions of this PedestrianSection.  # noqa: E501
        :type: list[PedestrianAction]
        """

        self._actions = actions

    @property
    def language(self):
        """Gets the language of this PedestrianSection.  # noqa: E501

        Language of the localized strings in the section, if any, in BCP47 format.  # noqa: E501

        :return: The language of this PedestrianSection.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this PedestrianSection.

        Language of the localized strings in the section, if any, in BCP47 format.  # noqa: E501

        :param language: The language of this PedestrianSection.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def post_actions(self):
        """Gets the post_actions of this PedestrianSection.  # noqa: E501

        Actions that must be done after `arrival`.  # noqa: E501

        :return: The post_actions of this PedestrianSection.  # noqa: E501
        :rtype: list[PedestrianPostAction]
        """
        return self._post_actions

    @post_actions.setter
    def post_actions(self, post_actions):
        """Sets the post_actions of this PedestrianSection.

        Actions that must be done after `arrival`.  # noqa: E501

        :param post_actions: The post_actions of this PedestrianSection.  # noqa: E501
        :type: list[PedestrianPostAction]
        """

        self._post_actions = post_actions

    @property
    def turn_by_turn_actions(self):
        """Gets the turn_by_turn_actions of this PedestrianSection.  # noqa: E501

        Actions for turn by turn guidance during the travel portion of the section, i.e., between `departure` and `arrival`.  # noqa: E501

        :return: The turn_by_turn_actions of this PedestrianSection.  # noqa: E501
        :rtype: list[OffsetAction]
        """
        return self._turn_by_turn_actions

    @turn_by_turn_actions.setter
    def turn_by_turn_actions(self, turn_by_turn_actions):
        """Sets the turn_by_turn_actions of this PedestrianSection.

        Actions for turn by turn guidance during the travel portion of the section, i.e., between `departure` and `arrival`.  # noqa: E501

        :param turn_by_turn_actions: The turn_by_turn_actions of this PedestrianSection.  # noqa: E501
        :type: list[OffsetAction]
        """

        self._turn_by_turn_actions = turn_by_turn_actions

    @property
    def departure(self):
        """Gets the departure of this PedestrianSection.  # noqa: E501


        :return: The departure of this PedestrianSection.  # noqa: E501
        :rtype: PedestrianDeparture
        """
        return self._departure

    @departure.setter
    def departure(self, departure):
        """Sets the departure of this PedestrianSection.


        :param departure: The departure of this PedestrianSection.  # noqa: E501
        :type: PedestrianDeparture
        """
        if departure is None:
            raise ValueError("Invalid value for `departure`, must not be `None`")  # noqa: E501

        self._departure = departure

    @property
    def arrival(self):
        """Gets the arrival of this PedestrianSection.  # noqa: E501


        :return: The arrival of this PedestrianSection.  # noqa: E501
        :rtype: PedestrianDeparture
        """
        return self._arrival

    @arrival.setter
    def arrival(self, arrival):
        """Sets the arrival of this PedestrianSection.


        :param arrival: The arrival of this PedestrianSection.  # noqa: E501
        :type: PedestrianDeparture
        """
        if arrival is None:
            raise ValueError("Invalid value for `arrival`, must not be `None`")  # noqa: E501

        self._arrival = arrival

    @property
    def passthrough(self):
        """Gets the passthrough of this PedestrianSection.  # noqa: E501

        List of via waypoints this section is passing through.  Each via waypoint of the request that is a `passThrough=true` waypoint, appears as a `Passthrough` in the response. It appears in the section that starts with the closest non-passthrough via specified before it or origin.  The passthrough vias appear in this list in the order they are traversed. They are traversed in the order they are specified in the request.   # noqa: E501

        :return: The passthrough of this PedestrianSection.  # noqa: E501
        :rtype: list[Passthrough]
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this PedestrianSection.

        List of via waypoints this section is passing through.  Each via waypoint of the request that is a `passThrough=true` waypoint, appears as a `Passthrough` in the response. It appears in the section that starts with the closest non-passthrough via specified before it or origin.  The passthrough vias appear in this list in the order they are traversed. They are traversed in the order they are specified in the request.   # noqa: E501

        :param passthrough: The passthrough of this PedestrianSection.  # noqa: E501
        :type: list[Passthrough]
        """

        self._passthrough = passthrough

    @property
    def summary(self):
        """Gets the summary of this PedestrianSection.  # noqa: E501

        Total value of key attributes (e.g. duration, length) summed up for the entire section, including `preActions`, `postActions`, and the travel portion of the section.   # noqa: E501

        :return: The summary of this PedestrianSection.  # noqa: E501
        :rtype: AllOfPedestrianSectionSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this PedestrianSection.

        Total value of key attributes (e.g. duration, length) summed up for the entire section, including `preActions`, `postActions`, and the travel portion of the section.   # noqa: E501

        :param summary: The summary of this PedestrianSection.  # noqa: E501
        :type: AllOfPedestrianSectionSummary
        """

        self._summary = summary

    @property
    def travel_summary(self):
        """Gets the travel_summary of this PedestrianSection.  # noqa: E501

        Total value of key attributes (e.g., duration, length) summed up for just the travel portion of the section, between `departure` and `arrival`. `preActions` and `postActions` are excluded.   # noqa: E501

        :return: The travel_summary of this PedestrianSection.  # noqa: E501
        :rtype: AllOfPedestrianSectionTravelSummary
        """
        return self._travel_summary

    @travel_summary.setter
    def travel_summary(self, travel_summary):
        """Sets the travel_summary of this PedestrianSection.

        Total value of key attributes (e.g., duration, length) summed up for just the travel portion of the section, between `departure` and `arrival`. `preActions` and `postActions` are excluded.   # noqa: E501

        :param travel_summary: The travel_summary of this PedestrianSection.  # noqa: E501
        :type: AllOfPedestrianSectionTravelSummary
        """

        self._travel_summary = travel_summary

    @property
    def polyline(self):
        """Gets the polyline of this PedestrianSection.  # noqa: E501


        :return: The polyline of this PedestrianSection.  # noqa: E501
        :rtype: Polyline
        """
        return self._polyline

    @polyline.setter
    def polyline(self, polyline):
        """Sets the polyline of this PedestrianSection.


        :param polyline: The polyline of this PedestrianSection.  # noqa: E501
        :type: Polyline
        """

        self._polyline = polyline

    @property
    def notices(self):
        """Gets the notices of this PedestrianSection.  # noqa: E501

        Contains a list of issues related to this section of the route.   # noqa: E501

        :return: The notices of this PedestrianSection.  # noqa: E501
        :rtype: list[PedestrianNotice]
        """
        return self._notices

    @notices.setter
    def notices(self, notices):
        """Sets the notices of this PedestrianSection.

        Contains a list of issues related to this section of the route.   # noqa: E501

        :param notices: The notices of this PedestrianSection.  # noqa: E501
        :type: list[PedestrianNotice]
        """

        self._notices = notices

    @property
    def transport(self):
        """Gets the transport of this PedestrianSection.  # noqa: E501


        :return: The transport of this PedestrianSection.  # noqa: E501
        :rtype: PedestrianTransport
        """
        return self._transport

    @transport.setter
    def transport(self, transport):
        """Sets the transport of this PedestrianSection.


        :param transport: The transport of this PedestrianSection.  # noqa: E501
        :type: PedestrianTransport
        """
        if transport is None:
            raise ValueError("Invalid value for `transport`, must not be `None`")  # noqa: E501

        self._transport = transport

    @property
    def spans(self):
        """Gets the spans of this PedestrianSection.  # noqa: E501

        Spans attached to a `Section` describing pedestrian content.   # noqa: E501

        :return: The spans of this PedestrianSection.  # noqa: E501
        :rtype: list[PedestrianSpan]
        """
        return self._spans

    @spans.setter
    def spans(self, spans):
        """Sets the spans of this PedestrianSection.

        Spans attached to a `Section` describing pedestrian content.   # noqa: E501

        :param spans: The spans of this PedestrianSection.  # noqa: E501
        :type: list[PedestrianSpan]
        """

        self._spans = spans

    @property
    def ref_replacements(self):
        """Gets the ref_replacements of this PedestrianSection.  # noqa: E501

        Dictionary of placeholders to replacement strings for the compact representation of map entity references.   # noqa: E501

        :return: The ref_replacements of this PedestrianSection.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._ref_replacements

    @ref_replacements.setter
    def ref_replacements(self, ref_replacements):
        """Sets the ref_replacements of this PedestrianSection.

        Dictionary of placeholders to replacement strings for the compact representation of map entity references.   # noqa: E501

        :param ref_replacements: The ref_replacements of this PedestrianSection.  # noqa: E501
        :type: dict(str, str)
        """

        self._ref_replacements = ref_replacements

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
        if issubclass(PedestrianSection, dict):
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
        if not isinstance(other, PedestrianSection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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

class TransitSection(object):
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
        'pre_actions': 'list[TransitPreAction]',
        'actions': 'list[OffsetAction]',
        'language': 'str',
        'post_actions': 'list[TransitPostAction]',
        'turn_by_turn_actions': 'list[OffsetAction]',
        'departure': 'TransitDeparture',
        'arrival': 'TransitDeparture',
        'passthrough': 'list[Passthrough]',
        'summary': 'AllOfTransitSectionSummary',
        'travel_summary': 'AllOfTransitSectionTravelSummary',
        'polyline': 'Polyline',
        'notices': 'list[TransitNotice]',
        'booking_links': 'list[WebLinkWithDeviceType]',
        'transport': 'TransitTransport',
        'intermediate_stops': 'list[TransitStop]',
        'agency': 'Agency',
        'attributions': 'list[Attribution]',
        'fares': 'list[Fare]',
        'booking': 'WebLink',
        'spans': 'list[TransitSpan]',
        'incidents': 'list[TransitIncident]'
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
        'booking_links': 'bookingLinks',
        'transport': 'transport',
        'intermediate_stops': 'intermediateStops',
        'agency': 'agency',
        'attributions': 'attributions',
        'fares': 'fares',
        'booking': 'booking',
        'spans': 'spans',
        'incidents': 'incidents'
    }

    def __init__(self, id=None, type=None, pre_actions=None, actions=None, language=None, post_actions=None, turn_by_turn_actions=None, departure=None, arrival=None, passthrough=None, summary=None, travel_summary=None, polyline=None, notices=None, booking_links=None, transport=None, intermediate_stops=None, agency=None, attributions=None, fares=None, booking=None, spans=None, incidents=None):  # noqa: E501
        """TransitSection - a model defined in Swagger"""  # noqa: E501
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
        self._booking_links = None
        self._transport = None
        self._intermediate_stops = None
        self._agency = None
        self._attributions = None
        self._fares = None
        self._booking = None
        self._spans = None
        self._incidents = None
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
        if booking_links is not None:
            self.booking_links = booking_links
        if transport is not None:
            self.transport = transport
        if intermediate_stops is not None:
            self.intermediate_stops = intermediate_stops
        if agency is not None:
            self.agency = agency
        if attributions is not None:
            self.attributions = attributions
        if fares is not None:
            self.fares = fares
        if booking is not None:
            self.booking = booking
        if spans is not None:
            self.spans = spans
        if incidents is not None:
            self.incidents = incidents

    @property
    def id(self):
        """Gets the id of this TransitSection.  # noqa: E501

        Unique identifier of the section  # noqa: E501

        :return: The id of this TransitSection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransitSection.

        Unique identifier of the section  # noqa: E501

        :param id: The id of this TransitSection.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this TransitSection.  # noqa: E501

        Section type used by the client to identify what extension to the BaseSection are available.  # noqa: E501

        :return: The type of this TransitSection.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TransitSection.

        Section type used by the client to identify what extension to the BaseSection are available.  # noqa: E501

        :param type: The type of this TransitSection.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def pre_actions(self):
        """Gets the pre_actions of this TransitSection.  # noqa: E501

        Actions that must be done prior to `departure`.  # noqa: E501

        :return: The pre_actions of this TransitSection.  # noqa: E501
        :rtype: list[TransitPreAction]
        """
        return self._pre_actions

    @pre_actions.setter
    def pre_actions(self, pre_actions):
        """Sets the pre_actions of this TransitSection.

        Actions that must be done prior to `departure`.  # noqa: E501

        :param pre_actions: The pre_actions of this TransitSection.  # noqa: E501
        :type: list[TransitPreAction]
        """

        self._pre_actions = pre_actions

    @property
    def actions(self):
        """Gets the actions of this TransitSection.  # noqa: E501

        Actions that must be done during the travel portion of the section, i.e., between `departure` and `arrival`.  *NOTE:* currentRoad and nextRoad are not populated for actions.   # noqa: E501

        :return: The actions of this TransitSection.  # noqa: E501
        :rtype: list[OffsetAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this TransitSection.

        Actions that must be done during the travel portion of the section, i.e., between `departure` and `arrival`.  *NOTE:* currentRoad and nextRoad are not populated for actions.   # noqa: E501

        :param actions: The actions of this TransitSection.  # noqa: E501
        :type: list[OffsetAction]
        """

        self._actions = actions

    @property
    def language(self):
        """Gets the language of this TransitSection.  # noqa: E501

        Language of the localized strings in the section, if any, in BCP47 format.  # noqa: E501

        :return: The language of this TransitSection.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this TransitSection.

        Language of the localized strings in the section, if any, in BCP47 format.  # noqa: E501

        :param language: The language of this TransitSection.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def post_actions(self):
        """Gets the post_actions of this TransitSection.  # noqa: E501

        Actions that must be done after `arrival`.  # noqa: E501

        :return: The post_actions of this TransitSection.  # noqa: E501
        :rtype: list[TransitPostAction]
        """
        return self._post_actions

    @post_actions.setter
    def post_actions(self, post_actions):
        """Sets the post_actions of this TransitSection.

        Actions that must be done after `arrival`.  # noqa: E501

        :param post_actions: The post_actions of this TransitSection.  # noqa: E501
        :type: list[TransitPostAction]
        """

        self._post_actions = post_actions

    @property
    def turn_by_turn_actions(self):
        """Gets the turn_by_turn_actions of this TransitSection.  # noqa: E501

        Actions for turn by turn guidance during the travel portion of the section, i.e., between `departure` and `arrival`.  # noqa: E501

        :return: The turn_by_turn_actions of this TransitSection.  # noqa: E501
        :rtype: list[OffsetAction]
        """
        return self._turn_by_turn_actions

    @turn_by_turn_actions.setter
    def turn_by_turn_actions(self, turn_by_turn_actions):
        """Sets the turn_by_turn_actions of this TransitSection.

        Actions for turn by turn guidance during the travel portion of the section, i.e., between `departure` and `arrival`.  # noqa: E501

        :param turn_by_turn_actions: The turn_by_turn_actions of this TransitSection.  # noqa: E501
        :type: list[OffsetAction]
        """

        self._turn_by_turn_actions = turn_by_turn_actions

    @property
    def departure(self):
        """Gets the departure of this TransitSection.  # noqa: E501


        :return: The departure of this TransitSection.  # noqa: E501
        :rtype: TransitDeparture
        """
        return self._departure

    @departure.setter
    def departure(self, departure):
        """Sets the departure of this TransitSection.


        :param departure: The departure of this TransitSection.  # noqa: E501
        :type: TransitDeparture
        """
        if departure is None:
            raise ValueError("Invalid value for `departure`, must not be `None`")  # noqa: E501

        self._departure = departure

    @property
    def arrival(self):
        """Gets the arrival of this TransitSection.  # noqa: E501


        :return: The arrival of this TransitSection.  # noqa: E501
        :rtype: TransitDeparture
        """
        return self._arrival

    @arrival.setter
    def arrival(self, arrival):
        """Sets the arrival of this TransitSection.


        :param arrival: The arrival of this TransitSection.  # noqa: E501
        :type: TransitDeparture
        """
        if arrival is None:
            raise ValueError("Invalid value for `arrival`, must not be `None`")  # noqa: E501

        self._arrival = arrival

    @property
    def passthrough(self):
        """Gets the passthrough of this TransitSection.  # noqa: E501

        List of via waypoints this section is passing through.  Each via waypoint of the request that is a `passThrough=true` waypoint, appears as a `Passthrough` in the response. It appears in the section that starts with the closest non-passthrough via specified before it or origin.  The passthrough vias appear in this list in the order they are traversed. They are traversed in the order they are specified in the request.   # noqa: E501

        :return: The passthrough of this TransitSection.  # noqa: E501
        :rtype: list[Passthrough]
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this TransitSection.

        List of via waypoints this section is passing through.  Each via waypoint of the request that is a `passThrough=true` waypoint, appears as a `Passthrough` in the response. It appears in the section that starts with the closest non-passthrough via specified before it or origin.  The passthrough vias appear in this list in the order they are traversed. They are traversed in the order they are specified in the request.   # noqa: E501

        :param passthrough: The passthrough of this TransitSection.  # noqa: E501
        :type: list[Passthrough]
        """

        self._passthrough = passthrough

    @property
    def summary(self):
        """Gets the summary of this TransitSection.  # noqa: E501

        Total value of key attributes (e.g., duration, length) summed up for the entire section, including `preActions`, `postActions`, and the travel portion of the section.   # noqa: E501

        :return: The summary of this TransitSection.  # noqa: E501
        :rtype: AllOfTransitSectionSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this TransitSection.

        Total value of key attributes (e.g., duration, length) summed up for the entire section, including `preActions`, `postActions`, and the travel portion of the section.   # noqa: E501

        :param summary: The summary of this TransitSection.  # noqa: E501
        :type: AllOfTransitSectionSummary
        """

        self._summary = summary

    @property
    def travel_summary(self):
        """Gets the travel_summary of this TransitSection.  # noqa: E501

        Total value of key attributes (e.g., duration, length) summed up for just the travel portion of the section, between `departure` and `arrival`. `preActions` and `postActions` are excluded.   # noqa: E501

        :return: The travel_summary of this TransitSection.  # noqa: E501
        :rtype: AllOfTransitSectionTravelSummary
        """
        return self._travel_summary

    @travel_summary.setter
    def travel_summary(self, travel_summary):
        """Sets the travel_summary of this TransitSection.

        Total value of key attributes (e.g., duration, length) summed up for just the travel portion of the section, between `departure` and `arrival`. `preActions` and `postActions` are excluded.   # noqa: E501

        :param travel_summary: The travel_summary of this TransitSection.  # noqa: E501
        :type: AllOfTransitSectionTravelSummary
        """

        self._travel_summary = travel_summary

    @property
    def polyline(self):
        """Gets the polyline of this TransitSection.  # noqa: E501


        :return: The polyline of this TransitSection.  # noqa: E501
        :rtype: Polyline
        """
        return self._polyline

    @polyline.setter
    def polyline(self, polyline):
        """Sets the polyline of this TransitSection.


        :param polyline: The polyline of this TransitSection.  # noqa: E501
        :type: Polyline
        """

        self._polyline = polyline

    @property
    def notices(self):
        """Gets the notices of this TransitSection.  # noqa: E501

        Contains a list of issues related to this section of the route.   # noqa: E501

        :return: The notices of this TransitSection.  # noqa: E501
        :rtype: list[TransitNotice]
        """
        return self._notices

    @notices.setter
    def notices(self, notices):
        """Sets the notices of this TransitSection.

        Contains a list of issues related to this section of the route.   # noqa: E501

        :param notices: The notices of this TransitSection.  # noqa: E501
        :type: list[TransitNotice]
        """

        self._notices = notices

    @property
    def booking_links(self):
        """Gets the booking_links of this TransitSection.  # noqa: E501

        Links to external ticket booking services  # noqa: E501

        :return: The booking_links of this TransitSection.  # noqa: E501
        :rtype: list[WebLinkWithDeviceType]
        """
        return self._booking_links

    @booking_links.setter
    def booking_links(self, booking_links):
        """Sets the booking_links of this TransitSection.

        Links to external ticket booking services  # noqa: E501

        :param booking_links: The booking_links of this TransitSection.  # noqa: E501
        :type: list[WebLinkWithDeviceType]
        """

        self._booking_links = booking_links

    @property
    def transport(self):
        """Gets the transport of this TransitSection.  # noqa: E501


        :return: The transport of this TransitSection.  # noqa: E501
        :rtype: TransitTransport
        """
        return self._transport

    @transport.setter
    def transport(self, transport):
        """Sets the transport of this TransitSection.


        :param transport: The transport of this TransitSection.  # noqa: E501
        :type: TransitTransport
        """

        self._transport = transport

    @property
    def intermediate_stops(self):
        """Gets the intermediate_stops of this TransitSection.  # noqa: E501

        Intermediate stops between departure and destination of the transit line. It can be missing if this information is not available or not requested.   # noqa: E501

        :return: The intermediate_stops of this TransitSection.  # noqa: E501
        :rtype: list[TransitStop]
        """
        return self._intermediate_stops

    @intermediate_stops.setter
    def intermediate_stops(self, intermediate_stops):
        """Sets the intermediate_stops of this TransitSection.

        Intermediate stops between departure and destination of the transit line. It can be missing if this information is not available or not requested.   # noqa: E501

        :param intermediate_stops: The intermediate_stops of this TransitSection.  # noqa: E501
        :type: list[TransitStop]
        """

        self._intermediate_stops = intermediate_stops

    @property
    def agency(self):
        """Gets the agency of this TransitSection.  # noqa: E501


        :return: The agency of this TransitSection.  # noqa: E501
        :rtype: Agency
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        """Sets the agency of this TransitSection.


        :param agency: The agency of this TransitSection.  # noqa: E501
        :type: Agency
        """

        self._agency = agency

    @property
    def attributions(self):
        """Gets the attributions of this TransitSection.  # noqa: E501

        List of required attributions to display.  # noqa: E501

        :return: The attributions of this TransitSection.  # noqa: E501
        :rtype: list[Attribution]
        """
        return self._attributions

    @attributions.setter
    def attributions(self, attributions):
        """Sets the attributions of this TransitSection.

        List of required attributions to display.  # noqa: E501

        :param attributions: The attributions of this TransitSection.  # noqa: E501
        :type: list[Attribution]
        """

        self._attributions = attributions

    @property
    def fares(self):
        """Gets the fares of this TransitSection.  # noqa: E501

        List of tickets to pay for this section of the route  # noqa: E501

        :return: The fares of this TransitSection.  # noqa: E501
        :rtype: list[Fare]
        """
        return self._fares

    @fares.setter
    def fares(self, fares):
        """Sets the fares of this TransitSection.

        List of tickets to pay for this section of the route  # noqa: E501

        :param fares: The fares of this TransitSection.  # noqa: E501
        :type: list[Fare]
        """

        self._fares = fares

    @property
    def booking(self):
        """Gets the booking of this TransitSection.  # noqa: E501


        :return: The booking of this TransitSection.  # noqa: E501
        :rtype: WebLink
        """
        return self._booking

    @booking.setter
    def booking(self, booking):
        """Sets the booking of this TransitSection.


        :param booking: The booking of this TransitSection.  # noqa: E501
        :type: WebLink
        """

        self._booking = booking

    @property
    def spans(self):
        """Gets the spans of this TransitSection.  # noqa: E501

        Span attached to a `Section` describing transit content.   # noqa: E501

        :return: The spans of this TransitSection.  # noqa: E501
        :rtype: list[TransitSpan]
        """
        return self._spans

    @spans.setter
    def spans(self, spans):
        """Sets the spans of this TransitSection.

        Span attached to a `Section` describing transit content.   # noqa: E501

        :param spans: The spans of this TransitSection.  # noqa: E501
        :type: list[TransitSpan]
        """

        self._spans = spans

    @property
    def incidents(self):
        """Gets the incidents of this TransitSection.  # noqa: E501

        A list of all incidents that apply to the section.  # noqa: E501

        :return: The incidents of this TransitSection.  # noqa: E501
        :rtype: list[TransitIncident]
        """
        return self._incidents

    @incidents.setter
    def incidents(self, incidents):
        """Sets the incidents of this TransitSection.

        A list of all incidents that apply to the section.  # noqa: E501

        :param incidents: The incidents of this TransitSection.  # noqa: E501
        :type: list[TransitIncident]
        """

        self._incidents = incidents

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
        if issubclass(TransitSection, dict):
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
        if not isinstance(other, TransitSection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

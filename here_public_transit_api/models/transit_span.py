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

class TransitSpan(object):
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
        'offset': 'int',
        'length': 'Distance',
        'duration': 'Duration',
        'country_code': 'CountryCode',
        'names': 'list[LocalizedString]',
        'segment_id': 'str',
        'segment_ref': 'str',
        'ref_replacements': 'dict(str, str)'
    }

    attribute_map = {
        'offset': 'offset',
        'length': 'length',
        'duration': 'duration',
        'country_code': 'countryCode',
        'names': 'names',
        'segment_id': 'segmentId',
        'segment_ref': 'segmentRef',
        'ref_replacements': 'refReplacements'
    }

    def __init__(self, offset=None, length=None, duration=None, country_code=None, names=None, segment_id=None, segment_ref=None, ref_replacements=None):  # noqa: E501
        """TransitSpan - a model defined in Swagger"""  # noqa: E501
        self._offset = None
        self._length = None
        self._duration = None
        self._country_code = None
        self._names = None
        self._segment_id = None
        self._segment_ref = None
        self._ref_replacements = None
        self.discriminator = None
        if offset is not None:
            self.offset = offset
        if length is not None:
            self.length = length
        if duration is not None:
            self.duration = duration
        if country_code is not None:
            self.country_code = country_code
        if names is not None:
            self.names = names
        if segment_id is not None:
            self.segment_id = segment_id
        if segment_ref is not None:
            self.segment_ref = segment_ref
        if ref_replacements is not None:
            self.ref_replacements = ref_replacements

    @property
    def offset(self):
        """Gets the offset of this TransitSpan.  # noqa: E501

        Offset of a coordinate in the section's polyline.   # noqa: E501

        :return: The offset of this TransitSpan.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this TransitSpan.

        Offset of a coordinate in the section's polyline.   # noqa: E501

        :param offset: The offset of this TransitSpan.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def length(self):
        """Gets the length of this TransitSpan.  # noqa: E501


        :return: The length of this TransitSpan.  # noqa: E501
        :rtype: Distance
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this TransitSpan.


        :param length: The length of this TransitSpan.  # noqa: E501
        :type: Distance
        """

        self._length = length

    @property
    def duration(self):
        """Gets the duration of this TransitSpan.  # noqa: E501


        :return: The duration of this TransitSpan.  # noqa: E501
        :rtype: Duration
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TransitSpan.


        :param duration: The duration of this TransitSpan.  # noqa: E501
        :type: Duration
        """

        self._duration = duration

    @property
    def country_code(self):
        """Gets the country_code of this TransitSpan.  # noqa: E501


        :return: The country_code of this TransitSpan.  # noqa: E501
        :rtype: CountryCode
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this TransitSpan.


        :param country_code: The country_code of this TransitSpan.  # noqa: E501
        :type: CountryCode
        """

        self._country_code = country_code

    @property
    def names(self):
        """Gets the names of this TransitSpan.  # noqa: E501

        Designated name for the span (e.g. a street name or a transport name)  # noqa: E501

        :return: The names of this TransitSpan.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this TransitSpan.

        Designated name for the span (e.g. a street name or a transport name)  # noqa: E501

        :param names: The names of this TransitSpan.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._names = names

    @property
    def segment_id(self):
        """Gets the segment_id of this TransitSpan.  # noqa: E501

        **Disclaimer: This property is currently in beta release, and is therefore subject to breaking changes.**  The directed topology segment id including prefix (e.g '+here:cm:segment:').  The id consists of two parts. * The direction ('+' or '-') * followed by the topology segment id (a unique identifier within the HERE platform catalogs).  The direction specifies whether the route is using the segment in its canonical direction ('+' aka traveling along the geometry's direction), or against it ('-' aka traveling against the geometry's direction).  This attribute will not appear for HERE Public Transit v8 and HERE Intermodal Routing v8 requests   # noqa: E501

        :return: The segment_id of this TransitSpan.  # noqa: E501
        :rtype: str
        """
        return self._segment_id

    @segment_id.setter
    def segment_id(self, segment_id):
        """Sets the segment_id of this TransitSpan.

        **Disclaimer: This property is currently in beta release, and is therefore subject to breaking changes.**  The directed topology segment id including prefix (e.g '+here:cm:segment:').  The id consists of two parts. * The direction ('+' or '-') * followed by the topology segment id (a unique identifier within the HERE platform catalogs).  The direction specifies whether the route is using the segment in its canonical direction ('+' aka traveling along the geometry's direction), or against it ('-' aka traveling against the geometry's direction).  This attribute will not appear for HERE Public Transit v8 and HERE Intermodal Routing v8 requests   # noqa: E501

        :param segment_id: The segment_id of this TransitSpan.  # noqa: E501
        :type: str
        """

        self._segment_id = segment_id

    @property
    def segment_ref(self):
        """Gets the segment_ref of this TransitSpan.  # noqa: E501

        A reference to the HMC topology segment used in this span.  The standard representation of a segment reference has the following structure: {catalogHrn}:{catalogVersion}:({layerId})?:{tileId}:{segmentId}(#{direction}({startOffset}..{endOffset})?)?  The individual parts are: * catalogHrn: The HERE Resource Name that identifies the source catalog of the segment, example: hrn:here:data::olp-here:rib-2 * catalogVersion: The catalog version * layerId (optional): The layer inside the catalog where the segment can be found, example: topology-geometry * tileId: The HERE tile key of the partition/tile where the segment is located in the given version of the catalog. This can be on a lower level than the actual segment is stored at (for example, the provided tile ID can be on level 14, despite topology-geometry partitions being tiled at level 12). The level of a HERE tile key is indicated by the position of the highest set bit in binary representation. Since the HERE tile key represents a morton code of the x and y portion of the Tile ID, the level 12 tile ID can be retrieved from the level 14 tile ID by removing the 4 least significant bits (or 2 bits per level) or 1 hexidecimal digit. For example, the level 14 tile 377894441 is included in the level 12 tile 23618402 (377894441<sub>10</sub> = 16863629<sub>16</sub> &rightarrow; 1686362<sub>16</sub> = 23618402<sub>10</sub>) * segmentId: The identifier of the referenced topology segment inside the catalog, example: here:cm:segment:84905195 * direction (optional): Either '*' for undirected or bidirectional, '+' for positive direction, '-' for negative direction, or '?' for unknown direction (not used by the routing service) * startOffset/endOffset (optional): The start- and end offset are non-negative numbers between 0 and 1, representing the start and end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments). Example: 0.7..1  This attribute will not appear for HERE Public Transit v8 and HERE Intermodal Routing v8 requests  Example of a segment reference in standard representation: hrn:here:data::olp-here:rib-2:1363::377894441:here:cm:segment:84905195#+0.7..1  The segment references can also be provided in a compact representation, to reduce the response size. In the compact representation, some parts are replaced by placeholders, which can be resolved using the refReplacements dictionary in the parent section. The placeholder format is \\$\\d+ and need to be surrounded by columns or string start/end. It can be captured with the following regular expression: (^|:)\\$\\d+(:|$)  Example of the segment reference previously mentioned in compact representation: $0:377894441:$1:84905195#+0.7..1 With the corresponding refReplacements: \"refReplacements\": {   \"0\": \"hrn:here:data::olp-here:rib-2:1363:\",   \"1\": \"here:cm:segment\" }   # noqa: E501

        :return: The segment_ref of this TransitSpan.  # noqa: E501
        :rtype: str
        """
        return self._segment_ref

    @segment_ref.setter
    def segment_ref(self, segment_ref):
        """Sets the segment_ref of this TransitSpan.

        A reference to the HMC topology segment used in this span.  The standard representation of a segment reference has the following structure: {catalogHrn}:{catalogVersion}:({layerId})?:{tileId}:{segmentId}(#{direction}({startOffset}..{endOffset})?)?  The individual parts are: * catalogHrn: The HERE Resource Name that identifies the source catalog of the segment, example: hrn:here:data::olp-here:rib-2 * catalogVersion: The catalog version * layerId (optional): The layer inside the catalog where the segment can be found, example: topology-geometry * tileId: The HERE tile key of the partition/tile where the segment is located in the given version of the catalog. This can be on a lower level than the actual segment is stored at (for example, the provided tile ID can be on level 14, despite topology-geometry partitions being tiled at level 12). The level of a HERE tile key is indicated by the position of the highest set bit in binary representation. Since the HERE tile key represents a morton code of the x and y portion of the Tile ID, the level 12 tile ID can be retrieved from the level 14 tile ID by removing the 4 least significant bits (or 2 bits per level) or 1 hexidecimal digit. For example, the level 14 tile 377894441 is included in the level 12 tile 23618402 (377894441<sub>10</sub> = 16863629<sub>16</sub> &rightarrow; 1686362<sub>16</sub> = 23618402<sub>10</sub>) * segmentId: The identifier of the referenced topology segment inside the catalog, example: here:cm:segment:84905195 * direction (optional): Either '*' for undirected or bidirectional, '+' for positive direction, '-' for negative direction, or '?' for unknown direction (not used by the routing service) * startOffset/endOffset (optional): The start- and end offset are non-negative numbers between 0 and 1, representing the start and end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments). Example: 0.7..1  This attribute will not appear for HERE Public Transit v8 and HERE Intermodal Routing v8 requests  Example of a segment reference in standard representation: hrn:here:data::olp-here:rib-2:1363::377894441:here:cm:segment:84905195#+0.7..1  The segment references can also be provided in a compact representation, to reduce the response size. In the compact representation, some parts are replaced by placeholders, which can be resolved using the refReplacements dictionary in the parent section. The placeholder format is \\$\\d+ and need to be surrounded by columns or string start/end. It can be captured with the following regular expression: (^|:)\\$\\d+(:|$)  Example of the segment reference previously mentioned in compact representation: $0:377894441:$1:84905195#+0.7..1 With the corresponding refReplacements: \"refReplacements\": {   \"0\": \"hrn:here:data::olp-here:rib-2:1363:\",   \"1\": \"here:cm:segment\" }   # noqa: E501

        :param segment_ref: The segment_ref of this TransitSpan.  # noqa: E501
        :type: str
        """

        self._segment_ref = segment_ref

    @property
    def ref_replacements(self):
        """Gets the ref_replacements of this TransitSpan.  # noqa: E501

        Dictionary of placeholders to replacement strings for the compact representation of map entity references.  This attribute will not appear for HERE Public Transit v8 and HERE Intermodal Routing v8 requests   # noqa: E501

        :return: The ref_replacements of this TransitSpan.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._ref_replacements

    @ref_replacements.setter
    def ref_replacements(self, ref_replacements):
        """Sets the ref_replacements of this TransitSpan.

        Dictionary of placeholders to replacement strings for the compact representation of map entity references.  This attribute will not appear for HERE Public Transit v8 and HERE Intermodal Routing v8 requests   # noqa: E501

        :param ref_replacements: The ref_replacements of this TransitSpan.  # noqa: E501
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
        if issubclass(TransitSpan, dict):
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
        if not isinstance(other, TransitSpan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

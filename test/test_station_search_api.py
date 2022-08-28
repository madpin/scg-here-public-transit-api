# coding: utf-8

"""
    Public Transit API

    Public Transit is a set of three REST APIs that provides public transit routing information and public transit stations information available within an area or for a given station.   # noqa: E501

    OpenAPI spec version: 8.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import here_public_transit_api
from here_public_transit_api.api.station_search_api import StationSearchApi  # noqa: E501
from here_public_transit_api.rest import ApiException


class TestStationSearchApi(unittest.TestCase):
    """StationSearchApi unit test stubs"""

    def setUp(self):
        self.api = StationSearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_health(self):
        """Test case for get_health

        Health  # noqa: E501
        """
        pass

    def test_get_stations(self):
        """Test case for get_stations

        Stations  # noqa: E501
        """
        pass

    def test_get_version(self):
        """Test case for get_version

        Version  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
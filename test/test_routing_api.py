# coding: utf-8

"""
    Routing API v8

    A location service providing customizable route calculations for a variety of vehicle types as well as pedestrian modes.  # noqa: E501

    OpenAPI spec version: 8.52.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import here_public_transit_api
from here_public_transit_api.api.routing_api import RoutingApi  # noqa: E501
from here_public_transit_api.rest import ApiException


class TestRoutingApi(unittest.TestCase):
    """RoutingApi unit test stubs"""

    def setUp(self):
        self.api = RoutingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_calculate_routes(self):
        """Test case for calculate_routes

        Calculate routes via GET  # noqa: E501
        """
        pass

    def test_calculate_routes_post(self):
        """Test case for calculate_routes_post

        Calculate routes via POST  # noqa: E501
        """
        pass

    def test_get_routes_by_handle(self):
        """Test case for get_routes_by_handle

        Get route by handle via GET  # noqa: E501
        """
        pass

    def test_get_routes_by_handle_post(self):
        """Test case for get_routes_by_handle_post

        Get route by handle via POST  # noqa: E501
        """
        pass

    def test_import_route(self):
        """Test case for import_route

        Calculate a route from a sequence of trace points  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

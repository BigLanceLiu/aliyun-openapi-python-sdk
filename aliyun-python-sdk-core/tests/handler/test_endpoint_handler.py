# coding=utf-8

from alibabacloud.credentials.provider import DefaultChainedCredentialsProvider
from alibabacloud.endpoint.resolver_endpoint_request import ResolveEndpointRequest
from tests import unittest

class TestResolveEndpointRequest(unittest.TestCase):
    def test_request(self):
        chained_credentials = DefaultChainedCredentialsProvider(None)
        r = ResolveEndpointRequest(
            "cn-hangzhou", "product_code", "location_service_code", "innerAPI")
        self.assertFalse(r.is_open_api_endpoint())
        r = ResolveEndpointRequest(
            "cn-hangzhou", "product_code", "location_service_code", "openAPI")
        self.assertTrue(r.is_open_api_endpoint())
        r = ResolveEndpointRequest("cn-hangzhou", "product_code", "location_service_code", None)
        self.assertTrue(r.is_open_api_endpoint())
        
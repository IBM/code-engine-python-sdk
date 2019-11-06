# coding: utf-8

# Copyright 2019 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Test the mysdk service API operations
"""

import pytest
import unittest
import os
import mysdk
from ibm_cloud_sdk_core.authenticators import NoAuthAuthenticator


@pytest.mark.skipif(
    os.getenv('VCAP_SERVICES') is None, reason='requires VCAP_SERVICES')
class TestExampleServiceV1(unittest.TestCase):
    def setUp(self):
        authenticator = NoAuthAuthenticator()
        self.example_service = mysdk.ExampleServiceV1(authenticator)
        self.example_service.set_service_url("http://localhost:3000")

    def tearDown(self):
        # Delete the resources
        print("Clean up complete.")

    def test_get_resource(self):
        env = self.example_service.get_resource("1").get_result()
        assert env is not None

    def test_list_resources(self):
        env = self.example_service.list_resources().get_result()
        assert env is not None

    def test_create_resource(self):
        env = self.example_service.create_resource(3, "To Kill a Mockingbird", tag="Book").get_result()
        assert env is not None

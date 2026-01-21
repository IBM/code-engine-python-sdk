# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
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
Unit Tests for IbmCloudCodeEngineV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import responses
import urllib
from ibm_code_engine_sdk.ibm_cloud_code_engine_v1 import *

service = IbmCloudCodeEngineV1(authenticator=NoAuthAuthenticator())

base_url = 'https://ibm-cloud-code-engine.cloud.ibm.com/api/v1'
service.set_service_url(base_url)

##############################################################################
# Start of Service: GetKubeconfig
##############################################################################
# region


class TestListKubeconfig:
    """
    Test Class for list_kubeconfig
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_kubeconfig_all_params(self):
        """
        list_kubeconfig()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/namespaces/testString/config')
        mock_response = '"operation_response"'
        responses.add(responses.GET, url, body=mock_response, content_type='text/plain', status=200)

        # Set up parameter values
        refresh_token = 'testString'
        id = 'testString'
        accept = 'text/plain'

        # Invoke method
        response = service.list_kubeconfig(refresh_token, id, accept=accept, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    @responses.activate
    def test_list_kubeconfig_required_params(self):
        """
        test_list_kubeconfig_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/namespaces/testString/config')
        mock_response = '"operation_response"'
        responses.add(responses.GET, url, body=mock_response, content_type='text/plain', status=200)

        # Set up parameter values
        refresh_token = 'testString'
        id = 'testString'

        # Invoke method
        response = service.list_kubeconfig(refresh_token, id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    @responses.activate
    def test_list_kubeconfig_value_error(self):
        """
        test_list_kubeconfig_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/namespaces/testString/config')
        mock_response = '"operation_response"'
        responses.add(responses.GET, url, body=mock_response, content_type='text/plain', status=200)

        # Set up parameter values
        refresh_token = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "refresh_token": refresh_token,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_kubeconfig(**req_copy)


class TestGetKubeconfig:
    """
    Test Class for get_kubeconfig
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_kubeconfig_all_params(self):
        """
        get_kubeconfig()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/project/testString/config')
        mock_response = '"operation_response"'
        responses.add(responses.GET, url, body=mock_response, content_type='text/plain', status=200)

        # Set up parameter values
        x_delegated_refresh_token = 'testString'
        id = 'testString'
        accept = 'text/plain'

        # Invoke method
        response = service.get_kubeconfig(x_delegated_refresh_token, id, accept=accept, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    @responses.activate
    def test_get_kubeconfig_required_params(self):
        """
        test_get_kubeconfig_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/project/testString/config')
        mock_response = '"operation_response"'
        responses.add(responses.GET, url, body=mock_response, content_type='text/plain', status=200)

        # Set up parameter values
        x_delegated_refresh_token = 'testString'
        id = 'testString'

        # Invoke method
        response = service.get_kubeconfig(x_delegated_refresh_token, id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    @responses.activate
    def test_get_kubeconfig_value_error(self):
        """
        test_get_kubeconfig_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/project/testString/config')
        mock_response = '"operation_response"'
        responses.add(responses.GET, url, body=mock_response, content_type='text/plain', status=200)

        # Set up parameter values
        x_delegated_refresh_token = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "x_delegated_refresh_token": x_delegated_refresh_token,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_kubeconfig(**req_copy)


# endregion
##############################################################################
# End of Service: GetKubeconfig
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region

# endregion
##############################################################################
# End of Model Tests
##############################################################################

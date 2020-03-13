# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
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

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import requests
import responses
from mysdk.example_service_v1 import *


service = ExampleServiceV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'http://cloud.ibm.com/mysdk/v1'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Resources
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_resources
#-----------------------------------------------------------------------------
class TestListResources():

    #--------------------------------------------------------
    # list_resources()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resources_all_params(self):
        # Set up mock
        url = base_url + '/resources'
        mock_response = '{"offset": 6, "limit": 5, "resources": [{"resource_id": "resource_id", "name": "name", "tag": "tag", "read_only": "read_only"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        limit = 38

        # Invoke method
        response = service.list_resources(
            limit=limit
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'limit={}'.format(limit) in query_string


    #--------------------------------------------------------
    # test_list_resources_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resources_required_params(self):
        # Set up mock
        url = base_url + '/resources'
        mock_response = '{"offset": 6, "limit": 5, "resources": [{"resource_id": "resource_id", "name": "name", "tag": "tag", "read_only": "read_only"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_resources()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_resource
#-----------------------------------------------------------------------------
class TestCreateResource():

    #--------------------------------------------------------
    # create_resource()
    #--------------------------------------------------------
    @responses.activate
    def test_create_resource_all_params(self):
        # Set up mock
        url = base_url + '/resources'
        mock_response = '{"resource_id": "resource_id", "name": "name", "tag": "tag", "read_only": "read_only"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        resource_id = 'testString'
        name = 'testString'
        tag = 'testString'

        # Invoke method
        response = service.create_resource(
            resource_id=resource_id,
            name=name,
            tag=tag,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['resource_id'] == resource_id
        assert req_body['name'] == name
        assert req_body['tag'] == tag


    #--------------------------------------------------------
    # test_create_resource_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_resource_required_params(self):
        # Set up mock
        url = base_url + '/resources'
        mock_response = '{"resource_id": "resource_id", "name": "name", "tag": "tag", "read_only": "read_only"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Invoke method
        response = service.create_resource()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


#-----------------------------------------------------------------------------
# Test Class for get_resource
#-----------------------------------------------------------------------------
class TestGetResource():

    #--------------------------------------------------------
    # get_resource()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_all_params(self):
        # Set up mock
        url = base_url + '/resources/testString'
        mock_response = '{"resource_id": "resource_id", "name": "name", "tag": "tag", "read_only": "read_only"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        resource_id = 'testString'

        # Invoke method
        response = service.get_resource(
            resource_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_resource_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_required_params(self):
        # Set up mock
        url = base_url + '/resources/testString'
        mock_response = '{"resource_id": "resource_id", "name": "name", "tag": "tag", "read_only": "read_only"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        resource_id = 'testString'

        # Invoke method
        response = service.get_resource(
            resource_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: Resources
##############################################################################


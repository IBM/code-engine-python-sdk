# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2024.
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
Unit Tests for CodeEngineV2
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from ibm_code_engine_sdk.code_engine_v2 import *

version = '2024-11-18'

_service = CodeEngineV2(authenticator=NoAuthAuthenticator())

_base_url = 'https://api.au-syd.codeengine.cloud.ibm.com/v2'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """

    # Form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if not request_url.endswith('/'):
        return request_url
    return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: Projects
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = CodeEngineV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CodeEngineV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CodeEngineV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListProjects:
    """
    Test Class for list_projects
    """

    @responses.activate
    def test_list_projects_all_params(self):
        """
        list_projects()
        """
        # Set up mock
        url = preprocess_url('/projects')
        mock_response = '{"first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}, "projects": [{"account_id": "4329073d16d2f3663f74bfa955259139", "created_at": "2021-03-29T12:18:13.992359829Z", "crn": "crn:v1:bluemix:public:codeengine:eu-de:a/4329073d16d2f3663f74bfa955259139:4e49b3e0-27a8-48d2-a784-c7ee48bb863b::", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "name": "project-name", "region": "us-east", "resource_group_id": "5c49eabcf5e85881a37e2d100a33b3df", "resource_type": "project_v2", "status": "active"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_projects(
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_projects_all_params_with_retries(self):
        # Enable retries and run test_list_projects_all_params.
        _service.enable_retries()
        self.test_list_projects_all_params()

        # Disable retries and run test_list_projects_all_params.
        _service.disable_retries()
        self.test_list_projects_all_params()

    @responses.activate
    def test_list_projects_required_params(self):
        """
        test_list_projects_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects')
        mock_response = '{"first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}, "projects": [{"account_id": "4329073d16d2f3663f74bfa955259139", "created_at": "2021-03-29T12:18:13.992359829Z", "crn": "crn:v1:bluemix:public:codeengine:eu-de:a/4329073d16d2f3663f74bfa955259139:4e49b3e0-27a8-48d2-a784-c7ee48bb863b::", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "name": "project-name", "region": "us-east", "resource_group_id": "5c49eabcf5e85881a37e2d100a33b3df", "resource_type": "project_v2", "status": "active"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_projects()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_projects_required_params_with_retries(self):
        # Enable retries and run test_list_projects_required_params.
        _service.enable_retries()
        self.test_list_projects_required_params()

        # Disable retries and run test_list_projects_required_params.
        _service.disable_retries()
        self.test_list_projects_required_params()

    @responses.activate
    def test_list_projects_with_pager_get_next(self):
        """
        test_list_projects_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects')
        mock_response1 = '{"next":{"start":"1"},"projects":[{"account_id":"4329073d16d2f3663f74bfa955259139","created_at":"2021-03-29T12:18:13.992359829Z","crn":"crn:v1:bluemix:public:codeengine:eu-de:a/4329073d16d2f3663f74bfa955259139:4e49b3e0-27a8-48d2-a784-c7ee48bb863b::","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b","id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","name":"project-name","region":"us-east","resource_group_id":"5c49eabcf5e85881a37e2d100a33b3df","resource_type":"project_v2","status":"active"}],"total_count":2,"limit":1}'
        mock_response2 = '{"projects":[{"account_id":"4329073d16d2f3663f74bfa955259139","created_at":"2021-03-29T12:18:13.992359829Z","crn":"crn:v1:bluemix:public:codeengine:eu-de:a/4329073d16d2f3663f74bfa955259139:4e49b3e0-27a8-48d2-a784-c7ee48bb863b::","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b","id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","name":"project-name","region":"us-east","resource_group_id":"5c49eabcf5e85881a37e2d100a33b3df","resource_type":"project_v2","status":"active"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = ProjectsPager(
            client=_service,
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_projects_with_pager_get_all(self):
        """
        test_list_projects_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects')
        mock_response1 = '{"next":{"start":"1"},"projects":[{"account_id":"4329073d16d2f3663f74bfa955259139","created_at":"2021-03-29T12:18:13.992359829Z","crn":"crn:v1:bluemix:public:codeengine:eu-de:a/4329073d16d2f3663f74bfa955259139:4e49b3e0-27a8-48d2-a784-c7ee48bb863b::","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b","id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","name":"project-name","region":"us-east","resource_group_id":"5c49eabcf5e85881a37e2d100a33b3df","resource_type":"project_v2","status":"active"}],"total_count":2,"limit":1}'
        mock_response2 = '{"projects":[{"account_id":"4329073d16d2f3663f74bfa955259139","created_at":"2021-03-29T12:18:13.992359829Z","crn":"crn:v1:bluemix:public:codeengine:eu-de:a/4329073d16d2f3663f74bfa955259139:4e49b3e0-27a8-48d2-a784-c7ee48bb863b::","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b","id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","name":"project-name","region":"us-east","resource_group_id":"5c49eabcf5e85881a37e2d100a33b3df","resource_type":"project_v2","status":"active"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = ProjectsPager(
            client=_service,
            limit=100,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateProject:
    """
    Test Class for create_project
    """

    @responses.activate
    def test_create_project_all_params(self):
        """
        create_project()
        """
        # Set up mock
        url = preprocess_url('/projects')
        mock_response = '{"account_id": "4329073d16d2f3663f74bfa955259139", "created_at": "2021-03-29T12:18:13.992359829Z", "crn": "crn:v1:bluemix:public:codeengine:eu-de:a/4329073d16d2f3663f74bfa955259139:4e49b3e0-27a8-48d2-a784-c7ee48bb863b::", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "name": "project-name", "region": "us-east", "resource_group_id": "5c49eabcf5e85881a37e2d100a33b3df", "resource_type": "project_v2", "status": "active"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        name = 'my-project'
        resource_group_id = 'b91e849cedb04e7e92bd68c040c672dc'
        tags = ['testString']

        # Invoke method
        response = _service.create_project(
            name,
            resource_group_id=resource_group_id,
            tags=tags,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'my-project'
        assert req_body['resource_group_id'] == 'b91e849cedb04e7e92bd68c040c672dc'
        assert req_body['tags'] == ['testString']

    def test_create_project_all_params_with_retries(self):
        # Enable retries and run test_create_project_all_params.
        _service.enable_retries()
        self.test_create_project_all_params()

        # Disable retries and run test_create_project_all_params.
        _service.disable_retries()
        self.test_create_project_all_params()

    @responses.activate
    def test_create_project_value_error(self):
        """
        test_create_project_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects')
        mock_response = '{"account_id": "4329073d16d2f3663f74bfa955259139", "created_at": "2021-03-29T12:18:13.992359829Z", "crn": "crn:v1:bluemix:public:codeengine:eu-de:a/4329073d16d2f3663f74bfa955259139:4e49b3e0-27a8-48d2-a784-c7ee48bb863b::", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "name": "project-name", "region": "us-east", "resource_group_id": "5c49eabcf5e85881a37e2d100a33b3df", "resource_type": "project_v2", "status": "active"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        name = 'my-project'
        resource_group_id = 'b91e849cedb04e7e92bd68c040c672dc'
        tags = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_project(**req_copy)

    def test_create_project_value_error_with_retries(self):
        # Enable retries and run test_create_project_value_error.
        _service.enable_retries()
        self.test_create_project_value_error()

        # Disable retries and run test_create_project_value_error.
        _service.disable_retries()
        self.test_create_project_value_error()


class TestGetProject:
    """
    Test Class for get_project
    """

    @responses.activate
    def test_get_project_all_params(self):
        """
        get_project()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005')
        mock_response = '{"account_id": "4329073d16d2f3663f74bfa955259139", "created_at": "2021-03-29T12:18:13.992359829Z", "crn": "crn:v1:bluemix:public:codeengine:eu-de:a/4329073d16d2f3663f74bfa955259139:4e49b3e0-27a8-48d2-a784-c7ee48bb863b::", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "name": "project-name", "region": "us-east", "resource_group_id": "5c49eabcf5e85881a37e2d100a33b3df", "resource_type": "project_v2", "status": "active"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.get_project(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_project_all_params_with_retries(self):
        # Enable retries and run test_get_project_all_params.
        _service.enable_retries()
        self.test_get_project_all_params()

        # Disable retries and run test_get_project_all_params.
        _service.disable_retries()
        self.test_get_project_all_params()

    @responses.activate
    def test_get_project_value_error(self):
        """
        test_get_project_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005')
        mock_response = '{"account_id": "4329073d16d2f3663f74bfa955259139", "created_at": "2021-03-29T12:18:13.992359829Z", "crn": "crn:v1:bluemix:public:codeengine:eu-de:a/4329073d16d2f3663f74bfa955259139:4e49b3e0-27a8-48d2-a784-c7ee48bb863b::", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "name": "project-name", "region": "us-east", "resource_group_id": "5c49eabcf5e85881a37e2d100a33b3df", "resource_type": "project_v2", "status": "active"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_project(**req_copy)

    def test_get_project_value_error_with_retries(self):
        # Enable retries and run test_get_project_value_error.
        _service.enable_retries()
        self.test_get_project_value_error()

        # Disable retries and run test_get_project_value_error.
        _service.disable_retries()
        self.test_get_project_value_error()


class TestDeleteProject:
    """
    Test Class for delete_project
    """

    @responses.activate
    def test_delete_project_all_params(self):
        """
        delete_project()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.delete_project(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_project_all_params_with_retries(self):
        # Enable retries and run test_delete_project_all_params.
        _service.enable_retries()
        self.test_delete_project_all_params()

        # Disable retries and run test_delete_project_all_params.
        _service.disable_retries()
        self.test_delete_project_all_params()

    @responses.activate
    def test_delete_project_value_error(self):
        """
        test_delete_project_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_project(**req_copy)

    def test_delete_project_value_error_with_retries(self):
        # Enable retries and run test_delete_project_value_error.
        _service.enable_retries()
        self.test_delete_project_value_error()

        # Disable retries and run test_delete_project_value_error.
        _service.disable_retries()
        self.test_delete_project_value_error()


class TestListAllowedOutboundDestination:
    """
    Test Class for list_allowed_outbound_destination
    """

    @responses.activate
    def test_list_allowed_outbound_destination_all_params(self):
        """
        list_allowed_outbound_destination()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/allowed_outbound_destinations')
        mock_response = '{"allowed_outbound_destinations": [{"entity_tag": "2385407409", "type": "cidr_block", "cidr_block": "cidr_block", "name": "name"}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_allowed_outbound_destination(
            project_id,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_allowed_outbound_destination_all_params_with_retries(self):
        # Enable retries and run test_list_allowed_outbound_destination_all_params.
        _service.enable_retries()
        self.test_list_allowed_outbound_destination_all_params()

        # Disable retries and run test_list_allowed_outbound_destination_all_params.
        _service.disable_retries()
        self.test_list_allowed_outbound_destination_all_params()

    @responses.activate
    def test_list_allowed_outbound_destination_required_params(self):
        """
        test_list_allowed_outbound_destination_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/allowed_outbound_destinations')
        mock_response = '{"allowed_outbound_destinations": [{"entity_tag": "2385407409", "type": "cidr_block", "cidr_block": "cidr_block", "name": "name"}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.list_allowed_outbound_destination(
            project_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_allowed_outbound_destination_required_params_with_retries(self):
        # Enable retries and run test_list_allowed_outbound_destination_required_params.
        _service.enable_retries()
        self.test_list_allowed_outbound_destination_required_params()

        # Disable retries and run test_list_allowed_outbound_destination_required_params.
        _service.disable_retries()
        self.test_list_allowed_outbound_destination_required_params()

    @responses.activate
    def test_list_allowed_outbound_destination_value_error(self):
        """
        test_list_allowed_outbound_destination_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/allowed_outbound_destinations')
        mock_response = '{"allowed_outbound_destinations": [{"entity_tag": "2385407409", "type": "cidr_block", "cidr_block": "cidr_block", "name": "name"}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_allowed_outbound_destination(**req_copy)

    def test_list_allowed_outbound_destination_value_error_with_retries(self):
        # Enable retries and run test_list_allowed_outbound_destination_value_error.
        _service.enable_retries()
        self.test_list_allowed_outbound_destination_value_error()

        # Disable retries and run test_list_allowed_outbound_destination_value_error.
        _service.disable_retries()
        self.test_list_allowed_outbound_destination_value_error()

    @responses.activate
    def test_list_allowed_outbound_destination_with_pager_get_next(self):
        """
        test_list_allowed_outbound_destination_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/allowed_outbound_destinations')
        mock_response1 = '{"next":{"start":"1"},"allowed_outbound_destinations":[{"entity_tag":"2385407409","type":"cidr_block","cidr_block":"cidr_block","name":"name"}],"total_count":2,"limit":1}'
        mock_response2 = '{"allowed_outbound_destinations":[{"entity_tag":"2385407409","type":"cidr_block","cidr_block":"cidr_block","name":"name"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = AllowedOutboundDestinationPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_allowed_outbound_destination_with_pager_get_all(self):
        """
        test_list_allowed_outbound_destination_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/allowed_outbound_destinations')
        mock_response1 = '{"next":{"start":"1"},"allowed_outbound_destinations":[{"entity_tag":"2385407409","type":"cidr_block","cidr_block":"cidr_block","name":"name"}],"total_count":2,"limit":1}'
        mock_response2 = '{"allowed_outbound_destinations":[{"entity_tag":"2385407409","type":"cidr_block","cidr_block":"cidr_block","name":"name"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = AllowedOutboundDestinationPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            limit=100,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateAllowedOutboundDestination:
    """
    Test Class for create_allowed_outbound_destination
    """

    @responses.activate
    def test_create_allowed_outbound_destination_all_params(self):
        """
        create_allowed_outbound_destination()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/allowed_outbound_destinations')
        mock_response = '{"entity_tag": "2385407409", "type": "cidr_block", "cidr_block": "cidr_block", "name": "name"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AllowedOutboundDestinationPrototypeCidrBlockDataPrototype model
        allowed_outbound_destination_prototype_model = {}
        allowed_outbound_destination_prototype_model['type'] = 'cidr_block'
        allowed_outbound_destination_prototype_model['cidr_block'] = 'testString'
        allowed_outbound_destination_prototype_model['name'] = 'testString'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        allowed_outbound_destination = allowed_outbound_destination_prototype_model

        # Invoke method
        response = _service.create_allowed_outbound_destination(
            project_id,
            allowed_outbound_destination,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == allowed_outbound_destination

    def test_create_allowed_outbound_destination_all_params_with_retries(self):
        # Enable retries and run test_create_allowed_outbound_destination_all_params.
        _service.enable_retries()
        self.test_create_allowed_outbound_destination_all_params()

        # Disable retries and run test_create_allowed_outbound_destination_all_params.
        _service.disable_retries()
        self.test_create_allowed_outbound_destination_all_params()

    @responses.activate
    def test_create_allowed_outbound_destination_required_params(self):
        """
        test_create_allowed_outbound_destination_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/allowed_outbound_destinations')
        mock_response = '{"entity_tag": "2385407409", "type": "cidr_block", "cidr_block": "cidr_block", "name": "name"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AllowedOutboundDestinationPrototypeCidrBlockDataPrototype model
        allowed_outbound_destination_prototype_model = {}
        allowed_outbound_destination_prototype_model['type'] = 'cidr_block'
        allowed_outbound_destination_prototype_model['cidr_block'] = 'testString'
        allowed_outbound_destination_prototype_model['name'] = 'testString'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        allowed_outbound_destination = allowed_outbound_destination_prototype_model

        # Invoke method
        response = _service.create_allowed_outbound_destination(
            project_id,
            allowed_outbound_destination,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == allowed_outbound_destination

    def test_create_allowed_outbound_destination_required_params_with_retries(self):
        # Enable retries and run test_create_allowed_outbound_destination_required_params.
        _service.enable_retries()
        self.test_create_allowed_outbound_destination_required_params()

        # Disable retries and run test_create_allowed_outbound_destination_required_params.
        _service.disable_retries()
        self.test_create_allowed_outbound_destination_required_params()

    @responses.activate
    def test_create_allowed_outbound_destination_value_error(self):
        """
        test_create_allowed_outbound_destination_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/allowed_outbound_destinations')
        mock_response = '{"entity_tag": "2385407409", "type": "cidr_block", "cidr_block": "cidr_block", "name": "name"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AllowedOutboundDestinationPrototypeCidrBlockDataPrototype model
        allowed_outbound_destination_prototype_model = {}
        allowed_outbound_destination_prototype_model['type'] = 'cidr_block'
        allowed_outbound_destination_prototype_model['cidr_block'] = 'testString'
        allowed_outbound_destination_prototype_model['name'] = 'testString'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        allowed_outbound_destination = allowed_outbound_destination_prototype_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "allowed_outbound_destination": allowed_outbound_destination,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_allowed_outbound_destination(**req_copy)

    def test_create_allowed_outbound_destination_value_error_with_retries(self):
        # Enable retries and run test_create_allowed_outbound_destination_value_error.
        _service.enable_retries()
        self.test_create_allowed_outbound_destination_value_error()

        # Disable retries and run test_create_allowed_outbound_destination_value_error.
        _service.disable_retries()
        self.test_create_allowed_outbound_destination_value_error()


class TestGetAllowedOutboundDestination:
    """
    Test Class for get_allowed_outbound_destination
    """

    @responses.activate
    def test_get_allowed_outbound_destination_all_params(self):
        """
        get_allowed_outbound_destination()
        """
        # Set up mock
        url = preprocess_url(
            '/projects/15314cc3-85b4-4338-903f-c28cdee6d005/allowed_outbound_destinations/my-allowed-outbound-destination'
        )
        mock_response = '{"entity_tag": "2385407409", "type": "cidr_block", "cidr_block": "cidr_block", "name": "name"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-allowed-outbound-destination'

        # Invoke method
        response = _service.get_allowed_outbound_destination(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_allowed_outbound_destination_all_params_with_retries(self):
        # Enable retries and run test_get_allowed_outbound_destination_all_params.
        _service.enable_retries()
        self.test_get_allowed_outbound_destination_all_params()

        # Disable retries and run test_get_allowed_outbound_destination_all_params.
        _service.disable_retries()
        self.test_get_allowed_outbound_destination_all_params()

    @responses.activate
    def test_get_allowed_outbound_destination_required_params(self):
        """
        test_get_allowed_outbound_destination_required_params()
        """
        # Set up mock
        url = preprocess_url(
            '/projects/15314cc3-85b4-4338-903f-c28cdee6d005/allowed_outbound_destinations/my-allowed-outbound-destination'
        )
        mock_response = '{"entity_tag": "2385407409", "type": "cidr_block", "cidr_block": "cidr_block", "name": "name"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-allowed-outbound-destination'

        # Invoke method
        response = _service.get_allowed_outbound_destination(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_allowed_outbound_destination_required_params_with_retries(self):
        # Enable retries and run test_get_allowed_outbound_destination_required_params.
        _service.enable_retries()
        self.test_get_allowed_outbound_destination_required_params()

        # Disable retries and run test_get_allowed_outbound_destination_required_params.
        _service.disable_retries()
        self.test_get_allowed_outbound_destination_required_params()

    @responses.activate
    def test_get_allowed_outbound_destination_value_error(self):
        """
        test_get_allowed_outbound_destination_value_error()
        """
        # Set up mock
        url = preprocess_url(
            '/projects/15314cc3-85b4-4338-903f-c28cdee6d005/allowed_outbound_destinations/my-allowed-outbound-destination'
        )
        mock_response = '{"entity_tag": "2385407409", "type": "cidr_block", "cidr_block": "cidr_block", "name": "name"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-allowed-outbound-destination'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_allowed_outbound_destination(**req_copy)

    def test_get_allowed_outbound_destination_value_error_with_retries(self):
        # Enable retries and run test_get_allowed_outbound_destination_value_error.
        _service.enable_retries()
        self.test_get_allowed_outbound_destination_value_error()

        # Disable retries and run test_get_allowed_outbound_destination_value_error.
        _service.disable_retries()
        self.test_get_allowed_outbound_destination_value_error()


class TestDeleteAllowedOutboundDestination:
    """
    Test Class for delete_allowed_outbound_destination
    """

    @responses.activate
    def test_delete_allowed_outbound_destination_all_params(self):
        """
        delete_allowed_outbound_destination()
        """
        # Set up mock
        url = preprocess_url(
            '/projects/15314cc3-85b4-4338-903f-c28cdee6d005/allowed_outbound_destinations/my-allowed-outbound-destination'
        )
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-allowed-outbound-destination'

        # Invoke method
        response = _service.delete_allowed_outbound_destination(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_allowed_outbound_destination_all_params_with_retries(self):
        # Enable retries and run test_delete_allowed_outbound_destination_all_params.
        _service.enable_retries()
        self.test_delete_allowed_outbound_destination_all_params()

        # Disable retries and run test_delete_allowed_outbound_destination_all_params.
        _service.disable_retries()
        self.test_delete_allowed_outbound_destination_all_params()

    @responses.activate
    def test_delete_allowed_outbound_destination_required_params(self):
        """
        test_delete_allowed_outbound_destination_required_params()
        """
        # Set up mock
        url = preprocess_url(
            '/projects/15314cc3-85b4-4338-903f-c28cdee6d005/allowed_outbound_destinations/my-allowed-outbound-destination'
        )
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-allowed-outbound-destination'

        # Invoke method
        response = _service.delete_allowed_outbound_destination(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_allowed_outbound_destination_required_params_with_retries(self):
        # Enable retries and run test_delete_allowed_outbound_destination_required_params.
        _service.enable_retries()
        self.test_delete_allowed_outbound_destination_required_params()

        # Disable retries and run test_delete_allowed_outbound_destination_required_params.
        _service.disable_retries()
        self.test_delete_allowed_outbound_destination_required_params()

    @responses.activate
    def test_delete_allowed_outbound_destination_value_error(self):
        """
        test_delete_allowed_outbound_destination_value_error()
        """
        # Set up mock
        url = preprocess_url(
            '/projects/15314cc3-85b4-4338-903f-c28cdee6d005/allowed_outbound_destinations/my-allowed-outbound-destination'
        )
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-allowed-outbound-destination'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_allowed_outbound_destination(**req_copy)

    def test_delete_allowed_outbound_destination_value_error_with_retries(self):
        # Enable retries and run test_delete_allowed_outbound_destination_value_error.
        _service.enable_retries()
        self.test_delete_allowed_outbound_destination_value_error()

        # Disable retries and run test_delete_allowed_outbound_destination_value_error.
        _service.disable_retries()
        self.test_delete_allowed_outbound_destination_value_error()


class TestUpdateAllowedOutboundDestination:
    """
    Test Class for update_allowed_outbound_destination
    """

    @responses.activate
    def test_update_allowed_outbound_destination_all_params(self):
        """
        update_allowed_outbound_destination()
        """
        # Set up mock
        url = preprocess_url(
            '/projects/15314cc3-85b4-4338-903f-c28cdee6d005/allowed_outbound_destinations/my-allowed-outbound-destination'
        )
        mock_response = '{"entity_tag": "2385407409", "type": "cidr_block", "cidr_block": "cidr_block", "name": "name"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a AllowedOutboundDestinationPatchCidrBlockDataPatch model
        allowed_outbound_destination_patch_model = {}
        allowed_outbound_destination_patch_model['type'] = 'cidr_block'
        allowed_outbound_destination_patch_model['cidr_block'] = 'testString'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-allowed-outbound-destination'
        if_match = 'testString'
        allowed_outbound_destination = allowed_outbound_destination_patch_model

        # Invoke method
        response = _service.update_allowed_outbound_destination(
            project_id,
            name,
            if_match,
            allowed_outbound_destination,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == allowed_outbound_destination

    def test_update_allowed_outbound_destination_all_params_with_retries(self):
        # Enable retries and run test_update_allowed_outbound_destination_all_params.
        _service.enable_retries()
        self.test_update_allowed_outbound_destination_all_params()

        # Disable retries and run test_update_allowed_outbound_destination_all_params.
        _service.disable_retries()
        self.test_update_allowed_outbound_destination_all_params()

    @responses.activate
    def test_update_allowed_outbound_destination_required_params(self):
        """
        test_update_allowed_outbound_destination_required_params()
        """
        # Set up mock
        url = preprocess_url(
            '/projects/15314cc3-85b4-4338-903f-c28cdee6d005/allowed_outbound_destinations/my-allowed-outbound-destination'
        )
        mock_response = '{"entity_tag": "2385407409", "type": "cidr_block", "cidr_block": "cidr_block", "name": "name"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a AllowedOutboundDestinationPatchCidrBlockDataPatch model
        allowed_outbound_destination_patch_model = {}
        allowed_outbound_destination_patch_model['type'] = 'cidr_block'
        allowed_outbound_destination_patch_model['cidr_block'] = 'testString'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-allowed-outbound-destination'
        if_match = 'testString'
        allowed_outbound_destination = allowed_outbound_destination_patch_model

        # Invoke method
        response = _service.update_allowed_outbound_destination(
            project_id,
            name,
            if_match,
            allowed_outbound_destination,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == allowed_outbound_destination

    def test_update_allowed_outbound_destination_required_params_with_retries(self):
        # Enable retries and run test_update_allowed_outbound_destination_required_params.
        _service.enable_retries()
        self.test_update_allowed_outbound_destination_required_params()

        # Disable retries and run test_update_allowed_outbound_destination_required_params.
        _service.disable_retries()
        self.test_update_allowed_outbound_destination_required_params()

    @responses.activate
    def test_update_allowed_outbound_destination_value_error(self):
        """
        test_update_allowed_outbound_destination_value_error()
        """
        # Set up mock
        url = preprocess_url(
            '/projects/15314cc3-85b4-4338-903f-c28cdee6d005/allowed_outbound_destinations/my-allowed-outbound-destination'
        )
        mock_response = '{"entity_tag": "2385407409", "type": "cidr_block", "cidr_block": "cidr_block", "name": "name"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a AllowedOutboundDestinationPatchCidrBlockDataPatch model
        allowed_outbound_destination_patch_model = {}
        allowed_outbound_destination_patch_model['type'] = 'cidr_block'
        allowed_outbound_destination_patch_model['cidr_block'] = 'testString'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-allowed-outbound-destination'
        if_match = 'testString'
        allowed_outbound_destination = allowed_outbound_destination_patch_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
            "if_match": if_match,
            "allowed_outbound_destination": allowed_outbound_destination,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_allowed_outbound_destination(**req_copy)

    def test_update_allowed_outbound_destination_value_error_with_retries(self):
        # Enable retries and run test_update_allowed_outbound_destination_value_error.
        _service.enable_retries()
        self.test_update_allowed_outbound_destination_value_error()

        # Disable retries and run test_update_allowed_outbound_destination_value_error.
        _service.disable_retries()
        self.test_update_allowed_outbound_destination_value_error()


class TestGetProjectEgressIps:
    """
    Test Class for get_project_egress_ips
    """

    @responses.activate
    def test_get_project_egress_ips_all_params(self):
        """
        get_project_egress_ips()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/egress_ips')
        mock_response = '{"private": ["private"], "public": ["public"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.get_project_egress_ips(
            project_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_project_egress_ips_all_params_with_retries(self):
        # Enable retries and run test_get_project_egress_ips_all_params.
        _service.enable_retries()
        self.test_get_project_egress_ips_all_params()

        # Disable retries and run test_get_project_egress_ips_all_params.
        _service.disable_retries()
        self.test_get_project_egress_ips_all_params()

    @responses.activate
    def test_get_project_egress_ips_value_error(self):
        """
        test_get_project_egress_ips_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/egress_ips')
        mock_response = '{"private": ["private"], "public": ["public"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_project_egress_ips(**req_copy)

    def test_get_project_egress_ips_value_error_with_retries(self):
        # Enable retries and run test_get_project_egress_ips_value_error.
        _service.enable_retries()
        self.test_get_project_egress_ips_value_error()

        # Disable retries and run test_get_project_egress_ips_value_error.
        _service.disable_retries()
        self.test_get_project_egress_ips_value_error()


class TestGetProjectStatusDetails:
    """
    Test Class for get_project_status_details
    """

    @responses.activate
    def test_get_project_status_details_all_params(self):
        """
        get_project_status_details()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/status_details')
        mock_response = '{"domain": "unknown", "project": "enabled", "vpe_not_enabled": false}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.get_project_status_details(
            project_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_project_status_details_all_params_with_retries(self):
        # Enable retries and run test_get_project_status_details_all_params.
        _service.enable_retries()
        self.test_get_project_status_details_all_params()

        # Disable retries and run test_get_project_status_details_all_params.
        _service.disable_retries()
        self.test_get_project_status_details_all_params()

    @responses.activate
    def test_get_project_status_details_value_error(self):
        """
        test_get_project_status_details_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/status_details')
        mock_response = '{"domain": "unknown", "project": "enabled", "vpe_not_enabled": false}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_project_status_details(**req_copy)

    def test_get_project_status_details_value_error_with_retries(self):
        # Enable retries and run test_get_project_status_details_value_error.
        _service.enable_retries()
        self.test_get_project_status_details_value_error()

        # Disable retries and run test_get_project_status_details_value_error.
        _service.disable_retries()
        self.test_get_project_status_details_value_error()


# endregion
##############################################################################
# End of Service: Projects
##############################################################################

##############################################################################
# Start of Service: Applications
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = CodeEngineV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CodeEngineV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CodeEngineV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListApps:
    """
    Test Class for list_apps
    """

    @responses.activate
    def test_list_apps_all_params(self):
        """
        list_apps()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps')
        mock_response = '{"apps": [{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "probe_liveness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "probe_readiness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_apps(
            project_id,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_apps_all_params_with_retries(self):
        # Enable retries and run test_list_apps_all_params.
        _service.enable_retries()
        self.test_list_apps_all_params()

        # Disable retries and run test_list_apps_all_params.
        _service.disable_retries()
        self.test_list_apps_all_params()

    @responses.activate
    def test_list_apps_required_params(self):
        """
        test_list_apps_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps')
        mock_response = '{"apps": [{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "probe_liveness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "probe_readiness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.list_apps(
            project_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_apps_required_params_with_retries(self):
        # Enable retries and run test_list_apps_required_params.
        _service.enable_retries()
        self.test_list_apps_required_params()

        # Disable retries and run test_list_apps_required_params.
        _service.disable_retries()
        self.test_list_apps_required_params()

    @responses.activate
    def test_list_apps_value_error(self):
        """
        test_list_apps_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps')
        mock_response = '{"apps": [{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "probe_liveness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "probe_readiness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_apps(**req_copy)

    def test_list_apps_value_error_with_retries(self):
        # Enable retries and run test_list_apps_value_error.
        _service.enable_retries()
        self.test_list_apps_value_error()

        # Disable retries and run test_list_apps_value_error.
        _service.disable_retries()
        self.test_list_apps_value_error()

    @responses.activate
    def test_list_apps_with_pager_get_next(self):
        """
        test_list_apps_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"apps":[{"build":"my-build","build_run":"my-build-run","computed_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"created_at":"2022-09-13T11:41:35+02:00","endpoint":"https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud","endpoint_internal":"http://my-app.vg67hzldruk.svc.cluster.local","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_port":8080,"image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","managed_domain_mappings":"local_public","name":"my-app","probe_liveness":{"failure_threshold":5,"initial_delay":5,"interval":5,"path":"path","port":8080,"timeout":300,"type":"tcp"},"probe_readiness":{"failure_threshold":5,"initial_delay":5,"interval":5,"path":"path","port":8080,"timeout":300,"type":"tcp"},"project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"app_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_concurrency":100,"scale_concurrency_target":80,"scale_cpu_limit":"1","scale_down_delay":300,"scale_ephemeral_storage_limit":"4G","scale_initial_instances":1,"scale_max_instances":10,"scale_memory_limit":"4G","scale_min_instances":1,"scale_request_timeout":300,"status":"ready","status_details":{"latest_created_revision":"my-app-00001","latest_ready_revision":"my-app-00001","reason":"ready"}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"apps":[{"build":"my-build","build_run":"my-build-run","computed_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"created_at":"2022-09-13T11:41:35+02:00","endpoint":"https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud","endpoint_internal":"http://my-app.vg67hzldruk.svc.cluster.local","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_port":8080,"image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","managed_domain_mappings":"local_public","name":"my-app","probe_liveness":{"failure_threshold":5,"initial_delay":5,"interval":5,"path":"path","port":8080,"timeout":300,"type":"tcp"},"probe_readiness":{"failure_threshold":5,"initial_delay":5,"interval":5,"path":"path","port":8080,"timeout":300,"type":"tcp"},"project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"app_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_concurrency":100,"scale_concurrency_target":80,"scale_cpu_limit":"1","scale_down_delay":300,"scale_ephemeral_storage_limit":"4G","scale_initial_instances":1,"scale_max_instances":10,"scale_memory_limit":"4G","scale_min_instances":1,"scale_request_timeout":300,"status":"ready","status_details":{"latest_created_revision":"my-app-00001","latest_ready_revision":"my-app-00001","reason":"ready"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = AppsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_apps_with_pager_get_all(self):
        """
        test_list_apps_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"apps":[{"build":"my-build","build_run":"my-build-run","computed_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"created_at":"2022-09-13T11:41:35+02:00","endpoint":"https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud","endpoint_internal":"http://my-app.vg67hzldruk.svc.cluster.local","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_port":8080,"image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","managed_domain_mappings":"local_public","name":"my-app","probe_liveness":{"failure_threshold":5,"initial_delay":5,"interval":5,"path":"path","port":8080,"timeout":300,"type":"tcp"},"probe_readiness":{"failure_threshold":5,"initial_delay":5,"interval":5,"path":"path","port":8080,"timeout":300,"type":"tcp"},"project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"app_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_concurrency":100,"scale_concurrency_target":80,"scale_cpu_limit":"1","scale_down_delay":300,"scale_ephemeral_storage_limit":"4G","scale_initial_instances":1,"scale_max_instances":10,"scale_memory_limit":"4G","scale_min_instances":1,"scale_request_timeout":300,"status":"ready","status_details":{"latest_created_revision":"my-app-00001","latest_ready_revision":"my-app-00001","reason":"ready"}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"apps":[{"build":"my-build","build_run":"my-build-run","computed_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"created_at":"2022-09-13T11:41:35+02:00","endpoint":"https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud","endpoint_internal":"http://my-app.vg67hzldruk.svc.cluster.local","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_port":8080,"image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","managed_domain_mappings":"local_public","name":"my-app","probe_liveness":{"failure_threshold":5,"initial_delay":5,"interval":5,"path":"path","port":8080,"timeout":300,"type":"tcp"},"probe_readiness":{"failure_threshold":5,"initial_delay":5,"interval":5,"path":"path","port":8080,"timeout":300,"type":"tcp"},"project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"app_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_concurrency":100,"scale_concurrency_target":80,"scale_cpu_limit":"1","scale_down_delay":300,"scale_ephemeral_storage_limit":"4G","scale_initial_instances":1,"scale_max_instances":10,"scale_memory_limit":"4G","scale_min_instances":1,"scale_request_timeout":300,"status":"ready","status_details":{"latest_created_revision":"my-app-00001","latest_ready_revision":"my-app-00001","reason":"ready"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = AppsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            limit=100,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateApp:
    """
    Test Class for create_app
    """

    @responses.activate
    def test_create_app_all_params(self):
        """
        create_app()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps')
        mock_response = '{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "probe_liveness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "probe_readiness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProbePrototype model
        probe_prototype_model = {}
        probe_prototype_model['failure_threshold'] = 5
        probe_prototype_model['initial_delay'] = 5
        probe_prototype_model['interval'] = 5
        probe_prototype_model['path'] = 'testString'
        probe_prototype_model['port'] = 8080
        probe_prototype_model['timeout'] = 300
        probe_prototype_model['type'] = 'tcp'

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Construct a dict representation of a VolumeMountPrototype model
        volume_mount_prototype_model = {}
        volume_mount_prototype_model['mount_path'] = '/app'
        volume_mount_prototype_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_prototype_model['reference'] = 'my-secret'
        volume_mount_prototype_model['type'] = 'secret'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        image_reference = 'icr.io/codeengine/helloworld'
        name = 'my-app'
        image_port = 8080
        image_secret = 'my-secret'
        managed_domain_mappings = 'local_public'
        probe_liveness = probe_prototype_model
        probe_readiness = probe_prototype_model
        run_arguments = ['testString']
        run_as_user = 1001
        run_commands = ['testString']
        run_env_variables = [env_var_prototype_model]
        run_service_account = 'default'
        run_volume_mounts = [volume_mount_prototype_model]
        scale_concurrency = 100
        scale_concurrency_target = 80
        scale_cpu_limit = '1'
        scale_down_delay = 300
        scale_ephemeral_storage_limit = '4G'
        scale_initial_instances = 1
        scale_max_instances = 10
        scale_memory_limit = '4G'
        scale_min_instances = 1
        scale_request_timeout = 300

        # Invoke method
        response = _service.create_app(
            project_id,
            image_reference,
            name,
            image_port=image_port,
            image_secret=image_secret,
            managed_domain_mappings=managed_domain_mappings,
            probe_liveness=probe_liveness,
            probe_readiness=probe_readiness,
            run_arguments=run_arguments,
            run_as_user=run_as_user,
            run_commands=run_commands,
            run_env_variables=run_env_variables,
            run_service_account=run_service_account,
            run_volume_mounts=run_volume_mounts,
            scale_concurrency=scale_concurrency,
            scale_concurrency_target=scale_concurrency_target,
            scale_cpu_limit=scale_cpu_limit,
            scale_down_delay=scale_down_delay,
            scale_ephemeral_storage_limit=scale_ephemeral_storage_limit,
            scale_initial_instances=scale_initial_instances,
            scale_max_instances=scale_max_instances,
            scale_memory_limit=scale_memory_limit,
            scale_min_instances=scale_min_instances,
            scale_request_timeout=scale_request_timeout,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['image_reference'] == 'icr.io/codeengine/helloworld'
        assert req_body['name'] == 'my-app'
        assert req_body['image_port'] == 8080
        assert req_body['image_secret'] == 'my-secret'
        assert req_body['managed_domain_mappings'] == 'local_public'
        assert req_body['probe_liveness'] == probe_prototype_model
        assert req_body['probe_readiness'] == probe_prototype_model
        assert req_body['run_arguments'] == ['testString']
        assert req_body['run_as_user'] == 1001
        assert req_body['run_commands'] == ['testString']
        assert req_body['run_env_variables'] == [env_var_prototype_model]
        assert req_body['run_service_account'] == 'default'
        assert req_body['run_volume_mounts'] == [volume_mount_prototype_model]
        assert req_body['scale_concurrency'] == 100
        assert req_body['scale_concurrency_target'] == 80
        assert req_body['scale_cpu_limit'] == '1'
        assert req_body['scale_down_delay'] == 300
        assert req_body['scale_ephemeral_storage_limit'] == '4G'
        assert req_body['scale_initial_instances'] == 1
        assert req_body['scale_max_instances'] == 10
        assert req_body['scale_memory_limit'] == '4G'
        assert req_body['scale_min_instances'] == 1
        assert req_body['scale_request_timeout'] == 300

    def test_create_app_all_params_with_retries(self):
        # Enable retries and run test_create_app_all_params.
        _service.enable_retries()
        self.test_create_app_all_params()

        # Disable retries and run test_create_app_all_params.
        _service.disable_retries()
        self.test_create_app_all_params()

    @responses.activate
    def test_create_app_required_params(self):
        """
        test_create_app_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps')
        mock_response = '{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "probe_liveness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "probe_readiness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProbePrototype model
        probe_prototype_model = {}
        probe_prototype_model['failure_threshold'] = 5
        probe_prototype_model['initial_delay'] = 5
        probe_prototype_model['interval'] = 5
        probe_prototype_model['path'] = 'testString'
        probe_prototype_model['port'] = 8080
        probe_prototype_model['timeout'] = 300
        probe_prototype_model['type'] = 'tcp'

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Construct a dict representation of a VolumeMountPrototype model
        volume_mount_prototype_model = {}
        volume_mount_prototype_model['mount_path'] = '/app'
        volume_mount_prototype_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_prototype_model['reference'] = 'my-secret'
        volume_mount_prototype_model['type'] = 'secret'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        image_reference = 'icr.io/codeengine/helloworld'
        name = 'my-app'
        image_port = 8080
        image_secret = 'my-secret'
        managed_domain_mappings = 'local_public'
        probe_liveness = probe_prototype_model
        probe_readiness = probe_prototype_model
        run_arguments = ['testString']
        run_as_user = 1001
        run_commands = ['testString']
        run_env_variables = [env_var_prototype_model]
        run_service_account = 'default'
        run_volume_mounts = [volume_mount_prototype_model]
        scale_concurrency = 100
        scale_concurrency_target = 80
        scale_cpu_limit = '1'
        scale_down_delay = 300
        scale_ephemeral_storage_limit = '4G'
        scale_initial_instances = 1
        scale_max_instances = 10
        scale_memory_limit = '4G'
        scale_min_instances = 1
        scale_request_timeout = 300

        # Invoke method
        response = _service.create_app(
            project_id,
            image_reference,
            name,
            image_port=image_port,
            image_secret=image_secret,
            managed_domain_mappings=managed_domain_mappings,
            probe_liveness=probe_liveness,
            probe_readiness=probe_readiness,
            run_arguments=run_arguments,
            run_as_user=run_as_user,
            run_commands=run_commands,
            run_env_variables=run_env_variables,
            run_service_account=run_service_account,
            run_volume_mounts=run_volume_mounts,
            scale_concurrency=scale_concurrency,
            scale_concurrency_target=scale_concurrency_target,
            scale_cpu_limit=scale_cpu_limit,
            scale_down_delay=scale_down_delay,
            scale_ephemeral_storage_limit=scale_ephemeral_storage_limit,
            scale_initial_instances=scale_initial_instances,
            scale_max_instances=scale_max_instances,
            scale_memory_limit=scale_memory_limit,
            scale_min_instances=scale_min_instances,
            scale_request_timeout=scale_request_timeout,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['image_reference'] == 'icr.io/codeengine/helloworld'
        assert req_body['name'] == 'my-app'
        assert req_body['image_port'] == 8080
        assert req_body['image_secret'] == 'my-secret'
        assert req_body['managed_domain_mappings'] == 'local_public'
        assert req_body['probe_liveness'] == probe_prototype_model
        assert req_body['probe_readiness'] == probe_prototype_model
        assert req_body['run_arguments'] == ['testString']
        assert req_body['run_as_user'] == 1001
        assert req_body['run_commands'] == ['testString']
        assert req_body['run_env_variables'] == [env_var_prototype_model]
        assert req_body['run_service_account'] == 'default'
        assert req_body['run_volume_mounts'] == [volume_mount_prototype_model]
        assert req_body['scale_concurrency'] == 100
        assert req_body['scale_concurrency_target'] == 80
        assert req_body['scale_cpu_limit'] == '1'
        assert req_body['scale_down_delay'] == 300
        assert req_body['scale_ephemeral_storage_limit'] == '4G'
        assert req_body['scale_initial_instances'] == 1
        assert req_body['scale_max_instances'] == 10
        assert req_body['scale_memory_limit'] == '4G'
        assert req_body['scale_min_instances'] == 1
        assert req_body['scale_request_timeout'] == 300

    def test_create_app_required_params_with_retries(self):
        # Enable retries and run test_create_app_required_params.
        _service.enable_retries()
        self.test_create_app_required_params()

        # Disable retries and run test_create_app_required_params.
        _service.disable_retries()
        self.test_create_app_required_params()

    @responses.activate
    def test_create_app_value_error(self):
        """
        test_create_app_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps')
        mock_response = '{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "probe_liveness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "probe_readiness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProbePrototype model
        probe_prototype_model = {}
        probe_prototype_model['failure_threshold'] = 5
        probe_prototype_model['initial_delay'] = 5
        probe_prototype_model['interval'] = 5
        probe_prototype_model['path'] = 'testString'
        probe_prototype_model['port'] = 8080
        probe_prototype_model['timeout'] = 300
        probe_prototype_model['type'] = 'tcp'

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Construct a dict representation of a VolumeMountPrototype model
        volume_mount_prototype_model = {}
        volume_mount_prototype_model['mount_path'] = '/app'
        volume_mount_prototype_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_prototype_model['reference'] = 'my-secret'
        volume_mount_prototype_model['type'] = 'secret'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        image_reference = 'icr.io/codeengine/helloworld'
        name = 'my-app'
        image_port = 8080
        image_secret = 'my-secret'
        managed_domain_mappings = 'local_public'
        probe_liveness = probe_prototype_model
        probe_readiness = probe_prototype_model
        run_arguments = ['testString']
        run_as_user = 1001
        run_commands = ['testString']
        run_env_variables = [env_var_prototype_model]
        run_service_account = 'default'
        run_volume_mounts = [volume_mount_prototype_model]
        scale_concurrency = 100
        scale_concurrency_target = 80
        scale_cpu_limit = '1'
        scale_down_delay = 300
        scale_ephemeral_storage_limit = '4G'
        scale_initial_instances = 1
        scale_max_instances = 10
        scale_memory_limit = '4G'
        scale_min_instances = 1
        scale_request_timeout = 300

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "image_reference": image_reference,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_app(**req_copy)

    def test_create_app_value_error_with_retries(self):
        # Enable retries and run test_create_app_value_error.
        _service.enable_retries()
        self.test_create_app_value_error()

        # Disable retries and run test_create_app_value_error.
        _service.disable_retries()
        self.test_create_app_value_error()


class TestGetApp:
    """
    Test Class for get_app
    """

    @responses.activate
    def test_get_app_all_params(self):
        """
        get_app()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app')
        mock_response = '{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "probe_liveness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "probe_readiness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-app'

        # Invoke method
        response = _service.get_app(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_app_all_params_with_retries(self):
        # Enable retries and run test_get_app_all_params.
        _service.enable_retries()
        self.test_get_app_all_params()

        # Disable retries and run test_get_app_all_params.
        _service.disable_retries()
        self.test_get_app_all_params()

    @responses.activate
    def test_get_app_required_params(self):
        """
        test_get_app_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app')
        mock_response = '{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "probe_liveness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "probe_readiness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-app'

        # Invoke method
        response = _service.get_app(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_app_required_params_with_retries(self):
        # Enable retries and run test_get_app_required_params.
        _service.enable_retries()
        self.test_get_app_required_params()

        # Disable retries and run test_get_app_required_params.
        _service.disable_retries()
        self.test_get_app_required_params()

    @responses.activate
    def test_get_app_value_error(self):
        """
        test_get_app_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app')
        mock_response = '{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "probe_liveness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "probe_readiness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-app'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_app(**req_copy)

    def test_get_app_value_error_with_retries(self):
        # Enable retries and run test_get_app_value_error.
        _service.enable_retries()
        self.test_get_app_value_error()

        # Disable retries and run test_get_app_value_error.
        _service.disable_retries()
        self.test_get_app_value_error()


class TestDeleteApp:
    """
    Test Class for delete_app
    """

    @responses.activate
    def test_delete_app_all_params(self):
        """
        delete_app()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-app'

        # Invoke method
        response = _service.delete_app(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_app_all_params_with_retries(self):
        # Enable retries and run test_delete_app_all_params.
        _service.enable_retries()
        self.test_delete_app_all_params()

        # Disable retries and run test_delete_app_all_params.
        _service.disable_retries()
        self.test_delete_app_all_params()

    @responses.activate
    def test_delete_app_required_params(self):
        """
        test_delete_app_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-app'

        # Invoke method
        response = _service.delete_app(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_app_required_params_with_retries(self):
        # Enable retries and run test_delete_app_required_params.
        _service.enable_retries()
        self.test_delete_app_required_params()

        # Disable retries and run test_delete_app_required_params.
        _service.disable_retries()
        self.test_delete_app_required_params()

    @responses.activate
    def test_delete_app_value_error(self):
        """
        test_delete_app_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-app'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_app(**req_copy)

    def test_delete_app_value_error_with_retries(self):
        # Enable retries and run test_delete_app_value_error.
        _service.enable_retries()
        self.test_delete_app_value_error()

        # Disable retries and run test_delete_app_value_error.
        _service.disable_retries()
        self.test_delete_app_value_error()


class TestUpdateApp:
    """
    Test Class for update_app
    """

    @responses.activate
    def test_update_app_all_params(self):
        """
        update_app()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app')
        mock_response = '{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "probe_liveness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "probe_readiness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProbePrototype model
        probe_prototype_model = {}
        probe_prototype_model['failure_threshold'] = 5
        probe_prototype_model['initial_delay'] = 5
        probe_prototype_model['interval'] = 5
        probe_prototype_model['path'] = 'testString'
        probe_prototype_model['port'] = 8080
        probe_prototype_model['timeout'] = 300
        probe_prototype_model['type'] = 'tcp'

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Construct a dict representation of a VolumeMountPrototype model
        volume_mount_prototype_model = {}
        volume_mount_prototype_model['mount_path'] = '/app'
        volume_mount_prototype_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_prototype_model['reference'] = 'my-secret'
        volume_mount_prototype_model['type'] = 'secret'

        # Construct a dict representation of a AppPatch model
        app_patch_model = {}
        app_patch_model['image_port'] = 8080
        app_patch_model['image_reference'] = 'icr.io/codeengine/helloworld'
        app_patch_model['image_secret'] = 'my-secret'
        app_patch_model['managed_domain_mappings'] = 'local_public'
        app_patch_model['probe_liveness'] = probe_prototype_model
        app_patch_model['probe_readiness'] = probe_prototype_model
        app_patch_model['run_arguments'] = ['testString']
        app_patch_model['run_as_user'] = 1001
        app_patch_model['run_commands'] = ['testString']
        app_patch_model['run_env_variables'] = [env_var_prototype_model]
        app_patch_model['run_service_account'] = 'default'
        app_patch_model['run_volume_mounts'] = [volume_mount_prototype_model]
        app_patch_model['scale_concurrency'] = 100
        app_patch_model['scale_concurrency_target'] = 80
        app_patch_model['scale_cpu_limit'] = '1'
        app_patch_model['scale_down_delay'] = 300
        app_patch_model['scale_ephemeral_storage_limit'] = '4G'
        app_patch_model['scale_initial_instances'] = 1
        app_patch_model['scale_max_instances'] = 10
        app_patch_model['scale_memory_limit'] = '4G'
        app_patch_model['scale_min_instances'] = 1
        app_patch_model['scale_request_timeout'] = 300

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-app'
        if_match = 'testString'
        app = app_patch_model

        # Invoke method
        response = _service.update_app(
            project_id,
            name,
            if_match,
            app,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == app

    def test_update_app_all_params_with_retries(self):
        # Enable retries and run test_update_app_all_params.
        _service.enable_retries()
        self.test_update_app_all_params()

        # Disable retries and run test_update_app_all_params.
        _service.disable_retries()
        self.test_update_app_all_params()

    @responses.activate
    def test_update_app_required_params(self):
        """
        test_update_app_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app')
        mock_response = '{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "probe_liveness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "probe_readiness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProbePrototype model
        probe_prototype_model = {}
        probe_prototype_model['failure_threshold'] = 5
        probe_prototype_model['initial_delay'] = 5
        probe_prototype_model['interval'] = 5
        probe_prototype_model['path'] = 'testString'
        probe_prototype_model['port'] = 8080
        probe_prototype_model['timeout'] = 300
        probe_prototype_model['type'] = 'tcp'

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Construct a dict representation of a VolumeMountPrototype model
        volume_mount_prototype_model = {}
        volume_mount_prototype_model['mount_path'] = '/app'
        volume_mount_prototype_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_prototype_model['reference'] = 'my-secret'
        volume_mount_prototype_model['type'] = 'secret'

        # Construct a dict representation of a AppPatch model
        app_patch_model = {}
        app_patch_model['image_port'] = 8080
        app_patch_model['image_reference'] = 'icr.io/codeengine/helloworld'
        app_patch_model['image_secret'] = 'my-secret'
        app_patch_model['managed_domain_mappings'] = 'local_public'
        app_patch_model['probe_liveness'] = probe_prototype_model
        app_patch_model['probe_readiness'] = probe_prototype_model
        app_patch_model['run_arguments'] = ['testString']
        app_patch_model['run_as_user'] = 1001
        app_patch_model['run_commands'] = ['testString']
        app_patch_model['run_env_variables'] = [env_var_prototype_model]
        app_patch_model['run_service_account'] = 'default'
        app_patch_model['run_volume_mounts'] = [volume_mount_prototype_model]
        app_patch_model['scale_concurrency'] = 100
        app_patch_model['scale_concurrency_target'] = 80
        app_patch_model['scale_cpu_limit'] = '1'
        app_patch_model['scale_down_delay'] = 300
        app_patch_model['scale_ephemeral_storage_limit'] = '4G'
        app_patch_model['scale_initial_instances'] = 1
        app_patch_model['scale_max_instances'] = 10
        app_patch_model['scale_memory_limit'] = '4G'
        app_patch_model['scale_min_instances'] = 1
        app_patch_model['scale_request_timeout'] = 300

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-app'
        if_match = 'testString'
        app = app_patch_model

        # Invoke method
        response = _service.update_app(
            project_id,
            name,
            if_match,
            app,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == app

    def test_update_app_required_params_with_retries(self):
        # Enable retries and run test_update_app_required_params.
        _service.enable_retries()
        self.test_update_app_required_params()

        # Disable retries and run test_update_app_required_params.
        _service.disable_retries()
        self.test_update_app_required_params()

    @responses.activate
    def test_update_app_value_error(self):
        """
        test_update_app_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app')
        mock_response = '{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "probe_liveness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "probe_readiness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProbePrototype model
        probe_prototype_model = {}
        probe_prototype_model['failure_threshold'] = 5
        probe_prototype_model['initial_delay'] = 5
        probe_prototype_model['interval'] = 5
        probe_prototype_model['path'] = 'testString'
        probe_prototype_model['port'] = 8080
        probe_prototype_model['timeout'] = 300
        probe_prototype_model['type'] = 'tcp'

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Construct a dict representation of a VolumeMountPrototype model
        volume_mount_prototype_model = {}
        volume_mount_prototype_model['mount_path'] = '/app'
        volume_mount_prototype_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_prototype_model['reference'] = 'my-secret'
        volume_mount_prototype_model['type'] = 'secret'

        # Construct a dict representation of a AppPatch model
        app_patch_model = {}
        app_patch_model['image_port'] = 8080
        app_patch_model['image_reference'] = 'icr.io/codeengine/helloworld'
        app_patch_model['image_secret'] = 'my-secret'
        app_patch_model['managed_domain_mappings'] = 'local_public'
        app_patch_model['probe_liveness'] = probe_prototype_model
        app_patch_model['probe_readiness'] = probe_prototype_model
        app_patch_model['run_arguments'] = ['testString']
        app_patch_model['run_as_user'] = 1001
        app_patch_model['run_commands'] = ['testString']
        app_patch_model['run_env_variables'] = [env_var_prototype_model]
        app_patch_model['run_service_account'] = 'default'
        app_patch_model['run_volume_mounts'] = [volume_mount_prototype_model]
        app_patch_model['scale_concurrency'] = 100
        app_patch_model['scale_concurrency_target'] = 80
        app_patch_model['scale_cpu_limit'] = '1'
        app_patch_model['scale_down_delay'] = 300
        app_patch_model['scale_ephemeral_storage_limit'] = '4G'
        app_patch_model['scale_initial_instances'] = 1
        app_patch_model['scale_max_instances'] = 10
        app_patch_model['scale_memory_limit'] = '4G'
        app_patch_model['scale_min_instances'] = 1
        app_patch_model['scale_request_timeout'] = 300

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-app'
        if_match = 'testString'
        app = app_patch_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
            "if_match": if_match,
            "app": app,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_app(**req_copy)

    def test_update_app_value_error_with_retries(self):
        # Enable retries and run test_update_app_value_error.
        _service.enable_retries()
        self.test_update_app_value_error()

        # Disable retries and run test_update_app_value_error.
        _service.disable_retries()
        self.test_update_app_value_error()


class TestListAppRevisions:
    """
    Test Class for list_app_revisions
    """

    @responses.activate
    def test_list_app_revisions_all_params(self):
        """
        list_app_revisions()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app/revisions')
        mock_response = '{"first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}, "revisions": [{"app_name": "my-app", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/revisions/my-app-00001", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-app-00001", "probe_liveness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "probe_readiness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_revision_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"actual_instances": 1, "reason": "ready"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        app_name = 'my-app'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_app_revisions(
            project_id,
            app_name,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_app_revisions_all_params_with_retries(self):
        # Enable retries and run test_list_app_revisions_all_params.
        _service.enable_retries()
        self.test_list_app_revisions_all_params()

        # Disable retries and run test_list_app_revisions_all_params.
        _service.disable_retries()
        self.test_list_app_revisions_all_params()

    @responses.activate
    def test_list_app_revisions_required_params(self):
        """
        test_list_app_revisions_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app/revisions')
        mock_response = '{"first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}, "revisions": [{"app_name": "my-app", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/revisions/my-app-00001", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-app-00001", "probe_liveness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "probe_readiness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_revision_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"actual_instances": 1, "reason": "ready"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        app_name = 'my-app'

        # Invoke method
        response = _service.list_app_revisions(
            project_id,
            app_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_app_revisions_required_params_with_retries(self):
        # Enable retries and run test_list_app_revisions_required_params.
        _service.enable_retries()
        self.test_list_app_revisions_required_params()

        # Disable retries and run test_list_app_revisions_required_params.
        _service.disable_retries()
        self.test_list_app_revisions_required_params()

    @responses.activate
    def test_list_app_revisions_value_error(self):
        """
        test_list_app_revisions_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app/revisions')
        mock_response = '{"first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}, "revisions": [{"app_name": "my-app", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/revisions/my-app-00001", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-app-00001", "probe_liveness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "probe_readiness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_revision_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"actual_instances": 1, "reason": "ready"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        app_name = 'my-app'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "app_name": app_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_app_revisions(**req_copy)

    def test_list_app_revisions_value_error_with_retries(self):
        # Enable retries and run test_list_app_revisions_value_error.
        _service.enable_retries()
        self.test_list_app_revisions_value_error()

        # Disable retries and run test_list_app_revisions_value_error.
        _service.disable_retries()
        self.test_list_app_revisions_value_error()

    @responses.activate
    def test_list_app_revisions_with_pager_get_next(self):
        """
        test_list_app_revisions_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app/revisions')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"revisions":[{"app_name":"my-app","computed_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/revisions/my-app-00001","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_port":8080,"image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","name":"my-app-00001","probe_liveness":{"failure_threshold":5,"initial_delay":5,"interval":5,"path":"path","port":8080,"timeout":300,"type":"tcp"},"probe_readiness":{"failure_threshold":5,"initial_delay":5,"interval":5,"path":"path","port":8080,"timeout":300,"type":"tcp"},"project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"app_revision_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_concurrency":100,"scale_concurrency_target":80,"scale_cpu_limit":"1","scale_down_delay":300,"scale_ephemeral_storage_limit":"4G","scale_initial_instances":1,"scale_max_instances":10,"scale_memory_limit":"4G","scale_min_instances":1,"scale_request_timeout":300,"status":"ready","status_details":{"actual_instances":1,"reason":"ready"}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"revisions":[{"app_name":"my-app","computed_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/revisions/my-app-00001","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_port":8080,"image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","name":"my-app-00001","probe_liveness":{"failure_threshold":5,"initial_delay":5,"interval":5,"path":"path","port":8080,"timeout":300,"type":"tcp"},"probe_readiness":{"failure_threshold":5,"initial_delay":5,"interval":5,"path":"path","port":8080,"timeout":300,"type":"tcp"},"project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"app_revision_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_concurrency":100,"scale_concurrency_target":80,"scale_cpu_limit":"1","scale_down_delay":300,"scale_ephemeral_storage_limit":"4G","scale_initial_instances":1,"scale_max_instances":10,"scale_memory_limit":"4G","scale_min_instances":1,"scale_request_timeout":300,"status":"ready","status_details":{"actual_instances":1,"reason":"ready"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = AppRevisionsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            app_name='my-app',
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_app_revisions_with_pager_get_all(self):
        """
        test_list_app_revisions_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app/revisions')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"revisions":[{"app_name":"my-app","computed_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/revisions/my-app-00001","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_port":8080,"image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","name":"my-app-00001","probe_liveness":{"failure_threshold":5,"initial_delay":5,"interval":5,"path":"path","port":8080,"timeout":300,"type":"tcp"},"probe_readiness":{"failure_threshold":5,"initial_delay":5,"interval":5,"path":"path","port":8080,"timeout":300,"type":"tcp"},"project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"app_revision_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_concurrency":100,"scale_concurrency_target":80,"scale_cpu_limit":"1","scale_down_delay":300,"scale_ephemeral_storage_limit":"4G","scale_initial_instances":1,"scale_max_instances":10,"scale_memory_limit":"4G","scale_min_instances":1,"scale_request_timeout":300,"status":"ready","status_details":{"actual_instances":1,"reason":"ready"}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"revisions":[{"app_name":"my-app","computed_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/revisions/my-app-00001","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_port":8080,"image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","name":"my-app-00001","probe_liveness":{"failure_threshold":5,"initial_delay":5,"interval":5,"path":"path","port":8080,"timeout":300,"type":"tcp"},"probe_readiness":{"failure_threshold":5,"initial_delay":5,"interval":5,"path":"path","port":8080,"timeout":300,"type":"tcp"},"project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"app_revision_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_concurrency":100,"scale_concurrency_target":80,"scale_cpu_limit":"1","scale_down_delay":300,"scale_ephemeral_storage_limit":"4G","scale_initial_instances":1,"scale_max_instances":10,"scale_memory_limit":"4G","scale_min_instances":1,"scale_request_timeout":300,"status":"ready","status_details":{"actual_instances":1,"reason":"ready"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = AppRevisionsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            app_name='my-app',
            limit=100,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetAppRevision:
    """
    Test Class for get_app_revision
    """

    @responses.activate
    def test_get_app_revision_all_params(self):
        """
        get_app_revision()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app/revisions/my-app-00001')
        mock_response = '{"app_name": "my-app", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/revisions/my-app-00001", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-app-00001", "probe_liveness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "probe_readiness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_revision_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"actual_instances": 1, "reason": "ready"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        app_name = 'my-app'
        name = 'my-app-00001'

        # Invoke method
        response = _service.get_app_revision(
            project_id,
            app_name,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_app_revision_all_params_with_retries(self):
        # Enable retries and run test_get_app_revision_all_params.
        _service.enable_retries()
        self.test_get_app_revision_all_params()

        # Disable retries and run test_get_app_revision_all_params.
        _service.disable_retries()
        self.test_get_app_revision_all_params()

    @responses.activate
    def test_get_app_revision_required_params(self):
        """
        test_get_app_revision_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app/revisions/my-app-00001')
        mock_response = '{"app_name": "my-app", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/revisions/my-app-00001", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-app-00001", "probe_liveness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "probe_readiness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_revision_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"actual_instances": 1, "reason": "ready"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        app_name = 'my-app'
        name = 'my-app-00001'

        # Invoke method
        response = _service.get_app_revision(
            project_id,
            app_name,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_app_revision_required_params_with_retries(self):
        # Enable retries and run test_get_app_revision_required_params.
        _service.enable_retries()
        self.test_get_app_revision_required_params()

        # Disable retries and run test_get_app_revision_required_params.
        _service.disable_retries()
        self.test_get_app_revision_required_params()

    @responses.activate
    def test_get_app_revision_value_error(self):
        """
        test_get_app_revision_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app/revisions/my-app-00001')
        mock_response = '{"app_name": "my-app", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/revisions/my-app-00001", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-app-00001", "probe_liveness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "probe_readiness": {"failure_threshold": 5, "initial_delay": 5, "interval": 5, "path": "path", "port": 8080, "timeout": 300, "type": "tcp"}, "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_revision_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"actual_instances": 1, "reason": "ready"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        app_name = 'my-app'
        name = 'my-app-00001'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "app_name": app_name,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_app_revision(**req_copy)

    def test_get_app_revision_value_error_with_retries(self):
        # Enable retries and run test_get_app_revision_value_error.
        _service.enable_retries()
        self.test_get_app_revision_value_error()

        # Disable retries and run test_get_app_revision_value_error.
        _service.disable_retries()
        self.test_get_app_revision_value_error()


class TestDeleteAppRevision:
    """
    Test Class for delete_app_revision
    """

    @responses.activate
    def test_delete_app_revision_all_params(self):
        """
        delete_app_revision()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app/revisions/my-app-00001')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        app_name = 'my-app'
        name = 'my-app-00001'

        # Invoke method
        response = _service.delete_app_revision(
            project_id,
            app_name,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_app_revision_all_params_with_retries(self):
        # Enable retries and run test_delete_app_revision_all_params.
        _service.enable_retries()
        self.test_delete_app_revision_all_params()

        # Disable retries and run test_delete_app_revision_all_params.
        _service.disable_retries()
        self.test_delete_app_revision_all_params()

    @responses.activate
    def test_delete_app_revision_value_error(self):
        """
        test_delete_app_revision_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app/revisions/my-app-00001')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        app_name = 'my-app'
        name = 'my-app-00001'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "app_name": app_name,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_app_revision(**req_copy)

    def test_delete_app_revision_value_error_with_retries(self):
        # Enable retries and run test_delete_app_revision_value_error.
        _service.enable_retries()
        self.test_delete_app_revision_value_error()

        # Disable retries and run test_delete_app_revision_value_error.
        _service.disable_retries()
        self.test_delete_app_revision_value_error()


class TestListAppInstances:
    """
    Test Class for list_app_instances
    """

    @responses.activate
    def test_list_app_instances_all_params(self):
        """
        list_app_instances()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app/instances')
        mock_response = '{"first": {"href": "href"}, "instances": [{"app_name": "my-app", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/instances", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-app-00001-deployment-6c9b5cf966-wjs44", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_instance_v2", "restarts": 4, "revision_name": "my-app", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_memory_limit": "4G", "status": "pending", "system_container": {"current_state": {"completed_at": "2022-09-22T17:40:00Z", "container_status": "container_status", "exit_code": 100, "reason": "ready", "started_at": "2022-09-22T17:34:00Z"}, "last_observed_state": {"completed_at": "2022-09-22T17:40:00Z", "container_status": "container_status", "exit_code": 100, "reason": "ready", "started_at": "2022-09-22T17:34:00Z"}}, "user_container": {"current_state": {"completed_at": "2022-09-22T17:40:00Z", "container_status": "container_status", "exit_code": 100, "reason": "ready", "started_at": "2022-09-22T17:34:00Z"}, "last_observed_state": {"completed_at": "2022-09-22T17:40:00Z", "container_status": "container_status", "exit_code": 100, "reason": "ready", "started_at": "2022-09-22T17:34:00Z"}}}], "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        app_name = 'my-app'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_app_instances(
            project_id,
            app_name,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_app_instances_all_params_with_retries(self):
        # Enable retries and run test_list_app_instances_all_params.
        _service.enable_retries()
        self.test_list_app_instances_all_params()

        # Disable retries and run test_list_app_instances_all_params.
        _service.disable_retries()
        self.test_list_app_instances_all_params()

    @responses.activate
    def test_list_app_instances_required_params(self):
        """
        test_list_app_instances_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app/instances')
        mock_response = '{"first": {"href": "href"}, "instances": [{"app_name": "my-app", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/instances", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-app-00001-deployment-6c9b5cf966-wjs44", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_instance_v2", "restarts": 4, "revision_name": "my-app", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_memory_limit": "4G", "status": "pending", "system_container": {"current_state": {"completed_at": "2022-09-22T17:40:00Z", "container_status": "container_status", "exit_code": 100, "reason": "ready", "started_at": "2022-09-22T17:34:00Z"}, "last_observed_state": {"completed_at": "2022-09-22T17:40:00Z", "container_status": "container_status", "exit_code": 100, "reason": "ready", "started_at": "2022-09-22T17:34:00Z"}}, "user_container": {"current_state": {"completed_at": "2022-09-22T17:40:00Z", "container_status": "container_status", "exit_code": 100, "reason": "ready", "started_at": "2022-09-22T17:34:00Z"}, "last_observed_state": {"completed_at": "2022-09-22T17:40:00Z", "container_status": "container_status", "exit_code": 100, "reason": "ready", "started_at": "2022-09-22T17:34:00Z"}}}], "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        app_name = 'my-app'

        # Invoke method
        response = _service.list_app_instances(
            project_id,
            app_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_app_instances_required_params_with_retries(self):
        # Enable retries and run test_list_app_instances_required_params.
        _service.enable_retries()
        self.test_list_app_instances_required_params()

        # Disable retries and run test_list_app_instances_required_params.
        _service.disable_retries()
        self.test_list_app_instances_required_params()

    @responses.activate
    def test_list_app_instances_value_error(self):
        """
        test_list_app_instances_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app/instances')
        mock_response = '{"first": {"href": "href"}, "instances": [{"app_name": "my-app", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/instances", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-app-00001-deployment-6c9b5cf966-wjs44", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "app_instance_v2", "restarts": 4, "revision_name": "my-app", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_memory_limit": "4G", "status": "pending", "system_container": {"current_state": {"completed_at": "2022-09-22T17:40:00Z", "container_status": "container_status", "exit_code": 100, "reason": "ready", "started_at": "2022-09-22T17:34:00Z"}, "last_observed_state": {"completed_at": "2022-09-22T17:40:00Z", "container_status": "container_status", "exit_code": 100, "reason": "ready", "started_at": "2022-09-22T17:34:00Z"}}, "user_container": {"current_state": {"completed_at": "2022-09-22T17:40:00Z", "container_status": "container_status", "exit_code": 100, "reason": "ready", "started_at": "2022-09-22T17:34:00Z"}, "last_observed_state": {"completed_at": "2022-09-22T17:40:00Z", "container_status": "container_status", "exit_code": 100, "reason": "ready", "started_at": "2022-09-22T17:34:00Z"}}}], "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        app_name = 'my-app'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "app_name": app_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_app_instances(**req_copy)

    def test_list_app_instances_value_error_with_retries(self):
        # Enable retries and run test_list_app_instances_value_error.
        _service.enable_retries()
        self.test_list_app_instances_value_error()

        # Disable retries and run test_list_app_instances_value_error.
        _service.disable_retries()
        self.test_list_app_instances_value_error()

    @responses.activate
    def test_list_app_instances_with_pager_get_next(self):
        """
        test_list_app_instances_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app/instances')
        mock_response1 = '{"next":{"start":"1"},"instances":[{"app_name":"my-app","created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/instances","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-app-00001-deployment-6c9b5cf966-wjs44","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"app_instance_v2","restarts":4,"revision_name":"my-app","scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_memory_limit":"4G","status":"pending","system_container":{"current_state":{"completed_at":"2022-09-22T17:40:00Z","container_status":"container_status","exit_code":100,"reason":"ready","started_at":"2022-09-22T17:34:00Z"},"last_observed_state":{"completed_at":"2022-09-22T17:40:00Z","container_status":"container_status","exit_code":100,"reason":"ready","started_at":"2022-09-22T17:34:00Z"}},"user_container":{"current_state":{"completed_at":"2022-09-22T17:40:00Z","container_status":"container_status","exit_code":100,"reason":"ready","started_at":"2022-09-22T17:34:00Z"},"last_observed_state":{"completed_at":"2022-09-22T17:40:00Z","container_status":"container_status","exit_code":100,"reason":"ready","started_at":"2022-09-22T17:34:00Z"}}}],"total_count":2,"limit":1}'
        mock_response2 = '{"instances":[{"app_name":"my-app","created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/instances","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-app-00001-deployment-6c9b5cf966-wjs44","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"app_instance_v2","restarts":4,"revision_name":"my-app","scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_memory_limit":"4G","status":"pending","system_container":{"current_state":{"completed_at":"2022-09-22T17:40:00Z","container_status":"container_status","exit_code":100,"reason":"ready","started_at":"2022-09-22T17:34:00Z"},"last_observed_state":{"completed_at":"2022-09-22T17:40:00Z","container_status":"container_status","exit_code":100,"reason":"ready","started_at":"2022-09-22T17:34:00Z"}},"user_container":{"current_state":{"completed_at":"2022-09-22T17:40:00Z","container_status":"container_status","exit_code":100,"reason":"ready","started_at":"2022-09-22T17:34:00Z"},"last_observed_state":{"completed_at":"2022-09-22T17:40:00Z","container_status":"container_status","exit_code":100,"reason":"ready","started_at":"2022-09-22T17:34:00Z"}}}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = AppInstancesPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            app_name='my-app',
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_app_instances_with_pager_get_all(self):
        """
        test_list_app_instances_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app/instances')
        mock_response1 = '{"next":{"start":"1"},"instances":[{"app_name":"my-app","created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/instances","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-app-00001-deployment-6c9b5cf966-wjs44","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"app_instance_v2","restarts":4,"revision_name":"my-app","scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_memory_limit":"4G","status":"pending","system_container":{"current_state":{"completed_at":"2022-09-22T17:40:00Z","container_status":"container_status","exit_code":100,"reason":"ready","started_at":"2022-09-22T17:34:00Z"},"last_observed_state":{"completed_at":"2022-09-22T17:40:00Z","container_status":"container_status","exit_code":100,"reason":"ready","started_at":"2022-09-22T17:34:00Z"}},"user_container":{"current_state":{"completed_at":"2022-09-22T17:40:00Z","container_status":"container_status","exit_code":100,"reason":"ready","started_at":"2022-09-22T17:34:00Z"},"last_observed_state":{"completed_at":"2022-09-22T17:40:00Z","container_status":"container_status","exit_code":100,"reason":"ready","started_at":"2022-09-22T17:34:00Z"}}}],"total_count":2,"limit":1}'
        mock_response2 = '{"instances":[{"app_name":"my-app","created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/instances","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-app-00001-deployment-6c9b5cf966-wjs44","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"app_instance_v2","restarts":4,"revision_name":"my-app","scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_memory_limit":"4G","status":"pending","system_container":{"current_state":{"completed_at":"2022-09-22T17:40:00Z","container_status":"container_status","exit_code":100,"reason":"ready","started_at":"2022-09-22T17:34:00Z"},"last_observed_state":{"completed_at":"2022-09-22T17:40:00Z","container_status":"container_status","exit_code":100,"reason":"ready","started_at":"2022-09-22T17:34:00Z"}},"user_container":{"current_state":{"completed_at":"2022-09-22T17:40:00Z","container_status":"container_status","exit_code":100,"reason":"ready","started_at":"2022-09-22T17:34:00Z"},"last_observed_state":{"completed_at":"2022-09-22T17:40:00Z","container_status":"container_status","exit_code":100,"reason":"ready","started_at":"2022-09-22T17:34:00Z"}}}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = AppInstancesPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            app_name='my-app',
            limit=100,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


# endregion
##############################################################################
# End of Service: Applications
##############################################################################

##############################################################################
# Start of Service: Jobs
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = CodeEngineV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CodeEngineV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CodeEngineV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListJobs:
    """
    Test Class for list_jobs
    """

    @responses.activate
    def test_list_jobs_all_params(self):
        """
        list_jobs()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs')
        mock_response = '{"first": {"href": "href"}, "jobs": [{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}], "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_jobs(
            project_id,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_jobs_all_params_with_retries(self):
        # Enable retries and run test_list_jobs_all_params.
        _service.enable_retries()
        self.test_list_jobs_all_params()

        # Disable retries and run test_list_jobs_all_params.
        _service.disable_retries()
        self.test_list_jobs_all_params()

    @responses.activate
    def test_list_jobs_required_params(self):
        """
        test_list_jobs_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs')
        mock_response = '{"first": {"href": "href"}, "jobs": [{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}], "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.list_jobs(
            project_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_jobs_required_params_with_retries(self):
        # Enable retries and run test_list_jobs_required_params.
        _service.enable_retries()
        self.test_list_jobs_required_params()

        # Disable retries and run test_list_jobs_required_params.
        _service.disable_retries()
        self.test_list_jobs_required_params()

    @responses.activate
    def test_list_jobs_value_error(self):
        """
        test_list_jobs_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs')
        mock_response = '{"first": {"href": "href"}, "jobs": [{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}], "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_jobs(**req_copy)

    def test_list_jobs_value_error_with_retries(self):
        # Enable retries and run test_list_jobs_value_error.
        _service.enable_retries()
        self.test_list_jobs_value_error()

        # Disable retries and run test_list_jobs_value_error.
        _service.disable_retries()
        self.test_list_jobs_value_error()

    @responses.activate
    def test_list_jobs_with_pager_get_next(self):
        """
        test_list_jobs_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"jobs":[{"build":"my-build","build_run":"my-build-run","computed_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"created_at":"2022-09-13T11:41:35+02:00","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","name":"my-job","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"job_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_mode":"task","run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_array_spec":"1-5,7-8,10","scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_max_execution_time":7200,"scale_memory_limit":"4G","scale_retry_limit":3}],"limit":1}'
        mock_response2 = '{"total_count":2,"jobs":[{"build":"my-build","build_run":"my-build-run","computed_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"created_at":"2022-09-13T11:41:35+02:00","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","name":"my-job","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"job_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_mode":"task","run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_array_spec":"1-5,7-8,10","scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_max_execution_time":7200,"scale_memory_limit":"4G","scale_retry_limit":3}],"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = JobsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_jobs_with_pager_get_all(self):
        """
        test_list_jobs_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"jobs":[{"build":"my-build","build_run":"my-build-run","computed_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"created_at":"2022-09-13T11:41:35+02:00","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","name":"my-job","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"job_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_mode":"task","run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_array_spec":"1-5,7-8,10","scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_max_execution_time":7200,"scale_memory_limit":"4G","scale_retry_limit":3}],"limit":1}'
        mock_response2 = '{"total_count":2,"jobs":[{"build":"my-build","build_run":"my-build-run","computed_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"created_at":"2022-09-13T11:41:35+02:00","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","name":"my-job","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"job_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_mode":"task","run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_array_spec":"1-5,7-8,10","scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_max_execution_time":7200,"scale_memory_limit":"4G","scale_retry_limit":3}],"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = JobsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            limit=100,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateJob:
    """
    Test Class for create_job
    """

    @responses.activate
    def test_create_job_all_params(self):
        """
        create_job()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs')
        mock_response = '{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Construct a dict representation of a VolumeMountPrototype model
        volume_mount_prototype_model = {}
        volume_mount_prototype_model['mount_path'] = '/app'
        volume_mount_prototype_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_prototype_model['reference'] = 'my-secret'
        volume_mount_prototype_model['type'] = 'secret'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        image_reference = 'icr.io/codeengine/helloworld'
        name = 'my-job'
        image_secret = 'my-secret'
        run_arguments = ['testString']
        run_as_user = 1001
        run_commands = ['testString']
        run_env_variables = [env_var_prototype_model]
        run_mode = 'task'
        run_service_account = 'default'
        run_volume_mounts = [volume_mount_prototype_model]
        scale_array_spec = '1-5,7-8,10'
        scale_cpu_limit = '1'
        scale_ephemeral_storage_limit = '4G'
        scale_max_execution_time = 7200
        scale_memory_limit = '4G'
        scale_retry_limit = 3

        # Invoke method
        response = _service.create_job(
            project_id,
            image_reference,
            name,
            image_secret=image_secret,
            run_arguments=run_arguments,
            run_as_user=run_as_user,
            run_commands=run_commands,
            run_env_variables=run_env_variables,
            run_mode=run_mode,
            run_service_account=run_service_account,
            run_volume_mounts=run_volume_mounts,
            scale_array_spec=scale_array_spec,
            scale_cpu_limit=scale_cpu_limit,
            scale_ephemeral_storage_limit=scale_ephemeral_storage_limit,
            scale_max_execution_time=scale_max_execution_time,
            scale_memory_limit=scale_memory_limit,
            scale_retry_limit=scale_retry_limit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['image_reference'] == 'icr.io/codeengine/helloworld'
        assert req_body['name'] == 'my-job'
        assert req_body['image_secret'] == 'my-secret'
        assert req_body['run_arguments'] == ['testString']
        assert req_body['run_as_user'] == 1001
        assert req_body['run_commands'] == ['testString']
        assert req_body['run_env_variables'] == [env_var_prototype_model]
        assert req_body['run_mode'] == 'task'
        assert req_body['run_service_account'] == 'default'
        assert req_body['run_volume_mounts'] == [volume_mount_prototype_model]
        assert req_body['scale_array_spec'] == '1-5,7-8,10'
        assert req_body['scale_cpu_limit'] == '1'
        assert req_body['scale_ephemeral_storage_limit'] == '4G'
        assert req_body['scale_max_execution_time'] == 7200
        assert req_body['scale_memory_limit'] == '4G'
        assert req_body['scale_retry_limit'] == 3

    def test_create_job_all_params_with_retries(self):
        # Enable retries and run test_create_job_all_params.
        _service.enable_retries()
        self.test_create_job_all_params()

        # Disable retries and run test_create_job_all_params.
        _service.disable_retries()
        self.test_create_job_all_params()

    @responses.activate
    def test_create_job_required_params(self):
        """
        test_create_job_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs')
        mock_response = '{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Construct a dict representation of a VolumeMountPrototype model
        volume_mount_prototype_model = {}
        volume_mount_prototype_model['mount_path'] = '/app'
        volume_mount_prototype_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_prototype_model['reference'] = 'my-secret'
        volume_mount_prototype_model['type'] = 'secret'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        image_reference = 'icr.io/codeengine/helloworld'
        name = 'my-job'
        image_secret = 'my-secret'
        run_arguments = ['testString']
        run_as_user = 1001
        run_commands = ['testString']
        run_env_variables = [env_var_prototype_model]
        run_mode = 'task'
        run_service_account = 'default'
        run_volume_mounts = [volume_mount_prototype_model]
        scale_array_spec = '1-5,7-8,10'
        scale_cpu_limit = '1'
        scale_ephemeral_storage_limit = '4G'
        scale_max_execution_time = 7200
        scale_memory_limit = '4G'
        scale_retry_limit = 3

        # Invoke method
        response = _service.create_job(
            project_id,
            image_reference,
            name,
            image_secret=image_secret,
            run_arguments=run_arguments,
            run_as_user=run_as_user,
            run_commands=run_commands,
            run_env_variables=run_env_variables,
            run_mode=run_mode,
            run_service_account=run_service_account,
            run_volume_mounts=run_volume_mounts,
            scale_array_spec=scale_array_spec,
            scale_cpu_limit=scale_cpu_limit,
            scale_ephemeral_storage_limit=scale_ephemeral_storage_limit,
            scale_max_execution_time=scale_max_execution_time,
            scale_memory_limit=scale_memory_limit,
            scale_retry_limit=scale_retry_limit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['image_reference'] == 'icr.io/codeengine/helloworld'
        assert req_body['name'] == 'my-job'
        assert req_body['image_secret'] == 'my-secret'
        assert req_body['run_arguments'] == ['testString']
        assert req_body['run_as_user'] == 1001
        assert req_body['run_commands'] == ['testString']
        assert req_body['run_env_variables'] == [env_var_prototype_model]
        assert req_body['run_mode'] == 'task'
        assert req_body['run_service_account'] == 'default'
        assert req_body['run_volume_mounts'] == [volume_mount_prototype_model]
        assert req_body['scale_array_spec'] == '1-5,7-8,10'
        assert req_body['scale_cpu_limit'] == '1'
        assert req_body['scale_ephemeral_storage_limit'] == '4G'
        assert req_body['scale_max_execution_time'] == 7200
        assert req_body['scale_memory_limit'] == '4G'
        assert req_body['scale_retry_limit'] == 3

    def test_create_job_required_params_with_retries(self):
        # Enable retries and run test_create_job_required_params.
        _service.enable_retries()
        self.test_create_job_required_params()

        # Disable retries and run test_create_job_required_params.
        _service.disable_retries()
        self.test_create_job_required_params()

    @responses.activate
    def test_create_job_value_error(self):
        """
        test_create_job_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs')
        mock_response = '{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Construct a dict representation of a VolumeMountPrototype model
        volume_mount_prototype_model = {}
        volume_mount_prototype_model['mount_path'] = '/app'
        volume_mount_prototype_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_prototype_model['reference'] = 'my-secret'
        volume_mount_prototype_model['type'] = 'secret'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        image_reference = 'icr.io/codeengine/helloworld'
        name = 'my-job'
        image_secret = 'my-secret'
        run_arguments = ['testString']
        run_as_user = 1001
        run_commands = ['testString']
        run_env_variables = [env_var_prototype_model]
        run_mode = 'task'
        run_service_account = 'default'
        run_volume_mounts = [volume_mount_prototype_model]
        scale_array_spec = '1-5,7-8,10'
        scale_cpu_limit = '1'
        scale_ephemeral_storage_limit = '4G'
        scale_max_execution_time = 7200
        scale_memory_limit = '4G'
        scale_retry_limit = 3

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "image_reference": image_reference,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_job(**req_copy)

    def test_create_job_value_error_with_retries(self):
        # Enable retries and run test_create_job_value_error.
        _service.enable_retries()
        self.test_create_job_value_error()

        # Disable retries and run test_create_job_value_error.
        _service.disable_retries()
        self.test_create_job_value_error()


class TestGetJob:
    """
    Test Class for get_job
    """

    @responses.activate
    def test_get_job_all_params(self):
        """
        get_job()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs/my-job')
        mock_response = '{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-job'

        # Invoke method
        response = _service.get_job(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_job_all_params_with_retries(self):
        # Enable retries and run test_get_job_all_params.
        _service.enable_retries()
        self.test_get_job_all_params()

        # Disable retries and run test_get_job_all_params.
        _service.disable_retries()
        self.test_get_job_all_params()

    @responses.activate
    def test_get_job_required_params(self):
        """
        test_get_job_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs/my-job')
        mock_response = '{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-job'

        # Invoke method
        response = _service.get_job(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_job_required_params_with_retries(self):
        # Enable retries and run test_get_job_required_params.
        _service.enable_retries()
        self.test_get_job_required_params()

        # Disable retries and run test_get_job_required_params.
        _service.disable_retries()
        self.test_get_job_required_params()

    @responses.activate
    def test_get_job_value_error(self):
        """
        test_get_job_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs/my-job')
        mock_response = '{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-job'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_job(**req_copy)

    def test_get_job_value_error_with_retries(self):
        # Enable retries and run test_get_job_value_error.
        _service.enable_retries()
        self.test_get_job_value_error()

        # Disable retries and run test_get_job_value_error.
        _service.disable_retries()
        self.test_get_job_value_error()


class TestDeleteJob:
    """
    Test Class for delete_job
    """

    @responses.activate
    def test_delete_job_all_params(self):
        """
        delete_job()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs/my-job')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-job'

        # Invoke method
        response = _service.delete_job(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_job_all_params_with_retries(self):
        # Enable retries and run test_delete_job_all_params.
        _service.enable_retries()
        self.test_delete_job_all_params()

        # Disable retries and run test_delete_job_all_params.
        _service.disable_retries()
        self.test_delete_job_all_params()

    @responses.activate
    def test_delete_job_required_params(self):
        """
        test_delete_job_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs/my-job')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-job'

        # Invoke method
        response = _service.delete_job(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_job_required_params_with_retries(self):
        # Enable retries and run test_delete_job_required_params.
        _service.enable_retries()
        self.test_delete_job_required_params()

        # Disable retries and run test_delete_job_required_params.
        _service.disable_retries()
        self.test_delete_job_required_params()

    @responses.activate
    def test_delete_job_value_error(self):
        """
        test_delete_job_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs/my-job')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-job'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_job(**req_copy)

    def test_delete_job_value_error_with_retries(self):
        # Enable retries and run test_delete_job_value_error.
        _service.enable_retries()
        self.test_delete_job_value_error()

        # Disable retries and run test_delete_job_value_error.
        _service.disable_retries()
        self.test_delete_job_value_error()


class TestUpdateJob:
    """
    Test Class for update_job
    """

    @responses.activate
    def test_update_job_all_params(self):
        """
        update_job()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs/my-job')
        mock_response = '{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Construct a dict representation of a VolumeMountPrototype model
        volume_mount_prototype_model = {}
        volume_mount_prototype_model['mount_path'] = '/app'
        volume_mount_prototype_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_prototype_model['reference'] = 'my-secret'
        volume_mount_prototype_model['type'] = 'secret'

        # Construct a dict representation of a JobPatch model
        job_patch_model = {}
        job_patch_model['image_reference'] = 'icr.io/codeengine/helloworld'
        job_patch_model['image_secret'] = 'my-secret'
        job_patch_model['run_arguments'] = ['testString']
        job_patch_model['run_as_user'] = 1001
        job_patch_model['run_commands'] = ['testString']
        job_patch_model['run_env_variables'] = [env_var_prototype_model]
        job_patch_model['run_mode'] = 'task'
        job_patch_model['run_service_account'] = 'default'
        job_patch_model['run_volume_mounts'] = [volume_mount_prototype_model]
        job_patch_model['scale_array_spec'] = '1-5,7-8,10'
        job_patch_model['scale_cpu_limit'] = '1'
        job_patch_model['scale_ephemeral_storage_limit'] = '4G'
        job_patch_model['scale_max_execution_time'] = 7200
        job_patch_model['scale_memory_limit'] = '4G'
        job_patch_model['scale_retry_limit'] = 3

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-job'
        if_match = 'testString'
        job = job_patch_model

        # Invoke method
        response = _service.update_job(
            project_id,
            name,
            if_match,
            job,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == job

    def test_update_job_all_params_with_retries(self):
        # Enable retries and run test_update_job_all_params.
        _service.enable_retries()
        self.test_update_job_all_params()

        # Disable retries and run test_update_job_all_params.
        _service.disable_retries()
        self.test_update_job_all_params()

    @responses.activate
    def test_update_job_required_params(self):
        """
        test_update_job_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs/my-job')
        mock_response = '{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Construct a dict representation of a VolumeMountPrototype model
        volume_mount_prototype_model = {}
        volume_mount_prototype_model['mount_path'] = '/app'
        volume_mount_prototype_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_prototype_model['reference'] = 'my-secret'
        volume_mount_prototype_model['type'] = 'secret'

        # Construct a dict representation of a JobPatch model
        job_patch_model = {}
        job_patch_model['image_reference'] = 'icr.io/codeengine/helloworld'
        job_patch_model['image_secret'] = 'my-secret'
        job_patch_model['run_arguments'] = ['testString']
        job_patch_model['run_as_user'] = 1001
        job_patch_model['run_commands'] = ['testString']
        job_patch_model['run_env_variables'] = [env_var_prototype_model]
        job_patch_model['run_mode'] = 'task'
        job_patch_model['run_service_account'] = 'default'
        job_patch_model['run_volume_mounts'] = [volume_mount_prototype_model]
        job_patch_model['scale_array_spec'] = '1-5,7-8,10'
        job_patch_model['scale_cpu_limit'] = '1'
        job_patch_model['scale_ephemeral_storage_limit'] = '4G'
        job_patch_model['scale_max_execution_time'] = 7200
        job_patch_model['scale_memory_limit'] = '4G'
        job_patch_model['scale_retry_limit'] = 3

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-job'
        if_match = 'testString'
        job = job_patch_model

        # Invoke method
        response = _service.update_job(
            project_id,
            name,
            if_match,
            job,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == job

    def test_update_job_required_params_with_retries(self):
        # Enable retries and run test_update_job_required_params.
        _service.enable_retries()
        self.test_update_job_required_params()

        # Disable retries and run test_update_job_required_params.
        _service.disable_retries()
        self.test_update_job_required_params()

    @responses.activate
    def test_update_job_value_error(self):
        """
        test_update_job_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs/my-job')
        mock_response = '{"build": "my-build", "build_run": "my-build-run", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Construct a dict representation of a VolumeMountPrototype model
        volume_mount_prototype_model = {}
        volume_mount_prototype_model['mount_path'] = '/app'
        volume_mount_prototype_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_prototype_model['reference'] = 'my-secret'
        volume_mount_prototype_model['type'] = 'secret'

        # Construct a dict representation of a JobPatch model
        job_patch_model = {}
        job_patch_model['image_reference'] = 'icr.io/codeengine/helloworld'
        job_patch_model['image_secret'] = 'my-secret'
        job_patch_model['run_arguments'] = ['testString']
        job_patch_model['run_as_user'] = 1001
        job_patch_model['run_commands'] = ['testString']
        job_patch_model['run_env_variables'] = [env_var_prototype_model]
        job_patch_model['run_mode'] = 'task'
        job_patch_model['run_service_account'] = 'default'
        job_patch_model['run_volume_mounts'] = [volume_mount_prototype_model]
        job_patch_model['scale_array_spec'] = '1-5,7-8,10'
        job_patch_model['scale_cpu_limit'] = '1'
        job_patch_model['scale_ephemeral_storage_limit'] = '4G'
        job_patch_model['scale_max_execution_time'] = 7200
        job_patch_model['scale_memory_limit'] = '4G'
        job_patch_model['scale_retry_limit'] = 3

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-job'
        if_match = 'testString'
        job = job_patch_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
            "if_match": if_match,
            "job": job,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_job(**req_copy)

    def test_update_job_value_error_with_retries(self):
        # Enable retries and run test_update_job_value_error.
        _service.enable_retries()
        self.test_update_job_value_error()

        # Disable retries and run test_update_job_value_error.
        _service.disable_retries()
        self.test_update_job_value_error()


class TestListJobRuns:
    """
    Test Class for list_job_runs
    """

    @responses.activate
    def test_list_job_runs_all_params(self):
        """
        list_job_runs()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/job_runs')
        mock_response = '{"first": {"href": "href"}, "job_runs": [{"computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "job_name": "my-job", "name": "my-job-run", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_run_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_size_variable_override": 2, "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3, "status": "failed", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "failed": 0, "failed_indices": "1,5", "pending": 0, "pending_indices": "9,12-15", "requested": 0, "running": 0, "running_indices": "10-11", "start_time": "2022-09-22T17:34:00Z", "succeeded": 1, "succeeded_indices": "2-4,6-8", "unknown": 0}}], "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        job_name = 'my-job'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_job_runs(
            project_id,
            job_name=job_name,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'job_name={}'.format(job_name) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_job_runs_all_params_with_retries(self):
        # Enable retries and run test_list_job_runs_all_params.
        _service.enable_retries()
        self.test_list_job_runs_all_params()

        # Disable retries and run test_list_job_runs_all_params.
        _service.disable_retries()
        self.test_list_job_runs_all_params()

    @responses.activate
    def test_list_job_runs_required_params(self):
        """
        test_list_job_runs_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/job_runs')
        mock_response = '{"first": {"href": "href"}, "job_runs": [{"computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "job_name": "my-job", "name": "my-job-run", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_run_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_size_variable_override": 2, "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3, "status": "failed", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "failed": 0, "failed_indices": "1,5", "pending": 0, "pending_indices": "9,12-15", "requested": 0, "running": 0, "running_indices": "10-11", "start_time": "2022-09-22T17:34:00Z", "succeeded": 1, "succeeded_indices": "2-4,6-8", "unknown": 0}}], "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.list_job_runs(
            project_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_job_runs_required_params_with_retries(self):
        # Enable retries and run test_list_job_runs_required_params.
        _service.enable_retries()
        self.test_list_job_runs_required_params()

        # Disable retries and run test_list_job_runs_required_params.
        _service.disable_retries()
        self.test_list_job_runs_required_params()

    @responses.activate
    def test_list_job_runs_value_error(self):
        """
        test_list_job_runs_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/job_runs')
        mock_response = '{"first": {"href": "href"}, "job_runs": [{"computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "job_name": "my-job", "name": "my-job-run", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_run_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_size_variable_override": 2, "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3, "status": "failed", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "failed": 0, "failed_indices": "1,5", "pending": 0, "pending_indices": "9,12-15", "requested": 0, "running": 0, "running_indices": "10-11", "start_time": "2022-09-22T17:34:00Z", "succeeded": 1, "succeeded_indices": "2-4,6-8", "unknown": 0}}], "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_job_runs(**req_copy)

    def test_list_job_runs_value_error_with_retries(self):
        # Enable retries and run test_list_job_runs_value_error.
        _service.enable_retries()
        self.test_list_job_runs_value_error()

        # Disable retries and run test_list_job_runs_value_error.
        _service.disable_retries()
        self.test_list_job_runs_value_error()

    @responses.activate
    def test_list_job_runs_with_pager_get_next(self):
        """
        test_list_job_runs_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/job_runs')
        mock_response1 = '{"next":{"start":"1"},"job_runs":[{"computed_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","job_name":"my-job","name":"my-job-run","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"job_run_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_mode":"task","run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_array_size_variable_override":2,"scale_array_spec":"1-5,7-8,10","scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_max_execution_time":7200,"scale_memory_limit":"4G","scale_retry_limit":3,"status":"failed","status_details":{"completion_time":"2022-09-22T17:40:00Z","failed":0,"failed_indices":"1,5","pending":0,"pending_indices":"9,12-15","requested":0,"running":0,"running_indices":"10-11","start_time":"2022-09-22T17:34:00Z","succeeded":1,"succeeded_indices":"2-4,6-8","unknown":0}}],"total_count":2,"limit":1}'
        mock_response2 = '{"job_runs":[{"computed_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","job_name":"my-job","name":"my-job-run","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"job_run_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_mode":"task","run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_array_size_variable_override":2,"scale_array_spec":"1-5,7-8,10","scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_max_execution_time":7200,"scale_memory_limit":"4G","scale_retry_limit":3,"status":"failed","status_details":{"completion_time":"2022-09-22T17:40:00Z","failed":0,"failed_indices":"1,5","pending":0,"pending_indices":"9,12-15","requested":0,"running":0,"running_indices":"10-11","start_time":"2022-09-22T17:34:00Z","succeeded":1,"succeeded_indices":"2-4,6-8","unknown":0}}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = JobRunsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            job_name='my-job',
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_job_runs_with_pager_get_all(self):
        """
        test_list_job_runs_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/job_runs')
        mock_response1 = '{"next":{"start":"1"},"job_runs":[{"computed_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","job_name":"my-job","name":"my-job-run","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"job_run_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_mode":"task","run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_array_size_variable_override":2,"scale_array_spec":"1-5,7-8,10","scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_max_execution_time":7200,"scale_memory_limit":"4G","scale_retry_limit":3,"status":"failed","status_details":{"completion_time":"2022-09-22T17:40:00Z","failed":0,"failed_indices":"1,5","pending":0,"pending_indices":"9,12-15","requested":0,"running":0,"running_indices":"10-11","start_time":"2022-09-22T17:34:00Z","succeeded":1,"succeeded_indices":"2-4,6-8","unknown":0}}],"total_count":2,"limit":1}'
        mock_response2 = '{"job_runs":[{"computed_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","job_name":"my-job","name":"my-job-run","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"job_run_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_mode":"task","run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_array_size_variable_override":2,"scale_array_spec":"1-5,7-8,10","scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_max_execution_time":7200,"scale_memory_limit":"4G","scale_retry_limit":3,"status":"failed","status_details":{"completion_time":"2022-09-22T17:40:00Z","failed":0,"failed_indices":"1,5","pending":0,"pending_indices":"9,12-15","requested":0,"running":0,"running_indices":"10-11","start_time":"2022-09-22T17:34:00Z","succeeded":1,"succeeded_indices":"2-4,6-8","unknown":0}}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = JobRunsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            job_name='my-job',
            limit=100,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateJobRun:
    """
    Test Class for create_job_run
    """

    @responses.activate
    def test_create_job_run_all_params(self):
        """
        create_job_run()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/job_runs')
        mock_response = '{"computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "job_name": "my-job", "name": "my-job-run", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_run_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_size_variable_override": 2, "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3, "status": "failed", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "failed": 0, "failed_indices": "1,5", "pending": 0, "pending_indices": "9,12-15", "requested": 0, "running": 0, "running_indices": "10-11", "start_time": "2022-09-22T17:34:00Z", "succeeded": 1, "succeeded_indices": "2-4,6-8", "unknown": 0}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Construct a dict representation of a VolumeMountPrototype model
        volume_mount_prototype_model = {}
        volume_mount_prototype_model['mount_path'] = '/app'
        volume_mount_prototype_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_prototype_model['reference'] = 'my-secret'
        volume_mount_prototype_model['type'] = 'secret'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        image_reference = 'icr.io/codeengine/helloworld'
        image_secret = 'my-secret'
        job_name = 'my-job'
        name = 'my-job-run'
        run_arguments = ['testString']
        run_as_user = 1001
        run_commands = ['testString']
        run_env_variables = [env_var_prototype_model]
        run_mode = 'task'
        run_service_account = 'default'
        run_volume_mounts = [volume_mount_prototype_model]
        scale_array_size_variable_override = 2
        scale_array_spec = '1-5,7-8,10'
        scale_cpu_limit = '1'
        scale_ephemeral_storage_limit = '4G'
        scale_max_execution_time = 7200
        scale_memory_limit = '4G'
        scale_retry_limit = 3

        # Invoke method
        response = _service.create_job_run(
            project_id,
            image_reference=image_reference,
            image_secret=image_secret,
            job_name=job_name,
            name=name,
            run_arguments=run_arguments,
            run_as_user=run_as_user,
            run_commands=run_commands,
            run_env_variables=run_env_variables,
            run_mode=run_mode,
            run_service_account=run_service_account,
            run_volume_mounts=run_volume_mounts,
            scale_array_size_variable_override=scale_array_size_variable_override,
            scale_array_spec=scale_array_spec,
            scale_cpu_limit=scale_cpu_limit,
            scale_ephemeral_storage_limit=scale_ephemeral_storage_limit,
            scale_max_execution_time=scale_max_execution_time,
            scale_memory_limit=scale_memory_limit,
            scale_retry_limit=scale_retry_limit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['image_reference'] == 'icr.io/codeengine/helloworld'
        assert req_body['image_secret'] == 'my-secret'
        assert req_body['job_name'] == 'my-job'
        assert req_body['name'] == 'my-job-run'
        assert req_body['run_arguments'] == ['testString']
        assert req_body['run_as_user'] == 1001
        assert req_body['run_commands'] == ['testString']
        assert req_body['run_env_variables'] == [env_var_prototype_model]
        assert req_body['run_mode'] == 'task'
        assert req_body['run_service_account'] == 'default'
        assert req_body['run_volume_mounts'] == [volume_mount_prototype_model]
        assert req_body['scale_array_size_variable_override'] == 2
        assert req_body['scale_array_spec'] == '1-5,7-8,10'
        assert req_body['scale_cpu_limit'] == '1'
        assert req_body['scale_ephemeral_storage_limit'] == '4G'
        assert req_body['scale_max_execution_time'] == 7200
        assert req_body['scale_memory_limit'] == '4G'
        assert req_body['scale_retry_limit'] == 3

    def test_create_job_run_all_params_with_retries(self):
        # Enable retries and run test_create_job_run_all_params.
        _service.enable_retries()
        self.test_create_job_run_all_params()

        # Disable retries and run test_create_job_run_all_params.
        _service.disable_retries()
        self.test_create_job_run_all_params()

    @responses.activate
    def test_create_job_run_required_params(self):
        """
        test_create_job_run_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/job_runs')
        mock_response = '{"computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "job_name": "my-job", "name": "my-job-run", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_run_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_size_variable_override": 2, "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3, "status": "failed", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "failed": 0, "failed_indices": "1,5", "pending": 0, "pending_indices": "9,12-15", "requested": 0, "running": 0, "running_indices": "10-11", "start_time": "2022-09-22T17:34:00Z", "succeeded": 1, "succeeded_indices": "2-4,6-8", "unknown": 0}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Construct a dict representation of a VolumeMountPrototype model
        volume_mount_prototype_model = {}
        volume_mount_prototype_model['mount_path'] = '/app'
        volume_mount_prototype_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_prototype_model['reference'] = 'my-secret'
        volume_mount_prototype_model['type'] = 'secret'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        image_reference = 'icr.io/codeengine/helloworld'
        image_secret = 'my-secret'
        job_name = 'my-job'
        name = 'my-job-run'
        run_arguments = ['testString']
        run_as_user = 1001
        run_commands = ['testString']
        run_env_variables = [env_var_prototype_model]
        run_mode = 'task'
        run_service_account = 'default'
        run_volume_mounts = [volume_mount_prototype_model]
        scale_array_size_variable_override = 2
        scale_array_spec = '1-5,7-8,10'
        scale_cpu_limit = '1'
        scale_ephemeral_storage_limit = '4G'
        scale_max_execution_time = 7200
        scale_memory_limit = '4G'
        scale_retry_limit = 3

        # Invoke method
        response = _service.create_job_run(
            project_id,
            image_reference=image_reference,
            image_secret=image_secret,
            job_name=job_name,
            name=name,
            run_arguments=run_arguments,
            run_as_user=run_as_user,
            run_commands=run_commands,
            run_env_variables=run_env_variables,
            run_mode=run_mode,
            run_service_account=run_service_account,
            run_volume_mounts=run_volume_mounts,
            scale_array_size_variable_override=scale_array_size_variable_override,
            scale_array_spec=scale_array_spec,
            scale_cpu_limit=scale_cpu_limit,
            scale_ephemeral_storage_limit=scale_ephemeral_storage_limit,
            scale_max_execution_time=scale_max_execution_time,
            scale_memory_limit=scale_memory_limit,
            scale_retry_limit=scale_retry_limit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['image_reference'] == 'icr.io/codeengine/helloworld'
        assert req_body['image_secret'] == 'my-secret'
        assert req_body['job_name'] == 'my-job'
        assert req_body['name'] == 'my-job-run'
        assert req_body['run_arguments'] == ['testString']
        assert req_body['run_as_user'] == 1001
        assert req_body['run_commands'] == ['testString']
        assert req_body['run_env_variables'] == [env_var_prototype_model]
        assert req_body['run_mode'] == 'task'
        assert req_body['run_service_account'] == 'default'
        assert req_body['run_volume_mounts'] == [volume_mount_prototype_model]
        assert req_body['scale_array_size_variable_override'] == 2
        assert req_body['scale_array_spec'] == '1-5,7-8,10'
        assert req_body['scale_cpu_limit'] == '1'
        assert req_body['scale_ephemeral_storage_limit'] == '4G'
        assert req_body['scale_max_execution_time'] == 7200
        assert req_body['scale_memory_limit'] == '4G'
        assert req_body['scale_retry_limit'] == 3

    def test_create_job_run_required_params_with_retries(self):
        # Enable retries and run test_create_job_run_required_params.
        _service.enable_retries()
        self.test_create_job_run_required_params()

        # Disable retries and run test_create_job_run_required_params.
        _service.disable_retries()
        self.test_create_job_run_required_params()

    @responses.activate
    def test_create_job_run_value_error(self):
        """
        test_create_job_run_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/job_runs')
        mock_response = '{"computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "job_name": "my-job", "name": "my-job-run", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_run_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_size_variable_override": 2, "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3, "status": "failed", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "failed": 0, "failed_indices": "1,5", "pending": 0, "pending_indices": "9,12-15", "requested": 0, "running": 0, "running_indices": "10-11", "start_time": "2022-09-22T17:34:00Z", "succeeded": 1, "succeeded_indices": "2-4,6-8", "unknown": 0}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Construct a dict representation of a VolumeMountPrototype model
        volume_mount_prototype_model = {}
        volume_mount_prototype_model['mount_path'] = '/app'
        volume_mount_prototype_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_prototype_model['reference'] = 'my-secret'
        volume_mount_prototype_model['type'] = 'secret'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        image_reference = 'icr.io/codeengine/helloworld'
        image_secret = 'my-secret'
        job_name = 'my-job'
        name = 'my-job-run'
        run_arguments = ['testString']
        run_as_user = 1001
        run_commands = ['testString']
        run_env_variables = [env_var_prototype_model]
        run_mode = 'task'
        run_service_account = 'default'
        run_volume_mounts = [volume_mount_prototype_model]
        scale_array_size_variable_override = 2
        scale_array_spec = '1-5,7-8,10'
        scale_cpu_limit = '1'
        scale_ephemeral_storage_limit = '4G'
        scale_max_execution_time = 7200
        scale_memory_limit = '4G'
        scale_retry_limit = 3

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_job_run(**req_copy)

    def test_create_job_run_value_error_with_retries(self):
        # Enable retries and run test_create_job_run_value_error.
        _service.enable_retries()
        self.test_create_job_run_value_error()

        # Disable retries and run test_create_job_run_value_error.
        _service.disable_retries()
        self.test_create_job_run_value_error()


class TestGetJobRun:
    """
    Test Class for get_job_run
    """

    @responses.activate
    def test_get_job_run_all_params(self):
        """
        get_job_run()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/job_runs/my-job-run')
        mock_response = '{"computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "job_name": "my-job", "name": "my-job-run", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_run_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_size_variable_override": 2, "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3, "status": "failed", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "failed": 0, "failed_indices": "1,5", "pending": 0, "pending_indices": "9,12-15", "requested": 0, "running": 0, "running_indices": "10-11", "start_time": "2022-09-22T17:34:00Z", "succeeded": 1, "succeeded_indices": "2-4,6-8", "unknown": 0}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-job-run'

        # Invoke method
        response = _service.get_job_run(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_job_run_all_params_with_retries(self):
        # Enable retries and run test_get_job_run_all_params.
        _service.enable_retries()
        self.test_get_job_run_all_params()

        # Disable retries and run test_get_job_run_all_params.
        _service.disable_retries()
        self.test_get_job_run_all_params()

    @responses.activate
    def test_get_job_run_required_params(self):
        """
        test_get_job_run_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/job_runs/my-job-run')
        mock_response = '{"computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "job_name": "my-job", "name": "my-job-run", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_run_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_size_variable_override": 2, "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3, "status": "failed", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "failed": 0, "failed_indices": "1,5", "pending": 0, "pending_indices": "9,12-15", "requested": 0, "running": 0, "running_indices": "10-11", "start_time": "2022-09-22T17:34:00Z", "succeeded": 1, "succeeded_indices": "2-4,6-8", "unknown": 0}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-job-run'

        # Invoke method
        response = _service.get_job_run(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_job_run_required_params_with_retries(self):
        # Enable retries and run test_get_job_run_required_params.
        _service.enable_retries()
        self.test_get_job_run_required_params()

        # Disable retries and run test_get_job_run_required_params.
        _service.disable_retries()
        self.test_get_job_run_required_params()

    @responses.activate
    def test_get_job_run_value_error(self):
        """
        test_get_job_run_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/job_runs/my-job-run')
        mock_response = '{"computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "job_name": "my-job", "name": "my-job-run", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "job_run_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "task", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_size_variable_override": 2, "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3, "status": "failed", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "failed": 0, "failed_indices": "1,5", "pending": 0, "pending_indices": "9,12-15", "requested": 0, "running": 0, "running_indices": "10-11", "start_time": "2022-09-22T17:34:00Z", "succeeded": 1, "succeeded_indices": "2-4,6-8", "unknown": 0}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-job-run'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_job_run(**req_copy)

    def test_get_job_run_value_error_with_retries(self):
        # Enable retries and run test_get_job_run_value_error.
        _service.enable_retries()
        self.test_get_job_run_value_error()

        # Disable retries and run test_get_job_run_value_error.
        _service.disable_retries()
        self.test_get_job_run_value_error()


class TestDeleteJobRun:
    """
    Test Class for delete_job_run
    """

    @responses.activate
    def test_delete_job_run_all_params(self):
        """
        delete_job_run()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/job_runs/my-job-run')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-job-run'

        # Invoke method
        response = _service.delete_job_run(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_job_run_all_params_with_retries(self):
        # Enable retries and run test_delete_job_run_all_params.
        _service.enable_retries()
        self.test_delete_job_run_all_params()

        # Disable retries and run test_delete_job_run_all_params.
        _service.disable_retries()
        self.test_delete_job_run_all_params()

    @responses.activate
    def test_delete_job_run_value_error(self):
        """
        test_delete_job_run_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/job_runs/my-job-run')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-job-run'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_job_run(**req_copy)

    def test_delete_job_run_value_error_with_retries(self):
        # Enable retries and run test_delete_job_run_value_error.
        _service.enable_retries()
        self.test_delete_job_run_value_error()

        # Disable retries and run test_delete_job_run_value_error.
        _service.disable_retries()
        self.test_delete_job_run_value_error()


# endregion
##############################################################################
# End of Service: Jobs
##############################################################################

##############################################################################
# Start of Service: Functions
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = CodeEngineV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CodeEngineV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CodeEngineV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListFunctionRuntimes:
    """
    Test Class for list_function_runtimes
    """

    @responses.activate
    def test_list_function_runtimes_all_params(self):
        """
        list_function_runtimes()
        """
        # Set up mock
        url = preprocess_url('/function_runtimes')
        mock_response = '{"function_runtimes": [{"default": true, "deprecated": false, "family": "nodejs", "id": "nodejs-18", "name": "Node.js 18", "optimized": true}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_function_runtimes()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_function_runtimes_all_params_with_retries(self):
        # Enable retries and run test_list_function_runtimes_all_params.
        _service.enable_retries()
        self.test_list_function_runtimes_all_params()

        # Disable retries and run test_list_function_runtimes_all_params.
        _service.disable_retries()
        self.test_list_function_runtimes_all_params()


class TestListFunctions:
    """
    Test Class for list_functions
    """

    @responses.activate
    def test_list_functions_all_params(self):
        """
        list_functions()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/functions')
        mock_response = '{"first": {"href": "href"}, "functions": [{"code_binary": false, "code_main": "main", "code_reference": "data:text/plain;base64,<base64encoded-source-code>", "code_secret": "my-secret", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-function.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-function.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/functions/my-function", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "managed_domain_mappings": "local_public", "name": "my-function", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "function_v2", "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "runtime": "nodejs-18", "scale_concurrency": 1, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_max_execution_time": 60, "scale_memory_limit": "1G", "status": "offline", "status_details": {"reason": "offline"}}], "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_functions(
            project_id,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_functions_all_params_with_retries(self):
        # Enable retries and run test_list_functions_all_params.
        _service.enable_retries()
        self.test_list_functions_all_params()

        # Disable retries and run test_list_functions_all_params.
        _service.disable_retries()
        self.test_list_functions_all_params()

    @responses.activate
    def test_list_functions_required_params(self):
        """
        test_list_functions_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/functions')
        mock_response = '{"first": {"href": "href"}, "functions": [{"code_binary": false, "code_main": "main", "code_reference": "data:text/plain;base64,<base64encoded-source-code>", "code_secret": "my-secret", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-function.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-function.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/functions/my-function", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "managed_domain_mappings": "local_public", "name": "my-function", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "function_v2", "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "runtime": "nodejs-18", "scale_concurrency": 1, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_max_execution_time": 60, "scale_memory_limit": "1G", "status": "offline", "status_details": {"reason": "offline"}}], "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.list_functions(
            project_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_functions_required_params_with_retries(self):
        # Enable retries and run test_list_functions_required_params.
        _service.enable_retries()
        self.test_list_functions_required_params()

        # Disable retries and run test_list_functions_required_params.
        _service.disable_retries()
        self.test_list_functions_required_params()

    @responses.activate
    def test_list_functions_value_error(self):
        """
        test_list_functions_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/functions')
        mock_response = '{"first": {"href": "href"}, "functions": [{"code_binary": false, "code_main": "main", "code_reference": "data:text/plain;base64,<base64encoded-source-code>", "code_secret": "my-secret", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-function.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-function.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/functions/my-function", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "managed_domain_mappings": "local_public", "name": "my-function", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "function_v2", "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "runtime": "nodejs-18", "scale_concurrency": 1, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_max_execution_time": 60, "scale_memory_limit": "1G", "status": "offline", "status_details": {"reason": "offline"}}], "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_functions(**req_copy)

    def test_list_functions_value_error_with_retries(self):
        # Enable retries and run test_list_functions_value_error.
        _service.enable_retries()
        self.test_list_functions_value_error()

        # Disable retries and run test_list_functions_value_error.
        _service.disable_retries()
        self.test_list_functions_value_error()

    @responses.activate
    def test_list_functions_with_pager_get_next(self):
        """
        test_list_functions_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/functions')
        mock_response1 = '{"next":{"start":"1"},"functions":[{"code_binary":false,"code_main":"main","code_reference":"data:text/plain;base64,<base64encoded-source-code>","code_secret":"my-secret","computed_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"created_at":"2022-09-13T11:41:35+02:00","endpoint":"https://my-function.vg67hzldruk.eu-de.codeengine.appdomain.cloud","endpoint_internal":"http://my-function.vg67hzldruk.svc.cluster.local","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/functions/my-function","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","managed_domain_mappings":"local_public","name":"my-function","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"function_v2","run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"runtime":"nodejs-18","scale_concurrency":1,"scale_cpu_limit":"1","scale_down_delay":300,"scale_max_execution_time":60,"scale_memory_limit":"1G","status":"offline","status_details":{"reason":"offline"}}],"total_count":2,"limit":1}'
        mock_response2 = '{"functions":[{"code_binary":false,"code_main":"main","code_reference":"data:text/plain;base64,<base64encoded-source-code>","code_secret":"my-secret","computed_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"created_at":"2022-09-13T11:41:35+02:00","endpoint":"https://my-function.vg67hzldruk.eu-de.codeengine.appdomain.cloud","endpoint_internal":"http://my-function.vg67hzldruk.svc.cluster.local","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/functions/my-function","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","managed_domain_mappings":"local_public","name":"my-function","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"function_v2","run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"runtime":"nodejs-18","scale_concurrency":1,"scale_cpu_limit":"1","scale_down_delay":300,"scale_max_execution_time":60,"scale_memory_limit":"1G","status":"offline","status_details":{"reason":"offline"}}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = FunctionsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_functions_with_pager_get_all(self):
        """
        test_list_functions_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/functions')
        mock_response1 = '{"next":{"start":"1"},"functions":[{"code_binary":false,"code_main":"main","code_reference":"data:text/plain;base64,<base64encoded-source-code>","code_secret":"my-secret","computed_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"created_at":"2022-09-13T11:41:35+02:00","endpoint":"https://my-function.vg67hzldruk.eu-de.codeengine.appdomain.cloud","endpoint_internal":"http://my-function.vg67hzldruk.svc.cluster.local","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/functions/my-function","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","managed_domain_mappings":"local_public","name":"my-function","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"function_v2","run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"runtime":"nodejs-18","scale_concurrency":1,"scale_cpu_limit":"1","scale_down_delay":300,"scale_max_execution_time":60,"scale_memory_limit":"1G","status":"offline","status_details":{"reason":"offline"}}],"total_count":2,"limit":1}'
        mock_response2 = '{"functions":[{"code_binary":false,"code_main":"main","code_reference":"data:text/plain;base64,<base64encoded-source-code>","code_secret":"my-secret","computed_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"created_at":"2022-09-13T11:41:35+02:00","endpoint":"https://my-function.vg67hzldruk.eu-de.codeengine.appdomain.cloud","endpoint_internal":"http://my-function.vg67hzldruk.svc.cluster.local","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/functions/my-function","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","managed_domain_mappings":"local_public","name":"my-function","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"function_v2","run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"runtime":"nodejs-18","scale_concurrency":1,"scale_cpu_limit":"1","scale_down_delay":300,"scale_max_execution_time":60,"scale_memory_limit":"1G","status":"offline","status_details":{"reason":"offline"}}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = FunctionsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            limit=100,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateFunction:
    """
    Test Class for create_function
    """

    @responses.activate
    def test_create_function_all_params(self):
        """
        create_function()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/functions')
        mock_response = '{"code_binary": false, "code_main": "main", "code_reference": "data:text/plain;base64,<base64encoded-source-code>", "code_secret": "my-secret", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-function.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-function.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/functions/my-function", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "managed_domain_mappings": "local_public", "name": "my-function", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "function_v2", "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "runtime": "nodejs-18", "scale_concurrency": 1, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_max_execution_time": 60, "scale_memory_limit": "1G", "status": "offline", "status_details": {"reason": "offline"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        code_reference = 'data:text/plain;base64,<base64encoded-source-code>'
        name = 'my-function'
        runtime = 'nodejs-18'
        code_binary = False
        code_main = 'main'
        code_secret = 'my-secret'
        managed_domain_mappings = 'local_public'
        run_env_variables = [env_var_prototype_model]
        scale_concurrency = 1
        scale_cpu_limit = '1'
        scale_down_delay = 300
        scale_max_execution_time = 60
        scale_memory_limit = '1G'

        # Invoke method
        response = _service.create_function(
            project_id,
            code_reference,
            name,
            runtime,
            code_binary=code_binary,
            code_main=code_main,
            code_secret=code_secret,
            managed_domain_mappings=managed_domain_mappings,
            run_env_variables=run_env_variables,
            scale_concurrency=scale_concurrency,
            scale_cpu_limit=scale_cpu_limit,
            scale_down_delay=scale_down_delay,
            scale_max_execution_time=scale_max_execution_time,
            scale_memory_limit=scale_memory_limit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['code_reference'] == 'data:text/plain;base64,<base64encoded-source-code>'
        assert req_body['name'] == 'my-function'
        assert req_body['runtime'] == 'nodejs-18'
        assert req_body['code_binary'] == False
        assert req_body['code_main'] == 'main'
        assert req_body['code_secret'] == 'my-secret'
        assert req_body['managed_domain_mappings'] == 'local_public'
        assert req_body['run_env_variables'] == [env_var_prototype_model]
        assert req_body['scale_concurrency'] == 1
        assert req_body['scale_cpu_limit'] == '1'
        assert req_body['scale_down_delay'] == 300
        assert req_body['scale_max_execution_time'] == 60
        assert req_body['scale_memory_limit'] == '1G'

    def test_create_function_all_params_with_retries(self):
        # Enable retries and run test_create_function_all_params.
        _service.enable_retries()
        self.test_create_function_all_params()

        # Disable retries and run test_create_function_all_params.
        _service.disable_retries()
        self.test_create_function_all_params()

    @responses.activate
    def test_create_function_required_params(self):
        """
        test_create_function_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/functions')
        mock_response = '{"code_binary": false, "code_main": "main", "code_reference": "data:text/plain;base64,<base64encoded-source-code>", "code_secret": "my-secret", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-function.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-function.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/functions/my-function", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "managed_domain_mappings": "local_public", "name": "my-function", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "function_v2", "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "runtime": "nodejs-18", "scale_concurrency": 1, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_max_execution_time": 60, "scale_memory_limit": "1G", "status": "offline", "status_details": {"reason": "offline"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        code_reference = 'data:text/plain;base64,<base64encoded-source-code>'
        name = 'my-function'
        runtime = 'nodejs-18'
        code_binary = False
        code_main = 'main'
        code_secret = 'my-secret'
        managed_domain_mappings = 'local_public'
        run_env_variables = [env_var_prototype_model]
        scale_concurrency = 1
        scale_cpu_limit = '1'
        scale_down_delay = 300
        scale_max_execution_time = 60
        scale_memory_limit = '1G'

        # Invoke method
        response = _service.create_function(
            project_id,
            code_reference,
            name,
            runtime,
            code_binary=code_binary,
            code_main=code_main,
            code_secret=code_secret,
            managed_domain_mappings=managed_domain_mappings,
            run_env_variables=run_env_variables,
            scale_concurrency=scale_concurrency,
            scale_cpu_limit=scale_cpu_limit,
            scale_down_delay=scale_down_delay,
            scale_max_execution_time=scale_max_execution_time,
            scale_memory_limit=scale_memory_limit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['code_reference'] == 'data:text/plain;base64,<base64encoded-source-code>'
        assert req_body['name'] == 'my-function'
        assert req_body['runtime'] == 'nodejs-18'
        assert req_body['code_binary'] == False
        assert req_body['code_main'] == 'main'
        assert req_body['code_secret'] == 'my-secret'
        assert req_body['managed_domain_mappings'] == 'local_public'
        assert req_body['run_env_variables'] == [env_var_prototype_model]
        assert req_body['scale_concurrency'] == 1
        assert req_body['scale_cpu_limit'] == '1'
        assert req_body['scale_down_delay'] == 300
        assert req_body['scale_max_execution_time'] == 60
        assert req_body['scale_memory_limit'] == '1G'

    def test_create_function_required_params_with_retries(self):
        # Enable retries and run test_create_function_required_params.
        _service.enable_retries()
        self.test_create_function_required_params()

        # Disable retries and run test_create_function_required_params.
        _service.disable_retries()
        self.test_create_function_required_params()

    @responses.activate
    def test_create_function_value_error(self):
        """
        test_create_function_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/functions')
        mock_response = '{"code_binary": false, "code_main": "main", "code_reference": "data:text/plain;base64,<base64encoded-source-code>", "code_secret": "my-secret", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-function.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-function.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/functions/my-function", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "managed_domain_mappings": "local_public", "name": "my-function", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "function_v2", "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "runtime": "nodejs-18", "scale_concurrency": 1, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_max_execution_time": 60, "scale_memory_limit": "1G", "status": "offline", "status_details": {"reason": "offline"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        code_reference = 'data:text/plain;base64,<base64encoded-source-code>'
        name = 'my-function'
        runtime = 'nodejs-18'
        code_binary = False
        code_main = 'main'
        code_secret = 'my-secret'
        managed_domain_mappings = 'local_public'
        run_env_variables = [env_var_prototype_model]
        scale_concurrency = 1
        scale_cpu_limit = '1'
        scale_down_delay = 300
        scale_max_execution_time = 60
        scale_memory_limit = '1G'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "code_reference": code_reference,
            "name": name,
            "runtime": runtime,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_function(**req_copy)

    def test_create_function_value_error_with_retries(self):
        # Enable retries and run test_create_function_value_error.
        _service.enable_retries()
        self.test_create_function_value_error()

        # Disable retries and run test_create_function_value_error.
        _service.disable_retries()
        self.test_create_function_value_error()


class TestGetFunction:
    """
    Test Class for get_function
    """

    @responses.activate
    def test_get_function_all_params(self):
        """
        get_function()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/functions/my-function')
        mock_response = '{"code_binary": false, "code_main": "main", "code_reference": "data:text/plain;base64,<base64encoded-source-code>", "code_secret": "my-secret", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-function.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-function.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/functions/my-function", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "managed_domain_mappings": "local_public", "name": "my-function", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "function_v2", "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "runtime": "nodejs-18", "scale_concurrency": 1, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_max_execution_time": 60, "scale_memory_limit": "1G", "status": "offline", "status_details": {"reason": "offline"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-function'

        # Invoke method
        response = _service.get_function(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_function_all_params_with_retries(self):
        # Enable retries and run test_get_function_all_params.
        _service.enable_retries()
        self.test_get_function_all_params()

        # Disable retries and run test_get_function_all_params.
        _service.disable_retries()
        self.test_get_function_all_params()

    @responses.activate
    def test_get_function_required_params(self):
        """
        test_get_function_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/functions/my-function')
        mock_response = '{"code_binary": false, "code_main": "main", "code_reference": "data:text/plain;base64,<base64encoded-source-code>", "code_secret": "my-secret", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-function.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-function.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/functions/my-function", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "managed_domain_mappings": "local_public", "name": "my-function", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "function_v2", "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "runtime": "nodejs-18", "scale_concurrency": 1, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_max_execution_time": 60, "scale_memory_limit": "1G", "status": "offline", "status_details": {"reason": "offline"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-function'

        # Invoke method
        response = _service.get_function(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_function_required_params_with_retries(self):
        # Enable retries and run test_get_function_required_params.
        _service.enable_retries()
        self.test_get_function_required_params()

        # Disable retries and run test_get_function_required_params.
        _service.disable_retries()
        self.test_get_function_required_params()

    @responses.activate
    def test_get_function_value_error(self):
        """
        test_get_function_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/functions/my-function')
        mock_response = '{"code_binary": false, "code_main": "main", "code_reference": "data:text/plain;base64,<base64encoded-source-code>", "code_secret": "my-secret", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-function.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-function.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/functions/my-function", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "managed_domain_mappings": "local_public", "name": "my-function", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "function_v2", "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "runtime": "nodejs-18", "scale_concurrency": 1, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_max_execution_time": 60, "scale_memory_limit": "1G", "status": "offline", "status_details": {"reason": "offline"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-function'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_function(**req_copy)

    def test_get_function_value_error_with_retries(self):
        # Enable retries and run test_get_function_value_error.
        _service.enable_retries()
        self.test_get_function_value_error()

        # Disable retries and run test_get_function_value_error.
        _service.disable_retries()
        self.test_get_function_value_error()


class TestDeleteFunction:
    """
    Test Class for delete_function
    """

    @responses.activate
    def test_delete_function_all_params(self):
        """
        delete_function()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/functions/my-function')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-function'

        # Invoke method
        response = _service.delete_function(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_function_all_params_with_retries(self):
        # Enable retries and run test_delete_function_all_params.
        _service.enable_retries()
        self.test_delete_function_all_params()

        # Disable retries and run test_delete_function_all_params.
        _service.disable_retries()
        self.test_delete_function_all_params()

    @responses.activate
    def test_delete_function_required_params(self):
        """
        test_delete_function_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/functions/my-function')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-function'

        # Invoke method
        response = _service.delete_function(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_function_required_params_with_retries(self):
        # Enable retries and run test_delete_function_required_params.
        _service.enable_retries()
        self.test_delete_function_required_params()

        # Disable retries and run test_delete_function_required_params.
        _service.disable_retries()
        self.test_delete_function_required_params()

    @responses.activate
    def test_delete_function_value_error(self):
        """
        test_delete_function_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/functions/my-function')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-function'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_function(**req_copy)

    def test_delete_function_value_error_with_retries(self):
        # Enable retries and run test_delete_function_value_error.
        _service.enable_retries()
        self.test_delete_function_value_error()

        # Disable retries and run test_delete_function_value_error.
        _service.disable_retries()
        self.test_delete_function_value_error()


class TestUpdateFunction:
    """
    Test Class for update_function
    """

    @responses.activate
    def test_update_function_all_params(self):
        """
        update_function()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/functions/my-function')
        mock_response = '{"code_binary": false, "code_main": "main", "code_reference": "data:text/plain;base64,<base64encoded-source-code>", "code_secret": "my-secret", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-function.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-function.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/functions/my-function", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "managed_domain_mappings": "local_public", "name": "my-function", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "function_v2", "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "runtime": "nodejs-18", "scale_concurrency": 1, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_max_execution_time": 60, "scale_memory_limit": "1G", "status": "offline", "status_details": {"reason": "offline"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Construct a dict representation of a FunctionPatch model
        function_patch_model = {}
        function_patch_model['code_binary'] = False
        function_patch_model['code_main'] = 'main'
        function_patch_model['code_reference'] = 'data:text/plain;base64,<base64encoded-source-code>'
        function_patch_model['code_secret'] = 'my-secret'
        function_patch_model['managed_domain_mappings'] = 'local_public'
        function_patch_model['run_env_variables'] = [env_var_prototype_model]
        function_patch_model['runtime'] = 'nodejs-18'
        function_patch_model['scale_concurrency'] = 1
        function_patch_model['scale_cpu_limit'] = '1'
        function_patch_model['scale_down_delay'] = 300
        function_patch_model['scale_max_execution_time'] = 60
        function_patch_model['scale_memory_limit'] = '1G'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-function'
        if_match = 'testString'
        function = function_patch_model

        # Invoke method
        response = _service.update_function(
            project_id,
            name,
            if_match,
            function,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == function

    def test_update_function_all_params_with_retries(self):
        # Enable retries and run test_update_function_all_params.
        _service.enable_retries()
        self.test_update_function_all_params()

        # Disable retries and run test_update_function_all_params.
        _service.disable_retries()
        self.test_update_function_all_params()

    @responses.activate
    def test_update_function_required_params(self):
        """
        test_update_function_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/functions/my-function')
        mock_response = '{"code_binary": false, "code_main": "main", "code_reference": "data:text/plain;base64,<base64encoded-source-code>", "code_secret": "my-secret", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-function.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-function.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/functions/my-function", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "managed_domain_mappings": "local_public", "name": "my-function", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "function_v2", "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "runtime": "nodejs-18", "scale_concurrency": 1, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_max_execution_time": 60, "scale_memory_limit": "1G", "status": "offline", "status_details": {"reason": "offline"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Construct a dict representation of a FunctionPatch model
        function_patch_model = {}
        function_patch_model['code_binary'] = False
        function_patch_model['code_main'] = 'main'
        function_patch_model['code_reference'] = 'data:text/plain;base64,<base64encoded-source-code>'
        function_patch_model['code_secret'] = 'my-secret'
        function_patch_model['managed_domain_mappings'] = 'local_public'
        function_patch_model['run_env_variables'] = [env_var_prototype_model]
        function_patch_model['runtime'] = 'nodejs-18'
        function_patch_model['scale_concurrency'] = 1
        function_patch_model['scale_cpu_limit'] = '1'
        function_patch_model['scale_down_delay'] = 300
        function_patch_model['scale_max_execution_time'] = 60
        function_patch_model['scale_memory_limit'] = '1G'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-function'
        if_match = 'testString'
        function = function_patch_model

        # Invoke method
        response = _service.update_function(
            project_id,
            name,
            if_match,
            function,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == function

    def test_update_function_required_params_with_retries(self):
        # Enable retries and run test_update_function_required_params.
        _service.enable_retries()
        self.test_update_function_required_params()

        # Disable retries and run test_update_function_required_params.
        _service.disable_retries()
        self.test_update_function_required_params()

    @responses.activate
    def test_update_function_value_error(self):
        """
        test_update_function_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/functions/my-function')
        mock_response = '{"code_binary": false, "code_main": "main", "code_reference": "data:text/plain;base64,<base64encoded-source-code>", "code_secret": "my-secret", "computed_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-function.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-function.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/functions/my-function", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "managed_domain_mappings": "local_public", "name": "my-function", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "function_v2", "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "runtime": "nodejs-18", "scale_concurrency": 1, "scale_cpu_limit": "1", "scale_down_delay": 300, "scale_max_execution_time": 60, "scale_memory_limit": "1G", "status": "offline", "status_details": {"reason": "offline"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {}
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Construct a dict representation of a FunctionPatch model
        function_patch_model = {}
        function_patch_model['code_binary'] = False
        function_patch_model['code_main'] = 'main'
        function_patch_model['code_reference'] = 'data:text/plain;base64,<base64encoded-source-code>'
        function_patch_model['code_secret'] = 'my-secret'
        function_patch_model['managed_domain_mappings'] = 'local_public'
        function_patch_model['run_env_variables'] = [env_var_prototype_model]
        function_patch_model['runtime'] = 'nodejs-18'
        function_patch_model['scale_concurrency'] = 1
        function_patch_model['scale_cpu_limit'] = '1'
        function_patch_model['scale_down_delay'] = 300
        function_patch_model['scale_max_execution_time'] = 60
        function_patch_model['scale_memory_limit'] = '1G'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-function'
        if_match = 'testString'
        function = function_patch_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
            "if_match": if_match,
            "function": function,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_function(**req_copy)

    def test_update_function_value_error_with_retries(self):
        # Enable retries and run test_update_function_value_error.
        _service.enable_retries()
        self.test_update_function_value_error()

        # Disable retries and run test_update_function_value_error.
        _service.disable_retries()
        self.test_update_function_value_error()


# endregion
##############################################################################
# End of Service: Functions
##############################################################################

##############################################################################
# Start of Service: ServiceBindings
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = CodeEngineV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CodeEngineV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CodeEngineV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListBindings:
    """
    Test Class for list_bindings
    """

    @responses.activate
    def test_list_bindings_all_params(self):
        """
        list_bindings()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/bindings')
        mock_response = '{"bindings": [{"component": {"name": "my-app-1", "resource_type": "app_v2"}, "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/bindings/my-binding", "id": "a172ced-b5f21bc-71ba50c-1638604", "prefix": "MY_COS", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "binding_v2", "secret_name": "my-service-access", "status": "active"}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_bindings(
            project_id,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_bindings_all_params_with_retries(self):
        # Enable retries and run test_list_bindings_all_params.
        _service.enable_retries()
        self.test_list_bindings_all_params()

        # Disable retries and run test_list_bindings_all_params.
        _service.disable_retries()
        self.test_list_bindings_all_params()

    @responses.activate
    def test_list_bindings_required_params(self):
        """
        test_list_bindings_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/bindings')
        mock_response = '{"bindings": [{"component": {"name": "my-app-1", "resource_type": "app_v2"}, "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/bindings/my-binding", "id": "a172ced-b5f21bc-71ba50c-1638604", "prefix": "MY_COS", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "binding_v2", "secret_name": "my-service-access", "status": "active"}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.list_bindings(
            project_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_bindings_required_params_with_retries(self):
        # Enable retries and run test_list_bindings_required_params.
        _service.enable_retries()
        self.test_list_bindings_required_params()

        # Disable retries and run test_list_bindings_required_params.
        _service.disable_retries()
        self.test_list_bindings_required_params()

    @responses.activate
    def test_list_bindings_value_error(self):
        """
        test_list_bindings_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/bindings')
        mock_response = '{"bindings": [{"component": {"name": "my-app-1", "resource_type": "app_v2"}, "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/bindings/my-binding", "id": "a172ced-b5f21bc-71ba50c-1638604", "prefix": "MY_COS", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "binding_v2", "secret_name": "my-service-access", "status": "active"}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_bindings(**req_copy)

    def test_list_bindings_value_error_with_retries(self):
        # Enable retries and run test_list_bindings_value_error.
        _service.enable_retries()
        self.test_list_bindings_value_error()

        # Disable retries and run test_list_bindings_value_error.
        _service.disable_retries()
        self.test_list_bindings_value_error()

    @responses.activate
    def test_list_bindings_with_pager_get_next(self):
        """
        test_list_bindings_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/bindings')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"bindings":[{"component":{"name":"my-app-1","resource_type":"app_v2"},"href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/bindings/my-binding","id":"a172ced-b5f21bc-71ba50c-1638604","prefix":"MY_COS","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"binding_v2","secret_name":"my-service-access","status":"active"}],"limit":1}'
        mock_response2 = '{"total_count":2,"bindings":[{"component":{"name":"my-app-1","resource_type":"app_v2"},"href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/bindings/my-binding","id":"a172ced-b5f21bc-71ba50c-1638604","prefix":"MY_COS","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"binding_v2","secret_name":"my-service-access","status":"active"}],"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = BindingsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_bindings_with_pager_get_all(self):
        """
        test_list_bindings_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/bindings')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"bindings":[{"component":{"name":"my-app-1","resource_type":"app_v2"},"href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/bindings/my-binding","id":"a172ced-b5f21bc-71ba50c-1638604","prefix":"MY_COS","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"binding_v2","secret_name":"my-service-access","status":"active"}],"limit":1}'
        mock_response2 = '{"total_count":2,"bindings":[{"component":{"name":"my-app-1","resource_type":"app_v2"},"href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/bindings/my-binding","id":"a172ced-b5f21bc-71ba50c-1638604","prefix":"MY_COS","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"binding_v2","secret_name":"my-service-access","status":"active"}],"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = BindingsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            limit=100,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateBinding:
    """
    Test Class for create_binding
    """

    @responses.activate
    def test_create_binding_all_params(self):
        """
        create_binding()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/bindings')
        mock_response = '{"component": {"name": "my-app-1", "resource_type": "app_v2"}, "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/bindings/my-binding", "id": "a172ced-b5f21bc-71ba50c-1638604", "prefix": "MY_COS", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "binding_v2", "secret_name": "my-service-access", "status": "active"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ComponentRef model
        component_ref_model = {}
        component_ref_model['name'] = 'my-app-1'
        component_ref_model['resource_type'] = 'app_v2'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        component = component_ref_model
        prefix = 'MY_COS'
        secret_name = 'my-service-access'

        # Invoke method
        response = _service.create_binding(
            project_id,
            component,
            prefix,
            secret_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['component'] == component_ref_model
        assert req_body['prefix'] == 'MY_COS'
        assert req_body['secret_name'] == 'my-service-access'

    def test_create_binding_all_params_with_retries(self):
        # Enable retries and run test_create_binding_all_params.
        _service.enable_retries()
        self.test_create_binding_all_params()

        # Disable retries and run test_create_binding_all_params.
        _service.disable_retries()
        self.test_create_binding_all_params()

    @responses.activate
    def test_create_binding_value_error(self):
        """
        test_create_binding_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/bindings')
        mock_response = '{"component": {"name": "my-app-1", "resource_type": "app_v2"}, "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/bindings/my-binding", "id": "a172ced-b5f21bc-71ba50c-1638604", "prefix": "MY_COS", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "binding_v2", "secret_name": "my-service-access", "status": "active"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ComponentRef model
        component_ref_model = {}
        component_ref_model['name'] = 'my-app-1'
        component_ref_model['resource_type'] = 'app_v2'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        component = component_ref_model
        prefix = 'MY_COS'
        secret_name = 'my-service-access'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "component": component,
            "prefix": prefix,
            "secret_name": secret_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_binding(**req_copy)

    def test_create_binding_value_error_with_retries(self):
        # Enable retries and run test_create_binding_value_error.
        _service.enable_retries()
        self.test_create_binding_value_error()

        # Disable retries and run test_create_binding_value_error.
        _service.disable_retries()
        self.test_create_binding_value_error()


class TestGetBinding:
    """
    Test Class for get_binding
    """

    @responses.activate
    def test_get_binding_all_params(self):
        """
        get_binding()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/bindings/a172ced-b5f21bc-71ba50c-1638604')
        mock_response = '{"component": {"name": "my-app-1", "resource_type": "app_v2"}, "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/bindings/my-binding", "id": "a172ced-b5f21bc-71ba50c-1638604", "prefix": "MY_COS", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "binding_v2", "secret_name": "my-service-access", "status": "active"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        id = 'a172ced-b5f21bc-71ba50c-1638604'

        # Invoke method
        response = _service.get_binding(
            project_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_binding_all_params_with_retries(self):
        # Enable retries and run test_get_binding_all_params.
        _service.enable_retries()
        self.test_get_binding_all_params()

        # Disable retries and run test_get_binding_all_params.
        _service.disable_retries()
        self.test_get_binding_all_params()

    @responses.activate
    def test_get_binding_value_error(self):
        """
        test_get_binding_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/bindings/a172ced-b5f21bc-71ba50c-1638604')
        mock_response = '{"component": {"name": "my-app-1", "resource_type": "app_v2"}, "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/bindings/my-binding", "id": "a172ced-b5f21bc-71ba50c-1638604", "prefix": "MY_COS", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "binding_v2", "secret_name": "my-service-access", "status": "active"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        id = 'a172ced-b5f21bc-71ba50c-1638604'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_binding(**req_copy)

    def test_get_binding_value_error_with_retries(self):
        # Enable retries and run test_get_binding_value_error.
        _service.enable_retries()
        self.test_get_binding_value_error()

        # Disable retries and run test_get_binding_value_error.
        _service.disable_retries()
        self.test_get_binding_value_error()


class TestDeleteBinding:
    """
    Test Class for delete_binding
    """

    @responses.activate
    def test_delete_binding_all_params(self):
        """
        delete_binding()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/bindings/a172ced-b5f21bc-71ba50c-1638604')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        id = 'a172ced-b5f21bc-71ba50c-1638604'

        # Invoke method
        response = _service.delete_binding(
            project_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_binding_all_params_with_retries(self):
        # Enable retries and run test_delete_binding_all_params.
        _service.enable_retries()
        self.test_delete_binding_all_params()

        # Disable retries and run test_delete_binding_all_params.
        _service.disable_retries()
        self.test_delete_binding_all_params()

    @responses.activate
    def test_delete_binding_value_error(self):
        """
        test_delete_binding_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/bindings/a172ced-b5f21bc-71ba50c-1638604')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        id = 'a172ced-b5f21bc-71ba50c-1638604'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_binding(**req_copy)

    def test_delete_binding_value_error_with_retries(self):
        # Enable retries and run test_delete_binding_value_error.
        _service.enable_retries()
        self.test_delete_binding_value_error()

        # Disable retries and run test_delete_binding_value_error.
        _service.disable_retries()
        self.test_delete_binding_value_error()


# endregion
##############################################################################
# End of Service: ServiceBindings
##############################################################################

##############################################################################
# Start of Service: ImageBuilds
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = CodeEngineV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CodeEngineV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CodeEngineV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListBuilds:
    """
    Test Class for list_builds
    """

    @responses.activate
    def test_list_builds_all_params(self):
        """
        list_builds()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/builds')
        mock_response = '{"builds": [{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "build_v2", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "ready", "status_details": {"reason": "registered"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_builds(
            project_id,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_builds_all_params_with_retries(self):
        # Enable retries and run test_list_builds_all_params.
        _service.enable_retries()
        self.test_list_builds_all_params()

        # Disable retries and run test_list_builds_all_params.
        _service.disable_retries()
        self.test_list_builds_all_params()

    @responses.activate
    def test_list_builds_required_params(self):
        """
        test_list_builds_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/builds')
        mock_response = '{"builds": [{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "build_v2", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "ready", "status_details": {"reason": "registered"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.list_builds(
            project_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_builds_required_params_with_retries(self):
        # Enable retries and run test_list_builds_required_params.
        _service.enable_retries()
        self.test_list_builds_required_params()

        # Disable retries and run test_list_builds_required_params.
        _service.disable_retries()
        self.test_list_builds_required_params()

    @responses.activate
    def test_list_builds_value_error(self):
        """
        test_list_builds_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/builds')
        mock_response = '{"builds": [{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "build_v2", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "ready", "status_details": {"reason": "registered"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_builds(**req_copy)

    def test_list_builds_value_error_with_retries(self):
        # Enable retries and run test_list_builds_value_error.
        _service.enable_retries()
        self.test_list_builds_value_error()

        # Disable retries and run test_list_builds_value_error.
        _service.disable_retries()
        self.test_list_builds_value_error()

    @responses.activate
    def test_list_builds_with_pager_get_next(self):
        """
        test_list_builds_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/builds')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"builds":[{"created_at":"2022-09-13T11:41:35+02:00","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-build","output_image":"private.de.icr.io/icr_namespace/image-name","output_secret":"ce-auto-icr-private-eu-de","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"build_v2","source_context_dir":"some/subfolder","source_revision":"main","source_secret":"source_secret","source_type":"git","source_url":"https://github.com/IBM/CodeEngine","status":"ready","status_details":{"reason":"registered"},"strategy_size":"medium","strategy_spec_file":"Dockerfile","strategy_type":"dockerfile","timeout":600}]}'
        mock_response2 = '{"total_count":2,"limit":1,"builds":[{"created_at":"2022-09-13T11:41:35+02:00","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-build","output_image":"private.de.icr.io/icr_namespace/image-name","output_secret":"ce-auto-icr-private-eu-de","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"build_v2","source_context_dir":"some/subfolder","source_revision":"main","source_secret":"source_secret","source_type":"git","source_url":"https://github.com/IBM/CodeEngine","status":"ready","status_details":{"reason":"registered"},"strategy_size":"medium","strategy_spec_file":"Dockerfile","strategy_type":"dockerfile","timeout":600}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = BuildsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_builds_with_pager_get_all(self):
        """
        test_list_builds_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/builds')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"builds":[{"created_at":"2022-09-13T11:41:35+02:00","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-build","output_image":"private.de.icr.io/icr_namespace/image-name","output_secret":"ce-auto-icr-private-eu-de","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"build_v2","source_context_dir":"some/subfolder","source_revision":"main","source_secret":"source_secret","source_type":"git","source_url":"https://github.com/IBM/CodeEngine","status":"ready","status_details":{"reason":"registered"},"strategy_size":"medium","strategy_spec_file":"Dockerfile","strategy_type":"dockerfile","timeout":600}]}'
        mock_response2 = '{"total_count":2,"limit":1,"builds":[{"created_at":"2022-09-13T11:41:35+02:00","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-build","output_image":"private.de.icr.io/icr_namespace/image-name","output_secret":"ce-auto-icr-private-eu-de","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"build_v2","source_context_dir":"some/subfolder","source_revision":"main","source_secret":"source_secret","source_type":"git","source_url":"https://github.com/IBM/CodeEngine","status":"ready","status_details":{"reason":"registered"},"strategy_size":"medium","strategy_spec_file":"Dockerfile","strategy_type":"dockerfile","timeout":600}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = BuildsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            limit=100,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateBuild:
    """
    Test Class for create_build
    """

    @responses.activate
    def test_create_build_all_params(self):
        """
        create_build()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/builds')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "build_v2", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "ready", "status_details": {"reason": "registered"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-build'
        output_image = 'private.de.icr.io/icr_namespace/image-name'
        output_secret = 'ce-auto-icr-private-eu-de'
        strategy_type = 'dockerfile'
        source_context_dir = 'some/subfolder'
        source_revision = 'main'
        source_secret = 'testString'
        source_type = 'git'
        source_url = 'https://github.com/IBM/CodeEngine'
        strategy_size = 'medium'
        strategy_spec_file = 'Dockerfile'
        timeout = 600

        # Invoke method
        response = _service.create_build(
            project_id,
            name,
            output_image,
            output_secret,
            strategy_type,
            source_context_dir=source_context_dir,
            source_revision=source_revision,
            source_secret=source_secret,
            source_type=source_type,
            source_url=source_url,
            strategy_size=strategy_size,
            strategy_spec_file=strategy_spec_file,
            timeout=timeout,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'my-build'
        assert req_body['output_image'] == 'private.de.icr.io/icr_namespace/image-name'
        assert req_body['output_secret'] == 'ce-auto-icr-private-eu-de'
        assert req_body['strategy_type'] == 'dockerfile'
        assert req_body['source_context_dir'] == 'some/subfolder'
        assert req_body['source_revision'] == 'main'
        assert req_body['source_secret'] == 'testString'
        assert req_body['source_type'] == 'git'
        assert req_body['source_url'] == 'https://github.com/IBM/CodeEngine'
        assert req_body['strategy_size'] == 'medium'
        assert req_body['strategy_spec_file'] == 'Dockerfile'
        assert req_body['timeout'] == 600

    def test_create_build_all_params_with_retries(self):
        # Enable retries and run test_create_build_all_params.
        _service.enable_retries()
        self.test_create_build_all_params()

        # Disable retries and run test_create_build_all_params.
        _service.disable_retries()
        self.test_create_build_all_params()

    @responses.activate
    def test_create_build_value_error(self):
        """
        test_create_build_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/builds')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "build_v2", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "ready", "status_details": {"reason": "registered"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-build'
        output_image = 'private.de.icr.io/icr_namespace/image-name'
        output_secret = 'ce-auto-icr-private-eu-de'
        strategy_type = 'dockerfile'
        source_context_dir = 'some/subfolder'
        source_revision = 'main'
        source_secret = 'testString'
        source_type = 'git'
        source_url = 'https://github.com/IBM/CodeEngine'
        strategy_size = 'medium'
        strategy_spec_file = 'Dockerfile'
        timeout = 600

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
            "output_image": output_image,
            "output_secret": output_secret,
            "strategy_type": strategy_type,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_build(**req_copy)

    def test_create_build_value_error_with_retries(self):
        # Enable retries and run test_create_build_value_error.
        _service.enable_retries()
        self.test_create_build_value_error()

        # Disable retries and run test_create_build_value_error.
        _service.disable_retries()
        self.test_create_build_value_error()


class TestGetBuild:
    """
    Test Class for get_build
    """

    @responses.activate
    def test_get_build_all_params(self):
        """
        get_build()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/builds/my-build')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "build_v2", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "ready", "status_details": {"reason": "registered"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-build'

        # Invoke method
        response = _service.get_build(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_build_all_params_with_retries(self):
        # Enable retries and run test_get_build_all_params.
        _service.enable_retries()
        self.test_get_build_all_params()

        # Disable retries and run test_get_build_all_params.
        _service.disable_retries()
        self.test_get_build_all_params()

    @responses.activate
    def test_get_build_value_error(self):
        """
        test_get_build_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/builds/my-build')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "build_v2", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "ready", "status_details": {"reason": "registered"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-build'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_build(**req_copy)

    def test_get_build_value_error_with_retries(self):
        # Enable retries and run test_get_build_value_error.
        _service.enable_retries()
        self.test_get_build_value_error()

        # Disable retries and run test_get_build_value_error.
        _service.disable_retries()
        self.test_get_build_value_error()


class TestDeleteBuild:
    """
    Test Class for delete_build
    """

    @responses.activate
    def test_delete_build_all_params(self):
        """
        delete_build()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/builds/my-build')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-build'

        # Invoke method
        response = _service.delete_build(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_build_all_params_with_retries(self):
        # Enable retries and run test_delete_build_all_params.
        _service.enable_retries()
        self.test_delete_build_all_params()

        # Disable retries and run test_delete_build_all_params.
        _service.disable_retries()
        self.test_delete_build_all_params()

    @responses.activate
    def test_delete_build_value_error(self):
        """
        test_delete_build_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/builds/my-build')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-build'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_build(**req_copy)

    def test_delete_build_value_error_with_retries(self):
        # Enable retries and run test_delete_build_value_error.
        _service.enable_retries()
        self.test_delete_build_value_error()

        # Disable retries and run test_delete_build_value_error.
        _service.disable_retries()
        self.test_delete_build_value_error()


class TestUpdateBuild:
    """
    Test Class for update_build
    """

    @responses.activate
    def test_update_build_all_params(self):
        """
        update_build()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/builds/my-build')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "build_v2", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "ready", "status_details": {"reason": "registered"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a BuildPatch model
        build_patch_model = {}
        build_patch_model['output_image'] = 'private.de.icr.io/icr_namespace/image-name'
        build_patch_model['output_secret'] = 'ce-auto-icr-private-eu-de'
        build_patch_model['source_context_dir'] = 'some/subfolder'
        build_patch_model['source_revision'] = 'main'
        build_patch_model['source_secret'] = 'testString'
        build_patch_model['source_type'] = 'git'
        build_patch_model['source_url'] = 'https://github.com/IBM/CodeEngine'
        build_patch_model['strategy_size'] = 'medium'
        build_patch_model['strategy_spec_file'] = 'Dockerfile'
        build_patch_model['strategy_type'] = 'dockerfile'
        build_patch_model['timeout'] = 600

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-build'
        if_match = 'testString'
        build = build_patch_model

        # Invoke method
        response = _service.update_build(
            project_id,
            name,
            if_match,
            build,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == build

    def test_update_build_all_params_with_retries(self):
        # Enable retries and run test_update_build_all_params.
        _service.enable_retries()
        self.test_update_build_all_params()

        # Disable retries and run test_update_build_all_params.
        _service.disable_retries()
        self.test_update_build_all_params()

    @responses.activate
    def test_update_build_value_error(self):
        """
        test_update_build_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/builds/my-build')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "build_v2", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "ready", "status_details": {"reason": "registered"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a BuildPatch model
        build_patch_model = {}
        build_patch_model['output_image'] = 'private.de.icr.io/icr_namespace/image-name'
        build_patch_model['output_secret'] = 'ce-auto-icr-private-eu-de'
        build_patch_model['source_context_dir'] = 'some/subfolder'
        build_patch_model['source_revision'] = 'main'
        build_patch_model['source_secret'] = 'testString'
        build_patch_model['source_type'] = 'git'
        build_patch_model['source_url'] = 'https://github.com/IBM/CodeEngine'
        build_patch_model['strategy_size'] = 'medium'
        build_patch_model['strategy_spec_file'] = 'Dockerfile'
        build_patch_model['strategy_type'] = 'dockerfile'
        build_patch_model['timeout'] = 600

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-build'
        if_match = 'testString'
        build = build_patch_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
            "if_match": if_match,
            "build": build,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_build(**req_copy)

    def test_update_build_value_error_with_retries(self):
        # Enable retries and run test_update_build_value_error.
        _service.enable_retries()
        self.test_update_build_value_error()

        # Disable retries and run test_update_build_value_error.
        _service.disable_retries()
        self.test_update_build_value_error()


class TestListBuildRuns:
    """
    Test Class for list_build_runs
    """

    @responses.activate
    def test_list_build_runs_all_params(self):
        """
        list_build_runs()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/build_runs')
        mock_response = '{"build_runs": [{"build_name": "build_name", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build-run", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "build_run_v2", "service_account": "default", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "succeeded", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "git_branch_name": "main", "git_commit_author": "John Doe", "git_commit_sha": "9a3d845c629d2b4a6b271b1d526dfafc1e7d9511", "output_digest": "sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384", "reason": "succeeded", "source_timestamp": "2022-09-22T17:34:00Z", "start_time": "2022-09-22T17:34:00Z"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        build_name = 'my-build'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_build_runs(
            project_id,
            build_name=build_name,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'build_name={}'.format(build_name) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_build_runs_all_params_with_retries(self):
        # Enable retries and run test_list_build_runs_all_params.
        _service.enable_retries()
        self.test_list_build_runs_all_params()

        # Disable retries and run test_list_build_runs_all_params.
        _service.disable_retries()
        self.test_list_build_runs_all_params()

    @responses.activate
    def test_list_build_runs_required_params(self):
        """
        test_list_build_runs_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/build_runs')
        mock_response = '{"build_runs": [{"build_name": "build_name", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build-run", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "build_run_v2", "service_account": "default", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "succeeded", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "git_branch_name": "main", "git_commit_author": "John Doe", "git_commit_sha": "9a3d845c629d2b4a6b271b1d526dfafc1e7d9511", "output_digest": "sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384", "reason": "succeeded", "source_timestamp": "2022-09-22T17:34:00Z", "start_time": "2022-09-22T17:34:00Z"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.list_build_runs(
            project_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_build_runs_required_params_with_retries(self):
        # Enable retries and run test_list_build_runs_required_params.
        _service.enable_retries()
        self.test_list_build_runs_required_params()

        # Disable retries and run test_list_build_runs_required_params.
        _service.disable_retries()
        self.test_list_build_runs_required_params()

    @responses.activate
    def test_list_build_runs_value_error(self):
        """
        test_list_build_runs_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/build_runs')
        mock_response = '{"build_runs": [{"build_name": "build_name", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build-run", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "build_run_v2", "service_account": "default", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "succeeded", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "git_branch_name": "main", "git_commit_author": "John Doe", "git_commit_sha": "9a3d845c629d2b4a6b271b1d526dfafc1e7d9511", "output_digest": "sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384", "reason": "succeeded", "source_timestamp": "2022-09-22T17:34:00Z", "start_time": "2022-09-22T17:34:00Z"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_build_runs(**req_copy)

    def test_list_build_runs_value_error_with_retries(self):
        # Enable retries and run test_list_build_runs_value_error.
        _service.enable_retries()
        self.test_list_build_runs_value_error()

        # Disable retries and run test_list_build_runs_value_error.
        _service.disable_retries()
        self.test_list_build_runs_value_error()

    @responses.activate
    def test_list_build_runs_with_pager_get_next(self):
        """
        test_list_build_runs_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/build_runs')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"build_runs":[{"build_name":"build_name","created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-build-run","output_image":"private.de.icr.io/icr_namespace/image-name","output_secret":"ce-auto-icr-private-eu-de","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"build_run_v2","service_account":"default","source_context_dir":"some/subfolder","source_revision":"main","source_secret":"source_secret","source_type":"git","source_url":"https://github.com/IBM/CodeEngine","status":"succeeded","status_details":{"completion_time":"2022-09-22T17:40:00Z","git_branch_name":"main","git_commit_author":"John Doe","git_commit_sha":"9a3d845c629d2b4a6b271b1d526dfafc1e7d9511","output_digest":"sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384","reason":"succeeded","source_timestamp":"2022-09-22T17:34:00Z","start_time":"2022-09-22T17:34:00Z"},"strategy_size":"medium","strategy_spec_file":"Dockerfile","strategy_type":"dockerfile","timeout":600}]}'
        mock_response2 = '{"total_count":2,"limit":1,"build_runs":[{"build_name":"build_name","created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-build-run","output_image":"private.de.icr.io/icr_namespace/image-name","output_secret":"ce-auto-icr-private-eu-de","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"build_run_v2","service_account":"default","source_context_dir":"some/subfolder","source_revision":"main","source_secret":"source_secret","source_type":"git","source_url":"https://github.com/IBM/CodeEngine","status":"succeeded","status_details":{"completion_time":"2022-09-22T17:40:00Z","git_branch_name":"main","git_commit_author":"John Doe","git_commit_sha":"9a3d845c629d2b4a6b271b1d526dfafc1e7d9511","output_digest":"sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384","reason":"succeeded","source_timestamp":"2022-09-22T17:34:00Z","start_time":"2022-09-22T17:34:00Z"},"strategy_size":"medium","strategy_spec_file":"Dockerfile","strategy_type":"dockerfile","timeout":600}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = BuildRunsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            build_name='my-build',
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_build_runs_with_pager_get_all(self):
        """
        test_list_build_runs_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/build_runs')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"build_runs":[{"build_name":"build_name","created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-build-run","output_image":"private.de.icr.io/icr_namespace/image-name","output_secret":"ce-auto-icr-private-eu-de","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"build_run_v2","service_account":"default","source_context_dir":"some/subfolder","source_revision":"main","source_secret":"source_secret","source_type":"git","source_url":"https://github.com/IBM/CodeEngine","status":"succeeded","status_details":{"completion_time":"2022-09-22T17:40:00Z","git_branch_name":"main","git_commit_author":"John Doe","git_commit_sha":"9a3d845c629d2b4a6b271b1d526dfafc1e7d9511","output_digest":"sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384","reason":"succeeded","source_timestamp":"2022-09-22T17:34:00Z","start_time":"2022-09-22T17:34:00Z"},"strategy_size":"medium","strategy_spec_file":"Dockerfile","strategy_type":"dockerfile","timeout":600}]}'
        mock_response2 = '{"total_count":2,"limit":1,"build_runs":[{"build_name":"build_name","created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-build-run","output_image":"private.de.icr.io/icr_namespace/image-name","output_secret":"ce-auto-icr-private-eu-de","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"build_run_v2","service_account":"default","source_context_dir":"some/subfolder","source_revision":"main","source_secret":"source_secret","source_type":"git","source_url":"https://github.com/IBM/CodeEngine","status":"succeeded","status_details":{"completion_time":"2022-09-22T17:40:00Z","git_branch_name":"main","git_commit_author":"John Doe","git_commit_sha":"9a3d845c629d2b4a6b271b1d526dfafc1e7d9511","output_digest":"sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384","reason":"succeeded","source_timestamp":"2022-09-22T17:34:00Z","start_time":"2022-09-22T17:34:00Z"},"strategy_size":"medium","strategy_spec_file":"Dockerfile","strategy_type":"dockerfile","timeout":600}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = BuildRunsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            build_name='my-build',
            limit=100,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateBuildRun:
    """
    Test Class for create_build_run
    """

    @responses.activate
    def test_create_build_run_all_params(self):
        """
        create_build_run()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/build_runs')
        mock_response = '{"build_name": "build_name", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build-run", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "build_run_v2", "service_account": "default", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "succeeded", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "git_branch_name": "main", "git_commit_author": "John Doe", "git_commit_sha": "9a3d845c629d2b4a6b271b1d526dfafc1e7d9511", "output_digest": "sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384", "reason": "succeeded", "source_timestamp": "2022-09-22T17:34:00Z", "start_time": "2022-09-22T17:34:00Z"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        build_name = 'testString'
        name = 'testString'
        output_image = 'private.de.icr.io/icr_namespace/image-name'
        output_secret = 'ce-auto-icr-private-eu-de'
        service_account = 'default'
        source_context_dir = 'some/subfolder'
        source_revision = 'main'
        source_secret = 'testString'
        source_type = 'git'
        source_url = 'https://github.com/IBM/CodeEngine'
        strategy_size = 'medium'
        strategy_spec_file = 'Dockerfile'
        strategy_type = 'dockerfile'
        timeout = 600

        # Invoke method
        response = _service.create_build_run(
            project_id,
            build_name=build_name,
            name=name,
            output_image=output_image,
            output_secret=output_secret,
            service_account=service_account,
            source_context_dir=source_context_dir,
            source_revision=source_revision,
            source_secret=source_secret,
            source_type=source_type,
            source_url=source_url,
            strategy_size=strategy_size,
            strategy_spec_file=strategy_spec_file,
            strategy_type=strategy_type,
            timeout=timeout,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['build_name'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['output_image'] == 'private.de.icr.io/icr_namespace/image-name'
        assert req_body['output_secret'] == 'ce-auto-icr-private-eu-de'
        assert req_body['service_account'] == 'default'
        assert req_body['source_context_dir'] == 'some/subfolder'
        assert req_body['source_revision'] == 'main'
        assert req_body['source_secret'] == 'testString'
        assert req_body['source_type'] == 'git'
        assert req_body['source_url'] == 'https://github.com/IBM/CodeEngine'
        assert req_body['strategy_size'] == 'medium'
        assert req_body['strategy_spec_file'] == 'Dockerfile'
        assert req_body['strategy_type'] == 'dockerfile'
        assert req_body['timeout'] == 600

    def test_create_build_run_all_params_with_retries(self):
        # Enable retries and run test_create_build_run_all_params.
        _service.enable_retries()
        self.test_create_build_run_all_params()

        # Disable retries and run test_create_build_run_all_params.
        _service.disable_retries()
        self.test_create_build_run_all_params()

    @responses.activate
    def test_create_build_run_value_error(self):
        """
        test_create_build_run_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/build_runs')
        mock_response = '{"build_name": "build_name", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build-run", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "build_run_v2", "service_account": "default", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "succeeded", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "git_branch_name": "main", "git_commit_author": "John Doe", "git_commit_sha": "9a3d845c629d2b4a6b271b1d526dfafc1e7d9511", "output_digest": "sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384", "reason": "succeeded", "source_timestamp": "2022-09-22T17:34:00Z", "start_time": "2022-09-22T17:34:00Z"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        build_name = 'testString'
        name = 'testString'
        output_image = 'private.de.icr.io/icr_namespace/image-name'
        output_secret = 'ce-auto-icr-private-eu-de'
        service_account = 'default'
        source_context_dir = 'some/subfolder'
        source_revision = 'main'
        source_secret = 'testString'
        source_type = 'git'
        source_url = 'https://github.com/IBM/CodeEngine'
        strategy_size = 'medium'
        strategy_spec_file = 'Dockerfile'
        strategy_type = 'dockerfile'
        timeout = 600

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_build_run(**req_copy)

    def test_create_build_run_value_error_with_retries(self):
        # Enable retries and run test_create_build_run_value_error.
        _service.enable_retries()
        self.test_create_build_run_value_error()

        # Disable retries and run test_create_build_run_value_error.
        _service.disable_retries()
        self.test_create_build_run_value_error()


class TestGetBuildRun:
    """
    Test Class for get_build_run
    """

    @responses.activate
    def test_get_build_run_all_params(self):
        """
        get_build_run()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/build_runs/my-build-run')
        mock_response = '{"build_name": "build_name", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build-run", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "build_run_v2", "service_account": "default", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "succeeded", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "git_branch_name": "main", "git_commit_author": "John Doe", "git_commit_sha": "9a3d845c629d2b4a6b271b1d526dfafc1e7d9511", "output_digest": "sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384", "reason": "succeeded", "source_timestamp": "2022-09-22T17:34:00Z", "start_time": "2022-09-22T17:34:00Z"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-build-run'

        # Invoke method
        response = _service.get_build_run(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_build_run_all_params_with_retries(self):
        # Enable retries and run test_get_build_run_all_params.
        _service.enable_retries()
        self.test_get_build_run_all_params()

        # Disable retries and run test_get_build_run_all_params.
        _service.disable_retries()
        self.test_get_build_run_all_params()

    @responses.activate
    def test_get_build_run_value_error(self):
        """
        test_get_build_run_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/build_runs/my-build-run')
        mock_response = '{"build_name": "build_name", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build-run", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "build_run_v2", "service_account": "default", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "succeeded", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "git_branch_name": "main", "git_commit_author": "John Doe", "git_commit_sha": "9a3d845c629d2b4a6b271b1d526dfafc1e7d9511", "output_digest": "sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384", "reason": "succeeded", "source_timestamp": "2022-09-22T17:34:00Z", "start_time": "2022-09-22T17:34:00Z"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-build-run'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_build_run(**req_copy)

    def test_get_build_run_value_error_with_retries(self):
        # Enable retries and run test_get_build_run_value_error.
        _service.enable_retries()
        self.test_get_build_run_value_error()

        # Disable retries and run test_get_build_run_value_error.
        _service.disable_retries()
        self.test_get_build_run_value_error()


class TestDeleteBuildRun:
    """
    Test Class for delete_build_run
    """

    @responses.activate
    def test_delete_build_run_all_params(self):
        """
        delete_build_run()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/build_runs/my-build-run')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-build-run'

        # Invoke method
        response = _service.delete_build_run(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_build_run_all_params_with_retries(self):
        # Enable retries and run test_delete_build_run_all_params.
        _service.enable_retries()
        self.test_delete_build_run_all_params()

        # Disable retries and run test_delete_build_run_all_params.
        _service.disable_retries()
        self.test_delete_build_run_all_params()

    @responses.activate
    def test_delete_build_run_value_error(self):
        """
        test_delete_build_run_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/build_runs/my-build-run')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-build-run'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_build_run(**req_copy)

    def test_delete_build_run_value_error_with_retries(self):
        # Enable retries and run test_delete_build_run_value_error.
        _service.enable_retries()
        self.test_delete_build_run_value_error()

        # Disable retries and run test_delete_build_run_value_error.
        _service.disable_retries()
        self.test_delete_build_run_value_error()


# endregion
##############################################################################
# End of Service: ImageBuilds
##############################################################################

##############################################################################
# Start of Service: DomainMappings
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = CodeEngineV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CodeEngineV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CodeEngineV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListDomainMappings:
    """
    Test Class for list_domain_mappings
    """

    @responses.activate
    def test_list_domain_mappings_all_params(self):
        """
        list_domain_mappings()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/domain_mappings')
        mock_response = '{"domain_mappings": [{"cname_target": "custom.abcdabcdabc.us-east.codeengine.appdomain.cloud", "component": {"name": "my-app-1", "resource_type": "app_v2"}, "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/domain_mappings/www.example.com", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "www.example.com", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "domain_mapping_v2", "status": "ready", "status_details": {"reason": "ready"}, "tls_secret": "my-tls-secret", "user_managed": true, "visibility": "public"}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_domain_mappings(
            project_id,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_domain_mappings_all_params_with_retries(self):
        # Enable retries and run test_list_domain_mappings_all_params.
        _service.enable_retries()
        self.test_list_domain_mappings_all_params()

        # Disable retries and run test_list_domain_mappings_all_params.
        _service.disable_retries()
        self.test_list_domain_mappings_all_params()

    @responses.activate
    def test_list_domain_mappings_required_params(self):
        """
        test_list_domain_mappings_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/domain_mappings')
        mock_response = '{"domain_mappings": [{"cname_target": "custom.abcdabcdabc.us-east.codeengine.appdomain.cloud", "component": {"name": "my-app-1", "resource_type": "app_v2"}, "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/domain_mappings/www.example.com", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "www.example.com", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "domain_mapping_v2", "status": "ready", "status_details": {"reason": "ready"}, "tls_secret": "my-tls-secret", "user_managed": true, "visibility": "public"}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.list_domain_mappings(
            project_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_domain_mappings_required_params_with_retries(self):
        # Enable retries and run test_list_domain_mappings_required_params.
        _service.enable_retries()
        self.test_list_domain_mappings_required_params()

        # Disable retries and run test_list_domain_mappings_required_params.
        _service.disable_retries()
        self.test_list_domain_mappings_required_params()

    @responses.activate
    def test_list_domain_mappings_value_error(self):
        """
        test_list_domain_mappings_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/domain_mappings')
        mock_response = '{"domain_mappings": [{"cname_target": "custom.abcdabcdabc.us-east.codeengine.appdomain.cloud", "component": {"name": "my-app-1", "resource_type": "app_v2"}, "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/domain_mappings/www.example.com", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "www.example.com", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "domain_mapping_v2", "status": "ready", "status_details": {"reason": "ready"}, "tls_secret": "my-tls-secret", "user_managed": true, "visibility": "public"}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_domain_mappings(**req_copy)

    def test_list_domain_mappings_value_error_with_retries(self):
        # Enable retries and run test_list_domain_mappings_value_error.
        _service.enable_retries()
        self.test_list_domain_mappings_value_error()

        # Disable retries and run test_list_domain_mappings_value_error.
        _service.disable_retries()
        self.test_list_domain_mappings_value_error()

    @responses.activate
    def test_list_domain_mappings_with_pager_get_next(self):
        """
        test_list_domain_mappings_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/domain_mappings')
        mock_response1 = '{"next":{"start":"1"},"domain_mappings":[{"cname_target":"custom.abcdabcdabc.us-east.codeengine.appdomain.cloud","component":{"name":"my-app-1","resource_type":"app_v2"},"created_at":"2022-09-13T11:41:35+02:00","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/domain_mappings/www.example.com","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"www.example.com","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"domain_mapping_v2","status":"ready","status_details":{"reason":"ready"},"tls_secret":"my-tls-secret","user_managed":true,"visibility":"public"}],"total_count":2,"limit":1}'
        mock_response2 = '{"domain_mappings":[{"cname_target":"custom.abcdabcdabc.us-east.codeengine.appdomain.cloud","component":{"name":"my-app-1","resource_type":"app_v2"},"created_at":"2022-09-13T11:41:35+02:00","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/domain_mappings/www.example.com","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"www.example.com","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"domain_mapping_v2","status":"ready","status_details":{"reason":"ready"},"tls_secret":"my-tls-secret","user_managed":true,"visibility":"public"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = DomainMappingsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_domain_mappings_with_pager_get_all(self):
        """
        test_list_domain_mappings_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/domain_mappings')
        mock_response1 = '{"next":{"start":"1"},"domain_mappings":[{"cname_target":"custom.abcdabcdabc.us-east.codeengine.appdomain.cloud","component":{"name":"my-app-1","resource_type":"app_v2"},"created_at":"2022-09-13T11:41:35+02:00","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/domain_mappings/www.example.com","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"www.example.com","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"domain_mapping_v2","status":"ready","status_details":{"reason":"ready"},"tls_secret":"my-tls-secret","user_managed":true,"visibility":"public"}],"total_count":2,"limit":1}'
        mock_response2 = '{"domain_mappings":[{"cname_target":"custom.abcdabcdabc.us-east.codeengine.appdomain.cloud","component":{"name":"my-app-1","resource_type":"app_v2"},"created_at":"2022-09-13T11:41:35+02:00","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/domain_mappings/www.example.com","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"www.example.com","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"domain_mapping_v2","status":"ready","status_details":{"reason":"ready"},"tls_secret":"my-tls-secret","user_managed":true,"visibility":"public"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = DomainMappingsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            limit=100,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateDomainMapping:
    """
    Test Class for create_domain_mapping
    """

    @responses.activate
    def test_create_domain_mapping_all_params(self):
        """
        create_domain_mapping()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/domain_mappings')
        mock_response = '{"cname_target": "custom.abcdabcdabc.us-east.codeengine.appdomain.cloud", "component": {"name": "my-app-1", "resource_type": "app_v2"}, "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/domain_mappings/www.example.com", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "www.example.com", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "domain_mapping_v2", "status": "ready", "status_details": {"reason": "ready"}, "tls_secret": "my-tls-secret", "user_managed": true, "visibility": "public"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ComponentRef model
        component_ref_model = {}
        component_ref_model['name'] = 'my-app-1'
        component_ref_model['resource_type'] = 'app_v2'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        component = component_ref_model
        name = 'www.example.com'
        tls_secret = 'my-tls-secret'

        # Invoke method
        response = _service.create_domain_mapping(
            project_id,
            component,
            name,
            tls_secret,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['component'] == component_ref_model
        assert req_body['name'] == 'www.example.com'
        assert req_body['tls_secret'] == 'my-tls-secret'

    def test_create_domain_mapping_all_params_with_retries(self):
        # Enable retries and run test_create_domain_mapping_all_params.
        _service.enable_retries()
        self.test_create_domain_mapping_all_params()

        # Disable retries and run test_create_domain_mapping_all_params.
        _service.disable_retries()
        self.test_create_domain_mapping_all_params()

    @responses.activate
    def test_create_domain_mapping_value_error(self):
        """
        test_create_domain_mapping_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/domain_mappings')
        mock_response = '{"cname_target": "custom.abcdabcdabc.us-east.codeengine.appdomain.cloud", "component": {"name": "my-app-1", "resource_type": "app_v2"}, "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/domain_mappings/www.example.com", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "www.example.com", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "domain_mapping_v2", "status": "ready", "status_details": {"reason": "ready"}, "tls_secret": "my-tls-secret", "user_managed": true, "visibility": "public"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ComponentRef model
        component_ref_model = {}
        component_ref_model['name'] = 'my-app-1'
        component_ref_model['resource_type'] = 'app_v2'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        component = component_ref_model
        name = 'www.example.com'
        tls_secret = 'my-tls-secret'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "component": component,
            "name": name,
            "tls_secret": tls_secret,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_domain_mapping(**req_copy)

    def test_create_domain_mapping_value_error_with_retries(self):
        # Enable retries and run test_create_domain_mapping_value_error.
        _service.enable_retries()
        self.test_create_domain_mapping_value_error()

        # Disable retries and run test_create_domain_mapping_value_error.
        _service.disable_retries()
        self.test_create_domain_mapping_value_error()


class TestGetDomainMapping:
    """
    Test Class for get_domain_mapping
    """

    @responses.activate
    def test_get_domain_mapping_all_params(self):
        """
        get_domain_mapping()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/domain_mappings/www.example.com')
        mock_response = '{"cname_target": "custom.abcdabcdabc.us-east.codeengine.appdomain.cloud", "component": {"name": "my-app-1", "resource_type": "app_v2"}, "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/domain_mappings/www.example.com", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "www.example.com", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "domain_mapping_v2", "status": "ready", "status_details": {"reason": "ready"}, "tls_secret": "my-tls-secret", "user_managed": true, "visibility": "public"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'www.example.com'

        # Invoke method
        response = _service.get_domain_mapping(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_domain_mapping_all_params_with_retries(self):
        # Enable retries and run test_get_domain_mapping_all_params.
        _service.enable_retries()
        self.test_get_domain_mapping_all_params()

        # Disable retries and run test_get_domain_mapping_all_params.
        _service.disable_retries()
        self.test_get_domain_mapping_all_params()

    @responses.activate
    def test_get_domain_mapping_value_error(self):
        """
        test_get_domain_mapping_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/domain_mappings/www.example.com')
        mock_response = '{"cname_target": "custom.abcdabcdabc.us-east.codeengine.appdomain.cloud", "component": {"name": "my-app-1", "resource_type": "app_v2"}, "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/domain_mappings/www.example.com", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "www.example.com", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "domain_mapping_v2", "status": "ready", "status_details": {"reason": "ready"}, "tls_secret": "my-tls-secret", "user_managed": true, "visibility": "public"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'www.example.com'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_domain_mapping(**req_copy)

    def test_get_domain_mapping_value_error_with_retries(self):
        # Enable retries and run test_get_domain_mapping_value_error.
        _service.enable_retries()
        self.test_get_domain_mapping_value_error()

        # Disable retries and run test_get_domain_mapping_value_error.
        _service.disable_retries()
        self.test_get_domain_mapping_value_error()


class TestDeleteDomainMapping:
    """
    Test Class for delete_domain_mapping
    """

    @responses.activate
    def test_delete_domain_mapping_all_params(self):
        """
        delete_domain_mapping()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/domain_mappings/www.example.com')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'www.example.com'

        # Invoke method
        response = _service.delete_domain_mapping(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_domain_mapping_all_params_with_retries(self):
        # Enable retries and run test_delete_domain_mapping_all_params.
        _service.enable_retries()
        self.test_delete_domain_mapping_all_params()

        # Disable retries and run test_delete_domain_mapping_all_params.
        _service.disable_retries()
        self.test_delete_domain_mapping_all_params()

    @responses.activate
    def test_delete_domain_mapping_value_error(self):
        """
        test_delete_domain_mapping_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/domain_mappings/www.example.com')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'www.example.com'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_domain_mapping(**req_copy)

    def test_delete_domain_mapping_value_error_with_retries(self):
        # Enable retries and run test_delete_domain_mapping_value_error.
        _service.enable_retries()
        self.test_delete_domain_mapping_value_error()

        # Disable retries and run test_delete_domain_mapping_value_error.
        _service.disable_retries()
        self.test_delete_domain_mapping_value_error()


class TestUpdateDomainMapping:
    """
    Test Class for update_domain_mapping
    """

    @responses.activate
    def test_update_domain_mapping_all_params(self):
        """
        update_domain_mapping()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/domain_mappings/www.example.com')
        mock_response = '{"cname_target": "custom.abcdabcdabc.us-east.codeengine.appdomain.cloud", "component": {"name": "my-app-1", "resource_type": "app_v2"}, "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/domain_mappings/www.example.com", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "www.example.com", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "domain_mapping_v2", "status": "ready", "status_details": {"reason": "ready"}, "tls_secret": "my-tls-secret", "user_managed": true, "visibility": "public"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ComponentRef model
        component_ref_model = {}
        component_ref_model['name'] = 'my-app-1'
        component_ref_model['resource_type'] = 'app_v2'

        # Construct a dict representation of a DomainMappingPatch model
        domain_mapping_patch_model = {}
        domain_mapping_patch_model['component'] = component_ref_model
        domain_mapping_patch_model['tls_secret'] = 'my-tls-secret'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'www.example.com'
        if_match = 'testString'
        domain_mapping = domain_mapping_patch_model

        # Invoke method
        response = _service.update_domain_mapping(
            project_id,
            name,
            if_match,
            domain_mapping,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == domain_mapping

    def test_update_domain_mapping_all_params_with_retries(self):
        # Enable retries and run test_update_domain_mapping_all_params.
        _service.enable_retries()
        self.test_update_domain_mapping_all_params()

        # Disable retries and run test_update_domain_mapping_all_params.
        _service.disable_retries()
        self.test_update_domain_mapping_all_params()

    @responses.activate
    def test_update_domain_mapping_value_error(self):
        """
        test_update_domain_mapping_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/domain_mappings/www.example.com')
        mock_response = '{"cname_target": "custom.abcdabcdabc.us-east.codeengine.appdomain.cloud", "component": {"name": "my-app-1", "resource_type": "app_v2"}, "created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/domain_mappings/www.example.com", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "www.example.com", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "domain_mapping_v2", "status": "ready", "status_details": {"reason": "ready"}, "tls_secret": "my-tls-secret", "user_managed": true, "visibility": "public"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ComponentRef model
        component_ref_model = {}
        component_ref_model['name'] = 'my-app-1'
        component_ref_model['resource_type'] = 'app_v2'

        # Construct a dict representation of a DomainMappingPatch model
        domain_mapping_patch_model = {}
        domain_mapping_patch_model['component'] = component_ref_model
        domain_mapping_patch_model['tls_secret'] = 'my-tls-secret'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'www.example.com'
        if_match = 'testString'
        domain_mapping = domain_mapping_patch_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
            "if_match": if_match,
            "domain_mapping": domain_mapping,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_domain_mapping(**req_copy)

    def test_update_domain_mapping_value_error_with_retries(self):
        # Enable retries and run test_update_domain_mapping_value_error.
        _service.enable_retries()
        self.test_update_domain_mapping_value_error()

        # Disable retries and run test_update_domain_mapping_value_error.
        _service.disable_retries()
        self.test_update_domain_mapping_value_error()


# endregion
##############################################################################
# End of Service: DomainMappings
##############################################################################

##############################################################################
# Start of Service: SecretsAndConfigmaps
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = CodeEngineV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CodeEngineV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CodeEngineV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListConfigMaps:
    """
    Test Class for list_config_maps
    """

    @responses.activate
    def test_list_config_maps_all_params(self):
        """
        list_config_maps()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/config_maps')
        mock_response = '{"config_maps": [{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-config-map", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "config_map_v2"}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_config_maps(
            project_id,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_config_maps_all_params_with_retries(self):
        # Enable retries and run test_list_config_maps_all_params.
        _service.enable_retries()
        self.test_list_config_maps_all_params()

        # Disable retries and run test_list_config_maps_all_params.
        _service.disable_retries()
        self.test_list_config_maps_all_params()

    @responses.activate
    def test_list_config_maps_required_params(self):
        """
        test_list_config_maps_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/config_maps')
        mock_response = '{"config_maps": [{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-config-map", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "config_map_v2"}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.list_config_maps(
            project_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_config_maps_required_params_with_retries(self):
        # Enable retries and run test_list_config_maps_required_params.
        _service.enable_retries()
        self.test_list_config_maps_required_params()

        # Disable retries and run test_list_config_maps_required_params.
        _service.disable_retries()
        self.test_list_config_maps_required_params()

    @responses.activate
    def test_list_config_maps_value_error(self):
        """
        test_list_config_maps_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/config_maps')
        mock_response = '{"config_maps": [{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-config-map", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "config_map_v2"}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_config_maps(**req_copy)

    def test_list_config_maps_value_error_with_retries(self):
        # Enable retries and run test_list_config_maps_value_error.
        _service.enable_retries()
        self.test_list_config_maps_value_error()

        # Disable retries and run test_list_config_maps_value_error.
        _service.disable_retries()
        self.test_list_config_maps_value_error()

    @responses.activate
    def test_list_config_maps_with_pager_get_next(self):
        """
        test_list_config_maps_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/config_maps')
        mock_response1 = '{"next":{"start":"1"},"config_maps":[{"created_at":"2022-09-13T11:41:35+02:00","data":{"mapKey":"inner"},"entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-config-map","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"config_map_v2"}],"total_count":2,"limit":1}'
        mock_response2 = '{"config_maps":[{"created_at":"2022-09-13T11:41:35+02:00","data":{"mapKey":"inner"},"entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-config-map","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"config_map_v2"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = ConfigMapsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_config_maps_with_pager_get_all(self):
        """
        test_list_config_maps_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/config_maps')
        mock_response1 = '{"next":{"start":"1"},"config_maps":[{"created_at":"2022-09-13T11:41:35+02:00","data":{"mapKey":"inner"},"entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-config-map","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"config_map_v2"}],"total_count":2,"limit":1}'
        mock_response2 = '{"config_maps":[{"created_at":"2022-09-13T11:41:35+02:00","data":{"mapKey":"inner"},"entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-config-map","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"config_map_v2"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = ConfigMapsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            limit=100,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateConfigMap:
    """
    Test Class for create_config_map
    """

    @responses.activate
    def test_create_config_map_all_params(self):
        """
        create_config_map()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/config_maps')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-config-map", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "config_map_v2"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-config-map'
        data = {'key1': 'testString'}

        # Invoke method
        response = _service.create_config_map(
            project_id,
            name,
            data=data,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'my-config-map'
        assert req_body['data'] == {'key1': 'testString'}

    def test_create_config_map_all_params_with_retries(self):
        # Enable retries and run test_create_config_map_all_params.
        _service.enable_retries()
        self.test_create_config_map_all_params()

        # Disable retries and run test_create_config_map_all_params.
        _service.disable_retries()
        self.test_create_config_map_all_params()

    @responses.activate
    def test_create_config_map_value_error(self):
        """
        test_create_config_map_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/config_maps')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-config-map", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "config_map_v2"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-config-map'
        data = {'key1': 'testString'}

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_config_map(**req_copy)

    def test_create_config_map_value_error_with_retries(self):
        # Enable retries and run test_create_config_map_value_error.
        _service.enable_retries()
        self.test_create_config_map_value_error()

        # Disable retries and run test_create_config_map_value_error.
        _service.disable_retries()
        self.test_create_config_map_value_error()


class TestGetConfigMap:
    """
    Test Class for get_config_map
    """

    @responses.activate
    def test_get_config_map_all_params(self):
        """
        get_config_map()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/config_maps/my-config-map')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-config-map", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "config_map_v2"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-config-map'

        # Invoke method
        response = _service.get_config_map(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_config_map_all_params_with_retries(self):
        # Enable retries and run test_get_config_map_all_params.
        _service.enable_retries()
        self.test_get_config_map_all_params()

        # Disable retries and run test_get_config_map_all_params.
        _service.disable_retries()
        self.test_get_config_map_all_params()

    @responses.activate
    def test_get_config_map_value_error(self):
        """
        test_get_config_map_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/config_maps/my-config-map')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-config-map", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "config_map_v2"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-config-map'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_config_map(**req_copy)

    def test_get_config_map_value_error_with_retries(self):
        # Enable retries and run test_get_config_map_value_error.
        _service.enable_retries()
        self.test_get_config_map_value_error()

        # Disable retries and run test_get_config_map_value_error.
        _service.disable_retries()
        self.test_get_config_map_value_error()


class TestReplaceConfigMap:
    """
    Test Class for replace_config_map
    """

    @responses.activate
    def test_replace_config_map_all_params(self):
        """
        replace_config_map()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/config_maps/my-config-map')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-config-map", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "config_map_v2"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-config-map'
        if_match = 'testString'
        data = {'key1': 'testString'}

        # Invoke method
        response = _service.replace_config_map(
            project_id,
            name,
            if_match,
            data=data,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['data'] == {'key1': 'testString'}

    def test_replace_config_map_all_params_with_retries(self):
        # Enable retries and run test_replace_config_map_all_params.
        _service.enable_retries()
        self.test_replace_config_map_all_params()

        # Disable retries and run test_replace_config_map_all_params.
        _service.disable_retries()
        self.test_replace_config_map_all_params()

    @responses.activate
    def test_replace_config_map_value_error(self):
        """
        test_replace_config_map_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/config_maps/my-config-map')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-config-map", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "config_map_v2"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-config-map'
        if_match = 'testString'
        data = {'key1': 'testString'}

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
            "if_match": if_match,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_config_map(**req_copy)

    def test_replace_config_map_value_error_with_retries(self):
        # Enable retries and run test_replace_config_map_value_error.
        _service.enable_retries()
        self.test_replace_config_map_value_error()

        # Disable retries and run test_replace_config_map_value_error.
        _service.disable_retries()
        self.test_replace_config_map_value_error()


class TestDeleteConfigMap:
    """
    Test Class for delete_config_map
    """

    @responses.activate
    def test_delete_config_map_all_params(self):
        """
        delete_config_map()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/config_maps/my-config-map')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-config-map'

        # Invoke method
        response = _service.delete_config_map(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_config_map_all_params_with_retries(self):
        # Enable retries and run test_delete_config_map_all_params.
        _service.enable_retries()
        self.test_delete_config_map_all_params()

        # Disable retries and run test_delete_config_map_all_params.
        _service.disable_retries()
        self.test_delete_config_map_all_params()

    @responses.activate
    def test_delete_config_map_value_error(self):
        """
        test_delete_config_map_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/config_maps/my-config-map')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-config-map'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_config_map(**req_copy)

    def test_delete_config_map_value_error_with_retries(self):
        # Enable retries and run test_delete_config_map_value_error.
        _service.enable_retries()
        self.test_delete_config_map_value_error()

        # Disable retries and run test_delete_config_map_value_error.
        _service.disable_retries()
        self.test_delete_config_map_value_error()


class TestListSecrets:
    """
    Test Class for list_secrets
    """

    @responses.activate
    def test_list_secrets_all_params(self):
        """
        list_secrets()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/secrets')
        mock_response = '{"first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}, "secrets": [{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "format": "generic", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-secret", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "resource_type", "service_access": {"resource_key": {"id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "name": "name"}, "role": {"crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer", "name": "Manager"}, "service_instance": {"id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "type": "type"}, "serviceid": {"crn": "crn", "id": "ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}}, "service_operator": {"apikey_id": "ApiKey-17041d26-55e4-40a8-8ab5-5a69b68e204b", "resource_group_ids": ["resource_group_ids"], "serviceid": {"crn": "crn", "id": "ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}, "user_managed": true}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_secrets(
            project_id,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_secrets_all_params_with_retries(self):
        # Enable retries and run test_list_secrets_all_params.
        _service.enable_retries()
        self.test_list_secrets_all_params()

        # Disable retries and run test_list_secrets_all_params.
        _service.disable_retries()
        self.test_list_secrets_all_params()

    @responses.activate
    def test_list_secrets_required_params(self):
        """
        test_list_secrets_required_params()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/secrets')
        mock_response = '{"first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}, "secrets": [{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "format": "generic", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-secret", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "resource_type", "service_access": {"resource_key": {"id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "name": "name"}, "role": {"crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer", "name": "Manager"}, "service_instance": {"id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "type": "type"}, "serviceid": {"crn": "crn", "id": "ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}}, "service_operator": {"apikey_id": "ApiKey-17041d26-55e4-40a8-8ab5-5a69b68e204b", "resource_group_ids": ["resource_group_ids"], "serviceid": {"crn": "crn", "id": "ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}, "user_managed": true}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.list_secrets(
            project_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_secrets_required_params_with_retries(self):
        # Enable retries and run test_list_secrets_required_params.
        _service.enable_retries()
        self.test_list_secrets_required_params()

        # Disable retries and run test_list_secrets_required_params.
        _service.disable_retries()
        self.test_list_secrets_required_params()

    @responses.activate
    def test_list_secrets_value_error(self):
        """
        test_list_secrets_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/secrets')
        mock_response = '{"first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}, "secrets": [{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "format": "generic", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-secret", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "resource_type", "service_access": {"resource_key": {"id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "name": "name"}, "role": {"crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer", "name": "Manager"}, "service_instance": {"id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "type": "type"}, "serviceid": {"crn": "crn", "id": "ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}}, "service_operator": {"apikey_id": "ApiKey-17041d26-55e4-40a8-8ab5-5a69b68e204b", "resource_group_ids": ["resource_group_ids"], "serviceid": {"crn": "crn", "id": "ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}, "user_managed": true}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_secrets(**req_copy)

    def test_list_secrets_value_error_with_retries(self):
        # Enable retries and run test_list_secrets_value_error.
        _service.enable_retries()
        self.test_list_secrets_value_error()

        # Disable retries and run test_list_secrets_value_error.
        _service.disable_retries()
        self.test_list_secrets_value_error()

    @responses.activate
    def test_list_secrets_with_pager_get_next(self):
        """
        test_list_secrets_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/secrets')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"secrets":[{"created_at":"2022-09-13T11:41:35+02:00","data":{"mapKey":"inner"},"entity_tag":"2385407409","format":"generic","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-secret","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"resource_type","service_access":{"resource_key":{"id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","name":"name"},"role":{"crn":"crn:v1:bluemix:public:iam::::serviceRole:Writer","name":"Manager"},"service_instance":{"id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","type":"type"},"serviceid":{"crn":"crn","id":"ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}},"service_operator":{"apikey_id":"ApiKey-17041d26-55e4-40a8-8ab5-5a69b68e204b","resource_group_ids":["resource_group_ids"],"serviceid":{"crn":"crn","id":"ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"},"user_managed":true}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"secrets":[{"created_at":"2022-09-13T11:41:35+02:00","data":{"mapKey":"inner"},"entity_tag":"2385407409","format":"generic","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-secret","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"resource_type","service_access":{"resource_key":{"id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","name":"name"},"role":{"crn":"crn:v1:bluemix:public:iam::::serviceRole:Writer","name":"Manager"},"service_instance":{"id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","type":"type"},"serviceid":{"crn":"crn","id":"ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}},"service_operator":{"apikey_id":"ApiKey-17041d26-55e4-40a8-8ab5-5a69b68e204b","resource_group_ids":["resource_group_ids"],"serviceid":{"crn":"crn","id":"ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"},"user_managed":true}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = SecretsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_secrets_with_pager_get_all(self):
        """
        test_list_secrets_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/secrets')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"secrets":[{"created_at":"2022-09-13T11:41:35+02:00","data":{"mapKey":"inner"},"entity_tag":"2385407409","format":"generic","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-secret","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"resource_type","service_access":{"resource_key":{"id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","name":"name"},"role":{"crn":"crn:v1:bluemix:public:iam::::serviceRole:Writer","name":"Manager"},"service_instance":{"id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","type":"type"},"serviceid":{"crn":"crn","id":"ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}},"service_operator":{"apikey_id":"ApiKey-17041d26-55e4-40a8-8ab5-5a69b68e204b","resource_group_ids":["resource_group_ids"],"serviceid":{"crn":"crn","id":"ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"},"user_managed":true}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"secrets":[{"created_at":"2022-09-13T11:41:35+02:00","data":{"mapKey":"inner"},"entity_tag":"2385407409","format":"generic","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-secret","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","region":"us-east","resource_type":"resource_type","service_access":{"resource_key":{"id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","name":"name"},"role":{"crn":"crn:v1:bluemix:public:iam::::serviceRole:Writer","name":"Manager"},"service_instance":{"id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","type":"type"},"serviceid":{"crn":"crn","id":"ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}},"service_operator":{"apikey_id":"ApiKey-17041d26-55e4-40a8-8ab5-5a69b68e204b","resource_group_ids":["resource_group_ids"],"serviceid":{"crn":"crn","id":"ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"},"user_managed":true}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = SecretsPager(
            client=_service,
            project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            limit=100,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateSecret:
    """
    Test Class for create_secret
    """

    @responses.activate
    def test_create_secret_all_params(self):
        """
        create_secret()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/secrets')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "format": "generic", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-secret", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "resource_type", "service_access": {"resource_key": {"id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "name": "name"}, "role": {"crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer", "name": "Manager"}, "service_instance": {"id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "type": "type"}, "serviceid": {"crn": "crn", "id": "ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}}, "service_operator": {"apikey_id": "ApiKey-17041d26-55e4-40a8-8ab5-5a69b68e204b", "resource_group_ids": ["resource_group_ids"], "serviceid": {"crn": "crn", "id": "ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}, "user_managed": true}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a SecretDataGenericSecretData model
        secret_data_model = {}
        secret_data_model['foo'] = 'testString'

        # Construct a dict representation of a ResourceKeyRefPrototype model
        resource_key_ref_prototype_model = {}
        resource_key_ref_prototype_model['id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'

        # Construct a dict representation of a RoleRefPrototype model
        role_ref_prototype_model = {}
        role_ref_prototype_model['crn'] = 'crn:v1:bluemix:public:iam::::serviceRole:Writer'

        # Construct a dict representation of a ServiceInstanceRefPrototype model
        service_instance_ref_prototype_model = {}
        service_instance_ref_prototype_model['id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'

        # Construct a dict representation of a ServiceIDRef model
        service_id_ref_model = {}
        service_id_ref_model['crn'] = 'testString'
        service_id_ref_model['id'] = 'ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637'

        # Construct a dict representation of a ServiceAccessSecretPrototypeProps model
        service_access_secret_prototype_props_model = {}
        service_access_secret_prototype_props_model['resource_key'] = resource_key_ref_prototype_model
        service_access_secret_prototype_props_model['role'] = role_ref_prototype_model
        service_access_secret_prototype_props_model['service_instance'] = service_instance_ref_prototype_model
        service_access_secret_prototype_props_model['serviceid'] = service_id_ref_model

        # Construct a dict representation of a ServiceIDRefPrototype model
        service_id_ref_prototype_model = {}
        service_id_ref_prototype_model['id'] = 'ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637'

        # Construct a dict representation of a OperatorSecretPrototypeProps model
        operator_secret_prototype_props_model = {}
        operator_secret_prototype_props_model['resource_group_ids'] = ['testString']
        operator_secret_prototype_props_model['serviceid'] = service_id_ref_prototype_model

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        format = 'generic'
        name = 'my-secret'
        data = secret_data_model
        service_access = service_access_secret_prototype_props_model
        service_operator = operator_secret_prototype_props_model

        # Invoke method
        response = _service.create_secret(
            project_id,
            format,
            name,
            data=data,
            service_access=service_access,
            service_operator=service_operator,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['format'] == 'generic'
        assert req_body['name'] == 'my-secret'
        assert req_body['data'] == secret_data_model
        assert req_body['service_access'] == service_access_secret_prototype_props_model
        assert req_body['service_operator'] == operator_secret_prototype_props_model

    def test_create_secret_all_params_with_retries(self):
        # Enable retries and run test_create_secret_all_params.
        _service.enable_retries()
        self.test_create_secret_all_params()

        # Disable retries and run test_create_secret_all_params.
        _service.disable_retries()
        self.test_create_secret_all_params()

    @responses.activate
    def test_create_secret_value_error(self):
        """
        test_create_secret_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/secrets')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "format": "generic", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-secret", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "resource_type", "service_access": {"resource_key": {"id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "name": "name"}, "role": {"crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer", "name": "Manager"}, "service_instance": {"id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "type": "type"}, "serviceid": {"crn": "crn", "id": "ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}}, "service_operator": {"apikey_id": "ApiKey-17041d26-55e4-40a8-8ab5-5a69b68e204b", "resource_group_ids": ["resource_group_ids"], "serviceid": {"crn": "crn", "id": "ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}, "user_managed": true}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a SecretDataGenericSecretData model
        secret_data_model = {}
        secret_data_model['foo'] = 'testString'

        # Construct a dict representation of a ResourceKeyRefPrototype model
        resource_key_ref_prototype_model = {}
        resource_key_ref_prototype_model['id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'

        # Construct a dict representation of a RoleRefPrototype model
        role_ref_prototype_model = {}
        role_ref_prototype_model['crn'] = 'crn:v1:bluemix:public:iam::::serviceRole:Writer'

        # Construct a dict representation of a ServiceInstanceRefPrototype model
        service_instance_ref_prototype_model = {}
        service_instance_ref_prototype_model['id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'

        # Construct a dict representation of a ServiceIDRef model
        service_id_ref_model = {}
        service_id_ref_model['crn'] = 'testString'
        service_id_ref_model['id'] = 'ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637'

        # Construct a dict representation of a ServiceAccessSecretPrototypeProps model
        service_access_secret_prototype_props_model = {}
        service_access_secret_prototype_props_model['resource_key'] = resource_key_ref_prototype_model
        service_access_secret_prototype_props_model['role'] = role_ref_prototype_model
        service_access_secret_prototype_props_model['service_instance'] = service_instance_ref_prototype_model
        service_access_secret_prototype_props_model['serviceid'] = service_id_ref_model

        # Construct a dict representation of a ServiceIDRefPrototype model
        service_id_ref_prototype_model = {}
        service_id_ref_prototype_model['id'] = 'ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637'

        # Construct a dict representation of a OperatorSecretPrototypeProps model
        operator_secret_prototype_props_model = {}
        operator_secret_prototype_props_model['resource_group_ids'] = ['testString']
        operator_secret_prototype_props_model['serviceid'] = service_id_ref_prototype_model

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        format = 'generic'
        name = 'my-secret'
        data = secret_data_model
        service_access = service_access_secret_prototype_props_model
        service_operator = operator_secret_prototype_props_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "format": format,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_secret(**req_copy)

    def test_create_secret_value_error_with_retries(self):
        # Enable retries and run test_create_secret_value_error.
        _service.enable_retries()
        self.test_create_secret_value_error()

        # Disable retries and run test_create_secret_value_error.
        _service.disable_retries()
        self.test_create_secret_value_error()


class TestGetSecret:
    """
    Test Class for get_secret
    """

    @responses.activate
    def test_get_secret_all_params(self):
        """
        get_secret()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/secrets/my-secret')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "format": "generic", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-secret", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "resource_type", "service_access": {"resource_key": {"id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "name": "name"}, "role": {"crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer", "name": "Manager"}, "service_instance": {"id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "type": "type"}, "serviceid": {"crn": "crn", "id": "ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}}, "service_operator": {"apikey_id": "ApiKey-17041d26-55e4-40a8-8ab5-5a69b68e204b", "resource_group_ids": ["resource_group_ids"], "serviceid": {"crn": "crn", "id": "ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}, "user_managed": true}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-secret'

        # Invoke method
        response = _service.get_secret(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_secret_all_params_with_retries(self):
        # Enable retries and run test_get_secret_all_params.
        _service.enable_retries()
        self.test_get_secret_all_params()

        # Disable retries and run test_get_secret_all_params.
        _service.disable_retries()
        self.test_get_secret_all_params()

    @responses.activate
    def test_get_secret_value_error(self):
        """
        test_get_secret_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/secrets/my-secret')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "format": "generic", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-secret", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "resource_type", "service_access": {"resource_key": {"id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "name": "name"}, "role": {"crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer", "name": "Manager"}, "service_instance": {"id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "type": "type"}, "serviceid": {"crn": "crn", "id": "ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}}, "service_operator": {"apikey_id": "ApiKey-17041d26-55e4-40a8-8ab5-5a69b68e204b", "resource_group_ids": ["resource_group_ids"], "serviceid": {"crn": "crn", "id": "ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}, "user_managed": true}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-secret'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_secret(**req_copy)

    def test_get_secret_value_error_with_retries(self):
        # Enable retries and run test_get_secret_value_error.
        _service.enable_retries()
        self.test_get_secret_value_error()

        # Disable retries and run test_get_secret_value_error.
        _service.disable_retries()
        self.test_get_secret_value_error()


class TestReplaceSecret:
    """
    Test Class for replace_secret
    """

    @responses.activate
    def test_replace_secret_all_params(self):
        """
        replace_secret()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/secrets/my-secret')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "format": "generic", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-secret", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "resource_type", "service_access": {"resource_key": {"id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "name": "name"}, "role": {"crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer", "name": "Manager"}, "service_instance": {"id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "type": "type"}, "serviceid": {"crn": "crn", "id": "ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}}, "service_operator": {"apikey_id": "ApiKey-17041d26-55e4-40a8-8ab5-5a69b68e204b", "resource_group_ids": ["resource_group_ids"], "serviceid": {"crn": "crn", "id": "ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}, "user_managed": true}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a SecretDataGenericSecretData model
        secret_data_model = {}
        secret_data_model['foo'] = 'testString'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-secret'
        if_match = 'testString'
        format = 'generic'
        data = secret_data_model

        # Invoke method
        response = _service.replace_secret(
            project_id,
            name,
            if_match,
            format,
            data=data,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['format'] == 'generic'
        assert req_body['data'] == secret_data_model

    def test_replace_secret_all_params_with_retries(self):
        # Enable retries and run test_replace_secret_all_params.
        _service.enable_retries()
        self.test_replace_secret_all_params()

        # Disable retries and run test_replace_secret_all_params.
        _service.disable_retries()
        self.test_replace_secret_all_params()

    @responses.activate
    def test_replace_secret_value_error(self):
        """
        test_replace_secret_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/secrets/my-secret')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "format": "generic", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-secret", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "region": "us-east", "resource_type": "resource_type", "service_access": {"resource_key": {"id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "name": "name"}, "role": {"crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer", "name": "Manager"}, "service_instance": {"id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "type": "type"}, "serviceid": {"crn": "crn", "id": "ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}}, "service_operator": {"apikey_id": "ApiKey-17041d26-55e4-40a8-8ab5-5a69b68e204b", "resource_group_ids": ["resource_group_ids"], "serviceid": {"crn": "crn", "id": "ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637"}, "user_managed": true}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a SecretDataGenericSecretData model
        secret_data_model = {}
        secret_data_model['foo'] = 'testString'

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-secret'
        if_match = 'testString'
        format = 'generic'
        data = secret_data_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
            "if_match": if_match,
            "format": format,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_secret(**req_copy)

    def test_replace_secret_value_error_with_retries(self):
        # Enable retries and run test_replace_secret_value_error.
        _service.enable_retries()
        self.test_replace_secret_value_error()

        # Disable retries and run test_replace_secret_value_error.
        _service.disable_retries()
        self.test_replace_secret_value_error()


class TestDeleteSecret:
    """
    Test Class for delete_secret
    """

    @responses.activate
    def test_delete_secret_all_params(self):
        """
        delete_secret()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/secrets/my-secret')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-secret'

        # Invoke method
        response = _service.delete_secret(
            project_id,
            name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_secret_all_params_with_retries(self):
        # Enable retries and run test_delete_secret_all_params.
        _service.enable_retries()
        self.test_delete_secret_all_params()

        # Disable retries and run test_delete_secret_all_params.
        _service.disable_retries()
        self.test_delete_secret_all_params()

    @responses.activate
    def test_delete_secret_value_error(self):
        """
        test_delete_secret_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/secrets/my-secret')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-secret'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_secret(**req_copy)

    def test_delete_secret_value_error_with_retries(self):
        # Enable retries and run test_delete_secret_value_error.
        _service.enable_retries()
        self.test_delete_secret_value_error()

        # Disable retries and run test_delete_secret_value_error.
        _service.disable_retries()
        self.test_delete_secret_value_error()


# endregion
##############################################################################
# End of Service: SecretsAndConfigmaps
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_AllowedOutboundDestinationList:
    """
    Test Class for AllowedOutboundDestinationList
    """

    def test_allowed_outbound_destination_list_serialization(self):
        """
        Test serialization/deserialization for AllowedOutboundDestinationList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        allowed_outbound_destination_model = {}  # AllowedOutboundDestinationCidrBlockData
        allowed_outbound_destination_model['entity_tag'] = '2385407409'
        allowed_outbound_destination_model['type'] = 'cidr_block'
        allowed_outbound_destination_model['cidr_block'] = '192.68.3.0/24'
        allowed_outbound_destination_model['name'] = 'my-cidr-block'

        list_first_metadata_model = {}  # ListFirstMetadata
        list_first_metadata_model['href'] = 'testString'

        list_next_metadata_model = {}  # ListNextMetadata
        list_next_metadata_model['href'] = 'testString'
        list_next_metadata_model['start'] = 'testString'

        # Construct a json representation of a AllowedOutboundDestinationList model
        allowed_outbound_destination_list_model_json = {}
        allowed_outbound_destination_list_model_json['allowed_outbound_destinations'] = [
            allowed_outbound_destination_model
        ]
        allowed_outbound_destination_list_model_json['first'] = list_first_metadata_model
        allowed_outbound_destination_list_model_json['limit'] = 100
        allowed_outbound_destination_list_model_json['next'] = list_next_metadata_model

        # Construct a model instance of AllowedOutboundDestinationList by calling from_dict on the json representation
        allowed_outbound_destination_list_model = AllowedOutboundDestinationList.from_dict(
            allowed_outbound_destination_list_model_json
        )
        assert allowed_outbound_destination_list_model != False

        # Construct a model instance of AllowedOutboundDestinationList by calling from_dict on the json representation
        allowed_outbound_destination_list_model_dict = AllowedOutboundDestinationList.from_dict(
            allowed_outbound_destination_list_model_json
        ).__dict__
        allowed_outbound_destination_list_model2 = AllowedOutboundDestinationList(
            **allowed_outbound_destination_list_model_dict
        )

        # Verify the model instances are equivalent
        assert allowed_outbound_destination_list_model == allowed_outbound_destination_list_model2

        # Convert model instance back to dict and verify no loss of data
        allowed_outbound_destination_list_model_json2 = allowed_outbound_destination_list_model.to_dict()
        assert allowed_outbound_destination_list_model_json2 == allowed_outbound_destination_list_model_json


class TestModel_App:
    """
    Test Class for App
    """

    def test_app_serialization(self):
        """
        Test serialization/deserialization for App
        """

        # Construct dict forms of any model objects needed in order to build this model.

        env_var_model = {}  # EnvVar
        env_var_model['key'] = 'MY_VARIABLE'
        env_var_model['name'] = 'SOME'
        env_var_model['prefix'] = 'PREFIX_'
        env_var_model['reference'] = 'my-secret'
        env_var_model['type'] = 'literal'
        env_var_model['value'] = 'VALUE'

        probe_model = {}  # Probe
        probe_model['failure_threshold'] = 5
        probe_model['initial_delay'] = 5
        probe_model['interval'] = 5
        probe_model['path'] = 'testString'
        probe_model['port'] = 8080
        probe_model['timeout'] = 300
        probe_model['type'] = 'tcp'

        volume_mount_model = {}  # VolumeMount
        volume_mount_model['mount_path'] = '/app'
        volume_mount_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_model['reference'] = 'my-secret'
        volume_mount_model['type'] = 'secret'

        app_status_model = {}  # AppStatus

        # Construct a json representation of a App model
        app_model_json = {}
        app_model_json['computed_env_variables'] = [env_var_model]
        app_model_json['entity_tag'] = '2385407409'
        app_model_json['image_port'] = 8080
        app_model_json['image_reference'] = 'icr.io/codeengine/helloworld'
        app_model_json['image_secret'] = 'my-secret'
        app_model_json['managed_domain_mappings'] = 'local_public'
        app_model_json['name'] = 'my-app'
        app_model_json['probe_liveness'] = probe_model
        app_model_json['probe_readiness'] = probe_model
        app_model_json['run_arguments'] = ['testString']
        app_model_json['run_as_user'] = 1001
        app_model_json['run_commands'] = ['testString']
        app_model_json['run_env_variables'] = [env_var_model]
        app_model_json['run_service_account'] = 'default'
        app_model_json['run_volume_mounts'] = [volume_mount_model]
        app_model_json['scale_concurrency'] = 100
        app_model_json['scale_concurrency_target'] = 80
        app_model_json['scale_cpu_limit'] = '1'
        app_model_json['scale_down_delay'] = 300
        app_model_json['scale_ephemeral_storage_limit'] = '4G'
        app_model_json['scale_initial_instances'] = 1
        app_model_json['scale_max_instances'] = 10
        app_model_json['scale_memory_limit'] = '4G'
        app_model_json['scale_min_instances'] = 1
        app_model_json['scale_request_timeout'] = 300
        app_model_json['status_details'] = app_status_model

        # Construct a model instance of App by calling from_dict on the json representation
        app_model = App.from_dict(app_model_json)
        assert app_model != False

        # Construct a model instance of App by calling from_dict on the json representation
        app_model_dict = App.from_dict(app_model_json).__dict__
        app_model2 = App(**app_model_dict)

        # Verify the model instances are equivalent
        assert app_model == app_model2

        # Convert model instance back to dict and verify no loss of data
        app_model_json2 = app_model.to_dict()
        assert app_model_json2 == app_model_json


class TestModel_AppInstance:
    """
    Test Class for AppInstance
    """

    def test_app_instance_serialization(self):
        """
        Test serialization/deserialization for AppInstance
        """

        # Construct dict forms of any model objects needed in order to build this model.

        container_status_details_model = {}  # ContainerStatusDetails

        container_status_model = {}  # ContainerStatus
        container_status_model['current_state'] = container_status_details_model
        container_status_model['last_observed_state'] = container_status_details_model

        # Construct a json representation of a AppInstance model
        app_instance_model_json = {}
        app_instance_model_json['app_name'] = 'my-app'
        app_instance_model_json['revision_name'] = 'my-app'
        app_instance_model_json['scale_cpu_limit'] = '1'
        app_instance_model_json['scale_ephemeral_storage_limit'] = '4G'
        app_instance_model_json['scale_memory_limit'] = '4G'
        app_instance_model_json['system_container'] = container_status_model
        app_instance_model_json['user_container'] = container_status_model

        # Construct a model instance of AppInstance by calling from_dict on the json representation
        app_instance_model = AppInstance.from_dict(app_instance_model_json)
        assert app_instance_model != False

        # Construct a model instance of AppInstance by calling from_dict on the json representation
        app_instance_model_dict = AppInstance.from_dict(app_instance_model_json).__dict__
        app_instance_model2 = AppInstance(**app_instance_model_dict)

        # Verify the model instances are equivalent
        assert app_instance_model == app_instance_model2

        # Convert model instance back to dict and verify no loss of data
        app_instance_model_json2 = app_instance_model.to_dict()
        assert app_instance_model_json2 == app_instance_model_json


class TestModel_AppInstanceList:
    """
    Test Class for AppInstanceList
    """

    def test_app_instance_list_serialization(self):
        """
        Test serialization/deserialization for AppInstanceList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        list_first_metadata_model = {}  # ListFirstMetadata
        list_first_metadata_model['href'] = (
            'https://api.us-east.codeengine.cloud.ibm.com/v2/projects/230828b4-4f15-40a9-b183-1268c6ab88d5/apps/my-app/instances?limit=50'
        )

        container_status_details_model = {}  # ContainerStatusDetails

        container_status_model = {}  # ContainerStatus
        container_status_model['current_state'] = container_status_details_model
        container_status_model['last_observed_state'] = container_status_details_model

        app_instance_model = {}  # AppInstance
        app_instance_model['app_name'] = 'crash'
        app_instance_model['revision_name'] = 'crash-00001'
        app_instance_model['scale_cpu_limit'] = '0.125'
        app_instance_model['scale_ephemeral_storage_limit'] = '400M'
        app_instance_model['scale_memory_limit'] = '250M'
        app_instance_model['system_container'] = container_status_model
        app_instance_model['user_container'] = container_status_model

        list_next_metadata_model = {}  # ListNextMetadata
        list_next_metadata_model['href'] = 'testString'
        list_next_metadata_model['start'] = 'testString'

        # Construct a json representation of a AppInstanceList model
        app_instance_list_model_json = {}
        app_instance_list_model_json['first'] = list_first_metadata_model
        app_instance_list_model_json['instances'] = [app_instance_model]
        app_instance_list_model_json['limit'] = 100
        app_instance_list_model_json['next'] = list_next_metadata_model

        # Construct a model instance of AppInstanceList by calling from_dict on the json representation
        app_instance_list_model = AppInstanceList.from_dict(app_instance_list_model_json)
        assert app_instance_list_model != False

        # Construct a model instance of AppInstanceList by calling from_dict on the json representation
        app_instance_list_model_dict = AppInstanceList.from_dict(app_instance_list_model_json).__dict__
        app_instance_list_model2 = AppInstanceList(**app_instance_list_model_dict)

        # Verify the model instances are equivalent
        assert app_instance_list_model == app_instance_list_model2

        # Convert model instance back to dict and verify no loss of data
        app_instance_list_model_json2 = app_instance_list_model.to_dict()
        assert app_instance_list_model_json2 == app_instance_list_model_json


class TestModel_AppList:
    """
    Test Class for AppList
    """

    def test_app_list_serialization(self):
        """
        Test serialization/deserialization for AppList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        env_var_model = {}  # EnvVar
        env_var_model['key'] = 'MY_VARIABLE'
        env_var_model['name'] = 'SOME'
        env_var_model['prefix'] = 'PREFIX_'
        env_var_model['reference'] = 'my-secret'
        env_var_model['type'] = 'literal'
        env_var_model['value'] = 'VALUE'

        probe_model = {}  # Probe
        probe_model['failure_threshold'] = 5
        probe_model['initial_delay'] = 5
        probe_model['interval'] = 5
        probe_model['path'] = 'testString'
        probe_model['port'] = 8080
        probe_model['timeout'] = 300
        probe_model['type'] = 'tcp'

        volume_mount_model = {}  # VolumeMount
        volume_mount_model['mount_path'] = '/app'
        volume_mount_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_model['reference'] = 'my-secret'
        volume_mount_model['type'] = 'secret'

        app_status_model = {}  # AppStatus

        app_model = {}  # App
        app_model['computed_env_variables'] = [env_var_model]
        app_model['entity_tag'] = '1'
        app_model['image_port'] = 8080
        app_model['image_reference'] = 'icr.io/codeengine/helloworld'
        app_model['image_secret'] = 'my-secret'
        app_model['managed_domain_mappings'] = 'local_public'
        app_model['name'] = 'my-app'
        app_model['probe_liveness'] = probe_model
        app_model['probe_readiness'] = probe_model
        app_model['run_arguments'] = []
        app_model['run_as_user'] = 1001
        app_model['run_commands'] = []
        app_model['run_env_variables'] = [env_var_model]
        app_model['run_service_account'] = 'default'
        app_model['run_volume_mounts'] = [volume_mount_model]
        app_model['scale_concurrency'] = 100
        app_model['scale_concurrency_target'] = 80
        app_model['scale_cpu_limit'] = '1'
        app_model['scale_down_delay'] = 300
        app_model['scale_ephemeral_storage_limit'] = '400M'
        app_model['scale_initial_instances'] = 1
        app_model['scale_max_instances'] = 10
        app_model['scale_memory_limit'] = '4G'
        app_model['scale_min_instances'] = 0
        app_model['scale_request_timeout'] = 300
        app_model['status_details'] = app_status_model

        list_first_metadata_model = {}  # ListFirstMetadata
        list_first_metadata_model['href'] = 'testString'

        list_next_metadata_model = {}  # ListNextMetadata
        list_next_metadata_model['href'] = 'testString'
        list_next_metadata_model['start'] = 'testString'

        # Construct a json representation of a AppList model
        app_list_model_json = {}
        app_list_model_json['apps'] = [app_model]
        app_list_model_json['first'] = list_first_metadata_model
        app_list_model_json['limit'] = 100
        app_list_model_json['next'] = list_next_metadata_model

        # Construct a model instance of AppList by calling from_dict on the json representation
        app_list_model = AppList.from_dict(app_list_model_json)
        assert app_list_model != False

        # Construct a model instance of AppList by calling from_dict on the json representation
        app_list_model_dict = AppList.from_dict(app_list_model_json).__dict__
        app_list_model2 = AppList(**app_list_model_dict)

        # Verify the model instances are equivalent
        assert app_list_model == app_list_model2

        # Convert model instance back to dict and verify no loss of data
        app_list_model_json2 = app_list_model.to_dict()
        assert app_list_model_json2 == app_list_model_json


class TestModel_AppPatch:
    """
    Test Class for AppPatch
    """

    def test_app_patch_serialization(self):
        """
        Test serialization/deserialization for AppPatch
        """

        # Construct dict forms of any model objects needed in order to build this model.

        probe_prototype_model = {}  # ProbePrototype
        probe_prototype_model['failure_threshold'] = 5
        probe_prototype_model['initial_delay'] = 5
        probe_prototype_model['interval'] = 5
        probe_prototype_model['path'] = 'testString'
        probe_prototype_model['port'] = 8080
        probe_prototype_model['timeout'] = 300
        probe_prototype_model['type'] = 'tcp'

        env_var_prototype_model = {}  # EnvVarPrototype
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        volume_mount_prototype_model = {}  # VolumeMountPrototype
        volume_mount_prototype_model['mount_path'] = '/app'
        volume_mount_prototype_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_prototype_model['reference'] = 'my-secret'
        volume_mount_prototype_model['type'] = 'secret'

        # Construct a json representation of a AppPatch model
        app_patch_model_json = {}
        app_patch_model_json['image_port'] = 8080
        app_patch_model_json['image_reference'] = 'icr.io/codeengine/helloworld'
        app_patch_model_json['image_secret'] = 'my-secret'
        app_patch_model_json['managed_domain_mappings'] = 'local_public'
        app_patch_model_json['probe_liveness'] = probe_prototype_model
        app_patch_model_json['probe_readiness'] = probe_prototype_model
        app_patch_model_json['run_arguments'] = ['testString']
        app_patch_model_json['run_as_user'] = 1001
        app_patch_model_json['run_commands'] = ['testString']
        app_patch_model_json['run_env_variables'] = [env_var_prototype_model]
        app_patch_model_json['run_service_account'] = 'default'
        app_patch_model_json['run_volume_mounts'] = [volume_mount_prototype_model]
        app_patch_model_json['scale_concurrency'] = 100
        app_patch_model_json['scale_concurrency_target'] = 80
        app_patch_model_json['scale_cpu_limit'] = '1'
        app_patch_model_json['scale_down_delay'] = 300
        app_patch_model_json['scale_ephemeral_storage_limit'] = '4G'
        app_patch_model_json['scale_initial_instances'] = 1
        app_patch_model_json['scale_max_instances'] = 10
        app_patch_model_json['scale_memory_limit'] = '4G'
        app_patch_model_json['scale_min_instances'] = 1
        app_patch_model_json['scale_request_timeout'] = 300

        # Construct a model instance of AppPatch by calling from_dict on the json representation
        app_patch_model = AppPatch.from_dict(app_patch_model_json)
        assert app_patch_model != False

        # Construct a model instance of AppPatch by calling from_dict on the json representation
        app_patch_model_dict = AppPatch.from_dict(app_patch_model_json).__dict__
        app_patch_model2 = AppPatch(**app_patch_model_dict)

        # Verify the model instances are equivalent
        assert app_patch_model == app_patch_model2

        # Convert model instance back to dict and verify no loss of data
        app_patch_model_json2 = app_patch_model.to_dict()
        assert app_patch_model_json2 == app_patch_model_json


class TestModel_AppRevision:
    """
    Test Class for AppRevision
    """

    def test_app_revision_serialization(self):
        """
        Test serialization/deserialization for AppRevision
        """

        # Construct dict forms of any model objects needed in order to build this model.

        env_var_model = {}  # EnvVar
        env_var_model['key'] = 'MY_VARIABLE'
        env_var_model['name'] = 'SOME'
        env_var_model['prefix'] = 'PREFIX_'
        env_var_model['reference'] = 'my-secret'
        env_var_model['type'] = 'literal'
        env_var_model['value'] = 'VALUE'

        probe_model = {}  # Probe
        probe_model['failure_threshold'] = 5
        probe_model['initial_delay'] = 5
        probe_model['interval'] = 5
        probe_model['path'] = 'testString'
        probe_model['port'] = 8080
        probe_model['timeout'] = 300
        probe_model['type'] = 'tcp'

        volume_mount_model = {}  # VolumeMount
        volume_mount_model['mount_path'] = '/app'
        volume_mount_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_model['reference'] = 'my-secret'
        volume_mount_model['type'] = 'secret'

        app_revision_status_model = {}  # AppRevisionStatus

        # Construct a json representation of a AppRevision model
        app_revision_model_json = {}
        app_revision_model_json['app_name'] = 'my-app'
        app_revision_model_json['computed_env_variables'] = [env_var_model]
        app_revision_model_json['image_port'] = 8080
        app_revision_model_json['image_reference'] = 'icr.io/codeengine/helloworld'
        app_revision_model_json['image_secret'] = 'my-secret'
        app_revision_model_json['probe_liveness'] = probe_model
        app_revision_model_json['probe_readiness'] = probe_model
        app_revision_model_json['run_arguments'] = ['testString']
        app_revision_model_json['run_as_user'] = 1001
        app_revision_model_json['run_commands'] = ['testString']
        app_revision_model_json['run_env_variables'] = [env_var_model]
        app_revision_model_json['run_service_account'] = 'default'
        app_revision_model_json['run_volume_mounts'] = [volume_mount_model]
        app_revision_model_json['scale_concurrency'] = 100
        app_revision_model_json['scale_concurrency_target'] = 80
        app_revision_model_json['scale_cpu_limit'] = '1'
        app_revision_model_json['scale_down_delay'] = 300
        app_revision_model_json['scale_ephemeral_storage_limit'] = '4G'
        app_revision_model_json['scale_initial_instances'] = 1
        app_revision_model_json['scale_max_instances'] = 10
        app_revision_model_json['scale_memory_limit'] = '4G'
        app_revision_model_json['scale_min_instances'] = 1
        app_revision_model_json['scale_request_timeout'] = 300
        app_revision_model_json['status_details'] = app_revision_status_model

        # Construct a model instance of AppRevision by calling from_dict on the json representation
        app_revision_model = AppRevision.from_dict(app_revision_model_json)
        assert app_revision_model != False

        # Construct a model instance of AppRevision by calling from_dict on the json representation
        app_revision_model_dict = AppRevision.from_dict(app_revision_model_json).__dict__
        app_revision_model2 = AppRevision(**app_revision_model_dict)

        # Verify the model instances are equivalent
        assert app_revision_model == app_revision_model2

        # Convert model instance back to dict and verify no loss of data
        app_revision_model_json2 = app_revision_model.to_dict()
        assert app_revision_model_json2 == app_revision_model_json


class TestModel_AppRevisionList:
    """
    Test Class for AppRevisionList
    """

    def test_app_revision_list_serialization(self):
        """
        Test serialization/deserialization for AppRevisionList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        list_first_metadata_model = {}  # ListFirstMetadata
        list_first_metadata_model['href'] = 'testString'

        list_next_metadata_model = {}  # ListNextMetadata
        list_next_metadata_model['href'] = 'testString'
        list_next_metadata_model['start'] = 'testString'

        env_var_model = {}  # EnvVar
        env_var_model['key'] = 'MY_VARIABLE'
        env_var_model['name'] = 'SOME'
        env_var_model['prefix'] = 'PREFIX_'
        env_var_model['reference'] = 'my-secret'
        env_var_model['type'] = 'literal'
        env_var_model['value'] = 'VALUE'

        probe_model = {}  # Probe
        probe_model['failure_threshold'] = 5
        probe_model['initial_delay'] = 5
        probe_model['interval'] = 5
        probe_model['path'] = 'testString'
        probe_model['port'] = 8080
        probe_model['timeout'] = 300
        probe_model['type'] = 'tcp'

        volume_mount_model = {}  # VolumeMount
        volume_mount_model['mount_path'] = '/app'
        volume_mount_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_model['reference'] = 'my-secret'
        volume_mount_model['type'] = 'secret'

        app_revision_status_model = {}  # AppRevisionStatus

        app_revision_model = {}  # AppRevision
        app_revision_model['app_name'] = 'my-app'
        app_revision_model['computed_env_variables'] = [env_var_model]
        app_revision_model['image_port'] = 8080
        app_revision_model['image_reference'] = 'icr.io/codeengine/helloworld'
        app_revision_model['image_secret'] = 'my-secret'
        app_revision_model['probe_liveness'] = probe_model
        app_revision_model['probe_readiness'] = probe_model
        app_revision_model['run_arguments'] = []
        app_revision_model['run_as_user'] = 1001
        app_revision_model['run_commands'] = []
        app_revision_model['run_env_variables'] = [env_var_model]
        app_revision_model['run_service_account'] = 'default'
        app_revision_model['run_volume_mounts'] = [volume_mount_model]
        app_revision_model['scale_concurrency'] = 100
        app_revision_model['scale_concurrency_target'] = 80
        app_revision_model['scale_cpu_limit'] = '1'
        app_revision_model['scale_down_delay'] = 300
        app_revision_model['scale_ephemeral_storage_limit'] = '400M'
        app_revision_model['scale_initial_instances'] = 1
        app_revision_model['scale_max_instances'] = 10
        app_revision_model['scale_memory_limit'] = '4G'
        app_revision_model['scale_min_instances'] = 0
        app_revision_model['scale_request_timeout'] = 300
        app_revision_model['status_details'] = app_revision_status_model

        # Construct a json representation of a AppRevisionList model
        app_revision_list_model_json = {}
        app_revision_list_model_json['first'] = list_first_metadata_model
        app_revision_list_model_json['limit'] = 100
        app_revision_list_model_json['next'] = list_next_metadata_model
        app_revision_list_model_json['revisions'] = [app_revision_model]

        # Construct a model instance of AppRevisionList by calling from_dict on the json representation
        app_revision_list_model = AppRevisionList.from_dict(app_revision_list_model_json)
        assert app_revision_list_model != False

        # Construct a model instance of AppRevisionList by calling from_dict on the json representation
        app_revision_list_model_dict = AppRevisionList.from_dict(app_revision_list_model_json).__dict__
        app_revision_list_model2 = AppRevisionList(**app_revision_list_model_dict)

        # Verify the model instances are equivalent
        assert app_revision_list_model == app_revision_list_model2

        # Convert model instance back to dict and verify no loss of data
        app_revision_list_model_json2 = app_revision_list_model.to_dict()
        assert app_revision_list_model_json2 == app_revision_list_model_json


class TestModel_AppRevisionStatus:
    """
    Test Class for AppRevisionStatus
    """

    def test_app_revision_status_serialization(self):
        """
        Test serialization/deserialization for AppRevisionStatus
        """

        # Construct a json representation of a AppRevisionStatus model
        app_revision_status_model_json = {}

        # Construct a model instance of AppRevisionStatus by calling from_dict on the json representation
        app_revision_status_model = AppRevisionStatus.from_dict(app_revision_status_model_json)
        assert app_revision_status_model != False

        # Construct a model instance of AppRevisionStatus by calling from_dict on the json representation
        app_revision_status_model_dict = AppRevisionStatus.from_dict(app_revision_status_model_json).__dict__
        app_revision_status_model2 = AppRevisionStatus(**app_revision_status_model_dict)

        # Verify the model instances are equivalent
        assert app_revision_status_model == app_revision_status_model2

        # Convert model instance back to dict and verify no loss of data
        app_revision_status_model_json2 = app_revision_status_model.to_dict()
        assert app_revision_status_model_json2 == app_revision_status_model_json


class TestModel_AppStatus:
    """
    Test Class for AppStatus
    """

    def test_app_status_serialization(self):
        """
        Test serialization/deserialization for AppStatus
        """

        # Construct a json representation of a AppStatus model
        app_status_model_json = {}

        # Construct a model instance of AppStatus by calling from_dict on the json representation
        app_status_model = AppStatus.from_dict(app_status_model_json)
        assert app_status_model != False

        # Construct a model instance of AppStatus by calling from_dict on the json representation
        app_status_model_dict = AppStatus.from_dict(app_status_model_json).__dict__
        app_status_model2 = AppStatus(**app_status_model_dict)

        # Verify the model instances are equivalent
        assert app_status_model == app_status_model2

        # Convert model instance back to dict and verify no loss of data
        app_status_model_json2 = app_status_model.to_dict()
        assert app_status_model_json2 == app_status_model_json


class TestModel_Binding:
    """
    Test Class for Binding
    """

    def test_binding_serialization(self):
        """
        Test serialization/deserialization for Binding
        """

        # Construct dict forms of any model objects needed in order to build this model.

        component_ref_model = {}  # ComponentRef
        component_ref_model['name'] = 'my-app-1'
        component_ref_model['resource_type'] = 'app_v2'

        # Construct a json representation of a Binding model
        binding_model_json = {}
        binding_model_json['component'] = component_ref_model
        binding_model_json['prefix'] = 'MY_COS'
        binding_model_json['secret_name'] = 'my-service-access'

        # Construct a model instance of Binding by calling from_dict on the json representation
        binding_model = Binding.from_dict(binding_model_json)
        assert binding_model != False

        # Construct a model instance of Binding by calling from_dict on the json representation
        binding_model_dict = Binding.from_dict(binding_model_json).__dict__
        binding_model2 = Binding(**binding_model_dict)

        # Verify the model instances are equivalent
        assert binding_model == binding_model2

        # Convert model instance back to dict and verify no loss of data
        binding_model_json2 = binding_model.to_dict()
        assert binding_model_json2 == binding_model_json


class TestModel_BindingList:
    """
    Test Class for BindingList
    """

    def test_binding_list_serialization(self):
        """
        Test serialization/deserialization for BindingList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        component_ref_model = {}  # ComponentRef
        component_ref_model['name'] = 'my-app-1'
        component_ref_model['resource_type'] = 'app_v2'

        binding_model = {}  # Binding
        binding_model['component'] = component_ref_model
        binding_model['prefix'] = 'PREFIX'
        binding_model['secret_name'] = 'my-service-access'

        list_first_metadata_model = {}  # ListFirstMetadata
        list_first_metadata_model['href'] = 'testString'

        list_next_metadata_model = {}  # ListNextMetadata
        list_next_metadata_model['href'] = 'testString'
        list_next_metadata_model['start'] = 'testString'

        # Construct a json representation of a BindingList model
        binding_list_model_json = {}
        binding_list_model_json['bindings'] = [binding_model]
        binding_list_model_json['first'] = list_first_metadata_model
        binding_list_model_json['limit'] = 100
        binding_list_model_json['next'] = list_next_metadata_model

        # Construct a model instance of BindingList by calling from_dict on the json representation
        binding_list_model = BindingList.from_dict(binding_list_model_json)
        assert binding_list_model != False

        # Construct a model instance of BindingList by calling from_dict on the json representation
        binding_list_model_dict = BindingList.from_dict(binding_list_model_json).__dict__
        binding_list_model2 = BindingList(**binding_list_model_dict)

        # Verify the model instances are equivalent
        assert binding_list_model == binding_list_model2

        # Convert model instance back to dict and verify no loss of data
        binding_list_model_json2 = binding_list_model.to_dict()
        assert binding_list_model_json2 == binding_list_model_json


class TestModel_Build:
    """
    Test Class for Build
    """

    def test_build_serialization(self):
        """
        Test serialization/deserialization for Build
        """

        # Construct dict forms of any model objects needed in order to build this model.

        build_status_model = {}  # BuildStatus

        # Construct a json representation of a Build model
        build_model_json = {}
        build_model_json['entity_tag'] = '2385407409'
        build_model_json['name'] = 'my-build'
        build_model_json['output_image'] = 'private.de.icr.io/icr_namespace/image-name'
        build_model_json['output_secret'] = 'ce-auto-icr-private-eu-de'
        build_model_json['source_context_dir'] = 'some/subfolder'
        build_model_json['source_revision'] = 'main'
        build_model_json['source_secret'] = 'testString'
        build_model_json['source_type'] = 'git'
        build_model_json['source_url'] = 'https://github.com/IBM/CodeEngine'
        build_model_json['status_details'] = build_status_model
        build_model_json['strategy_size'] = 'medium'
        build_model_json['strategy_spec_file'] = 'Dockerfile'
        build_model_json['strategy_type'] = 'dockerfile'
        build_model_json['timeout'] = 600

        # Construct a model instance of Build by calling from_dict on the json representation
        build_model = Build.from_dict(build_model_json)
        assert build_model != False

        # Construct a model instance of Build by calling from_dict on the json representation
        build_model_dict = Build.from_dict(build_model_json).__dict__
        build_model2 = Build(**build_model_dict)

        # Verify the model instances are equivalent
        assert build_model == build_model2

        # Convert model instance back to dict and verify no loss of data
        build_model_json2 = build_model.to_dict()
        assert build_model_json2 == build_model_json


class TestModel_BuildList:
    """
    Test Class for BuildList
    """

    def test_build_list_serialization(self):
        """
        Test serialization/deserialization for BuildList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        build_status_model = {}  # BuildStatus

        build_model = {}  # Build
        build_model['entity_tag'] = '2385407409'
        build_model['name'] = 'my-build'
        build_model['output_image'] = 'private.de.icr.io/icr_namespace/test-image-1'
        build_model['output_secret'] = 'ce-auto-icr-private-eu-de'
        build_model['source_context_dir'] = 'some/subfolder'
        build_model['source_revision'] = 'main'
        build_model['source_secret'] = 'testString'
        build_model['source_type'] = 'git'
        build_model['source_url'] = 'https://github.com/IBM/CodeEngine'
        build_model['status_details'] = build_status_model
        build_model['strategy_size'] = 'medium'
        build_model['strategy_spec_file'] = 'Dockerfile'
        build_model['strategy_type'] = 'dockerfile'
        build_model['timeout'] = 600

        list_first_metadata_model = {}  # ListFirstMetadata
        list_first_metadata_model['href'] = 'testString'

        list_next_metadata_model = {}  # ListNextMetadata
        list_next_metadata_model['href'] = 'testString'
        list_next_metadata_model['start'] = 'testString'

        # Construct a json representation of a BuildList model
        build_list_model_json = {}
        build_list_model_json['builds'] = [build_model]
        build_list_model_json['first'] = list_first_metadata_model
        build_list_model_json['limit'] = 100
        build_list_model_json['next'] = list_next_metadata_model

        # Construct a model instance of BuildList by calling from_dict on the json representation
        build_list_model = BuildList.from_dict(build_list_model_json)
        assert build_list_model != False

        # Construct a model instance of BuildList by calling from_dict on the json representation
        build_list_model_dict = BuildList.from_dict(build_list_model_json).__dict__
        build_list_model2 = BuildList(**build_list_model_dict)

        # Verify the model instances are equivalent
        assert build_list_model == build_list_model2

        # Convert model instance back to dict and verify no loss of data
        build_list_model_json2 = build_list_model.to_dict()
        assert build_list_model_json2 == build_list_model_json


class TestModel_BuildPatch:
    """
    Test Class for BuildPatch
    """

    def test_build_patch_serialization(self):
        """
        Test serialization/deserialization for BuildPatch
        """

        # Construct a json representation of a BuildPatch model
        build_patch_model_json = {}
        build_patch_model_json['output_image'] = 'private.de.icr.io/icr_namespace/image-name'
        build_patch_model_json['output_secret'] = 'ce-auto-icr-private-eu-de'
        build_patch_model_json['source_context_dir'] = 'some/subfolder'
        build_patch_model_json['source_revision'] = 'main'
        build_patch_model_json['source_secret'] = 'testString'
        build_patch_model_json['source_type'] = 'git'
        build_patch_model_json['source_url'] = 'https://github.com/IBM/CodeEngine'
        build_patch_model_json['strategy_size'] = 'medium'
        build_patch_model_json['strategy_spec_file'] = 'Dockerfile'
        build_patch_model_json['strategy_type'] = 'dockerfile'
        build_patch_model_json['timeout'] = 600

        # Construct a model instance of BuildPatch by calling from_dict on the json representation
        build_patch_model = BuildPatch.from_dict(build_patch_model_json)
        assert build_patch_model != False

        # Construct a model instance of BuildPatch by calling from_dict on the json representation
        build_patch_model_dict = BuildPatch.from_dict(build_patch_model_json).__dict__
        build_patch_model2 = BuildPatch(**build_patch_model_dict)

        # Verify the model instances are equivalent
        assert build_patch_model == build_patch_model2

        # Convert model instance back to dict and verify no loss of data
        build_patch_model_json2 = build_patch_model.to_dict()
        assert build_patch_model_json2 == build_patch_model_json


class TestModel_BuildRun:
    """
    Test Class for BuildRun
    """

    def test_build_run_serialization(self):
        """
        Test serialization/deserialization for BuildRun
        """

        # Construct dict forms of any model objects needed in order to build this model.

        build_run_status_model = {}  # BuildRunStatus

        # Construct a json representation of a BuildRun model
        build_run_model_json = {}
        build_run_model_json['build_name'] = 'testString'
        build_run_model_json['name'] = 'my-build-run'
        build_run_model_json['output_image'] = 'private.de.icr.io/icr_namespace/image-name'
        build_run_model_json['output_secret'] = 'ce-auto-icr-private-eu-de'
        build_run_model_json['service_account'] = 'default'
        build_run_model_json['source_context_dir'] = 'some/subfolder'
        build_run_model_json['source_revision'] = 'main'
        build_run_model_json['source_secret'] = 'testString'
        build_run_model_json['source_type'] = 'git'
        build_run_model_json['source_url'] = 'https://github.com/IBM/CodeEngine'
        build_run_model_json['status_details'] = build_run_status_model
        build_run_model_json['strategy_size'] = 'medium'
        build_run_model_json['strategy_spec_file'] = 'Dockerfile'
        build_run_model_json['strategy_type'] = 'dockerfile'
        build_run_model_json['timeout'] = 600

        # Construct a model instance of BuildRun by calling from_dict on the json representation
        build_run_model = BuildRun.from_dict(build_run_model_json)
        assert build_run_model != False

        # Construct a model instance of BuildRun by calling from_dict on the json representation
        build_run_model_dict = BuildRun.from_dict(build_run_model_json).__dict__
        build_run_model2 = BuildRun(**build_run_model_dict)

        # Verify the model instances are equivalent
        assert build_run_model == build_run_model2

        # Convert model instance back to dict and verify no loss of data
        build_run_model_json2 = build_run_model.to_dict()
        assert build_run_model_json2 == build_run_model_json


class TestModel_BuildRunList:
    """
    Test Class for BuildRunList
    """

    def test_build_run_list_serialization(self):
        """
        Test serialization/deserialization for BuildRunList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        build_run_status_model = {}  # BuildRunStatus

        build_run_model = {}  # BuildRun
        build_run_model['build_name'] = 'my-build'
        build_run_model['name'] = 'my-buildrun-1'
        build_run_model['output_image'] = 'private.de.icr.io/icr_namespace/image-name'
        build_run_model['output_secret'] = 'ce-auto-icr-private-eu-de'
        build_run_model['service_account'] = 'default'
        build_run_model['source_context_dir'] = 'some/subfolder'
        build_run_model['source_revision'] = 'main'
        build_run_model['source_secret'] = 'testString'
        build_run_model['source_type'] = 'git'
        build_run_model['source_url'] = 'https://github.com/IBM/CodeEngine'
        build_run_model['status_details'] = build_run_status_model
        build_run_model['strategy_size'] = 'medium'
        build_run_model['strategy_spec_file'] = 'Dockerfile'
        build_run_model['strategy_type'] = 'dockerfile'
        build_run_model['timeout'] = 600

        list_first_metadata_model = {}  # ListFirstMetadata
        list_first_metadata_model['href'] = 'testString'

        list_next_metadata_model = {}  # ListNextMetadata
        list_next_metadata_model['href'] = 'testString'
        list_next_metadata_model['start'] = 'testString'

        # Construct a json representation of a BuildRunList model
        build_run_list_model_json = {}
        build_run_list_model_json['build_runs'] = [build_run_model]
        build_run_list_model_json['first'] = list_first_metadata_model
        build_run_list_model_json['limit'] = 100
        build_run_list_model_json['next'] = list_next_metadata_model

        # Construct a model instance of BuildRunList by calling from_dict on the json representation
        build_run_list_model = BuildRunList.from_dict(build_run_list_model_json)
        assert build_run_list_model != False

        # Construct a model instance of BuildRunList by calling from_dict on the json representation
        build_run_list_model_dict = BuildRunList.from_dict(build_run_list_model_json).__dict__
        build_run_list_model2 = BuildRunList(**build_run_list_model_dict)

        # Verify the model instances are equivalent
        assert build_run_list_model == build_run_list_model2

        # Convert model instance back to dict and verify no loss of data
        build_run_list_model_json2 = build_run_list_model.to_dict()
        assert build_run_list_model_json2 == build_run_list_model_json


class TestModel_BuildRunStatus:
    """
    Test Class for BuildRunStatus
    """

    def test_build_run_status_serialization(self):
        """
        Test serialization/deserialization for BuildRunStatus
        """

        # Construct a json representation of a BuildRunStatus model
        build_run_status_model_json = {}

        # Construct a model instance of BuildRunStatus by calling from_dict on the json representation
        build_run_status_model = BuildRunStatus.from_dict(build_run_status_model_json)
        assert build_run_status_model != False

        # Construct a model instance of BuildRunStatus by calling from_dict on the json representation
        build_run_status_model_dict = BuildRunStatus.from_dict(build_run_status_model_json).__dict__
        build_run_status_model2 = BuildRunStatus(**build_run_status_model_dict)

        # Verify the model instances are equivalent
        assert build_run_status_model == build_run_status_model2

        # Convert model instance back to dict and verify no loss of data
        build_run_status_model_json2 = build_run_status_model.to_dict()
        assert build_run_status_model_json2 == build_run_status_model_json


class TestModel_BuildStatus:
    """
    Test Class for BuildStatus
    """

    def test_build_status_serialization(self):
        """
        Test serialization/deserialization for BuildStatus
        """

        # Construct a json representation of a BuildStatus model
        build_status_model_json = {}

        # Construct a model instance of BuildStatus by calling from_dict on the json representation
        build_status_model = BuildStatus.from_dict(build_status_model_json)
        assert build_status_model != False

        # Construct a model instance of BuildStatus by calling from_dict on the json representation
        build_status_model_dict = BuildStatus.from_dict(build_status_model_json).__dict__
        build_status_model2 = BuildStatus(**build_status_model_dict)

        # Verify the model instances are equivalent
        assert build_status_model == build_status_model2

        # Convert model instance back to dict and verify no loss of data
        build_status_model_json2 = build_status_model.to_dict()
        assert build_status_model_json2 == build_status_model_json


class TestModel_ComponentRef:
    """
    Test Class for ComponentRef
    """

    def test_component_ref_serialization(self):
        """
        Test serialization/deserialization for ComponentRef
        """

        # Construct a json representation of a ComponentRef model
        component_ref_model_json = {}
        component_ref_model_json['name'] = 'my-app-1'
        component_ref_model_json['resource_type'] = 'app_v2'

        # Construct a model instance of ComponentRef by calling from_dict on the json representation
        component_ref_model = ComponentRef.from_dict(component_ref_model_json)
        assert component_ref_model != False

        # Construct a model instance of ComponentRef by calling from_dict on the json representation
        component_ref_model_dict = ComponentRef.from_dict(component_ref_model_json).__dict__
        component_ref_model2 = ComponentRef(**component_ref_model_dict)

        # Verify the model instances are equivalent
        assert component_ref_model == component_ref_model2

        # Convert model instance back to dict and verify no loss of data
        component_ref_model_json2 = component_ref_model.to_dict()
        assert component_ref_model_json2 == component_ref_model_json


class TestModel_ConfigMap:
    """
    Test Class for ConfigMap
    """

    def test_config_map_serialization(self):
        """
        Test serialization/deserialization for ConfigMap
        """

        # Construct a json representation of a ConfigMap model
        config_map_model_json = {}
        config_map_model_json['data'] = {'key1': 'testString'}
        config_map_model_json['entity_tag'] = '2385407409'
        config_map_model_json['name'] = 'my-config-map'

        # Construct a model instance of ConfigMap by calling from_dict on the json representation
        config_map_model = ConfigMap.from_dict(config_map_model_json)
        assert config_map_model != False

        # Construct a model instance of ConfigMap by calling from_dict on the json representation
        config_map_model_dict = ConfigMap.from_dict(config_map_model_json).__dict__
        config_map_model2 = ConfigMap(**config_map_model_dict)

        # Verify the model instances are equivalent
        assert config_map_model == config_map_model2

        # Convert model instance back to dict and verify no loss of data
        config_map_model_json2 = config_map_model.to_dict()
        assert config_map_model_json2 == config_map_model_json


class TestModel_ConfigMapList:
    """
    Test Class for ConfigMapList
    """

    def test_config_map_list_serialization(self):
        """
        Test serialization/deserialization for ConfigMapList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        config_map_model = {}  # ConfigMap
        config_map_model['data'] = {'key1': 'testString'}
        config_map_model['entity_tag'] = '2386238209'
        config_map_model['name'] = 'my-config-map'

        list_first_metadata_model = {}  # ListFirstMetadata
        list_first_metadata_model['href'] = 'testString'

        list_next_metadata_model = {}  # ListNextMetadata
        list_next_metadata_model['href'] = 'testString'
        list_next_metadata_model['start'] = 'testString'

        # Construct a json representation of a ConfigMapList model
        config_map_list_model_json = {}
        config_map_list_model_json['config_maps'] = [config_map_model]
        config_map_list_model_json['first'] = list_first_metadata_model
        config_map_list_model_json['limit'] = 100
        config_map_list_model_json['next'] = list_next_metadata_model

        # Construct a model instance of ConfigMapList by calling from_dict on the json representation
        config_map_list_model = ConfigMapList.from_dict(config_map_list_model_json)
        assert config_map_list_model != False

        # Construct a model instance of ConfigMapList by calling from_dict on the json representation
        config_map_list_model_dict = ConfigMapList.from_dict(config_map_list_model_json).__dict__
        config_map_list_model2 = ConfigMapList(**config_map_list_model_dict)

        # Verify the model instances are equivalent
        assert config_map_list_model == config_map_list_model2

        # Convert model instance back to dict and verify no loss of data
        config_map_list_model_json2 = config_map_list_model.to_dict()
        assert config_map_list_model_json2 == config_map_list_model_json


class TestModel_ContainerStatus:
    """
    Test Class for ContainerStatus
    """

    def test_container_status_serialization(self):
        """
        Test serialization/deserialization for ContainerStatus
        """

        # Construct dict forms of any model objects needed in order to build this model.

        container_status_details_model = {}  # ContainerStatusDetails

        # Construct a json representation of a ContainerStatus model
        container_status_model_json = {}
        container_status_model_json['current_state'] = container_status_details_model
        container_status_model_json['last_observed_state'] = container_status_details_model

        # Construct a model instance of ContainerStatus by calling from_dict on the json representation
        container_status_model = ContainerStatus.from_dict(container_status_model_json)
        assert container_status_model != False

        # Construct a model instance of ContainerStatus by calling from_dict on the json representation
        container_status_model_dict = ContainerStatus.from_dict(container_status_model_json).__dict__
        container_status_model2 = ContainerStatus(**container_status_model_dict)

        # Verify the model instances are equivalent
        assert container_status_model == container_status_model2

        # Convert model instance back to dict and verify no loss of data
        container_status_model_json2 = container_status_model.to_dict()
        assert container_status_model_json2 == container_status_model_json


class TestModel_ContainerStatusDetails:
    """
    Test Class for ContainerStatusDetails
    """

    def test_container_status_details_serialization(self):
        """
        Test serialization/deserialization for ContainerStatusDetails
        """

        # Construct a json representation of a ContainerStatusDetails model
        container_status_details_model_json = {}

        # Construct a model instance of ContainerStatusDetails by calling from_dict on the json representation
        container_status_details_model = ContainerStatusDetails.from_dict(container_status_details_model_json)
        assert container_status_details_model != False

        # Construct a model instance of ContainerStatusDetails by calling from_dict on the json representation
        container_status_details_model_dict = ContainerStatusDetails.from_dict(
            container_status_details_model_json
        ).__dict__
        container_status_details_model2 = ContainerStatusDetails(**container_status_details_model_dict)

        # Verify the model instances are equivalent
        assert container_status_details_model == container_status_details_model2

        # Convert model instance back to dict and verify no loss of data
        container_status_details_model_json2 = container_status_details_model.to_dict()
        assert container_status_details_model_json2 == container_status_details_model_json


class TestModel_DomainMapping:
    """
    Test Class for DomainMapping
    """

    def test_domain_mapping_serialization(self):
        """
        Test serialization/deserialization for DomainMapping
        """

        # Construct dict forms of any model objects needed in order to build this model.

        component_ref_model = {}  # ComponentRef
        component_ref_model['name'] = 'my-app'
        component_ref_model['resource_type'] = 'app_v2'

        domain_mapping_status_model = {}  # DomainMappingStatus

        # Construct a json representation of a DomainMapping model
        domain_mapping_model_json = {}
        domain_mapping_model_json['component'] = component_ref_model
        domain_mapping_model_json['entity_tag'] = '2385407409'
        domain_mapping_model_json['name'] = 'www.example.com'
        domain_mapping_model_json['status_details'] = domain_mapping_status_model
        domain_mapping_model_json['tls_secret'] = 'my-tls-secret'

        # Construct a model instance of DomainMapping by calling from_dict on the json representation
        domain_mapping_model = DomainMapping.from_dict(domain_mapping_model_json)
        assert domain_mapping_model != False

        # Construct a model instance of DomainMapping by calling from_dict on the json representation
        domain_mapping_model_dict = DomainMapping.from_dict(domain_mapping_model_json).__dict__
        domain_mapping_model2 = DomainMapping(**domain_mapping_model_dict)

        # Verify the model instances are equivalent
        assert domain_mapping_model == domain_mapping_model2

        # Convert model instance back to dict and verify no loss of data
        domain_mapping_model_json2 = domain_mapping_model.to_dict()
        assert domain_mapping_model_json2 == domain_mapping_model_json


class TestModel_DomainMappingList:
    """
    Test Class for DomainMappingList
    """

    def test_domain_mapping_list_serialization(self):
        """
        Test serialization/deserialization for DomainMappingList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        component_ref_model = {}  # ComponentRef
        component_ref_model['name'] = 'my-app'
        component_ref_model['resource_type'] = 'app_v2'

        domain_mapping_status_model = {}  # DomainMappingStatus

        domain_mapping_model = {}  # DomainMapping
        domain_mapping_model['component'] = component_ref_model
        domain_mapping_model['entity_tag'] = '2385407409'
        domain_mapping_model['name'] = 'www.example.com'
        domain_mapping_model['status_details'] = domain_mapping_status_model
        domain_mapping_model['tls_secret'] = 'my-tls-secret'

        list_first_metadata_model = {}  # ListFirstMetadata
        list_first_metadata_model['href'] = 'testString'

        list_next_metadata_model = {}  # ListNextMetadata
        list_next_metadata_model['href'] = 'testString'
        list_next_metadata_model['start'] = 'testString'

        # Construct a json representation of a DomainMappingList model
        domain_mapping_list_model_json = {}
        domain_mapping_list_model_json['domain_mappings'] = [domain_mapping_model]
        domain_mapping_list_model_json['first'] = list_first_metadata_model
        domain_mapping_list_model_json['limit'] = 100
        domain_mapping_list_model_json['next'] = list_next_metadata_model

        # Construct a model instance of DomainMappingList by calling from_dict on the json representation
        domain_mapping_list_model = DomainMappingList.from_dict(domain_mapping_list_model_json)
        assert domain_mapping_list_model != False

        # Construct a model instance of DomainMappingList by calling from_dict on the json representation
        domain_mapping_list_model_dict = DomainMappingList.from_dict(domain_mapping_list_model_json).__dict__
        domain_mapping_list_model2 = DomainMappingList(**domain_mapping_list_model_dict)

        # Verify the model instances are equivalent
        assert domain_mapping_list_model == domain_mapping_list_model2

        # Convert model instance back to dict and verify no loss of data
        domain_mapping_list_model_json2 = domain_mapping_list_model.to_dict()
        assert domain_mapping_list_model_json2 == domain_mapping_list_model_json


class TestModel_DomainMappingPatch:
    """
    Test Class for DomainMappingPatch
    """

    def test_domain_mapping_patch_serialization(self):
        """
        Test serialization/deserialization for DomainMappingPatch
        """

        # Construct dict forms of any model objects needed in order to build this model.

        component_ref_model = {}  # ComponentRef
        component_ref_model['name'] = 'my-app'
        component_ref_model['resource_type'] = 'app_v2'

        # Construct a json representation of a DomainMappingPatch model
        domain_mapping_patch_model_json = {}
        domain_mapping_patch_model_json['component'] = component_ref_model
        domain_mapping_patch_model_json['tls_secret'] = 'my-tls-secret'

        # Construct a model instance of DomainMappingPatch by calling from_dict on the json representation
        domain_mapping_patch_model = DomainMappingPatch.from_dict(domain_mapping_patch_model_json)
        assert domain_mapping_patch_model != False

        # Construct a model instance of DomainMappingPatch by calling from_dict on the json representation
        domain_mapping_patch_model_dict = DomainMappingPatch.from_dict(domain_mapping_patch_model_json).__dict__
        domain_mapping_patch_model2 = DomainMappingPatch(**domain_mapping_patch_model_dict)

        # Verify the model instances are equivalent
        assert domain_mapping_patch_model == domain_mapping_patch_model2

        # Convert model instance back to dict and verify no loss of data
        domain_mapping_patch_model_json2 = domain_mapping_patch_model.to_dict()
        assert domain_mapping_patch_model_json2 == domain_mapping_patch_model_json


class TestModel_DomainMappingStatus:
    """
    Test Class for DomainMappingStatus
    """

    def test_domain_mapping_status_serialization(self):
        """
        Test serialization/deserialization for DomainMappingStatus
        """

        # Construct a json representation of a DomainMappingStatus model
        domain_mapping_status_model_json = {}

        # Construct a model instance of DomainMappingStatus by calling from_dict on the json representation
        domain_mapping_status_model = DomainMappingStatus.from_dict(domain_mapping_status_model_json)
        assert domain_mapping_status_model != False

        # Construct a model instance of DomainMappingStatus by calling from_dict on the json representation
        domain_mapping_status_model_dict = DomainMappingStatus.from_dict(domain_mapping_status_model_json).__dict__
        domain_mapping_status_model2 = DomainMappingStatus(**domain_mapping_status_model_dict)

        # Verify the model instances are equivalent
        assert domain_mapping_status_model == domain_mapping_status_model2

        # Convert model instance back to dict and verify no loss of data
        domain_mapping_status_model_json2 = domain_mapping_status_model.to_dict()
        assert domain_mapping_status_model_json2 == domain_mapping_status_model_json


class TestModel_EnvVar:
    """
    Test Class for EnvVar
    """

    def test_env_var_serialization(self):
        """
        Test serialization/deserialization for EnvVar
        """

        # Construct a json representation of a EnvVar model
        env_var_model_json = {}
        env_var_model_json['key'] = 'MY_VARIABLE'
        env_var_model_json['name'] = 'SOME'
        env_var_model_json['prefix'] = 'PREFIX_'
        env_var_model_json['reference'] = 'my-secret'
        env_var_model_json['type'] = 'literal'
        env_var_model_json['value'] = 'VALUE'

        # Construct a model instance of EnvVar by calling from_dict on the json representation
        env_var_model = EnvVar.from_dict(env_var_model_json)
        assert env_var_model != False

        # Construct a model instance of EnvVar by calling from_dict on the json representation
        env_var_model_dict = EnvVar.from_dict(env_var_model_json).__dict__
        env_var_model2 = EnvVar(**env_var_model_dict)

        # Verify the model instances are equivalent
        assert env_var_model == env_var_model2

        # Convert model instance back to dict and verify no loss of data
        env_var_model_json2 = env_var_model.to_dict()
        assert env_var_model_json2 == env_var_model_json


class TestModel_EnvVarPrototype:
    """
    Test Class for EnvVarPrototype
    """

    def test_env_var_prototype_serialization(self):
        """
        Test serialization/deserialization for EnvVarPrototype
        """

        # Construct a json representation of a EnvVarPrototype model
        env_var_prototype_model_json = {}
        env_var_prototype_model_json['key'] = 'MY_VARIABLE'
        env_var_prototype_model_json['name'] = 'SOME'
        env_var_prototype_model_json['prefix'] = 'PREFIX_'
        env_var_prototype_model_json['reference'] = 'my-secret'
        env_var_prototype_model_json['type'] = 'literal'
        env_var_prototype_model_json['value'] = 'VALUE'

        # Construct a model instance of EnvVarPrototype by calling from_dict on the json representation
        env_var_prototype_model = EnvVarPrototype.from_dict(env_var_prototype_model_json)
        assert env_var_prototype_model != False

        # Construct a model instance of EnvVarPrototype by calling from_dict on the json representation
        env_var_prototype_model_dict = EnvVarPrototype.from_dict(env_var_prototype_model_json).__dict__
        env_var_prototype_model2 = EnvVarPrototype(**env_var_prototype_model_dict)

        # Verify the model instances are equivalent
        assert env_var_prototype_model == env_var_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        env_var_prototype_model_json2 = env_var_prototype_model.to_dict()
        assert env_var_prototype_model_json2 == env_var_prototype_model_json


class TestModel_Function:
    """
    Test Class for Function
    """

    def test_function_serialization(self):
        """
        Test serialization/deserialization for Function
        """

        # Construct dict forms of any model objects needed in order to build this model.

        env_var_model = {}  # EnvVar
        env_var_model['key'] = 'MY_VARIABLE'
        env_var_model['name'] = 'SOME'
        env_var_model['prefix'] = 'PREFIX_'
        env_var_model['reference'] = 'my-secret'
        env_var_model['type'] = 'literal'
        env_var_model['value'] = 'VALUE'

        function_status_model = {}  # FunctionStatus

        # Construct a json representation of a Function model
        function_model_json = {}
        function_model_json['code_binary'] = False
        function_model_json['code_main'] = 'main'
        function_model_json['code_reference'] = 'data:text/plain;base64,<base64encoded-source-code>'
        function_model_json['code_secret'] = 'my-secret'
        function_model_json['computed_env_variables'] = [env_var_model]
        function_model_json['entity_tag'] = '2385407409'
        function_model_json['managed_domain_mappings'] = 'local_public'
        function_model_json['name'] = 'my-function'
        function_model_json['run_env_variables'] = [env_var_model]
        function_model_json['runtime'] = 'nodejs-18'
        function_model_json['scale_concurrency'] = 1
        function_model_json['scale_cpu_limit'] = '1'
        function_model_json['scale_down_delay'] = 300
        function_model_json['scale_max_execution_time'] = 60
        function_model_json['scale_memory_limit'] = '1G'
        function_model_json['status_details'] = function_status_model

        # Construct a model instance of Function by calling from_dict on the json representation
        function_model = Function.from_dict(function_model_json)
        assert function_model != False

        # Construct a model instance of Function by calling from_dict on the json representation
        function_model_dict = Function.from_dict(function_model_json).__dict__
        function_model2 = Function(**function_model_dict)

        # Verify the model instances are equivalent
        assert function_model == function_model2

        # Convert model instance back to dict and verify no loss of data
        function_model_json2 = function_model.to_dict()
        assert function_model_json2 == function_model_json


class TestModel_FunctionList:
    """
    Test Class for FunctionList
    """

    def test_function_list_serialization(self):
        """
        Test serialization/deserialization for FunctionList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        list_first_metadata_model = {}  # ListFirstMetadata
        list_first_metadata_model['href'] = 'testString'

        env_var_model = {}  # EnvVar
        env_var_model['key'] = 'MY_VARIABLE'
        env_var_model['name'] = 'SOME'
        env_var_model['prefix'] = 'PREFIX_'
        env_var_model['reference'] = 'my-secret'
        env_var_model['type'] = 'literal'
        env_var_model['value'] = 'VALUE'

        function_status_model = {}  # FunctionStatus

        function_model = {}  # Function
        function_model['code_binary'] = True
        function_model['code_main'] = 'main'
        function_model['code_reference'] = 'icr.io/codeengine/samples/function-nodejs-codebundle'
        function_model['code_secret'] = 'my-secret'
        function_model['computed_env_variables'] = [env_var_model]
        function_model['entity_tag'] = '1'
        function_model['managed_domain_mappings'] = 'local_public'
        function_model['name'] = 'my-function'
        function_model['run_env_variables'] = [env_var_model]
        function_model['runtime'] = 'nodejs-18'
        function_model['scale_concurrency'] = 1
        function_model['scale_cpu_limit'] = '0.5'
        function_model['scale_down_delay'] = 0
        function_model['scale_max_execution_time'] = 60
        function_model['scale_memory_limit'] = '2G'
        function_model['status_details'] = function_status_model

        list_next_metadata_model = {}  # ListNextMetadata
        list_next_metadata_model['href'] = 'testString'
        list_next_metadata_model['start'] = 'testString'

        # Construct a json representation of a FunctionList model
        function_list_model_json = {}
        function_list_model_json['first'] = list_first_metadata_model
        function_list_model_json['functions'] = [function_model]
        function_list_model_json['limit'] = 100
        function_list_model_json['next'] = list_next_metadata_model

        # Construct a model instance of FunctionList by calling from_dict on the json representation
        function_list_model = FunctionList.from_dict(function_list_model_json)
        assert function_list_model != False

        # Construct a model instance of FunctionList by calling from_dict on the json representation
        function_list_model_dict = FunctionList.from_dict(function_list_model_json).__dict__
        function_list_model2 = FunctionList(**function_list_model_dict)

        # Verify the model instances are equivalent
        assert function_list_model == function_list_model2

        # Convert model instance back to dict and verify no loss of data
        function_list_model_json2 = function_list_model.to_dict()
        assert function_list_model_json2 == function_list_model_json


class TestModel_FunctionPatch:
    """
    Test Class for FunctionPatch
    """

    def test_function_patch_serialization(self):
        """
        Test serialization/deserialization for FunctionPatch
        """

        # Construct dict forms of any model objects needed in order to build this model.

        env_var_prototype_model = {}  # EnvVarPrototype
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'SOME'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'VALUE'

        # Construct a json representation of a FunctionPatch model
        function_patch_model_json = {}
        function_patch_model_json['code_binary'] = False
        function_patch_model_json['code_main'] = 'main'
        function_patch_model_json['code_reference'] = 'data:text/plain;base64,<base64encoded-source-code>'
        function_patch_model_json['code_secret'] = 'my-secret'
        function_patch_model_json['managed_domain_mappings'] = 'local_public'
        function_patch_model_json['run_env_variables'] = [env_var_prototype_model]
        function_patch_model_json['runtime'] = 'nodejs-18'
        function_patch_model_json['scale_concurrency'] = 1
        function_patch_model_json['scale_cpu_limit'] = '1'
        function_patch_model_json['scale_down_delay'] = 300
        function_patch_model_json['scale_max_execution_time'] = 60
        function_patch_model_json['scale_memory_limit'] = '1G'

        # Construct a model instance of FunctionPatch by calling from_dict on the json representation
        function_patch_model = FunctionPatch.from_dict(function_patch_model_json)
        assert function_patch_model != False

        # Construct a model instance of FunctionPatch by calling from_dict on the json representation
        function_patch_model_dict = FunctionPatch.from_dict(function_patch_model_json).__dict__
        function_patch_model2 = FunctionPatch(**function_patch_model_dict)

        # Verify the model instances are equivalent
        assert function_patch_model == function_patch_model2

        # Convert model instance back to dict and verify no loss of data
        function_patch_model_json2 = function_patch_model.to_dict()
        assert function_patch_model_json2 == function_patch_model_json


class TestModel_FunctionRuntime:
    """
    Test Class for FunctionRuntime
    """

    def test_function_runtime_serialization(self):
        """
        Test serialization/deserialization for FunctionRuntime
        """

        # Construct a json representation of a FunctionRuntime model
        function_runtime_model_json = {}

        # Construct a model instance of FunctionRuntime by calling from_dict on the json representation
        function_runtime_model = FunctionRuntime.from_dict(function_runtime_model_json)
        assert function_runtime_model != False

        # Construct a model instance of FunctionRuntime by calling from_dict on the json representation
        function_runtime_model_dict = FunctionRuntime.from_dict(function_runtime_model_json).__dict__
        function_runtime_model2 = FunctionRuntime(**function_runtime_model_dict)

        # Verify the model instances are equivalent
        assert function_runtime_model == function_runtime_model2

        # Convert model instance back to dict and verify no loss of data
        function_runtime_model_json2 = function_runtime_model.to_dict()
        assert function_runtime_model_json2 == function_runtime_model_json


class TestModel_FunctionRuntimeList:
    """
    Test Class for FunctionRuntimeList
    """

    def test_function_runtime_list_serialization(self):
        """
        Test serialization/deserialization for FunctionRuntimeList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        function_runtime_model = {}  # FunctionRuntime

        # Construct a json representation of a FunctionRuntimeList model
        function_runtime_list_model_json = {}
        function_runtime_list_model_json['function_runtimes'] = [function_runtime_model]

        # Construct a model instance of FunctionRuntimeList by calling from_dict on the json representation
        function_runtime_list_model = FunctionRuntimeList.from_dict(function_runtime_list_model_json)
        assert function_runtime_list_model != False

        # Construct a model instance of FunctionRuntimeList by calling from_dict on the json representation
        function_runtime_list_model_dict = FunctionRuntimeList.from_dict(function_runtime_list_model_json).__dict__
        function_runtime_list_model2 = FunctionRuntimeList(**function_runtime_list_model_dict)

        # Verify the model instances are equivalent
        assert function_runtime_list_model == function_runtime_list_model2

        # Convert model instance back to dict and verify no loss of data
        function_runtime_list_model_json2 = function_runtime_list_model.to_dict()
        assert function_runtime_list_model_json2 == function_runtime_list_model_json


class TestModel_FunctionStatus:
    """
    Test Class for FunctionStatus
    """

    def test_function_status_serialization(self):
        """
        Test serialization/deserialization for FunctionStatus
        """

        # Construct a json representation of a FunctionStatus model
        function_status_model_json = {}

        # Construct a model instance of FunctionStatus by calling from_dict on the json representation
        function_status_model = FunctionStatus.from_dict(function_status_model_json)
        assert function_status_model != False

        # Construct a model instance of FunctionStatus by calling from_dict on the json representation
        function_status_model_dict = FunctionStatus.from_dict(function_status_model_json).__dict__
        function_status_model2 = FunctionStatus(**function_status_model_dict)

        # Verify the model instances are equivalent
        assert function_status_model == function_status_model2

        # Convert model instance back to dict and verify no loss of data
        function_status_model_json2 = function_status_model.to_dict()
        assert function_status_model_json2 == function_status_model_json


class TestModel_Job:
    """
    Test Class for Job
    """

    def test_job_serialization(self):
        """
        Test serialization/deserialization for Job
        """

        # Construct dict forms of any model objects needed in order to build this model.

        env_var_model = {}  # EnvVar
        env_var_model['key'] = 'MY_VARIABLE'
        env_var_model['name'] = 'SOME'
        env_var_model['prefix'] = 'PREFIX_'
        env_var_model['reference'] = 'my-secret'
        env_var_model['type'] = 'literal'
        env_var_model['value'] = 'VALUE'

        volume_mount_model = {}  # VolumeMount
        volume_mount_model['mount_path'] = '/app'
        volume_mount_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_model['reference'] = 'my-secret'
        volume_mount_model['type'] = 'secret'

        # Construct a json representation of a Job model
        job_model_json = {}
        job_model_json['computed_env_variables'] = [env_var_model]
        job_model_json['entity_tag'] = '2385407409'
        job_model_json['image_reference'] = 'icr.io/codeengine/helloworld'
        job_model_json['image_secret'] = 'my-secret'
        job_model_json['name'] = 'my-job'
        job_model_json['run_arguments'] = ['testString']
        job_model_json['run_as_user'] = 1001
        job_model_json['run_commands'] = ['testString']
        job_model_json['run_env_variables'] = [env_var_model]
        job_model_json['run_mode'] = 'task'
        job_model_json['run_service_account'] = 'default'
        job_model_json['run_volume_mounts'] = [volume_mount_model]
        job_model_json['scale_array_spec'] = '1-5,7-8,10'
        job_model_json['scale_cpu_limit'] = '1'
        job_model_json['scale_ephemeral_storage_limit'] = '4G'
        job_model_json['scale_max_execution_time'] = 7200
        job_model_json['scale_memory_limit'] = '4G'
        job_model_json['scale_retry_limit'] = 3

        # Construct a model instance of Job by calling from_dict on the json representation
        job_model = Job.from_dict(job_model_json)
        assert job_model != False

        # Construct a model instance of Job by calling from_dict on the json representation
        job_model_dict = Job.from_dict(job_model_json).__dict__
        job_model2 = Job(**job_model_dict)

        # Verify the model instances are equivalent
        assert job_model == job_model2

        # Convert model instance back to dict and verify no loss of data
        job_model_json2 = job_model.to_dict()
        assert job_model_json2 == job_model_json


class TestModel_JobList:
    """
    Test Class for JobList
    """

    def test_job_list_serialization(self):
        """
        Test serialization/deserialization for JobList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        list_first_metadata_model = {}  # ListFirstMetadata
        list_first_metadata_model['href'] = 'testString'

        env_var_model = {}  # EnvVar
        env_var_model['key'] = 'MY_VARIABLE'
        env_var_model['name'] = 'SOME'
        env_var_model['prefix'] = 'PREFIX_'
        env_var_model['reference'] = 'my-secret'
        env_var_model['type'] = 'literal'
        env_var_model['value'] = 'VALUE'

        volume_mount_model = {}  # VolumeMount
        volume_mount_model['mount_path'] = '/app'
        volume_mount_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_model['reference'] = 'my-secret'
        volume_mount_model['type'] = 'secret'

        job_model = {}  # Job
        job_model['computed_env_variables'] = [env_var_model]
        job_model['entity_tag'] = '2386231540'
        job_model['image_reference'] = 'icr.io/codeengine/helloworld'
        job_model['image_secret'] = 'my-secret'
        job_model['name'] = 'my-job'
        job_model['run_arguments'] = []
        job_model['run_as_user'] = 1001
        job_model['run_commands'] = []
        job_model['run_env_variables'] = [env_var_model]
        job_model['run_mode'] = 'task'
        job_model['run_service_account'] = 'default'
        job_model['run_volume_mounts'] = [volume_mount_model]
        job_model['scale_array_spec'] = '0'
        job_model['scale_cpu_limit'] = '1'
        job_model['scale_ephemeral_storage_limit'] = '400M'
        job_model['scale_max_execution_time'] = 7200
        job_model['scale_memory_limit'] = '4G'
        job_model['scale_retry_limit'] = 3

        list_next_metadata_model = {}  # ListNextMetadata
        list_next_metadata_model['href'] = 'testString'
        list_next_metadata_model['start'] = 'testString'

        # Construct a json representation of a JobList model
        job_list_model_json = {}
        job_list_model_json['first'] = list_first_metadata_model
        job_list_model_json['jobs'] = [job_model]
        job_list_model_json['limit'] = 100
        job_list_model_json['next'] = list_next_metadata_model

        # Construct a model instance of JobList by calling from_dict on the json representation
        job_list_model = JobList.from_dict(job_list_model_json)
        assert job_list_model != False

        # Construct a model instance of JobList by calling from_dict on the json representation
        job_list_model_dict = JobList.from_dict(job_list_model_json).__dict__
        job_list_model2 = JobList(**job_list_model_dict)

        # Verify the model instances are equivalent
        assert job_list_model == job_list_model2

        # Convert model instance back to dict and verify no loss of data
        job_list_model_json2 = job_list_model.to_dict()
        assert job_list_model_json2 == job_list_model_json


class TestModel_JobPatch:
    """
    Test Class for JobPatch
    """

    def test_job_patch_serialization(self):
        """
        Test serialization/deserialization for JobPatch
        """

        # Construct dict forms of any model objects needed in order to build this model.

        env_var_prototype_model = {}  # EnvVarPrototype
        env_var_prototype_model['key'] = 'MY_VARIABLE'
        env_var_prototype_model['name'] = 'MY_PROPERTY'
        env_var_prototype_model['prefix'] = 'PREFIX_'
        env_var_prototype_model['reference'] = 'my-secret'
        env_var_prototype_model['type'] = 'literal'
        env_var_prototype_model['value'] = 'OTHER'

        volume_mount_prototype_model = {}  # VolumeMountPrototype
        volume_mount_prototype_model['mount_path'] = '/app'
        volume_mount_prototype_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_prototype_model['reference'] = 'my-secret'
        volume_mount_prototype_model['type'] = 'secret'

        # Construct a json representation of a JobPatch model
        job_patch_model_json = {}
        job_patch_model_json['image_reference'] = 'icr.io/codeengine/helloworld'
        job_patch_model_json['image_secret'] = 'my-secret'
        job_patch_model_json['run_arguments'] = ['testString']
        job_patch_model_json['run_as_user'] = 1001
        job_patch_model_json['run_commands'] = ['testString']
        job_patch_model_json['run_env_variables'] = [env_var_prototype_model]
        job_patch_model_json['run_mode'] = 'task'
        job_patch_model_json['run_service_account'] = 'default'
        job_patch_model_json['run_volume_mounts'] = [volume_mount_prototype_model]
        job_patch_model_json['scale_array_spec'] = '1-5,7-8,10'
        job_patch_model_json['scale_cpu_limit'] = '1'
        job_patch_model_json['scale_ephemeral_storage_limit'] = '4G'
        job_patch_model_json['scale_max_execution_time'] = 7200
        job_patch_model_json['scale_memory_limit'] = '4G'
        job_patch_model_json['scale_retry_limit'] = 3

        # Construct a model instance of JobPatch by calling from_dict on the json representation
        job_patch_model = JobPatch.from_dict(job_patch_model_json)
        assert job_patch_model != False

        # Construct a model instance of JobPatch by calling from_dict on the json representation
        job_patch_model_dict = JobPatch.from_dict(job_patch_model_json).__dict__
        job_patch_model2 = JobPatch(**job_patch_model_dict)

        # Verify the model instances are equivalent
        assert job_patch_model == job_patch_model2

        # Convert model instance back to dict and verify no loss of data
        job_patch_model_json2 = job_patch_model.to_dict()
        assert job_patch_model_json2 == job_patch_model_json


class TestModel_JobRun:
    """
    Test Class for JobRun
    """

    def test_job_run_serialization(self):
        """
        Test serialization/deserialization for JobRun
        """

        # Construct dict forms of any model objects needed in order to build this model.

        env_var_model = {}  # EnvVar
        env_var_model['key'] = 'MY_VARIABLE'
        env_var_model['name'] = 'SOME'
        env_var_model['prefix'] = 'PREFIX_'
        env_var_model['reference'] = 'my-secret'
        env_var_model['type'] = 'literal'
        env_var_model['value'] = 'VALUE'

        volume_mount_model = {}  # VolumeMount
        volume_mount_model['mount_path'] = '/app'
        volume_mount_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_model['reference'] = 'my-secret'
        volume_mount_model['type'] = 'secret'

        job_run_status_model = {}  # JobRunStatus

        # Construct a json representation of a JobRun model
        job_run_model_json = {}
        job_run_model_json['computed_env_variables'] = [env_var_model]
        job_run_model_json['image_reference'] = 'icr.io/codeengine/helloworld'
        job_run_model_json['image_secret'] = 'my-secret'
        job_run_model_json['job_name'] = 'my-job'
        job_run_model_json['name'] = 'my-job-run'
        job_run_model_json['run_arguments'] = ['testString']
        job_run_model_json['run_as_user'] = 1001
        job_run_model_json['run_commands'] = ['testString']
        job_run_model_json['run_env_variables'] = [env_var_model]
        job_run_model_json['run_mode'] = 'task'
        job_run_model_json['run_service_account'] = 'default'
        job_run_model_json['run_volume_mounts'] = [volume_mount_model]
        job_run_model_json['scale_array_size_variable_override'] = 2
        job_run_model_json['scale_array_spec'] = '1-5,7-8,10'
        job_run_model_json['scale_cpu_limit'] = '1'
        job_run_model_json['scale_ephemeral_storage_limit'] = '4G'
        job_run_model_json['scale_max_execution_time'] = 7200
        job_run_model_json['scale_memory_limit'] = '4G'
        job_run_model_json['scale_retry_limit'] = 3
        job_run_model_json['status_details'] = job_run_status_model

        # Construct a model instance of JobRun by calling from_dict on the json representation
        job_run_model = JobRun.from_dict(job_run_model_json)
        assert job_run_model != False

        # Construct a model instance of JobRun by calling from_dict on the json representation
        job_run_model_dict = JobRun.from_dict(job_run_model_json).__dict__
        job_run_model2 = JobRun(**job_run_model_dict)

        # Verify the model instances are equivalent
        assert job_run_model == job_run_model2

        # Convert model instance back to dict and verify no loss of data
        job_run_model_json2 = job_run_model.to_dict()
        assert job_run_model_json2 == job_run_model_json


class TestModel_JobRunList:
    """
    Test Class for JobRunList
    """

    def test_job_run_list_serialization(self):
        """
        Test serialization/deserialization for JobRunList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        list_first_metadata_model = {}  # ListFirstMetadata
        list_first_metadata_model['href'] = 'testString'

        env_var_model = {}  # EnvVar
        env_var_model['key'] = 'MY_VARIABLE'
        env_var_model['name'] = 'SOME'
        env_var_model['prefix'] = 'PREFIX_'
        env_var_model['reference'] = 'my-secret'
        env_var_model['type'] = 'literal'
        env_var_model['value'] = 'VALUE'

        volume_mount_model = {}  # VolumeMount
        volume_mount_model['mount_path'] = '/app'
        volume_mount_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_model['reference'] = 'my-secret'
        volume_mount_model['type'] = 'secret'

        job_run_status_model = {}  # JobRunStatus

        job_run_model = {}  # JobRun
        job_run_model['computed_env_variables'] = [env_var_model]
        job_run_model['image_reference'] = 'icr.io/codeengine/helloworld'
        job_run_model['image_secret'] = 'my-secret'
        job_run_model['job_name'] = 'my-job'
        job_run_model['name'] = 'my-job-run-1'
        job_run_model['run_arguments'] = []
        job_run_model['run_as_user'] = 1001
        job_run_model['run_commands'] = []
        job_run_model['run_env_variables'] = [env_var_model]
        job_run_model['run_mode'] = 'task'
        job_run_model['run_service_account'] = 'default'
        job_run_model['run_volume_mounts'] = [volume_mount_model]
        job_run_model['scale_array_size_variable_override'] = 2
        job_run_model['scale_array_spec'] = '0'
        job_run_model['scale_cpu_limit'] = '1'
        job_run_model['scale_ephemeral_storage_limit'] = '400M'
        job_run_model['scale_max_execution_time'] = 7200
        job_run_model['scale_memory_limit'] = '4G'
        job_run_model['scale_retry_limit'] = 3
        job_run_model['status_details'] = job_run_status_model

        list_next_metadata_model = {}  # ListNextMetadata
        list_next_metadata_model['href'] = 'testString'
        list_next_metadata_model['start'] = 'testString'

        # Construct a json representation of a JobRunList model
        job_run_list_model_json = {}
        job_run_list_model_json['first'] = list_first_metadata_model
        job_run_list_model_json['job_runs'] = [job_run_model]
        job_run_list_model_json['limit'] = 100
        job_run_list_model_json['next'] = list_next_metadata_model

        # Construct a model instance of JobRunList by calling from_dict on the json representation
        job_run_list_model = JobRunList.from_dict(job_run_list_model_json)
        assert job_run_list_model != False

        # Construct a model instance of JobRunList by calling from_dict on the json representation
        job_run_list_model_dict = JobRunList.from_dict(job_run_list_model_json).__dict__
        job_run_list_model2 = JobRunList(**job_run_list_model_dict)

        # Verify the model instances are equivalent
        assert job_run_list_model == job_run_list_model2

        # Convert model instance back to dict and verify no loss of data
        job_run_list_model_json2 = job_run_list_model.to_dict()
        assert job_run_list_model_json2 == job_run_list_model_json


class TestModel_JobRunStatus:
    """
    Test Class for JobRunStatus
    """

    def test_job_run_status_serialization(self):
        """
        Test serialization/deserialization for JobRunStatus
        """

        # Construct a json representation of a JobRunStatus model
        job_run_status_model_json = {}

        # Construct a model instance of JobRunStatus by calling from_dict on the json representation
        job_run_status_model = JobRunStatus.from_dict(job_run_status_model_json)
        assert job_run_status_model != False

        # Construct a model instance of JobRunStatus by calling from_dict on the json representation
        job_run_status_model_dict = JobRunStatus.from_dict(job_run_status_model_json).__dict__
        job_run_status_model2 = JobRunStatus(**job_run_status_model_dict)

        # Verify the model instances are equivalent
        assert job_run_status_model == job_run_status_model2

        # Convert model instance back to dict and verify no loss of data
        job_run_status_model_json2 = job_run_status_model.to_dict()
        assert job_run_status_model_json2 == job_run_status_model_json


class TestModel_ListFirstMetadata:
    """
    Test Class for ListFirstMetadata
    """

    def test_list_first_metadata_serialization(self):
        """
        Test serialization/deserialization for ListFirstMetadata
        """

        # Construct a json representation of a ListFirstMetadata model
        list_first_metadata_model_json = {}
        list_first_metadata_model_json['href'] = 'testString'

        # Construct a model instance of ListFirstMetadata by calling from_dict on the json representation
        list_first_metadata_model = ListFirstMetadata.from_dict(list_first_metadata_model_json)
        assert list_first_metadata_model != False

        # Construct a model instance of ListFirstMetadata by calling from_dict on the json representation
        list_first_metadata_model_dict = ListFirstMetadata.from_dict(list_first_metadata_model_json).__dict__
        list_first_metadata_model2 = ListFirstMetadata(**list_first_metadata_model_dict)

        # Verify the model instances are equivalent
        assert list_first_metadata_model == list_first_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        list_first_metadata_model_json2 = list_first_metadata_model.to_dict()
        assert list_first_metadata_model_json2 == list_first_metadata_model_json


class TestModel_ListNextMetadata:
    """
    Test Class for ListNextMetadata
    """

    def test_list_next_metadata_serialization(self):
        """
        Test serialization/deserialization for ListNextMetadata
        """

        # Construct a json representation of a ListNextMetadata model
        list_next_metadata_model_json = {}
        list_next_metadata_model_json['href'] = 'testString'
        list_next_metadata_model_json['start'] = 'testString'

        # Construct a model instance of ListNextMetadata by calling from_dict on the json representation
        list_next_metadata_model = ListNextMetadata.from_dict(list_next_metadata_model_json)
        assert list_next_metadata_model != False

        # Construct a model instance of ListNextMetadata by calling from_dict on the json representation
        list_next_metadata_model_dict = ListNextMetadata.from_dict(list_next_metadata_model_json).__dict__
        list_next_metadata_model2 = ListNextMetadata(**list_next_metadata_model_dict)

        # Verify the model instances are equivalent
        assert list_next_metadata_model == list_next_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        list_next_metadata_model_json2 = list_next_metadata_model.to_dict()
        assert list_next_metadata_model_json2 == list_next_metadata_model_json


class TestModel_OperatorSecretProps:
    """
    Test Class for OperatorSecretProps
    """

    def test_operator_secret_props_serialization(self):
        """
        Test serialization/deserialization for OperatorSecretProps
        """

        # Construct dict forms of any model objects needed in order to build this model.

        service_id_ref_model = {}  # ServiceIDRef
        service_id_ref_model['crn'] = 'testString'
        service_id_ref_model['id'] = 'ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637'

        # Construct a json representation of a OperatorSecretProps model
        operator_secret_props_model_json = {}
        operator_secret_props_model_json['apikey_id'] = 'ApiKey-17041d26-55e4-40a8-8ab5-5a69b68e204b'
        operator_secret_props_model_json['resource_group_ids'] = ['testString']
        operator_secret_props_model_json['serviceid'] = service_id_ref_model
        operator_secret_props_model_json['user_managed'] = True

        # Construct a model instance of OperatorSecretProps by calling from_dict on the json representation
        operator_secret_props_model = OperatorSecretProps.from_dict(operator_secret_props_model_json)
        assert operator_secret_props_model != False

        # Construct a model instance of OperatorSecretProps by calling from_dict on the json representation
        operator_secret_props_model_dict = OperatorSecretProps.from_dict(operator_secret_props_model_json).__dict__
        operator_secret_props_model2 = OperatorSecretProps(**operator_secret_props_model_dict)

        # Verify the model instances are equivalent
        assert operator_secret_props_model == operator_secret_props_model2

        # Convert model instance back to dict and verify no loss of data
        operator_secret_props_model_json2 = operator_secret_props_model.to_dict()
        assert operator_secret_props_model_json2 == operator_secret_props_model_json


class TestModel_OperatorSecretPrototypeProps:
    """
    Test Class for OperatorSecretPrototypeProps
    """

    def test_operator_secret_prototype_props_serialization(self):
        """
        Test serialization/deserialization for OperatorSecretPrototypeProps
        """

        # Construct dict forms of any model objects needed in order to build this model.

        service_id_ref_prototype_model = {}  # ServiceIDRefPrototype
        service_id_ref_prototype_model['id'] = 'ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637'

        # Construct a json representation of a OperatorSecretPrototypeProps model
        operator_secret_prototype_props_model_json = {}
        operator_secret_prototype_props_model_json['resource_group_ids'] = ['testString']
        operator_secret_prototype_props_model_json['serviceid'] = service_id_ref_prototype_model

        # Construct a model instance of OperatorSecretPrototypeProps by calling from_dict on the json representation
        operator_secret_prototype_props_model = OperatorSecretPrototypeProps.from_dict(
            operator_secret_prototype_props_model_json
        )
        assert operator_secret_prototype_props_model != False

        # Construct a model instance of OperatorSecretPrototypeProps by calling from_dict on the json representation
        operator_secret_prototype_props_model_dict = OperatorSecretPrototypeProps.from_dict(
            operator_secret_prototype_props_model_json
        ).__dict__
        operator_secret_prototype_props_model2 = OperatorSecretPrototypeProps(
            **operator_secret_prototype_props_model_dict
        )

        # Verify the model instances are equivalent
        assert operator_secret_prototype_props_model == operator_secret_prototype_props_model2

        # Convert model instance back to dict and verify no loss of data
        operator_secret_prototype_props_model_json2 = operator_secret_prototype_props_model.to_dict()
        assert operator_secret_prototype_props_model_json2 == operator_secret_prototype_props_model_json


class TestModel_Probe:
    """
    Test Class for Probe
    """

    def test_probe_serialization(self):
        """
        Test serialization/deserialization for Probe
        """

        # Construct a json representation of a Probe model
        probe_model_json = {}
        probe_model_json['failure_threshold'] = 5
        probe_model_json['initial_delay'] = 5
        probe_model_json['interval'] = 5
        probe_model_json['path'] = 'testString'
        probe_model_json['port'] = 8080
        probe_model_json['timeout'] = 300
        probe_model_json['type'] = 'tcp'

        # Construct a model instance of Probe by calling from_dict on the json representation
        probe_model = Probe.from_dict(probe_model_json)
        assert probe_model != False

        # Construct a model instance of Probe by calling from_dict on the json representation
        probe_model_dict = Probe.from_dict(probe_model_json).__dict__
        probe_model2 = Probe(**probe_model_dict)

        # Verify the model instances are equivalent
        assert probe_model == probe_model2

        # Convert model instance back to dict and verify no loss of data
        probe_model_json2 = probe_model.to_dict()
        assert probe_model_json2 == probe_model_json


class TestModel_ProbePrototype:
    """
    Test Class for ProbePrototype
    """

    def test_probe_prototype_serialization(self):
        """
        Test serialization/deserialization for ProbePrototype
        """

        # Construct a json representation of a ProbePrototype model
        probe_prototype_model_json = {}
        probe_prototype_model_json['failure_threshold'] = 5
        probe_prototype_model_json['initial_delay'] = 5
        probe_prototype_model_json['interval'] = 5
        probe_prototype_model_json['path'] = 'testString'
        probe_prototype_model_json['port'] = 8080
        probe_prototype_model_json['timeout'] = 300
        probe_prototype_model_json['type'] = 'tcp'

        # Construct a model instance of ProbePrototype by calling from_dict on the json representation
        probe_prototype_model = ProbePrototype.from_dict(probe_prototype_model_json)
        assert probe_prototype_model != False

        # Construct a model instance of ProbePrototype by calling from_dict on the json representation
        probe_prototype_model_dict = ProbePrototype.from_dict(probe_prototype_model_json).__dict__
        probe_prototype_model2 = ProbePrototype(**probe_prototype_model_dict)

        # Verify the model instances are equivalent
        assert probe_prototype_model == probe_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        probe_prototype_model_json2 = probe_prototype_model.to_dict()
        assert probe_prototype_model_json2 == probe_prototype_model_json


class TestModel_Project:
    """
    Test Class for Project
    """

    def test_project_serialization(self):
        """
        Test serialization/deserialization for Project
        """

        # Construct a json representation of a Project model
        project_model_json = {}
        project_model_json['name'] = 'project-name'
        project_model_json['resource_group_id'] = '5c49eabcf5e85881a37e2d100a33b3df'

        # Construct a model instance of Project by calling from_dict on the json representation
        project_model = Project.from_dict(project_model_json)
        assert project_model != False

        # Construct a model instance of Project by calling from_dict on the json representation
        project_model_dict = Project.from_dict(project_model_json).__dict__
        project_model2 = Project(**project_model_dict)

        # Verify the model instances are equivalent
        assert project_model == project_model2

        # Convert model instance back to dict and verify no loss of data
        project_model_json2 = project_model.to_dict()
        assert project_model_json2 == project_model_json


class TestModel_ProjectEgressIPAddresses:
    """
    Test Class for ProjectEgressIPAddresses
    """

    def test_project_egress_ip_addresses_serialization(self):
        """
        Test serialization/deserialization for ProjectEgressIPAddresses
        """

        # Construct a json representation of a ProjectEgressIPAddresses model
        project_egress_ip_addresses_model_json = {}
        project_egress_ip_addresses_model_json['private'] = ['testString']
        project_egress_ip_addresses_model_json['public'] = ['testString']

        # Construct a model instance of ProjectEgressIPAddresses by calling from_dict on the json representation
        project_egress_ip_addresses_model = ProjectEgressIPAddresses.from_dict(project_egress_ip_addresses_model_json)
        assert project_egress_ip_addresses_model != False

        # Construct a model instance of ProjectEgressIPAddresses by calling from_dict on the json representation
        project_egress_ip_addresses_model_dict = ProjectEgressIPAddresses.from_dict(
            project_egress_ip_addresses_model_json
        ).__dict__
        project_egress_ip_addresses_model2 = ProjectEgressIPAddresses(**project_egress_ip_addresses_model_dict)

        # Verify the model instances are equivalent
        assert project_egress_ip_addresses_model == project_egress_ip_addresses_model2

        # Convert model instance back to dict and verify no loss of data
        project_egress_ip_addresses_model_json2 = project_egress_ip_addresses_model.to_dict()
        assert project_egress_ip_addresses_model_json2 == project_egress_ip_addresses_model_json


class TestModel_ProjectList:
    """
    Test Class for ProjectList
    """

    def test_project_list_serialization(self):
        """
        Test serialization/deserialization for ProjectList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        list_first_metadata_model = {}  # ListFirstMetadata
        list_first_metadata_model['href'] = 'testString'

        list_next_metadata_model = {}  # ListNextMetadata
        list_next_metadata_model['href'] = 'testString'
        list_next_metadata_model['start'] = 'testString'

        project_model = {}  # Project
        project_model['name'] = 'test_project'
        project_model['resource_group_id'] = 'b91e849cedb04e7e92bd68c040c672dc'

        # Construct a json representation of a ProjectList model
        project_list_model_json = {}
        project_list_model_json['first'] = list_first_metadata_model
        project_list_model_json['limit'] = 100
        project_list_model_json['next'] = list_next_metadata_model
        project_list_model_json['projects'] = [project_model]

        # Construct a model instance of ProjectList by calling from_dict on the json representation
        project_list_model = ProjectList.from_dict(project_list_model_json)
        assert project_list_model != False

        # Construct a model instance of ProjectList by calling from_dict on the json representation
        project_list_model_dict = ProjectList.from_dict(project_list_model_json).__dict__
        project_list_model2 = ProjectList(**project_list_model_dict)

        # Verify the model instances are equivalent
        assert project_list_model == project_list_model2

        # Convert model instance back to dict and verify no loss of data
        project_list_model_json2 = project_list_model.to_dict()
        assert project_list_model_json2 == project_list_model_json


class TestModel_ProjectStatusDetails:
    """
    Test Class for ProjectStatusDetails
    """

    def test_project_status_details_serialization(self):
        """
        Test serialization/deserialization for ProjectStatusDetails
        """

        # Construct a json representation of a ProjectStatusDetails model
        project_status_details_model_json = {}
        project_status_details_model_json['domain'] = 'unknown'
        project_status_details_model_json['project'] = 'enabled'
        project_status_details_model_json['vpe_not_enabled'] = True

        # Construct a model instance of ProjectStatusDetails by calling from_dict on the json representation
        project_status_details_model = ProjectStatusDetails.from_dict(project_status_details_model_json)
        assert project_status_details_model != False

        # Construct a model instance of ProjectStatusDetails by calling from_dict on the json representation
        project_status_details_model_dict = ProjectStatusDetails.from_dict(project_status_details_model_json).__dict__
        project_status_details_model2 = ProjectStatusDetails(**project_status_details_model_dict)

        # Verify the model instances are equivalent
        assert project_status_details_model == project_status_details_model2

        # Convert model instance back to dict and verify no loss of data
        project_status_details_model_json2 = project_status_details_model.to_dict()
        assert project_status_details_model_json2 == project_status_details_model_json


class TestModel_ResourceKeyRef:
    """
    Test Class for ResourceKeyRef
    """

    def test_resource_key_ref_serialization(self):
        """
        Test serialization/deserialization for ResourceKeyRef
        """

        # Construct a json representation of a ResourceKeyRef model
        resource_key_ref_model_json = {}
        resource_key_ref_model_json['id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'
        resource_key_ref_model_json['name'] = 'testString'

        # Construct a model instance of ResourceKeyRef by calling from_dict on the json representation
        resource_key_ref_model = ResourceKeyRef.from_dict(resource_key_ref_model_json)
        assert resource_key_ref_model != False

        # Construct a model instance of ResourceKeyRef by calling from_dict on the json representation
        resource_key_ref_model_dict = ResourceKeyRef.from_dict(resource_key_ref_model_json).__dict__
        resource_key_ref_model2 = ResourceKeyRef(**resource_key_ref_model_dict)

        # Verify the model instances are equivalent
        assert resource_key_ref_model == resource_key_ref_model2

        # Convert model instance back to dict and verify no loss of data
        resource_key_ref_model_json2 = resource_key_ref_model.to_dict()
        assert resource_key_ref_model_json2 == resource_key_ref_model_json


class TestModel_ResourceKeyRefPrototype:
    """
    Test Class for ResourceKeyRefPrototype
    """

    def test_resource_key_ref_prototype_serialization(self):
        """
        Test serialization/deserialization for ResourceKeyRefPrototype
        """

        # Construct a json representation of a ResourceKeyRefPrototype model
        resource_key_ref_prototype_model_json = {}
        resource_key_ref_prototype_model_json['id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'

        # Construct a model instance of ResourceKeyRefPrototype by calling from_dict on the json representation
        resource_key_ref_prototype_model = ResourceKeyRefPrototype.from_dict(resource_key_ref_prototype_model_json)
        assert resource_key_ref_prototype_model != False

        # Construct a model instance of ResourceKeyRefPrototype by calling from_dict on the json representation
        resource_key_ref_prototype_model_dict = ResourceKeyRefPrototype.from_dict(
            resource_key_ref_prototype_model_json
        ).__dict__
        resource_key_ref_prototype_model2 = ResourceKeyRefPrototype(**resource_key_ref_prototype_model_dict)

        # Verify the model instances are equivalent
        assert resource_key_ref_prototype_model == resource_key_ref_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        resource_key_ref_prototype_model_json2 = resource_key_ref_prototype_model.to_dict()
        assert resource_key_ref_prototype_model_json2 == resource_key_ref_prototype_model_json


class TestModel_RoleRef:
    """
    Test Class for RoleRef
    """

    def test_role_ref_serialization(self):
        """
        Test serialization/deserialization for RoleRef
        """

        # Construct a json representation of a RoleRef model
        role_ref_model_json = {}
        role_ref_model_json['crn'] = 'crn:v1:bluemix:public:iam::::serviceRole:Writer'
        role_ref_model_json['name'] = 'Manager'

        # Construct a model instance of RoleRef by calling from_dict on the json representation
        role_ref_model = RoleRef.from_dict(role_ref_model_json)
        assert role_ref_model != False

        # Construct a model instance of RoleRef by calling from_dict on the json representation
        role_ref_model_dict = RoleRef.from_dict(role_ref_model_json).__dict__
        role_ref_model2 = RoleRef(**role_ref_model_dict)

        # Verify the model instances are equivalent
        assert role_ref_model == role_ref_model2

        # Convert model instance back to dict and verify no loss of data
        role_ref_model_json2 = role_ref_model.to_dict()
        assert role_ref_model_json2 == role_ref_model_json


class TestModel_RoleRefPrototype:
    """
    Test Class for RoleRefPrototype
    """

    def test_role_ref_prototype_serialization(self):
        """
        Test serialization/deserialization for RoleRefPrototype
        """

        # Construct a json representation of a RoleRefPrototype model
        role_ref_prototype_model_json = {}
        role_ref_prototype_model_json['crn'] = 'crn:v1:bluemix:public:iam::::serviceRole:Writer'

        # Construct a model instance of RoleRefPrototype by calling from_dict on the json representation
        role_ref_prototype_model = RoleRefPrototype.from_dict(role_ref_prototype_model_json)
        assert role_ref_prototype_model != False

        # Construct a model instance of RoleRefPrototype by calling from_dict on the json representation
        role_ref_prototype_model_dict = RoleRefPrototype.from_dict(role_ref_prototype_model_json).__dict__
        role_ref_prototype_model2 = RoleRefPrototype(**role_ref_prototype_model_dict)

        # Verify the model instances are equivalent
        assert role_ref_prototype_model == role_ref_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        role_ref_prototype_model_json2 = role_ref_prototype_model.to_dict()
        assert role_ref_prototype_model_json2 == role_ref_prototype_model_json


class TestModel_Secret:
    """
    Test Class for Secret
    """

    def test_secret_serialization(self):
        """
        Test serialization/deserialization for Secret
        """

        # Construct dict forms of any model objects needed in order to build this model.

        resource_key_ref_model = {}  # ResourceKeyRef
        resource_key_ref_model['id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'
        resource_key_ref_model['name'] = 'testString'

        role_ref_model = {}  # RoleRef
        role_ref_model['crn'] = 'crn:v1:bluemix:public:iam::::serviceRole:Writer'
        role_ref_model['name'] = 'Manager'

        service_instance_ref_model = {}  # ServiceInstanceRef
        service_instance_ref_model['id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'
        service_instance_ref_model['type'] = 'testString'

        service_id_ref_model = {}  # ServiceIDRef
        service_id_ref_model['crn'] = 'testString'
        service_id_ref_model['id'] = 'ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637'

        service_access_secret_props_model = {}  # ServiceAccessSecretProps
        service_access_secret_props_model['resource_key'] = resource_key_ref_model
        service_access_secret_props_model['role'] = role_ref_model
        service_access_secret_props_model['service_instance'] = service_instance_ref_model
        service_access_secret_props_model['serviceid'] = service_id_ref_model

        operator_secret_props_model = {}  # OperatorSecretProps
        operator_secret_props_model['apikey_id'] = 'ApiKey-17041d26-55e4-40a8-8ab5-5a69b68e204b'
        operator_secret_props_model['resource_group_ids'] = ['testString']
        operator_secret_props_model['serviceid'] = service_id_ref_model
        operator_secret_props_model['user_managed'] = True

        # Construct a json representation of a Secret model
        secret_model_json = {}
        secret_model_json['data'] = {'key1': 'testString'}
        secret_model_json['entity_tag'] = '2385407409'
        secret_model_json['format'] = 'generic'
        secret_model_json['name'] = 'my-secret'
        secret_model_json['service_access'] = service_access_secret_props_model
        secret_model_json['service_operator'] = operator_secret_props_model

        # Construct a model instance of Secret by calling from_dict on the json representation
        secret_model = Secret.from_dict(secret_model_json)
        assert secret_model != False

        # Construct a model instance of Secret by calling from_dict on the json representation
        secret_model_dict = Secret.from_dict(secret_model_json).__dict__
        secret_model2 = Secret(**secret_model_dict)

        # Verify the model instances are equivalent
        assert secret_model == secret_model2

        # Convert model instance back to dict and verify no loss of data
        secret_model_json2 = secret_model.to_dict()
        assert secret_model_json2 == secret_model_json


class TestModel_SecretList:
    """
    Test Class for SecretList
    """

    def test_secret_list_serialization(self):
        """
        Test serialization/deserialization for SecretList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        list_first_metadata_model = {}  # ListFirstMetadata
        list_first_metadata_model['href'] = 'testString'

        list_next_metadata_model = {}  # ListNextMetadata
        list_next_metadata_model['href'] = 'testString'
        list_next_metadata_model['start'] = 'testString'

        resource_key_ref_model = {}  # ResourceKeyRef
        resource_key_ref_model['id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'
        resource_key_ref_model['name'] = 'testString'

        role_ref_model = {}  # RoleRef
        role_ref_model['crn'] = 'crn:v1:bluemix:public:iam::::serviceRole:Writer'
        role_ref_model['name'] = 'Manager'

        service_instance_ref_model = {}  # ServiceInstanceRef
        service_instance_ref_model['id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'
        service_instance_ref_model['type'] = 'testString'

        service_id_ref_model = {}  # ServiceIDRef
        service_id_ref_model['crn'] = 'testString'
        service_id_ref_model['id'] = 'ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637'

        service_access_secret_props_model = {}  # ServiceAccessSecretProps
        service_access_secret_props_model['resource_key'] = resource_key_ref_model
        service_access_secret_props_model['role'] = role_ref_model
        service_access_secret_props_model['service_instance'] = service_instance_ref_model
        service_access_secret_props_model['serviceid'] = service_id_ref_model

        operator_secret_props_model = {}  # OperatorSecretProps
        operator_secret_props_model['apikey_id'] = 'ApiKey-17041d26-55e4-40a8-8ab5-5a69b68e204b'
        operator_secret_props_model['resource_group_ids'] = ['testString']
        operator_secret_props_model['serviceid'] = service_id_ref_model
        operator_secret_props_model['user_managed'] = True

        secret_model = {}  # Secret
        secret_model['data'] = {'key1': 'testString'}
        secret_model['entity_tag'] = '2386255530'
        secret_model['format'] = 'generic'
        secret_model['name'] = 'my-secret'
        secret_model['service_access'] = service_access_secret_props_model
        secret_model['service_operator'] = operator_secret_props_model

        # Construct a json representation of a SecretList model
        secret_list_model_json = {}
        secret_list_model_json['first'] = list_first_metadata_model
        secret_list_model_json['limit'] = 100
        secret_list_model_json['next'] = list_next_metadata_model
        secret_list_model_json['secrets'] = [secret_model]

        # Construct a model instance of SecretList by calling from_dict on the json representation
        secret_list_model = SecretList.from_dict(secret_list_model_json)
        assert secret_list_model != False

        # Construct a model instance of SecretList by calling from_dict on the json representation
        secret_list_model_dict = SecretList.from_dict(secret_list_model_json).__dict__
        secret_list_model2 = SecretList(**secret_list_model_dict)

        # Verify the model instances are equivalent
        assert secret_list_model == secret_list_model2

        # Convert model instance back to dict and verify no loss of data
        secret_list_model_json2 = secret_list_model.to_dict()
        assert secret_list_model_json2 == secret_list_model_json


class TestModel_ServiceAccessSecretProps:
    """
    Test Class for ServiceAccessSecretProps
    """

    def test_service_access_secret_props_serialization(self):
        """
        Test serialization/deserialization for ServiceAccessSecretProps
        """

        # Construct dict forms of any model objects needed in order to build this model.

        resource_key_ref_model = {}  # ResourceKeyRef
        resource_key_ref_model['id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'
        resource_key_ref_model['name'] = 'testString'

        role_ref_model = {}  # RoleRef
        role_ref_model['crn'] = 'crn:v1:bluemix:public:iam::::serviceRole:Writer'
        role_ref_model['name'] = 'Manager'

        service_instance_ref_model = {}  # ServiceInstanceRef
        service_instance_ref_model['id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'
        service_instance_ref_model['type'] = 'testString'

        service_id_ref_model = {}  # ServiceIDRef
        service_id_ref_model['crn'] = 'testString'
        service_id_ref_model['id'] = 'ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637'

        # Construct a json representation of a ServiceAccessSecretProps model
        service_access_secret_props_model_json = {}
        service_access_secret_props_model_json['resource_key'] = resource_key_ref_model
        service_access_secret_props_model_json['role'] = role_ref_model
        service_access_secret_props_model_json['service_instance'] = service_instance_ref_model
        service_access_secret_props_model_json['serviceid'] = service_id_ref_model

        # Construct a model instance of ServiceAccessSecretProps by calling from_dict on the json representation
        service_access_secret_props_model = ServiceAccessSecretProps.from_dict(service_access_secret_props_model_json)
        assert service_access_secret_props_model != False

        # Construct a model instance of ServiceAccessSecretProps by calling from_dict on the json representation
        service_access_secret_props_model_dict = ServiceAccessSecretProps.from_dict(
            service_access_secret_props_model_json
        ).__dict__
        service_access_secret_props_model2 = ServiceAccessSecretProps(**service_access_secret_props_model_dict)

        # Verify the model instances are equivalent
        assert service_access_secret_props_model == service_access_secret_props_model2

        # Convert model instance back to dict and verify no loss of data
        service_access_secret_props_model_json2 = service_access_secret_props_model.to_dict()
        assert service_access_secret_props_model_json2 == service_access_secret_props_model_json


class TestModel_ServiceAccessSecretPrototypeProps:
    """
    Test Class for ServiceAccessSecretPrototypeProps
    """

    def test_service_access_secret_prototype_props_serialization(self):
        """
        Test serialization/deserialization for ServiceAccessSecretPrototypeProps
        """

        # Construct dict forms of any model objects needed in order to build this model.

        resource_key_ref_prototype_model = {}  # ResourceKeyRefPrototype
        resource_key_ref_prototype_model['id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'

        role_ref_prototype_model = {}  # RoleRefPrototype
        role_ref_prototype_model['crn'] = 'crn:v1:bluemix:public:iam::::serviceRole:Writer'

        service_instance_ref_prototype_model = {}  # ServiceInstanceRefPrototype
        service_instance_ref_prototype_model['id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'

        service_id_ref_model = {}  # ServiceIDRef
        service_id_ref_model['crn'] = 'testString'
        service_id_ref_model['id'] = 'ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637'

        # Construct a json representation of a ServiceAccessSecretPrototypeProps model
        service_access_secret_prototype_props_model_json = {}
        service_access_secret_prototype_props_model_json['resource_key'] = resource_key_ref_prototype_model
        service_access_secret_prototype_props_model_json['role'] = role_ref_prototype_model
        service_access_secret_prototype_props_model_json['service_instance'] = service_instance_ref_prototype_model
        service_access_secret_prototype_props_model_json['serviceid'] = service_id_ref_model

        # Construct a model instance of ServiceAccessSecretPrototypeProps by calling from_dict on the json representation
        service_access_secret_prototype_props_model = ServiceAccessSecretPrototypeProps.from_dict(
            service_access_secret_prototype_props_model_json
        )
        assert service_access_secret_prototype_props_model != False

        # Construct a model instance of ServiceAccessSecretPrototypeProps by calling from_dict on the json representation
        service_access_secret_prototype_props_model_dict = ServiceAccessSecretPrototypeProps.from_dict(
            service_access_secret_prototype_props_model_json
        ).__dict__
        service_access_secret_prototype_props_model2 = ServiceAccessSecretPrototypeProps(
            **service_access_secret_prototype_props_model_dict
        )

        # Verify the model instances are equivalent
        assert service_access_secret_prototype_props_model == service_access_secret_prototype_props_model2

        # Convert model instance back to dict and verify no loss of data
        service_access_secret_prototype_props_model_json2 = service_access_secret_prototype_props_model.to_dict()
        assert service_access_secret_prototype_props_model_json2 == service_access_secret_prototype_props_model_json


class TestModel_ServiceIDRef:
    """
    Test Class for ServiceIDRef
    """

    def test_service_id_ref_serialization(self):
        """
        Test serialization/deserialization for ServiceIDRef
        """

        # Construct a json representation of a ServiceIDRef model
        service_id_ref_model_json = {}
        service_id_ref_model_json['crn'] = 'testString'
        service_id_ref_model_json['id'] = 'ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637'

        # Construct a model instance of ServiceIDRef by calling from_dict on the json representation
        service_id_ref_model = ServiceIDRef.from_dict(service_id_ref_model_json)
        assert service_id_ref_model != False

        # Construct a model instance of ServiceIDRef by calling from_dict on the json representation
        service_id_ref_model_dict = ServiceIDRef.from_dict(service_id_ref_model_json).__dict__
        service_id_ref_model2 = ServiceIDRef(**service_id_ref_model_dict)

        # Verify the model instances are equivalent
        assert service_id_ref_model == service_id_ref_model2

        # Convert model instance back to dict and verify no loss of data
        service_id_ref_model_json2 = service_id_ref_model.to_dict()
        assert service_id_ref_model_json2 == service_id_ref_model_json


class TestModel_ServiceIDRefPrototype:
    """
    Test Class for ServiceIDRefPrototype
    """

    def test_service_id_ref_prototype_serialization(self):
        """
        Test serialization/deserialization for ServiceIDRefPrototype
        """

        # Construct a json representation of a ServiceIDRefPrototype model
        service_id_ref_prototype_model_json = {}
        service_id_ref_prototype_model_json['id'] = 'ServiceId-8fa4bc74-6441-4e5b-af3a-2b1af325a637'

        # Construct a model instance of ServiceIDRefPrototype by calling from_dict on the json representation
        service_id_ref_prototype_model = ServiceIDRefPrototype.from_dict(service_id_ref_prototype_model_json)
        assert service_id_ref_prototype_model != False

        # Construct a model instance of ServiceIDRefPrototype by calling from_dict on the json representation
        service_id_ref_prototype_model_dict = ServiceIDRefPrototype.from_dict(
            service_id_ref_prototype_model_json
        ).__dict__
        service_id_ref_prototype_model2 = ServiceIDRefPrototype(**service_id_ref_prototype_model_dict)

        # Verify the model instances are equivalent
        assert service_id_ref_prototype_model == service_id_ref_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        service_id_ref_prototype_model_json2 = service_id_ref_prototype_model.to_dict()
        assert service_id_ref_prototype_model_json2 == service_id_ref_prototype_model_json


class TestModel_ServiceInstanceRef:
    """
    Test Class for ServiceInstanceRef
    """

    def test_service_instance_ref_serialization(self):
        """
        Test serialization/deserialization for ServiceInstanceRef
        """

        # Construct a json representation of a ServiceInstanceRef model
        service_instance_ref_model_json = {}
        service_instance_ref_model_json['id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'
        service_instance_ref_model_json['type'] = 'testString'

        # Construct a model instance of ServiceInstanceRef by calling from_dict on the json representation
        service_instance_ref_model = ServiceInstanceRef.from_dict(service_instance_ref_model_json)
        assert service_instance_ref_model != False

        # Construct a model instance of ServiceInstanceRef by calling from_dict on the json representation
        service_instance_ref_model_dict = ServiceInstanceRef.from_dict(service_instance_ref_model_json).__dict__
        service_instance_ref_model2 = ServiceInstanceRef(**service_instance_ref_model_dict)

        # Verify the model instances are equivalent
        assert service_instance_ref_model == service_instance_ref_model2

        # Convert model instance back to dict and verify no loss of data
        service_instance_ref_model_json2 = service_instance_ref_model.to_dict()
        assert service_instance_ref_model_json2 == service_instance_ref_model_json


class TestModel_ServiceInstanceRefPrototype:
    """
    Test Class for ServiceInstanceRefPrototype
    """

    def test_service_instance_ref_prototype_serialization(self):
        """
        Test serialization/deserialization for ServiceInstanceRefPrototype
        """

        # Construct a json representation of a ServiceInstanceRefPrototype model
        service_instance_ref_prototype_model_json = {}
        service_instance_ref_prototype_model_json['id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'

        # Construct a model instance of ServiceInstanceRefPrototype by calling from_dict on the json representation
        service_instance_ref_prototype_model = ServiceInstanceRefPrototype.from_dict(
            service_instance_ref_prototype_model_json
        )
        assert service_instance_ref_prototype_model != False

        # Construct a model instance of ServiceInstanceRefPrototype by calling from_dict on the json representation
        service_instance_ref_prototype_model_dict = ServiceInstanceRefPrototype.from_dict(
            service_instance_ref_prototype_model_json
        ).__dict__
        service_instance_ref_prototype_model2 = ServiceInstanceRefPrototype(**service_instance_ref_prototype_model_dict)

        # Verify the model instances are equivalent
        assert service_instance_ref_prototype_model == service_instance_ref_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        service_instance_ref_prototype_model_json2 = service_instance_ref_prototype_model.to_dict()
        assert service_instance_ref_prototype_model_json2 == service_instance_ref_prototype_model_json


class TestModel_VolumeMount:
    """
    Test Class for VolumeMount
    """

    def test_volume_mount_serialization(self):
        """
        Test serialization/deserialization for VolumeMount
        """

        # Construct a json representation of a VolumeMount model
        volume_mount_model_json = {}
        volume_mount_model_json['mount_path'] = '/app'
        volume_mount_model_json['name'] = 'codeengine-mount-b69u90'
        volume_mount_model_json['reference'] = 'my-secret'
        volume_mount_model_json['type'] = 'secret'

        # Construct a model instance of VolumeMount by calling from_dict on the json representation
        volume_mount_model = VolumeMount.from_dict(volume_mount_model_json)
        assert volume_mount_model != False

        # Construct a model instance of VolumeMount by calling from_dict on the json representation
        volume_mount_model_dict = VolumeMount.from_dict(volume_mount_model_json).__dict__
        volume_mount_model2 = VolumeMount(**volume_mount_model_dict)

        # Verify the model instances are equivalent
        assert volume_mount_model == volume_mount_model2

        # Convert model instance back to dict and verify no loss of data
        volume_mount_model_json2 = volume_mount_model.to_dict()
        assert volume_mount_model_json2 == volume_mount_model_json


class TestModel_VolumeMountPrototype:
    """
    Test Class for VolumeMountPrototype
    """

    def test_volume_mount_prototype_serialization(self):
        """
        Test serialization/deserialization for VolumeMountPrototype
        """

        # Construct a json representation of a VolumeMountPrototype model
        volume_mount_prototype_model_json = {}
        volume_mount_prototype_model_json['mount_path'] = '/app'
        volume_mount_prototype_model_json['name'] = 'codeengine-mount-b69u90'
        volume_mount_prototype_model_json['reference'] = 'my-secret'
        volume_mount_prototype_model_json['type'] = 'secret'

        # Construct a model instance of VolumeMountPrototype by calling from_dict on the json representation
        volume_mount_prototype_model = VolumeMountPrototype.from_dict(volume_mount_prototype_model_json)
        assert volume_mount_prototype_model != False

        # Construct a model instance of VolumeMountPrototype by calling from_dict on the json representation
        volume_mount_prototype_model_dict = VolumeMountPrototype.from_dict(volume_mount_prototype_model_json).__dict__
        volume_mount_prototype_model2 = VolumeMountPrototype(**volume_mount_prototype_model_dict)

        # Verify the model instances are equivalent
        assert volume_mount_prototype_model == volume_mount_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        volume_mount_prototype_model_json2 = volume_mount_prototype_model.to_dict()
        assert volume_mount_prototype_model_json2 == volume_mount_prototype_model_json


class TestModel_AllowedOutboundDestinationPatchCidrBlockDataPatch:
    """
    Test Class for AllowedOutboundDestinationPatchCidrBlockDataPatch
    """

    def test_allowed_outbound_destination_patch_cidr_block_data_patch_serialization(self):
        """
        Test serialization/deserialization for AllowedOutboundDestinationPatchCidrBlockDataPatch
        """

        # Construct a json representation of a AllowedOutboundDestinationPatchCidrBlockDataPatch model
        allowed_outbound_destination_patch_cidr_block_data_patch_model_json = {}
        allowed_outbound_destination_patch_cidr_block_data_patch_model_json['type'] = 'cidr_block'
        allowed_outbound_destination_patch_cidr_block_data_patch_model_json['cidr_block'] = 'testString'

        # Construct a model instance of AllowedOutboundDestinationPatchCidrBlockDataPatch by calling from_dict on the json representation
        allowed_outbound_destination_patch_cidr_block_data_patch_model = (
            AllowedOutboundDestinationPatchCidrBlockDataPatch.from_dict(
                allowed_outbound_destination_patch_cidr_block_data_patch_model_json
            )
        )
        assert allowed_outbound_destination_patch_cidr_block_data_patch_model != False

        # Construct a model instance of AllowedOutboundDestinationPatchCidrBlockDataPatch by calling from_dict on the json representation
        allowed_outbound_destination_patch_cidr_block_data_patch_model_dict = (
            AllowedOutboundDestinationPatchCidrBlockDataPatch.from_dict(
                allowed_outbound_destination_patch_cidr_block_data_patch_model_json
            ).__dict__
        )
        allowed_outbound_destination_patch_cidr_block_data_patch_model2 = (
            AllowedOutboundDestinationPatchCidrBlockDataPatch(
                **allowed_outbound_destination_patch_cidr_block_data_patch_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            allowed_outbound_destination_patch_cidr_block_data_patch_model
            == allowed_outbound_destination_patch_cidr_block_data_patch_model2
        )

        # Convert model instance back to dict and verify no loss of data
        allowed_outbound_destination_patch_cidr_block_data_patch_model_json2 = (
            allowed_outbound_destination_patch_cidr_block_data_patch_model.to_dict()
        )
        assert (
            allowed_outbound_destination_patch_cidr_block_data_patch_model_json2
            == allowed_outbound_destination_patch_cidr_block_data_patch_model_json
        )


class TestModel_AllowedOutboundDestinationPrototypeCidrBlockDataPrototype:
    """
    Test Class for AllowedOutboundDestinationPrototypeCidrBlockDataPrototype
    """

    def test_allowed_outbound_destination_prototype_cidr_block_data_prototype_serialization(self):
        """
        Test serialization/deserialization for AllowedOutboundDestinationPrototypeCidrBlockDataPrototype
        """

        # Construct a json representation of a AllowedOutboundDestinationPrototypeCidrBlockDataPrototype model
        allowed_outbound_destination_prototype_cidr_block_data_prototype_model_json = {}
        allowed_outbound_destination_prototype_cidr_block_data_prototype_model_json['type'] = 'cidr_block'
        allowed_outbound_destination_prototype_cidr_block_data_prototype_model_json['cidr_block'] = 'testString'
        allowed_outbound_destination_prototype_cidr_block_data_prototype_model_json['name'] = 'testString'

        # Construct a model instance of AllowedOutboundDestinationPrototypeCidrBlockDataPrototype by calling from_dict on the json representation
        allowed_outbound_destination_prototype_cidr_block_data_prototype_model = (
            AllowedOutboundDestinationPrototypeCidrBlockDataPrototype.from_dict(
                allowed_outbound_destination_prototype_cidr_block_data_prototype_model_json
            )
        )
        assert allowed_outbound_destination_prototype_cidr_block_data_prototype_model != False

        # Construct a model instance of AllowedOutboundDestinationPrototypeCidrBlockDataPrototype by calling from_dict on the json representation
        allowed_outbound_destination_prototype_cidr_block_data_prototype_model_dict = (
            AllowedOutboundDestinationPrototypeCidrBlockDataPrototype.from_dict(
                allowed_outbound_destination_prototype_cidr_block_data_prototype_model_json
            ).__dict__
        )
        allowed_outbound_destination_prototype_cidr_block_data_prototype_model2 = (
            AllowedOutboundDestinationPrototypeCidrBlockDataPrototype(
                **allowed_outbound_destination_prototype_cidr_block_data_prototype_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            allowed_outbound_destination_prototype_cidr_block_data_prototype_model
            == allowed_outbound_destination_prototype_cidr_block_data_prototype_model2
        )

        # Convert model instance back to dict and verify no loss of data
        allowed_outbound_destination_prototype_cidr_block_data_prototype_model_json2 = (
            allowed_outbound_destination_prototype_cidr_block_data_prototype_model.to_dict()
        )
        assert (
            allowed_outbound_destination_prototype_cidr_block_data_prototype_model_json2
            == allowed_outbound_destination_prototype_cidr_block_data_prototype_model_json
        )


class TestModel_AllowedOutboundDestinationCidrBlockData:
    """
    Test Class for AllowedOutboundDestinationCidrBlockData
    """

    def test_allowed_outbound_destination_cidr_block_data_serialization(self):
        """
        Test serialization/deserialization for AllowedOutboundDestinationCidrBlockData
        """

        # Construct a json representation of a AllowedOutboundDestinationCidrBlockData model
        allowed_outbound_destination_cidr_block_data_model_json = {}
        allowed_outbound_destination_cidr_block_data_model_json['entity_tag'] = '2385407409'
        allowed_outbound_destination_cidr_block_data_model_json['type'] = 'cidr_block'
        allowed_outbound_destination_cidr_block_data_model_json['cidr_block'] = 'testString'
        allowed_outbound_destination_cidr_block_data_model_json['name'] = 'testString'

        # Construct a model instance of AllowedOutboundDestinationCidrBlockData by calling from_dict on the json representation
        allowed_outbound_destination_cidr_block_data_model = AllowedOutboundDestinationCidrBlockData.from_dict(
            allowed_outbound_destination_cidr_block_data_model_json
        )
        assert allowed_outbound_destination_cidr_block_data_model != False

        # Construct a model instance of AllowedOutboundDestinationCidrBlockData by calling from_dict on the json representation
        allowed_outbound_destination_cidr_block_data_model_dict = AllowedOutboundDestinationCidrBlockData.from_dict(
            allowed_outbound_destination_cidr_block_data_model_json
        ).__dict__
        allowed_outbound_destination_cidr_block_data_model2 = AllowedOutboundDestinationCidrBlockData(
            **allowed_outbound_destination_cidr_block_data_model_dict
        )

        # Verify the model instances are equivalent
        assert allowed_outbound_destination_cidr_block_data_model == allowed_outbound_destination_cidr_block_data_model2

        # Convert model instance back to dict and verify no loss of data
        allowed_outbound_destination_cidr_block_data_model_json2 = (
            allowed_outbound_destination_cidr_block_data_model.to_dict()
        )
        assert (
            allowed_outbound_destination_cidr_block_data_model_json2
            == allowed_outbound_destination_cidr_block_data_model_json
        )


class TestModel_SecretDataBasicAuthSecretData:
    """
    Test Class for SecretDataBasicAuthSecretData
    """

    def test_secret_data_basic_auth_secret_data_serialization(self):
        """
        Test serialization/deserialization for SecretDataBasicAuthSecretData
        """

        # Construct a json representation of a SecretDataBasicAuthSecretData model
        secret_data_basic_auth_secret_data_model_json = {}
        secret_data_basic_auth_secret_data_model_json['username'] = 'testString'
        secret_data_basic_auth_secret_data_model_json['password'] = 'testString'
        secret_data_basic_auth_secret_data_model_json['foo'] = 'testString'

        # Construct a model instance of SecretDataBasicAuthSecretData by calling from_dict on the json representation
        secret_data_basic_auth_secret_data_model = SecretDataBasicAuthSecretData.from_dict(
            secret_data_basic_auth_secret_data_model_json
        )
        assert secret_data_basic_auth_secret_data_model != False

        # Construct a model instance of SecretDataBasicAuthSecretData by calling from_dict on the json representation
        secret_data_basic_auth_secret_data_model_dict = SecretDataBasicAuthSecretData.from_dict(
            secret_data_basic_auth_secret_data_model_json
        ).__dict__
        secret_data_basic_auth_secret_data_model2 = SecretDataBasicAuthSecretData(
            **secret_data_basic_auth_secret_data_model_dict
        )

        # Verify the model instances are equivalent
        assert secret_data_basic_auth_secret_data_model == secret_data_basic_auth_secret_data_model2

        # Convert model instance back to dict and verify no loss of data
        secret_data_basic_auth_secret_data_model_json2 = secret_data_basic_auth_secret_data_model.to_dict()
        assert secret_data_basic_auth_secret_data_model_json2 == secret_data_basic_auth_secret_data_model_json

        # Test get_properties and set_properties methods.
        secret_data_basic_auth_secret_data_model.set_properties({})
        actual_dict = secret_data_basic_auth_secret_data_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        secret_data_basic_auth_secret_data_model.set_properties(expected_dict)
        actual_dict = secret_data_basic_auth_secret_data_model.get_properties()
        assert actual_dict.keys() == expected_dict.keys()


class TestModel_SecretDataGenericSecretData:
    """
    Test Class for SecretDataGenericSecretData
    """

    def test_secret_data_generic_secret_data_serialization(self):
        """
        Test serialization/deserialization for SecretDataGenericSecretData
        """

        # Construct a json representation of a SecretDataGenericSecretData model
        secret_data_generic_secret_data_model_json = {}
        secret_data_generic_secret_data_model_json['foo'] = 'testString'

        # Construct a model instance of SecretDataGenericSecretData by calling from_dict on the json representation
        secret_data_generic_secret_data_model = SecretDataGenericSecretData.from_dict(
            secret_data_generic_secret_data_model_json
        )
        assert secret_data_generic_secret_data_model != False

        # Construct a model instance of SecretDataGenericSecretData by calling from_dict on the json representation
        secret_data_generic_secret_data_model_dict = SecretDataGenericSecretData.from_dict(
            secret_data_generic_secret_data_model_json
        ).__dict__
        secret_data_generic_secret_data_model2 = SecretDataGenericSecretData(
            **secret_data_generic_secret_data_model_dict
        )

        # Verify the model instances are equivalent
        assert secret_data_generic_secret_data_model == secret_data_generic_secret_data_model2

        # Convert model instance back to dict and verify no loss of data
        secret_data_generic_secret_data_model_json2 = secret_data_generic_secret_data_model.to_dict()
        assert secret_data_generic_secret_data_model_json2 == secret_data_generic_secret_data_model_json

        # Test get_properties and set_properties methods.
        secret_data_generic_secret_data_model.set_properties({})
        actual_dict = secret_data_generic_secret_data_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        secret_data_generic_secret_data_model.set_properties(expected_dict)
        actual_dict = secret_data_generic_secret_data_model.get_properties()
        assert actual_dict.keys() == expected_dict.keys()


class TestModel_SecretDataRegistrySecretData:
    """
    Test Class for SecretDataRegistrySecretData
    """

    def test_secret_data_registry_secret_data_serialization(self):
        """
        Test serialization/deserialization for SecretDataRegistrySecretData
        """

        # Construct a json representation of a SecretDataRegistrySecretData model
        secret_data_registry_secret_data_model_json = {}
        secret_data_registry_secret_data_model_json['username'] = 'testString'
        secret_data_registry_secret_data_model_json['password'] = 'testString'
        secret_data_registry_secret_data_model_json['server'] = 'testString'
        secret_data_registry_secret_data_model_json['email'] = 'testString'
        secret_data_registry_secret_data_model_json['foo'] = 'testString'

        # Construct a model instance of SecretDataRegistrySecretData by calling from_dict on the json representation
        secret_data_registry_secret_data_model = SecretDataRegistrySecretData.from_dict(
            secret_data_registry_secret_data_model_json
        )
        assert secret_data_registry_secret_data_model != False

        # Construct a model instance of SecretDataRegistrySecretData by calling from_dict on the json representation
        secret_data_registry_secret_data_model_dict = SecretDataRegistrySecretData.from_dict(
            secret_data_registry_secret_data_model_json
        ).__dict__
        secret_data_registry_secret_data_model2 = SecretDataRegistrySecretData(
            **secret_data_registry_secret_data_model_dict
        )

        # Verify the model instances are equivalent
        assert secret_data_registry_secret_data_model == secret_data_registry_secret_data_model2

        # Convert model instance back to dict and verify no loss of data
        secret_data_registry_secret_data_model_json2 = secret_data_registry_secret_data_model.to_dict()
        assert secret_data_registry_secret_data_model_json2 == secret_data_registry_secret_data_model_json

        # Test get_properties and set_properties methods.
        secret_data_registry_secret_data_model.set_properties({})
        actual_dict = secret_data_registry_secret_data_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        secret_data_registry_secret_data_model.set_properties(expected_dict)
        actual_dict = secret_data_registry_secret_data_model.get_properties()
        assert actual_dict.keys() == expected_dict.keys()


class TestModel_SecretDataSSHSecretData:
    """
    Test Class for SecretDataSSHSecretData
    """

    def test_secret_data_ssh_secret_data_serialization(self):
        """
        Test serialization/deserialization for SecretDataSSHSecretData
        """

        # Construct a json representation of a SecretDataSSHSecretData model
        secret_data_ssh_secret_data_model_json = {}
        secret_data_ssh_secret_data_model_json['ssh_key'] = 'testString'
        secret_data_ssh_secret_data_model_json['known_hosts'] = 'testString'
        secret_data_ssh_secret_data_model_json['foo'] = 'testString'

        # Construct a model instance of SecretDataSSHSecretData by calling from_dict on the json representation
        secret_data_ssh_secret_data_model = SecretDataSSHSecretData.from_dict(secret_data_ssh_secret_data_model_json)
        assert secret_data_ssh_secret_data_model != False

        # Construct a model instance of SecretDataSSHSecretData by calling from_dict on the json representation
        secret_data_ssh_secret_data_model_dict = SecretDataSSHSecretData.from_dict(
            secret_data_ssh_secret_data_model_json
        ).__dict__
        secret_data_ssh_secret_data_model2 = SecretDataSSHSecretData(**secret_data_ssh_secret_data_model_dict)

        # Verify the model instances are equivalent
        assert secret_data_ssh_secret_data_model == secret_data_ssh_secret_data_model2

        # Convert model instance back to dict and verify no loss of data
        secret_data_ssh_secret_data_model_json2 = secret_data_ssh_secret_data_model.to_dict()
        assert secret_data_ssh_secret_data_model_json2 == secret_data_ssh_secret_data_model_json

        # Test get_properties and set_properties methods.
        secret_data_ssh_secret_data_model.set_properties({})
        actual_dict = secret_data_ssh_secret_data_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        secret_data_ssh_secret_data_model.set_properties(expected_dict)
        actual_dict = secret_data_ssh_secret_data_model.get_properties()
        assert actual_dict.keys() == expected_dict.keys()


class TestModel_SecretDataTLSSecretData:
    """
    Test Class for SecretDataTLSSecretData
    """

    def test_secret_data_tls_secret_data_serialization(self):
        """
        Test serialization/deserialization for SecretDataTLSSecretData
        """

        # Construct a json representation of a SecretDataTLSSecretData model
        secret_data_tls_secret_data_model_json = {}
        secret_data_tls_secret_data_model_json['tls_cert'] = 'testString'
        secret_data_tls_secret_data_model_json['tls_key'] = 'testString'
        secret_data_tls_secret_data_model_json['foo'] = 'testString'

        # Construct a model instance of SecretDataTLSSecretData by calling from_dict on the json representation
        secret_data_tls_secret_data_model = SecretDataTLSSecretData.from_dict(secret_data_tls_secret_data_model_json)
        assert secret_data_tls_secret_data_model != False

        # Construct a model instance of SecretDataTLSSecretData by calling from_dict on the json representation
        secret_data_tls_secret_data_model_dict = SecretDataTLSSecretData.from_dict(
            secret_data_tls_secret_data_model_json
        ).__dict__
        secret_data_tls_secret_data_model2 = SecretDataTLSSecretData(**secret_data_tls_secret_data_model_dict)

        # Verify the model instances are equivalent
        assert secret_data_tls_secret_data_model == secret_data_tls_secret_data_model2

        # Convert model instance back to dict and verify no loss of data
        secret_data_tls_secret_data_model_json2 = secret_data_tls_secret_data_model.to_dict()
        assert secret_data_tls_secret_data_model_json2 == secret_data_tls_secret_data_model_json

        # Test get_properties and set_properties methods.
        secret_data_tls_secret_data_model.set_properties({})
        actual_dict = secret_data_tls_secret_data_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        secret_data_tls_secret_data_model.set_properties(expected_dict)
        actual_dict = secret_data_tls_secret_data_model.get_properties()
        assert actual_dict.keys() == expected_dict.keys()


# endregion
##############################################################################
# End of Model Tests
##############################################################################

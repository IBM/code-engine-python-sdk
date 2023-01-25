# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2023.
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
    # First, unquote the path since it might have some quoted/escaped characters in it
    # due to how the generator inserts the operation paths into the unit test code.
    operation_path = urllib.parse.unquote(operation_path)

    # Next, quote the path using urllib so that we approximate what will
    # happen during request processing.
    operation_path = urllib.parse.quote(operation_path, safe='/')

    # Finally, form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if re.fullmatch('.*/+', request_url) is None:
        return request_url
    else:
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
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_projects(limit=limit, start=start, headers={})

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
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

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
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

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
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

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
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=202)

        # Set up parameter values
        name = 'my-project'
        resource_group_id = 'b91e849cedb04e7e92bd68c040c672dc'
        tags = ['testString']

        # Invoke method
        response = _service.create_project(name, resource_group_id=resource_group_id, tags=tags, headers={})

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
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=202)

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
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.get_project(id, headers={})

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
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

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
        responses.add(responses.DELETE, url, status=202)

        # Set up parameter values
        id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.delete_project(id, headers={})

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
        responses.add(responses.DELETE, url, status=202)

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
        mock_response = '{"apps": [{"created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_apps(project_id, limit=limit, start=start, headers={})

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
        mock_response = '{"apps": [{"created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.list_apps(project_id, headers={})

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
        mock_response = '{"apps": [{"created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

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
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"apps":[{"created_at":"2022-09-13T11:41:35+02:00","endpoint":"https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud","endpoint_internal":"http://my-app.vg67hzldruk.svc.cluster.local","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_port":8080,"image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","managed_domain_mappings":"local_public","name":"my-app","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"app_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_concurrency":100,"scale_concurrency_target":80,"scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_initial_instances":1,"scale_max_instances":10,"scale_memory_limit":"4G","scale_min_instances":1,"scale_request_timeout":300,"status":"ready","status_details":{"latest_created_revision":"my-app-00001","latest_ready_revision":"my-app-00001","reason":"ready"}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"apps":[{"created_at":"2022-09-13T11:41:35+02:00","endpoint":"https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud","endpoint_internal":"http://my-app.vg67hzldruk.svc.cluster.local","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_port":8080,"image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","managed_domain_mappings":"local_public","name":"my-app","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"app_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_concurrency":100,"scale_concurrency_target":80,"scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_initial_instances":1,"scale_max_instances":10,"scale_memory_limit":"4G","scale_min_instances":1,"scale_request_timeout":300,"status":"ready","status_details":{"latest_created_revision":"my-app-00001","latest_ready_revision":"my-app-00001","reason":"ready"}}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

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
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"apps":[{"created_at":"2022-09-13T11:41:35+02:00","endpoint":"https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud","endpoint_internal":"http://my-app.vg67hzldruk.svc.cluster.local","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_port":8080,"image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","managed_domain_mappings":"local_public","name":"my-app","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"app_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_concurrency":100,"scale_concurrency_target":80,"scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_initial_instances":1,"scale_max_instances":10,"scale_memory_limit":"4G","scale_min_instances":1,"scale_request_timeout":300,"status":"ready","status_details":{"latest_created_revision":"my-app-00001","latest_ready_revision":"my-app-00001","reason":"ready"}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"apps":[{"created_at":"2022-09-13T11:41:35+02:00","endpoint":"https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud","endpoint_internal":"http://my-app.vg67hzldruk.svc.cluster.local","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_port":8080,"image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","managed_domain_mappings":"local_public","name":"my-app","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"app_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_concurrency":100,"scale_concurrency_target":80,"scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_initial_instances":1,"scale_max_instances":10,"scale_memory_limit":"4G","scale_min_instances":1,"scale_request_timeout":300,"status":"ready","status_details":{"latest_created_revision":"my-app-00001","latest_ready_revision":"my-app-00001","reason":"ready"}}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

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
        run_arguments = ['testString']
        run_as_user = 1001
        run_commands = ['testString']
        run_env_variables = [env_var_prototype_model]
        run_service_account = 'default'
        run_volume_mounts = [volume_mount_prototype_model]
        scale_concurrency = 100
        scale_concurrency_target = 80
        scale_cpu_limit = '1'
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
            run_arguments=run_arguments,
            run_as_user=run_as_user,
            run_commands=run_commands,
            run_env_variables=run_env_variables,
            run_service_account=run_service_account,
            run_volume_mounts=run_volume_mounts,
            scale_concurrency=scale_concurrency,
            scale_concurrency_target=scale_concurrency_target,
            scale_cpu_limit=scale_cpu_limit,
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
        assert req_body['run_arguments'] == ['testString']
        assert req_body['run_as_user'] == 1001
        assert req_body['run_commands'] == ['testString']
        assert req_body['run_env_variables'] == [env_var_prototype_model]
        assert req_body['run_service_account'] == 'default'
        assert req_body['run_volume_mounts'] == [volume_mount_prototype_model]
        assert req_body['scale_concurrency'] == 100
        assert req_body['scale_concurrency_target'] == 80
        assert req_body['scale_cpu_limit'] == '1'
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
    def test_create_app_value_error(self):
        """
        test_create_app_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

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
        run_arguments = ['testString']
        run_as_user = 1001
        run_commands = ['testString']
        run_env_variables = [env_var_prototype_model]
        run_service_account = 'default'
        run_volume_mounts = [volume_mount_prototype_model]
        scale_concurrency = 100
        scale_concurrency_target = 80
        scale_cpu_limit = '1'
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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-app'

        # Invoke method
        response = _service.get_app(project_id, name, headers={})

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
    def test_get_app_value_error(self):
        """
        test_get_app_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

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
        responses.add(responses.DELETE, url, status=202)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-app'

        # Invoke method
        response = _service.delete_app(project_id, name, headers={})

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
    def test_delete_app_value_error(self):
        """
        test_delete_app_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app')
        responses.add(responses.DELETE, url, status=202)

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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

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
        app_patch_model['run_arguments'] = ['testString']
        app_patch_model['run_as_user'] = 1001
        app_patch_model['run_commands'] = ['testString']
        app_patch_model['run_env_variables'] = [env_var_prototype_model]
        app_patch_model['run_service_account'] = 'default'
        app_patch_model['run_volume_mounts'] = [volume_mount_prototype_model]
        app_patch_model['scale_concurrency'] = 100
        app_patch_model['scale_concurrency_target'] = 80
        app_patch_model['scale_cpu_limit'] = '1'
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
        response = _service.update_app(project_id, name, if_match, app, headers={})

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
    def test_update_app_value_error(self):
        """
        test_update_app_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "endpoint": "https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud", "endpoint_internal": "http://my-app.vg67hzldruk.svc.cluster.local", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "managed_domain_mappings": "local_public", "name": "my-app", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "app_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"latest_created_revision": "my-app-00001", "latest_ready_revision": "my-app-00001", "reason": "ready"}}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

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
        app_patch_model['run_arguments'] = ['testString']
        app_patch_model['run_as_user'] = 1001
        app_patch_model['run_commands'] = ['testString']
        app_patch_model['run_env_variables'] = [env_var_prototype_model]
        app_patch_model['run_service_account'] = 'default'
        app_patch_model['run_volume_mounts'] = [volume_mount_prototype_model]
        app_patch_model['scale_concurrency'] = 100
        app_patch_model['scale_concurrency_target'] = 80
        app_patch_model['scale_cpu_limit'] = '1'
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
        mock_response = '{"first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}, "revisions": [{"app_name": "my-app", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/revisions/my-app-00001", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-app-00001", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "app_revision_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"actual_instances": 1, "reason": "ready"}}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        app_name = 'my-app'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_app_revisions(project_id, app_name, limit=limit, start=start, headers={})

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
        mock_response = '{"first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}, "revisions": [{"app_name": "my-app", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/revisions/my-app-00001", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-app-00001", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "app_revision_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"actual_instances": 1, "reason": "ready"}}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        app_name = 'my-app'

        # Invoke method
        response = _service.list_app_revisions(project_id, app_name, headers={})

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
        mock_response = '{"first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}, "revisions": [{"app_name": "my-app", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/revisions/my-app-00001", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-app-00001", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "app_revision_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"actual_instances": 1, "reason": "ready"}}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

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
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"revisions":[{"app_name":"my-app","created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/revisions/my-app-00001","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_port":8080,"image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","name":"my-app-00001","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"app_revision_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_concurrency":100,"scale_concurrency_target":80,"scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_initial_instances":1,"scale_max_instances":10,"scale_memory_limit":"4G","scale_min_instances":1,"scale_request_timeout":300,"status":"ready","status_details":{"actual_instances":1,"reason":"ready"}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"revisions":[{"app_name":"my-app","created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/revisions/my-app-00001","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_port":8080,"image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","name":"my-app-00001","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"app_revision_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_concurrency":100,"scale_concurrency_target":80,"scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_initial_instances":1,"scale_max_instances":10,"scale_memory_limit":"4G","scale_min_instances":1,"scale_request_timeout":300,"status":"ready","status_details":{"actual_instances":1,"reason":"ready"}}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

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
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"revisions":[{"app_name":"my-app","created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/revisions/my-app-00001","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_port":8080,"image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","name":"my-app-00001","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"app_revision_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_concurrency":100,"scale_concurrency_target":80,"scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_initial_instances":1,"scale_max_instances":10,"scale_memory_limit":"4G","scale_min_instances":1,"scale_request_timeout":300,"status":"ready","status_details":{"actual_instances":1,"reason":"ready"}}]}'
        mock_response2 = '{"total_count":2,"limit":1,"revisions":[{"app_name":"my-app","created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/revisions/my-app-00001","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_port":8080,"image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","name":"my-app-00001","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"app_revision_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_concurrency":100,"scale_concurrency_target":80,"scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_initial_instances":1,"scale_max_instances":10,"scale_memory_limit":"4G","scale_min_instances":1,"scale_request_timeout":300,"status":"ready","status_details":{"actual_instances":1,"reason":"ready"}}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

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
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app/revisions/my-app-001')
        mock_response = '{"app_name": "my-app", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/revisions/my-app-00001", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-app-00001", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "app_revision_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"actual_instances": 1, "reason": "ready"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        app_name = 'my-app'
        name = 'my-app-001'

        # Invoke method
        response = _service.get_app_revision(project_id, app_name, name, headers={})

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
    def test_get_app_revision_value_error(self):
        """
        test_get_app_revision_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app/revisions/my-app-001')
        mock_response = '{"app_name": "my-app", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/revisions/my-app-00001", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_port": 8080, "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-app-00001", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "app_revision_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_concurrency": 100, "scale_concurrency_target": 80, "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_initial_instances": 1, "scale_max_instances": 10, "scale_memory_limit": "4G", "scale_min_instances": 1, "scale_request_timeout": 300, "status": "ready", "status_details": {"actual_instances": 1, "reason": "ready"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        app_name = 'my-app'
        name = 'my-app-001'

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
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app/revisions/my-app-001')
        responses.add(responses.DELETE, url, status=202)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        app_name = 'my-app'
        name = 'my-app-001'

        # Invoke method
        response = _service.delete_app_revision(project_id, app_name, name, headers={})

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
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/apps/my-app/revisions/my-app-001')
        responses.add(responses.DELETE, url, status=202)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        app_name = 'my-app'
        name = 'my-app-001'

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
        mock_response = '{"first": {"href": "href"}, "jobs": [{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "daemon", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}], "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_jobs(project_id, limit=limit, start=start, headers={})

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
        mock_response = '{"first": {"href": "href"}, "jobs": [{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "daemon", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}], "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.list_jobs(project_id, headers={})

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
        mock_response = '{"first": {"href": "href"}, "jobs": [{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "daemon", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}], "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

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
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"jobs":[{"created_at":"2022-09-13T11:41:35+02:00","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","name":"my-job","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"job_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_mode":"daemon","run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_array_spec":"1-5,7-8,10","scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_max_execution_time":7200,"scale_memory_limit":"4G","scale_retry_limit":3}],"limit":1}'
        mock_response2 = '{"total_count":2,"jobs":[{"created_at":"2022-09-13T11:41:35+02:00","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","name":"my-job","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"job_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_mode":"daemon","run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_array_spec":"1-5,7-8,10","scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_max_execution_time":7200,"scale_memory_limit":"4G","scale_retry_limit":3}],"limit":1}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

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
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"jobs":[{"created_at":"2022-09-13T11:41:35+02:00","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","name":"my-job","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"job_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_mode":"daemon","run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_array_spec":"1-5,7-8,10","scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_max_execution_time":7200,"scale_memory_limit":"4G","scale_retry_limit":3}],"limit":1}'
        mock_response2 = '{"total_count":2,"jobs":[{"created_at":"2022-09-13T11:41:35+02:00","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","name":"my-job","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"job_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_mode":"daemon","run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_array_spec":"1-5,7-8,10","scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_max_execution_time":7200,"scale_memory_limit":"4G","scale_retry_limit":3}],"limit":1}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "daemon", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

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
        run_mode = 'daemon'
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
        assert req_body['run_mode'] == 'daemon'
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
    def test_create_job_value_error(self):
        """
        test_create_job_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "daemon", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

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
        run_mode = 'daemon'
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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "daemon", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-job'

        # Invoke method
        response = _service.get_job(project_id, name, headers={})

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
    def test_get_job_value_error(self):
        """
        test_get_job_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs/my-job')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "daemon", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

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
        responses.add(responses.DELETE, url, status=202)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-job'

        # Invoke method
        response = _service.delete_job(project_id, name, headers={})

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
    def test_delete_job_value_error(self):
        """
        test_delete_job_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs/my-job')
        responses.add(responses.DELETE, url, status=202)

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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "daemon", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

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
        job_patch_model['run_mode'] = 'daemon'
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
        response = _service.update_job(project_id, name, if_match, job, headers={})

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
    def test_update_job_value_error(self):
        """
        test_update_job_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/jobs/my-job')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "name": "my-job", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "job_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "daemon", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

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
        job_patch_model['run_mode'] = 'daemon'
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
        mock_response = '{"first": {"href": "href"}, "job_runs": [{"created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "job_name": "my-job", "name": "my-job-run", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "job_run_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "daemon", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3, "status": "completed", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "failed": 0, "pending": 0, "requested": 0, "running": 0, "start_time": "2022-09-22T17:34:00Z", "succeeded": 1, "unknown": 0}}], "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        job_name = 'my-job'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_job_runs(project_id, job_name=job_name, limit=limit, start=start, headers={})

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
        mock_response = '{"first": {"href": "href"}, "job_runs": [{"created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "job_name": "my-job", "name": "my-job-run", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "job_run_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "daemon", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3, "status": "completed", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "failed": 0, "pending": 0, "requested": 0, "running": 0, "start_time": "2022-09-22T17:34:00Z", "succeeded": 1, "unknown": 0}}], "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.list_job_runs(project_id, headers={})

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
        mock_response = '{"first": {"href": "href"}, "job_runs": [{"created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "job_name": "my-job", "name": "my-job-run", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "job_run_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "daemon", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3, "status": "completed", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "failed": 0, "pending": 0, "requested": 0, "running": 0, "start_time": "2022-09-22T17:34:00Z", "succeeded": 1, "unknown": 0}}], "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

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
        mock_response1 = '{"next":{"start":"1"},"job_runs":[{"created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","job_name":"my-job","name":"my-job-run","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"job_run_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_mode":"daemon","run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_array_spec":"1-5,7-8,10","scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_max_execution_time":7200,"scale_memory_limit":"4G","scale_retry_limit":3,"status":"completed","status_details":{"completion_time":"2022-09-22T17:40:00Z","failed":0,"pending":0,"requested":0,"running":0,"start_time":"2022-09-22T17:34:00Z","succeeded":1,"unknown":0}}],"total_count":2,"limit":1}'
        mock_response2 = '{"job_runs":[{"created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","job_name":"my-job","name":"my-job-run","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"job_run_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_mode":"daemon","run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_array_spec":"1-5,7-8,10","scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_max_execution_time":7200,"scale_memory_limit":"4G","scale_retry_limit":3,"status":"completed","status_details":{"completion_time":"2022-09-22T17:40:00Z","failed":0,"pending":0,"requested":0,"running":0,"start_time":"2022-09-22T17:34:00Z","succeeded":1,"unknown":0}}],"total_count":2,"limit":1}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

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
        mock_response1 = '{"next":{"start":"1"},"job_runs":[{"created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","job_name":"my-job","name":"my-job-run","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"job_run_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_mode":"daemon","run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_array_spec":"1-5,7-8,10","scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_max_execution_time":7200,"scale_memory_limit":"4G","scale_retry_limit":3,"status":"completed","status_details":{"completion_time":"2022-09-22T17:40:00Z","failed":0,"pending":0,"requested":0,"running":0,"start_time":"2022-09-22T17:34:00Z","succeeded":1,"unknown":0}}],"total_count":2,"limit":1}'
        mock_response2 = '{"job_runs":[{"created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","image_reference":"icr.io/codeengine/helloworld","image_secret":"my-secret","job_name":"my-job","name":"my-job-run","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"job_run_v2","run_arguments":["run_arguments"],"run_as_user":1001,"run_commands":["run_commands"],"run_env_variables":[{"key":"MY_VARIABLE","name":"SOME","prefix":"PREFIX_","reference":"my-secret","type":"literal","value":"VALUE"}],"run_mode":"daemon","run_service_account":"default","run_volume_mounts":[{"mount_path":"/app","name":"codeengine-mount-b69u90","reference":"my-secret","type":"secret"}],"scale_array_spec":"1-5,7-8,10","scale_cpu_limit":"1","scale_ephemeral_storage_limit":"4G","scale_max_execution_time":7200,"scale_memory_limit":"4G","scale_retry_limit":3,"status":"completed","status_details":{"completion_time":"2022-09-22T17:40:00Z","failed":0,"pending":0,"requested":0,"running":0,"start_time":"2022-09-22T17:34:00Z","succeeded":1,"unknown":0}}],"total_count":2,"limit":1}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "job_name": "my-job", "name": "my-job-run", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "job_run_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "daemon", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3, "status": "completed", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "failed": 0, "pending": 0, "requested": 0, "running": 0, "start_time": "2022-09-22T17:34:00Z", "succeeded": 1, "unknown": 0}}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=202)

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
        run_mode = 'daemon'
        run_service_account = 'default'
        run_volume_mounts = [volume_mount_prototype_model]
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
        assert req_body['run_mode'] == 'daemon'
        assert req_body['run_service_account'] == 'default'
        assert req_body['run_volume_mounts'] == [volume_mount_prototype_model]
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
    def test_create_job_run_value_error(self):
        """
        test_create_job_run_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/job_runs')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "job_name": "my-job", "name": "my-job-run", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "job_run_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "daemon", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3, "status": "completed", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "failed": 0, "pending": 0, "requested": 0, "running": 0, "start_time": "2022-09-22T17:34:00Z", "succeeded": 1, "unknown": 0}}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=202)

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
        run_mode = 'daemon'
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
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/job_runs/my-job')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "job_name": "my-job", "name": "my-job-run", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "job_run_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "daemon", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3, "status": "completed", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "failed": 0, "pending": 0, "requested": 0, "running": 0, "start_time": "2022-09-22T17:34:00Z", "succeeded": 1, "unknown": 0}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-job'

        # Invoke method
        response = _service.get_job_run(project_id, name, headers={})

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
    def test_get_job_run_value_error(self):
        """
        test_get_job_run_value_error()
        """
        # Set up mock
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/job_runs/my-job')
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "image_reference": "icr.io/codeengine/helloworld", "image_secret": "my-secret", "job_name": "my-job", "name": "my-job-run", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "job_run_v2", "run_arguments": ["run_arguments"], "run_as_user": 1001, "run_commands": ["run_commands"], "run_env_variables": [{"key": "MY_VARIABLE", "name": "SOME", "prefix": "PREFIX_", "reference": "my-secret", "type": "literal", "value": "VALUE"}], "run_mode": "daemon", "run_service_account": "default", "run_volume_mounts": [{"mount_path": "/app", "name": "codeengine-mount-b69u90", "reference": "my-secret", "type": "secret"}], "scale_array_spec": "1-5,7-8,10", "scale_cpu_limit": "1", "scale_ephemeral_storage_limit": "4G", "scale_max_execution_time": 7200, "scale_memory_limit": "4G", "scale_retry_limit": 3, "status": "completed", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "failed": 0, "pending": 0, "requested": 0, "running": 0, "start_time": "2022-09-22T17:34:00Z", "succeeded": 1, "unknown": 0}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

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
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/job_runs/my-job')
        responses.add(responses.DELETE, url, status=202)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-job'

        # Invoke method
        response = _service.delete_job_run(project_id, name, headers={})

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
        url = preprocess_url('/projects/15314cc3-85b4-4338-903f-c28cdee6d005/job_runs/my-job')
        responses.add(responses.DELETE, url, status=202)

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
# Start of Service: Builds
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
        mock_response = '{"builds": [{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "build_v2", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "ready", "status_details": {"reason": "registered"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_builds(project_id, limit=limit, start=start, headers={})

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
        mock_response = '{"builds": [{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "build_v2", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "ready", "status_details": {"reason": "registered"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.list_builds(project_id, headers={})

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
        mock_response = '{"builds": [{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "build_v2", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "ready", "status_details": {"reason": "registered"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

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
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"builds":[{"created_at":"2022-09-13T11:41:35+02:00","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-build","output_image":"private.de.icr.io/icr_namespace/image-name","output_secret":"ce-auto-icr-private-eu-de","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"build_v2","source_context_dir":"some/subfolder","source_revision":"main","source_secret":"source_secret","source_type":"git","source_url":"https://github.com/IBM/CodeEngine","status":"ready","status_details":{"reason":"registered"},"strategy_size":"medium","strategy_spec_file":"Dockerfile","strategy_type":"dockerfile","timeout":600}]}'
        mock_response2 = '{"total_count":2,"limit":1,"builds":[{"created_at":"2022-09-13T11:41:35+02:00","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-build","output_image":"private.de.icr.io/icr_namespace/image-name","output_secret":"ce-auto-icr-private-eu-de","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"build_v2","source_context_dir":"some/subfolder","source_revision":"main","source_secret":"source_secret","source_type":"git","source_url":"https://github.com/IBM/CodeEngine","status":"ready","status_details":{"reason":"registered"},"strategy_size":"medium","strategy_spec_file":"Dockerfile","strategy_type":"dockerfile","timeout":600}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

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
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"builds":[{"created_at":"2022-09-13T11:41:35+02:00","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-build","output_image":"private.de.icr.io/icr_namespace/image-name","output_secret":"ce-auto-icr-private-eu-de","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"build_v2","source_context_dir":"some/subfolder","source_revision":"main","source_secret":"source_secret","source_type":"git","source_url":"https://github.com/IBM/CodeEngine","status":"ready","status_details":{"reason":"registered"},"strategy_size":"medium","strategy_spec_file":"Dockerfile","strategy_type":"dockerfile","timeout":600}]}'
        mock_response2 = '{"total_count":2,"limit":1,"builds":[{"created_at":"2022-09-13T11:41:35+02:00","entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-build","output_image":"private.de.icr.io/icr_namespace/image-name","output_secret":"ce-auto-icr-private-eu-de","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"build_v2","source_context_dir":"some/subfolder","source_revision":"main","source_secret":"source_secret","source_type":"git","source_url":"https://github.com/IBM/CodeEngine","status":"ready","status_details":{"reason":"registered"},"strategy_size":"medium","strategy_spec_file":"Dockerfile","strategy_type":"dockerfile","timeout":600}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "build_v2", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "ready", "status_details": {"reason": "registered"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-build'
        output_image = 'private.de.icr.io/icr_namespace/image-name'
        output_secret = 'ce-auto-icr-private-eu-de'
        source_url = 'https://github.com/IBM/CodeEngine'
        strategy_type = 'dockerfile'
        source_context_dir = 'some/subfolder'
        source_revision = 'main'
        source_secret = 'testString'
        source_type = 'git'
        strategy_size = 'medium'
        strategy_spec_file = 'Dockerfile'
        timeout = 600

        # Invoke method
        response = _service.create_build(
            project_id,
            name,
            output_image,
            output_secret,
            source_url,
            strategy_type,
            source_context_dir=source_context_dir,
            source_revision=source_revision,
            source_secret=source_secret,
            source_type=source_type,
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
        assert req_body['source_url'] == 'https://github.com/IBM/CodeEngine'
        assert req_body['strategy_type'] == 'dockerfile'
        assert req_body['source_context_dir'] == 'some/subfolder'
        assert req_body['source_revision'] == 'main'
        assert req_body['source_secret'] == 'testString'
        assert req_body['source_type'] == 'git'
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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "build_v2", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "ready", "status_details": {"reason": "registered"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-build'
        output_image = 'private.de.icr.io/icr_namespace/image-name'
        output_secret = 'ce-auto-icr-private-eu-de'
        source_url = 'https://github.com/IBM/CodeEngine'
        strategy_type = 'dockerfile'
        source_context_dir = 'some/subfolder'
        source_revision = 'main'
        source_secret = 'testString'
        source_type = 'git'
        strategy_size = 'medium'
        strategy_spec_file = 'Dockerfile'
        timeout = 600

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
            "output_image": output_image,
            "output_secret": output_secret,
            "source_url": source_url,
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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "build_v2", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "ready", "status_details": {"reason": "registered"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-build'

        # Invoke method
        response = _service.get_build(project_id, name, headers={})

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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "build_v2", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "ready", "status_details": {"reason": "registered"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

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
        responses.add(responses.DELETE, url, status=202)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-build'

        # Invoke method
        response = _service.delete_build(project_id, name, headers={})

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
        responses.add(responses.DELETE, url, status=202)

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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "build_v2", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "ready", "status_details": {"reason": "registered"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

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
        response = _service.update_build(project_id, name, if_match, build, headers={})

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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "build_v2", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "ready", "status_details": {"reason": "registered"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}'
        responses.add(responses.PATCH, url, body=mock_response, content_type='application/json', status=200)

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
        mock_response = '{"build_runs": [{"build_name": "build_name", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build-run", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "build_run_v2", "service_account": "default", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "succeeded", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "output_digest": "sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384", "reason": "succeeded", "start_time": "2022-09-22T17:34:00Z"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        build_name = 'my-build'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_build_runs(project_id, build_name=build_name, limit=limit, start=start, headers={})

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
        mock_response = '{"build_runs": [{"build_name": "build_name", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build-run", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "build_run_v2", "service_account": "default", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "succeeded", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "output_digest": "sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384", "reason": "succeeded", "start_time": "2022-09-22T17:34:00Z"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.list_build_runs(project_id, headers={})

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
        mock_response = '{"build_runs": [{"build_name": "build_name", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build-run", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "build_run_v2", "service_account": "default", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "succeeded", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "output_digest": "sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384", "reason": "succeeded", "start_time": "2022-09-22T17:34:00Z"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

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
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"build_runs":[{"build_name":"build_name","created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-build-run","output_image":"private.de.icr.io/icr_namespace/image-name","output_secret":"ce-auto-icr-private-eu-de","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"build_run_v2","service_account":"default","source_context_dir":"some/subfolder","source_revision":"main","source_secret":"source_secret","source_type":"git","source_url":"https://github.com/IBM/CodeEngine","status":"succeeded","status_details":{"completion_time":"2022-09-22T17:40:00Z","output_digest":"sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384","reason":"succeeded","start_time":"2022-09-22T17:34:00Z"},"strategy_size":"medium","strategy_spec_file":"Dockerfile","strategy_type":"dockerfile","timeout":600}]}'
        mock_response2 = '{"total_count":2,"limit":1,"build_runs":[{"build_name":"build_name","created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-build-run","output_image":"private.de.icr.io/icr_namespace/image-name","output_secret":"ce-auto-icr-private-eu-de","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"build_run_v2","service_account":"default","source_context_dir":"some/subfolder","source_revision":"main","source_secret":"source_secret","source_type":"git","source_url":"https://github.com/IBM/CodeEngine","status":"succeeded","status_details":{"completion_time":"2022-09-22T17:40:00Z","output_digest":"sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384","reason":"succeeded","start_time":"2022-09-22T17:34:00Z"},"strategy_size":"medium","strategy_spec_file":"Dockerfile","strategy_type":"dockerfile","timeout":600}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

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
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"build_runs":[{"build_name":"build_name","created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-build-run","output_image":"private.de.icr.io/icr_namespace/image-name","output_secret":"ce-auto-icr-private-eu-de","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"build_run_v2","service_account":"default","source_context_dir":"some/subfolder","source_revision":"main","source_secret":"source_secret","source_type":"git","source_url":"https://github.com/IBM/CodeEngine","status":"succeeded","status_details":{"completion_time":"2022-09-22T17:40:00Z","output_digest":"sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384","reason":"succeeded","start_time":"2022-09-22T17:34:00Z"},"strategy_size":"medium","strategy_spec_file":"Dockerfile","strategy_type":"dockerfile","timeout":600}]}'
        mock_response2 = '{"total_count":2,"limit":1,"build_runs":[{"build_name":"build_name","created_at":"2022-09-13T11:41:35+02:00","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-build-run","output_image":"private.de.icr.io/icr_namespace/image-name","output_secret":"ce-auto-icr-private-eu-de","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"build_run_v2","service_account":"default","source_context_dir":"some/subfolder","source_revision":"main","source_secret":"source_secret","source_type":"git","source_url":"https://github.com/IBM/CodeEngine","status":"succeeded","status_details":{"completion_time":"2022-09-22T17:40:00Z","output_digest":"sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384","reason":"succeeded","start_time":"2022-09-22T17:34:00Z"},"strategy_size":"medium","strategy_spec_file":"Dockerfile","strategy_type":"dockerfile","timeout":600}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

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
        mock_response = '{"build_name": "build_name", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build-run", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "build_run_v2", "service_account": "default", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "succeeded", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "output_digest": "sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384", "reason": "succeeded", "start_time": "2022-09-22T17:34:00Z"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=202)

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
        mock_response = '{"build_name": "build_name", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build-run", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "build_run_v2", "service_account": "default", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "succeeded", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "output_digest": "sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384", "reason": "succeeded", "start_time": "2022-09-22T17:34:00Z"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=202)

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
        mock_response = '{"build_name": "build_name", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build-run", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "build_run_v2", "service_account": "default", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "succeeded", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "output_digest": "sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384", "reason": "succeeded", "start_time": "2022-09-22T17:34:00Z"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-build-run'

        # Invoke method
        response = _service.get_build_run(project_id, name, headers={})

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
        mock_response = '{"build_name": "build_name", "created_at": "2022-09-13T11:41:35+02:00", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-build-run", "output_image": "private.de.icr.io/icr_namespace/image-name", "output_secret": "ce-auto-icr-private-eu-de", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "build_run_v2", "service_account": "default", "source_context_dir": "some/subfolder", "source_revision": "main", "source_secret": "source_secret", "source_type": "git", "source_url": "https://github.com/IBM/CodeEngine", "status": "succeeded", "status_details": {"completion_time": "2022-09-22T17:40:00Z", "output_digest": "sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384", "reason": "succeeded", "start_time": "2022-09-22T17:34:00Z"}, "strategy_size": "medium", "strategy_spec_file": "Dockerfile", "strategy_type": "dockerfile", "timeout": 600}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

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
        responses.add(responses.DELETE, url, status=202)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-build-run'

        # Invoke method
        response = _service.delete_build_run(project_id, name, headers={})

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
        responses.add(responses.DELETE, url, status=202)

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
# End of Service: Builds
##############################################################################

##############################################################################
# Start of Service: SecretsAndConfigMaps
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
        mock_response = '{"config_maps": [{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-config-map", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "config_map_v2"}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_config_maps(project_id, limit=limit, start=start, headers={})

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
        mock_response = '{"config_maps": [{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-config-map", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "config_map_v2"}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.list_config_maps(project_id, headers={})

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
        mock_response = '{"config_maps": [{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-config-map", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "config_map_v2"}], "first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

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
        mock_response1 = '{"next":{"start":"1"},"config_maps":[{"created_at":"2022-09-13T11:41:35+02:00","data":{"mapKey":"inner"},"entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-config-map","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"config_map_v2"}],"total_count":2,"limit":1}'
        mock_response2 = '{"config_maps":[{"created_at":"2022-09-13T11:41:35+02:00","data":{"mapKey":"inner"},"entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-config-map","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"config_map_v2"}],"total_count":2,"limit":1}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

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
        mock_response1 = '{"next":{"start":"1"},"config_maps":[{"created_at":"2022-09-13T11:41:35+02:00","data":{"mapKey":"inner"},"entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-config-map","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"config_map_v2"}],"total_count":2,"limit":1}'
        mock_response2 = '{"config_maps":[{"created_at":"2022-09-13T11:41:35+02:00","data":{"mapKey":"inner"},"entity_tag":"2385407409","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-config-map","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"config_map_v2"}],"total_count":2,"limit":1}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-config-map", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "config_map_v2"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-configmap'
        data = {'key1': 'testString'}

        # Invoke method
        response = _service.create_config_map(project_id, name, data=data, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'my-configmap'
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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-config-map", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "config_map_v2"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-configmap'
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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-config-map", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "config_map_v2"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-config-map'

        # Invoke method
        response = _service.get_config_map(project_id, name, headers={})

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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-config-map", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "config_map_v2"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-config-map", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "config_map_v2"}'
        responses.add(responses.PUT, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-config-map'
        if_match = 'testString'
        data = {'key1': 'testString'}

        # Invoke method
        response = _service.replace_config_map(project_id, name, if_match, data=data, headers={})

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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-config-map", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "config_map_v2"}'
        responses.add(responses.PUT, url, body=mock_response, content_type='application/json', status=200)

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
        responses.add(responses.DELETE, url, status=202)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-config-map'

        # Invoke method
        response = _service.delete_config_map(project_id, name, headers={})

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
        responses.add(responses.DELETE, url, status=202)

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
        mock_response = '{"first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}, "secrets": [{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "format": "generic", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-secret", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "resource_type"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        limit = 100
        start = 'testString'

        # Invoke method
        response = _service.list_secrets(project_id, limit=limit, start=start, headers={})

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
        mock_response = '{"first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}, "secrets": [{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "format": "generic", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-secret", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "resource_type"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'

        # Invoke method
        response = _service.list_secrets(project_id, headers={})

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
        mock_response = '{"first": {"href": "href"}, "limit": 100, "next": {"href": "href", "start": "start"}, "secrets": [{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "format": "generic", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-secret", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "resource_type"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

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
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"secrets":[{"created_at":"2022-09-13T11:41:35+02:00","data":{"mapKey":"inner"},"entity_tag":"2385407409","format":"generic","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-secret","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"resource_type"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"secrets":[{"created_at":"2022-09-13T11:41:35+02:00","data":{"mapKey":"inner"},"entity_tag":"2385407409","format":"generic","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-secret","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"resource_type"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

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
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"secrets":[{"created_at":"2022-09-13T11:41:35+02:00","data":{"mapKey":"inner"},"entity_tag":"2385407409","format":"generic","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-secret","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"resource_type"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"secrets":[{"created_at":"2022-09-13T11:41:35+02:00","data":{"mapKey":"inner"},"entity_tag":"2385407409","format":"generic","href":"https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret","id":"e33b1cv7-7390-4437-a5c2-130d5ccdddc3","name":"my-secret","project_id":"4e49b3e0-27a8-48d2-a784-c7ee48bb863b","resource_type":"resource_type"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "format": "generic", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-secret", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "resource_type"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        format = 'generic'
        name = 'my-secret'
        data = {'key1': 'testString'}

        # Invoke method
        response = _service.create_secret(project_id, format, name, data=data, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['format'] == 'generic'
        assert req_body['name'] == 'my-secret'
        assert req_body['data'] == {'key1': 'testString'}

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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "format": "generic", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-secret", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "resource_type"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        format = 'generic'
        name = 'my-secret'
        data = {'key1': 'testString'}

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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "format": "generic", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-secret", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "resource_type"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-secret'

        # Invoke method
        response = _service.get_secret(project_id, name, headers={})

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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "format": "generic", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-secret", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "resource_type"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "format": "generic", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-secret", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "resource_type"}'
        responses.add(responses.PUT, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-secret'
        if_match = 'testString'
        data = {'key1': 'testString'}
        format = 'generic'

        # Invoke method
        response = _service.replace_secret(project_id, name, if_match, data=data, format=format, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['data'] == {'key1': 'testString'}
        assert req_body['format'] == 'generic'

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
        mock_response = '{"created_at": "2022-09-13T11:41:35+02:00", "data": {"mapKey": "inner"}, "entity_tag": "2385407409", "format": "generic", "href": "https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret", "id": "e33b1cv7-7390-4437-a5c2-130d5ccdddc3", "name": "my-secret", "project_id": "4e49b3e0-27a8-48d2-a784-c7ee48bb863b", "resource_type": "resource_type"}'
        responses.add(responses.PUT, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-secret'
        if_match = 'testString'
        data = {'key1': 'testString'}
        format = 'generic'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
            "if_match": if_match,
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
        responses.add(responses.DELETE, url, status=202)

        # Set up parameter values
        project_id = '15314cc3-85b4-4338-903f-c28cdee6d005'
        name = 'my-secret'

        # Invoke method
        response = _service.delete_secret(project_id, name, headers={})

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
        responses.add(responses.DELETE, url, status=202)

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
# End of Service: SecretsAndConfigMaps
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
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
        env_var_model['name'] = 'CE_SUBDOMAIN'
        env_var_model['prefix'] = 'PREFIX_'
        env_var_model['reference'] = 'my-secret'
        env_var_model['type'] = 'literal'
        env_var_model['value'] = 'uyh5shf7s0f'

        volume_mount_model = {}  # VolumeMount
        volume_mount_model['mount_path'] = '/app'
        volume_mount_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_model['reference'] = 'my-secret'
        volume_mount_model['type'] = 'secret'

        app_status_model = {}  # AppStatus
        app_status_model['latest_created_revision'] = 'my-app-00001'
        app_status_model['latest_ready_revision'] = 'my-app-00001'
        app_status_model['reason'] = 'ready'

        # Construct a json representation of a App model
        app_model_json = {}
        app_model_json['created_at'] = '2022-09-13T11:41:35+02:00'
        app_model_json['endpoint'] = 'https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud'
        app_model_json['endpoint_internal'] = 'http://my-app.vg67hzldruk.svc.cluster.local'
        app_model_json['entity_tag'] = '2385407409'
        app_model_json[
            'href'
        ] = 'https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app'
        app_model_json['id'] = 'e33b1cv7-7390-4437-a5c2-130d5ccdddc3'
        app_model_json['image_port'] = 8080
        app_model_json['image_reference'] = 'icr.io/codeengine/helloworld'
        app_model_json['image_secret'] = 'my-secret'
        app_model_json['managed_domain_mappings'] = 'local_public'
        app_model_json['name'] = 'my-app'
        app_model_json['project_id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'
        app_model_json['resource_type'] = 'app_v2'
        app_model_json['run_arguments'] = ['testString']
        app_model_json['run_as_user'] = 1001
        app_model_json['run_commands'] = ['testString']
        app_model_json['run_env_variables'] = [env_var_model]
        app_model_json['run_service_account'] = 'default'
        app_model_json['run_volume_mounts'] = [volume_mount_model]
        app_model_json['scale_concurrency'] = 100
        app_model_json['scale_concurrency_target'] = 80
        app_model_json['scale_cpu_limit'] = '1'
        app_model_json['scale_ephemeral_storage_limit'] = '4G'
        app_model_json['scale_initial_instances'] = 1
        app_model_json['scale_max_instances'] = 10
        app_model_json['scale_memory_limit'] = '4G'
        app_model_json['scale_min_instances'] = 1
        app_model_json['scale_request_timeout'] = 300
        app_model_json['status'] = 'ready'
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
        env_var_model['name'] = 'CE_SUBDOMAIN'
        env_var_model['prefix'] = 'PREFIX_'
        env_var_model['reference'] = 'my-secret'
        env_var_model['type'] = 'literal'
        env_var_model['value'] = 'uyh5shf7s0f'

        volume_mount_model = {}  # VolumeMount
        volume_mount_model['mount_path'] = '/app'
        volume_mount_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_model['reference'] = 'my-secret'
        volume_mount_model['type'] = 'secret'

        app_status_model = {}  # AppStatus
        app_status_model['latest_created_revision'] = 'my-app-00001'
        app_status_model['latest_ready_revision'] = 'my-app-00001'
        app_status_model['reason'] = 'ready'

        app_model = {}  # App
        app_model['created_at'] = '2022-11-15T22:07:55+01:00'
        app_model['endpoint'] = 'https://my-app.vg67hzldruk.eu-de.codeengine.appdomain.cloud'
        app_model['endpoint_internal'] = 'http://my-app.vg67hzldruk.svc.cluster.local'
        app_model['entity_tag'] = '1'
        app_model[
            'href'
        ] = 'https://api.us-east.codeengine.cloud.ibm.com/v2/projects/230828b4-4f15-40a9-b183-1268c6ab88d5/apps/my-app'
        app_model['id'] = '230828b4-4f15-40a9-b183-1268c6ab88d5'
        app_model['image_port'] = 8080
        app_model['image_reference'] = 'icr.io/codeengine/helloworld'
        app_model['image_secret'] = 'my-secret'
        app_model['managed_domain_mappings'] = 'local_public'
        app_model['name'] = 'my-app'
        app_model['project_id'] = '15314cc3-85b4-4338-903f-c28cdee6d005'
        app_model['resource_type'] = 'app_v2'
        app_model['run_arguments'] = []
        app_model['run_as_user'] = 1001
        app_model['run_commands'] = []
        app_model['run_env_variables'] = [env_var_model]
        app_model['run_service_account'] = 'default'
        app_model['run_volume_mounts'] = [volume_mount_model]
        app_model['scale_concurrency'] = 100
        app_model['scale_concurrency_target'] = 80
        app_model['scale_cpu_limit'] = '1'
        app_model['scale_ephemeral_storage_limit'] = '400M'
        app_model['scale_initial_instances'] = 1
        app_model['scale_max_instances'] = 10
        app_model['scale_memory_limit'] = '4G'
        app_model['scale_min_instances'] = 0
        app_model['scale_request_timeout'] = 300
        app_model['status'] = 'ready'
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
        app_patch_model_json['run_arguments'] = ['testString']
        app_patch_model_json['run_as_user'] = 1001
        app_patch_model_json['run_commands'] = ['testString']
        app_patch_model_json['run_env_variables'] = [env_var_prototype_model]
        app_patch_model_json['run_service_account'] = 'default'
        app_patch_model_json['run_volume_mounts'] = [volume_mount_prototype_model]
        app_patch_model_json['scale_concurrency'] = 100
        app_patch_model_json['scale_concurrency_target'] = 80
        app_patch_model_json['scale_cpu_limit'] = '1'
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
        env_var_model['name'] = 'CE_SUBDOMAIN'
        env_var_model['prefix'] = 'PREFIX_'
        env_var_model['reference'] = 'my-secret'
        env_var_model['type'] = 'literal'
        env_var_model['value'] = 'uyh5shf7s0f'

        volume_mount_model = {}  # VolumeMount
        volume_mount_model['mount_path'] = '/app'
        volume_mount_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_model['reference'] = 'my-secret'
        volume_mount_model['type'] = 'secret'

        app_revision_status_model = {}  # AppRevisionStatus
        app_revision_status_model['actual_instances'] = 1
        app_revision_status_model['reason'] = 'ready'

        # Construct a json representation of a AppRevision model
        app_revision_model_json = {}
        app_revision_model_json['app_name'] = 'my-app'
        app_revision_model_json['created_at'] = '2022-09-13T11:41:35+02:00'
        app_revision_model_json[
            'href'
        ] = 'https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/apps/my-app/revisions/my-app-00001'
        app_revision_model_json['id'] = 'e33b1cv7-7390-4437-a5c2-130d5ccdddc3'
        app_revision_model_json['image_port'] = 8080
        app_revision_model_json['image_reference'] = 'icr.io/codeengine/helloworld'
        app_revision_model_json['image_secret'] = 'my-secret'
        app_revision_model_json['name'] = 'my-app-00001'
        app_revision_model_json['project_id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'
        app_revision_model_json['resource_type'] = 'app_revision_v2'
        app_revision_model_json['run_arguments'] = ['testString']
        app_revision_model_json['run_as_user'] = 1001
        app_revision_model_json['run_commands'] = ['testString']
        app_revision_model_json['run_env_variables'] = [env_var_model]
        app_revision_model_json['run_service_account'] = 'default'
        app_revision_model_json['run_volume_mounts'] = [volume_mount_model]
        app_revision_model_json['scale_concurrency'] = 100
        app_revision_model_json['scale_concurrency_target'] = 80
        app_revision_model_json['scale_cpu_limit'] = '1'
        app_revision_model_json['scale_ephemeral_storage_limit'] = '4G'
        app_revision_model_json['scale_initial_instances'] = 1
        app_revision_model_json['scale_max_instances'] = 10
        app_revision_model_json['scale_memory_limit'] = '4G'
        app_revision_model_json['scale_min_instances'] = 1
        app_revision_model_json['scale_request_timeout'] = 300
        app_revision_model_json['status'] = 'ready'
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
        env_var_model['name'] = 'CE_SUBDOMAIN'
        env_var_model['prefix'] = 'PREFIX_'
        env_var_model['reference'] = 'my-secret'
        env_var_model['type'] = 'literal'
        env_var_model['value'] = 'uyh5shf7s0f'

        volume_mount_model = {}  # VolumeMount
        volume_mount_model['mount_path'] = '/app'
        volume_mount_model['name'] = 'codeengine-mount-b69u90'
        volume_mount_model['reference'] = 'my-secret'
        volume_mount_model['type'] = 'secret'

        app_revision_status_model = {}  # AppRevisionStatus
        app_revision_status_model['actual_instances'] = 1
        app_revision_status_model['reason'] = 'ready'

        app_revision_model = {}  # AppRevision
        app_revision_model['app_name'] = 'my-app'
        app_revision_model['created_at'] = '2022-11-15T22:07:55+01:00'
        app_revision_model[
            'href'
        ] = 'https://api.us-east.codeengine.cloud.ibm.com/v2/projects/230828b4-4f15-40a9-b183-1268c6ab88d5/apps/my-app/revisions/my-app-00001'
        app_revision_model['id'] = 'b63b3e28-2c1b-4784-9cd6-18c201fc6806'
        app_revision_model['image_port'] = 8080
        app_revision_model['image_reference'] = 'icr.io/codeengine/helloworld'
        app_revision_model['image_secret'] = 'my-secret'
        app_revision_model['name'] = 'my-app-00001'
        app_revision_model['project_id'] = '230828b4-4f15-40a9-b183-1268c6ab88d5'
        app_revision_model['resource_type'] = 'app_revision_v2'
        app_revision_model['run_arguments'] = []
        app_revision_model['run_as_user'] = 1001
        app_revision_model['run_commands'] = []
        app_revision_model['run_env_variables'] = [env_var_model]
        app_revision_model['run_service_account'] = 'default'
        app_revision_model['run_volume_mounts'] = [volume_mount_model]
        app_revision_model['scale_concurrency'] = 100
        app_revision_model['scale_concurrency_target'] = 80
        app_revision_model['scale_cpu_limit'] = '1'
        app_revision_model['scale_ephemeral_storage_limit'] = '400M'
        app_revision_model['scale_initial_instances'] = 1
        app_revision_model['scale_max_instances'] = 10
        app_revision_model['scale_memory_limit'] = '4G'
        app_revision_model['scale_min_instances'] = 0
        app_revision_model['scale_request_timeout'] = 300
        app_revision_model['status'] = 'ready'
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
        app_revision_status_model_json['actual_instances'] = 1
        app_revision_status_model_json['reason'] = 'ready'

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
        app_status_model_json['latest_created_revision'] = 'my-app-00001'
        app_status_model_json['latest_ready_revision'] = 'my-app-00001'
        app_status_model_json['reason'] = 'ready'

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
        build_status_model['reason'] = 'registered'

        # Construct a json representation of a Build model
        build_model_json = {}
        build_model_json['created_at'] = '2022-09-13T11:41:35+02:00'
        build_model_json['entity_tag'] = '2385407409'
        build_model_json[
            'href'
        ] = 'https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/builds/my-build'
        build_model_json['id'] = 'e33b1cv7-7390-4437-a5c2-130d5ccdddc3'
        build_model_json['name'] = 'my-build'
        build_model_json['output_image'] = 'private.de.icr.io/icr_namespace/image-name'
        build_model_json['output_secret'] = 'ce-auto-icr-private-eu-de'
        build_model_json['project_id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'
        build_model_json['resource_type'] = 'build_v2'
        build_model_json['source_context_dir'] = 'some/subfolder'
        build_model_json['source_revision'] = 'main'
        build_model_json['source_secret'] = 'testString'
        build_model_json['source_type'] = 'git'
        build_model_json['source_url'] = 'https://github.com/IBM/CodeEngine'
        build_model_json['status'] = 'ready'
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
        build_status_model['reason'] = 'registered'

        build_model = {}  # Build
        build_model['created_at'] = '2022-11-15T11:31:27+01:00'
        build_model['entity_tag'] = '2385407409'
        build_model[
            'href'
        ] = 'https://api.us-east.codeengine.cloud.ibm.com/v2/projects/230828b4-4f15-40a9-b183-1268c6ab88d5/builds/my-build'
        build_model['id'] = '27587824-aba8-4f70-8c1d-416326907049'
        build_model['name'] = 'my-build'
        build_model['output_image'] = 'private.de.icr.io/icr_namespace/test-image-1'
        build_model['output_secret'] = 'ce-auto-icr-private-eu-de'
        build_model['project_id'] = '230828b4-4f15-40a9-b183-1268c6ab88d5'
        build_model['resource_type'] = 'build_v2'
        build_model['source_context_dir'] = 'some/subfolder'
        build_model['source_revision'] = 'main'
        build_model['source_secret'] = 'testString'
        build_model['source_type'] = 'git'
        build_model['source_url'] = 'https://github.com/IBM/CodeEngine'
        build_model['status'] = 'ready'
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
        build_run_status_model['completion_time'] = '2022-09-22T17:40:00Z'
        build_run_status_model[
            'output_digest'
        ] = 'sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384'
        build_run_status_model['reason'] = 'succeeded'
        build_run_status_model['start_time'] = '2022-09-22T17:34:00Z'

        # Construct a json representation of a BuildRun model
        build_run_model_json = {}
        build_run_model_json['build_name'] = 'testString'
        build_run_model_json['created_at'] = '2022-09-13T11:41:35+02:00'
        build_run_model_json[
            'href'
        ] = 'https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-build-run'
        build_run_model_json['id'] = 'e33b1cv7-7390-4437-a5c2-130d5ccdddc3'
        build_run_model_json['name'] = 'my-build-run'
        build_run_model_json['output_image'] = 'private.de.icr.io/icr_namespace/image-name'
        build_run_model_json['output_secret'] = 'ce-auto-icr-private-eu-de'
        build_run_model_json['project_id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'
        build_run_model_json['resource_type'] = 'build_run_v2'
        build_run_model_json['service_account'] = 'default'
        build_run_model_json['source_context_dir'] = 'some/subfolder'
        build_run_model_json['source_revision'] = 'main'
        build_run_model_json['source_secret'] = 'testString'
        build_run_model_json['source_type'] = 'git'
        build_run_model_json['source_url'] = 'https://github.com/IBM/CodeEngine'
        build_run_model_json['status'] = 'succeeded'
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
        build_run_status_model['completion_time'] = '2022-09-22T17:40:00Z'
        build_run_status_model[
            'output_digest'
        ] = 'sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384'
        build_run_status_model['reason'] = 'succeeded'
        build_run_status_model['start_time'] = '2022-09-22T17:34:00Z'

        build_run_model = {}  # BuildRun
        build_run_model['build_name'] = 'my-build'
        build_run_model['created_at'] = '2022-06-20T10:10:00+02:00'
        build_run_model[
            'href'
        ] = 'https://api.us-east.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/build_runs/my-buildrun-1'
        build_run_model['id'] = 'ca151bf7-b1bf-4e18-a1cb-857329c2d097'
        build_run_model['name'] = 'my-buildrun-1'
        build_run_model['output_image'] = 'private.de.icr.io/icr_namespace/image-name'
        build_run_model['output_secret'] = 'ce-auto-icr-private-eu-de'
        build_run_model['project_id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'
        build_run_model['resource_type'] = 'build_run_v2'
        build_run_model['service_account'] = 'default'
        build_run_model['source_context_dir'] = 'some/subfolder'
        build_run_model['source_revision'] = 'main'
        build_run_model['source_secret'] = 'testString'
        build_run_model['source_type'] = 'git'
        build_run_model['source_url'] = 'https://github.com/IBM/CodeEngine'
        build_run_model['status'] = 'succeeded'
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
        build_run_status_model_json['completion_time'] = '2022-09-22T17:40:00Z'
        build_run_status_model_json[
            'output_digest'
        ] = 'sha256:9a3d845c629d2b4a6b271b1d526dfafc1e7d9511f8863b43b5bb0483ef626384'
        build_run_status_model_json['reason'] = 'succeeded'
        build_run_status_model_json['start_time'] = '2022-09-22T17:34:00Z'

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
        build_status_model_json['reason'] = 'registered'

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
        config_map_model_json['created_at'] = '2022-09-13T11:41:35+02:00'
        config_map_model_json['data'] = {'key1': 'testString'}
        config_map_model_json['entity_tag'] = '2385407409'
        config_map_model_json[
            'href'
        ] = 'https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/config_maps/my-config-map'
        config_map_model_json['id'] = 'e33b1cv7-7390-4437-a5c2-130d5ccdddc3'
        config_map_model_json['name'] = 'my-config-map'
        config_map_model_json['project_id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'
        config_map_model_json['resource_type'] = 'config_map_v2'

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
        config_map_model['created_at'] = '2022-11-15T21:45:49+01:00'
        config_map_model['data'] = {'key1': 'testString'}
        config_map_model['entity_tag'] = '2386238209'
        config_map_model[
            'href'
        ] = 'https://api.us-east.codeengine.cloud.ibm.com/v2/projects/230828b4-4f15-40a9-b183-1268c6ab88d5/config_maps/my-config-map'
        config_map_model['id'] = 'b8376985-d6df-43c5-8feb-194d45390bc8'
        config_map_model['name'] = 'my-config-map'
        config_map_model['project_id'] = '230828b4-4f15-40a9-b183-1268c6ab88d5'
        config_map_model['resource_type'] = 'config_map_v2'

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
        job_model_json['created_at'] = '2022-09-13T11:41:35+02:00'
        job_model_json['entity_tag'] = '2385407409'
        job_model_json[
            'href'
        ] = 'https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/jobs/my-job'
        job_model_json['id'] = 'e33b1cv7-7390-4437-a5c2-130d5ccdddc3'
        job_model_json['image_reference'] = 'icr.io/codeengine/helloworld'
        job_model_json['image_secret'] = 'my-secret'
        job_model_json['name'] = 'my-job'
        job_model_json['project_id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'
        job_model_json['resource_type'] = 'job_v2'
        job_model_json['run_arguments'] = ['testString']
        job_model_json['run_as_user'] = 1001
        job_model_json['run_commands'] = ['testString']
        job_model_json['run_env_variables'] = [env_var_model]
        job_model_json['run_mode'] = 'daemon'
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
        job_model['created_at'] = '2022-11-15T21:40:40+01:00'
        job_model['entity_tag'] = '2386231540'
        job_model[
            'href'
        ] = 'https://api.us-east.codeengine.cloud.ibm.com/v2/projects/230828b4-4f15-40a9-b183-1268c6ab88d5/jobs/my-job'
        job_model['id'] = '7e49dd78-09d0-45c7-ad7e-cd968e0e7747'
        job_model['image_reference'] = 'icr.io/codeengine/helloworld'
        job_model['image_secret'] = 'my-secret'
        job_model['name'] = 'my-job'
        job_model['project_id'] = '230828b4-4f15-40a9-b183-1268c6ab88d5'
        job_model['resource_type'] = 'job_v2'
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
        job_patch_model_json['run_mode'] = 'daemon'
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
        job_run_status_model['completion_time'] = '2022-09-22T17:40:00Z'
        job_run_status_model['failed'] = 0
        job_run_status_model['pending'] = 0
        job_run_status_model['requested'] = 0
        job_run_status_model['running'] = 0
        job_run_status_model['start_time'] = '2022-09-22T17:34:00Z'
        job_run_status_model['succeeded'] = 1
        job_run_status_model['unknown'] = 0

        # Construct a json representation of a JobRun model
        job_run_model_json = {}
        job_run_model_json['created_at'] = '2022-09-13T11:41:35+02:00'
        job_run_model_json[
            'href'
        ] = 'https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/job_runs/my-job-run'
        job_run_model_json['id'] = 'e33b1cv7-7390-4437-a5c2-130d5ccdddc3'
        job_run_model_json['image_reference'] = 'icr.io/codeengine/helloworld'
        job_run_model_json['image_secret'] = 'my-secret'
        job_run_model_json['job_name'] = 'my-job'
        job_run_model_json['name'] = 'my-job-run'
        job_run_model_json['project_id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'
        job_run_model_json['resource_type'] = 'job_run_v2'
        job_run_model_json['run_arguments'] = ['testString']
        job_run_model_json['run_as_user'] = 1001
        job_run_model_json['run_commands'] = ['testString']
        job_run_model_json['run_env_variables'] = [env_var_model]
        job_run_model_json['run_mode'] = 'daemon'
        job_run_model_json['run_service_account'] = 'default'
        job_run_model_json['run_volume_mounts'] = [volume_mount_model]
        job_run_model_json['scale_array_spec'] = '1-5,7-8,10'
        job_run_model_json['scale_cpu_limit'] = '1'
        job_run_model_json['scale_ephemeral_storage_limit'] = '4G'
        job_run_model_json['scale_max_execution_time'] = 7200
        job_run_model_json['scale_memory_limit'] = '4G'
        job_run_model_json['scale_retry_limit'] = 3
        job_run_model_json['status'] = 'completed'
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
        job_run_status_model['completion_time'] = '2022-09-22T17:40:00Z'
        job_run_status_model['failed'] = 0
        job_run_status_model['pending'] = 0
        job_run_status_model['requested'] = 0
        job_run_status_model['running'] = 0
        job_run_status_model['start_time'] = '2022-09-22T17:34:00Z'
        job_run_status_model['succeeded'] = 1
        job_run_status_model['unknown'] = 0

        job_run_model = {}  # JobRun
        job_run_model['created_at'] = '2022-11-15T22:06:21+01:00'
        job_run_model[
            'href'
        ] = 'https://api.us-east.codeengine.cloud.ibm.com/v2/projects/230828b4-4f15-40a9-b183-1268c6ab88d5/jobs/my-job-run-1'
        job_run_model['id'] = 'ced5039e-b1d3-4c51-aa29-8dbde3531ace'
        job_run_model['image_reference'] = 'icr.io/codeengine/helloworld'
        job_run_model['image_secret'] = 'my-secret'
        job_run_model['job_name'] = 'my-job'
        job_run_model['name'] = 'my-job-run-1'
        job_run_model['project_id'] = '230828b4-4f15-40a9-b183-1268c6ab88d5'
        job_run_model['resource_type'] = 'job_run_v2'
        job_run_model['run_arguments'] = []
        job_run_model['run_as_user'] = 1001
        job_run_model['run_commands'] = []
        job_run_model['run_env_variables'] = [env_var_model]
        job_run_model['run_mode'] = 'task'
        job_run_model['run_service_account'] = 'default'
        job_run_model['run_volume_mounts'] = [volume_mount_model]
        job_run_model['scale_array_spec'] = '0'
        job_run_model['scale_cpu_limit'] = '1'
        job_run_model['scale_ephemeral_storage_limit'] = '400M'
        job_run_model['scale_max_execution_time'] = 7200
        job_run_model['scale_memory_limit'] = '4G'
        job_run_model['scale_retry_limit'] = 3
        job_run_model['status'] = 'completed'
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
        job_run_status_model_json['completion_time'] = '2022-09-22T17:40:00Z'
        job_run_status_model_json['failed'] = 0
        job_run_status_model_json['pending'] = 0
        job_run_status_model_json['requested'] = 0
        job_run_status_model_json['running'] = 0
        job_run_status_model_json['start_time'] = '2022-09-22T17:34:00Z'
        job_run_status_model_json['succeeded'] = 1
        job_run_status_model_json['unknown'] = 0

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
        project_model_json['account_id'] = '4329073d16d2f3663f74bfa955259139'
        project_model_json['created_at'] = '2021-03-29T12:18:13.992359829Z'
        project_model_json[
            'crn'
        ] = 'crn:v1:bluemix:public:codeengine:eu-de:a/4329073d16d2f3663f74bfa955259139:4e49b3e0-27a8-48d2-a784-c7ee48bb863b::'
        project_model_json[
            'href'
        ] = 'https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b'
        project_model_json['id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'
        project_model_json['name'] = 'project-name'
        project_model_json['region'] = 'us-east'
        project_model_json['resource_group_id'] = '5c49eabcf5e85881a37e2d100a33b3df'
        project_model_json['resource_type'] = 'project_v2'
        project_model_json['status'] = 'active'

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
        project_model['account_id'] = 'f9f1030ebf674eda8d57bdbc2b9e536a'
        project_model['created_at'] = '2021-03-29T12:18:13.992359829Z'
        project_model[
            'crn'
        ] = 'crn:v1:bluemix:public:codeengine:us-east:a/4329073d16d2f3663f74bfa955259139:15314cc3-85b4-4338-903f-c28cdee6d005::'
        project_model[
            'href'
        ] = 'https://api.us-east.codeengine.cloud.ibm.com/v2/projects/15314cc3-85b4-4338-903f-c28cdee6d005'
        project_model['id'] = '15314cc3-85b4-4338-903f-c28cdee6d005'
        project_model['name'] = 'test_project'
        project_model['region'] = 'us-east'
        project_model['resource_group_id'] = 'b91e849cedb04e7e92bd68c040c672dc'
        project_model['resource_type'] = 'project_v2'
        project_model['status'] = 'active'

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


class TestModel_Secret:
    """
    Test Class for Secret
    """

    def test_secret_serialization(self):
        """
        Test serialization/deserialization for Secret
        """

        # Construct a json representation of a Secret model
        secret_model_json = {}
        secret_model_json['created_at'] = '2022-09-13T11:41:35+02:00'
        secret_model_json['data'] = {'key1': 'testString'}
        secret_model_json['entity_tag'] = '2385407409'
        secret_model_json['format'] = 'generic'
        secret_model_json[
            'href'
        ] = 'https://api.eu-de.codeengine.cloud.ibm.com/v2/projects/4e49b3e0-27a8-48d2-a784-c7ee48bb863b/secrets/my-secret'
        secret_model_json['id'] = 'e33b1cv7-7390-4437-a5c2-130d5ccdddc3'
        secret_model_json['name'] = 'my-secret'
        secret_model_json['project_id'] = '4e49b3e0-27a8-48d2-a784-c7ee48bb863b'
        secret_model_json['resource_type'] = 'testString'

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

        secret_model = {}  # Secret
        secret_model['created_at'] = '2022-11-15T21:59:08+01:00'
        secret_model['data'] = {'key1': 'testString'}
        secret_model['entity_tag'] = '2386255530'
        secret_model['format'] = 'generic'
        secret_model[
            'href'
        ] = 'https://api.us-east.codeengine.cloud.ibm.com/v2/projects/230828b4-4f15-40a9-b183-1268c6ab88d5/secrets/my-secret'
        secret_model['id'] = '36e3a621-4895-4bd1-b7e8-1163ab49a28f'
        secret_model['name'] = 'my-secret'
        secret_model['project_id'] = '230828b4-4f15-40a9-b183-1268c6ab88d5'
        secret_model['resource_type'] = 'secret_generic_v2'

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


# endregion
##############################################################################
# End of Model Tests
##############################################################################

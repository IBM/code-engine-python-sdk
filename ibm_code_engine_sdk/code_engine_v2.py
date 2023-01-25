# coding: utf-8

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

# IBM OpenAPI SDK Code Generator Version: 3.64.0-959a5845-20230112-195144

"""
REST API for Code Engine

API Version: 2.0.0
"""

from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class CodeEngineV2(BaseService):
    """The Code Engine V2 service."""

    DEFAULT_SERVICE_URL = 'https://api.au-syd.codeengine.cloud.ibm.com/v2'
    DEFAULT_SERVICE_NAME = 'code_engine'

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'CodeEngineV2':
        """
        Return a new client for the Code Engine service using the specified
               parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(authenticator)
        service.configure_service(service_name)
        return service

    def __init__(
        self,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the Code Engine service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)

    #########################
    # Projects
    #########################

    def list_projects(self, *, limit: int = None, start: str = None, **kwargs) -> DetailedResponse:
        """
        List all projects.

        List all projects in the current account.

        :param int limit: (optional) Optional maximum number of projects per page.
        :param str start: (optional) An optional token that indicates the beginning
               of the page of results to be returned. Any additional query parameters are
               ignored if a page token is present. If omitted, the first page of results
               is returned. This value is obtained from the 'start' query parameter in the
               'next_url' field of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectList` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='list_projects'
        )
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'start': start,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/projects'
        request = self.prepare_request(method='GET', url=url, headers=headers, params=params)

        response = self.send(request, **kwargs)
        return response

    def create_project(
        self, name: str, *, resource_group_id: str = None, tags: List[str] = None, **kwargs
    ) -> DetailedResponse:
        """
        Create a project.

        Create a Code Engine project on IBM Cloud. The project will be created in the
        region that corresponds to the API endpoint that is being called.

        :param str name: The name of the project.
        :param str resource_group_id: (optional) Optional ID of the resource group
               for your project deployment. If this field is not defined, the default
               resource group of the account will be used.
        :param List[str] tags: (optional) Optional list of labels to assign to your
               project. Tags are not part of the project resource that is returned by the
               server, but can be obtained and managed through the Global Tagging API in
               IBM Cloud. Find more information on [Global Tagging API
               docs](https://cloud.ibm.com/apidocs/tagging).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Project` object
        """

        if name is None:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='create_project'
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'resource_group_id': resource_group_id,
            'tags': tags,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/projects'
        request = self.prepare_request(method='POST', url=url, headers=headers, data=data)

        response = self.send(request, **kwargs)
        return response

    def get_project(self, id: str, **kwargs) -> DetailedResponse:
        """
        Get a project.

        Display the details of a single project.

        :param str id: The ID of the project.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Project` object
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_project'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def delete_project(self, id: str, **kwargs) -> DetailedResponse:
        """
        Delete a project.

        Delete a project.

        :param str id: The ID of the project.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='delete_project'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Applications
    #########################

    def list_apps(self, project_id: str, *, limit: int = None, start: str = None, **kwargs) -> DetailedResponse:
        """
        List applications.

        List all applications in a project.

        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of apps per page.
        :param str start: (optional) An optional token that indicates the beginning
               of the page of results to be returned. If omitted, the first page of
               results is returned. This value is obtained from the 'start' query
               parameter in the 'next_url' field of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AppList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='list_apps'
        )
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'start': start,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/apps'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers, params=params)

        response = self.send(request, **kwargs)
        return response

    def create_app(
        self,
        project_id: str,
        image_reference: str,
        name: str,
        *,
        image_port: int = None,
        image_secret: str = None,
        managed_domain_mappings: str = None,
        run_arguments: List[str] = None,
        run_as_user: int = None,
        run_commands: List[str] = None,
        run_env_variables: List['EnvVarPrototype'] = None,
        run_service_account: str = None,
        run_volume_mounts: List['VolumeMountPrototype'] = None,
        scale_concurrency: int = None,
        scale_concurrency_target: int = None,
        scale_cpu_limit: str = None,
        scale_ephemeral_storage_limit: str = None,
        scale_initial_instances: int = None,
        scale_max_instances: int = None,
        scale_memory_limit: str = None,
        scale_min_instances: int = None,
        scale_request_timeout: int = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create an application.

        Create an application.

        :param str project_id: The ID of the project.
        :param str image_reference: The name of the image that is used for this
               job. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and
               `TAG` are optional. If `REGISTRY` is not specified, the default is
               `docker.io`. If `TAG` is not specified, the default is `latest`. If the
               image reference points to a registry that requires authentication, make
               sure to also specify the property `image_secret`.
        :param str name: The name of the app. Use a name that is unique within the
               project.
        :param int image_port: (optional) Optional port the app listens on. While
               the app will always be exposed via port `443` for end users, this port is
               used to connect to the port that is exposed by the container image.
        :param str image_secret: (optional) Optional name of the image registry
               access secret. The image registry access secret is used to authenticate
               with a private registry when you download the container image. If the image
               reference points to a registry that requires authentication, the app will
               be created but cannot reach the ready status, until this property is
               provided, too.
        :param str managed_domain_mappings: (optional) Optional value controlling
               which of the system managed domain mappings will be setup for the
               application. Valid values are 'local_public', 'local_private' and 'local'.
               Visibility can only be 'local_private' if the project supports application
               private visibility.
        :param List[str] run_arguments: (optional) Optional arguments for the app
               that are passed to start the container. If not specified an empty string
               array will be applied and the arguments specified by the container image,
               will be used to start the container.
        :param int run_as_user: (optional) Optional user ID (UID) to run the app
               (e.g., `1001`).
        :param List[str] run_commands: (optional) Optional commands for the app
               that are passed to start the container. If not specified an empty string
               array will be applied and the command specified by the container image,
               will be used to start the container.
        :param List[EnvVarPrototype] run_env_variables: (optional) Optional
               references to config maps, secrets or a literal values that are exposed as
               environment variables within the running application.
        :param str run_service_account: (optional) Optional name of the service
               account. For built-in service accounts, you can use the shortened names
               `manager` , `none`, `reader`, and `writer`.
        :param List[VolumeMountPrototype] run_volume_mounts: (optional) Optional
               mounts of config maps or a secrets.
        :param int scale_concurrency: (optional) Optional maximum number of
               requests that can be processed concurrently per instance.
        :param int scale_concurrency_target: (optional) Optional threshold of
               concurrent requests per instance at which one or more additional instances
               are created. Use this value to scale up instances based on concurrent
               number of requests. This option defaults to the value of the
               `scale_concurrency` option, if not specified.
        :param str scale_cpu_limit: (optional) Optional number of CPU set for the
               instance of the app. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
        :param str scale_ephemeral_storage_limit: (optional) Optional amount of
               ephemeral storage to set for the instance of the app. The amount specified
               as ephemeral storage, must not exceed the amount of `scale_memory_limit`.
               The units for specifying ephemeral storage are Megabyte (M) or Gigabyte
               (G), whereas G and M are the shorthand expressions for GB and MB. For more
               information see [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param int scale_initial_instances: (optional) Optional initial number of
               instances that are created upon app creation or app update.
        :param int scale_max_instances: (optional) Optional maximum number of
               instances for this app. If you set this value to `0`, this property does
               not set a upper scaling limit. However, the app scaling is still limited by
               the project quota for instances. See [Limits and quotas for Code
               Engine](https://cloud.ibm.com/docs/codeengine?topic=codeengine-limits).
        :param str scale_memory_limit: (optional) Optional amount of memory set for
               the instance of the app. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
               The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G
               and M are the shorthand expressions for GB and MB. For more information see
               [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param int scale_min_instances: (optional) Optional minimum number of
               instances for this app. If you set this value to `0`, the app will scale
               down to zero, if not hit by any request for some time.
        :param int scale_request_timeout: (optional) Optional amount of time in
               seconds that is allowed for a running app to respond to a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `App` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if image_reference is None:
            raise ValueError('image_reference must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if run_env_variables is not None:
            run_env_variables = [convert_model(x) for x in run_env_variables]
        if run_volume_mounts is not None:
            run_volume_mounts = [convert_model(x) for x in run_volume_mounts]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='create_app'
        )
        headers.update(sdk_headers)

        data = {
            'image_reference': image_reference,
            'name': name,
            'image_port': image_port,
            'image_secret': image_secret,
            'managed_domain_mappings': managed_domain_mappings,
            'run_arguments': run_arguments,
            'run_as_user': run_as_user,
            'run_commands': run_commands,
            'run_env_variables': run_env_variables,
            'run_service_account': run_service_account,
            'run_volume_mounts': run_volume_mounts,
            'scale_concurrency': scale_concurrency,
            'scale_concurrency_target': scale_concurrency_target,
            'scale_cpu_limit': scale_cpu_limit,
            'scale_ephemeral_storage_limit': scale_ephemeral_storage_limit,
            'scale_initial_instances': scale_initial_instances,
            'scale_max_instances': scale_max_instances,
            'scale_memory_limit': scale_memory_limit,
            'scale_min_instances': scale_min_instances,
            'scale_request_timeout': scale_request_timeout,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/apps'.format(**path_param_dict)
        request = self.prepare_request(method='POST', url=url, headers=headers, data=data)

        response = self.send(request, **kwargs)
        return response

    def get_app(self, project_id: str, name: str, **kwargs) -> DetailedResponse:
        """
        Get an application.

        Display the details of an application.

        :param str project_id: The ID of the project.
        :param str name: The name of your application.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `App` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_app'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/apps/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def delete_app(self, project_id: str, name: str, **kwargs) -> DetailedResponse:
        """
        Delete an application.

        Delete an application.

        :param str project_id: The ID of the project.
        :param str name: The name of your application.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='delete_app'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/apps/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def update_app(self, project_id: str, name: str, if_match: str, app: 'AppPatch', **kwargs) -> DetailedResponse:
        """
        Update an application.

        An application contains one or more revisions. A revision represents an immutable
        version of the configuration properties of the application. Each update of an
        application configuration property creates a new revision of the application.
        [Learn more](https://cloud.ibm.com/docs/codeengine?topic=codeengine-update-app).

        :param str project_id: The ID of the project.
        :param str name: The name of your application.
        :param str if_match: Version of the app settings to be updated. Specify the
               version that you retrieved as entity_tag (ETag header) when reading the
               app. This value helps identifying parallel usage of this API. Pass * to
               indicate to update any version available. This might result in stale
               updates.
        :param AppPatch app: App patch.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `App` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        if not if_match:
            raise ValueError('if_match must be provided')
        if app is None:
            raise ValueError('app must be provided')
        if isinstance(app, AppPatch):
            app = convert_model(app)
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='update_app'
        )
        headers.update(sdk_headers)

        data = json.dumps(app)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/apps/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH', url=url, headers=headers, data=data)

        response = self.send(request, **kwargs)
        return response

    def list_app_revisions(
        self, project_id: str, app_name: str, *, limit: int = None, start: str = None, **kwargs
    ) -> DetailedResponse:
        """
        List application revisions.

        List all application revisions in a particular application.

        :param str project_id: The ID of the project.
        :param str app_name: The name of your application.
        :param int limit: (optional) Optional maximum number of apps per page.
        :param str start: (optional) An optional token that indicates the beginning
               of the page of results to be returned. If omitted, the first page of
               results is returned. This value is obtained from the 'start' query
               parameter in the 'next_url' field of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AppRevisionList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not app_name:
            raise ValueError('app_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='list_app_revisions'
        )
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'start': start,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'app_name']
        path_param_values = self.encode_path_vars(project_id, app_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/apps/{app_name}/revisions'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers, params=params)

        response = self.send(request, **kwargs)
        return response

    def get_app_revision(self, project_id: str, app_name: str, name: str, **kwargs) -> DetailedResponse:
        """
        Get an application revision.

        Display the details of an application revision.

        :param str project_id: The ID of the project.
        :param str app_name: The name of your application.
        :param str name: The name of your application revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AppRevision` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not app_name:
            raise ValueError('app_name must be provided')
        if not name:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_app_revision'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'app_name', 'name']
        path_param_values = self.encode_path_vars(project_id, app_name, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/apps/{app_name}/revisions/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def delete_app_revision(self, project_id: str, app_name: str, name: str, **kwargs) -> DetailedResponse:
        """
        Delete an application revision.

        Delete an application revision.

        :param str project_id: The ID of the project.
        :param str app_name: The name of your application.
        :param str name: The name of your application revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not app_name:
            raise ValueError('app_name must be provided')
        if not name:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='delete_app_revision'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'app_name', 'name']
        path_param_values = self.encode_path_vars(project_id, app_name, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/apps/{app_name}/revisions/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Jobs
    #########################

    def list_jobs(self, project_id: str, *, limit: int = None, start: str = None, **kwargs) -> DetailedResponse:
        """
        List jobs.

        List all jobs in a project.

        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of jobs per page.
        :param str start: (optional) An optional token that indicates the beginning
               of the page of results to be returned. If omitted, the first page of
               results is returned. This value is obtained from the 'start' query
               parameter in the 'next_url' field of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `JobList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='list_jobs'
        )
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'start': start,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/jobs'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers, params=params)

        response = self.send(request, **kwargs)
        return response

    def create_job(
        self,
        project_id: str,
        image_reference: str,
        name: str,
        *,
        image_secret: str = None,
        run_arguments: List[str] = None,
        run_as_user: int = None,
        run_commands: List[str] = None,
        run_env_variables: List['EnvVarPrototype'] = None,
        run_mode: str = None,
        run_service_account: str = None,
        run_volume_mounts: List['VolumeMountPrototype'] = None,
        scale_array_spec: str = None,
        scale_cpu_limit: str = None,
        scale_ephemeral_storage_limit: str = None,
        scale_max_execution_time: int = None,
        scale_memory_limit: str = None,
        scale_retry_limit: int = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a job.

        Create a job.

        :param str project_id: The ID of the project.
        :param str image_reference: The name of the image that is used for this
               job. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and
               `TAG` are optional. If `REGISTRY` is not specified, the default is
               `docker.io`. If `TAG` is not specified, the default is `latest`. If the
               image reference points to a registry that requires authentication, make
               sure to also specify the property `image_secret`.
        :param str name: The name of the job. Use a name that is unique within the
               project.
        :param str image_secret: (optional) The name of the image registry access
               secret. The image registry access secret is used to authenticate with a
               private registry when you download the container image. If the image
               reference points to a registry that requires authentication, the job / job
               runs will be created but submitted job runs will fail, until this property
               is provided, too.
        :param List[str] run_arguments: (optional) Set arguments for the job that
               are passed to start job run containers. If not specified an empty string
               array will be applied and the arguments specified by the container image,
               will be used to start the container.
        :param int run_as_user: (optional) The user ID (UID) to run the application
               (e.g., 1001).
        :param List[str] run_commands: (optional) Set commands for the job that are
               passed to start job run containers. If not specified an empty string array
               will be applied and the command specified by the container image, will be
               used to start the container.
        :param List[EnvVarPrototype] run_env_variables: (optional) Optional
               references to config maps, secrets or a literal values.
        :param str run_mode: (optional) The mode for runs of the job. Valid values
               are `task` and `daemon`. In `task` mode, the `max_execution_time` and
               `retry_limit` options apply. In `daemon` mode, since there is no timeout
               and failed instances are restarted indefinitely, the `max_execution_time`
               and `retry_limit` options are not allowed.
        :param str run_service_account: (optional) The name of the service account.
               For built-in service accounts, you can use the shortened names `manager`,
               `none`, `reader`, and `writer`.
        :param List[VolumeMountPrototype] run_volume_mounts: (optional) Optional
               mounts of config maps or a secrets.
        :param str scale_array_spec: (optional) Define a custom set of array
               indices as comma-separated list containing single values and
               hyphen-separated ranges like `5,12-14,23,27`. Each instance can pick up its
               array index via environment variable `JOB_INDEX`. The number of unique
               array indices specified here determines the number of job instances to run.
        :param str scale_cpu_limit: (optional) Optional amount of CPU set for the
               instance of the job. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
        :param str scale_ephemeral_storage_limit: (optional) Optional amount of
               ephemeral storage to set for the instance of the job. The amount specified
               as ephemeral storage, must not exceed the amount of `scale_memory_limit`.
               The units for specifying ephemeral storage are Megabyte (M) or Gigabyte
               (G), whereas G and M are the shorthand expressions for GB and MB. For more
               information see [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param int scale_max_execution_time: (optional) The maximum execution time
               in seconds for runs of the job. This option can only be specified if `mode`
               is `task`.
        :param str scale_memory_limit: (optional) Optional amount of memory set for
               the instance of the job. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
               The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G
               and M are the shorthand expressions for GB and MB. For more information see
               [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param int scale_retry_limit: (optional) The number of times to rerun an
               instance of the job before the job is marked as failed. This option can
               only be specified if `mode` is `task`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Job` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if image_reference is None:
            raise ValueError('image_reference must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if run_env_variables is not None:
            run_env_variables = [convert_model(x) for x in run_env_variables]
        if run_volume_mounts is not None:
            run_volume_mounts = [convert_model(x) for x in run_volume_mounts]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='create_job'
        )
        headers.update(sdk_headers)

        data = {
            'image_reference': image_reference,
            'name': name,
            'image_secret': image_secret,
            'run_arguments': run_arguments,
            'run_as_user': run_as_user,
            'run_commands': run_commands,
            'run_env_variables': run_env_variables,
            'run_mode': run_mode,
            'run_service_account': run_service_account,
            'run_volume_mounts': run_volume_mounts,
            'scale_array_spec': scale_array_spec,
            'scale_cpu_limit': scale_cpu_limit,
            'scale_ephemeral_storage_limit': scale_ephemeral_storage_limit,
            'scale_max_execution_time': scale_max_execution_time,
            'scale_memory_limit': scale_memory_limit,
            'scale_retry_limit': scale_retry_limit,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/jobs'.format(**path_param_dict)
        request = self.prepare_request(method='POST', url=url, headers=headers, data=data)

        response = self.send(request, **kwargs)
        return response

    def get_job(self, project_id: str, name: str, **kwargs) -> DetailedResponse:
        """
        Get a job.

        Display the details of a job.

        :param str project_id: The ID of the project.
        :param str name: The name of your job.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Job` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_job'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/jobs/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def delete_job(self, project_id: str, name: str, **kwargs) -> DetailedResponse:
        """
        Delete a job.

        Delete a job.

        :param str project_id: The ID of the project.
        :param str name: The name of your job.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='delete_job'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/jobs/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def update_job(self, project_id: str, name: str, if_match: str, job: 'JobPatch', **kwargs) -> DetailedResponse:
        """
        Update a job.

        Update the given job.

        :param str project_id: The ID of the project.
        :param str name: The name of your job.
        :param str if_match: Version of the job settings to be updated. Specify the
               version that you retrieved as entity_tag (ETag header) when reading the
               job. This value helps identifying parallel usage of this API. Pass * to
               indicate to update any version available. This might result in stale
               updates.
        :param JobPatch job: Job patch prototype.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Job` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        if not if_match:
            raise ValueError('if_match must be provided')
        if job is None:
            raise ValueError('job must be provided')
        if isinstance(job, JobPatch):
            job = convert_model(job)
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='update_job'
        )
        headers.update(sdk_headers)

        data = json.dumps(job)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/jobs/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH', url=url, headers=headers, data=data)

        response = self.send(request, **kwargs)
        return response

    def list_job_runs(
        self, project_id: str, *, job_name: str = None, limit: int = None, start: str = None, **kwargs
    ) -> DetailedResponse:
        """
        List job runs.

        List all job runs in a project.

        :param str project_id: The ID of the project.
        :param str job_name: (optional) Optional name of the job that should be
               filtered for.
        :param int limit: (optional) Optional maximum number of job runs per page.
        :param str start: (optional) An optional token that indicates the beginning
               of the page of results to be returned. If omitted, the first page of
               results is returned. This value is obtained from the 'start' query
               parameter in the 'next_url' field of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `JobRunList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='list_job_runs'
        )
        headers.update(sdk_headers)

        params = {
            'job_name': job_name,
            'limit': limit,
            'start': start,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/job_runs'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers, params=params)

        response = self.send(request, **kwargs)
        return response

    def create_job_run(
        self,
        project_id: str,
        *,
        image_reference: str = None,
        image_secret: str = None,
        job_name: str = None,
        name: str = None,
        run_arguments: List[str] = None,
        run_as_user: int = None,
        run_commands: List[str] = None,
        run_env_variables: List['EnvVarPrototype'] = None,
        run_mode: str = None,
        run_service_account: str = None,
        run_volume_mounts: List['VolumeMountPrototype'] = None,
        scale_array_spec: str = None,
        scale_cpu_limit: str = None,
        scale_ephemeral_storage_limit: str = None,
        scale_max_execution_time: int = None,
        scale_memory_limit: str = None,
        scale_retry_limit: int = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a job run.

        Create an job run.

        :param str project_id: The ID of the project.
        :param str image_reference: (optional) The name of the image that is used
               for this job. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where
               `REGISTRY` and `TAG` are optional. If `REGISTRY` is not specified, the
               default is `docker.io`. If `TAG` is not specified, the default is `latest`.
               If the image reference points to a registry that requires authentication,
               make sure to also specify the property `image_secret`.
        :param str image_secret: (optional) The name of the image registry access
               secret. The image registry access secret is used to authenticate with a
               private registry when you download the container image. If the image
               reference points to a registry that requires authentication, the job / job
               runs will be created but submitted job runs will fail, until this property
               is provided, too.
        :param str job_name: (optional) Optional name of the job on which this job
               run is based on. If specified, the job run will inherit the configuration
               of the referenced job.
        :param str name: (optional) The name of the job. Use a name that is unique
               within the project.
        :param List[str] run_arguments: (optional) Set arguments for the job that
               are passed to start job run containers. If not specified an empty string
               array will be applied and the arguments specified by the container image,
               will be used to start the container.
        :param int run_as_user: (optional) The user ID (UID) to run the application
               (e.g., 1001).
        :param List[str] run_commands: (optional) Set commands for the job that are
               passed to start job run containers. If not specified an empty string array
               will be applied and the command specified by the container image, will be
               used to start the container.
        :param List[EnvVarPrototype] run_env_variables: (optional) Optional
               references to config maps, secrets or a literal values.
        :param str run_mode: (optional) The mode for runs of the job. Valid values
               are `task` and `daemon`. In `task` mode, the `max_execution_time` and
               `retry_limit` options apply. In `daemon` mode, since there is no timeout
               and failed instances are restarted indefinitely, the `max_execution_time`
               and `retry_limit` options are not allowed.
        :param str run_service_account: (optional) The name of the service account.
               For built-in service accounts, you can use the shortened names `manager`,
               `none`, `reader`, and `writer`.
        :param List[VolumeMountPrototype] run_volume_mounts: (optional) Optional
               mounts of config maps or a secrets.
        :param str scale_array_spec: (optional) Define a custom set of array
               indices as comma-separated list containing single values and
               hyphen-separated ranges like `5,12-14,23,27`. Each instance can pick up its
               array index via environment variable `JOB_INDEX`. The number of unique
               array indices specified here determines the number of job instances to run.
        :param str scale_cpu_limit: (optional) Optional amount of CPU set for the
               instance of the job. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
        :param str scale_ephemeral_storage_limit: (optional) Optional amount of
               ephemeral storage to set for the instance of the job. The amount specified
               as ephemeral storage, must not exceed the amount of `scale_memory_limit`.
               The units for specifying ephemeral storage are Megabyte (M) or Gigabyte
               (G), whereas G and M are the shorthand expressions for GB and MB. For more
               information see [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param int scale_max_execution_time: (optional) The maximum execution time
               in seconds for runs of the job. This option can only be specified if `mode`
               is `task`.
        :param str scale_memory_limit: (optional) Optional amount of memory set for
               the instance of the job. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
               The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G
               and M are the shorthand expressions for GB and MB. For more information see
               [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param int scale_retry_limit: (optional) The number of times to rerun an
               instance of the job before the job is marked as failed. This option can
               only be specified if `mode` is `task`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `JobRun` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if run_env_variables is not None:
            run_env_variables = [convert_model(x) for x in run_env_variables]
        if run_volume_mounts is not None:
            run_volume_mounts = [convert_model(x) for x in run_volume_mounts]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='create_job_run'
        )
        headers.update(sdk_headers)

        data = {
            'image_reference': image_reference,
            'image_secret': image_secret,
            'job_name': job_name,
            'name': name,
            'run_arguments': run_arguments,
            'run_as_user': run_as_user,
            'run_commands': run_commands,
            'run_env_variables': run_env_variables,
            'run_mode': run_mode,
            'run_service_account': run_service_account,
            'run_volume_mounts': run_volume_mounts,
            'scale_array_spec': scale_array_spec,
            'scale_cpu_limit': scale_cpu_limit,
            'scale_ephemeral_storage_limit': scale_ephemeral_storage_limit,
            'scale_max_execution_time': scale_max_execution_time,
            'scale_memory_limit': scale_memory_limit,
            'scale_retry_limit': scale_retry_limit,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/job_runs'.format(**path_param_dict)
        request = self.prepare_request(method='POST', url=url, headers=headers, data=data)

        response = self.send(request, **kwargs)
        return response

    def get_job_run(self, project_id: str, name: str, **kwargs) -> DetailedResponse:
        """
        Get a job run.

        Display the details of a job run.

        :param str project_id: The ID of the project.
        :param str name: The name of your job run.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `JobRun` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_job_run'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/job_runs/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def delete_job_run(self, project_id: str, name: str, **kwargs) -> DetailedResponse:
        """
        Delete a job run.

        Delete a job run.

        :param str project_id: The ID of the project.
        :param str name: The name of your job run.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='delete_job_run'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/job_runs/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Builds
    #########################

    def list_builds(self, project_id: str, *, limit: int = None, start: str = None, **kwargs) -> DetailedResponse:
        """
        List builds.

        List all builds in a project.

        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of builds per page.
        :param str start: (optional) The token to continue traversing paginated
               list of builds.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BuildList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='list_builds'
        )
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'start': start,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/builds'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers, params=params)

        response = self.send(request, **kwargs)
        return response

    def create_build(
        self,
        project_id: str,
        name: str,
        output_image: str,
        output_secret: str,
        source_url: str,
        strategy_type: str,
        *,
        source_context_dir: str = None,
        source_revision: str = None,
        source_secret: str = None,
        source_type: str = None,
        strategy_size: str = None,
        strategy_spec_file: str = None,
        timeout: int = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a build.

        Create a build.

        :param str project_id: The ID of the project.
        :param str name: The name of the build. Use a name that is unique within
               the project.
        :param str output_image: The name of the image.
        :param str output_secret: The secret that is required to access the image
               registry. Make sure that the secret is granted with push permissions
               towards the specified container registry namespace.
        :param str source_url: The URL of the code repository. This field is
               required if the `source_type` is `git`. If the `source_type` value is
               `local`, this field must be omitted. If the repository is publicly
               available you can provide a 'https' URL like
               `https://github.com/IBM/CodeEngine`. If the repository requires
               authentication, you need to provide a 'ssh' URL like
               `git@github.com:IBM/CodeEngine.git` along with a `source_secret` that
               points to a secret of format `ssh_auth`.
        :param str strategy_type: The strategy to use for building the image.
        :param str source_context_dir: (optional) Option directory in the
               repository that contains the buildpacks file or the Dockerfile.
        :param str source_revision: (optional) Commit, tag, or branch in the source
               repository to pull. This field is optional if the `source_type` is `git`
               and uses the HEAD of default branch if not specified. If the `source_type`
               value is `local`, this field must be omitted.
        :param str source_secret: (optional) Name of the secret that is used access
               the repository source. This field is optional if the `source_type` is
               `git`. Additionally, if the `source_url` points to a repository that
               requires authentication, the build will be created but cannot access any
               source code, until this property is provided, too. If the `source_type`
               value is `local`, this field must be omitted.
        :param str source_type: (optional) Specifies the type of source to
               determine if your build source is in a repository or based on local source
               code.
               * local - For builds from local source code.
               * git - For builds from git version controlled source code.
        :param str strategy_size: (optional) Optional size for the build, which
               determines the amount of resources used. Build sizes are `small`, `medium`,
               `large`, `xlarge`.
        :param str strategy_spec_file: (optional) Optional path to the
               specification file that is used for build strategies for building an image.
        :param int timeout: (optional) The maximum amount of time, in seconds, that
               can pass before the build must succeed or fail.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Build` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if output_image is None:
            raise ValueError('output_image must be provided')
        if output_secret is None:
            raise ValueError('output_secret must be provided')
        if source_url is None:
            raise ValueError('source_url must be provided')
        if strategy_type is None:
            raise ValueError('strategy_type must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='create_build'
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'output_image': output_image,
            'output_secret': output_secret,
            'source_url': source_url,
            'strategy_type': strategy_type,
            'source_context_dir': source_context_dir,
            'source_revision': source_revision,
            'source_secret': source_secret,
            'source_type': source_type,
            'strategy_size': strategy_size,
            'strategy_spec_file': strategy_spec_file,
            'timeout': timeout,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/builds'.format(**path_param_dict)
        request = self.prepare_request(method='POST', url=url, headers=headers, data=data)

        response = self.send(request, **kwargs)
        return response

    def get_build(self, project_id: str, name: str, **kwargs) -> DetailedResponse:
        """
        Get a build.

        Display the details of a build.

        :param str project_id: The ID of the project.
        :param str name: The name of your build.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Build` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_build'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/builds/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def delete_build(self, project_id: str, name: str, **kwargs) -> DetailedResponse:
        """
        Delete a build.

        Delete a build.

        :param str project_id: The ID of the project.
        :param str name: The name of your build.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='delete_build'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/builds/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def update_build(
        self, project_id: str, name: str, if_match: str, build: 'BuildPatch', **kwargs
    ) -> DetailedResponse:
        """
        Update a build.

        Update a build.

        :param str project_id: The ID of the project.
        :param str name: The name of your build.
        :param str if_match: Version of the build settings to be updated. Specify
               the version that you retrieved as entity_tag (ETag header) when reading the
               build. This value helps identifying parallel usage of this API. Pass * to
               indicate to update any version available. This might result in stale
               updates.
        :param BuildPatch build: Build patch.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Build` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        if not if_match:
            raise ValueError('if_match must be provided')
        if build is None:
            raise ValueError('build must be provided')
        if isinstance(build, BuildPatch):
            build = convert_model(build)
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='update_build'
        )
        headers.update(sdk_headers)

        data = json.dumps(build)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/builds/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH', url=url, headers=headers, data=data)

        response = self.send(request, **kwargs)
        return response

    def list_build_runs(
        self, project_id: str, *, build_name: str = None, limit: int = None, start: str = None, **kwargs
    ) -> DetailedResponse:
        """
        List build runs.

        List all build runs in a project.

        :param str project_id: The ID of the project.
        :param str build_name: (optional) Optional name of the build that should be
               filtered for.
        :param int limit: (optional) Optional maximum number of build runs per
               page.
        :param str start: (optional) An optional token that indicates the beginning
               of the page of results to be returned. If omitted, the first page of
               results is returned. This value is obtained from the 'start' query
               parameter in the 'next_url' field of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BuildRunList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='list_build_runs'
        )
        headers.update(sdk_headers)

        params = {
            'build_name': build_name,
            'limit': limit,
            'start': start,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/build_runs'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers, params=params)

        response = self.send(request, **kwargs)
        return response

    def create_build_run(
        self,
        project_id: str,
        *,
        build_name: str = None,
        name: str = None,
        output_image: str = None,
        output_secret: str = None,
        service_account: str = None,
        source_context_dir: str = None,
        source_revision: str = None,
        source_secret: str = None,
        source_type: str = None,
        source_url: str = None,
        strategy_size: str = None,
        strategy_spec_file: str = None,
        strategy_type: str = None,
        timeout: int = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a build run.

        Create a build run.

        :param str project_id: The ID of the project.
        :param str build_name: (optional) Optional name of the build on which this
               build run is based on. If specified, the build run will inherit the
               configuration of the referenced build. If not specified, make sure to
               specify at least the fields `strategy_type`, `source_url`, `output_image`
               and `output_secret` to describe the build run.
        :param str name: (optional) Name of the build run. This field is optional,
               if the field `build_name` is specified and its value will be generated like
               so: `[BUILD_NAME]-run-[timestamp with format: YYMMDD-hhmmss] if not set.`.
        :param str output_image: (optional) The name of the image.
        :param str output_secret: (optional) The secret that is required to access
               the image registry. Make sure that the secret is granted with push
               permissions towards the specified container registry namespace.
        :param str service_account: (optional) Optional service account which is
               used for resource control.
        :param str source_context_dir: (optional) Option directory in the
               repository that contains the buildpacks file or the Dockerfile.
        :param str source_revision: (optional) Commit, tag, or branch in the source
               repository to pull. This field is optional if the `source_type` is `git`
               and uses the HEAD of default branch if not specified. If the `source_type`
               value is `local`, this field must be omitted.
        :param str source_secret: (optional) Name of the secret that is used access
               the repository source. This field is optional if the `source_type` is
               `git`. Additionally, if the `source_url` points to a repository that
               requires authentication, the build will be created but cannot access any
               source code, until this property is provided, too. If the `source_type`
               value is `local`, this field must be omitted.
        :param str source_type: (optional) Specifies the type of source to
               determine if your build source is in a repository or based on local source
               code.
               * local - For builds from local source code.
               * git - For builds from git version controlled source code.
        :param str source_url: (optional) The URL of the code repository. This
               field is required if the `source_type` is `git`. If the `source_type` value
               is `local`, this field must be omitted. If the repository is publicly
               available you can provide a 'https' URL like
               `https://github.com/IBM/CodeEngine`. If the repository requires
               authentication, you need to provide a 'ssh' URL like
               `git@github.com:IBM/CodeEngine.git` along with a `source_secret` that
               points to a secret of format `ssh_auth`.
        :param str strategy_size: (optional) Optional size for the build, which
               determines the amount of resources used. Build sizes are `small`, `medium`,
               `large`, `xlarge`.
        :param str strategy_spec_file: (optional) Optional path to the
               specification file that is used for build strategies for building an image.
        :param str strategy_type: (optional) The strategy to use for building the
               image.
        :param int timeout: (optional) The maximum amount of time, in seconds, that
               can pass before the build must succeed or fail.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BuildRun` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='create_build_run'
        )
        headers.update(sdk_headers)

        data = {
            'build_name': build_name,
            'name': name,
            'output_image': output_image,
            'output_secret': output_secret,
            'service_account': service_account,
            'source_context_dir': source_context_dir,
            'source_revision': source_revision,
            'source_secret': source_secret,
            'source_type': source_type,
            'source_url': source_url,
            'strategy_size': strategy_size,
            'strategy_spec_file': strategy_spec_file,
            'strategy_type': strategy_type,
            'timeout': timeout,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/build_runs'.format(**path_param_dict)
        request = self.prepare_request(method='POST', url=url, headers=headers, data=data)

        response = self.send(request, **kwargs)
        return response

    def get_build_run(self, project_id: str, name: str, **kwargs) -> DetailedResponse:
        """
        Get a build run.

        Display the details of a build run.

        :param str project_id: The ID of the project.
        :param str name: The name of your build run.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BuildRun` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_build_run'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/build_runs/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def delete_build_run(self, project_id: str, name: str, **kwargs) -> DetailedResponse:
        """
        Delete a build run.

        Delete a build run.

        :param str project_id: The ID of the project.
        :param str name: The name of your build run.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='delete_build_run'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/build_runs/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Secrets and config maps
    #########################

    def list_config_maps(self, project_id: str, *, limit: int = None, start: str = None, **kwargs) -> DetailedResponse:
        """
        List config maps.

        List all config maps in a project.

        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of config maps per
               page.
        :param str start: (optional) An optional token that indicates the beginning
               of the page of results to be returned. If omitted, the first page of
               results is returned. This value is obtained from the 'start' query
               parameter in the 'next_url' field of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ConfigMapList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='list_config_maps'
        )
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'start': start,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/config_maps'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers, params=params)

        response = self.send(request, **kwargs)
        return response

    def create_config_map(self, project_id: str, name: str, *, data: dict = None, **kwargs) -> DetailedResponse:
        """
        Create a config map.

        Create a config map.

        :param str project_id: The ID of the project.
        :param str name: The name of the configmap. Use a name that is unique
               within the project.
        :param dict data: (optional) The key-value pair for the config map. Values
               must be specified in `KEY=VALUE` format. Each `KEY` field must consist of
               alphanumeric characters, `-`, `_` or `.` and must not be exceed a max
               length of 253 characters. Each `VALUE` field can consists of any character
               and must not be exceed a max length of 1048576 characters.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ConfigMap` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='create_config_map'
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'data': data,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/config_maps'.format(**path_param_dict)
        request = self.prepare_request(method='POST', url=url, headers=headers, data=data)

        response = self.send(request, **kwargs)
        return response

    def get_config_map(self, project_id: str, name: str, **kwargs) -> DetailedResponse:
        """
        Get a config map.

        Display the details of a config map.

        :param str project_id: The ID of the project.
        :param str name: The name of your configmap.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ConfigMap` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_config_map'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/config_maps/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def replace_config_map(
        self, project_id: str, name: str, if_match: str, *, data: dict = None, **kwargs
    ) -> DetailedResponse:
        """
        Update a config map.

        Update a config map.

        :param str project_id: The ID of the project.
        :param str name: The name of your configmap.
        :param str if_match: Version of the config map settings to be updated.
               Specify the version that you retrieved as entity_tag (ETag header) when
               reading the config map. This value helps identifying parallel usage of this
               API. Pass * to indicate to update any version available. This might result
               in stale updates.
        :param dict data: (optional) The key-value pair for the config map. Values
               must be specified in `KEY=VALUE` format. Each `KEY` field must consist of
               alphanumeric characters, `-`, `_` or `.` and must not be exceed a max
               length of 253 characters. Each `VALUE` field can consists of any character
               and must not be exceed a max length of 1048576 characters.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ConfigMap` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        if not if_match:
            raise ValueError('if_match must be provided')
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='replace_config_map'
        )
        headers.update(sdk_headers)

        data = {
            'data': data,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/config_maps/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT', url=url, headers=headers, data=data)

        response = self.send(request, **kwargs)
        return response

    def delete_config_map(self, project_id: str, name: str, **kwargs) -> DetailedResponse:
        """
        Delete a config map.

        Delete a config map.

        :param str project_id: The ID of the project.
        :param str name: The name of your configmap.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='delete_config_map'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/config_maps/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def list_secrets(self, project_id: str, *, limit: int = None, start: str = None, **kwargs) -> DetailedResponse:
        """
        List secrets.

        List all secrets in a project.

        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of secrets per page.
        :param str start: (optional) An optional token that indicates the beginning
               of the page of results to be returned. If omitted, the first page of
               results is returned. This value is obtained from the 'start' query
               parameter in the 'next_url' field of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SecretList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='list_secrets'
        )
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'start': start,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/secrets'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers, params=params)

        response = self.send(request, **kwargs)
        return response

    def create_secret(
        self, project_id: str, format: str, name: str, *, data: dict = None, **kwargs
    ) -> DetailedResponse:
        """
        Create a secret.

        Create a secret.

        :param str project_id: The ID of the project.
        :param str format: Specify the format of the secret.
        :param str name: The name of the secret.
        :param dict data: (optional) Data container that allows to specify config
               parameters and their values as a key-value map. Each key field must consist
               of alphanumeric characters, `-`, `_` or `.` and must not be exceed a max
               length of 253 characters. Each value field can consists of any character
               and must not be exceed a max length of 1048576 characters.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Secret` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if format is None:
            raise ValueError('format must be provided')
        if name is None:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='create_secret'
        )
        headers.update(sdk_headers)

        data = {
            'format': format,
            'name': name,
            'data': data,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/secrets'.format(**path_param_dict)
        request = self.prepare_request(method='POST', url=url, headers=headers, data=data)

        response = self.send(request, **kwargs)
        return response

    def get_secret(self, project_id: str, name: str, **kwargs) -> DetailedResponse:
        """
        Get a secret.

        Get a secret.

        :param str project_id: The ID of the project.
        :param str name: The name of your secret.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Secret` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_secret'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/secrets/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def replace_secret(
        self, project_id: str, name: str, if_match: str, *, data: dict = None, format: str = None, **kwargs
    ) -> DetailedResponse:
        """
        Update a secret.

        Update a secret.

        :param str project_id: The ID of the project.
        :param str name: The name of your secret.
        :param str if_match: Version of the secret settings to be updated. Specify
               the version that you retrieved as entity_tag (ETag header) when reading the
               secret. This value helps identifying parallel usage of this API. Pass * to
               indicate to update any version available. This might result in stale
               updates.
        :param dict data: (optional) Data container that allows to specify config
               parameters and their values as a key-value map. Each key field must consist
               of alphanumeric characters, `-`, `_` or `.` and must not be exceed a max
               length of 253 characters. Each value field can consists of any character
               and must not be exceed a max length of 1048576 characters.
        :param str format: (optional) Specify the format of the secret.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Secret` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        if not if_match:
            raise ValueError('if_match must be provided')
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='replace_secret'
        )
        headers.update(sdk_headers)

        data = {
            'data': data,
            'format': format,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/secrets/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT', url=url, headers=headers, data=data)

        response = self.send(request, **kwargs)
        return response

    def delete_secret(self, project_id: str, name: str, **kwargs) -> DetailedResponse:
        """
        Delete a secret.

        Delete a secret.

        :param str project_id: The ID of the project.
        :param str name: The name of your secret.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='delete_secret'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/secrets/{name}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class App:
    """
    App is the response model for app resources.

    :attr str created_at: The date when the resource was created.
    :attr str endpoint: (optional) Optional URL to invoke app. Depending on
          visibility this is accessible publicly ot in the private network only. Empty in
          case 'managed_domain_mappings' is set to 'local'.
    :attr str endpoint_internal: (optional) URL to app that is only visible within
          the project.
    :attr str entity_tag: The version of the job instance, which is used to achieve
          optimistic locking.
    :attr str href: When you provision a new app,  a URL is created identifying the
          location of the instance.
    :attr str id: The identifier of the resource.
    :attr int image_port: (optional) Optional port the app listens on. While the app
          will always be exposed via port `443` for end users, this port is used to
          connect to the port that is exposed by the container image.
    :attr str image_reference: The name of the image that is used for this job. The
          format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and `TAG` are
          optional. If `REGISTRY` is not specified, the default is `docker.io`. If `TAG`
          is not specified, the default is `latest`. If the image reference points to a
          registry that requires authentication, make sure to also specify the property
          `image_secret`.
    :attr str image_secret: (optional) Optional name of the image registry access
          secret. The image registry access secret is used to authenticate with a private
          registry when you download the container image. If the image reference points to
          a registry that requires authentication, the app will be created but cannot
          reach the ready status, until this property is provided, too.
    :attr str managed_domain_mappings: Optional value controlling which of the
          system managed domain mappings will be setup for the application. Valid values
          are 'local_public', 'local_private' and 'local'. Visibility can only be
          'local_private' if the project supports application private visibility.
    :attr str name: The name of the app.
    :attr str project_id: The ID of the project the resource is located in.
    :attr str resource_type: The type of the app.
    :attr List[str] run_arguments: Optional arguments for the app that are passed to
          start the container. If not specified an empty string array will be applied and
          the arguments specified by the container image, will be used to start the
          container.
    :attr int run_as_user: (optional) Optional user ID (UID) to run the app (e.g.,
          `1001`).
    :attr List[str] run_commands: Optional commands for the app that are passed to
          start the container. If not specified an empty string array will be applied and
          the command specified by the container image, will be used to start the
          container.
    :attr List[EnvVar] run_env_variables: References to config maps, secrets or a
          literal values, which are exposed as environment variables in the application.
    :attr str run_service_account: (optional) Optional name of the service account.
          For built-in service accounts, you can use the shortened names `manager` ,
          `none`, `reader`, and `writer`.
    :attr List[VolumeMount] run_volume_mounts: Mounts of config maps or secrets.
    :attr int scale_concurrency: (optional) Optional maximum number of requests that
          can be processed concurrently per instance.
    :attr int scale_concurrency_target: (optional) Optional threshold of concurrent
          requests per instance at which one or more additional instances are created. Use
          this value to scale up instances based on concurrent number of requests. This
          option defaults to the value of the `scale_concurrency` option, if not
          specified.
    :attr str scale_cpu_limit: Optional number of CPU set for the instance of the
          app. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
    :attr str scale_ephemeral_storage_limit: Optional amount of ephemeral storage to
          set for the instance of the app. The amount specified as ephemeral storage, must
          not exceed the amount of `scale_memory_limit`. The units for specifying
          ephemeral storage are Megabyte (M) or Gigabyte (G), whereas G and M are the
          shorthand expressions for GB and MB. For more information see [Units of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :attr int scale_initial_instances: (optional) Optional initial number of
          instances that are created upon app creation or app update.
    :attr int scale_max_instances: Optional maximum number of instances for this
          app. If you set this value to `0`, this property does not set a upper scaling
          limit. However, the app scaling is still limited by the project quota for
          instances. See [Limits and quotas for Code
          Engine](https://cloud.ibm.com/docs/codeengine?topic=codeengine-limits).
    :attr str scale_memory_limit: Optional amount of memory set for the instance of
          the app. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
          The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and
          M are the shorthand expressions for GB and MB. For more information see [Units
          of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :attr int scale_min_instances: Optional minimum number of instances for this
          app. If you set this value to `0`, the app will scale down to zero, if not hit
          by any request for some time.
    :attr int scale_request_timeout: Optional amount of time in seconds that is
          allowed for a running app to respond to a request.
    :attr str status: The current status of the app.
    :attr AppStatus status_details: (optional) The detailed status of the
          application.
    """

    def __init__(
        self,
        created_at: str,
        entity_tag: str,
        href: str,
        id: str,
        image_reference: str,
        managed_domain_mappings: str,
        name: str,
        project_id: str,
        resource_type: str,
        run_arguments: List[str],
        run_commands: List[str],
        run_env_variables: List['EnvVar'],
        run_volume_mounts: List['VolumeMount'],
        scale_cpu_limit: str,
        scale_ephemeral_storage_limit: str,
        scale_max_instances: int,
        scale_memory_limit: str,
        scale_min_instances: int,
        scale_request_timeout: int,
        status: str,
        *,
        endpoint: str = None,
        endpoint_internal: str = None,
        image_port: int = None,
        image_secret: str = None,
        run_as_user: int = None,
        run_service_account: str = None,
        scale_concurrency: int = None,
        scale_concurrency_target: int = None,
        scale_initial_instances: int = None,
        status_details: 'AppStatus' = None,
    ) -> None:
        """
        Initialize a App object.

        :param str created_at: The date when the resource was created.
        :param str entity_tag: The version of the job instance, which is used to
               achieve optimistic locking.
        :param str href: When you provision a new app,  a URL is created
               identifying the location of the instance.
        :param str id: The identifier of the resource.
        :param str image_reference: The name of the image that is used for this
               job. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and
               `TAG` are optional. If `REGISTRY` is not specified, the default is
               `docker.io`. If `TAG` is not specified, the default is `latest`. If the
               image reference points to a registry that requires authentication, make
               sure to also specify the property `image_secret`.
        :param str managed_domain_mappings: Optional value controlling which of the
               system managed domain mappings will be setup for the application. Valid
               values are 'local_public', 'local_private' and 'local'. Visibility can only
               be 'local_private' if the project supports application private visibility.
        :param str name: The name of the app.
        :param str project_id: The ID of the project the resource is located in.
        :param str resource_type: The type of the app.
        :param List[str] run_arguments: Optional arguments for the app that are
               passed to start the container. If not specified an empty string array will
               be applied and the arguments specified by the container image, will be used
               to start the container.
        :param List[str] run_commands: Optional commands for the app that are
               passed to start the container. If not specified an empty string array will
               be applied and the command specified by the container image, will be used
               to start the container.
        :param List[EnvVar] run_env_variables: References to config maps, secrets
               or a literal values, which are exposed as environment variables in the
               application.
        :param List[VolumeMount] run_volume_mounts: Mounts of config maps or
               secrets.
        :param str scale_cpu_limit: Optional number of CPU set for the instance of
               the app. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
        :param str scale_ephemeral_storage_limit: Optional amount of ephemeral
               storage to set for the instance of the app. The amount specified as
               ephemeral storage, must not exceed the amount of `scale_memory_limit`. The
               units for specifying ephemeral storage are Megabyte (M) or Gigabyte (G),
               whereas G and M are the shorthand expressions for GB and MB. For more
               information see [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param int scale_max_instances: Optional maximum number of instances for
               this app. If you set this value to `0`, this property does not set a upper
               scaling limit. However, the app scaling is still limited by the project
               quota for instances. See [Limits and quotas for Code
               Engine](https://cloud.ibm.com/docs/codeengine?topic=codeengine-limits).
        :param str scale_memory_limit: Optional amount of memory set for the
               instance of the app. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
               The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G
               and M are the shorthand expressions for GB and MB. For more information see
               [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param int scale_min_instances: Optional minimum number of instances for
               this app. If you set this value to `0`, the app will scale down to zero, if
               not hit by any request for some time.
        :param int scale_request_timeout: Optional amount of time in seconds that
               is allowed for a running app to respond to a request.
        :param str status: The current status of the app.
        :param str endpoint: (optional) Optional URL to invoke app. Depending on
               visibility this is accessible publicly ot in the private network only.
               Empty in case 'managed_domain_mappings' is set to 'local'.
        :param str endpoint_internal: (optional) URL to app that is only visible
               within the project.
        :param int image_port: (optional) Optional port the app listens on. While
               the app will always be exposed via port `443` for end users, this port is
               used to connect to the port that is exposed by the container image.
        :param str image_secret: (optional) Optional name of the image registry
               access secret. The image registry access secret is used to authenticate
               with a private registry when you download the container image. If the image
               reference points to a registry that requires authentication, the app will
               be created but cannot reach the ready status, until this property is
               provided, too.
        :param int run_as_user: (optional) Optional user ID (UID) to run the app
               (e.g., `1001`).
        :param str run_service_account: (optional) Optional name of the service
               account. For built-in service accounts, you can use the shortened names
               `manager` , `none`, `reader`, and `writer`.
        :param int scale_concurrency: (optional) Optional maximum number of
               requests that can be processed concurrently per instance.
        :param int scale_concurrency_target: (optional) Optional threshold of
               concurrent requests per instance at which one or more additional instances
               are created. Use this value to scale up instances based on concurrent
               number of requests. This option defaults to the value of the
               `scale_concurrency` option, if not specified.
        :param int scale_initial_instances: (optional) Optional initial number of
               instances that are created upon app creation or app update.
        :param AppStatus status_details: (optional) The detailed status of the
               application.
        """
        self.created_at = created_at
        self.endpoint = endpoint
        self.endpoint_internal = endpoint_internal
        self.entity_tag = entity_tag
        self.href = href
        self.id = id
        self.image_port = image_port
        self.image_reference = image_reference
        self.image_secret = image_secret
        self.managed_domain_mappings = managed_domain_mappings
        self.name = name
        self.project_id = project_id
        self.resource_type = resource_type
        self.run_arguments = run_arguments
        self.run_as_user = run_as_user
        self.run_commands = run_commands
        self.run_env_variables = run_env_variables
        self.run_service_account = run_service_account
        self.run_volume_mounts = run_volume_mounts
        self.scale_concurrency = scale_concurrency
        self.scale_concurrency_target = scale_concurrency_target
        self.scale_cpu_limit = scale_cpu_limit
        self.scale_ephemeral_storage_limit = scale_ephemeral_storage_limit
        self.scale_initial_instances = scale_initial_instances
        self.scale_max_instances = scale_max_instances
        self.scale_memory_limit = scale_memory_limit
        self.scale_min_instances = scale_min_instances
        self.scale_request_timeout = scale_request_timeout
        self.status = status
        self.status_details = status_details

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'App':
        """Initialize a App object from a json dictionary."""
        args = {}
        if 'created_at' in _dict:
            args['created_at'] = _dict.get('created_at')
        else:
            raise ValueError('Required property \'created_at\' not present in App JSON')
        if 'endpoint' in _dict:
            args['endpoint'] = _dict.get('endpoint')
        if 'endpoint_internal' in _dict:
            args['endpoint_internal'] = _dict.get('endpoint_internal')
        if 'entity_tag' in _dict:
            args['entity_tag'] = _dict.get('entity_tag')
        else:
            raise ValueError('Required property \'entity_tag\' not present in App JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in App JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in App JSON')
        if 'image_port' in _dict:
            args['image_port'] = _dict.get('image_port')
        if 'image_reference' in _dict:
            args['image_reference'] = _dict.get('image_reference')
        else:
            raise ValueError('Required property \'image_reference\' not present in App JSON')
        if 'image_secret' in _dict:
            args['image_secret'] = _dict.get('image_secret')
        if 'managed_domain_mappings' in _dict:
            args['managed_domain_mappings'] = _dict.get('managed_domain_mappings')
        else:
            raise ValueError('Required property \'managed_domain_mappings\' not present in App JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in App JSON')
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        else:
            raise ValueError('Required property \'project_id\' not present in App JSON')
        if 'resource_type' in _dict:
            args['resource_type'] = _dict.get('resource_type')
        else:
            raise ValueError('Required property \'resource_type\' not present in App JSON')
        if 'run_arguments' in _dict:
            args['run_arguments'] = _dict.get('run_arguments')
        else:
            raise ValueError('Required property \'run_arguments\' not present in App JSON')
        if 'run_as_user' in _dict:
            args['run_as_user'] = _dict.get('run_as_user')
        if 'run_commands' in _dict:
            args['run_commands'] = _dict.get('run_commands')
        else:
            raise ValueError('Required property \'run_commands\' not present in App JSON')
        if 'run_env_variables' in _dict:
            args['run_env_variables'] = [EnvVar.from_dict(v) for v in _dict.get('run_env_variables')]
        else:
            raise ValueError('Required property \'run_env_variables\' not present in App JSON')
        if 'run_service_account' in _dict:
            args['run_service_account'] = _dict.get('run_service_account')
        if 'run_volume_mounts' in _dict:
            args['run_volume_mounts'] = [VolumeMount.from_dict(v) for v in _dict.get('run_volume_mounts')]
        else:
            raise ValueError('Required property \'run_volume_mounts\' not present in App JSON')
        if 'scale_concurrency' in _dict:
            args['scale_concurrency'] = _dict.get('scale_concurrency')
        if 'scale_concurrency_target' in _dict:
            args['scale_concurrency_target'] = _dict.get('scale_concurrency_target')
        if 'scale_cpu_limit' in _dict:
            args['scale_cpu_limit'] = _dict.get('scale_cpu_limit')
        else:
            raise ValueError('Required property \'scale_cpu_limit\' not present in App JSON')
        if 'scale_ephemeral_storage_limit' in _dict:
            args['scale_ephemeral_storage_limit'] = _dict.get('scale_ephemeral_storage_limit')
        else:
            raise ValueError('Required property \'scale_ephemeral_storage_limit\' not present in App JSON')
        if 'scale_initial_instances' in _dict:
            args['scale_initial_instances'] = _dict.get('scale_initial_instances')
        if 'scale_max_instances' in _dict:
            args['scale_max_instances'] = _dict.get('scale_max_instances')
        else:
            raise ValueError('Required property \'scale_max_instances\' not present in App JSON')
        if 'scale_memory_limit' in _dict:
            args['scale_memory_limit'] = _dict.get('scale_memory_limit')
        else:
            raise ValueError('Required property \'scale_memory_limit\' not present in App JSON')
        if 'scale_min_instances' in _dict:
            args['scale_min_instances'] = _dict.get('scale_min_instances')
        else:
            raise ValueError('Required property \'scale_min_instances\' not present in App JSON')
        if 'scale_request_timeout' in _dict:
            args['scale_request_timeout'] = _dict.get('scale_request_timeout')
        else:
            raise ValueError('Required property \'scale_request_timeout\' not present in App JSON')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in App JSON')
        if 'status_details' in _dict:
            args['status_details'] = AppStatus.from_dict(_dict.get('status_details'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a App object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = self.created_at
        if hasattr(self, 'endpoint') and self.endpoint is not None:
            _dict['endpoint'] = self.endpoint
        if hasattr(self, 'endpoint_internal') and self.endpoint_internal is not None:
            _dict['endpoint_internal'] = self.endpoint_internal
        if hasattr(self, 'entity_tag') and self.entity_tag is not None:
            _dict['entity_tag'] = self.entity_tag
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'image_port') and self.image_port is not None:
            _dict['image_port'] = self.image_port
        if hasattr(self, 'image_reference') and self.image_reference is not None:
            _dict['image_reference'] = self.image_reference
        if hasattr(self, 'image_secret') and self.image_secret is not None:
            _dict['image_secret'] = self.image_secret
        if hasattr(self, 'managed_domain_mappings') and self.managed_domain_mappings is not None:
            _dict['managed_domain_mappings'] = self.managed_domain_mappings
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'project_id') and self.project_id is not None:
            _dict['project_id'] = self.project_id
        if hasattr(self, 'resource_type') and self.resource_type is not None:
            _dict['resource_type'] = self.resource_type
        if hasattr(self, 'run_arguments') and self.run_arguments is not None:
            _dict['run_arguments'] = self.run_arguments
        if hasattr(self, 'run_as_user') and self.run_as_user is not None:
            _dict['run_as_user'] = self.run_as_user
        if hasattr(self, 'run_commands') and self.run_commands is not None:
            _dict['run_commands'] = self.run_commands
        if hasattr(self, 'run_env_variables') and self.run_env_variables is not None:
            run_env_variables_list = []
            for v in self.run_env_variables:
                if isinstance(v, dict):
                    run_env_variables_list.append(v)
                else:
                    run_env_variables_list.append(v.to_dict())
            _dict['run_env_variables'] = run_env_variables_list
        if hasattr(self, 'run_service_account') and self.run_service_account is not None:
            _dict['run_service_account'] = self.run_service_account
        if hasattr(self, 'run_volume_mounts') and self.run_volume_mounts is not None:
            run_volume_mounts_list = []
            for v in self.run_volume_mounts:
                if isinstance(v, dict):
                    run_volume_mounts_list.append(v)
                else:
                    run_volume_mounts_list.append(v.to_dict())
            _dict['run_volume_mounts'] = run_volume_mounts_list
        if hasattr(self, 'scale_concurrency') and self.scale_concurrency is not None:
            _dict['scale_concurrency'] = self.scale_concurrency
        if hasattr(self, 'scale_concurrency_target') and self.scale_concurrency_target is not None:
            _dict['scale_concurrency_target'] = self.scale_concurrency_target
        if hasattr(self, 'scale_cpu_limit') and self.scale_cpu_limit is not None:
            _dict['scale_cpu_limit'] = self.scale_cpu_limit
        if hasattr(self, 'scale_ephemeral_storage_limit') and self.scale_ephemeral_storage_limit is not None:
            _dict['scale_ephemeral_storage_limit'] = self.scale_ephemeral_storage_limit
        if hasattr(self, 'scale_initial_instances') and self.scale_initial_instances is not None:
            _dict['scale_initial_instances'] = self.scale_initial_instances
        if hasattr(self, 'scale_max_instances') and self.scale_max_instances is not None:
            _dict['scale_max_instances'] = self.scale_max_instances
        if hasattr(self, 'scale_memory_limit') and self.scale_memory_limit is not None:
            _dict['scale_memory_limit'] = self.scale_memory_limit
        if hasattr(self, 'scale_min_instances') and self.scale_min_instances is not None:
            _dict['scale_min_instances'] = self.scale_min_instances
        if hasattr(self, 'scale_request_timeout') and self.scale_request_timeout is not None:
            _dict['scale_request_timeout'] = self.scale_request_timeout
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'status_details') and self.status_details is not None:
            if isinstance(self.status_details, dict):
                _dict['status_details'] = self.status_details
            else:
                _dict['status_details'] = self.status_details.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this App object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'App') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'App') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ManagedDomainMappingsEnum(str, Enum):
        """
        Optional value controlling which of the system managed domain mappings will be
        setup for the application. Valid values are 'local_public', 'local_private' and
        'local'. Visibility can only be 'local_private' if the project supports
        application private visibility.
        """

        LOCAL = 'local'
        LOCAL_PRIVATE = 'local_private'
        LOCAL_PUBLIC = 'local_public'

    class ResourceTypeEnum(str, Enum):
        """
        The type of the app.
        """

        APP_V2 = 'app_v2'

    class RunServiceAccountEnum(str, Enum):
        """
        Optional name of the service account. For built-in service accounts, you can use
        the shortened names `manager` , `none`, `reader`, and `writer`.
        """

        DEFAULT = 'default'
        MANAGER = 'manager'
        READER = 'reader'
        WRITER = 'writer'
        NONE = 'none'

    class StatusEnum(str, Enum):
        """
        The current status of the app.
        """

        READY = 'ready'
        DEPLOYING = 'deploying'
        FAILED = 'failed'
        WARNING = 'warning'


class AppList:
    """
    Contains a list of apps and pagination information.

    :attr List[App] apps: List of all apps.
    :attr ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :attr int limit: Maximum number of resources per page.
    :attr ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    """

    def __init__(
        self, apps: List['App'], limit: int, *, first: 'ListFirstMetadata' = None, next: 'ListNextMetadata' = None
    ) -> None:
        """
        Initialize a AppList object.

        :param List[App] apps: List of all apps.
        :param int limit: Maximum number of resources per page.
        :param ListFirstMetadata first: (optional) Describes properties needed to
               retrieve the first page of a result list.
        :param ListNextMetadata next: (optional) Describes properties needed to
               retrieve the next page of a result list.
        """
        self.apps = apps
        self.first = first
        self.limit = limit
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AppList':
        """Initialize a AppList object from a json dictionary."""
        args = {}
        if 'apps' in _dict:
            args['apps'] = [App.from_dict(v) for v in _dict.get('apps')]
        else:
            raise ValueError('Required property \'apps\' not present in AppList JSON')
        if 'first' in _dict:
            args['first'] = ListFirstMetadata.from_dict(_dict.get('first'))
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in AppList JSON')
        if 'next' in _dict:
            args['next'] = ListNextMetadata.from_dict(_dict.get('next'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AppList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'apps') and self.apps is not None:
            apps_list = []
            for v in self.apps:
                if isinstance(v, dict):
                    apps_list.append(v)
                else:
                    apps_list.append(v.to_dict())
            _dict['apps'] = apps_list
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AppList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AppList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AppList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AppPatch:
    """
    App is the request model for app update operations.

    :attr int image_port: (optional) Optional port the app listens on. While the app
          will always be exposed via port `443` for end users, this port is used to
          connect to the port that is exposed by the container image.
    :attr str image_reference: (optional) The name of the image that is used for
          this job. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and
          `TAG` are optional. If `REGISTRY` is not specified, the default is `docker.io`.
          If `TAG` is not specified, the default is `latest`. If the image reference
          points to a registry that requires authentication, make sure to also specify the
          property `image_secret`.
    :attr str image_secret: (optional) Optional name of the image registry access
          secret. The image registry access secret is used to authenticate with a private
          registry when you download the container image. If the image reference points to
          a registry that requires authentication, the app will be created but cannot
          reach the ready status, until this property is provided, too.
    :attr str managed_domain_mappings: (optional) Optional value controlling which
          of the system managed domain mappings will be setup for the application. Valid
          values are 'local_public', 'local_private' and 'local'. Visibility can only be
          'local_private' if the project supports application private visibility.
    :attr List[str] run_arguments: (optional) Optional arguments for the app that
          are passed to start the container. If not specified an empty string array will
          be applied and the arguments specified by the container image, will be used to
          start the container.
    :attr int run_as_user: (optional) Optional user ID (UID) to run the app (e.g.,
          `1001`).
    :attr List[str] run_commands: (optional) Optional commands for the app that are
          passed to start the container. If not specified an empty string array will be
          applied and the command specified by the container image, will be used to start
          the container.
    :attr List[EnvVarPrototype] run_env_variables: (optional) Optional references to
          config maps, secrets or a literal values.
    :attr str run_service_account: (optional) Optional name of the service account.
          For built-in service accounts, you can use the shortened names `manager` ,
          `none`, `reader`, and `writer`.
    :attr List[VolumeMountPrototype] run_volume_mounts: (optional) Optional mounts
          of config maps or a secrets. In case this is provided, existing
          `run_volume_mounts` will be overwritten.
    :attr int scale_concurrency: (optional) Optional maximum number of requests that
          can be processed concurrently per instance.
    :attr int scale_concurrency_target: (optional) Optional threshold of concurrent
          requests per instance at which one or more additional instances are created. Use
          this value to scale up instances based on concurrent number of requests. This
          option defaults to the value of the `scale_concurrency` option, if not
          specified.
    :attr str scale_cpu_limit: (optional) Optional number of CPU set for the
          instance of the app. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
    :attr str scale_ephemeral_storage_limit: (optional) Optional amount of ephemeral
          storage to set for the instance of the app. The amount specified as ephemeral
          storage, must not exceed the amount of `scale_memory_limit`. The units for
          specifying ephemeral storage are Megabyte (M) or Gigabyte (G), whereas G and M
          are the shorthand expressions for GB and MB. For more information see [Units of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :attr int scale_initial_instances: (optional) Optional initial number of
          instances that are created upon app creation or app update.
    :attr int scale_max_instances: (optional) Optional maximum number of instances
          for this app. If you set this value to `0`, this property does not set a upper
          scaling limit. However, the app scaling is still limited by the project quota
          for instances. See [Limits and quotas for Code
          Engine](https://cloud.ibm.com/docs/codeengine?topic=codeengine-limits).
    :attr str scale_memory_limit: (optional) Optional amount of memory set for the
          instance of the app. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
          The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and
          M are the shorthand expressions for GB and MB. For more information see [Units
          of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :attr int scale_min_instances: (optional) Optional minimum number of instances
          for this app. If you set this value to `0`, the app will scale down to zero, if
          not hit by any request for some time.
    :attr int scale_request_timeout: (optional) Optional amount of time in seconds
          that is allowed for a running app to respond to a request.
    """

    def __init__(
        self,
        *,
        image_port: int = None,
        image_reference: str = None,
        image_secret: str = None,
        managed_domain_mappings: str = None,
        run_arguments: List[str] = None,
        run_as_user: int = None,
        run_commands: List[str] = None,
        run_env_variables: List['EnvVarPrototype'] = None,
        run_service_account: str = None,
        run_volume_mounts: List['VolumeMountPrototype'] = None,
        scale_concurrency: int = None,
        scale_concurrency_target: int = None,
        scale_cpu_limit: str = None,
        scale_ephemeral_storage_limit: str = None,
        scale_initial_instances: int = None,
        scale_max_instances: int = None,
        scale_memory_limit: str = None,
        scale_min_instances: int = None,
        scale_request_timeout: int = None,
    ) -> None:
        """
        Initialize a AppPatch object.

        :param int image_port: (optional) Optional port the app listens on. While
               the app will always be exposed via port `443` for end users, this port is
               used to connect to the port that is exposed by the container image.
        :param str image_reference: (optional) The name of the image that is used
               for this job. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where
               `REGISTRY` and `TAG` are optional. If `REGISTRY` is not specified, the
               default is `docker.io`. If `TAG` is not specified, the default is `latest`.
               If the image reference points to a registry that requires authentication,
               make sure to also specify the property `image_secret`.
        :param str image_secret: (optional) Optional name of the image registry
               access secret. The image registry access secret is used to authenticate
               with a private registry when you download the container image. If the image
               reference points to a registry that requires authentication, the app will
               be created but cannot reach the ready status, until this property is
               provided, too.
        :param str managed_domain_mappings: (optional) Optional value controlling
               which of the system managed domain mappings will be setup for the
               application. Valid values are 'local_public', 'local_private' and 'local'.
               Visibility can only be 'local_private' if the project supports application
               private visibility.
        :param List[str] run_arguments: (optional) Optional arguments for the app
               that are passed to start the container. If not specified an empty string
               array will be applied and the arguments specified by the container image,
               will be used to start the container.
        :param int run_as_user: (optional) Optional user ID (UID) to run the app
               (e.g., `1001`).
        :param List[str] run_commands: (optional) Optional commands for the app
               that are passed to start the container. If not specified an empty string
               array will be applied and the command specified by the container image,
               will be used to start the container.
        :param List[EnvVarPrototype] run_env_variables: (optional) Optional
               references to config maps, secrets or a literal values.
        :param str run_service_account: (optional) Optional name of the service
               account. For built-in service accounts, you can use the shortened names
               `manager` , `none`, `reader`, and `writer`.
        :param List[VolumeMountPrototype] run_volume_mounts: (optional) Optional
               mounts of config maps or a secrets. In case this is provided, existing
               `run_volume_mounts` will be overwritten.
        :param int scale_concurrency: (optional) Optional maximum number of
               requests that can be processed concurrently per instance.
        :param int scale_concurrency_target: (optional) Optional threshold of
               concurrent requests per instance at which one or more additional instances
               are created. Use this value to scale up instances based on concurrent
               number of requests. This option defaults to the value of the
               `scale_concurrency` option, if not specified.
        :param str scale_cpu_limit: (optional) Optional number of CPU set for the
               instance of the app. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
        :param str scale_ephemeral_storage_limit: (optional) Optional amount of
               ephemeral storage to set for the instance of the app. The amount specified
               as ephemeral storage, must not exceed the amount of `scale_memory_limit`.
               The units for specifying ephemeral storage are Megabyte (M) or Gigabyte
               (G), whereas G and M are the shorthand expressions for GB and MB. For more
               information see [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param int scale_initial_instances: (optional) Optional initial number of
               instances that are created upon app creation or app update.
        :param int scale_max_instances: (optional) Optional maximum number of
               instances for this app. If you set this value to `0`, this property does
               not set a upper scaling limit. However, the app scaling is still limited by
               the project quota for instances. See [Limits and quotas for Code
               Engine](https://cloud.ibm.com/docs/codeengine?topic=codeengine-limits).
        :param str scale_memory_limit: (optional) Optional amount of memory set for
               the instance of the app. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
               The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G
               and M are the shorthand expressions for GB and MB. For more information see
               [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param int scale_min_instances: (optional) Optional minimum number of
               instances for this app. If you set this value to `0`, the app will scale
               down to zero, if not hit by any request for some time.
        :param int scale_request_timeout: (optional) Optional amount of time in
               seconds that is allowed for a running app to respond to a request.
        """
        self.image_port = image_port
        self.image_reference = image_reference
        self.image_secret = image_secret
        self.managed_domain_mappings = managed_domain_mappings
        self.run_arguments = run_arguments
        self.run_as_user = run_as_user
        self.run_commands = run_commands
        self.run_env_variables = run_env_variables
        self.run_service_account = run_service_account
        self.run_volume_mounts = run_volume_mounts
        self.scale_concurrency = scale_concurrency
        self.scale_concurrency_target = scale_concurrency_target
        self.scale_cpu_limit = scale_cpu_limit
        self.scale_ephemeral_storage_limit = scale_ephemeral_storage_limit
        self.scale_initial_instances = scale_initial_instances
        self.scale_max_instances = scale_max_instances
        self.scale_memory_limit = scale_memory_limit
        self.scale_min_instances = scale_min_instances
        self.scale_request_timeout = scale_request_timeout

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AppPatch':
        """Initialize a AppPatch object from a json dictionary."""
        args = {}
        if 'image_port' in _dict:
            args['image_port'] = _dict.get('image_port')
        if 'image_reference' in _dict:
            args['image_reference'] = _dict.get('image_reference')
        if 'image_secret' in _dict:
            args['image_secret'] = _dict.get('image_secret')
        if 'managed_domain_mappings' in _dict:
            args['managed_domain_mappings'] = _dict.get('managed_domain_mappings')
        if 'run_arguments' in _dict:
            args['run_arguments'] = _dict.get('run_arguments')
        if 'run_as_user' in _dict:
            args['run_as_user'] = _dict.get('run_as_user')
        if 'run_commands' in _dict:
            args['run_commands'] = _dict.get('run_commands')
        if 'run_env_variables' in _dict:
            args['run_env_variables'] = [EnvVarPrototype.from_dict(v) for v in _dict.get('run_env_variables')]
        if 'run_service_account' in _dict:
            args['run_service_account'] = _dict.get('run_service_account')
        if 'run_volume_mounts' in _dict:
            args['run_volume_mounts'] = [VolumeMountPrototype.from_dict(v) for v in _dict.get('run_volume_mounts')]
        if 'scale_concurrency' in _dict:
            args['scale_concurrency'] = _dict.get('scale_concurrency')
        if 'scale_concurrency_target' in _dict:
            args['scale_concurrency_target'] = _dict.get('scale_concurrency_target')
        if 'scale_cpu_limit' in _dict:
            args['scale_cpu_limit'] = _dict.get('scale_cpu_limit')
        if 'scale_ephemeral_storage_limit' in _dict:
            args['scale_ephemeral_storage_limit'] = _dict.get('scale_ephemeral_storage_limit')
        if 'scale_initial_instances' in _dict:
            args['scale_initial_instances'] = _dict.get('scale_initial_instances')
        if 'scale_max_instances' in _dict:
            args['scale_max_instances'] = _dict.get('scale_max_instances')
        if 'scale_memory_limit' in _dict:
            args['scale_memory_limit'] = _dict.get('scale_memory_limit')
        if 'scale_min_instances' in _dict:
            args['scale_min_instances'] = _dict.get('scale_min_instances')
        if 'scale_request_timeout' in _dict:
            args['scale_request_timeout'] = _dict.get('scale_request_timeout')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AppPatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'image_port') and self.image_port is not None:
            _dict['image_port'] = self.image_port
        if hasattr(self, 'image_reference') and self.image_reference is not None:
            _dict['image_reference'] = self.image_reference
        if hasattr(self, 'image_secret') and self.image_secret is not None:
            _dict['image_secret'] = self.image_secret
        if hasattr(self, 'managed_domain_mappings') and self.managed_domain_mappings is not None:
            _dict['managed_domain_mappings'] = self.managed_domain_mappings
        if hasattr(self, 'run_arguments') and self.run_arguments is not None:
            _dict['run_arguments'] = self.run_arguments
        if hasattr(self, 'run_as_user') and self.run_as_user is not None:
            _dict['run_as_user'] = self.run_as_user
        if hasattr(self, 'run_commands') and self.run_commands is not None:
            _dict['run_commands'] = self.run_commands
        if hasattr(self, 'run_env_variables') and self.run_env_variables is not None:
            run_env_variables_list = []
            for v in self.run_env_variables:
                if isinstance(v, dict):
                    run_env_variables_list.append(v)
                else:
                    run_env_variables_list.append(v.to_dict())
            _dict['run_env_variables'] = run_env_variables_list
        if hasattr(self, 'run_service_account') and self.run_service_account is not None:
            _dict['run_service_account'] = self.run_service_account
        if hasattr(self, 'run_volume_mounts') and self.run_volume_mounts is not None:
            run_volume_mounts_list = []
            for v in self.run_volume_mounts:
                if isinstance(v, dict):
                    run_volume_mounts_list.append(v)
                else:
                    run_volume_mounts_list.append(v.to_dict())
            _dict['run_volume_mounts'] = run_volume_mounts_list
        if hasattr(self, 'scale_concurrency') and self.scale_concurrency is not None:
            _dict['scale_concurrency'] = self.scale_concurrency
        if hasattr(self, 'scale_concurrency_target') and self.scale_concurrency_target is not None:
            _dict['scale_concurrency_target'] = self.scale_concurrency_target
        if hasattr(self, 'scale_cpu_limit') and self.scale_cpu_limit is not None:
            _dict['scale_cpu_limit'] = self.scale_cpu_limit
        if hasattr(self, 'scale_ephemeral_storage_limit') and self.scale_ephemeral_storage_limit is not None:
            _dict['scale_ephemeral_storage_limit'] = self.scale_ephemeral_storage_limit
        if hasattr(self, 'scale_initial_instances') and self.scale_initial_instances is not None:
            _dict['scale_initial_instances'] = self.scale_initial_instances
        if hasattr(self, 'scale_max_instances') and self.scale_max_instances is not None:
            _dict['scale_max_instances'] = self.scale_max_instances
        if hasattr(self, 'scale_memory_limit') and self.scale_memory_limit is not None:
            _dict['scale_memory_limit'] = self.scale_memory_limit
        if hasattr(self, 'scale_min_instances') and self.scale_min_instances is not None:
            _dict['scale_min_instances'] = self.scale_min_instances
        if hasattr(self, 'scale_request_timeout') and self.scale_request_timeout is not None:
            _dict['scale_request_timeout'] = self.scale_request_timeout
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AppPatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AppPatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AppPatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ManagedDomainMappingsEnum(str, Enum):
        """
        Optional value controlling which of the system managed domain mappings will be
        setup for the application. Valid values are 'local_public', 'local_private' and
        'local'. Visibility can only be 'local_private' if the project supports
        application private visibility.
        """

        LOCAL = 'local'
        LOCAL_PRIVATE = 'local_private'
        LOCAL_PUBLIC = 'local_public'

    class RunServiceAccountEnum(str, Enum):
        """
        Optional name of the service account. For built-in service accounts, you can use
        the shortened names `manager` , `none`, `reader`, and `writer`.
        """

        DEFAULT = 'default'
        MANAGER = 'manager'
        READER = 'reader'
        WRITER = 'writer'
        NONE = 'none'


class AppRevision:
    """
    AppRevision is the response model for app revision resources.

    :attr str app_name: (optional) Name of the associated app.
    :attr str created_at: The date when the resource was created.
    :attr str href: When you provision a new revision,  a URL is created identifying
          the location of the instance.
    :attr str id: The identifier of the resource.
    :attr int image_port: (optional) Optional port the app listens on. While the app
          will always be exposed via port `443` for end users, this port is used to
          connect to the port that is exposed by the container image.
    :attr str image_reference: The name of the image that is used for this job. The
          format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and `TAG` are
          optional. If `REGISTRY` is not specified, the default is `docker.io`. If `TAG`
          is not specified, the default is `latest`. If the image reference points to a
          registry that requires authentication, make sure to also specify the property
          `image_secret`.
    :attr str image_secret: (optional) Optional name of the image registry access
          secret. The image registry access secret is used to authenticate with a private
          registry when you download the container image. If the image reference points to
          a registry that requires authentication, the app will be created but cannot
          reach the ready status, until this property is provided, too.
    :attr str name: The name of the app revison.
    :attr str project_id: The ID of the project the resource is located in.
    :attr str resource_type: The type of the app revision.
    :attr List[str] run_arguments: Optional arguments for the app that are passed to
          start the container. If not specified an empty string array will be applied and
          the arguments specified by the container image, will be used to start the
          container.
    :attr int run_as_user: (optional) Optional user ID (UID) to run the app (e.g.,
          `1001`).
    :attr List[str] run_commands: Optional commands for the app that are passed to
          start the container. If not specified an empty string array will be applied and
          the command specified by the container image, will be used to start the
          container.
    :attr List[EnvVar] run_env_variables: References to config maps, secrets or a
          literal values, which are exposed as environment variables in the application.
    :attr str run_service_account: (optional) Optional name of the service account.
          For built-in service accounts, you can use the shortened names `manager` ,
          `none`, `reader`, and `writer`.
    :attr List[VolumeMount] run_volume_mounts: Mounts of config maps or secrets.
    :attr int scale_concurrency: (optional) Optional maximum number of requests that
          can be processed concurrently per instance.
    :attr int scale_concurrency_target: (optional) Optional threshold of concurrent
          requests per instance at which one or more additional instances are created. Use
          this value to scale up instances based on concurrent number of requests. This
          option defaults to the value of the `scale_concurrency` option, if not
          specified.
    :attr str scale_cpu_limit: Optional number of CPU set for the instance of the
          app. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
    :attr str scale_ephemeral_storage_limit: Optional amount of ephemeral storage to
          set for the instance of the app. The amount specified as ephemeral storage, must
          not exceed the amount of `scale_memory_limit`. The units for specifying
          ephemeral storage are Megabyte (M) or Gigabyte (G), whereas G and M are the
          shorthand expressions for GB and MB. For more information see [Units of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :attr int scale_initial_instances: (optional) Optional initial number of
          instances that are created upon app creation or app update.
    :attr int scale_max_instances: Optional maximum number of instances for this
          app. If you set this value to `0`, this property does not set a upper scaling
          limit. However, the app scaling is still limited by the project quota for
          instances. See [Limits and quotas for Code
          Engine](https://cloud.ibm.com/docs/codeengine?topic=codeengine-limits).
    :attr str scale_memory_limit: Optional amount of memory set for the instance of
          the app. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
          The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and
          M are the shorthand expressions for GB and MB. For more information see [Units
          of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :attr int scale_min_instances: Optional minimum number of instances for this
          app. If you set this value to `0`, the app will scale down to zero, if not hit
          by any request for some time.
    :attr int scale_request_timeout: Optional amount of time in seconds that is
          allowed for a running app to respond to a request.
    :attr str status: The current status of the app revision.
    :attr AppRevisionStatus status_details: (optional) The detailed status of the
          application revision.
    """

    def __init__(
        self,
        created_at: str,
        href: str,
        id: str,
        image_reference: str,
        name: str,
        project_id: str,
        resource_type: str,
        run_arguments: List[str],
        run_commands: List[str],
        run_env_variables: List['EnvVar'],
        run_volume_mounts: List['VolumeMount'],
        scale_cpu_limit: str,
        scale_ephemeral_storage_limit: str,
        scale_max_instances: int,
        scale_memory_limit: str,
        scale_min_instances: int,
        scale_request_timeout: int,
        status: str,
        *,
        app_name: str = None,
        image_port: int = None,
        image_secret: str = None,
        run_as_user: int = None,
        run_service_account: str = None,
        scale_concurrency: int = None,
        scale_concurrency_target: int = None,
        scale_initial_instances: int = None,
        status_details: 'AppRevisionStatus' = None,
    ) -> None:
        """
        Initialize a AppRevision object.

        :param str created_at: The date when the resource was created.
        :param str href: When you provision a new revision,  a URL is created
               identifying the location of the instance.
        :param str id: The identifier of the resource.
        :param str image_reference: The name of the image that is used for this
               job. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and
               `TAG` are optional. If `REGISTRY` is not specified, the default is
               `docker.io`. If `TAG` is not specified, the default is `latest`. If the
               image reference points to a registry that requires authentication, make
               sure to also specify the property `image_secret`.
        :param str name: The name of the app revison.
        :param str project_id: The ID of the project the resource is located in.
        :param str resource_type: The type of the app revision.
        :param List[str] run_arguments: Optional arguments for the app that are
               passed to start the container. If not specified an empty string array will
               be applied and the arguments specified by the container image, will be used
               to start the container.
        :param List[str] run_commands: Optional commands for the app that are
               passed to start the container. If not specified an empty string array will
               be applied and the command specified by the container image, will be used
               to start the container.
        :param List[EnvVar] run_env_variables: References to config maps, secrets
               or a literal values, which are exposed as environment variables in the
               application.
        :param List[VolumeMount] run_volume_mounts: Mounts of config maps or
               secrets.
        :param str scale_cpu_limit: Optional number of CPU set for the instance of
               the app. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
        :param str scale_ephemeral_storage_limit: Optional amount of ephemeral
               storage to set for the instance of the app. The amount specified as
               ephemeral storage, must not exceed the amount of `scale_memory_limit`. The
               units for specifying ephemeral storage are Megabyte (M) or Gigabyte (G),
               whereas G and M are the shorthand expressions for GB and MB. For more
               information see [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param int scale_max_instances: Optional maximum number of instances for
               this app. If you set this value to `0`, this property does not set a upper
               scaling limit. However, the app scaling is still limited by the project
               quota for instances. See [Limits and quotas for Code
               Engine](https://cloud.ibm.com/docs/codeengine?topic=codeengine-limits).
        :param str scale_memory_limit: Optional amount of memory set for the
               instance of the app. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
               The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G
               and M are the shorthand expressions for GB and MB. For more information see
               [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param int scale_min_instances: Optional minimum number of instances for
               this app. If you set this value to `0`, the app will scale down to zero, if
               not hit by any request for some time.
        :param int scale_request_timeout: Optional amount of time in seconds that
               is allowed for a running app to respond to a request.
        :param str status: The current status of the app revision.
        :param str app_name: (optional) Name of the associated app.
        :param int image_port: (optional) Optional port the app listens on. While
               the app will always be exposed via port `443` for end users, this port is
               used to connect to the port that is exposed by the container image.
        :param str image_secret: (optional) Optional name of the image registry
               access secret. The image registry access secret is used to authenticate
               with a private registry when you download the container image. If the image
               reference points to a registry that requires authentication, the app will
               be created but cannot reach the ready status, until this property is
               provided, too.
        :param int run_as_user: (optional) Optional user ID (UID) to run the app
               (e.g., `1001`).
        :param str run_service_account: (optional) Optional name of the service
               account. For built-in service accounts, you can use the shortened names
               `manager` , `none`, `reader`, and `writer`.
        :param int scale_concurrency: (optional) Optional maximum number of
               requests that can be processed concurrently per instance.
        :param int scale_concurrency_target: (optional) Optional threshold of
               concurrent requests per instance at which one or more additional instances
               are created. Use this value to scale up instances based on concurrent
               number of requests. This option defaults to the value of the
               `scale_concurrency` option, if not specified.
        :param int scale_initial_instances: (optional) Optional initial number of
               instances that are created upon app creation or app update.
        :param AppRevisionStatus status_details: (optional) The detailed status of
               the application revision.
        """
        self.app_name = app_name
        self.created_at = created_at
        self.href = href
        self.id = id
        self.image_port = image_port
        self.image_reference = image_reference
        self.image_secret = image_secret
        self.name = name
        self.project_id = project_id
        self.resource_type = resource_type
        self.run_arguments = run_arguments
        self.run_as_user = run_as_user
        self.run_commands = run_commands
        self.run_env_variables = run_env_variables
        self.run_service_account = run_service_account
        self.run_volume_mounts = run_volume_mounts
        self.scale_concurrency = scale_concurrency
        self.scale_concurrency_target = scale_concurrency_target
        self.scale_cpu_limit = scale_cpu_limit
        self.scale_ephemeral_storage_limit = scale_ephemeral_storage_limit
        self.scale_initial_instances = scale_initial_instances
        self.scale_max_instances = scale_max_instances
        self.scale_memory_limit = scale_memory_limit
        self.scale_min_instances = scale_min_instances
        self.scale_request_timeout = scale_request_timeout
        self.status = status
        self.status_details = status_details

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AppRevision':
        """Initialize a AppRevision object from a json dictionary."""
        args = {}
        if 'app_name' in _dict:
            args['app_name'] = _dict.get('app_name')
        if 'created_at' in _dict:
            args['created_at'] = _dict.get('created_at')
        else:
            raise ValueError('Required property \'created_at\' not present in AppRevision JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in AppRevision JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in AppRevision JSON')
        if 'image_port' in _dict:
            args['image_port'] = _dict.get('image_port')
        if 'image_reference' in _dict:
            args['image_reference'] = _dict.get('image_reference')
        else:
            raise ValueError('Required property \'image_reference\' not present in AppRevision JSON')
        if 'image_secret' in _dict:
            args['image_secret'] = _dict.get('image_secret')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in AppRevision JSON')
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        else:
            raise ValueError('Required property \'project_id\' not present in AppRevision JSON')
        if 'resource_type' in _dict:
            args['resource_type'] = _dict.get('resource_type')
        else:
            raise ValueError('Required property \'resource_type\' not present in AppRevision JSON')
        if 'run_arguments' in _dict:
            args['run_arguments'] = _dict.get('run_arguments')
        else:
            raise ValueError('Required property \'run_arguments\' not present in AppRevision JSON')
        if 'run_as_user' in _dict:
            args['run_as_user'] = _dict.get('run_as_user')
        if 'run_commands' in _dict:
            args['run_commands'] = _dict.get('run_commands')
        else:
            raise ValueError('Required property \'run_commands\' not present in AppRevision JSON')
        if 'run_env_variables' in _dict:
            args['run_env_variables'] = [EnvVar.from_dict(v) for v in _dict.get('run_env_variables')]
        else:
            raise ValueError('Required property \'run_env_variables\' not present in AppRevision JSON')
        if 'run_service_account' in _dict:
            args['run_service_account'] = _dict.get('run_service_account')
        if 'run_volume_mounts' in _dict:
            args['run_volume_mounts'] = [VolumeMount.from_dict(v) for v in _dict.get('run_volume_mounts')]
        else:
            raise ValueError('Required property \'run_volume_mounts\' not present in AppRevision JSON')
        if 'scale_concurrency' in _dict:
            args['scale_concurrency'] = _dict.get('scale_concurrency')
        if 'scale_concurrency_target' in _dict:
            args['scale_concurrency_target'] = _dict.get('scale_concurrency_target')
        if 'scale_cpu_limit' in _dict:
            args['scale_cpu_limit'] = _dict.get('scale_cpu_limit')
        else:
            raise ValueError('Required property \'scale_cpu_limit\' not present in AppRevision JSON')
        if 'scale_ephemeral_storage_limit' in _dict:
            args['scale_ephemeral_storage_limit'] = _dict.get('scale_ephemeral_storage_limit')
        else:
            raise ValueError('Required property \'scale_ephemeral_storage_limit\' not present in AppRevision JSON')
        if 'scale_initial_instances' in _dict:
            args['scale_initial_instances'] = _dict.get('scale_initial_instances')
        if 'scale_max_instances' in _dict:
            args['scale_max_instances'] = _dict.get('scale_max_instances')
        else:
            raise ValueError('Required property \'scale_max_instances\' not present in AppRevision JSON')
        if 'scale_memory_limit' in _dict:
            args['scale_memory_limit'] = _dict.get('scale_memory_limit')
        else:
            raise ValueError('Required property \'scale_memory_limit\' not present in AppRevision JSON')
        if 'scale_min_instances' in _dict:
            args['scale_min_instances'] = _dict.get('scale_min_instances')
        else:
            raise ValueError('Required property \'scale_min_instances\' not present in AppRevision JSON')
        if 'scale_request_timeout' in _dict:
            args['scale_request_timeout'] = _dict.get('scale_request_timeout')
        else:
            raise ValueError('Required property \'scale_request_timeout\' not present in AppRevision JSON')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in AppRevision JSON')
        if 'status_details' in _dict:
            args['status_details'] = AppRevisionStatus.from_dict(_dict.get('status_details'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AppRevision object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'app_name') and self.app_name is not None:
            _dict['app_name'] = self.app_name
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = self.created_at
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'image_port') and self.image_port is not None:
            _dict['image_port'] = self.image_port
        if hasattr(self, 'image_reference') and self.image_reference is not None:
            _dict['image_reference'] = self.image_reference
        if hasattr(self, 'image_secret') and self.image_secret is not None:
            _dict['image_secret'] = self.image_secret
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'project_id') and self.project_id is not None:
            _dict['project_id'] = self.project_id
        if hasattr(self, 'resource_type') and self.resource_type is not None:
            _dict['resource_type'] = self.resource_type
        if hasattr(self, 'run_arguments') and self.run_arguments is not None:
            _dict['run_arguments'] = self.run_arguments
        if hasattr(self, 'run_as_user') and self.run_as_user is not None:
            _dict['run_as_user'] = self.run_as_user
        if hasattr(self, 'run_commands') and self.run_commands is not None:
            _dict['run_commands'] = self.run_commands
        if hasattr(self, 'run_env_variables') and self.run_env_variables is not None:
            run_env_variables_list = []
            for v in self.run_env_variables:
                if isinstance(v, dict):
                    run_env_variables_list.append(v)
                else:
                    run_env_variables_list.append(v.to_dict())
            _dict['run_env_variables'] = run_env_variables_list
        if hasattr(self, 'run_service_account') and self.run_service_account is not None:
            _dict['run_service_account'] = self.run_service_account
        if hasattr(self, 'run_volume_mounts') and self.run_volume_mounts is not None:
            run_volume_mounts_list = []
            for v in self.run_volume_mounts:
                if isinstance(v, dict):
                    run_volume_mounts_list.append(v)
                else:
                    run_volume_mounts_list.append(v.to_dict())
            _dict['run_volume_mounts'] = run_volume_mounts_list
        if hasattr(self, 'scale_concurrency') and self.scale_concurrency is not None:
            _dict['scale_concurrency'] = self.scale_concurrency
        if hasattr(self, 'scale_concurrency_target') and self.scale_concurrency_target is not None:
            _dict['scale_concurrency_target'] = self.scale_concurrency_target
        if hasattr(self, 'scale_cpu_limit') and self.scale_cpu_limit is not None:
            _dict['scale_cpu_limit'] = self.scale_cpu_limit
        if hasattr(self, 'scale_ephemeral_storage_limit') and self.scale_ephemeral_storage_limit is not None:
            _dict['scale_ephemeral_storage_limit'] = self.scale_ephemeral_storage_limit
        if hasattr(self, 'scale_initial_instances') and self.scale_initial_instances is not None:
            _dict['scale_initial_instances'] = self.scale_initial_instances
        if hasattr(self, 'scale_max_instances') and self.scale_max_instances is not None:
            _dict['scale_max_instances'] = self.scale_max_instances
        if hasattr(self, 'scale_memory_limit') and self.scale_memory_limit is not None:
            _dict['scale_memory_limit'] = self.scale_memory_limit
        if hasattr(self, 'scale_min_instances') and self.scale_min_instances is not None:
            _dict['scale_min_instances'] = self.scale_min_instances
        if hasattr(self, 'scale_request_timeout') and self.scale_request_timeout is not None:
            _dict['scale_request_timeout'] = self.scale_request_timeout
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'status_details') and self.status_details is not None:
            if isinstance(self.status_details, dict):
                _dict['status_details'] = self.status_details
            else:
                _dict['status_details'] = self.status_details.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AppRevision object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AppRevision') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AppRevision') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ResourceTypeEnum(str, Enum):
        """
        The type of the app revision.
        """

        APP_REVISION_V2 = 'app_revision_v2'

    class RunServiceAccountEnum(str, Enum):
        """
        Optional name of the service account. For built-in service accounts, you can use
        the shortened names `manager` , `none`, `reader`, and `writer`.
        """

        DEFAULT = 'default'
        MANAGER = 'manager'
        READER = 'reader'
        WRITER = 'writer'
        NONE = 'none'

    class StatusEnum(str, Enum):
        """
        The current status of the app revision.
        """

        READY = 'ready'
        LOADING = 'loading'
        WARNING = 'warning'
        FAILED = 'failed'


class AppRevisionList:
    """
    Contains a list of app revisions and pagination information.

    :attr ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :attr int limit: Maximum number of resources per page.
    :attr ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    :attr List[AppRevision] revisions: List of all app revisions.
    """

    def __init__(
        self,
        limit: int,
        revisions: List['AppRevision'],
        *,
        first: 'ListFirstMetadata' = None,
        next: 'ListNextMetadata' = None,
    ) -> None:
        """
        Initialize a AppRevisionList object.

        :param int limit: Maximum number of resources per page.
        :param List[AppRevision] revisions: List of all app revisions.
        :param ListFirstMetadata first: (optional) Describes properties needed to
               retrieve the first page of a result list.
        :param ListNextMetadata next: (optional) Describes properties needed to
               retrieve the next page of a result list.
        """
        self.first = first
        self.limit = limit
        self.next = next
        self.revisions = revisions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AppRevisionList':
        """Initialize a AppRevisionList object from a json dictionary."""
        args = {}
        if 'first' in _dict:
            args['first'] = ListFirstMetadata.from_dict(_dict.get('first'))
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in AppRevisionList JSON')
        if 'next' in _dict:
            args['next'] = ListNextMetadata.from_dict(_dict.get('next'))
        if 'revisions' in _dict:
            args['revisions'] = [AppRevision.from_dict(v) for v in _dict.get('revisions')]
        else:
            raise ValueError('Required property \'revisions\' not present in AppRevisionList JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AppRevisionList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'revisions') and self.revisions is not None:
            revisions_list = []
            for v in self.revisions:
                if isinstance(v, dict):
                    revisions_list.append(v)
                else:
                    revisions_list.append(v.to_dict())
            _dict['revisions'] = revisions_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AppRevisionList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AppRevisionList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AppRevisionList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AppRevisionStatus:
    """
    The detailed status of the application revision.

    :attr int actual_instances: (optional) The number of running instances of the
          revision.
    :attr str reason: (optional) Optional information to provide more context in
          case of a 'failed' or 'warning' status.
    """

    def __init__(self, *, actual_instances: int = None, reason: str = None) -> None:
        """
        Initialize a AppRevisionStatus object.

        :param int actual_instances: (optional) The number of running instances of
               the revision.
        :param str reason: (optional) Optional information to provide more context
               in case of a 'failed' or 'warning' status.
        """
        self.actual_instances = actual_instances
        self.reason = reason

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AppRevisionStatus':
        """Initialize a AppRevisionStatus object from a json dictionary."""
        args = {}
        if 'actual_instances' in _dict:
            args['actual_instances'] = _dict.get('actual_instances')
        if 'reason' in _dict:
            args['reason'] = _dict.get('reason')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AppRevisionStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'actual_instances') and self.actual_instances is not None:
            _dict['actual_instances'] = self.actual_instances
        if hasattr(self, 'reason') and self.reason is not None:
            _dict['reason'] = self.reason
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AppRevisionStatus object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AppRevisionStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AppRevisionStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ReasonEnum(str, Enum):
        """
        Optional information to provide more context in case of a 'failed' or 'warning'
        status.
        """

        READY = 'ready'
        WAITING = 'waiting'
        DEPLOYING = 'deploying'
        DEPLOYING_WAITING_FOR_RESOURCES = 'deploying_waiting_for_resources'
        INITIAL_SCALE_NEVER_ACHIEVED = 'initial_scale_never_achieved'
        FETCH_IMAGE_FAILED_UNKNOWN_MANIFEST = 'fetch_image_failed_unknown_manifest'
        FETCH_IMAGE_FAILED_UNKNOWN_REPOSITORY = 'fetch_image_failed_unknown_repository'
        FETCH_IMAGE_FAILED_REGISTRY_NOT_FOUND = 'fetch_image_failed_registry_not_found'
        FETCH_IMAGE_FAILED_MISSING_PULL_SECRET = 'fetch_image_failed_missing_pull_secret'
        FETCH_IMAGE_FAILED_WRONG_PULL_CREDENTIALS = 'fetch_image_failed_wrong_pull_credentials'
        FETCH_IMAGE_FAILED_MISSING_PULL_CREDENTIALS = 'fetch_image_failed_missing_pull_credentials'
        CONTAINER_FAILED_EXIT_CODE_0 = 'container_failed_exit_code_0'
        CONTAINER_FAILED_EXIT_CODE_1 = 'container_failed_exit_code_1'
        CONTAINER_FAILED_EXIT_CODE_139 = 'container_failed_exit_code_139'
        CONTAINER_FAILED_EXIT_CODE_24 = 'container_failed_exit_code_24'
        IMAGE_PULL_BACK_OFF = 'image_pull_back_off'
        INVALID_TAR_HEADER_IMAGE_PULL_ERR = 'invalid_tar_header_image_pull_err'


class AppStatus:
    """
    The detailed status of the application.

    :attr str latest_created_revision: (optional) Latest app revision that has been
          created.
    :attr str latest_ready_revision: (optional) Latest app revision that reached a
          ready state.
    :attr str reason: (optional) Optional information to provide more context in
          case of a 'failed' or 'warning' status.
    """

    def __init__(
        self, *, latest_created_revision: str = None, latest_ready_revision: str = None, reason: str = None
    ) -> None:
        """
        Initialize a AppStatus object.

        :param str latest_created_revision: (optional) Latest app revision that has
               been created.
        :param str latest_ready_revision: (optional) Latest app revision that
               reached a ready state.
        :param str reason: (optional) Optional information to provide more context
               in case of a 'failed' or 'warning' status.
        """
        self.latest_created_revision = latest_created_revision
        self.latest_ready_revision = latest_ready_revision
        self.reason = reason

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AppStatus':
        """Initialize a AppStatus object from a json dictionary."""
        args = {}
        if 'latest_created_revision' in _dict:
            args['latest_created_revision'] = _dict.get('latest_created_revision')
        if 'latest_ready_revision' in _dict:
            args['latest_ready_revision'] = _dict.get('latest_ready_revision')
        if 'reason' in _dict:
            args['reason'] = _dict.get('reason')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AppStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'latest_created_revision') and self.latest_created_revision is not None:
            _dict['latest_created_revision'] = self.latest_created_revision
        if hasattr(self, 'latest_ready_revision') and self.latest_ready_revision is not None:
            _dict['latest_ready_revision'] = self.latest_ready_revision
        if hasattr(self, 'reason') and self.reason is not None:
            _dict['reason'] = self.reason
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AppStatus object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AppStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AppStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ReasonEnum(str, Enum):
        """
        Optional information to provide more context in case of a 'failed' or 'warning'
        status.
        """

        READY = 'ready'
        DEPLOYING = 'deploying'
        WAITING_FOR_RESOURCES = 'waiting_for_resources'
        NO_REVISION_READY = 'no_revision_ready'
        READY_BUT_LATEST_REVISION_FAILED = 'ready_but_latest_revision_failed'


class Build:
    """
    Response model for build definitions.

    :attr str created_at: The date when the resource was created.
    :attr str entity_tag: The version of the build instance, which is used to
          achieve optimistic locking.
    :attr str href: (optional) When you provision a new build,  a URL is created
          identifying the location of the instance.
    :attr str id: The identifier of the resource.
    :attr str name: (optional) The name of the build.
    :attr str output_image: The name of the image.
    :attr str output_secret: The secret that is required to access the image
          registry. Make sure that the secret is granted with push permissions towards the
          specified container registry namespace.
    :attr str project_id: The ID of the project the resource is located in.
    :attr str resource_type: (optional) The type of the build.
    :attr str source_context_dir: (optional) Option directory in the repository that
          contains the buildpacks file or the Dockerfile.
    :attr str source_revision: (optional) Commit, tag, or branch in the source
          repository to pull. This field is optional if the `source_type` is `git` and
          uses the HEAD of default branch if not specified. If the `source_type` value is
          `local`, this field must be omitted.
    :attr str source_secret: (optional) Name of the secret that is used access the
          repository source. This field is optional if the `source_type` is `git`.
          Additionally, if the `source_url` points to a repository that requires
          authentication, the build will be created but cannot access any source code,
          until this property is provided, too. If the `source_type` value is `local`,
          this field must be omitted.
    :attr str source_type: Specifies the type of source to determine if your build
          source is in a repository or based on local source code.
          * local - For builds from local source code.
          * git - For builds from git version controlled source code.
    :attr str source_url: The URL of the code repository. This field is required if
          the `source_type` is `git`. If the `source_type` value is `local`, this field
          must be omitted. If the repository is publicly available you can provide a
          'https' URL like `https://github.com/IBM/CodeEngine`. If the repository requires
          authentication, you need to provide a 'ssh' URL like
          `git@github.com:IBM/CodeEngine.git` along with a `source_secret` that points to
          a secret of format `ssh_auth`.
    :attr str status: (optional) The current status of the build.
    :attr BuildStatus status_details: (optional) The detailed status of the build.
    :attr str strategy_size: Optional size for the build, which determines the
          amount of resources used. Build sizes are `small`, `medium`, `large`, `xlarge`.
    :attr str strategy_spec_file: (optional) Optional path to the specification file
          that is used for build strategies for building an image.
    :attr str strategy_type: The strategy to use for building the image.
    :attr int timeout: (optional) The maximum amount of time, in seconds, that can
          pass before the build must succeed or fail.
    """

    def __init__(
        self,
        created_at: str,
        entity_tag: str,
        id: str,
        output_image: str,
        output_secret: str,
        project_id: str,
        source_type: str,
        source_url: str,
        strategy_size: str,
        strategy_type: str,
        *,
        href: str = None,
        name: str = None,
        resource_type: str = None,
        source_context_dir: str = None,
        source_revision: str = None,
        source_secret: str = None,
        status: str = None,
        status_details: 'BuildStatus' = None,
        strategy_spec_file: str = None,
        timeout: int = None,
    ) -> None:
        """
        Initialize a Build object.

        :param str created_at: The date when the resource was created.
        :param str entity_tag: The version of the build instance, which is used to
               achieve optimistic locking.
        :param str id: The identifier of the resource.
        :param str output_image: The name of the image.
        :param str output_secret: The secret that is required to access the image
               registry. Make sure that the secret is granted with push permissions
               towards the specified container registry namespace.
        :param str project_id: The ID of the project the resource is located in.
        :param str source_type: Specifies the type of source to determine if your
               build source is in a repository or based on local source code.
               * local - For builds from local source code.
               * git - For builds from git version controlled source code.
        :param str source_url: The URL of the code repository. This field is
               required if the `source_type` is `git`. If the `source_type` value is
               `local`, this field must be omitted. If the repository is publicly
               available you can provide a 'https' URL like
               `https://github.com/IBM/CodeEngine`. If the repository requires
               authentication, you need to provide a 'ssh' URL like
               `git@github.com:IBM/CodeEngine.git` along with a `source_secret` that
               points to a secret of format `ssh_auth`.
        :param str strategy_size: Optional size for the build, which determines the
               amount of resources used. Build sizes are `small`, `medium`, `large`,
               `xlarge`.
        :param str strategy_type: The strategy to use for building the image.
        :param str href: (optional) When you provision a new build,  a URL is
               created identifying the location of the instance.
        :param str name: (optional) The name of the build.
        :param str resource_type: (optional) The type of the build.
        :param str source_context_dir: (optional) Option directory in the
               repository that contains the buildpacks file or the Dockerfile.
        :param str source_revision: (optional) Commit, tag, or branch in the source
               repository to pull. This field is optional if the `source_type` is `git`
               and uses the HEAD of default branch if not specified. If the `source_type`
               value is `local`, this field must be omitted.
        :param str source_secret: (optional) Name of the secret that is used access
               the repository source. This field is optional if the `source_type` is
               `git`. Additionally, if the `source_url` points to a repository that
               requires authentication, the build will be created but cannot access any
               source code, until this property is provided, too. If the `source_type`
               value is `local`, this field must be omitted.
        :param str status: (optional) The current status of the build.
        :param BuildStatus status_details: (optional) The detailed status of the
               build.
        :param str strategy_spec_file: (optional) Optional path to the
               specification file that is used for build strategies for building an image.
        :param int timeout: (optional) The maximum amount of time, in seconds, that
               can pass before the build must succeed or fail.
        """
        self.created_at = created_at
        self.entity_tag = entity_tag
        self.href = href
        self.id = id
        self.name = name
        self.output_image = output_image
        self.output_secret = output_secret
        self.project_id = project_id
        self.resource_type = resource_type
        self.source_context_dir = source_context_dir
        self.source_revision = source_revision
        self.source_secret = source_secret
        self.source_type = source_type
        self.source_url = source_url
        self.status = status
        self.status_details = status_details
        self.strategy_size = strategy_size
        self.strategy_spec_file = strategy_spec_file
        self.strategy_type = strategy_type
        self.timeout = timeout

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Build':
        """Initialize a Build object from a json dictionary."""
        args = {}
        if 'created_at' in _dict:
            args['created_at'] = _dict.get('created_at')
        else:
            raise ValueError('Required property \'created_at\' not present in Build JSON')
        if 'entity_tag' in _dict:
            args['entity_tag'] = _dict.get('entity_tag')
        else:
            raise ValueError('Required property \'entity_tag\' not present in Build JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Build JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'output_image' in _dict:
            args['output_image'] = _dict.get('output_image')
        else:
            raise ValueError('Required property \'output_image\' not present in Build JSON')
        if 'output_secret' in _dict:
            args['output_secret'] = _dict.get('output_secret')
        else:
            raise ValueError('Required property \'output_secret\' not present in Build JSON')
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        else:
            raise ValueError('Required property \'project_id\' not present in Build JSON')
        if 'resource_type' in _dict:
            args['resource_type'] = _dict.get('resource_type')
        if 'source_context_dir' in _dict:
            args['source_context_dir'] = _dict.get('source_context_dir')
        if 'source_revision' in _dict:
            args['source_revision'] = _dict.get('source_revision')
        if 'source_secret' in _dict:
            args['source_secret'] = _dict.get('source_secret')
        if 'source_type' in _dict:
            args['source_type'] = _dict.get('source_type')
        else:
            raise ValueError('Required property \'source_type\' not present in Build JSON')
        if 'source_url' in _dict:
            args['source_url'] = _dict.get('source_url')
        else:
            raise ValueError('Required property \'source_url\' not present in Build JSON')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'status_details' in _dict:
            args['status_details'] = BuildStatus.from_dict(_dict.get('status_details'))
        if 'strategy_size' in _dict:
            args['strategy_size'] = _dict.get('strategy_size')
        else:
            raise ValueError('Required property \'strategy_size\' not present in Build JSON')
        if 'strategy_spec_file' in _dict:
            args['strategy_spec_file'] = _dict.get('strategy_spec_file')
        if 'strategy_type' in _dict:
            args['strategy_type'] = _dict.get('strategy_type')
        else:
            raise ValueError('Required property \'strategy_type\' not present in Build JSON')
        if 'timeout' in _dict:
            args['timeout'] = _dict.get('timeout')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Build object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = self.created_at
        if hasattr(self, 'entity_tag') and self.entity_tag is not None:
            _dict['entity_tag'] = self.entity_tag
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'output_image') and self.output_image is not None:
            _dict['output_image'] = self.output_image
        if hasattr(self, 'output_secret') and self.output_secret is not None:
            _dict['output_secret'] = self.output_secret
        if hasattr(self, 'project_id') and self.project_id is not None:
            _dict['project_id'] = self.project_id
        if hasattr(self, 'resource_type') and self.resource_type is not None:
            _dict['resource_type'] = self.resource_type
        if hasattr(self, 'source_context_dir') and self.source_context_dir is not None:
            _dict['source_context_dir'] = self.source_context_dir
        if hasattr(self, 'source_revision') and self.source_revision is not None:
            _dict['source_revision'] = self.source_revision
        if hasattr(self, 'source_secret') and self.source_secret is not None:
            _dict['source_secret'] = self.source_secret
        if hasattr(self, 'source_type') and self.source_type is not None:
            _dict['source_type'] = self.source_type
        if hasattr(self, 'source_url') and self.source_url is not None:
            _dict['source_url'] = self.source_url
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'status_details') and self.status_details is not None:
            if isinstance(self.status_details, dict):
                _dict['status_details'] = self.status_details
            else:
                _dict['status_details'] = self.status_details.to_dict()
        if hasattr(self, 'strategy_size') and self.strategy_size is not None:
            _dict['strategy_size'] = self.strategy_size
        if hasattr(self, 'strategy_spec_file') and self.strategy_spec_file is not None:
            _dict['strategy_spec_file'] = self.strategy_spec_file
        if hasattr(self, 'strategy_type') and self.strategy_type is not None:
            _dict['strategy_type'] = self.strategy_type
        if hasattr(self, 'timeout') and self.timeout is not None:
            _dict['timeout'] = self.timeout
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Build object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Build') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Build') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ResourceTypeEnum(str, Enum):
        """
        The type of the build.
        """

        BUILD_V2 = 'build_v2'

    class SourceTypeEnum(str, Enum):
        """
        Specifies the type of source to determine if your build source is in a repository
        or based on local source code.
        * local - For builds from local source code.
        * git - For builds from git version controlled source code.
        """

        LOCAL = 'local'
        GIT = 'git'

    class StatusEnum(str, Enum):
        """
        The current status of the build.
        """

        READY = 'ready'
        FAILED = 'failed'


class BuildList:
    """
    Contains a list of builds and pagination information.

    :attr List[Build] builds: List of all builds.
    :attr ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :attr int limit: Maximum number of resources per page.
    :attr ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    """

    def __init__(
        self, builds: List['Build'], limit: int, *, first: 'ListFirstMetadata' = None, next: 'ListNextMetadata' = None
    ) -> None:
        """
        Initialize a BuildList object.

        :param List[Build] builds: List of all builds.
        :param int limit: Maximum number of resources per page.
        :param ListFirstMetadata first: (optional) Describes properties needed to
               retrieve the first page of a result list.
        :param ListNextMetadata next: (optional) Describes properties needed to
               retrieve the next page of a result list.
        """
        self.builds = builds
        self.first = first
        self.limit = limit
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BuildList':
        """Initialize a BuildList object from a json dictionary."""
        args = {}
        if 'builds' in _dict:
            args['builds'] = [Build.from_dict(v) for v in _dict.get('builds')]
        else:
            raise ValueError('Required property \'builds\' not present in BuildList JSON')
        if 'first' in _dict:
            args['first'] = ListFirstMetadata.from_dict(_dict.get('first'))
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in BuildList JSON')
        if 'next' in _dict:
            args['next'] = ListNextMetadata.from_dict(_dict.get('next'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BuildList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'builds') and self.builds is not None:
            builds_list = []
            for v in self.builds:
                if isinstance(v, dict):
                    builds_list.append(v)
                else:
                    builds_list.append(v.to_dict())
            _dict['builds'] = builds_list
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BuildList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BuildList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BuildList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BuildPatch:
    """
    Patch a build object.

    :attr str output_image: (optional) The name of the image.
    :attr str output_secret: (optional) The secret that is required to access the
          image registry. Make sure that the secret is granted with push permissions
          towards the specified container registry namespace.
    :attr str source_context_dir: (optional) Option directory in the repository that
          contains the buildpacks file or the Dockerfile.
    :attr str source_revision: (optional) Commit, tag, or branch in the source
          repository to pull. This field is optional if the `source_type` is `git` and
          uses the HEAD of default branch if not specified. If the `source_type` value is
          `local`, this field must be omitted.
    :attr str source_secret: (optional) Name of the secret that is used access the
          repository source. This field is optional if the `source_type` is `git`.
          Additionally, if the `source_url` points to a repository that requires
          authentication, the build will be created but cannot access any source code,
          until this property is provided, too. If the `source_type` value is `local`,
          this field must be omitted.
    :attr str source_type: (optional) Specifies the type of source to determine if
          your build source is in a repository or based on local source code.
          * local - For builds from local source code.
          * git - For builds from git version controlled source code.
    :attr str source_url: (optional) The URL of the code repository. This field is
          required if the `source_type` is `git`. If the `source_type` value is `local`,
          this field must be omitted. If the repository is publicly available you can
          provide a 'https' URL like `https://github.com/IBM/CodeEngine`. If the
          repository requires authentication, you need to provide a 'ssh' URL like
          `git@github.com:IBM/CodeEngine.git` along with a `source_secret` that points to
          a secret of format `ssh_auth`.
    :attr str strategy_size: (optional) Optional size for the build, which
          determines the amount of resources used. Build sizes are `small`, `medium`,
          `large`, `xlarge`.
    :attr str strategy_spec_file: (optional) Optional path to the specification file
          that is used for build strategies for building an image.
    :attr str strategy_type: (optional) The strategy to use for building the image.
    :attr int timeout: (optional) The maximum amount of time, in seconds, that can
          pass before the build must succeed or fail.
    """

    def __init__(
        self,
        *,
        output_image: str = None,
        output_secret: str = None,
        source_context_dir: str = None,
        source_revision: str = None,
        source_secret: str = None,
        source_type: str = None,
        source_url: str = None,
        strategy_size: str = None,
        strategy_spec_file: str = None,
        strategy_type: str = None,
        timeout: int = None,
    ) -> None:
        """
        Initialize a BuildPatch object.

        :param str output_image: (optional) The name of the image.
        :param str output_secret: (optional) The secret that is required to access
               the image registry. Make sure that the secret is granted with push
               permissions towards the specified container registry namespace.
        :param str source_context_dir: (optional) Option directory in the
               repository that contains the buildpacks file or the Dockerfile.
        :param str source_revision: (optional) Commit, tag, or branch in the source
               repository to pull. This field is optional if the `source_type` is `git`
               and uses the HEAD of default branch if not specified. If the `source_type`
               value is `local`, this field must be omitted.
        :param str source_secret: (optional) Name of the secret that is used access
               the repository source. This field is optional if the `source_type` is
               `git`. Additionally, if the `source_url` points to a repository that
               requires authentication, the build will be created but cannot access any
               source code, until this property is provided, too. If the `source_type`
               value is `local`, this field must be omitted.
        :param str source_type: (optional) Specifies the type of source to
               determine if your build source is in a repository or based on local source
               code.
               * local - For builds from local source code.
               * git - For builds from git version controlled source code.
        :param str source_url: (optional) The URL of the code repository. This
               field is required if the `source_type` is `git`. If the `source_type` value
               is `local`, this field must be omitted. If the repository is publicly
               available you can provide a 'https' URL like
               `https://github.com/IBM/CodeEngine`. If the repository requires
               authentication, you need to provide a 'ssh' URL like
               `git@github.com:IBM/CodeEngine.git` along with a `source_secret` that
               points to a secret of format `ssh_auth`.
        :param str strategy_size: (optional) Optional size for the build, which
               determines the amount of resources used. Build sizes are `small`, `medium`,
               `large`, `xlarge`.
        :param str strategy_spec_file: (optional) Optional path to the
               specification file that is used for build strategies for building an image.
        :param str strategy_type: (optional) The strategy to use for building the
               image.
        :param int timeout: (optional) The maximum amount of time, in seconds, that
               can pass before the build must succeed or fail.
        """
        self.output_image = output_image
        self.output_secret = output_secret
        self.source_context_dir = source_context_dir
        self.source_revision = source_revision
        self.source_secret = source_secret
        self.source_type = source_type
        self.source_url = source_url
        self.strategy_size = strategy_size
        self.strategy_spec_file = strategy_spec_file
        self.strategy_type = strategy_type
        self.timeout = timeout

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BuildPatch':
        """Initialize a BuildPatch object from a json dictionary."""
        args = {}
        if 'output_image' in _dict:
            args['output_image'] = _dict.get('output_image')
        if 'output_secret' in _dict:
            args['output_secret'] = _dict.get('output_secret')
        if 'source_context_dir' in _dict:
            args['source_context_dir'] = _dict.get('source_context_dir')
        if 'source_revision' in _dict:
            args['source_revision'] = _dict.get('source_revision')
        if 'source_secret' in _dict:
            args['source_secret'] = _dict.get('source_secret')
        if 'source_type' in _dict:
            args['source_type'] = _dict.get('source_type')
        if 'source_url' in _dict:
            args['source_url'] = _dict.get('source_url')
        if 'strategy_size' in _dict:
            args['strategy_size'] = _dict.get('strategy_size')
        if 'strategy_spec_file' in _dict:
            args['strategy_spec_file'] = _dict.get('strategy_spec_file')
        if 'strategy_type' in _dict:
            args['strategy_type'] = _dict.get('strategy_type')
        if 'timeout' in _dict:
            args['timeout'] = _dict.get('timeout')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BuildPatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'output_image') and self.output_image is not None:
            _dict['output_image'] = self.output_image
        if hasattr(self, 'output_secret') and self.output_secret is not None:
            _dict['output_secret'] = self.output_secret
        if hasattr(self, 'source_context_dir') and self.source_context_dir is not None:
            _dict['source_context_dir'] = self.source_context_dir
        if hasattr(self, 'source_revision') and self.source_revision is not None:
            _dict['source_revision'] = self.source_revision
        if hasattr(self, 'source_secret') and self.source_secret is not None:
            _dict['source_secret'] = self.source_secret
        if hasattr(self, 'source_type') and self.source_type is not None:
            _dict['source_type'] = self.source_type
        if hasattr(self, 'source_url') and self.source_url is not None:
            _dict['source_url'] = self.source_url
        if hasattr(self, 'strategy_size') and self.strategy_size is not None:
            _dict['strategy_size'] = self.strategy_size
        if hasattr(self, 'strategy_spec_file') and self.strategy_spec_file is not None:
            _dict['strategy_spec_file'] = self.strategy_spec_file
        if hasattr(self, 'strategy_type') and self.strategy_type is not None:
            _dict['strategy_type'] = self.strategy_type
        if hasattr(self, 'timeout') and self.timeout is not None:
            _dict['timeout'] = self.timeout
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BuildPatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BuildPatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BuildPatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class SourceTypeEnum(str, Enum):
        """
        Specifies the type of source to determine if your build source is in a repository
        or based on local source code.
        * local - For builds from local source code.
        * git - For builds from git version controlled source code.
        """

        LOCAL = 'local'
        GIT = 'git'


class BuildRun:
    """
    Response model for build run objects.

    :attr str build_name: Optional name of the build on which this build run is
          based on. If specified, the build run will inherit the configuration of the
          referenced build. If not specified, make sure to specify at least the fields
          `strategy_type`, `source_url`, `output_image` and `output_secret` to describe
          the build run.
    :attr str created_at: The date when the resource was created.
    :attr str href: (optional) When you trigger a new build run,  a URL is created
          identifying the location of the instance.
    :attr str id: The identifier of the resource.
    :attr str name: The name of the build run.
    :attr str output_image: (optional) The name of the image.
    :attr str output_secret: (optional) The secret that is required to access the
          image registry. Make sure that the secret is granted with push permissions
          towards the specified container registry namespace.
    :attr str project_id: The ID of the project the resource is located in.
    :attr str resource_type: The type of the build run.
    :attr str service_account: (optional) Optional service account which is used for
          resource control.
    :attr str source_context_dir: (optional) Option directory in the repository that
          contains the buildpacks file or the Dockerfile.
    :attr str source_revision: (optional) Commit, tag, or branch in the source
          repository to pull. This field is optional if the `source_type` is `git` and
          uses the HEAD of default branch if not specified. If the `source_type` value is
          `local`, this field must be omitted.
    :attr str source_secret: (optional) Name of the secret that is used access the
          repository source. This field is optional if the `source_type` is `git`.
          Additionally, if the `source_url` points to a repository that requires
          authentication, the build will be created but cannot access any source code,
          until this property is provided, too. If the `source_type` value is `local`,
          this field must be omitted.
    :attr str source_type: (optional) Specifies the type of source to determine if
          your build source is in a repository or based on local source code.
          * local - For builds from local source code.
          * git - For builds from git version controlled source code.
    :attr str source_url: (optional) The URL of the code repository. This field is
          required if the `source_type` is `git`. If the `source_type` value is `local`,
          this field must be omitted. If the repository is publicly available you can
          provide a 'https' URL like `https://github.com/IBM/CodeEngine`. If the
          repository requires authentication, you need to provide a 'ssh' URL like
          `git@github.com:IBM/CodeEngine.git` along with a `source_secret` that points to
          a secret of format `ssh_auth`.
    :attr str status: The current status of the build run.
    :attr BuildRunStatus status_details: (optional) Current status condition of a
          build run.
    :attr str strategy_size: (optional) Optional size for the build, which
          determines the amount of resources used. Build sizes are `small`, `medium`,
          `large`, `xlarge`.
    :attr str strategy_spec_file: (optional) Optional path to the specification file
          that is used for build strategies for building an image.
    :attr str strategy_type: (optional) The strategy to use for building the image.
    :attr int timeout: (optional) The maximum amount of time, in seconds, that can
          pass before the build must succeed or fail.
    """

    def __init__(
        self,
        build_name: str,
        created_at: str,
        id: str,
        name: str,
        project_id: str,
        resource_type: str,
        status: str,
        *,
        href: str = None,
        output_image: str = None,
        output_secret: str = None,
        service_account: str = None,
        source_context_dir: str = None,
        source_revision: str = None,
        source_secret: str = None,
        source_type: str = None,
        source_url: str = None,
        status_details: 'BuildRunStatus' = None,
        strategy_size: str = None,
        strategy_spec_file: str = None,
        strategy_type: str = None,
        timeout: int = None,
    ) -> None:
        """
        Initialize a BuildRun object.

        :param str build_name: Optional name of the build on which this build run
               is based on. If specified, the build run will inherit the configuration of
               the referenced build. If not specified, make sure to specify at least the
               fields `strategy_type`, `source_url`, `output_image` and `output_secret` to
               describe the build run.
        :param str created_at: The date when the resource was created.
        :param str id: The identifier of the resource.
        :param str name: The name of the build run.
        :param str project_id: The ID of the project the resource is located in.
        :param str resource_type: The type of the build run.
        :param str status: The current status of the build run.
        :param str href: (optional) When you trigger a new build run,  a URL is
               created identifying the location of the instance.
        :param str output_image: (optional) The name of the image.
        :param str output_secret: (optional) The secret that is required to access
               the image registry. Make sure that the secret is granted with push
               permissions towards the specified container registry namespace.
        :param str service_account: (optional) Optional service account which is
               used for resource control.
        :param str source_context_dir: (optional) Option directory in the
               repository that contains the buildpacks file or the Dockerfile.
        :param str source_revision: (optional) Commit, tag, or branch in the source
               repository to pull. This field is optional if the `source_type` is `git`
               and uses the HEAD of default branch if not specified. If the `source_type`
               value is `local`, this field must be omitted.
        :param str source_secret: (optional) Name of the secret that is used access
               the repository source. This field is optional if the `source_type` is
               `git`. Additionally, if the `source_url` points to a repository that
               requires authentication, the build will be created but cannot access any
               source code, until this property is provided, too. If the `source_type`
               value is `local`, this field must be omitted.
        :param str source_type: (optional) Specifies the type of source to
               determine if your build source is in a repository or based on local source
               code.
               * local - For builds from local source code.
               * git - For builds from git version controlled source code.
        :param str source_url: (optional) The URL of the code repository. This
               field is required if the `source_type` is `git`. If the `source_type` value
               is `local`, this field must be omitted. If the repository is publicly
               available you can provide a 'https' URL like
               `https://github.com/IBM/CodeEngine`. If the repository requires
               authentication, you need to provide a 'ssh' URL like
               `git@github.com:IBM/CodeEngine.git` along with a `source_secret` that
               points to a secret of format `ssh_auth`.
        :param BuildRunStatus status_details: (optional) Current status condition
               of a build run.
        :param str strategy_size: (optional) Optional size for the build, which
               determines the amount of resources used. Build sizes are `small`, `medium`,
               `large`, `xlarge`.
        :param str strategy_spec_file: (optional) Optional path to the
               specification file that is used for build strategies for building an image.
        :param str strategy_type: (optional) The strategy to use for building the
               image.
        :param int timeout: (optional) The maximum amount of time, in seconds, that
               can pass before the build must succeed or fail.
        """
        self.build_name = build_name
        self.created_at = created_at
        self.href = href
        self.id = id
        self.name = name
        self.output_image = output_image
        self.output_secret = output_secret
        self.project_id = project_id
        self.resource_type = resource_type
        self.service_account = service_account
        self.source_context_dir = source_context_dir
        self.source_revision = source_revision
        self.source_secret = source_secret
        self.source_type = source_type
        self.source_url = source_url
        self.status = status
        self.status_details = status_details
        self.strategy_size = strategy_size
        self.strategy_spec_file = strategy_spec_file
        self.strategy_type = strategy_type
        self.timeout = timeout

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BuildRun':
        """Initialize a BuildRun object from a json dictionary."""
        args = {}
        if 'build_name' in _dict:
            args['build_name'] = _dict.get('build_name')
        else:
            raise ValueError('Required property \'build_name\' not present in BuildRun JSON')
        if 'created_at' in _dict:
            args['created_at'] = _dict.get('created_at')
        else:
            raise ValueError('Required property \'created_at\' not present in BuildRun JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in BuildRun JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in BuildRun JSON')
        if 'output_image' in _dict:
            args['output_image'] = _dict.get('output_image')
        if 'output_secret' in _dict:
            args['output_secret'] = _dict.get('output_secret')
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        else:
            raise ValueError('Required property \'project_id\' not present in BuildRun JSON')
        if 'resource_type' in _dict:
            args['resource_type'] = _dict.get('resource_type')
        else:
            raise ValueError('Required property \'resource_type\' not present in BuildRun JSON')
        if 'service_account' in _dict:
            args['service_account'] = _dict.get('service_account')
        if 'source_context_dir' in _dict:
            args['source_context_dir'] = _dict.get('source_context_dir')
        if 'source_revision' in _dict:
            args['source_revision'] = _dict.get('source_revision')
        if 'source_secret' in _dict:
            args['source_secret'] = _dict.get('source_secret')
        if 'source_type' in _dict:
            args['source_type'] = _dict.get('source_type')
        if 'source_url' in _dict:
            args['source_url'] = _dict.get('source_url')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in BuildRun JSON')
        if 'status_details' in _dict:
            args['status_details'] = BuildRunStatus.from_dict(_dict.get('status_details'))
        if 'strategy_size' in _dict:
            args['strategy_size'] = _dict.get('strategy_size')
        if 'strategy_spec_file' in _dict:
            args['strategy_spec_file'] = _dict.get('strategy_spec_file')
        if 'strategy_type' in _dict:
            args['strategy_type'] = _dict.get('strategy_type')
        if 'timeout' in _dict:
            args['timeout'] = _dict.get('timeout')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BuildRun object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'build_name') and self.build_name is not None:
            _dict['build_name'] = self.build_name
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = self.created_at
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'output_image') and self.output_image is not None:
            _dict['output_image'] = self.output_image
        if hasattr(self, 'output_secret') and self.output_secret is not None:
            _dict['output_secret'] = self.output_secret
        if hasattr(self, 'project_id') and self.project_id is not None:
            _dict['project_id'] = self.project_id
        if hasattr(self, 'resource_type') and self.resource_type is not None:
            _dict['resource_type'] = self.resource_type
        if hasattr(self, 'service_account') and self.service_account is not None:
            _dict['service_account'] = self.service_account
        if hasattr(self, 'source_context_dir') and self.source_context_dir is not None:
            _dict['source_context_dir'] = self.source_context_dir
        if hasattr(self, 'source_revision') and self.source_revision is not None:
            _dict['source_revision'] = self.source_revision
        if hasattr(self, 'source_secret') and self.source_secret is not None:
            _dict['source_secret'] = self.source_secret
        if hasattr(self, 'source_type') and self.source_type is not None:
            _dict['source_type'] = self.source_type
        if hasattr(self, 'source_url') and self.source_url is not None:
            _dict['source_url'] = self.source_url
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'status_details') and self.status_details is not None:
            if isinstance(self.status_details, dict):
                _dict['status_details'] = self.status_details
            else:
                _dict['status_details'] = self.status_details.to_dict()
        if hasattr(self, 'strategy_size') and self.strategy_size is not None:
            _dict['strategy_size'] = self.strategy_size
        if hasattr(self, 'strategy_spec_file') and self.strategy_spec_file is not None:
            _dict['strategy_spec_file'] = self.strategy_spec_file
        if hasattr(self, 'strategy_type') and self.strategy_type is not None:
            _dict['strategy_type'] = self.strategy_type
        if hasattr(self, 'timeout') and self.timeout is not None:
            _dict['timeout'] = self.timeout
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BuildRun object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BuildRun') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BuildRun') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ResourceTypeEnum(str, Enum):
        """
        The type of the build run.
        """

        BUILD_RUN_V2 = 'build_run_v2'

    class ServiceAccountEnum(str, Enum):
        """
        Optional service account which is used for resource control.
        """

        DEFAULT = 'default'
        MANAGER = 'manager'
        READER = 'reader'
        WRITER = 'writer'
        NONE = 'none'

    class SourceTypeEnum(str, Enum):
        """
        Specifies the type of source to determine if your build source is in a repository
        or based on local source code.
        * local - For builds from local source code.
        * git - For builds from git version controlled source code.
        """

        LOCAL = 'local'
        GIT = 'git'

    class StatusEnum(str, Enum):
        """
        The current status of the build run.
        """

        SUCCEEDED = 'succeeded'
        RUNNING = 'running'
        PENDING = 'pending'
        FAILED = 'failed'


class BuildRunList:
    """
    Contains a list of build runs and pagination information.

    :attr List[BuildRun] build_runs: List of all build runs.
    :attr ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :attr int limit: Maximum number of resources per page.
    :attr ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    """

    def __init__(
        self,
        build_runs: List['BuildRun'],
        limit: int,
        *,
        first: 'ListFirstMetadata' = None,
        next: 'ListNextMetadata' = None,
    ) -> None:
        """
        Initialize a BuildRunList object.

        :param List[BuildRun] build_runs: List of all build runs.
        :param int limit: Maximum number of resources per page.
        :param ListFirstMetadata first: (optional) Describes properties needed to
               retrieve the first page of a result list.
        :param ListNextMetadata next: (optional) Describes properties needed to
               retrieve the next page of a result list.
        """
        self.build_runs = build_runs
        self.first = first
        self.limit = limit
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BuildRunList':
        """Initialize a BuildRunList object from a json dictionary."""
        args = {}
        if 'build_runs' in _dict:
            args['build_runs'] = [BuildRun.from_dict(v) for v in _dict.get('build_runs')]
        else:
            raise ValueError('Required property \'build_runs\' not present in BuildRunList JSON')
        if 'first' in _dict:
            args['first'] = ListFirstMetadata.from_dict(_dict.get('first'))
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in BuildRunList JSON')
        if 'next' in _dict:
            args['next'] = ListNextMetadata.from_dict(_dict.get('next'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BuildRunList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'build_runs') and self.build_runs is not None:
            build_runs_list = []
            for v in self.build_runs:
                if isinstance(v, dict):
                    build_runs_list.append(v)
                else:
                    build_runs_list.append(v.to_dict())
            _dict['build_runs'] = build_runs_list
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BuildRunList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BuildRunList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BuildRunList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BuildRunStatus:
    """
    Current status condition of a build run.

    :attr str completion_time: (optional) Time the build run completed.
    :attr str output_digest: (optional) Describes the time the build run completed.
    :attr str reason: (optional) Optional information to provide more context in
          case of a 'failed' or 'warning' status.
    :attr str start_time: (optional) Time the build run started.
    """

    def __init__(
        self, *, completion_time: str = None, output_digest: str = None, reason: str = None, start_time: str = None
    ) -> None:
        """
        Initialize a BuildRunStatus object.

        :param str completion_time: (optional) Time the build run completed.
        :param str output_digest: (optional) Describes the time the build run
               completed.
        :param str reason: (optional) Optional information to provide more context
               in case of a 'failed' or 'warning' status.
        :param str start_time: (optional) Time the build run started.
        """
        self.completion_time = completion_time
        self.output_digest = output_digest
        self.reason = reason
        self.start_time = start_time

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BuildRunStatus':
        """Initialize a BuildRunStatus object from a json dictionary."""
        args = {}
        if 'completion_time' in _dict:
            args['completion_time'] = _dict.get('completion_time')
        if 'output_digest' in _dict:
            args['output_digest'] = _dict.get('output_digest')
        if 'reason' in _dict:
            args['reason'] = _dict.get('reason')
        if 'start_time' in _dict:
            args['start_time'] = _dict.get('start_time')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BuildRunStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'completion_time') and self.completion_time is not None:
            _dict['completion_time'] = self.completion_time
        if hasattr(self, 'output_digest') and self.output_digest is not None:
            _dict['output_digest'] = self.output_digest
        if hasattr(self, 'reason') and self.reason is not None:
            _dict['reason'] = self.reason
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = self.start_time
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BuildRunStatus object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BuildRunStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BuildRunStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ReasonEnum(str, Enum):
        """
        Optional information to provide more context in case of a 'failed' or 'warning'
        status.
        """

        SUCCEEDED = 'succeeded'
        RUNNING = 'running'
        PENDING = 'pending'
        FAILED_TO_EXECUTE_BUILD_RUN = 'failed_to_execute_build_run'
        EXCEEDED_EPHEMERAL_STORAGE = 'exceeded_ephemeral_storage'
        MISSING_REGISTRY_ACCESS = 'missing_registry_access'
        MISSING_CODE_REPO_ACCESS = 'missing_code_repo_access'
        MISSING_SECRETS = 'missing_secrets'
        UNKNOWN_STRATEGY = 'unknown_strategy'
        INVALID_BUILD_CONFIGURATION = 'invalid_build_configuration'
        POD_EVICTED_BECAUSE_OF_STORAGE_QUOTA_EXCEEDS = 'pod_evicted_because_of_storage_quota_exceeds'
        POD_EVICTED = 'pod_evicted'
        MISSING_TASK_RUN = 'missing_task_run'
        TASK_RUN_GENERATION_FAILED = 'task_run_generation_failed'
        BUILD_NOT_FOUND = 'build_not_found'
        TIMEOUT = 'timeout'
        FAILED = 'failed'


class BuildStatus:
    """
    The detailed status of the build.

    :attr str reason: (optional) Optional information to provide more context in
          case of a 'failed' or 'warning' status.
    """

    def __init__(self, *, reason: str = None) -> None:
        """
        Initialize a BuildStatus object.

        :param str reason: (optional) Optional information to provide more context
               in case of a 'failed' or 'warning' status.
        """
        self.reason = reason

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BuildStatus':
        """Initialize a BuildStatus object from a json dictionary."""
        args = {}
        if 'reason' in _dict:
            args['reason'] = _dict.get('reason')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BuildStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'reason') and self.reason is not None:
            _dict['reason'] = self.reason
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BuildStatus object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BuildStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BuildStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ReasonEnum(str, Enum):
        """
        Optional information to provide more context in case of a 'failed' or 'warning'
        status.
        """

        REGISTERED = 'registered'
        STRATEGY_NOT_FOUND = 'strategy_not_found'
        CLUSTER_BUILD_STRATEGY_NOT_FOUND = 'cluster_build_strategy_not_found'
        SET_OWNER_REFERENCE_FAILED = 'set_owner_reference_failed'
        SPEC_SOURCE_SECRET_NOT_FOUND = 'spec_source_secret_not_found'
        SPEC_OUTPUT_SECRET_REF_NOT_FOUND = 'spec_output_secret_ref_not_found'
        SPEC_RUNTIME_SECRET_REF_NOT_FOUND = 'spec_runtime_secret_ref_not_found'
        MULTIPLE_SECRET_REF_NOT_FOUND = 'multiple_secret_ref_not_found'
        RUNTIME_PATHS_CAN_NOT_BE_EMPTY = 'runtime_paths_can_not_be_empty'
        REMOTE_REPOSITORY_UNREACHABLE = 'remote_repository_unreachable'
        FAILED = 'failed'


class ConfigMap:
    """
    Describes the model of a configmap.

    :attr str created_at: The date when the resource was created.
    :attr dict data: (optional) The key-value pair for the config map. Values must
          be specified in `KEY=VALUE` format.
    :attr str entity_tag: The version of the config map instance, which is used to
          achieve optimistic locking.
    :attr str href: (optional) When you provision a new config map,  a URL is
          created identifying the location of the instance.
    :attr str id: The identifier of the resource.
    :attr str name: The name of the config map.
    :attr str project_id: The ID of the project the resource is located in.
    :attr str resource_type: The type of the config map.
    """

    def __init__(
        self,
        created_at: str,
        entity_tag: str,
        id: str,
        name: str,
        project_id: str,
        resource_type: str,
        *,
        data: dict = None,
        href: str = None,
    ) -> None:
        """
        Initialize a ConfigMap object.

        :param str created_at: The date when the resource was created.
        :param str entity_tag: The version of the config map instance, which is
               used to achieve optimistic locking.
        :param str id: The identifier of the resource.
        :param str name: The name of the config map.
        :param str project_id: The ID of the project the resource is located in.
        :param str resource_type: The type of the config map.
        :param dict data: (optional) The key-value pair for the config map. Values
               must be specified in `KEY=VALUE` format.
        :param str href: (optional) When you provision a new config map,  a URL is
               created identifying the location of the instance.
        """
        self.created_at = created_at
        self.data = data
        self.entity_tag = entity_tag
        self.href = href
        self.id = id
        self.name = name
        self.project_id = project_id
        self.resource_type = resource_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConfigMap':
        """Initialize a ConfigMap object from a json dictionary."""
        args = {}
        if 'created_at' in _dict:
            args['created_at'] = _dict.get('created_at')
        else:
            raise ValueError('Required property \'created_at\' not present in ConfigMap JSON')
        if 'data' in _dict:
            args['data'] = _dict.get('data')
        if 'entity_tag' in _dict:
            args['entity_tag'] = _dict.get('entity_tag')
        else:
            raise ValueError('Required property \'entity_tag\' not present in ConfigMap JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ConfigMap JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ConfigMap JSON')
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        else:
            raise ValueError('Required property \'project_id\' not present in ConfigMap JSON')
        if 'resource_type' in _dict:
            args['resource_type'] = _dict.get('resource_type')
        else:
            raise ValueError('Required property \'resource_type\' not present in ConfigMap JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConfigMap object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = self.created_at
        if hasattr(self, 'data') and self.data is not None:
            _dict['data'] = self.data
        if hasattr(self, 'entity_tag') and self.entity_tag is not None:
            _dict['entity_tag'] = self.entity_tag
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'project_id') and self.project_id is not None:
            _dict['project_id'] = self.project_id
        if hasattr(self, 'resource_type') and self.resource_type is not None:
            _dict['resource_type'] = self.resource_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConfigMap object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConfigMap') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConfigMap') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ResourceTypeEnum(str, Enum):
        """
        The type of the config map.
        """

        CONFIG_MAP_V2 = 'config_map_v2'


class ConfigMapList:
    """
    Contains a list of configmaps and pagination information.

    :attr List[ConfigMap] config_maps: List of all configmaps.
    :attr ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :attr int limit: Maximum number of resources per page.
    :attr ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    """

    def __init__(
        self,
        config_maps: List['ConfigMap'],
        limit: int,
        *,
        first: 'ListFirstMetadata' = None,
        next: 'ListNextMetadata' = None,
    ) -> None:
        """
        Initialize a ConfigMapList object.

        :param List[ConfigMap] config_maps: List of all configmaps.
        :param int limit: Maximum number of resources per page.
        :param ListFirstMetadata first: (optional) Describes properties needed to
               retrieve the first page of a result list.
        :param ListNextMetadata next: (optional) Describes properties needed to
               retrieve the next page of a result list.
        """
        self.config_maps = config_maps
        self.first = first
        self.limit = limit
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConfigMapList':
        """Initialize a ConfigMapList object from a json dictionary."""
        args = {}
        if 'config_maps' in _dict:
            args['config_maps'] = [ConfigMap.from_dict(v) for v in _dict.get('config_maps')]
        else:
            raise ValueError('Required property \'config_maps\' not present in ConfigMapList JSON')
        if 'first' in _dict:
            args['first'] = ListFirstMetadata.from_dict(_dict.get('first'))
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ConfigMapList JSON')
        if 'next' in _dict:
            args['next'] = ListNextMetadata.from_dict(_dict.get('next'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConfigMapList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'config_maps') and self.config_maps is not None:
            config_maps_list = []
            for v in self.config_maps:
                if isinstance(v, dict):
                    config_maps_list.append(v)
                else:
                    config_maps_list.append(v.to_dict())
            _dict['config_maps'] = config_maps_list
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConfigMapList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConfigMapList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConfigMapList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EnvVar:
    """
    Response model for environment variables.

    :attr str key: (optional) The key to reference as environment variable.
    :attr str name: (optional) The name of the environment variable.
    :attr str prefix: (optional) A prefix that can be added to all keys of a full
          secret or config map reference.
    :attr str reference: (optional) The name of the secret or config map.
    :attr str type: Specify the type of the environment variable.
    :attr str value: (optional) The literal value of the environment variable.
    """

    def __init__(
        self,
        type: str,
        *,
        key: str = None,
        name: str = None,
        prefix: str = None,
        reference: str = None,
        value: str = None,
    ) -> None:
        """
        Initialize a EnvVar object.

        :param str type: Specify the type of the environment variable.
        :param str key: (optional) The key to reference as environment variable.
        :param str name: (optional) The name of the environment variable.
        :param str prefix: (optional) A prefix that can be added to all keys of a
               full secret or config map reference.
        :param str reference: (optional) The name of the secret or config map.
        :param str value: (optional) The literal value of the environment variable.
        """
        self.key = key
        self.name = name
        self.prefix = prefix
        self.reference = reference
        self.type = type
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnvVar':
        """Initialize a EnvVar object from a json dictionary."""
        args = {}
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'prefix' in _dict:
            args['prefix'] = _dict.get('prefix')
        if 'reference' in _dict:
            args['reference'] = _dict.get('reference')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in EnvVar JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnvVar object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'prefix') and self.prefix is not None:
            _dict['prefix'] = self.prefix
        if hasattr(self, 'reference') and self.reference is not None:
            _dict['reference'] = self.reference
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EnvVar object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnvVar') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnvVar') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Specify the type of the environment variable.
        """

        LITERAL = 'literal'
        CONFIG_MAP_FULL_REFERENCE = 'config_map_full_reference'
        SECRET_FULL_REFERENCE = 'secret_full_reference'
        CONFIG_MAP_KEY_REFERENCE = 'config_map_key_reference'
        SECRET_KEY_REFERENCE = 'secret_key_reference'


class EnvVarPrototype:
    """
    Prototype model for environment variables.

    :attr str key: (optional) The key to reference as environment variable.
    :attr str name: (optional) The name of the environment variable.
    :attr str prefix: (optional) A prefix that can be added to all keys of a full
          secret or config map reference.
    :attr str reference: (optional) The name of the secret or config map.
    :attr str type: (optional) Specify the type of the environment variable.
    :attr str value: (optional) The literal value of the environment variable.
    """

    def __init__(
        self,
        *,
        key: str = None,
        name: str = None,
        prefix: str = None,
        reference: str = None,
        type: str = None,
        value: str = None,
    ) -> None:
        """
        Initialize a EnvVarPrototype object.

        :param str key: (optional) The key to reference as environment variable.
        :param str name: (optional) The name of the environment variable.
        :param str prefix: (optional) A prefix that can be added to all keys of a
               full secret or config map reference.
        :param str reference: (optional) The name of the secret or config map.
        :param str type: (optional) Specify the type of the environment variable.
        :param str value: (optional) The literal value of the environment variable.
        """
        self.key = key
        self.name = name
        self.prefix = prefix
        self.reference = reference
        self.type = type
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnvVarPrototype':
        """Initialize a EnvVarPrototype object from a json dictionary."""
        args = {}
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'prefix' in _dict:
            args['prefix'] = _dict.get('prefix')
        if 'reference' in _dict:
            args['reference'] = _dict.get('reference')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnvVarPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'prefix') and self.prefix is not None:
            _dict['prefix'] = self.prefix
        if hasattr(self, 'reference') and self.reference is not None:
            _dict['reference'] = self.reference
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EnvVarPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnvVarPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnvVarPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Specify the type of the environment variable.
        """

        LITERAL = 'literal'
        CONFIG_MAP_FULL_REFERENCE = 'config_map_full_reference'
        SECRET_FULL_REFERENCE = 'secret_full_reference'
        CONFIG_MAP_KEY_REFERENCE = 'config_map_key_reference'
        SECRET_KEY_REFERENCE = 'secret_key_reference'


class Job:
    """
    Job is the response model for job resources.

    :attr str created_at: The date when the resource was created.
    :attr str entity_tag: The version of the job instance, which is used to achieve
          optimistic locking.
    :attr str href: When you provision a new job,  a URL is created identifying the
          location of the instance.
    :attr str id: The identifier of the resource.
    :attr str image_reference: The name of the image that is used for this job. The
          format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and `TAG` are
          optional. If `REGISTRY` is not specified, the default is `docker.io`. If `TAG`
          is not specified, the default is `latest`. If the image reference points to a
          registry that requires authentication, make sure to also specify the property
          `image_secret`.
    :attr str image_secret: (optional) The name of the image registry access secret.
          The image registry access secret is used to authenticate with a private registry
          when you download the container image. If the image reference points to a
          registry that requires authentication, the job / job runs will be created but
          submitted job runs will fail, until this property is provided, too.
    :attr str name: The name of the job.
    :attr str project_id: The ID of the project the resource is located in.
    :attr str resource_type: The type of the job.
    :attr List[str] run_arguments: Set arguments for the job that are passed to
          start job run containers. If not specified an empty string array will be applied
          and the arguments specified by the container image, will be used to start the
          container.
    :attr int run_as_user: (optional) The user ID (UID) to run the application
          (e.g., 1001).
    :attr List[str] run_commands: Set commands for the job that are passed to start
          job run containers. If not specified an empty string array will be applied and
          the command specified by the container image, will be used to start the
          container.
    :attr List[EnvVar] run_env_variables: References to config maps, secrets or a
          literal values, which are exposed as environment variables in the job run.
    :attr str run_mode: The mode for runs of the job. Valid values are `task` and
          `daemon`. In `task` mode, the `max_execution_time` and `retry_limit` options
          apply. In `daemon` mode, since there is no timeout and failed instances are
          restarted indefinitely, the `max_execution_time` and `retry_limit` options are
          not allowed.
    :attr str run_service_account: (optional) The name of the service account. For
          built-in service accounts, you can use the shortened names `manager`, `none`,
          `reader`, and `writer`.
    :attr List[VolumeMount] run_volume_mounts: Optional mounts of config maps or a
          secrets.
    :attr str scale_array_spec: Define a custom set of array indices as
          comma-separated list containing single values and hyphen-separated ranges like
          `5,12-14,23,27`. Each instance can pick up its array index via environment
          variable `JOB_INDEX`. The number of unique array indices specified here
          determines the number of job instances to run.
    :attr str scale_cpu_limit: Optional amount of CPU set for the instance of the
          job. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
    :attr str scale_ephemeral_storage_limit: Optional amount of ephemeral storage to
          set for the instance of the job. The amount specified as ephemeral storage, must
          not exceed the amount of `scale_memory_limit`. The units for specifying
          ephemeral storage are Megabyte (M) or Gigabyte (G), whereas G and M are the
          shorthand expressions for GB and MB. For more information see [Units of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :attr int scale_max_execution_time: (optional) The maximum execution time in
          seconds for runs of the job. This option can only be specified if `mode` is
          `task`.
    :attr str scale_memory_limit: Optional amount of memory set for the instance of
          the job. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
          The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and
          M are the shorthand expressions for GB and MB. For more information see [Units
          of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :attr int scale_retry_limit: (optional) The number of times to rerun an instance
          of the job before the job is marked as failed. This option can only be specified
          if `mode` is `task`.
    """

    def __init__(
        self,
        created_at: str,
        entity_tag: str,
        href: str,
        id: str,
        image_reference: str,
        name: str,
        project_id: str,
        resource_type: str,
        run_arguments: List[str],
        run_commands: List[str],
        run_env_variables: List['EnvVar'],
        run_mode: str,
        run_volume_mounts: List['VolumeMount'],
        scale_array_spec: str,
        scale_cpu_limit: str,
        scale_ephemeral_storage_limit: str,
        scale_memory_limit: str,
        *,
        image_secret: str = None,
        run_as_user: int = None,
        run_service_account: str = None,
        scale_max_execution_time: int = None,
        scale_retry_limit: int = None,
    ) -> None:
        """
        Initialize a Job object.

        :param str created_at: The date when the resource was created.
        :param str entity_tag: The version of the job instance, which is used to
               achieve optimistic locking.
        :param str href: When you provision a new job,  a URL is created
               identifying the location of the instance.
        :param str id: The identifier of the resource.
        :param str image_reference: The name of the image that is used for this
               job. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and
               `TAG` are optional. If `REGISTRY` is not specified, the default is
               `docker.io`. If `TAG` is not specified, the default is `latest`. If the
               image reference points to a registry that requires authentication, make
               sure to also specify the property `image_secret`.
        :param str name: The name of the job.
        :param str project_id: The ID of the project the resource is located in.
        :param str resource_type: The type of the job.
        :param List[str] run_arguments: Set arguments for the job that are passed
               to start job run containers. If not specified an empty string array will be
               applied and the arguments specified by the container image, will be used to
               start the container.
        :param List[str] run_commands: Set commands for the job that are passed to
               start job run containers. If not specified an empty string array will be
               applied and the command specified by the container image, will be used to
               start the container.
        :param List[EnvVar] run_env_variables: References to config maps, secrets
               or a literal values, which are exposed as environment variables in the job
               run.
        :param str run_mode: The mode for runs of the job. Valid values are `task`
               and `daemon`. In `task` mode, the `max_execution_time` and `retry_limit`
               options apply. In `daemon` mode, since there is no timeout and failed
               instances are restarted indefinitely, the `max_execution_time` and
               `retry_limit` options are not allowed.
        :param List[VolumeMount] run_volume_mounts: Optional mounts of config maps
               or a secrets.
        :param str scale_array_spec: Define a custom set of array indices as
               comma-separated list containing single values and hyphen-separated ranges
               like `5,12-14,23,27`. Each instance can pick up its array index via
               environment variable `JOB_INDEX`. The number of unique array indices
               specified here determines the number of job instances to run.
        :param str scale_cpu_limit: Optional amount of CPU set for the instance of
               the job. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
        :param str scale_ephemeral_storage_limit: Optional amount of ephemeral
               storage to set for the instance of the job. The amount specified as
               ephemeral storage, must not exceed the amount of `scale_memory_limit`. The
               units for specifying ephemeral storage are Megabyte (M) or Gigabyte (G),
               whereas G and M are the shorthand expressions for GB and MB. For more
               information see [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param str scale_memory_limit: Optional amount of memory set for the
               instance of the job. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
               The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G
               and M are the shorthand expressions for GB and MB. For more information see
               [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param str image_secret: (optional) The name of the image registry access
               secret. The image registry access secret is used to authenticate with a
               private registry when you download the container image. If the image
               reference points to a registry that requires authentication, the job / job
               runs will be created but submitted job runs will fail, until this property
               is provided, too.
        :param int run_as_user: (optional) The user ID (UID) to run the application
               (e.g., 1001).
        :param str run_service_account: (optional) The name of the service account.
               For built-in service accounts, you can use the shortened names `manager`,
               `none`, `reader`, and `writer`.
        :param int scale_max_execution_time: (optional) The maximum execution time
               in seconds for runs of the job. This option can only be specified if `mode`
               is `task`.
        :param int scale_retry_limit: (optional) The number of times to rerun an
               instance of the job before the job is marked as failed. This option can
               only be specified if `mode` is `task`.
        """
        self.created_at = created_at
        self.entity_tag = entity_tag
        self.href = href
        self.id = id
        self.image_reference = image_reference
        self.image_secret = image_secret
        self.name = name
        self.project_id = project_id
        self.resource_type = resource_type
        self.run_arguments = run_arguments
        self.run_as_user = run_as_user
        self.run_commands = run_commands
        self.run_env_variables = run_env_variables
        self.run_mode = run_mode
        self.run_service_account = run_service_account
        self.run_volume_mounts = run_volume_mounts
        self.scale_array_spec = scale_array_spec
        self.scale_cpu_limit = scale_cpu_limit
        self.scale_ephemeral_storage_limit = scale_ephemeral_storage_limit
        self.scale_max_execution_time = scale_max_execution_time
        self.scale_memory_limit = scale_memory_limit
        self.scale_retry_limit = scale_retry_limit

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Job':
        """Initialize a Job object from a json dictionary."""
        args = {}
        if 'created_at' in _dict:
            args['created_at'] = _dict.get('created_at')
        else:
            raise ValueError('Required property \'created_at\' not present in Job JSON')
        if 'entity_tag' in _dict:
            args['entity_tag'] = _dict.get('entity_tag')
        else:
            raise ValueError('Required property \'entity_tag\' not present in Job JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in Job JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Job JSON')
        if 'image_reference' in _dict:
            args['image_reference'] = _dict.get('image_reference')
        else:
            raise ValueError('Required property \'image_reference\' not present in Job JSON')
        if 'image_secret' in _dict:
            args['image_secret'] = _dict.get('image_secret')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in Job JSON')
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        else:
            raise ValueError('Required property \'project_id\' not present in Job JSON')
        if 'resource_type' in _dict:
            args['resource_type'] = _dict.get('resource_type')
        else:
            raise ValueError('Required property \'resource_type\' not present in Job JSON')
        if 'run_arguments' in _dict:
            args['run_arguments'] = _dict.get('run_arguments')
        else:
            raise ValueError('Required property \'run_arguments\' not present in Job JSON')
        if 'run_as_user' in _dict:
            args['run_as_user'] = _dict.get('run_as_user')
        if 'run_commands' in _dict:
            args['run_commands'] = _dict.get('run_commands')
        else:
            raise ValueError('Required property \'run_commands\' not present in Job JSON')
        if 'run_env_variables' in _dict:
            args['run_env_variables'] = [EnvVar.from_dict(v) for v in _dict.get('run_env_variables')]
        else:
            raise ValueError('Required property \'run_env_variables\' not present in Job JSON')
        if 'run_mode' in _dict:
            args['run_mode'] = _dict.get('run_mode')
        else:
            raise ValueError('Required property \'run_mode\' not present in Job JSON')
        if 'run_service_account' in _dict:
            args['run_service_account'] = _dict.get('run_service_account')
        if 'run_volume_mounts' in _dict:
            args['run_volume_mounts'] = [VolumeMount.from_dict(v) for v in _dict.get('run_volume_mounts')]
        else:
            raise ValueError('Required property \'run_volume_mounts\' not present in Job JSON')
        if 'scale_array_spec' in _dict:
            args['scale_array_spec'] = _dict.get('scale_array_spec')
        else:
            raise ValueError('Required property \'scale_array_spec\' not present in Job JSON')
        if 'scale_cpu_limit' in _dict:
            args['scale_cpu_limit'] = _dict.get('scale_cpu_limit')
        else:
            raise ValueError('Required property \'scale_cpu_limit\' not present in Job JSON')
        if 'scale_ephemeral_storage_limit' in _dict:
            args['scale_ephemeral_storage_limit'] = _dict.get('scale_ephemeral_storage_limit')
        else:
            raise ValueError('Required property \'scale_ephemeral_storage_limit\' not present in Job JSON')
        if 'scale_max_execution_time' in _dict:
            args['scale_max_execution_time'] = _dict.get('scale_max_execution_time')
        if 'scale_memory_limit' in _dict:
            args['scale_memory_limit'] = _dict.get('scale_memory_limit')
        else:
            raise ValueError('Required property \'scale_memory_limit\' not present in Job JSON')
        if 'scale_retry_limit' in _dict:
            args['scale_retry_limit'] = _dict.get('scale_retry_limit')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Job object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = self.created_at
        if hasattr(self, 'entity_tag') and self.entity_tag is not None:
            _dict['entity_tag'] = self.entity_tag
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'image_reference') and self.image_reference is not None:
            _dict['image_reference'] = self.image_reference
        if hasattr(self, 'image_secret') and self.image_secret is not None:
            _dict['image_secret'] = self.image_secret
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'project_id') and self.project_id is not None:
            _dict['project_id'] = self.project_id
        if hasattr(self, 'resource_type') and self.resource_type is not None:
            _dict['resource_type'] = self.resource_type
        if hasattr(self, 'run_arguments') and self.run_arguments is not None:
            _dict['run_arguments'] = self.run_arguments
        if hasattr(self, 'run_as_user') and self.run_as_user is not None:
            _dict['run_as_user'] = self.run_as_user
        if hasattr(self, 'run_commands') and self.run_commands is not None:
            _dict['run_commands'] = self.run_commands
        if hasattr(self, 'run_env_variables') and self.run_env_variables is not None:
            run_env_variables_list = []
            for v in self.run_env_variables:
                if isinstance(v, dict):
                    run_env_variables_list.append(v)
                else:
                    run_env_variables_list.append(v.to_dict())
            _dict['run_env_variables'] = run_env_variables_list
        if hasattr(self, 'run_mode') and self.run_mode is not None:
            _dict['run_mode'] = self.run_mode
        if hasattr(self, 'run_service_account') and self.run_service_account is not None:
            _dict['run_service_account'] = self.run_service_account
        if hasattr(self, 'run_volume_mounts') and self.run_volume_mounts is not None:
            run_volume_mounts_list = []
            for v in self.run_volume_mounts:
                if isinstance(v, dict):
                    run_volume_mounts_list.append(v)
                else:
                    run_volume_mounts_list.append(v.to_dict())
            _dict['run_volume_mounts'] = run_volume_mounts_list
        if hasattr(self, 'scale_array_spec') and self.scale_array_spec is not None:
            _dict['scale_array_spec'] = self.scale_array_spec
        if hasattr(self, 'scale_cpu_limit') and self.scale_cpu_limit is not None:
            _dict['scale_cpu_limit'] = self.scale_cpu_limit
        if hasattr(self, 'scale_ephemeral_storage_limit') and self.scale_ephemeral_storage_limit is not None:
            _dict['scale_ephemeral_storage_limit'] = self.scale_ephemeral_storage_limit
        if hasattr(self, 'scale_max_execution_time') and self.scale_max_execution_time is not None:
            _dict['scale_max_execution_time'] = self.scale_max_execution_time
        if hasattr(self, 'scale_memory_limit') and self.scale_memory_limit is not None:
            _dict['scale_memory_limit'] = self.scale_memory_limit
        if hasattr(self, 'scale_retry_limit') and self.scale_retry_limit is not None:
            _dict['scale_retry_limit'] = self.scale_retry_limit
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Job object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Job') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Job') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ResourceTypeEnum(str, Enum):
        """
        The type of the job.
        """

        JOB_V2 = 'job_v2'

    class RunModeEnum(str, Enum):
        """
        The mode for runs of the job. Valid values are `task` and `daemon`. In `task`
        mode, the `max_execution_time` and `retry_limit` options apply. In `daemon` mode,
        since there is no timeout and failed instances are restarted indefinitely, the
        `max_execution_time` and `retry_limit` options are not allowed.
        """

        TASK = 'task'
        DAEMON = 'daemon'

    class RunServiceAccountEnum(str, Enum):
        """
        The name of the service account. For built-in service accounts, you can use the
        shortened names `manager`, `none`, `reader`, and `writer`.
        """

        DEFAULT = 'default'
        MANAGER = 'manager'
        READER = 'reader'
        WRITER = 'writer'
        NONE = 'none'


class JobList:
    """
    Contains a list of jobs and pagination information.

    :attr ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :attr List[Job] jobs: List of all jobs.
    :attr int limit: Maximum number of resources per page.
    :attr ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    """

    def __init__(
        self, jobs: List['Job'], limit: int, *, first: 'ListFirstMetadata' = None, next: 'ListNextMetadata' = None
    ) -> None:
        """
        Initialize a JobList object.

        :param List[Job] jobs: List of all jobs.
        :param int limit: Maximum number of resources per page.
        :param ListFirstMetadata first: (optional) Describes properties needed to
               retrieve the first page of a result list.
        :param ListNextMetadata next: (optional) Describes properties needed to
               retrieve the next page of a result list.
        """
        self.first = first
        self.jobs = jobs
        self.limit = limit
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'JobList':
        """Initialize a JobList object from a json dictionary."""
        args = {}
        if 'first' in _dict:
            args['first'] = ListFirstMetadata.from_dict(_dict.get('first'))
        if 'jobs' in _dict:
            args['jobs'] = [Job.from_dict(v) for v in _dict.get('jobs')]
        else:
            raise ValueError('Required property \'jobs\' not present in JobList JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in JobList JSON')
        if 'next' in _dict:
            args['next'] = ListNextMetadata.from_dict(_dict.get('next'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a JobList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'jobs') and self.jobs is not None:
            jobs_list = []
            for v in self.jobs:
                if isinstance(v, dict):
                    jobs_list.append(v)
                else:
                    jobs_list.append(v.to_dict())
            _dict['jobs'] = jobs_list
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this JobList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'JobList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'JobList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class JobPatch:
    """
    Request model for job update operations.

    :attr str image_reference: (optional) The name of the image that is used for
          this job. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and
          `TAG` are optional. If `REGISTRY` is not specified, the default is `docker.io`.
          If `TAG` is not specified, the default is `latest`. If the image reference
          points to a registry that requires authentication, make sure to also specify the
          property `image_secret`.
    :attr str image_secret: (optional) The name of the image registry access secret.
          The image registry access secret is used to authenticate with a private registry
          when you download the container image. If the image reference points to a
          registry that requires authentication, the job / job runs will be created but
          submitted job runs will fail, until this property is provided, too.
    :attr List[str] run_arguments: (optional) Set arguments for the job that are
          passed to start job run containers. If not specified an empty string array will
          be applied and the arguments specified by the container image, will be used to
          start the container.
    :attr int run_as_user: (optional) The user ID (UID) to run the application
          (e.g., 1001).
    :attr List[str] run_commands: (optional) Set commands for the job that are
          passed to start job run containers. If not specified an empty string array will
          be applied and the command specified by the container image, will be used to
          start the container.
    :attr List[EnvVarPrototype] run_env_variables: (optional) Optional references to
          config maps, secrets or a literal values.
    :attr str run_mode: (optional) The mode for runs of the job. Valid values are
          `task` and `daemon`. In `task` mode, the `max_execution_time` and `retry_limit`
          options apply. In `daemon` mode, since there is no timeout and failed instances
          are restarted indefinitely, the `max_execution_time` and `retry_limit` options
          are not allowed.
    :attr str run_service_account: (optional) The name of the service account. For
          built-in service accounts, you can use the shortened names `manager`, `none`,
          `reader`, and `writer`.
    :attr List[VolumeMountPrototype] run_volume_mounts: (optional) Optional mounts
          of config maps or a secrets. In case this is provided, existing
          `run_volume_mounts` will be overwritten.
    :attr str scale_array_spec: (optional) Define a custom set of array indices as
          comma-separated list containing single values and hyphen-separated ranges like
          `5,12-14,23,27`. Each instance can pick up its array index via environment
          variable `JOB_INDEX`. The number of unique array indices specified here
          determines the number of job instances to run.
    :attr str scale_cpu_limit: (optional) Optional amount of CPU set for the
          instance of the job. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
    :attr str scale_ephemeral_storage_limit: (optional) Optional amount of ephemeral
          storage to set for the instance of the job. The amount specified as ephemeral
          storage, must not exceed the amount of `scale_memory_limit`. The units for
          specifying ephemeral storage are Megabyte (M) or Gigabyte (G), whereas G and M
          are the shorthand expressions for GB and MB. For more information see [Units of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :attr int scale_max_execution_time: (optional) The maximum execution time in
          seconds for runs of the job. This option can only be specified if `mode` is
          `task`.
    :attr str scale_memory_limit: (optional) Optional amount of memory set for the
          instance of the job. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
          The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and
          M are the shorthand expressions for GB and MB. For more information see [Units
          of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :attr int scale_retry_limit: (optional) The number of times to rerun an instance
          of the job before the job is marked as failed. This option can only be specified
          if `mode` is `task`.
    """

    def __init__(
        self,
        *,
        image_reference: str = None,
        image_secret: str = None,
        run_arguments: List[str] = None,
        run_as_user: int = None,
        run_commands: List[str] = None,
        run_env_variables: List['EnvVarPrototype'] = None,
        run_mode: str = None,
        run_service_account: str = None,
        run_volume_mounts: List['VolumeMountPrototype'] = None,
        scale_array_spec: str = None,
        scale_cpu_limit: str = None,
        scale_ephemeral_storage_limit: str = None,
        scale_max_execution_time: int = None,
        scale_memory_limit: str = None,
        scale_retry_limit: int = None,
    ) -> None:
        """
        Initialize a JobPatch object.

        :param str image_reference: (optional) The name of the image that is used
               for this job. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where
               `REGISTRY` and `TAG` are optional. If `REGISTRY` is not specified, the
               default is `docker.io`. If `TAG` is not specified, the default is `latest`.
               If the image reference points to a registry that requires authentication,
               make sure to also specify the property `image_secret`.
        :param str image_secret: (optional) The name of the image registry access
               secret. The image registry access secret is used to authenticate with a
               private registry when you download the container image. If the image
               reference points to a registry that requires authentication, the job / job
               runs will be created but submitted job runs will fail, until this property
               is provided, too.
        :param List[str] run_arguments: (optional) Set arguments for the job that
               are passed to start job run containers. If not specified an empty string
               array will be applied and the arguments specified by the container image,
               will be used to start the container.
        :param int run_as_user: (optional) The user ID (UID) to run the application
               (e.g., 1001).
        :param List[str] run_commands: (optional) Set commands for the job that are
               passed to start job run containers. If not specified an empty string array
               will be applied and the command specified by the container image, will be
               used to start the container.
        :param List[EnvVarPrototype] run_env_variables: (optional) Optional
               references to config maps, secrets or a literal values.
        :param str run_mode: (optional) The mode for runs of the job. Valid values
               are `task` and `daemon`. In `task` mode, the `max_execution_time` and
               `retry_limit` options apply. In `daemon` mode, since there is no timeout
               and failed instances are restarted indefinitely, the `max_execution_time`
               and `retry_limit` options are not allowed.
        :param str run_service_account: (optional) The name of the service account.
               For built-in service accounts, you can use the shortened names `manager`,
               `none`, `reader`, and `writer`.
        :param List[VolumeMountPrototype] run_volume_mounts: (optional) Optional
               mounts of config maps or a secrets. In case this is provided, existing
               `run_volume_mounts` will be overwritten.
        :param str scale_array_spec: (optional) Define a custom set of array
               indices as comma-separated list containing single values and
               hyphen-separated ranges like `5,12-14,23,27`. Each instance can pick up its
               array index via environment variable `JOB_INDEX`. The number of unique
               array indices specified here determines the number of job instances to run.
        :param str scale_cpu_limit: (optional) Optional amount of CPU set for the
               instance of the job. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
        :param str scale_ephemeral_storage_limit: (optional) Optional amount of
               ephemeral storage to set for the instance of the job. The amount specified
               as ephemeral storage, must not exceed the amount of `scale_memory_limit`.
               The units for specifying ephemeral storage are Megabyte (M) or Gigabyte
               (G), whereas G and M are the shorthand expressions for GB and MB. For more
               information see [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param int scale_max_execution_time: (optional) The maximum execution time
               in seconds for runs of the job. This option can only be specified if `mode`
               is `task`.
        :param str scale_memory_limit: (optional) Optional amount of memory set for
               the instance of the job. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
               The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G
               and M are the shorthand expressions for GB and MB. For more information see
               [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param int scale_retry_limit: (optional) The number of times to rerun an
               instance of the job before the job is marked as failed. This option can
               only be specified if `mode` is `task`.
        """
        self.image_reference = image_reference
        self.image_secret = image_secret
        self.run_arguments = run_arguments
        self.run_as_user = run_as_user
        self.run_commands = run_commands
        self.run_env_variables = run_env_variables
        self.run_mode = run_mode
        self.run_service_account = run_service_account
        self.run_volume_mounts = run_volume_mounts
        self.scale_array_spec = scale_array_spec
        self.scale_cpu_limit = scale_cpu_limit
        self.scale_ephemeral_storage_limit = scale_ephemeral_storage_limit
        self.scale_max_execution_time = scale_max_execution_time
        self.scale_memory_limit = scale_memory_limit
        self.scale_retry_limit = scale_retry_limit

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'JobPatch':
        """Initialize a JobPatch object from a json dictionary."""
        args = {}
        if 'image_reference' in _dict:
            args['image_reference'] = _dict.get('image_reference')
        if 'image_secret' in _dict:
            args['image_secret'] = _dict.get('image_secret')
        if 'run_arguments' in _dict:
            args['run_arguments'] = _dict.get('run_arguments')
        if 'run_as_user' in _dict:
            args['run_as_user'] = _dict.get('run_as_user')
        if 'run_commands' in _dict:
            args['run_commands'] = _dict.get('run_commands')
        if 'run_env_variables' in _dict:
            args['run_env_variables'] = [EnvVarPrototype.from_dict(v) for v in _dict.get('run_env_variables')]
        if 'run_mode' in _dict:
            args['run_mode'] = _dict.get('run_mode')
        if 'run_service_account' in _dict:
            args['run_service_account'] = _dict.get('run_service_account')
        if 'run_volume_mounts' in _dict:
            args['run_volume_mounts'] = [VolumeMountPrototype.from_dict(v) for v in _dict.get('run_volume_mounts')]
        if 'scale_array_spec' in _dict:
            args['scale_array_spec'] = _dict.get('scale_array_spec')
        if 'scale_cpu_limit' in _dict:
            args['scale_cpu_limit'] = _dict.get('scale_cpu_limit')
        if 'scale_ephemeral_storage_limit' in _dict:
            args['scale_ephemeral_storage_limit'] = _dict.get('scale_ephemeral_storage_limit')
        if 'scale_max_execution_time' in _dict:
            args['scale_max_execution_time'] = _dict.get('scale_max_execution_time')
        if 'scale_memory_limit' in _dict:
            args['scale_memory_limit'] = _dict.get('scale_memory_limit')
        if 'scale_retry_limit' in _dict:
            args['scale_retry_limit'] = _dict.get('scale_retry_limit')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a JobPatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'image_reference') and self.image_reference is not None:
            _dict['image_reference'] = self.image_reference
        if hasattr(self, 'image_secret') and self.image_secret is not None:
            _dict['image_secret'] = self.image_secret
        if hasattr(self, 'run_arguments') and self.run_arguments is not None:
            _dict['run_arguments'] = self.run_arguments
        if hasattr(self, 'run_as_user') and self.run_as_user is not None:
            _dict['run_as_user'] = self.run_as_user
        if hasattr(self, 'run_commands') and self.run_commands is not None:
            _dict['run_commands'] = self.run_commands
        if hasattr(self, 'run_env_variables') and self.run_env_variables is not None:
            run_env_variables_list = []
            for v in self.run_env_variables:
                if isinstance(v, dict):
                    run_env_variables_list.append(v)
                else:
                    run_env_variables_list.append(v.to_dict())
            _dict['run_env_variables'] = run_env_variables_list
        if hasattr(self, 'run_mode') and self.run_mode is not None:
            _dict['run_mode'] = self.run_mode
        if hasattr(self, 'run_service_account') and self.run_service_account is not None:
            _dict['run_service_account'] = self.run_service_account
        if hasattr(self, 'run_volume_mounts') and self.run_volume_mounts is not None:
            run_volume_mounts_list = []
            for v in self.run_volume_mounts:
                if isinstance(v, dict):
                    run_volume_mounts_list.append(v)
                else:
                    run_volume_mounts_list.append(v.to_dict())
            _dict['run_volume_mounts'] = run_volume_mounts_list
        if hasattr(self, 'scale_array_spec') and self.scale_array_spec is not None:
            _dict['scale_array_spec'] = self.scale_array_spec
        if hasattr(self, 'scale_cpu_limit') and self.scale_cpu_limit is not None:
            _dict['scale_cpu_limit'] = self.scale_cpu_limit
        if hasattr(self, 'scale_ephemeral_storage_limit') and self.scale_ephemeral_storage_limit is not None:
            _dict['scale_ephemeral_storage_limit'] = self.scale_ephemeral_storage_limit
        if hasattr(self, 'scale_max_execution_time') and self.scale_max_execution_time is not None:
            _dict['scale_max_execution_time'] = self.scale_max_execution_time
        if hasattr(self, 'scale_memory_limit') and self.scale_memory_limit is not None:
            _dict['scale_memory_limit'] = self.scale_memory_limit
        if hasattr(self, 'scale_retry_limit') and self.scale_retry_limit is not None:
            _dict['scale_retry_limit'] = self.scale_retry_limit
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this JobPatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'JobPatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'JobPatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class RunModeEnum(str, Enum):
        """
        The mode for runs of the job. Valid values are `task` and `daemon`. In `task`
        mode, the `max_execution_time` and `retry_limit` options apply. In `daemon` mode,
        since there is no timeout and failed instances are restarted indefinitely, the
        `max_execution_time` and `retry_limit` options are not allowed.
        """

        TASK = 'task'
        DAEMON = 'daemon'

    class RunServiceAccountEnum(str, Enum):
        """
        The name of the service account. For built-in service accounts, you can use the
        shortened names `manager`, `none`, `reader`, and `writer`.
        """

        DEFAULT = 'default'
        MANAGER = 'manager'
        READER = 'reader'
        WRITER = 'writer'
        NONE = 'none'


class JobRun:
    """
    Response model for job run resources.

    :attr str created_at: (optional) The date when the resource was created.
    :attr str href: (optional) When you provision a new job run,  a URL is created
          identifying the location of the instance.
    :attr str id: (optional) The identifier of the resource.
    :attr str image_reference: (optional) The name of the image that is used for
          this job. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and
          `TAG` are optional. If `REGISTRY` is not specified, the default is `docker.io`.
          If `TAG` is not specified, the default is `latest`. If the image reference
          points to a registry that requires authentication, make sure to also specify the
          property `image_secret`.
    :attr str image_secret: (optional) The name of the image registry access secret.
          The image registry access secret is used to authenticate with a private registry
          when you download the container image. If the image reference points to a
          registry that requires authentication, the job / job runs will be created but
          submitted job runs will fail, until this property is provided, too.
    :attr str job_name: (optional) Optional name of the job reference of this job
          run. If specified, the job run will inherit the configuration of the referenced
          job.
    :attr str name: (optional) The name of the job run.
    :attr str project_id: The ID of the project the resource is located in.
    :attr str resource_type: (optional) The type of the job run.
    :attr List[str] run_arguments: Set arguments for the job that are passed to
          start job run containers. If not specified an empty string array will be applied
          and the arguments specified by the container image, will be used to start the
          container.
    :attr int run_as_user: (optional) The user ID (UID) to run the application
          (e.g., 1001).
    :attr List[str] run_commands: Set commands for the job that are passed to start
          job run containers. If not specified an empty string array will be applied and
          the command specified by the container image, will be used to start the
          container.
    :attr List[EnvVar] run_env_variables: References to config maps, secrets or a
          literal values, which are exposed as environment variables in the job run.
    :attr str run_mode: (optional) The mode for runs of the job. Valid values are
          `task` and `daemon`. In `task` mode, the `max_execution_time` and `retry_limit`
          options apply. In `daemon` mode, since there is no timeout and failed instances
          are restarted indefinitely, the `max_execution_time` and `retry_limit` options
          are not allowed.
    :attr str run_service_account: (optional) The name of the service account. For
          built-in service accounts, you can use the shortened names `manager`, `none`,
          `reader`, and `writer`.
    :attr List[VolumeMount] run_volume_mounts: Optional mounts of config maps or a
          secrets.
    :attr str scale_array_spec: (optional) Define a custom set of array indices as
          comma-separated list containing single values and hyphen-separated ranges like
          `5,12-14,23,27`. Each instance can pick up its array index via environment
          variable `JOB_INDEX`. The number of unique array indices specified here
          determines the number of job instances to run.
    :attr str scale_cpu_limit: (optional) Optional amount of CPU set for the
          instance of the job. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
    :attr str scale_ephemeral_storage_limit: (optional) Optional amount of ephemeral
          storage to set for the instance of the job. The amount specified as ephemeral
          storage, must not exceed the amount of `scale_memory_limit`. The units for
          specifying ephemeral storage are Megabyte (M) or Gigabyte (G), whereas G and M
          are the shorthand expressions for GB and MB. For more information see [Units of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :attr int scale_max_execution_time: (optional) The maximum execution time in
          seconds for runs of the job. This option can only be specified if `mode` is
          `task`.
    :attr str scale_memory_limit: (optional) Optional amount of memory set for the
          instance of the job. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
          The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and
          M are the shorthand expressions for GB and MB. For more information see [Units
          of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :attr int scale_retry_limit: (optional) The number of times to rerun an instance
          of the job before the job is marked as failed. This option can only be specified
          if `mode` is `task`.
    :attr str status: (optional) The current status of the job run.
    :attr JobRunStatus status_details: (optional) The detailed status of the job
          run.
    """

    def __init__(
        self,
        project_id: str,
        run_arguments: List[str],
        run_commands: List[str],
        run_env_variables: List['EnvVar'],
        run_volume_mounts: List['VolumeMount'],
        *,
        created_at: str = None,
        href: str = None,
        id: str = None,
        image_reference: str = None,
        image_secret: str = None,
        job_name: str = None,
        name: str = None,
        resource_type: str = None,
        run_as_user: int = None,
        run_mode: str = None,
        run_service_account: str = None,
        scale_array_spec: str = None,
        scale_cpu_limit: str = None,
        scale_ephemeral_storage_limit: str = None,
        scale_max_execution_time: int = None,
        scale_memory_limit: str = None,
        scale_retry_limit: int = None,
        status: str = None,
        status_details: 'JobRunStatus' = None,
    ) -> None:
        """
        Initialize a JobRun object.

        :param str project_id: The ID of the project the resource is located in.
        :param List[str] run_arguments: Set arguments for the job that are passed
               to start job run containers. If not specified an empty string array will be
               applied and the arguments specified by the container image, will be used to
               start the container.
        :param List[str] run_commands: Set commands for the job that are passed to
               start job run containers. If not specified an empty string array will be
               applied and the command specified by the container image, will be used to
               start the container.
        :param List[EnvVar] run_env_variables: References to config maps, secrets
               or a literal values, which are exposed as environment variables in the job
               run.
        :param List[VolumeMount] run_volume_mounts: Optional mounts of config maps
               or a secrets.
        :param str created_at: (optional) The date when the resource was created.
        :param str href: (optional) When you provision a new job run,  a URL is
               created identifying the location of the instance.
        :param str id: (optional) The identifier of the resource.
        :param str image_reference: (optional) The name of the image that is used
               for this job. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where
               `REGISTRY` and `TAG` are optional. If `REGISTRY` is not specified, the
               default is `docker.io`. If `TAG` is not specified, the default is `latest`.
               If the image reference points to a registry that requires authentication,
               make sure to also specify the property `image_secret`.
        :param str image_secret: (optional) The name of the image registry access
               secret. The image registry access secret is used to authenticate with a
               private registry when you download the container image. If the image
               reference points to a registry that requires authentication, the job / job
               runs will be created but submitted job runs will fail, until this property
               is provided, too.
        :param str job_name: (optional) Optional name of the job reference of this
               job run. If specified, the job run will inherit the configuration of the
               referenced job.
        :param str name: (optional) The name of the job run.
        :param str resource_type: (optional) The type of the job run.
        :param int run_as_user: (optional) The user ID (UID) to run the application
               (e.g., 1001).
        :param str run_mode: (optional) The mode for runs of the job. Valid values
               are `task` and `daemon`. In `task` mode, the `max_execution_time` and
               `retry_limit` options apply. In `daemon` mode, since there is no timeout
               and failed instances are restarted indefinitely, the `max_execution_time`
               and `retry_limit` options are not allowed.
        :param str run_service_account: (optional) The name of the service account.
               For built-in service accounts, you can use the shortened names `manager`,
               `none`, `reader`, and `writer`.
        :param str scale_array_spec: (optional) Define a custom set of array
               indices as comma-separated list containing single values and
               hyphen-separated ranges like `5,12-14,23,27`. Each instance can pick up its
               array index via environment variable `JOB_INDEX`. The number of unique
               array indices specified here determines the number of job instances to run.
        :param str scale_cpu_limit: (optional) Optional amount of CPU set for the
               instance of the job. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
        :param str scale_ephemeral_storage_limit: (optional) Optional amount of
               ephemeral storage to set for the instance of the job. The amount specified
               as ephemeral storage, must not exceed the amount of `scale_memory_limit`.
               The units for specifying ephemeral storage are Megabyte (M) or Gigabyte
               (G), whereas G and M are the shorthand expressions for GB and MB. For more
               information see [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param int scale_max_execution_time: (optional) The maximum execution time
               in seconds for runs of the job. This option can only be specified if `mode`
               is `task`.
        :param str scale_memory_limit: (optional) Optional amount of memory set for
               the instance of the job. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
               The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G
               and M are the shorthand expressions for GB and MB. For more information see
               [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param int scale_retry_limit: (optional) The number of times to rerun an
               instance of the job before the job is marked as failed. This option can
               only be specified if `mode` is `task`.
        :param str status: (optional) The current status of the job run.
        :param JobRunStatus status_details: (optional) The detailed status of the
               job run.
        """
        self.created_at = created_at
        self.href = href
        self.id = id
        self.image_reference = image_reference
        self.image_secret = image_secret
        self.job_name = job_name
        self.name = name
        self.project_id = project_id
        self.resource_type = resource_type
        self.run_arguments = run_arguments
        self.run_as_user = run_as_user
        self.run_commands = run_commands
        self.run_env_variables = run_env_variables
        self.run_mode = run_mode
        self.run_service_account = run_service_account
        self.run_volume_mounts = run_volume_mounts
        self.scale_array_spec = scale_array_spec
        self.scale_cpu_limit = scale_cpu_limit
        self.scale_ephemeral_storage_limit = scale_ephemeral_storage_limit
        self.scale_max_execution_time = scale_max_execution_time
        self.scale_memory_limit = scale_memory_limit
        self.scale_retry_limit = scale_retry_limit
        self.status = status
        self.status_details = status_details

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'JobRun':
        """Initialize a JobRun object from a json dictionary."""
        args = {}
        if 'created_at' in _dict:
            args['created_at'] = _dict.get('created_at')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'image_reference' in _dict:
            args['image_reference'] = _dict.get('image_reference')
        if 'image_secret' in _dict:
            args['image_secret'] = _dict.get('image_secret')
        if 'job_name' in _dict:
            args['job_name'] = _dict.get('job_name')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        else:
            raise ValueError('Required property \'project_id\' not present in JobRun JSON')
        if 'resource_type' in _dict:
            args['resource_type'] = _dict.get('resource_type')
        if 'run_arguments' in _dict:
            args['run_arguments'] = _dict.get('run_arguments')
        else:
            raise ValueError('Required property \'run_arguments\' not present in JobRun JSON')
        if 'run_as_user' in _dict:
            args['run_as_user'] = _dict.get('run_as_user')
        if 'run_commands' in _dict:
            args['run_commands'] = _dict.get('run_commands')
        else:
            raise ValueError('Required property \'run_commands\' not present in JobRun JSON')
        if 'run_env_variables' in _dict:
            args['run_env_variables'] = [EnvVar.from_dict(v) for v in _dict.get('run_env_variables')]
        else:
            raise ValueError('Required property \'run_env_variables\' not present in JobRun JSON')
        if 'run_mode' in _dict:
            args['run_mode'] = _dict.get('run_mode')
        if 'run_service_account' in _dict:
            args['run_service_account'] = _dict.get('run_service_account')
        if 'run_volume_mounts' in _dict:
            args['run_volume_mounts'] = [VolumeMount.from_dict(v) for v in _dict.get('run_volume_mounts')]
        else:
            raise ValueError('Required property \'run_volume_mounts\' not present in JobRun JSON')
        if 'scale_array_spec' in _dict:
            args['scale_array_spec'] = _dict.get('scale_array_spec')
        if 'scale_cpu_limit' in _dict:
            args['scale_cpu_limit'] = _dict.get('scale_cpu_limit')
        if 'scale_ephemeral_storage_limit' in _dict:
            args['scale_ephemeral_storage_limit'] = _dict.get('scale_ephemeral_storage_limit')
        if 'scale_max_execution_time' in _dict:
            args['scale_max_execution_time'] = _dict.get('scale_max_execution_time')
        if 'scale_memory_limit' in _dict:
            args['scale_memory_limit'] = _dict.get('scale_memory_limit')
        if 'scale_retry_limit' in _dict:
            args['scale_retry_limit'] = _dict.get('scale_retry_limit')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'status_details' in _dict:
            args['status_details'] = JobRunStatus.from_dict(_dict.get('status_details'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a JobRun object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = self.created_at
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'image_reference') and self.image_reference is not None:
            _dict['image_reference'] = self.image_reference
        if hasattr(self, 'image_secret') and self.image_secret is not None:
            _dict['image_secret'] = self.image_secret
        if hasattr(self, 'job_name') and self.job_name is not None:
            _dict['job_name'] = self.job_name
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'project_id') and self.project_id is not None:
            _dict['project_id'] = self.project_id
        if hasattr(self, 'resource_type') and self.resource_type is not None:
            _dict['resource_type'] = self.resource_type
        if hasattr(self, 'run_arguments') and self.run_arguments is not None:
            _dict['run_arguments'] = self.run_arguments
        if hasattr(self, 'run_as_user') and self.run_as_user is not None:
            _dict['run_as_user'] = self.run_as_user
        if hasattr(self, 'run_commands') and self.run_commands is not None:
            _dict['run_commands'] = self.run_commands
        if hasattr(self, 'run_env_variables') and self.run_env_variables is not None:
            run_env_variables_list = []
            for v in self.run_env_variables:
                if isinstance(v, dict):
                    run_env_variables_list.append(v)
                else:
                    run_env_variables_list.append(v.to_dict())
            _dict['run_env_variables'] = run_env_variables_list
        if hasattr(self, 'run_mode') and self.run_mode is not None:
            _dict['run_mode'] = self.run_mode
        if hasattr(self, 'run_service_account') and self.run_service_account is not None:
            _dict['run_service_account'] = self.run_service_account
        if hasattr(self, 'run_volume_mounts') and self.run_volume_mounts is not None:
            run_volume_mounts_list = []
            for v in self.run_volume_mounts:
                if isinstance(v, dict):
                    run_volume_mounts_list.append(v)
                else:
                    run_volume_mounts_list.append(v.to_dict())
            _dict['run_volume_mounts'] = run_volume_mounts_list
        if hasattr(self, 'scale_array_spec') and self.scale_array_spec is not None:
            _dict['scale_array_spec'] = self.scale_array_spec
        if hasattr(self, 'scale_cpu_limit') and self.scale_cpu_limit is not None:
            _dict['scale_cpu_limit'] = self.scale_cpu_limit
        if hasattr(self, 'scale_ephemeral_storage_limit') and self.scale_ephemeral_storage_limit is not None:
            _dict['scale_ephemeral_storage_limit'] = self.scale_ephemeral_storage_limit
        if hasattr(self, 'scale_max_execution_time') and self.scale_max_execution_time is not None:
            _dict['scale_max_execution_time'] = self.scale_max_execution_time
        if hasattr(self, 'scale_memory_limit') and self.scale_memory_limit is not None:
            _dict['scale_memory_limit'] = self.scale_memory_limit
        if hasattr(self, 'scale_retry_limit') and self.scale_retry_limit is not None:
            _dict['scale_retry_limit'] = self.scale_retry_limit
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'status_details') and self.status_details is not None:
            if isinstance(self.status_details, dict):
                _dict['status_details'] = self.status_details
            else:
                _dict['status_details'] = self.status_details.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this JobRun object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'JobRun') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'JobRun') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ResourceTypeEnum(str, Enum):
        """
        The type of the job run.
        """

        JOB_RUN_V2 = 'job_run_v2'

    class RunModeEnum(str, Enum):
        """
        The mode for runs of the job. Valid values are `task` and `daemon`. In `task`
        mode, the `max_execution_time` and `retry_limit` options apply. In `daemon` mode,
        since there is no timeout and failed instances are restarted indefinitely, the
        `max_execution_time` and `retry_limit` options are not allowed.
        """

        TASK = 'task'
        DAEMON = 'daemon'

    class RunServiceAccountEnum(str, Enum):
        """
        The name of the service account. For built-in service accounts, you can use the
        shortened names `manager`, `none`, `reader`, and `writer`.
        """

        DEFAULT = 'default'
        MANAGER = 'manager'
        READER = 'reader'
        WRITER = 'writer'
        NONE = 'none'

    class StatusEnum(str, Enum):
        """
        The current status of the job run.
        """

        COMPLETED = 'completed'
        RUNNING = 'running'
        PENDING = 'pending'


class JobRunList:
    """
    Contains a list of job runs and pagination information.

    :attr ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :attr List[JobRun] job_runs: List of all jobs.
    :attr int limit: Maximum number of resources per page.
    :attr ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    """

    def __init__(
        self,
        job_runs: List['JobRun'],
        limit: int,
        *,
        first: 'ListFirstMetadata' = None,
        next: 'ListNextMetadata' = None,
    ) -> None:
        """
        Initialize a JobRunList object.

        :param List[JobRun] job_runs: List of all jobs.
        :param int limit: Maximum number of resources per page.
        :param ListFirstMetadata first: (optional) Describes properties needed to
               retrieve the first page of a result list.
        :param ListNextMetadata next: (optional) Describes properties needed to
               retrieve the next page of a result list.
        """
        self.first = first
        self.job_runs = job_runs
        self.limit = limit
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'JobRunList':
        """Initialize a JobRunList object from a json dictionary."""
        args = {}
        if 'first' in _dict:
            args['first'] = ListFirstMetadata.from_dict(_dict.get('first'))
        if 'job_runs' in _dict:
            args['job_runs'] = [JobRun.from_dict(v) for v in _dict.get('job_runs')]
        else:
            raise ValueError('Required property \'job_runs\' not present in JobRunList JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in JobRunList JSON')
        if 'next' in _dict:
            args['next'] = ListNextMetadata.from_dict(_dict.get('next'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a JobRunList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'job_runs') and self.job_runs is not None:
            job_runs_list = []
            for v in self.job_runs:
                if isinstance(v, dict):
                    job_runs_list.append(v)
                else:
                    job_runs_list.append(v.to_dict())
            _dict['job_runs'] = job_runs_list
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this JobRunList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'JobRunList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'JobRunList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class JobRunStatus:
    """
    The detailed status of the job run.

    :attr str completion_time: (optional) Time the job run completed.
    :attr int failed: (optional) Number of failed job run instances.
    :attr int pending: (optional) Number of pending job run instances.
    :attr int requested: (optional) Number of requested job run instances.
    :attr int running: (optional) Number of running job run instances.
    :attr str start_time: (optional) Time the job run started.
    :attr int succeeded: (optional) Number of succeeded job run instances.
    :attr int unknown: (optional) Number of job run instances with unknown state.
    """

    def __init__(
        self,
        *,
        completion_time: str = None,
        failed: int = None,
        pending: int = None,
        requested: int = None,
        running: int = None,
        start_time: str = None,
        succeeded: int = None,
        unknown: int = None,
    ) -> None:
        """
        Initialize a JobRunStatus object.

        :param str completion_time: (optional) Time the job run completed.
        :param int failed: (optional) Number of failed job run instances.
        :param int pending: (optional) Number of pending job run instances.
        :param int requested: (optional) Number of requested job run instances.
        :param int running: (optional) Number of running job run instances.
        :param str start_time: (optional) Time the job run started.
        :param int succeeded: (optional) Number of succeeded job run instances.
        :param int unknown: (optional) Number of job run instances with unknown
               state.
        """
        self.completion_time = completion_time
        self.failed = failed
        self.pending = pending
        self.requested = requested
        self.running = running
        self.start_time = start_time
        self.succeeded = succeeded
        self.unknown = unknown

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'JobRunStatus':
        """Initialize a JobRunStatus object from a json dictionary."""
        args = {}
        if 'completion_time' in _dict:
            args['completion_time'] = _dict.get('completion_time')
        if 'failed' in _dict:
            args['failed'] = _dict.get('failed')
        if 'pending' in _dict:
            args['pending'] = _dict.get('pending')
        if 'requested' in _dict:
            args['requested'] = _dict.get('requested')
        if 'running' in _dict:
            args['running'] = _dict.get('running')
        if 'start_time' in _dict:
            args['start_time'] = _dict.get('start_time')
        if 'succeeded' in _dict:
            args['succeeded'] = _dict.get('succeeded')
        if 'unknown' in _dict:
            args['unknown'] = _dict.get('unknown')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a JobRunStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'completion_time') and self.completion_time is not None:
            _dict['completion_time'] = self.completion_time
        if hasattr(self, 'failed') and self.failed is not None:
            _dict['failed'] = self.failed
        if hasattr(self, 'pending') and self.pending is not None:
            _dict['pending'] = self.pending
        if hasattr(self, 'requested') and self.requested is not None:
            _dict['requested'] = self.requested
        if hasattr(self, 'running') and self.running is not None:
            _dict['running'] = self.running
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = self.start_time
        if hasattr(self, 'succeeded') and self.succeeded is not None:
            _dict['succeeded'] = self.succeeded
        if hasattr(self, 'unknown') and self.unknown is not None:
            _dict['unknown'] = self.unknown
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this JobRunStatus object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'JobRunStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'JobRunStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListFirstMetadata:
    """
    Describes properties needed to retrieve the first page of a result list.

    :attr str href: (optional) Href that points to the first page.
    """

    def __init__(self, *, href: str = None) -> None:
        """
        Initialize a ListFirstMetadata object.

        :param str href: (optional) Href that points to the first page.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListFirstMetadata':
        """Initialize a ListFirstMetadata object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListFirstMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListFirstMetadata object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListFirstMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListFirstMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListNextMetadata:
    """
    Describes properties needed to retrieve the next page of a result list.

    :attr str href: (optional) Href that points to the next page.
    :attr str start: (optional) Token.
    """

    def __init__(self, *, href: str = None, start: str = None) -> None:
        """
        Initialize a ListNextMetadata object.

        :param str href: (optional) Href that points to the next page.
        :param str start: (optional) Token.
        """
        self.href = href
        self.start = start

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListNextMetadata':
        """Initialize a ListNextMetadata object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'start' in _dict:
            args['start'] = _dict.get('start')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListNextMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListNextMetadata object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListNextMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListNextMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Project:
    """
    Describes the model of a project.

    :attr str account_id: An alphanumeric value identifying the account ID.
    :attr str created_at: The date when the project was created.
    :attr str crn: The CRN of the project.
    :attr str href: When you provision a new resource, a URL is created identifying
          the location of the instance.
    :attr str id: The ID of the project.
    :attr str name: The name of the project.
    :attr str region: The region for your project deployment. Possible values:
          'au-syd', 'br-sao', 'ca-tor', 'eu-de', 'eu-gb', 'jp-osa', 'jp-tok', 'us-east',
          'us-south'.
    :attr str resource_group_id: The ID of the resource group.
    :attr str resource_type: The type of the project.
    :attr str status: The current state of the project. For example, if the project
          is created and ready to get used, it will return active.
    """

    def __init__(
        self,
        account_id: str,
        created_at: str,
        crn: str,
        href: str,
        id: str,
        name: str,
        region: str,
        resource_group_id: str,
        resource_type: str,
        status: str,
    ) -> None:
        """
        Initialize a Project object.

        :param str account_id: An alphanumeric value identifying the account ID.
        :param str created_at: The date when the project was created.
        :param str crn: The CRN of the project.
        :param str href: When you provision a new resource, a URL is created
               identifying the location of the instance.
        :param str id: The ID of the project.
        :param str name: The name of the project.
        :param str region: The region for your project deployment. Possible values:
               'au-syd', 'br-sao', 'ca-tor', 'eu-de', 'eu-gb', 'jp-osa', 'jp-tok',
               'us-east', 'us-south'.
        :param str resource_group_id: The ID of the resource group.
        :param str resource_type: The type of the project.
        :param str status: The current state of the project. For example, if the
               project is created and ready to get used, it will return active.
        """
        self.account_id = account_id
        self.created_at = created_at
        self.crn = crn
        self.href = href
        self.id = id
        self.name = name
        self.region = region
        self.resource_group_id = resource_group_id
        self.resource_type = resource_type
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Project':
        """Initialize a Project object from a json dictionary."""
        args = {}
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in Project JSON')
        if 'created_at' in _dict:
            args['created_at'] = _dict.get('created_at')
        else:
            raise ValueError('Required property \'created_at\' not present in Project JSON')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in Project JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in Project JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Project JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in Project JSON')
        if 'region' in _dict:
            args['region'] = _dict.get('region')
        else:
            raise ValueError('Required property \'region\' not present in Project JSON')
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        else:
            raise ValueError('Required property \'resource_group_id\' not present in Project JSON')
        if 'resource_type' in _dict:
            args['resource_type'] = _dict.get('resource_type')
        else:
            raise ValueError('Required property \'resource_type\' not present in Project JSON')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in Project JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Project object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = self.created_at
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'region') and self.region is not None:
            _dict['region'] = self.region
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'resource_type') and self.resource_type is not None:
            _dict['resource_type'] = self.resource_type
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Project object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Project') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Project') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ResourceTypeEnum(str, Enum):
        """
        The type of the project.
        """

        PROJECT_V2 = 'project_v2'

    class StatusEnum(str, Enum):
        """
        The current state of the project. For example, if the project is created and ready
        to get used, it will return active.
        """

        ACTIVE = 'active'
        INACTIVE = 'inactive'
        PENDING_REMOVAL = 'pending_removal'
        HARD_DELETING = 'hard_deleting'
        HARD_DELETION_FAILED = 'hard_deletion_failed'
        HARD_DELETED = 'hard_deleted'
        DELETING = 'deleting'
        DELETION_FAILED = 'deletion_failed'
        SOFT_DELETED = 'soft_deleted'
        PREPARING = 'preparing'
        CREATING = 'creating'
        CREATION_FAILED = 'creation_failed'


class ProjectList:
    """
    Contains a list of projects and pagination information.

    :attr ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :attr int limit: Maximum number of resources per page.
    :attr ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    :attr List[Project] projects: List of projects.
    """

    def __init__(
        self,
        limit: int,
        projects: List['Project'],
        *,
        first: 'ListFirstMetadata' = None,
        next: 'ListNextMetadata' = None,
    ) -> None:
        """
        Initialize a ProjectList object.

        :param int limit: Maximum number of resources per page.
        :param List[Project] projects: List of projects.
        :param ListFirstMetadata first: (optional) Describes properties needed to
               retrieve the first page of a result list.
        :param ListNextMetadata next: (optional) Describes properties needed to
               retrieve the next page of a result list.
        """
        self.first = first
        self.limit = limit
        self.next = next
        self.projects = projects

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectList':
        """Initialize a ProjectList object from a json dictionary."""
        args = {}
        if 'first' in _dict:
            args['first'] = ListFirstMetadata.from_dict(_dict.get('first'))
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ProjectList JSON')
        if 'next' in _dict:
            args['next'] = ListNextMetadata.from_dict(_dict.get('next'))
        if 'projects' in _dict:
            args['projects'] = [Project.from_dict(v) for v in _dict.get('projects')]
        else:
            raise ValueError('Required property \'projects\' not present in ProjectList JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'projects') and self.projects is not None:
            projects_list = []
            for v in self.projects:
                if isinstance(v, dict):
                    projects_list.append(v)
                else:
                    projects_list.append(v.to_dict())
            _dict['projects'] = projects_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Secret:
    """
    Describes the model of a secret.

    :attr str created_at: The date when the resource was created.
    :attr dict data: (optional) Data container that allows to specify config
          parameters and their values as a key-value map. Each key field must consist of
          alphanumeric characters, `-`, `_` or `.` and must not be exceed a max length of
          253 characters. Each value field can consists of any character and must not be
          exceed a max length of 1048576 characters.
    :attr str entity_tag: The version of the secret instance, which is used to
          achieve optimistic locking.
    :attr str format: (optional) Specify the format of the secret.
    :attr str href: (optional) When you provision a new secret,  a URL is created
          identifying the location of the instance.
    :attr str id: The identifier of the resource.
    :attr str name: The name of the secret.
    :attr str project_id: The ID of the project the resource is located in.
    :attr str resource_type: The type of the secret.
    """

    def __init__(
        self,
        created_at: str,
        entity_tag: str,
        id: str,
        name: str,
        project_id: str,
        resource_type: str,
        *,
        data: dict = None,
        format: str = None,
        href: str = None,
    ) -> None:
        """
        Initialize a Secret object.

        :param str created_at: The date when the resource was created.
        :param str entity_tag: The version of the secret instance, which is used to
               achieve optimistic locking.
        :param str id: The identifier of the resource.
        :param str name: The name of the secret.
        :param str project_id: The ID of the project the resource is located in.
        :param str resource_type: The type of the secret.
        :param dict data: (optional) Data container that allows to specify config
               parameters and their values as a key-value map. Each key field must consist
               of alphanumeric characters, `-`, `_` or `.` and must not be exceed a max
               length of 253 characters. Each value field can consists of any character
               and must not be exceed a max length of 1048576 characters.
        :param str format: (optional) Specify the format of the secret.
        :param str href: (optional) When you provision a new secret,  a URL is
               created identifying the location of the instance.
        """
        self.created_at = created_at
        self.data = data
        self.entity_tag = entity_tag
        self.format = format
        self.href = href
        self.id = id
        self.name = name
        self.project_id = project_id
        self.resource_type = resource_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Secret':
        """Initialize a Secret object from a json dictionary."""
        args = {}
        if 'created_at' in _dict:
            args['created_at'] = _dict.get('created_at')
        else:
            raise ValueError('Required property \'created_at\' not present in Secret JSON')
        if 'data' in _dict:
            args['data'] = _dict.get('data')
        if 'entity_tag' in _dict:
            args['entity_tag'] = _dict.get('entity_tag')
        else:
            raise ValueError('Required property \'entity_tag\' not present in Secret JSON')
        if 'format' in _dict:
            args['format'] = _dict.get('format')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Secret JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in Secret JSON')
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        else:
            raise ValueError('Required property \'project_id\' not present in Secret JSON')
        if 'resource_type' in _dict:
            args['resource_type'] = _dict.get('resource_type')
        else:
            raise ValueError('Required property \'resource_type\' not present in Secret JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Secret object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = self.created_at
        if hasattr(self, 'data') and self.data is not None:
            _dict['data'] = self.data
        if hasattr(self, 'entity_tag') and self.entity_tag is not None:
            _dict['entity_tag'] = self.entity_tag
        if hasattr(self, 'format') and self.format is not None:
            _dict['format'] = self.format
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'project_id') and self.project_id is not None:
            _dict['project_id'] = self.project_id
        if hasattr(self, 'resource_type') and self.resource_type is not None:
            _dict['resource_type'] = self.resource_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Secret object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Secret') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Secret') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class FormatEnum(str, Enum):
        """
        Specify the format of the secret.
        """

        GENERIC = 'generic'
        SSH_AUTH = 'ssh_auth'
        BASIC_AUTH = 'basic_auth'
        TLS = 'tls'
        SERVICE_ACCESS = 'service_access'
        REGISTRY = 'registry'
        OTHER = 'other'


class SecretList:
    """
    List of secret resources.

    :attr ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :attr int limit: Maximum number of resources per page.
    :attr ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    :attr List[Secret] secrets: List of Secrets.
    """

    def __init__(
        self, limit: int, secrets: List['Secret'], *, first: 'ListFirstMetadata' = None, next: 'ListNextMetadata' = None
    ) -> None:
        """
        Initialize a SecretList object.

        :param int limit: Maximum number of resources per page.
        :param List[Secret] secrets: List of Secrets.
        :param ListFirstMetadata first: (optional) Describes properties needed to
               retrieve the first page of a result list.
        :param ListNextMetadata next: (optional) Describes properties needed to
               retrieve the next page of a result list.
        """
        self.first = first
        self.limit = limit
        self.next = next
        self.secrets = secrets

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecretList':
        """Initialize a SecretList object from a json dictionary."""
        args = {}
        if 'first' in _dict:
            args['first'] = ListFirstMetadata.from_dict(_dict.get('first'))
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in SecretList JSON')
        if 'next' in _dict:
            args['next'] = ListNextMetadata.from_dict(_dict.get('next'))
        if 'secrets' in _dict:
            args['secrets'] = [Secret.from_dict(v) for v in _dict.get('secrets')]
        else:
            raise ValueError('Required property \'secrets\' not present in SecretList JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecretList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'secrets') and self.secrets is not None:
            secrets_list = []
            for v in self.secrets:
                if isinstance(v, dict):
                    secrets_list.append(v)
                else:
                    secrets_list.append(v.to_dict())
            _dict['secrets'] = secrets_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SecretList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecretList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecretList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class VolumeMount:
    """
    Response model of a volume mount.

    :attr str mount_path: The path that should be mounted.
    :attr str name: The name of the mount.
    :attr str reference: The name of the referenced secret or config map.
    :attr str type: Specify the type of the volume mount. Allowed types are:
          'config_map', 'secret'.
    """

    def __init__(self, mount_path: str, name: str, reference: str, type: str) -> None:
        """
        Initialize a VolumeMount object.

        :param str mount_path: The path that should be mounted.
        :param str name: The name of the mount.
        :param str reference: The name of the referenced secret or config map.
        :param str type: Specify the type of the volume mount. Allowed types are:
               'config_map', 'secret'.
        """
        self.mount_path = mount_path
        self.name = name
        self.reference = reference
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VolumeMount':
        """Initialize a VolumeMount object from a json dictionary."""
        args = {}
        if 'mount_path' in _dict:
            args['mount_path'] = _dict.get('mount_path')
        else:
            raise ValueError('Required property \'mount_path\' not present in VolumeMount JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in VolumeMount JSON')
        if 'reference' in _dict:
            args['reference'] = _dict.get('reference')
        else:
            raise ValueError('Required property \'reference\' not present in VolumeMount JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in VolumeMount JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VolumeMount object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'mount_path') and self.mount_path is not None:
            _dict['mount_path'] = self.mount_path
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'reference') and self.reference is not None:
            _dict['reference'] = self.reference
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this VolumeMount object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VolumeMount') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VolumeMount') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Specify the type of the volume mount. Allowed types are: 'config_map', 'secret'.
        """

        CONFIG_MAP = 'config_map'
        SECRET = 'secret'


class VolumeMountPrototype:
    """
    Prototype model of a volume mount.

    :attr str mount_path: The path that should be mounted.
    :attr str name: (optional) Optional name of the mount. If not set, it will be
          generated based on the `ref` and a random ID. In case the `ref` is longer than
          58 characters, it will be cut off.
    :attr str reference: The name of the referenced secret or config map.
    :attr str type: Specify the type of the volume mount. Allowed types are:
          'config_map', 'secret'.
    """

    def __init__(self, mount_path: str, reference: str, type: str, *, name: str = None) -> None:
        """
        Initialize a VolumeMountPrototype object.

        :param str mount_path: The path that should be mounted.
        :param str reference: The name of the referenced secret or config map.
        :param str type: Specify the type of the volume mount. Allowed types are:
               'config_map', 'secret'.
        :param str name: (optional) Optional name of the mount. If not set, it will
               be generated based on the `ref` and a random ID. In case the `ref` is
               longer than 58 characters, it will be cut off.
        """
        self.mount_path = mount_path
        self.name = name
        self.reference = reference
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'VolumeMountPrototype':
        """Initialize a VolumeMountPrototype object from a json dictionary."""
        args = {}
        if 'mount_path' in _dict:
            args['mount_path'] = _dict.get('mount_path')
        else:
            raise ValueError('Required property \'mount_path\' not present in VolumeMountPrototype JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'reference' in _dict:
            args['reference'] = _dict.get('reference')
        else:
            raise ValueError('Required property \'reference\' not present in VolumeMountPrototype JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in VolumeMountPrototype JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VolumeMountPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'mount_path') and self.mount_path is not None:
            _dict['mount_path'] = self.mount_path
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'reference') and self.reference is not None:
            _dict['reference'] = self.reference
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this VolumeMountPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'VolumeMountPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'VolumeMountPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Specify the type of the volume mount. Allowed types are: 'config_map', 'secret'.
        """

        CONFIG_MAP = 'config_map'
        SECRET = 'secret'


##############################################################################
# Pagers
##############################################################################


class ProjectsPager:
    """
    ProjectsPager can be used to simplify the use of the "list_projects" method.
    """

    def __init__(
        self,
        *,
        client: CodeEngineV2,
        limit: int = None,
    ) -> None:
        """
        Initialize a ProjectsPager object.
        :param int limit: (optional) Optional maximum number of projects per page.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of Project.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_projects(
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('projects')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of Project.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class AppsPager:
    """
    AppsPager can be used to simplify the use of the "list_apps" method.
    """

    def __init__(
        self,
        *,
        client: CodeEngineV2,
        project_id: str,
        limit: int = None,
    ) -> None:
        """
        Initialize a AppsPager object.
        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of apps per page.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._project_id = project_id
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of App.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_apps(
            project_id=self._project_id,
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('apps')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of App.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class AppRevisionsPager:
    """
    AppRevisionsPager can be used to simplify the use of the "list_app_revisions" method.
    """

    def __init__(
        self,
        *,
        client: CodeEngineV2,
        project_id: str,
        app_name: str,
        limit: int = None,
    ) -> None:
        """
        Initialize a AppRevisionsPager object.
        :param str project_id: The ID of the project.
        :param str app_name: The name of your application.
        :param int limit: (optional) Optional maximum number of apps per page.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._project_id = project_id
        self._app_name = app_name
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of AppRevision.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_app_revisions(
            project_id=self._project_id,
            app_name=self._app_name,
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('revisions')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of AppRevision.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class JobsPager:
    """
    JobsPager can be used to simplify the use of the "list_jobs" method.
    """

    def __init__(
        self,
        *,
        client: CodeEngineV2,
        project_id: str,
        limit: int = None,
    ) -> None:
        """
        Initialize a JobsPager object.
        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of jobs per page.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._project_id = project_id
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of Job.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_jobs(
            project_id=self._project_id,
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('jobs')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of Job.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class JobRunsPager:
    """
    JobRunsPager can be used to simplify the use of the "list_job_runs" method.
    """

    def __init__(
        self,
        *,
        client: CodeEngineV2,
        project_id: str,
        job_name: str = None,
        limit: int = None,
    ) -> None:
        """
        Initialize a JobRunsPager object.
        :param str project_id: The ID of the project.
        :param str job_name: (optional) Optional name of the job that should be
               filtered for.
        :param int limit: (optional) Optional maximum number of job runs per page.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._project_id = project_id
        self._job_name = job_name
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of JobRun.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_job_runs(
            project_id=self._project_id,
            job_name=self._job_name,
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('job_runs')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of JobRun.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class BuildsPager:
    """
    BuildsPager can be used to simplify the use of the "list_builds" method.
    """

    def __init__(
        self,
        *,
        client: CodeEngineV2,
        project_id: str,
        limit: int = None,
    ) -> None:
        """
        Initialize a BuildsPager object.
        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of builds per page.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._project_id = project_id
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of Build.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_builds(
            project_id=self._project_id,
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('builds')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of Build.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class BuildRunsPager:
    """
    BuildRunsPager can be used to simplify the use of the "list_build_runs" method.
    """

    def __init__(
        self,
        *,
        client: CodeEngineV2,
        project_id: str,
        build_name: str = None,
        limit: int = None,
    ) -> None:
        """
        Initialize a BuildRunsPager object.
        :param str project_id: The ID of the project.
        :param str build_name: (optional) Optional name of the build that should be
               filtered for.
        :param int limit: (optional) Optional maximum number of build runs per
               page.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._project_id = project_id
        self._build_name = build_name
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of BuildRun.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_build_runs(
            project_id=self._project_id,
            build_name=self._build_name,
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('build_runs')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of BuildRun.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class ConfigMapsPager:
    """
    ConfigMapsPager can be used to simplify the use of the "list_config_maps" method.
    """

    def __init__(
        self,
        *,
        client: CodeEngineV2,
        project_id: str,
        limit: int = None,
    ) -> None:
        """
        Initialize a ConfigMapsPager object.
        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of config maps per
               page.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._project_id = project_id
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of ConfigMap.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_config_maps(
            project_id=self._project_id,
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('config_maps')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of ConfigMap.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class SecretsPager:
    """
    SecretsPager can be used to simplify the use of the "list_secrets" method.
    """

    def __init__(
        self,
        *,
        client: CodeEngineV2,
        project_id: str,
        limit: int = None,
    ) -> None:
        """
        Initialize a SecretsPager object.
        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of secrets per page.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._project_id = project_id
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of Secret.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_secrets(
            project_id=self._project_id,
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('secrets')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of Secret.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results

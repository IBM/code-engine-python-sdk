# coding: utf-8

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

# IBM OpenAPI SDK Code Generator Version: 3.94.1-71478489-20240820-161623

"""
REST API for Code Engine

API Version: 2.0.0
"""

from enum import Enum
from typing import Dict, List, Optional
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
        version: Optional[str] = None,
    ) -> 'CodeEngineV2':
        """
        Return a new client for the Code Engine service using the specified
               parameters and external configuration.

        :param str version: (optional) The API version, in format `YYYY-MM-DD`. For
               the API behavior documented here, specify any date between `2021-03-31` and
               `2024-11-18`.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator,
            version,
        )
        service.configure_service(service_name)
        return service

    def __init__(
        self,
        authenticator: Authenticator = None,
        version: Optional[str] = None,
    ) -> None:
        """
        Construct a new client for the Code Engine service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.

        :param str version: (optional) The API version, in format `YYYY-MM-DD`. For
               the API behavior documented here, specify any date between `2021-03-31` and
               `2024-11-18`.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)
        self.version = version

    #########################
    # Projects
    #########################

    def list_projects(
        self,
        *,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List all projects.

        List all projects in the current account.

        :param int limit: (optional) Optional maximum number of projects per page.
        :param str start: (optional) An optional token that indicates the beginning
               of the page of results to be returned. Any additional query parameters are
               ignored if a page token is present. If omitted, the first page of results
               is returned. This value is obtained from the 'start' query parameter in the
               `next` object of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectList` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_projects',
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
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_project(
        self,
        name: str,
        *,
        resource_group_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        **kwargs,
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_project',
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
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_project(
        self,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_project',
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
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_project(
        self,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_project',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def list_allowed_outbound_destination(
        self,
        project_id: str,
        *,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List allowed outbound destinations.

        List all allowed outbound destinations in a project.

        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of allowed outbound
               destinations per page.
        :param str start: (optional) An optional token that indicates the beginning
               of the page of results to be returned. If omitted, the first page of
               results is returned. This value is obtained from the 'start' query
               parameter in the `next` object of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AllowedOutboundDestinationList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_allowed_outbound_destination',
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
        url = '/projects/{project_id}/allowed_outbound_destinations'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_allowed_outbound_destination(
        self,
        project_id: str,
        allowed_outbound_destination: 'AllowedOutboundDestinationPrototype',
        **kwargs,
    ) -> DetailedResponse:
        """
        Create an allowed outbound destination.

        Create an allowed outbound destination.

        :param str project_id: The ID of the project.
        :param AllowedOutboundDestinationPrototype allowed_outbound_destination:
               AllowedOutboundDestination prototype.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AllowedOutboundDestination` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if allowed_outbound_destination is None:
            raise ValueError('allowed_outbound_destination must be provided')
        if isinstance(allowed_outbound_destination, AllowedOutboundDestinationPrototype):
            allowed_outbound_destination = convert_model(allowed_outbound_destination)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_allowed_outbound_destination',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = json.dumps(allowed_outbound_destination)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/allowed_outbound_destinations'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_allowed_outbound_destination(
        self,
        project_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get an allowed outbound destination.

        Display the details of an allowed outbound destination.

        :param str project_id: The ID of the project.
        :param str name: The name of your allowed outbound destination.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AllowedOutboundDestination` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_allowed_outbound_destination',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/allowed_outbound_destinations/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_allowed_outbound_destination(
        self,
        project_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete an allowed outbound destination.

        Delete an allowed outbound destination.

        :param str project_id: The ID of the project.
        :param str name: The name of your allowed outbound destination.
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_allowed_outbound_destination',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/allowed_outbound_destinations/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_allowed_outbound_destination(
        self,
        project_id: str,
        name: str,
        if_match: str,
        allowed_outbound_destination: 'AllowedOutboundDestinationPatch',
        **kwargs,
    ) -> DetailedResponse:
        """
        Update an allowed outbound destination.

        Update an allowed outbound destination.

        :param str project_id: The ID of the project.
        :param str name: The name of your allowed outbound destination.
        :param str if_match: Version of the allowed outbound destination to be
               updated. Specify the version that you retrieved as entity_tag (ETag header)
               when reading the allowed outbound destination. This value helps identifying
               parallel usage of this API. Pass * to indicate to update any version
               available. This might result in stale updates.
        :param AllowedOutboundDestinationPatch allowed_outbound_destination:
               AllowedOutboundDestination patch.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AllowedOutboundDestination` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        if not if_match:
            raise ValueError('if_match must be provided')
        if allowed_outbound_destination is None:
            raise ValueError('allowed_outbound_destination must be provided')
        if isinstance(allowed_outbound_destination, AllowedOutboundDestinationPatch):
            allowed_outbound_destination = convert_model(allowed_outbound_destination)
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='update_allowed_outbound_destination',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = json.dumps(allowed_outbound_destination)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/allowed_outbound_destinations/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_project_egress_ips(
        self,
        project_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List egress IP addresses.

        Lists all egress IP addresses (public and private) that are used by components
        running in this project. For information about using egress IP addresses, see
        [Code Engine public and private IP
        addresses](https://cloud.ibm.com/docs/codeengine?topic=codeengine-network-addresses).

        :param str project_id: The ID of the project.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectEgressIPAddresses` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_project_egress_ips',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/egress_ips'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_project_status_details(
        self,
        project_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get the status details for a project.

        Retrieves status details about the given project.

        :param str project_id: The ID of the project.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectStatusDetails` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_project_status_details',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/status_details'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Applications
    #########################

    def list_apps(
        self,
        project_id: str,
        *,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List applications.

        List all applications in a project.

        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of apps per page.
        :param str start: (optional) An optional token that indicates the beginning
               of the page of results to be returned. If omitted, the first page of
               results is returned. This value is obtained from the 'start' query
               parameter in the `next` object of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AppList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_apps',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
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
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_app(
        self,
        project_id: str,
        image_reference: str,
        name: str,
        *,
        image_port: Optional[int] = None,
        image_secret: Optional[str] = None,
        managed_domain_mappings: Optional[str] = None,
        probe_liveness: Optional['ProbePrototype'] = None,
        probe_readiness: Optional['ProbePrototype'] = None,
        run_arguments: Optional[List[str]] = None,
        run_as_user: Optional[int] = None,
        run_commands: Optional[List[str]] = None,
        run_env_variables: Optional[List['EnvVarPrototype']] = None,
        run_service_account: Optional[str] = None,
        run_volume_mounts: Optional[List['VolumeMountPrototype']] = None,
        scale_concurrency: Optional[int] = None,
        scale_concurrency_target: Optional[int] = None,
        scale_cpu_limit: Optional[str] = None,
        scale_down_delay: Optional[int] = None,
        scale_ephemeral_storage_limit: Optional[str] = None,
        scale_initial_instances: Optional[int] = None,
        scale_max_instances: Optional[int] = None,
        scale_memory_limit: Optional[str] = None,
        scale_min_instances: Optional[int] = None,
        scale_request_timeout: Optional[int] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create an application.

        Create an application.

        :param str project_id: The ID of the project.
        :param str image_reference: The name of the image that is used for this
               app. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and
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
        :param ProbePrototype probe_liveness: (optional) Request model for probes.
        :param ProbePrototype probe_readiness: (optional) Request model for probes.
        :param List[str] run_arguments: (optional) Optional arguments for the app
               that are passed to start the container. If not specified an empty string
               array will be applied and the arguments specified by the container image,
               will be used to start the container.
        :param int run_as_user: (optional) Optional user ID (UID) to run the app.
        :param List[str] run_commands: (optional) Optional commands for the app
               that are passed to start the container. If not specified an empty string
               array will be applied and the command specified by the container image,
               will be used to start the container.
        :param List[EnvVarPrototype] run_env_variables: (optional) Optional
               references to config maps, secrets or literal values that are exposed as
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
        :param int scale_down_delay: (optional) Optional amount of time in seconds
               that delays the scale-down behavior for an app instance.
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
        if probe_liveness is not None:
            probe_liveness = convert_model(probe_liveness)
        if probe_readiness is not None:
            probe_readiness = convert_model(probe_readiness)
        if run_env_variables is not None:
            run_env_variables = [convert_model(x) for x in run_env_variables]
        if run_volume_mounts is not None:
            run_volume_mounts = [convert_model(x) for x in run_volume_mounts]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_app',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'image_reference': image_reference,
            'name': name,
            'image_port': image_port,
            'image_secret': image_secret,
            'managed_domain_mappings': managed_domain_mappings,
            'probe_liveness': probe_liveness,
            'probe_readiness': probe_readiness,
            'run_arguments': run_arguments,
            'run_as_user': run_as_user,
            'run_commands': run_commands,
            'run_env_variables': run_env_variables,
            'run_service_account': run_service_account,
            'run_volume_mounts': run_volume_mounts,
            'scale_concurrency': scale_concurrency,
            'scale_concurrency_target': scale_concurrency_target,
            'scale_cpu_limit': scale_cpu_limit,
            'scale_down_delay': scale_down_delay,
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
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_app(
        self,
        project_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_app',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/apps/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_app(
        self,
        project_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_app',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/apps/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_app(
        self,
        project_id: str,
        name: str,
        if_match: str,
        app: 'AppPatch',
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='update_app',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

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
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_app_revisions(
        self,
        project_id: str,
        app_name: str,
        *,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        **kwargs,
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
               parameter in the `next` object of the operation response.
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_app_revisions',
        )
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'start': start,
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'app_name']
        path_param_values = self.encode_path_vars(project_id, app_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/apps/{app_name}/revisions'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_app_revision(
        self,
        project_id: str,
        app_name: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_app_revision',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'app_name', 'name']
        path_param_values = self.encode_path_vars(project_id, app_name, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/apps/{app_name}/revisions/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_app_revision(
        self,
        project_id: str,
        app_name: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_app_revision',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'app_name', 'name']
        path_param_values = self.encode_path_vars(project_id, app_name, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/apps/{app_name}/revisions/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def list_app_instances(
        self,
        project_id: str,
        app_name: str,
        *,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List application instances.

        List all instances of an application.

        :param str project_id: The ID of the project.
        :param str app_name: The name of your application.
        :param int limit: (optional) Optional maximum number of apps per page.
        :param str start: (optional) An optional token that indicates the beginning
               of the page of results to be returned. If omitted, the first page of
               results is returned. This value is obtained from the 'start' query
               parameter in the `next` object of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AppInstanceList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not app_name:
            raise ValueError('app_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_app_instances',
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
        url = '/projects/{project_id}/apps/{app_name}/instances'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Jobs
    #########################

    def list_jobs(
        self,
        project_id: str,
        *,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List jobs.

        List all jobs in a project.

        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of jobs per page.
        :param str start: (optional) An optional token that indicates the beginning
               of the page of results to be returned. If omitted, the first page of
               results is returned. This value is obtained from the 'start' query
               parameter in the `next` object of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `JobList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_jobs',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
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
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_job(
        self,
        project_id: str,
        image_reference: str,
        name: str,
        *,
        image_secret: Optional[str] = None,
        run_arguments: Optional[List[str]] = None,
        run_as_user: Optional[int] = None,
        run_commands: Optional[List[str]] = None,
        run_env_variables: Optional[List['EnvVarPrototype']] = None,
        run_mode: Optional[str] = None,
        run_service_account: Optional[str] = None,
        run_volume_mounts: Optional[List['VolumeMountPrototype']] = None,
        scale_array_spec: Optional[str] = None,
        scale_cpu_limit: Optional[str] = None,
        scale_ephemeral_storage_limit: Optional[str] = None,
        scale_max_execution_time: Optional[int] = None,
        scale_memory_limit: Optional[str] = None,
        scale_retry_limit: Optional[int] = None,
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
               is provided, too. This property must not be set on a job run, which
               references a job template.
        :param List[str] run_arguments: (optional) Set arguments for the job that
               are passed to start job run containers. If not specified an empty string
               array will be applied and the arguments specified by the container image,
               will be used to start the container.
        :param int run_as_user: (optional) The user ID (UID) to run the job.
        :param List[str] run_commands: (optional) Set commands for the job that are
               passed to start job run containers. If not specified an empty string array
               will be applied and the command specified by the container image, will be
               used to start the container.
        :param List[EnvVarPrototype] run_env_variables: (optional) Optional
               references to config maps, secrets or literal values.
        :param str run_mode: (optional) The mode for runs of the job. Valid values
               are `task` and `daemon`. In `task` mode, the `max_execution_time` and
               `retry_limit` properties apply. In `daemon` mode, since there is no timeout
               and failed instances are restarted indefinitely, the `max_execution_time`
               and `retry_limit` properties are not allowed.
        :param str run_service_account: (optional) The name of the service account.
               For built-in service accounts, you can use the shortened names `manager`,
               `none`, `reader`, and `writer`. This property must not be set on a job run,
               which references a job template.
        :param List[VolumeMountPrototype] run_volume_mounts: (optional) Optional
               mounts of config maps or a secrets.
        :param str scale_array_spec: (optional) Define a custom set of array
               indices as a comma-separated list containing single values and
               hyphen-separated ranges, such as  5,12-14,23,27. Each instance gets its
               array index value from the environment variable JOB_INDEX. The number of
               unique array indices that you specify with this parameter determines the
               number of job instances to run.
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
               in seconds for runs of the job. This property can only be specified if
               `run_mode` is `task`.
        :param str scale_memory_limit: (optional) Optional amount of memory set for
               the instance of the job. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
               The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G
               and M are the shorthand expressions for GB and MB. For more information see
               [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param int scale_retry_limit: (optional) The number of times to rerun an
               instance of the job before the job is marked as failed. This property can
               only be specified if `run_mode` is `task`.
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_job',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

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
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_job(
        self,
        project_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_job',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/jobs/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_job(
        self,
        project_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_job',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/jobs/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_job(
        self,
        project_id: str,
        name: str,
        if_match: str,
        job: 'JobPatch',
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='update_job',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

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
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_job_runs(
        self,
        project_id: str,
        *,
        job_name: Optional[str] = None,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List job runs.

        List all job runs in a project.

        :param str project_id: The ID of the project.
        :param str job_name: (optional) Optional name of the job that you want to
               use to filter.
        :param int limit: (optional) Optional maximum number of job runs per page.
        :param str start: (optional) An optional token that indicates the beginning
               of the page of results to be returned. If omitted, the first page of
               results is returned. This value is obtained from the 'start' query
               parameter in the `next` object of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `JobRunList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_job_runs',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
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
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_job_run(
        self,
        project_id: str,
        *,
        image_reference: Optional[str] = None,
        image_secret: Optional[str] = None,
        job_name: Optional[str] = None,
        name: Optional[str] = None,
        run_arguments: Optional[List[str]] = None,
        run_as_user: Optional[int] = None,
        run_commands: Optional[List[str]] = None,
        run_env_variables: Optional[List['EnvVarPrototype']] = None,
        run_mode: Optional[str] = None,
        run_service_account: Optional[str] = None,
        run_volume_mounts: Optional[List['VolumeMountPrototype']] = None,
        scale_array_size_variable_override: Optional[int] = None,
        scale_array_spec: Optional[str] = None,
        scale_cpu_limit: Optional[str] = None,
        scale_ephemeral_storage_limit: Optional[str] = None,
        scale_max_execution_time: Optional[int] = None,
        scale_memory_limit: Optional[str] = None,
        scale_retry_limit: Optional[int] = None,
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
               is provided, too. This property must not be set on a job run, which
               references a job template.
        :param str job_name: (optional) Optional name of the job on which this job
               run is based on. If specified, the job run will inherit the configuration
               of the referenced job.
        :param str name: (optional) The name of the job. Use a name that is unique
               within the project.
        :param List[str] run_arguments: (optional) Set arguments for the job that
               are passed to start job run containers. If not specified an empty string
               array will be applied and the arguments specified by the container image,
               will be used to start the container.
        :param int run_as_user: (optional) The user ID (UID) to run the job.
        :param List[str] run_commands: (optional) Set commands for the job that are
               passed to start job run containers. If not specified an empty string array
               will be applied and the command specified by the container image, will be
               used to start the container.
        :param List[EnvVarPrototype] run_env_variables: (optional) Optional
               references to config maps, secrets or literal values.
        :param str run_mode: (optional) The mode for runs of the job. Valid values
               are `task` and `daemon`. In `task` mode, the `max_execution_time` and
               `retry_limit` properties apply. In `daemon` mode, since there is no timeout
               and failed instances are restarted indefinitely, the `max_execution_time`
               and `retry_limit` properties are not allowed.
        :param str run_service_account: (optional) The name of the service account.
               For built-in service accounts, you can use the shortened names `manager`,
               `none`, `reader`, and `writer`. This property must not be set on a job run,
               which references a job template.
        :param List[VolumeMountPrototype] run_volume_mounts: (optional) Optional
               mounts of config maps or a secrets.
        :param int scale_array_size_variable_override: (optional) Optional value to
               override the JOB_ARRAY_SIZE environment variable for a job run.
        :param str scale_array_spec: (optional) Define a custom set of array
               indices as a comma-separated list containing single values and
               hyphen-separated ranges, such as  5,12-14,23,27. Each instance gets its
               array index value from the environment variable JOB_INDEX. The number of
               unique array indices that you specify with this parameter determines the
               number of job instances to run.
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
               in seconds for runs of the job. This property can only be specified if
               `run_mode` is `task`.
        :param str scale_memory_limit: (optional) Optional amount of memory set for
               the instance of the job. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
               The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G
               and M are the shorthand expressions for GB and MB. For more information see
               [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param int scale_retry_limit: (optional) The number of times to rerun an
               instance of the job before the job is marked as failed. This property can
               only be specified if `run_mode` is `task`.
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_job_run',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

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
            'scale_array_size_variable_override': scale_array_size_variable_override,
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
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_job_run(
        self,
        project_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_job_run',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/job_runs/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_job_run(
        self,
        project_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_job_run',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/job_runs/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Functions
    #########################

    def list_function_runtimes(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        List the function runtimes.

        List all valid function runtimes.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `FunctionRuntimeList` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_function_runtimes',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/function_runtimes'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def list_functions(
        self,
        project_id: str,
        *,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List functions.

        List all functions in a project.

        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of functions per page.
        :param str start: (optional) An optional token that indicates the beginning
               of the page of results to be returned. If omitted, the first page of
               results is returned. This value is obtained from the 'start' query
               parameter in the 'next_url' field of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `FunctionList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_functions',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
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
        url = '/projects/{project_id}/functions'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_function(
        self,
        project_id: str,
        code_reference: str,
        name: str,
        runtime: str,
        *,
        code_binary: Optional[bool] = None,
        code_main: Optional[str] = None,
        code_secret: Optional[str] = None,
        managed_domain_mappings: Optional[str] = None,
        run_env_variables: Optional[List['EnvVarPrototype']] = None,
        scale_concurrency: Optional[int] = None,
        scale_cpu_limit: Optional[str] = None,
        scale_down_delay: Optional[int] = None,
        scale_max_execution_time: Optional[int] = None,
        scale_memory_limit: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a function.

        Create a function.

        :param str project_id: The ID of the project.
        :param str code_reference: Specifies either a reference to a code bundle or
               the source code itself. To specify the source code, use the data URL scheme
               and include the source code as base64 encoded. The data URL scheme is
               defined in [RFC 2397](https://tools.ietf.org/html/rfc2397).
        :param str name: The name of the function. Use a name that is unique within
               the project.
        :param str runtime: The managed runtime used to execute the injected code.
        :param bool code_binary: (optional) Specifies whether the code is binary or
               not. Defaults to false when `code_reference` is set to a data URL. When
               `code_reference` is set to a code bundle URL, this field is always true.
        :param str code_main: (optional) Specifies the name of the function that
               should be invoked.
        :param str code_secret: (optional) The name of the secret that is used to
               access the specified `code_reference`. The secret is used to authenticate
               with a non-public endpoint that is specified as`code_reference`.
        :param str managed_domain_mappings: (optional) Optional value controlling
               which of the system managed domain mappings will be setup for the function.
               Valid values are 'local_public', 'local_private' and 'local'. Visibility
               can only be 'local_private' if the project supports function private
               visibility.
        :param List[EnvVarPrototype] run_env_variables: (optional) Optional
               references to config maps, secrets or literal values.
        :param int scale_concurrency: (optional) Number of parallel requests
               handled by a single instance, supported only by Node.js, default is `1`.
        :param str scale_cpu_limit: (optional) Optional amount of CPU set for the
               instance of the function. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
        :param int scale_down_delay: (optional) Optional amount of time in seconds
               that delays the scale down behavior for a function.
        :param int scale_max_execution_time: (optional) Timeout in secs after which
               the function is terminated.
        :param str scale_memory_limit: (optional) Optional amount of memory set for
               the instance of the function. For valid values see [Supported memory and
               CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
               The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G
               and M are the shorthand expressions for GB and MB. For more information see
               [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Function` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if code_reference is None:
            raise ValueError('code_reference must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if runtime is None:
            raise ValueError('runtime must be provided')
        if run_env_variables is not None:
            run_env_variables = [convert_model(x) for x in run_env_variables]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_function',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'code_reference': code_reference,
            'name': name,
            'runtime': runtime,
            'code_binary': code_binary,
            'code_main': code_main,
            'code_secret': code_secret,
            'managed_domain_mappings': managed_domain_mappings,
            'run_env_variables': run_env_variables,
            'scale_concurrency': scale_concurrency,
            'scale_cpu_limit': scale_cpu_limit,
            'scale_down_delay': scale_down_delay,
            'scale_max_execution_time': scale_max_execution_time,
            'scale_memory_limit': scale_memory_limit,
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
        url = '/projects/{project_id}/functions'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_function(
        self,
        project_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a function.

        Display the details of a function.

        :param str project_id: The ID of the project.
        :param str name: The name of your function.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Function` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_function',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/functions/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_function(
        self,
        project_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a function.

        Delete a function.

        :param str project_id: The ID of the project.
        :param str name: The name of your function.
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_function',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/functions/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_function(
        self,
        project_id: str,
        name: str,
        if_match: str,
        function: 'FunctionPatch',
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a function.

        Update the given function.

        :param str project_id: The ID of the project.
        :param str name: The name of your function.
        :param str if_match: Version of the function settings to be updated.
               Specify the version that you retrieved as entity_tag (ETag header) when
               reading the function. This value helps identifying parallel usage of this
               API. Pass * to indicate to update any version available. This might result
               in stale updates.
        :param FunctionPatch function: Function patch.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Function` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        if not if_match:
            raise ValueError('if_match must be provided')
        if function is None:
            raise ValueError('function must be provided')
        if isinstance(function, FunctionPatch):
            function = convert_model(function)
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='update_function',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = json.dumps(function)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/functions/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Service bindings
    #########################

    def list_bindings(
        self,
        project_id: str,
        *,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List bindings.

        List all bindings in a project.

        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of bindings per page.
        :param str start: (optional) An optional token that indicates the beginning
               of the page of results to be returned. If omitted, the first page of
               results is returned. This value is obtained from the 'start' query
               parameter in the `next` object of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BindingList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_bindings',
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
        url = '/projects/{project_id}/bindings'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_binding(
        self,
        project_id: str,
        component: 'ComponentRef',
        prefix: str,
        secret_name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a binding.

        Create a binding. Creating a service binding with a Code Engine app will update
        the app, creating a new revision. For more information see the
        [documentaion](https://cloud.ibm.com/docs/codeengine?topic=codeengine-service-binding).

        :param str project_id: The ID of the project.
        :param ComponentRef component: A reference to another component.
        :param str prefix: Optional value that is set as prefix in the component
               that is bound. Will be generated if not provided.
        :param str secret_name: The service access secret that is bound to a
               component.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Binding` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if component is None:
            raise ValueError('component must be provided')
        if prefix is None:
            raise ValueError('prefix must be provided')
        if secret_name is None:
            raise ValueError('secret_name must be provided')
        component = convert_model(component)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_binding',
        )
        headers.update(sdk_headers)

        data = {
            'component': component,
            'prefix': prefix,
            'secret_name': secret_name,
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
        url = '/projects/{project_id}/bindings'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_binding(
        self,
        project_id: str,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a binding.

        Display the details of a binding.

        :param str project_id: The ID of the project.
        :param str id: The id of your binding.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Binding` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_binding',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'id']
        path_param_values = self.encode_path_vars(project_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/bindings/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_binding(
        self,
        project_id: str,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a binding.

        Delete a binding.

        :param str project_id: The ID of the project.
        :param str id: The id of your binding.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_binding',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'id']
        path_param_values = self.encode_path_vars(project_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/bindings/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Image builds
    #########################

    def list_builds(
        self,
        project_id: str,
        *,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List builds.

        List all builds in a project.

        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of builds per page.
        :param str start: (optional) An optional token that indicates the beginning
               of the page of results to be returned. If omitted, the first page of
               results is returned. This value is obtained from the 'start' query
               parameter in the `next` object of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BuildList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_builds',
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
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_build(
        self,
        project_id: str,
        name: str,
        output_image: str,
        output_secret: str,
        strategy_type: str,
        *,
        source_context_dir: Optional[str] = None,
        source_revision: Optional[str] = None,
        source_secret: Optional[str] = None,
        source_type: Optional[str] = None,
        source_url: Optional[str] = None,
        strategy_size: Optional[str] = None,
        strategy_spec_file: Optional[str] = None,
        timeout: Optional[int] = None,
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
        :param str strategy_type: The strategy to use for building the image.
        :param str source_context_dir: (optional) Optional directory in the
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
               `large`, `xlarge`, `xxlarge`.
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
        if strategy_type is None:
            raise ValueError('strategy_type must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_build',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'output_image': output_image,
            'output_secret': output_secret,
            'strategy_type': strategy_type,
            'source_context_dir': source_context_dir,
            'source_revision': source_revision,
            'source_secret': source_secret,
            'source_type': source_type,
            'source_url': source_url,
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
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_build(
        self,
        project_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_build',
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
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_build(
        self,
        project_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_build',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/builds/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_build(
        self,
        project_id: str,
        name: str,
        if_match: str,
        build: 'BuildPatch',
        **kwargs,
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='update_build',
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
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_build_runs(
        self,
        project_id: str,
        *,
        build_name: Optional[str] = None,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        **kwargs,
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
               parameter in the `next` object of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BuildRunList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_build_runs',
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
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_build_run(
        self,
        project_id: str,
        *,
        build_name: Optional[str] = None,
        name: Optional[str] = None,
        output_image: Optional[str] = None,
        output_secret: Optional[str] = None,
        service_account: Optional[str] = None,
        source_context_dir: Optional[str] = None,
        source_revision: Optional[str] = None,
        source_secret: Optional[str] = None,
        source_type: Optional[str] = None,
        source_url: Optional[str] = None,
        strategy_size: Optional[str] = None,
        strategy_spec_file: Optional[str] = None,
        strategy_type: Optional[str] = None,
        timeout: Optional[int] = None,
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
        :param str service_account: (optional) Optional service account, which is
               used for resource control.” or “Optional service account that is used for
               resource control.
        :param str source_context_dir: (optional) Optional directory in the
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
               `large`, `xlarge`, `xxlarge`.
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_build_run',
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
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_build_run(
        self,
        project_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_build_run',
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
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_build_run(
        self,
        project_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_build_run',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/build_runs/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Domain mappings
    #########################

    def list_domain_mappings(
        self,
        project_id: str,
        *,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List domain mappings.

        List all domain mappings in a project.

        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of domain mappings per
               page.
        :param str start: (optional) An optional token that indicates the beginning
               of the page of results to be returned. If omitted, the first page of
               results is returned. This value is obtained from the 'start' query
               parameter in the `next` object of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DomainMappingList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_domain_mappings',
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
        url = '/projects/{project_id}/domain_mappings'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_domain_mapping(
        self,
        project_id: str,
        component: 'ComponentRef',
        name: str,
        tls_secret: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a domain mapping.

        Create a domain mapping.

        :param str project_id: The ID of the project.
        :param ComponentRef component: A reference to another component.
        :param str name: The name of the domain mapping.
        :param str tls_secret: The name of the TLS secret that includes the
               certificate and private key of this domain mapping.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DomainMapping` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if component is None:
            raise ValueError('component must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if tls_secret is None:
            raise ValueError('tls_secret must be provided')
        component = convert_model(component)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_domain_mapping',
        )
        headers.update(sdk_headers)

        data = {
            'component': component,
            'name': name,
            'tls_secret': tls_secret,
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
        url = '/projects/{project_id}/domain_mappings'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_domain_mapping(
        self,
        project_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a domain mapping.

        Get domain mapping.

        :param str project_id: The ID of the project.
        :param str name: The name of your domain mapping.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DomainMapping` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_domain_mapping',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/domain_mappings/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_domain_mapping(
        self,
        project_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a domain mapping.

        Delete a domain mapping.

        :param str project_id: The ID of the project.
        :param str name: The name of your domain mapping.
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_domain_mapping',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/domain_mappings/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_domain_mapping(
        self,
        project_id: str,
        name: str,
        if_match: str,
        domain_mapping: 'DomainMappingPatch',
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a domain mapping.

        Update a domain mapping.

        :param str project_id: The ID of the project.
        :param str name: The name of your domain mapping.
        :param str if_match: Version of the domain mapping to be updated. Specify
               the version that you retrieved as entity_tag (ETag header) when reading the
               domain mapping. This value helps identify parallel usage of this API. Pass
               * to indicate to update any version available. This might result in stale
               updates.
        :param DomainMappingPatch domain_mapping: DomainMapping patch.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DomainMapping` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not name:
            raise ValueError('name must be provided')
        if not if_match:
            raise ValueError('if_match must be provided')
        if domain_mapping is None:
            raise ValueError('domain_mapping must be provided')
        if isinstance(domain_mapping, DomainMappingPatch):
            domain_mapping = convert_model(domain_mapping)
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='update_domain_mapping',
        )
        headers.update(sdk_headers)

        data = json.dumps(domain_mapping)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/domain_mappings/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Secrets and configmaps
    #########################

    def list_config_maps(
        self,
        project_id: str,
        *,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List config maps.

        List all config maps in a project.

        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of config maps per
               page.
        :param str start: (optional) An optional token that indicates the beginning
               of the page of results to be returned. If omitted, the first page of
               results is returned. This value is obtained from the 'start' query
               parameter in the `next` object of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ConfigMapList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_config_maps',
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
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_config_map(
        self,
        project_id: str,
        name: str,
        *,
        data: Optional[dict] = None,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_config_map',
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
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_config_map(
        self,
        project_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_config_map',
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
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_config_map(
        self,
        project_id: str,
        name: str,
        if_match: str,
        *,
        data: Optional[dict] = None,
        **kwargs,
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='replace_config_map',
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
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_config_map(
        self,
        project_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_config_map',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/config_maps/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def list_secrets(
        self,
        project_id: str,
        *,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List secrets.

        List all secrets in a project.

        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of secrets per page.
        :param str start: (optional) An optional token that indicates the beginning
               of the page of results to be returned. If omitted, the first page of
               results is returned. This value is obtained from the 'start' query
               parameter in the `next` object of the operation response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SecretList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_secrets',
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
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_secret(
        self,
        project_id: str,
        format: str,
        name: str,
        *,
        data: Optional['SecretData'] = None,
        service_access: Optional['ServiceAccessSecretPrototypeProps'] = None,
        service_operator: Optional['OperatorSecretPrototypeProps'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a secret.

        Create a secret.

        :param str project_id: The ID of the project.
        :param str format: Specify the format of the secret. The format of the
               secret will determine how the secret is used.
        :param str name: The name of the secret.
        :param SecretData data: (optional) Data container that allows to specify
               config parameters and their values as a key-value map. Each key field must
               consist of alphanumeric characters, `-`, `_` or `.` and must not exceed a
               max length of 253 characters. Each value field can consists of any
               character and must not exceed a max length of 1048576 characters.
        :param ServiceAccessSecretPrototypeProps service_access: (optional)
               Properties for Service Access Secrets.
        :param OperatorSecretPrototypeProps service_operator: (optional) Properties
               for the IBM Cloud Operator Secrets.
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
        if data is not None:
            data = convert_model(data)
        if service_access is not None:
            service_access = convert_model(service_access)
        if service_operator is not None:
            service_operator = convert_model(service_operator)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_secret',
        )
        headers.update(sdk_headers)

        data = {
            'format': format,
            'name': name,
            'data': data,
            'service_access': service_access,
            'service_operator': service_operator,
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
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_secret(
        self,
        project_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_secret',
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
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_secret(
        self,
        project_id: str,
        name: str,
        if_match: str,
        format: str,
        *,
        data: Optional['SecretData'] = None,
        **kwargs,
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
        :param str format: Specify the format of the secret. The format of the
               secret will determine how the secret is used.
        :param SecretData data: (optional) Data container that allows to specify
               config parameters and their values as a key-value map. Each key field must
               consist of alphanumeric characters, `-`, `_` or `.` and must not exceed a
               max length of 253 characters. Each value field can consists of any
               character and must not exceed a max length of 1048576 characters.
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
        if format is None:
            raise ValueError('format must be provided')
        if data is not None:
            data = convert_model(data)
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='replace_secret',
        )
        headers.update(sdk_headers)

        data = {
            'format': format,
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
        url = '/projects/{project_id}/secrets/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_secret(
        self,
        project_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
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
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_secret',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'name']
        path_param_values = self.encode_path_vars(project_id, name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/projects/{project_id}/secrets/{name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class AllowedOutboundDestination:
    """
    AllowedOutboundDestination Describes the model of an allowed outbound destination.

    :param str entity_tag: The version of the allowed outbound destination, which is
          used to achieve optimistic locking.
    :param str type: Specify the type of the allowed outbound destination. Allowed
          types are: 'cidr_block'.
    """

    def __init__(
        self,
        entity_tag: str,
        type: str,
    ) -> None:
        """
        Initialize a AllowedOutboundDestination object.

        :param str entity_tag: The version of the allowed outbound destination,
               which is used to achieve optimistic locking.
        :param str type: Specify the type of the allowed outbound destination.
               Allowed types are: 'cidr_block'.
        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['AllowedOutboundDestinationCidrBlockData'])
        )
        raise Exception(msg)

    class TypeEnum(str, Enum):
        """
        Specify the type of the allowed outbound destination. Allowed types are:
        'cidr_block'.
        """

        CIDR_BLOCK = 'cidr_block'


class AllowedOutboundDestinationList:
    """
    Contains a list of allowed outbound destinations and pagination information.

    :param List[AllowedOutboundDestination] allowed_outbound_destinations: List of
          all allowed outbound destinations.
    :param ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :param int limit: Maximum number of resources per page.
    :param ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    """

    def __init__(
        self,
        allowed_outbound_destinations: List['AllowedOutboundDestination'],
        limit: int,
        *,
        first: Optional['ListFirstMetadata'] = None,
        next: Optional['ListNextMetadata'] = None,
    ) -> None:
        """
        Initialize a AllowedOutboundDestinationList object.

        :param List[AllowedOutboundDestination] allowed_outbound_destinations: List
               of all allowed outbound destinations.
        :param int limit: Maximum number of resources per page.
        :param ListFirstMetadata first: (optional) Describes properties needed to
               retrieve the first page of a result list.
        :param ListNextMetadata next: (optional) Describes properties needed to
               retrieve the next page of a result list.
        """
        self.allowed_outbound_destinations = allowed_outbound_destinations
        self.first = first
        self.limit = limit
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AllowedOutboundDestinationList':
        """Initialize a AllowedOutboundDestinationList object from a json dictionary."""
        args = {}
        if (allowed_outbound_destinations := _dict.get('allowed_outbound_destinations')) is not None:
            args['allowed_outbound_destinations'] = allowed_outbound_destinations
        else:
            raise ValueError(
                'Required property \'allowed_outbound_destinations\' not present in AllowedOutboundDestinationList JSON'
            )
        if (first := _dict.get('first')) is not None:
            args['first'] = ListFirstMetadata.from_dict(first)
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in AllowedOutboundDestinationList JSON')
        if (next := _dict.get('next')) is not None:
            args['next'] = ListNextMetadata.from_dict(next)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AllowedOutboundDestinationList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'allowed_outbound_destinations') and self.allowed_outbound_destinations is not None:
            allowed_outbound_destinations_list = []
            for v in self.allowed_outbound_destinations:
                if isinstance(v, dict):
                    allowed_outbound_destinations_list.append(v)
                else:
                    allowed_outbound_destinations_list.append(v.to_dict())
            _dict['allowed_outbound_destinations'] = allowed_outbound_destinations_list
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
        """Return a `str` version of this AllowedOutboundDestinationList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AllowedOutboundDestinationList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AllowedOutboundDestinationList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AllowedOutboundDestinationPatch:
    """
    AllowedOutboundDestinationPatch is the request model for allowed outbound destination
    update operations.

    :param str type: (optional) Specify the type of the allowed outbound
          destination. Allowed types are: 'cidr_block'.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
    ) -> None:
        """
        Initialize a AllowedOutboundDestinationPatch object.

        :param str type: (optional) Specify the type of the allowed outbound
               destination. Allowed types are: 'cidr_block'.
        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['AllowedOutboundDestinationPatchCidrBlockDataPatch'])
        )
        raise Exception(msg)

    class TypeEnum(str, Enum):
        """
        Specify the type of the allowed outbound destination. Allowed types are:
        'cidr_block'.
        """

        CIDR_BLOCK = 'cidr_block'


class AllowedOutboundDestinationPrototype:
    """
    AllowedOutboundDestinationPrototype is the request model for allowed outbound
    destination create operations.

    :param str type: Specify the type of the allowed outbound destination. Allowed
          types are: 'cidr_block'.
    """

    def __init__(
        self,
        type: str,
    ) -> None:
        """
        Initialize a AllowedOutboundDestinationPrototype object.

        :param str type: Specify the type of the allowed outbound destination.
               Allowed types are: 'cidr_block'.
        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['AllowedOutboundDestinationPrototypeCidrBlockDataPrototype'])
        )
        raise Exception(msg)

    class TypeEnum(str, Enum):
        """
        Specify the type of the allowed outbound destination. Allowed types are:
        'cidr_block'.
        """

        CIDR_BLOCK = 'cidr_block'


class App:
    """
    App is the response model for app resources.

    :param str build: (optional) Reference to a build that is associated with the
          application.
    :param str build_run: (optional) Reference to a build run that is associated
          with the application.
    :param List[EnvVar] computed_env_variables: (optional) References to config
          maps, secrets or literal values, which are defined and set by Code Engine and
          are exposed as environment variables in the application.
    :param str created_at: (optional) The timestamp when the resource was created.
    :param str endpoint: (optional) Optional URL to invoke the app. Depending on
          visibility,  this is accessible publicly or in the private network only. Empty
          in case 'managed_domain_mappings' is set to 'local'.
    :param str endpoint_internal: (optional) The URL to the app that is only visible
          within the project.
    :param str entity_tag: The version of the app instance, which is used to achieve
          optimistic locking.
    :param str href: (optional) When you provision a new app,  a URL is created
          identifying the location of the instance.
    :param str id: (optional) The identifier of the resource.
    :param int image_port: (optional) Optional port the app listens on. While the
          app will always be exposed via port `443` for end users, this port is used to
          connect to the port that is exposed by the container image.
    :param str image_reference: The name of the image that is used for this app. The
          format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and `TAG` are
          optional. If `REGISTRY` is not specified, the default is `docker.io`. If `TAG`
          is not specified, the default is `latest`. If the image reference points to a
          registry that requires authentication, make sure to also specify the property
          `image_secret`.
    :param str image_secret: (optional) Optional name of the image registry access
          secret. The image registry access secret is used to authenticate with a private
          registry when you download the container image. If the image reference points to
          a registry that requires authentication, the app will be created but cannot
          reach the ready status, until this property is provided, too.
    :param str managed_domain_mappings: Optional value controlling which of the
          system managed domain mappings will be setup for the application. Valid values
          are 'local_public', 'local_private' and 'local'. Visibility can only be
          'local_private' if the project supports application private visibility.
    :param str name: The name of the app.
    :param Probe probe_liveness: (optional) Response model for probes.
    :param Probe probe_readiness: (optional) Response model for probes.
    :param str project_id: (optional) The ID of the project in which the resource is
          located.
    :param str region: (optional) The region of the project the resource is located
          in. Possible values: 'au-syd', 'br-sao', 'ca-tor', 'eu-de', 'eu-gb', 'jp-osa',
          'jp-tok', 'us-east', 'us-south'.
    :param str resource_type: (optional) The type of the app.
    :param List[str] run_arguments: Optional arguments for the app that are passed
          to start the container. If not specified an empty string array will be applied
          and the arguments specified by the container image, will be used to start the
          container.
    :param int run_as_user: (optional) Optional user ID (UID) to run the app.
    :param List[str] run_commands: Optional commands for the app that are passed to
          start the container. If not specified an empty string array will be applied and
          the command specified by the container image, will be used to start the
          container.
    :param List[EnvVar] run_env_variables: References to config maps, secrets or
          literal values, which are defined by the app owner and are exposed as
          environment variables in the application.
    :param str run_service_account: (optional) Optional name of the service account.
          For built-in service accounts, you can use the shortened names `manager` ,
          `none`, `reader`, and `writer`.
    :param List[VolumeMount] run_volume_mounts: Mounts of config maps or secrets.
    :param int scale_concurrency: (optional) Optional maximum number of requests
          that can be processed concurrently per instance.
    :param int scale_concurrency_target: (optional) Optional threshold of concurrent
          requests per instance at which one or more additional instances are created. Use
          this value to scale up instances based on concurrent number of requests. This
          option defaults to the value of the `scale_concurrency` option, if not
          specified.
    :param str scale_cpu_limit: Optional number of CPU set for the instance of the
          app. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
    :param int scale_down_delay: (optional) Optional amount of time in seconds that
          delays the scale-down behavior for an app instance.
    :param str scale_ephemeral_storage_limit: Optional amount of ephemeral storage
          to set for the instance of the app. The amount specified as ephemeral storage,
          must not exceed the amount of `scale_memory_limit`. The units for specifying
          ephemeral storage are Megabyte (M) or Gigabyte (G), whereas G and M are the
          shorthand expressions for GB and MB. For more information see [Units of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :param int scale_initial_instances: (optional) Optional initial number of
          instances that are created upon app creation or app update.
    :param int scale_max_instances: Optional maximum number of instances for this
          app. If you set this value to `0`, this property does not set a upper scaling
          limit. However, the app scaling is still limited by the project quota for
          instances. See [Limits and quotas for Code
          Engine](https://cloud.ibm.com/docs/codeengine?topic=codeengine-limits).
    :param str scale_memory_limit: Optional amount of memory set for the instance of
          the app. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
          The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and
          M are the shorthand expressions for GB and MB. For more information see [Units
          of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :param int scale_min_instances: Optional minimum number of instances for this
          app. If you set this value to `0`, the app will scale down to zero, if not hit
          by any request for some time.
    :param int scale_request_timeout: Optional amount of time in seconds that is
          allowed for a running app to respond to a request.
    :param str status: (optional) The current status of the app.
    :param AppStatus status_details: (optional) The detailed status of the
          application.
    """

    def __init__(
        self,
        entity_tag: str,
        image_reference: str,
        managed_domain_mappings: str,
        name: str,
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
        *,
        build: Optional[str] = None,
        build_run: Optional[str] = None,
        computed_env_variables: Optional[List['EnvVar']] = None,
        created_at: Optional[str] = None,
        endpoint: Optional[str] = None,
        endpoint_internal: Optional[str] = None,
        href: Optional[str] = None,
        id: Optional[str] = None,
        image_port: Optional[int] = None,
        image_secret: Optional[str] = None,
        probe_liveness: Optional['Probe'] = None,
        probe_readiness: Optional['Probe'] = None,
        project_id: Optional[str] = None,
        region: Optional[str] = None,
        resource_type: Optional[str] = None,
        run_as_user: Optional[int] = None,
        run_service_account: Optional[str] = None,
        scale_concurrency: Optional[int] = None,
        scale_concurrency_target: Optional[int] = None,
        scale_down_delay: Optional[int] = None,
        scale_initial_instances: Optional[int] = None,
        status: Optional[str] = None,
        status_details: Optional['AppStatus'] = None,
    ) -> None:
        """
        Initialize a App object.

        :param str entity_tag: The version of the app instance, which is used to
               achieve optimistic locking.
        :param str image_reference: The name of the image that is used for this
               app. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and
               `TAG` are optional. If `REGISTRY` is not specified, the default is
               `docker.io`. If `TAG` is not specified, the default is `latest`. If the
               image reference points to a registry that requires authentication, make
               sure to also specify the property `image_secret`.
        :param str managed_domain_mappings: Optional value controlling which of the
               system managed domain mappings will be setup for the application. Valid
               values are 'local_public', 'local_private' and 'local'. Visibility can only
               be 'local_private' if the project supports application private visibility.
        :param str name: The name of the app.
        :param List[str] run_arguments: Optional arguments for the app that are
               passed to start the container. If not specified an empty string array will
               be applied and the arguments specified by the container image, will be used
               to start the container.
        :param List[str] run_commands: Optional commands for the app that are
               passed to start the container. If not specified an empty string array will
               be applied and the command specified by the container image, will be used
               to start the container.
        :param List[EnvVar] run_env_variables: References to config maps, secrets
               or literal values, which are defined by the app owner and are exposed as
               environment variables in the application.
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
        :param List[EnvVar] computed_env_variables: (optional) References to config
               maps, secrets or literal values, which are defined and set by Code Engine
               and are exposed as environment variables in the application.
        :param int image_port: (optional) Optional port the app listens on. While
               the app will always be exposed via port `443` for end users, this port is
               used to connect to the port that is exposed by the container image.
        :param str image_secret: (optional) Optional name of the image registry
               access secret. The image registry access secret is used to authenticate
               with a private registry when you download the container image. If the image
               reference points to a registry that requires authentication, the app will
               be created but cannot reach the ready status, until this property is
               provided, too.
        :param Probe probe_liveness: (optional) Response model for probes.
        :param Probe probe_readiness: (optional) Response model for probes.
        :param int run_as_user: (optional) Optional user ID (UID) to run the app.
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
        :param int scale_down_delay: (optional) Optional amount of time in seconds
               that delays the scale-down behavior for an app instance.
        :param int scale_initial_instances: (optional) Optional initial number of
               instances that are created upon app creation or app update.
        :param AppStatus status_details: (optional) The detailed status of the
               application.
        """
        self.build = build
        self.build_run = build_run
        self.computed_env_variables = computed_env_variables
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
        self.probe_liveness = probe_liveness
        self.probe_readiness = probe_readiness
        self.project_id = project_id
        self.region = region
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
        self.scale_down_delay = scale_down_delay
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
        if (build := _dict.get('build')) is not None:
            args['build'] = build
        if (build_run := _dict.get('build_run')) is not None:
            args['build_run'] = build_run
        if (computed_env_variables := _dict.get('computed_env_variables')) is not None:
            args['computed_env_variables'] = [EnvVar.from_dict(v) for v in computed_env_variables]
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = created_at
        if (endpoint := _dict.get('endpoint')) is not None:
            args['endpoint'] = endpoint
        if (endpoint_internal := _dict.get('endpoint_internal')) is not None:
            args['endpoint_internal'] = endpoint_internal
        if (entity_tag := _dict.get('entity_tag')) is not None:
            args['entity_tag'] = entity_tag
        else:
            raise ValueError('Required property \'entity_tag\' not present in App JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (image_port := _dict.get('image_port')) is not None:
            args['image_port'] = image_port
        if (image_reference := _dict.get('image_reference')) is not None:
            args['image_reference'] = image_reference
        else:
            raise ValueError('Required property \'image_reference\' not present in App JSON')
        if (image_secret := _dict.get('image_secret')) is not None:
            args['image_secret'] = image_secret
        if (managed_domain_mappings := _dict.get('managed_domain_mappings')) is not None:
            args['managed_domain_mappings'] = managed_domain_mappings
        else:
            raise ValueError('Required property \'managed_domain_mappings\' not present in App JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in App JSON')
        if (probe_liveness := _dict.get('probe_liveness')) is not None:
            args['probe_liveness'] = Probe.from_dict(probe_liveness)
        if (probe_readiness := _dict.get('probe_readiness')) is not None:
            args['probe_readiness'] = Probe.from_dict(probe_readiness)
        if (project_id := _dict.get('project_id')) is not None:
            args['project_id'] = project_id
        if (region := _dict.get('region')) is not None:
            args['region'] = region
        if (resource_type := _dict.get('resource_type')) is not None:
            args['resource_type'] = resource_type
        if (run_arguments := _dict.get('run_arguments')) is not None:
            args['run_arguments'] = run_arguments
        else:
            raise ValueError('Required property \'run_arguments\' not present in App JSON')
        if (run_as_user := _dict.get('run_as_user')) is not None:
            args['run_as_user'] = run_as_user
        if (run_commands := _dict.get('run_commands')) is not None:
            args['run_commands'] = run_commands
        else:
            raise ValueError('Required property \'run_commands\' not present in App JSON')
        if (run_env_variables := _dict.get('run_env_variables')) is not None:
            args['run_env_variables'] = [EnvVar.from_dict(v) for v in run_env_variables]
        else:
            raise ValueError('Required property \'run_env_variables\' not present in App JSON')
        if (run_service_account := _dict.get('run_service_account')) is not None:
            args['run_service_account'] = run_service_account
        if (run_volume_mounts := _dict.get('run_volume_mounts')) is not None:
            args['run_volume_mounts'] = [VolumeMount.from_dict(v) for v in run_volume_mounts]
        else:
            raise ValueError('Required property \'run_volume_mounts\' not present in App JSON')
        if (scale_concurrency := _dict.get('scale_concurrency')) is not None:
            args['scale_concurrency'] = scale_concurrency
        if (scale_concurrency_target := _dict.get('scale_concurrency_target')) is not None:
            args['scale_concurrency_target'] = scale_concurrency_target
        if (scale_cpu_limit := _dict.get('scale_cpu_limit')) is not None:
            args['scale_cpu_limit'] = scale_cpu_limit
        else:
            raise ValueError('Required property \'scale_cpu_limit\' not present in App JSON')
        if (scale_down_delay := _dict.get('scale_down_delay')) is not None:
            args['scale_down_delay'] = scale_down_delay
        if (scale_ephemeral_storage_limit := _dict.get('scale_ephemeral_storage_limit')) is not None:
            args['scale_ephemeral_storage_limit'] = scale_ephemeral_storage_limit
        else:
            raise ValueError('Required property \'scale_ephemeral_storage_limit\' not present in App JSON')
        if (scale_initial_instances := _dict.get('scale_initial_instances')) is not None:
            args['scale_initial_instances'] = scale_initial_instances
        if (scale_max_instances := _dict.get('scale_max_instances')) is not None:
            args['scale_max_instances'] = scale_max_instances
        else:
            raise ValueError('Required property \'scale_max_instances\' not present in App JSON')
        if (scale_memory_limit := _dict.get('scale_memory_limit')) is not None:
            args['scale_memory_limit'] = scale_memory_limit
        else:
            raise ValueError('Required property \'scale_memory_limit\' not present in App JSON')
        if (scale_min_instances := _dict.get('scale_min_instances')) is not None:
            args['scale_min_instances'] = scale_min_instances
        else:
            raise ValueError('Required property \'scale_min_instances\' not present in App JSON')
        if (scale_request_timeout := _dict.get('scale_request_timeout')) is not None:
            args['scale_request_timeout'] = scale_request_timeout
        else:
            raise ValueError('Required property \'scale_request_timeout\' not present in App JSON')
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (status_details := _dict.get('status_details')) is not None:
            args['status_details'] = AppStatus.from_dict(status_details)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a App object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'build') and getattr(self, 'build') is not None:
            _dict['build'] = getattr(self, 'build')
        if hasattr(self, 'build_run') and getattr(self, 'build_run') is not None:
            _dict['build_run'] = getattr(self, 'build_run')
        if hasattr(self, 'computed_env_variables') and self.computed_env_variables is not None:
            computed_env_variables_list = []
            for v in self.computed_env_variables:
                if isinstance(v, dict):
                    computed_env_variables_list.append(v)
                else:
                    computed_env_variables_list.append(v.to_dict())
            _dict['computed_env_variables'] = computed_env_variables_list
        if hasattr(self, 'created_at') and getattr(self, 'created_at') is not None:
            _dict['created_at'] = getattr(self, 'created_at')
        if hasattr(self, 'endpoint') and getattr(self, 'endpoint') is not None:
            _dict['endpoint'] = getattr(self, 'endpoint')
        if hasattr(self, 'endpoint_internal') and getattr(self, 'endpoint_internal') is not None:
            _dict['endpoint_internal'] = getattr(self, 'endpoint_internal')
        if hasattr(self, 'entity_tag') and self.entity_tag is not None:
            _dict['entity_tag'] = self.entity_tag
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
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
        if hasattr(self, 'probe_liveness') and self.probe_liveness is not None:
            if isinstance(self.probe_liveness, dict):
                _dict['probe_liveness'] = self.probe_liveness
            else:
                _dict['probe_liveness'] = self.probe_liveness.to_dict()
        if hasattr(self, 'probe_readiness') and self.probe_readiness is not None:
            if isinstance(self.probe_readiness, dict):
                _dict['probe_readiness'] = self.probe_readiness
            else:
                _dict['probe_readiness'] = self.probe_readiness.to_dict()
        if hasattr(self, 'project_id') and getattr(self, 'project_id') is not None:
            _dict['project_id'] = getattr(self, 'project_id')
        if hasattr(self, 'region') and getattr(self, 'region') is not None:
            _dict['region'] = getattr(self, 'region')
        if hasattr(self, 'resource_type') and getattr(self, 'resource_type') is not None:
            _dict['resource_type'] = getattr(self, 'resource_type')
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
        if hasattr(self, 'scale_down_delay') and self.scale_down_delay is not None:
            _dict['scale_down_delay'] = self.scale_down_delay
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
        if hasattr(self, 'status') and getattr(self, 'status') is not None:
            _dict['status'] = getattr(self, 'status')
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


class AppInstance:
    """
    AppInstance is the response model for app instance resources.

    :param str app_name: The name of the application that is associated with this
          instance.
    :param str created_at: (optional) The timestamp when the resource was created.
    :param str href: (optional) When you provision a new app instance, a URL is
          created identifying the location of the instance.
    :param str id: (optional) The identifier of the resource.
    :param str name: (optional) The name of the app instance.
    :param str project_id: (optional) The ID of the project in which the resource is
          located.
    :param str region: (optional) The region of the project the resource is located
          in. Possible values: 'au-syd', 'br-sao', 'ca-tor', 'eu-de', 'eu-gb', 'jp-osa',
          'jp-tok', 'us-east', 'us-south'.
    :param str resource_type: (optional) The type of the app instance.
    :param int restarts: (optional) The number of restarts of the app instance.
    :param str revision_name: The name of the revision that is associated with this
          instance.
    :param str scale_cpu_limit: The number of CPU set for the instance. For valid
          values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
    :param str scale_ephemeral_storage_limit: The amount of ephemeral storage set
          for the instance. The amount specified as ephemeral storage, must not exceed the
          amount of `scale_memory_limit`. The units for specifying ephemeral storage are
          Megabyte (M) or Gigabyte (G), whereas G and M are the shorthand expressions for
          GB and MB. For more information see [Units of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :param str scale_memory_limit: The amount of memory set for the instance. For
          valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
          The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and
          M are the shorthand expressions for GB and MB. For more information see [Units
          of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :param str status: (optional) The current status of the instance.
    :param ContainerStatus system_container: (optional) The status of a container.
    :param ContainerStatus user_container: (optional) The status of a container.
    """

    def __init__(
        self,
        app_name: str,
        revision_name: str,
        scale_cpu_limit: str,
        scale_ephemeral_storage_limit: str,
        scale_memory_limit: str,
        *,
        created_at: Optional[str] = None,
        href: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        region: Optional[str] = None,
        resource_type: Optional[str] = None,
        restarts: Optional[int] = None,
        status: Optional[str] = None,
        system_container: Optional['ContainerStatus'] = None,
        user_container: Optional['ContainerStatus'] = None,
    ) -> None:
        """
        Initialize a AppInstance object.

        :param str app_name: The name of the application that is associated with
               this instance.
        :param str revision_name: The name of the revision that is associated with
               this instance.
        :param str scale_cpu_limit: The number of CPU set for the instance. For
               valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
        :param str scale_ephemeral_storage_limit: The amount of ephemeral storage
               set for the instance. The amount specified as ephemeral storage, must not
               exceed the amount of `scale_memory_limit`. The units for specifying
               ephemeral storage are Megabyte (M) or Gigabyte (G), whereas G and M are the
               shorthand expressions for GB and MB. For more information see [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param str scale_memory_limit: The amount of memory set for the instance.
               For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
               The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G
               and M are the shorthand expressions for GB and MB. For more information see
               [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param ContainerStatus system_container: (optional) The status of a
               container.
        :param ContainerStatus user_container: (optional) The status of a
               container.
        """
        self.app_name = app_name
        self.created_at = created_at
        self.href = href
        self.id = id
        self.name = name
        self.project_id = project_id
        self.region = region
        self.resource_type = resource_type
        self.restarts = restarts
        self.revision_name = revision_name
        self.scale_cpu_limit = scale_cpu_limit
        self.scale_ephemeral_storage_limit = scale_ephemeral_storage_limit
        self.scale_memory_limit = scale_memory_limit
        self.status = status
        self.system_container = system_container
        self.user_container = user_container

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AppInstance':
        """Initialize a AppInstance object from a json dictionary."""
        args = {}
        if (app_name := _dict.get('app_name')) is not None:
            args['app_name'] = app_name
        else:
            raise ValueError('Required property \'app_name\' not present in AppInstance JSON')
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = created_at
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (project_id := _dict.get('project_id')) is not None:
            args['project_id'] = project_id
        if (region := _dict.get('region')) is not None:
            args['region'] = region
        if (resource_type := _dict.get('resource_type')) is not None:
            args['resource_type'] = resource_type
        if (restarts := _dict.get('restarts')) is not None:
            args['restarts'] = restarts
        if (revision_name := _dict.get('revision_name')) is not None:
            args['revision_name'] = revision_name
        else:
            raise ValueError('Required property \'revision_name\' not present in AppInstance JSON')
        if (scale_cpu_limit := _dict.get('scale_cpu_limit')) is not None:
            args['scale_cpu_limit'] = scale_cpu_limit
        else:
            raise ValueError('Required property \'scale_cpu_limit\' not present in AppInstance JSON')
        if (scale_ephemeral_storage_limit := _dict.get('scale_ephemeral_storage_limit')) is not None:
            args['scale_ephemeral_storage_limit'] = scale_ephemeral_storage_limit
        else:
            raise ValueError('Required property \'scale_ephemeral_storage_limit\' not present in AppInstance JSON')
        if (scale_memory_limit := _dict.get('scale_memory_limit')) is not None:
            args['scale_memory_limit'] = scale_memory_limit
        else:
            raise ValueError('Required property \'scale_memory_limit\' not present in AppInstance JSON')
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (system_container := _dict.get('system_container')) is not None:
            args['system_container'] = ContainerStatus.from_dict(system_container)
        if (user_container := _dict.get('user_container')) is not None:
            args['user_container'] = ContainerStatus.from_dict(user_container)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AppInstance object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'app_name') and self.app_name is not None:
            _dict['app_name'] = self.app_name
        if hasattr(self, 'created_at') and getattr(self, 'created_at') is not None:
            _dict['created_at'] = getattr(self, 'created_at')
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'name') and getattr(self, 'name') is not None:
            _dict['name'] = getattr(self, 'name')
        if hasattr(self, 'project_id') and getattr(self, 'project_id') is not None:
            _dict['project_id'] = getattr(self, 'project_id')
        if hasattr(self, 'region') and getattr(self, 'region') is not None:
            _dict['region'] = getattr(self, 'region')
        if hasattr(self, 'resource_type') and getattr(self, 'resource_type') is not None:
            _dict['resource_type'] = getattr(self, 'resource_type')
        if hasattr(self, 'restarts') and getattr(self, 'restarts') is not None:
            _dict['restarts'] = getattr(self, 'restarts')
        if hasattr(self, 'revision_name') and self.revision_name is not None:
            _dict['revision_name'] = self.revision_name
        if hasattr(self, 'scale_cpu_limit') and self.scale_cpu_limit is not None:
            _dict['scale_cpu_limit'] = self.scale_cpu_limit
        if hasattr(self, 'scale_ephemeral_storage_limit') and self.scale_ephemeral_storage_limit is not None:
            _dict['scale_ephemeral_storage_limit'] = self.scale_ephemeral_storage_limit
        if hasattr(self, 'scale_memory_limit') and self.scale_memory_limit is not None:
            _dict['scale_memory_limit'] = self.scale_memory_limit
        if hasattr(self, 'status') and getattr(self, 'status') is not None:
            _dict['status'] = getattr(self, 'status')
        if hasattr(self, 'system_container') and self.system_container is not None:
            if isinstance(self.system_container, dict):
                _dict['system_container'] = self.system_container
            else:
                _dict['system_container'] = self.system_container.to_dict()
        if hasattr(self, 'user_container') and self.user_container is not None:
            if isinstance(self.user_container, dict):
                _dict['user_container'] = self.user_container
            else:
                _dict['user_container'] = self.user_container.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AppInstance object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AppInstance') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AppInstance') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ResourceTypeEnum(str, Enum):
        """
        The type of the app instance.
        """

        APP_INSTANCE_V2 = 'app_instance_v2'

    class StatusEnum(str, Enum):
        """
        The current status of the instance.
        """

        PENDING = 'pending'
        RUNNING = 'running'
        SUCCEEDED = 'succeeded'
        FAILED = 'failed'


class AppInstanceList:
    """
    Contains a list of app instances and pagination information.

    :param ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :param List[AppInstance] instances: List of all app instances.
    :param int limit: Maximum number of resources per page.
    :param ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    """

    def __init__(
        self,
        instances: List['AppInstance'],
        limit: int,
        *,
        first: Optional['ListFirstMetadata'] = None,
        next: Optional['ListNextMetadata'] = None,
    ) -> None:
        """
        Initialize a AppInstanceList object.

        :param List[AppInstance] instances: List of all app instances.
        :param int limit: Maximum number of resources per page.
        :param ListFirstMetadata first: (optional) Describes properties needed to
               retrieve the first page of a result list.
        :param ListNextMetadata next: (optional) Describes properties needed to
               retrieve the next page of a result list.
        """
        self.first = first
        self.instances = instances
        self.limit = limit
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AppInstanceList':
        """Initialize a AppInstanceList object from a json dictionary."""
        args = {}
        if (first := _dict.get('first')) is not None:
            args['first'] = ListFirstMetadata.from_dict(first)
        if (instances := _dict.get('instances')) is not None:
            args['instances'] = [AppInstance.from_dict(v) for v in instances]
        else:
            raise ValueError('Required property \'instances\' not present in AppInstanceList JSON')
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in AppInstanceList JSON')
        if (next := _dict.get('next')) is not None:
            args['next'] = ListNextMetadata.from_dict(next)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AppInstanceList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'instances') and self.instances is not None:
            instances_list = []
            for v in self.instances:
                if isinstance(v, dict):
                    instances_list.append(v)
                else:
                    instances_list.append(v.to_dict())
            _dict['instances'] = instances_list
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
        """Return a `str` version of this AppInstanceList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AppInstanceList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AppInstanceList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AppList:
    """
    Contains a list of apps and pagination information.

    :param List[App] apps: List of all apps.
    :param ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :param int limit: Maximum number of resources per page.
    :param ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    """

    def __init__(
        self,
        apps: List['App'],
        limit: int,
        *,
        first: Optional['ListFirstMetadata'] = None,
        next: Optional['ListNextMetadata'] = None,
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
        if (apps := _dict.get('apps')) is not None:
            args['apps'] = [App.from_dict(v) for v in apps]
        else:
            raise ValueError('Required property \'apps\' not present in AppList JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = ListFirstMetadata.from_dict(first)
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in AppList JSON')
        if (next := _dict.get('next')) is not None:
            args['next'] = ListNextMetadata.from_dict(next)
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

    :param int image_port: (optional) Optional port the app listens on. While the
          app will always be exposed via port `443` for end users, this port is used to
          connect to the port that is exposed by the container image.
    :param str image_reference: (optional) The name of the image that is used for
          this app. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and
          `TAG` are optional. If `REGISTRY` is not specified, the default is `docker.io`.
          If `TAG` is not specified, the default is `latest`. If the image reference
          points to a registry that requires authentication, make sure to also specify the
          property `image_secret`.
    :param str image_secret: (optional) Optional name of the image registry access
          secret. The image registry access secret is used to authenticate with a private
          registry when you download the container image. If the image reference points to
          a registry that requires authentication, the app will be created but cannot
          reach the ready status, until this property is provided, too.
    :param str managed_domain_mappings: (optional) Optional value controlling which
          of the system managed domain mappings will be setup for the application. Valid
          values are 'local_public', 'local_private' and 'local'. Visibility can only be
          'local_private' if the project supports application private visibility.
    :param ProbePrototype probe_liveness: (optional) Request model for probes.
    :param ProbePrototype probe_readiness: (optional) Request model for probes.
    :param List[str] run_arguments: (optional) Optional arguments for the app that
          are passed to start the container. If not specified an empty string array will
          be applied and the arguments specified by the container image, will be used to
          start the container.
    :param int run_as_user: (optional) Optional user ID (UID) to run the app.
    :param List[str] run_commands: (optional) Optional commands for the app that are
          passed to start the container. If not specified an empty string array will be
          applied and the command specified by the container image, will be used to start
          the container.
    :param List[EnvVarPrototype] run_env_variables: (optional) Optional references
          to config maps, secrets or literal values.
    :param str run_service_account: (optional) Optional name of the service account.
          For built-in service accounts, you can use the shortened names `manager` ,
          `none`, `reader`, and `writer`.
    :param List[VolumeMountPrototype] run_volume_mounts: (optional) Optional mounts
          of config maps or a secrets. In case this is provided, existing
          `run_volume_mounts` will be overwritten.
    :param int scale_concurrency: (optional) Optional maximum number of requests
          that can be processed concurrently per instance.
    :param int scale_concurrency_target: (optional) Optional threshold of concurrent
          requests per instance at which one or more additional instances are created. Use
          this value to scale up instances based on concurrent number of requests. This
          option defaults to the value of the `scale_concurrency` option, if not
          specified.
    :param str scale_cpu_limit: (optional) Optional number of CPU set for the
          instance of the app. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
    :param int scale_down_delay: (optional) Optional amount of time in seconds that
          delays the scale-down behavior for an app instance.
    :param str scale_ephemeral_storage_limit: (optional) Optional amount of
          ephemeral storage to set for the instance of the app. The amount specified as
          ephemeral storage, must not exceed the amount of `scale_memory_limit`. The units
          for specifying ephemeral storage are Megabyte (M) or Gigabyte (G), whereas G and
          M are the shorthand expressions for GB and MB. For more information see [Units
          of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :param int scale_initial_instances: (optional) Optional initial number of
          instances that are created upon app creation or app update.
    :param int scale_max_instances: (optional) Optional maximum number of instances
          for this app. If you set this value to `0`, this property does not set a upper
          scaling limit. However, the app scaling is still limited by the project quota
          for instances. See [Limits and quotas for Code
          Engine](https://cloud.ibm.com/docs/codeengine?topic=codeengine-limits).
    :param str scale_memory_limit: (optional) Optional amount of memory set for the
          instance of the app. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
          The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and
          M are the shorthand expressions for GB and MB. For more information see [Units
          of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :param int scale_min_instances: (optional) Optional minimum number of instances
          for this app. If you set this value to `0`, the app will scale down to zero, if
          not hit by any request for some time.
    :param int scale_request_timeout: (optional) Optional amount of time in seconds
          that is allowed for a running app to respond to a request.
    """

    def __init__(
        self,
        *,
        image_port: Optional[int] = None,
        image_reference: Optional[str] = None,
        image_secret: Optional[str] = None,
        managed_domain_mappings: Optional[str] = None,
        probe_liveness: Optional['ProbePrototype'] = None,
        probe_readiness: Optional['ProbePrototype'] = None,
        run_arguments: Optional[List[str]] = None,
        run_as_user: Optional[int] = None,
        run_commands: Optional[List[str]] = None,
        run_env_variables: Optional[List['EnvVarPrototype']] = None,
        run_service_account: Optional[str] = None,
        run_volume_mounts: Optional[List['VolumeMountPrototype']] = None,
        scale_concurrency: Optional[int] = None,
        scale_concurrency_target: Optional[int] = None,
        scale_cpu_limit: Optional[str] = None,
        scale_down_delay: Optional[int] = None,
        scale_ephemeral_storage_limit: Optional[str] = None,
        scale_initial_instances: Optional[int] = None,
        scale_max_instances: Optional[int] = None,
        scale_memory_limit: Optional[str] = None,
        scale_min_instances: Optional[int] = None,
        scale_request_timeout: Optional[int] = None,
    ) -> None:
        """
        Initialize a AppPatch object.

        :param int image_port: (optional) Optional port the app listens on. While
               the app will always be exposed via port `443` for end users, this port is
               used to connect to the port that is exposed by the container image.
        :param str image_reference: (optional) The name of the image that is used
               for this app. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where
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
        :param ProbePrototype probe_liveness: (optional) Request model for probes.
        :param ProbePrototype probe_readiness: (optional) Request model for probes.
        :param List[str] run_arguments: (optional) Optional arguments for the app
               that are passed to start the container. If not specified an empty string
               array will be applied and the arguments specified by the container image,
               will be used to start the container.
        :param int run_as_user: (optional) Optional user ID (UID) to run the app.
        :param List[str] run_commands: (optional) Optional commands for the app
               that are passed to start the container. If not specified an empty string
               array will be applied and the command specified by the container image,
               will be used to start the container.
        :param List[EnvVarPrototype] run_env_variables: (optional) Optional
               references to config maps, secrets or literal values.
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
        :param int scale_down_delay: (optional) Optional amount of time in seconds
               that delays the scale-down behavior for an app instance.
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
        self.probe_liveness = probe_liveness
        self.probe_readiness = probe_readiness
        self.run_arguments = run_arguments
        self.run_as_user = run_as_user
        self.run_commands = run_commands
        self.run_env_variables = run_env_variables
        self.run_service_account = run_service_account
        self.run_volume_mounts = run_volume_mounts
        self.scale_concurrency = scale_concurrency
        self.scale_concurrency_target = scale_concurrency_target
        self.scale_cpu_limit = scale_cpu_limit
        self.scale_down_delay = scale_down_delay
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
        if (image_port := _dict.get('image_port')) is not None:
            args['image_port'] = image_port
        if (image_reference := _dict.get('image_reference')) is not None:
            args['image_reference'] = image_reference
        if (image_secret := _dict.get('image_secret')) is not None:
            args['image_secret'] = image_secret
        if (managed_domain_mappings := _dict.get('managed_domain_mappings')) is not None:
            args['managed_domain_mappings'] = managed_domain_mappings
        if (probe_liveness := _dict.get('probe_liveness')) is not None:
            args['probe_liveness'] = ProbePrototype.from_dict(probe_liveness)
        if (probe_readiness := _dict.get('probe_readiness')) is not None:
            args['probe_readiness'] = ProbePrototype.from_dict(probe_readiness)
        if (run_arguments := _dict.get('run_arguments')) is not None:
            args['run_arguments'] = run_arguments
        if (run_as_user := _dict.get('run_as_user')) is not None:
            args['run_as_user'] = run_as_user
        if (run_commands := _dict.get('run_commands')) is not None:
            args['run_commands'] = run_commands
        if (run_env_variables := _dict.get('run_env_variables')) is not None:
            args['run_env_variables'] = [EnvVarPrototype.from_dict(v) for v in run_env_variables]
        if (run_service_account := _dict.get('run_service_account')) is not None:
            args['run_service_account'] = run_service_account
        if (run_volume_mounts := _dict.get('run_volume_mounts')) is not None:
            args['run_volume_mounts'] = [VolumeMountPrototype.from_dict(v) for v in run_volume_mounts]
        if (scale_concurrency := _dict.get('scale_concurrency')) is not None:
            args['scale_concurrency'] = scale_concurrency
        if (scale_concurrency_target := _dict.get('scale_concurrency_target')) is not None:
            args['scale_concurrency_target'] = scale_concurrency_target
        if (scale_cpu_limit := _dict.get('scale_cpu_limit')) is not None:
            args['scale_cpu_limit'] = scale_cpu_limit
        if (scale_down_delay := _dict.get('scale_down_delay')) is not None:
            args['scale_down_delay'] = scale_down_delay
        if (scale_ephemeral_storage_limit := _dict.get('scale_ephemeral_storage_limit')) is not None:
            args['scale_ephemeral_storage_limit'] = scale_ephemeral_storage_limit
        if (scale_initial_instances := _dict.get('scale_initial_instances')) is not None:
            args['scale_initial_instances'] = scale_initial_instances
        if (scale_max_instances := _dict.get('scale_max_instances')) is not None:
            args['scale_max_instances'] = scale_max_instances
        if (scale_memory_limit := _dict.get('scale_memory_limit')) is not None:
            args['scale_memory_limit'] = scale_memory_limit
        if (scale_min_instances := _dict.get('scale_min_instances')) is not None:
            args['scale_min_instances'] = scale_min_instances
        if (scale_request_timeout := _dict.get('scale_request_timeout')) is not None:
            args['scale_request_timeout'] = scale_request_timeout
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
        if hasattr(self, 'probe_liveness') and self.probe_liveness is not None:
            if isinstance(self.probe_liveness, dict):
                _dict['probe_liveness'] = self.probe_liveness
            else:
                _dict['probe_liveness'] = self.probe_liveness.to_dict()
        if hasattr(self, 'probe_readiness') and self.probe_readiness is not None:
            if isinstance(self.probe_readiness, dict):
                _dict['probe_readiness'] = self.probe_readiness
            else:
                _dict['probe_readiness'] = self.probe_readiness.to_dict()
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
        if hasattr(self, 'scale_down_delay') and self.scale_down_delay is not None:
            _dict['scale_down_delay'] = self.scale_down_delay
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

    :param str app_name: (optional) Name of the associated app.
    :param List[EnvVar] computed_env_variables: (optional) References to config
          maps, secrets or literal values, which are defined and set by Code Engine and
          are exposed as environment variables in the application.
    :param str created_at: (optional) The timestamp when the resource was created.
    :param str href: (optional) When you provision a new revision,  a URL is created
          identifying the location of the instance.
    :param str id: (optional) The identifier of the resource.
    :param int image_port: (optional) Optional port the app listens on. While the
          app will always be exposed via port `443` for end users, this port is used to
          connect to the port that is exposed by the container image.
    :param str image_reference: The name of the image that is used for this app. The
          format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and `TAG` are
          optional. If `REGISTRY` is not specified, the default is `docker.io`. If `TAG`
          is not specified, the default is `latest`. If the image reference points to a
          registry that requires authentication, make sure to also specify the property
          `image_secret`.
    :param str image_secret: (optional) Optional name of the image registry access
          secret. The image registry access secret is used to authenticate with a private
          registry when you download the container image. If the image reference points to
          a registry that requires authentication, the app will be created but cannot
          reach the ready status, until this property is provided, too.
    :param str name: (optional) The name of the app revision.
    :param Probe probe_liveness: (optional) Response model for probes.
    :param Probe probe_readiness: (optional) Response model for probes.
    :param str project_id: (optional) The ID of the project in which the resource is
          located.
    :param str region: (optional) The region of the project the resource is located
          in. Possible values: 'au-syd', 'br-sao', 'ca-tor', 'eu-de', 'eu-gb', 'jp-osa',
          'jp-tok', 'us-east', 'us-south'.
    :param str resource_type: (optional) The type of the app revision.
    :param List[str] run_arguments: Optional arguments for the app that are passed
          to start the container. If not specified an empty string array will be applied
          and the arguments specified by the container image, will be used to start the
          container.
    :param int run_as_user: (optional) Optional user ID (UID) to run the app.
    :param List[str] run_commands: Optional commands for the app that are passed to
          start the container. If not specified an empty string array will be applied and
          the command specified by the container image, will be used to start the
          container.
    :param List[EnvVar] run_env_variables: References to config maps, secrets or
          literal values, which are defined by the app owner and are exposed as
          environment variables in the application.
    :param str run_service_account: (optional) Optional name of the service account.
          For built-in service accounts, you can use the shortened names `manager` ,
          `none`, `reader`, and `writer`.
    :param List[VolumeMount] run_volume_mounts: Mounts of config maps or secrets.
    :param int scale_concurrency: (optional) Optional maximum number of requests
          that can be processed concurrently per instance.
    :param int scale_concurrency_target: (optional) Optional threshold of concurrent
          requests per instance at which one or more additional instances are created. Use
          this value to scale up instances based on concurrent number of requests. This
          option defaults to the value of the `scale_concurrency` option, if not
          specified.
    :param str scale_cpu_limit: Optional number of CPU set for the instance of the
          app. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
    :param int scale_down_delay: (optional) Optional amount of time in seconds that
          delays the scale-down behavior for an app instance.
    :param str scale_ephemeral_storage_limit: Optional amount of ephemeral storage
          to set for the instance of the app. The amount specified as ephemeral storage,
          must not exceed the amount of `scale_memory_limit`. The units for specifying
          ephemeral storage are Megabyte (M) or Gigabyte (G), whereas G and M are the
          shorthand expressions for GB and MB. For more information see [Units of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :param int scale_initial_instances: (optional) Optional initial number of
          instances that are created upon app creation or app update.
    :param int scale_max_instances: Optional maximum number of instances for this
          app. If you set this value to `0`, this property does not set a upper scaling
          limit. However, the app scaling is still limited by the project quota for
          instances. See [Limits and quotas for Code
          Engine](https://cloud.ibm.com/docs/codeengine?topic=codeengine-limits).
    :param str scale_memory_limit: Optional amount of memory set for the instance of
          the app. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
          The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and
          M are the shorthand expressions for GB and MB. For more information see [Units
          of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :param int scale_min_instances: Optional minimum number of instances for this
          app. If you set this value to `0`, the app will scale down to zero, if not hit
          by any request for some time.
    :param int scale_request_timeout: Optional amount of time in seconds that is
          allowed for a running app to respond to a request.
    :param str status: (optional) The current status of the app revision.
    :param AppRevisionStatus status_details: (optional) The detailed status of the
          application revision.
    """

    def __init__(
        self,
        image_reference: str,
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
        *,
        app_name: Optional[str] = None,
        computed_env_variables: Optional[List['EnvVar']] = None,
        created_at: Optional[str] = None,
        href: Optional[str] = None,
        id: Optional[str] = None,
        image_port: Optional[int] = None,
        image_secret: Optional[str] = None,
        name: Optional[str] = None,
        probe_liveness: Optional['Probe'] = None,
        probe_readiness: Optional['Probe'] = None,
        project_id: Optional[str] = None,
        region: Optional[str] = None,
        resource_type: Optional[str] = None,
        run_as_user: Optional[int] = None,
        run_service_account: Optional[str] = None,
        scale_concurrency: Optional[int] = None,
        scale_concurrency_target: Optional[int] = None,
        scale_down_delay: Optional[int] = None,
        scale_initial_instances: Optional[int] = None,
        status: Optional[str] = None,
        status_details: Optional['AppRevisionStatus'] = None,
    ) -> None:
        """
        Initialize a AppRevision object.

        :param str image_reference: The name of the image that is used for this
               app. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and
               `TAG` are optional. If `REGISTRY` is not specified, the default is
               `docker.io`. If `TAG` is not specified, the default is `latest`. If the
               image reference points to a registry that requires authentication, make
               sure to also specify the property `image_secret`.
        :param List[str] run_arguments: Optional arguments for the app that are
               passed to start the container. If not specified an empty string array will
               be applied and the arguments specified by the container image, will be used
               to start the container.
        :param List[str] run_commands: Optional commands for the app that are
               passed to start the container. If not specified an empty string array will
               be applied and the command specified by the container image, will be used
               to start the container.
        :param List[EnvVar] run_env_variables: References to config maps, secrets
               or literal values, which are defined by the app owner and are exposed as
               environment variables in the application.
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
        :param str app_name: (optional) Name of the associated app.
        :param List[EnvVar] computed_env_variables: (optional) References to config
               maps, secrets or literal values, which are defined and set by Code Engine
               and are exposed as environment variables in the application.
        :param int image_port: (optional) Optional port the app listens on. While
               the app will always be exposed via port `443` for end users, this port is
               used to connect to the port that is exposed by the container image.
        :param str image_secret: (optional) Optional name of the image registry
               access secret. The image registry access secret is used to authenticate
               with a private registry when you download the container image. If the image
               reference points to a registry that requires authentication, the app will
               be created but cannot reach the ready status, until this property is
               provided, too.
        :param Probe probe_liveness: (optional) Response model for probes.
        :param Probe probe_readiness: (optional) Response model for probes.
        :param int run_as_user: (optional) Optional user ID (UID) to run the app.
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
        :param int scale_down_delay: (optional) Optional amount of time in seconds
               that delays the scale-down behavior for an app instance.
        :param int scale_initial_instances: (optional) Optional initial number of
               instances that are created upon app creation or app update.
        :param AppRevisionStatus status_details: (optional) The detailed status of
               the application revision.
        """
        self.app_name = app_name
        self.computed_env_variables = computed_env_variables
        self.created_at = created_at
        self.href = href
        self.id = id
        self.image_port = image_port
        self.image_reference = image_reference
        self.image_secret = image_secret
        self.name = name
        self.probe_liveness = probe_liveness
        self.probe_readiness = probe_readiness
        self.project_id = project_id
        self.region = region
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
        self.scale_down_delay = scale_down_delay
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
        if (app_name := _dict.get('app_name')) is not None:
            args['app_name'] = app_name
        if (computed_env_variables := _dict.get('computed_env_variables')) is not None:
            args['computed_env_variables'] = [EnvVar.from_dict(v) for v in computed_env_variables]
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = created_at
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (image_port := _dict.get('image_port')) is not None:
            args['image_port'] = image_port
        if (image_reference := _dict.get('image_reference')) is not None:
            args['image_reference'] = image_reference
        else:
            raise ValueError('Required property \'image_reference\' not present in AppRevision JSON')
        if (image_secret := _dict.get('image_secret')) is not None:
            args['image_secret'] = image_secret
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (probe_liveness := _dict.get('probe_liveness')) is not None:
            args['probe_liveness'] = Probe.from_dict(probe_liveness)
        if (probe_readiness := _dict.get('probe_readiness')) is not None:
            args['probe_readiness'] = Probe.from_dict(probe_readiness)
        if (project_id := _dict.get('project_id')) is not None:
            args['project_id'] = project_id
        if (region := _dict.get('region')) is not None:
            args['region'] = region
        if (resource_type := _dict.get('resource_type')) is not None:
            args['resource_type'] = resource_type
        if (run_arguments := _dict.get('run_arguments')) is not None:
            args['run_arguments'] = run_arguments
        else:
            raise ValueError('Required property \'run_arguments\' not present in AppRevision JSON')
        if (run_as_user := _dict.get('run_as_user')) is not None:
            args['run_as_user'] = run_as_user
        if (run_commands := _dict.get('run_commands')) is not None:
            args['run_commands'] = run_commands
        else:
            raise ValueError('Required property \'run_commands\' not present in AppRevision JSON')
        if (run_env_variables := _dict.get('run_env_variables')) is not None:
            args['run_env_variables'] = [EnvVar.from_dict(v) for v in run_env_variables]
        else:
            raise ValueError('Required property \'run_env_variables\' not present in AppRevision JSON')
        if (run_service_account := _dict.get('run_service_account')) is not None:
            args['run_service_account'] = run_service_account
        if (run_volume_mounts := _dict.get('run_volume_mounts')) is not None:
            args['run_volume_mounts'] = [VolumeMount.from_dict(v) for v in run_volume_mounts]
        else:
            raise ValueError('Required property \'run_volume_mounts\' not present in AppRevision JSON')
        if (scale_concurrency := _dict.get('scale_concurrency')) is not None:
            args['scale_concurrency'] = scale_concurrency
        if (scale_concurrency_target := _dict.get('scale_concurrency_target')) is not None:
            args['scale_concurrency_target'] = scale_concurrency_target
        if (scale_cpu_limit := _dict.get('scale_cpu_limit')) is not None:
            args['scale_cpu_limit'] = scale_cpu_limit
        else:
            raise ValueError('Required property \'scale_cpu_limit\' not present in AppRevision JSON')
        if (scale_down_delay := _dict.get('scale_down_delay')) is not None:
            args['scale_down_delay'] = scale_down_delay
        if (scale_ephemeral_storage_limit := _dict.get('scale_ephemeral_storage_limit')) is not None:
            args['scale_ephemeral_storage_limit'] = scale_ephemeral_storage_limit
        else:
            raise ValueError('Required property \'scale_ephemeral_storage_limit\' not present in AppRevision JSON')
        if (scale_initial_instances := _dict.get('scale_initial_instances')) is not None:
            args['scale_initial_instances'] = scale_initial_instances
        if (scale_max_instances := _dict.get('scale_max_instances')) is not None:
            args['scale_max_instances'] = scale_max_instances
        else:
            raise ValueError('Required property \'scale_max_instances\' not present in AppRevision JSON')
        if (scale_memory_limit := _dict.get('scale_memory_limit')) is not None:
            args['scale_memory_limit'] = scale_memory_limit
        else:
            raise ValueError('Required property \'scale_memory_limit\' not present in AppRevision JSON')
        if (scale_min_instances := _dict.get('scale_min_instances')) is not None:
            args['scale_min_instances'] = scale_min_instances
        else:
            raise ValueError('Required property \'scale_min_instances\' not present in AppRevision JSON')
        if (scale_request_timeout := _dict.get('scale_request_timeout')) is not None:
            args['scale_request_timeout'] = scale_request_timeout
        else:
            raise ValueError('Required property \'scale_request_timeout\' not present in AppRevision JSON')
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (status_details := _dict.get('status_details')) is not None:
            args['status_details'] = AppRevisionStatus.from_dict(status_details)
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
        if hasattr(self, 'computed_env_variables') and self.computed_env_variables is not None:
            computed_env_variables_list = []
            for v in self.computed_env_variables:
                if isinstance(v, dict):
                    computed_env_variables_list.append(v)
                else:
                    computed_env_variables_list.append(v.to_dict())
            _dict['computed_env_variables'] = computed_env_variables_list
        if hasattr(self, 'created_at') and getattr(self, 'created_at') is not None:
            _dict['created_at'] = getattr(self, 'created_at')
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'image_port') and self.image_port is not None:
            _dict['image_port'] = self.image_port
        if hasattr(self, 'image_reference') and self.image_reference is not None:
            _dict['image_reference'] = self.image_reference
        if hasattr(self, 'image_secret') and self.image_secret is not None:
            _dict['image_secret'] = self.image_secret
        if hasattr(self, 'name') and getattr(self, 'name') is not None:
            _dict['name'] = getattr(self, 'name')
        if hasattr(self, 'probe_liveness') and self.probe_liveness is not None:
            if isinstance(self.probe_liveness, dict):
                _dict['probe_liveness'] = self.probe_liveness
            else:
                _dict['probe_liveness'] = self.probe_liveness.to_dict()
        if hasattr(self, 'probe_readiness') and self.probe_readiness is not None:
            if isinstance(self.probe_readiness, dict):
                _dict['probe_readiness'] = self.probe_readiness
            else:
                _dict['probe_readiness'] = self.probe_readiness.to_dict()
        if hasattr(self, 'project_id') and getattr(self, 'project_id') is not None:
            _dict['project_id'] = getattr(self, 'project_id')
        if hasattr(self, 'region') and getattr(self, 'region') is not None:
            _dict['region'] = getattr(self, 'region')
        if hasattr(self, 'resource_type') and getattr(self, 'resource_type') is not None:
            _dict['resource_type'] = getattr(self, 'resource_type')
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
        if hasattr(self, 'scale_down_delay') and self.scale_down_delay is not None:
            _dict['scale_down_delay'] = self.scale_down_delay
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
        if hasattr(self, 'status') and getattr(self, 'status') is not None:
            _dict['status'] = getattr(self, 'status')
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

    :param ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :param int limit: Maximum number of resources per page.
    :param ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    :param List[AppRevision] revisions: List of all app revisions.
    """

    def __init__(
        self,
        limit: int,
        revisions: List['AppRevision'],
        *,
        first: Optional['ListFirstMetadata'] = None,
        next: Optional['ListNextMetadata'] = None,
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
        if (first := _dict.get('first')) is not None:
            args['first'] = ListFirstMetadata.from_dict(first)
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in AppRevisionList JSON')
        if (next := _dict.get('next')) is not None:
            args['next'] = ListNextMetadata.from_dict(next)
        if (revisions := _dict.get('revisions')) is not None:
            args['revisions'] = [AppRevision.from_dict(v) for v in revisions]
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

    :param int actual_instances: (optional) The number of running instances of the
          revision.
    :param str reason: (optional) Optional information to provide more context in
          case of a 'failed' or 'warning' status.
    """

    def __init__(
        self,
        *,
        actual_instances: Optional[int] = None,
        reason: Optional[str] = None,
    ) -> None:
        """
        Initialize a AppRevisionStatus object.

        """
        self.actual_instances = actual_instances
        self.reason = reason

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AppRevisionStatus':
        """Initialize a AppRevisionStatus object from a json dictionary."""
        args = {}
        if (actual_instances := _dict.get('actual_instances')) is not None:
            args['actual_instances'] = actual_instances
        if (reason := _dict.get('reason')) is not None:
            args['reason'] = reason
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AppRevisionStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'actual_instances') and getattr(self, 'actual_instances') is not None:
            _dict['actual_instances'] = getattr(self, 'actual_instances')
        if hasattr(self, 'reason') and getattr(self, 'reason') is not None:
            _dict['reason'] = getattr(self, 'reason')
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

    :param str latest_created_revision: (optional) Latest app revision that has been
          created.
    :param str latest_ready_revision: (optional) Latest app revision that reached a
          ready state.
    :param str reason: (optional) Optional information to provide more context in
          case of a 'failed' or 'warning' status.
    """

    def __init__(
        self,
        *,
        latest_created_revision: Optional[str] = None,
        latest_ready_revision: Optional[str] = None,
        reason: Optional[str] = None,
    ) -> None:
        """
        Initialize a AppStatus object.

        """
        self.latest_created_revision = latest_created_revision
        self.latest_ready_revision = latest_ready_revision
        self.reason = reason

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AppStatus':
        """Initialize a AppStatus object from a json dictionary."""
        args = {}
        if (latest_created_revision := _dict.get('latest_created_revision')) is not None:
            args['latest_created_revision'] = latest_created_revision
        if (latest_ready_revision := _dict.get('latest_ready_revision')) is not None:
            args['latest_ready_revision'] = latest_ready_revision
        if (reason := _dict.get('reason')) is not None:
            args['reason'] = reason
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AppStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'latest_created_revision') and getattr(self, 'latest_created_revision') is not None:
            _dict['latest_created_revision'] = getattr(self, 'latest_created_revision')
        if hasattr(self, 'latest_ready_revision') and getattr(self, 'latest_ready_revision') is not None:
            _dict['latest_ready_revision'] = getattr(self, 'latest_ready_revision')
        if hasattr(self, 'reason') and getattr(self, 'reason') is not None:
            _dict['reason'] = getattr(self, 'reason')
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


class Binding:
    """
    Describes the model of a binding.

    :param ComponentRef component: A reference to another component.
    :param str href: (optional) When you provision a new binding,  a URL is created
          identifying the location of the instance.
    :param str id: (optional) The ID of the binding.
    :param str prefix: The value that is set as a prefix in the component that is
          bound.
    :param str project_id: (optional) The ID of the project in which the resource is
          located.
    :param str resource_type: (optional) The type of the binding.
    :param str secret_name: The service access secret that is bound to a component.
    :param str status: (optional) The current status of the binding.
    """

    def __init__(
        self,
        component: 'ComponentRef',
        prefix: str,
        secret_name: str,
        *,
        href: Optional[str] = None,
        id: Optional[str] = None,
        project_id: Optional[str] = None,
        resource_type: Optional[str] = None,
        status: Optional[str] = None,
    ) -> None:
        """
        Initialize a Binding object.

        :param ComponentRef component: A reference to another component.
        :param str prefix: The value that is set as a prefix in the component that
               is bound.
        :param str secret_name: The service access secret that is bound to a
               component.
        """
        self.component = component
        self.href = href
        self.id = id
        self.prefix = prefix
        self.project_id = project_id
        self.resource_type = resource_type
        self.secret_name = secret_name
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Binding':
        """Initialize a Binding object from a json dictionary."""
        args = {}
        if (component := _dict.get('component')) is not None:
            args['component'] = ComponentRef.from_dict(component)
        else:
            raise ValueError('Required property \'component\' not present in Binding JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (prefix := _dict.get('prefix')) is not None:
            args['prefix'] = prefix
        else:
            raise ValueError('Required property \'prefix\' not present in Binding JSON')
        if (project_id := _dict.get('project_id')) is not None:
            args['project_id'] = project_id
        if (resource_type := _dict.get('resource_type')) is not None:
            args['resource_type'] = resource_type
        if (secret_name := _dict.get('secret_name')) is not None:
            args['secret_name'] = secret_name
        else:
            raise ValueError('Required property \'secret_name\' not present in Binding JSON')
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Binding object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'component') and self.component is not None:
            if isinstance(self.component, dict):
                _dict['component'] = self.component
            else:
                _dict['component'] = self.component.to_dict()
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'prefix') and self.prefix is not None:
            _dict['prefix'] = self.prefix
        if hasattr(self, 'project_id') and getattr(self, 'project_id') is not None:
            _dict['project_id'] = getattr(self, 'project_id')
        if hasattr(self, 'resource_type') and getattr(self, 'resource_type') is not None:
            _dict['resource_type'] = getattr(self, 'resource_type')
        if hasattr(self, 'secret_name') and self.secret_name is not None:
            _dict['secret_name'] = self.secret_name
        if hasattr(self, 'status') and getattr(self, 'status') is not None:
            _dict['status'] = getattr(self, 'status')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Binding object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Binding') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Binding') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ResourceTypeEnum(str, Enum):
        """
        The type of the binding.
        """

        BINDING_V2 = 'binding_v2'


class BindingList:
    """
    Contains a list of bindings and pagination information.

    :param List[Binding] bindings: List of all bindings.
    :param ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :param int limit: Maximum number of resources per page.
    :param ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    """

    def __init__(
        self,
        bindings: List['Binding'],
        limit: int,
        *,
        first: Optional['ListFirstMetadata'] = None,
        next: Optional['ListNextMetadata'] = None,
    ) -> None:
        """
        Initialize a BindingList object.

        :param List[Binding] bindings: List of all bindings.
        :param int limit: Maximum number of resources per page.
        :param ListFirstMetadata first: (optional) Describes properties needed to
               retrieve the first page of a result list.
        :param ListNextMetadata next: (optional) Describes properties needed to
               retrieve the next page of a result list.
        """
        self.bindings = bindings
        self.first = first
        self.limit = limit
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BindingList':
        """Initialize a BindingList object from a json dictionary."""
        args = {}
        if (bindings := _dict.get('bindings')) is not None:
            args['bindings'] = [Binding.from_dict(v) for v in bindings]
        else:
            raise ValueError('Required property \'bindings\' not present in BindingList JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = ListFirstMetadata.from_dict(first)
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in BindingList JSON')
        if (next := _dict.get('next')) is not None:
            args['next'] = ListNextMetadata.from_dict(next)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BindingList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'bindings') and self.bindings is not None:
            bindings_list = []
            for v in self.bindings:
                if isinstance(v, dict):
                    bindings_list.append(v)
                else:
                    bindings_list.append(v.to_dict())
            _dict['bindings'] = bindings_list
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
        """Return a `str` version of this BindingList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BindingList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BindingList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Build:
    """
    Response model for build definitions.

    :param str created_at: (optional) The timestamp when the resource was created.
    :param str entity_tag: The version of the build instance, which is used to
          achieve optimistic locking.
    :param str href: (optional) When you provision a new build,  a URL is created
          identifying the location of the instance.
    :param str id: (optional) The identifier of the resource.
    :param str name: (optional) The name of the build.
    :param str output_image: The name of the image.
    :param str output_secret: The secret that is required to access the image
          registry. Make sure that the secret is granted with push permissions towards the
          specified container registry namespace.
    :param str project_id: (optional) The ID of the project in which the resource is
          located.
    :param str region: (optional) The region of the project the resource is located
          in. Possible values: 'au-syd', 'br-sao', 'ca-tor', 'eu-de', 'eu-gb', 'jp-osa',
          'jp-tok', 'us-east', 'us-south'.
    :param str resource_type: (optional) The type of the build.
    :param str source_context_dir: (optional) Optional directory in the repository
          that contains the buildpacks file or the Dockerfile.
    :param str source_revision: (optional) Commit, tag, or branch in the source
          repository to pull. This field is optional if the `source_type` is `git` and
          uses the HEAD of default branch if not specified. If the `source_type` value is
          `local`, this field must be omitted.
    :param str source_secret: (optional) Name of the secret that is used access the
          repository source. This field is optional if the `source_type` is `git`.
          Additionally, if the `source_url` points to a repository that requires
          authentication, the build will be created but cannot access any source code,
          until this property is provided, too. If the `source_type` value is `local`,
          this field must be omitted.
    :param str source_type: Specifies the type of source to determine if your build
          source is in a repository or based on local source code.
          * local - For builds from local source code.
          * git - For builds from git version controlled source code.
    :param str source_url: (optional) The URL of the code repository. This field is
          required if the `source_type` is `git`. If the `source_type` value is `local`,
          this field must be omitted. If the repository is publicly available you can
          provide a 'https' URL like `https://github.com/IBM/CodeEngine`. If the
          repository requires authentication, you need to provide a 'ssh' URL like
          `git@github.com:IBM/CodeEngine.git` along with a `source_secret` that points to
          a secret of format `ssh_auth`.
    :param str status: (optional) The current status of the build.
    :param BuildStatus status_details: (optional) The detailed status of the build.
    :param str strategy_size: Optional size for the build, which determines the
          amount of resources used. Build sizes are `small`, `medium`, `large`, `xlarge`,
          `xxlarge`.
    :param str strategy_spec_file: (optional) Optional path to the specification
          file that is used for build strategies for building an image.
    :param str strategy_type: The strategy to use for building the image.
    :param int timeout: (optional) The maximum amount of time, in seconds, that can
          pass before the build must succeed or fail.
    """

    def __init__(
        self,
        entity_tag: str,
        output_image: str,
        output_secret: str,
        source_type: str,
        strategy_size: str,
        strategy_type: str,
        *,
        created_at: Optional[str] = None,
        href: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        region: Optional[str] = None,
        resource_type: Optional[str] = None,
        source_context_dir: Optional[str] = None,
        source_revision: Optional[str] = None,
        source_secret: Optional[str] = None,
        source_url: Optional[str] = None,
        status: Optional[str] = None,
        status_details: Optional['BuildStatus'] = None,
        strategy_spec_file: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> None:
        """
        Initialize a Build object.

        :param str entity_tag: The version of the build instance, which is used to
               achieve optimistic locking.
        :param str output_image: The name of the image.
        :param str output_secret: The secret that is required to access the image
               registry. Make sure that the secret is granted with push permissions
               towards the specified container registry namespace.
        :param str source_type: Specifies the type of source to determine if your
               build source is in a repository or based on local source code.
               * local - For builds from local source code.
               * git - For builds from git version controlled source code.
        :param str strategy_size: Optional size for the build, which determines the
               amount of resources used. Build sizes are `small`, `medium`, `large`,
               `xlarge`, `xxlarge`.
        :param str strategy_type: The strategy to use for building the image.
        :param str name: (optional) The name of the build.
        :param str source_context_dir: (optional) Optional directory in the
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
        :param str source_url: (optional) The URL of the code repository. This
               field is required if the `source_type` is `git`. If the `source_type` value
               is `local`, this field must be omitted. If the repository is publicly
               available you can provide a 'https' URL like
               `https://github.com/IBM/CodeEngine`. If the repository requires
               authentication, you need to provide a 'ssh' URL like
               `git@github.com:IBM/CodeEngine.git` along with a `source_secret` that
               points to a secret of format `ssh_auth`.
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
        self.region = region
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
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = created_at
        if (entity_tag := _dict.get('entity_tag')) is not None:
            args['entity_tag'] = entity_tag
        else:
            raise ValueError('Required property \'entity_tag\' not present in Build JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (output_image := _dict.get('output_image')) is not None:
            args['output_image'] = output_image
        else:
            raise ValueError('Required property \'output_image\' not present in Build JSON')
        if (output_secret := _dict.get('output_secret')) is not None:
            args['output_secret'] = output_secret
        else:
            raise ValueError('Required property \'output_secret\' not present in Build JSON')
        if (project_id := _dict.get('project_id')) is not None:
            args['project_id'] = project_id
        if (region := _dict.get('region')) is not None:
            args['region'] = region
        if (resource_type := _dict.get('resource_type')) is not None:
            args['resource_type'] = resource_type
        if (source_context_dir := _dict.get('source_context_dir')) is not None:
            args['source_context_dir'] = source_context_dir
        if (source_revision := _dict.get('source_revision')) is not None:
            args['source_revision'] = source_revision
        if (source_secret := _dict.get('source_secret')) is not None:
            args['source_secret'] = source_secret
        if (source_type := _dict.get('source_type')) is not None:
            args['source_type'] = source_type
        else:
            raise ValueError('Required property \'source_type\' not present in Build JSON')
        if (source_url := _dict.get('source_url')) is not None:
            args['source_url'] = source_url
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (status_details := _dict.get('status_details')) is not None:
            args['status_details'] = BuildStatus.from_dict(status_details)
        if (strategy_size := _dict.get('strategy_size')) is not None:
            args['strategy_size'] = strategy_size
        else:
            raise ValueError('Required property \'strategy_size\' not present in Build JSON')
        if (strategy_spec_file := _dict.get('strategy_spec_file')) is not None:
            args['strategy_spec_file'] = strategy_spec_file
        if (strategy_type := _dict.get('strategy_type')) is not None:
            args['strategy_type'] = strategy_type
        else:
            raise ValueError('Required property \'strategy_type\' not present in Build JSON')
        if (timeout := _dict.get('timeout')) is not None:
            args['timeout'] = timeout
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Build object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'created_at') and getattr(self, 'created_at') is not None:
            _dict['created_at'] = getattr(self, 'created_at')
        if hasattr(self, 'entity_tag') and self.entity_tag is not None:
            _dict['entity_tag'] = self.entity_tag
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'output_image') and self.output_image is not None:
            _dict['output_image'] = self.output_image
        if hasattr(self, 'output_secret') and self.output_secret is not None:
            _dict['output_secret'] = self.output_secret
        if hasattr(self, 'project_id') and getattr(self, 'project_id') is not None:
            _dict['project_id'] = getattr(self, 'project_id')
        if hasattr(self, 'region') and getattr(self, 'region') is not None:
            _dict['region'] = getattr(self, 'region')
        if hasattr(self, 'resource_type') and getattr(self, 'resource_type') is not None:
            _dict['resource_type'] = getattr(self, 'resource_type')
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
        if hasattr(self, 'status') and getattr(self, 'status') is not None:
            _dict['status'] = getattr(self, 'status')
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

    :param List[Build] builds: List of all builds.
    :param ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :param int limit: Maximum number of resources per page.
    :param ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    """

    def __init__(
        self,
        builds: List['Build'],
        limit: int,
        *,
        first: Optional['ListFirstMetadata'] = None,
        next: Optional['ListNextMetadata'] = None,
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
        if (builds := _dict.get('builds')) is not None:
            args['builds'] = [Build.from_dict(v) for v in builds]
        else:
            raise ValueError('Required property \'builds\' not present in BuildList JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = ListFirstMetadata.from_dict(first)
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in BuildList JSON')
        if (next := _dict.get('next')) is not None:
            args['next'] = ListNextMetadata.from_dict(next)
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

    :param str output_image: (optional) The name of the image.
    :param str output_secret: (optional) The secret that is required to access the
          image registry. Make sure that the secret is granted with push permissions
          towards the specified container registry namespace.
    :param str source_context_dir: (optional) Optional directory in the repository
          that contains the buildpacks file or the Dockerfile.
    :param str source_revision: (optional) Commit, tag, or branch in the source
          repository to pull. This field is optional if the `source_type` is `git` and
          uses the HEAD of default branch if not specified. If the `source_type` value is
          `local`, this field must be omitted.
    :param str source_secret: (optional) Name of the secret that is used access the
          repository source. This field is optional if the `source_type` is `git`.
          Additionally, if the `source_url` points to a repository that requires
          authentication, the build will be created but cannot access any source code,
          until this property is provided, too. If the `source_type` value is `local`,
          this field must be omitted.
    :param str source_type: (optional) Specifies the type of source to determine if
          your build source is in a repository or based on local source code.
          * local - For builds from local source code.
          * git - For builds from git version controlled source code.
    :param str source_url: (optional) The URL of the code repository. This field is
          required if the `source_type` is `git`. If the `source_type` value is `local`,
          this field must be omitted. If the repository is publicly available you can
          provide a 'https' URL like `https://github.com/IBM/CodeEngine`. If the
          repository requires authentication, you need to provide a 'ssh' URL like
          `git@github.com:IBM/CodeEngine.git` along with a `source_secret` that points to
          a secret of format `ssh_auth`.
    :param str strategy_size: (optional) Optional size for the build, which
          determines the amount of resources used. Build sizes are `small`, `medium`,
          `large`, `xlarge`, `xxlarge`.
    :param str strategy_spec_file: (optional) Optional path to the specification
          file that is used for build strategies for building an image.
    :param str strategy_type: (optional) The strategy to use for building the image.
    :param int timeout: (optional) The maximum amount of time, in seconds, that can
          pass before the build must succeed or fail.
    """

    def __init__(
        self,
        *,
        output_image: Optional[str] = None,
        output_secret: Optional[str] = None,
        source_context_dir: Optional[str] = None,
        source_revision: Optional[str] = None,
        source_secret: Optional[str] = None,
        source_type: Optional[str] = None,
        source_url: Optional[str] = None,
        strategy_size: Optional[str] = None,
        strategy_spec_file: Optional[str] = None,
        strategy_type: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> None:
        """
        Initialize a BuildPatch object.

        :param str output_image: (optional) The name of the image.
        :param str output_secret: (optional) The secret that is required to access
               the image registry. Make sure that the secret is granted with push
               permissions towards the specified container registry namespace.
        :param str source_context_dir: (optional) Optional directory in the
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
               `large`, `xlarge`, `xxlarge`.
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
        if (output_image := _dict.get('output_image')) is not None:
            args['output_image'] = output_image
        if (output_secret := _dict.get('output_secret')) is not None:
            args['output_secret'] = output_secret
        if (source_context_dir := _dict.get('source_context_dir')) is not None:
            args['source_context_dir'] = source_context_dir
        if (source_revision := _dict.get('source_revision')) is not None:
            args['source_revision'] = source_revision
        if (source_secret := _dict.get('source_secret')) is not None:
            args['source_secret'] = source_secret
        if (source_type := _dict.get('source_type')) is not None:
            args['source_type'] = source_type
        if (source_url := _dict.get('source_url')) is not None:
            args['source_url'] = source_url
        if (strategy_size := _dict.get('strategy_size')) is not None:
            args['strategy_size'] = strategy_size
        if (strategy_spec_file := _dict.get('strategy_spec_file')) is not None:
            args['strategy_spec_file'] = strategy_spec_file
        if (strategy_type := _dict.get('strategy_type')) is not None:
            args['strategy_type'] = strategy_type
        if (timeout := _dict.get('timeout')) is not None:
            args['timeout'] = timeout
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

    :param str build_name: Optional name of the build on which this build run is
          based on. If specified, the build run will inherit the configuration of the
          referenced build. If not specified, make sure to specify at least the fields
          `strategy_type`, `source_url`, `output_image` and `output_secret` to describe
          the build run.
    :param str created_at: (optional) The timestamp when the resource was created.
    :param str href: (optional) When you trigger a new build run,  a URL is created
          identifying the location of the instance.
    :param str id: (optional) The identifier of the resource.
    :param str name: The name of the build run.
    :param str output_image: (optional) The name of the image.
    :param str output_secret: (optional) The secret that is required to access the
          image registry. Make sure that the secret is granted with push permissions
          towards the specified container registry namespace.
    :param str project_id: (optional) The ID of the project in which the resource is
          located.
    :param str region: (optional) The region of the project the resource is located
          in. Possible values: 'au-syd', 'br-sao', 'ca-tor', 'eu-de', 'eu-gb', 'jp-osa',
          'jp-tok', 'us-east', 'us-south'.
    :param str resource_type: (optional) The type of the build run.
    :param str service_account: (optional) Optional service account, which is used
          for resource control.” or “Optional service account that is used for resource
          control.
    :param str source_context_dir: (optional) Optional directory in the repository
          that contains the buildpacks file or the Dockerfile.
    :param str source_revision: (optional) Commit, tag, or branch in the source
          repository to pull. This field is optional if the `source_type` is `git` and
          uses the HEAD of default branch if not specified. If the `source_type` value is
          `local`, this field must be omitted.
    :param str source_secret: (optional) Name of the secret that is used access the
          repository source. This field is optional if the `source_type` is `git`.
          Additionally, if the `source_url` points to a repository that requires
          authentication, the build will be created but cannot access any source code,
          until this property is provided, too. If the `source_type` value is `local`,
          this field must be omitted.
    :param str source_type: (optional) Specifies the type of source to determine if
          your build source is in a repository or based on local source code.
          * local - For builds from local source code.
          * git - For builds from git version controlled source code.
    :param str source_url: (optional) The URL of the code repository. This field is
          required if the `source_type` is `git`. If the `source_type` value is `local`,
          this field must be omitted. If the repository is publicly available you can
          provide a 'https' URL like `https://github.com/IBM/CodeEngine`. If the
          repository requires authentication, you need to provide a 'ssh' URL like
          `git@github.com:IBM/CodeEngine.git` along with a `source_secret` that points to
          a secret of format `ssh_auth`.
    :param str status: (optional) The current status of the build run.
    :param BuildRunStatus status_details: (optional) Current status condition of a
          build run.
    :param str strategy_size: (optional) Optional size for the build, which
          determines the amount of resources used. Build sizes are `small`, `medium`,
          `large`, `xlarge`, `xxlarge`.
    :param str strategy_spec_file: (optional) Optional path to the specification
          file that is used for build strategies for building an image.
    :param str strategy_type: (optional) The strategy to use for building the image.
    :param int timeout: (optional) The maximum amount of time, in seconds, that can
          pass before the build must succeed or fail.
    """

    def __init__(
        self,
        build_name: str,
        name: str,
        *,
        created_at: Optional[str] = None,
        href: Optional[str] = None,
        id: Optional[str] = None,
        output_image: Optional[str] = None,
        output_secret: Optional[str] = None,
        project_id: Optional[str] = None,
        region: Optional[str] = None,
        resource_type: Optional[str] = None,
        service_account: Optional[str] = None,
        source_context_dir: Optional[str] = None,
        source_revision: Optional[str] = None,
        source_secret: Optional[str] = None,
        source_type: Optional[str] = None,
        source_url: Optional[str] = None,
        status: Optional[str] = None,
        status_details: Optional['BuildRunStatus'] = None,
        strategy_size: Optional[str] = None,
        strategy_spec_file: Optional[str] = None,
        strategy_type: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> None:
        """
        Initialize a BuildRun object.

        :param str build_name: Optional name of the build on which this build run
               is based on. If specified, the build run will inherit the configuration of
               the referenced build. If not specified, make sure to specify at least the
               fields `strategy_type`, `source_url`, `output_image` and `output_secret` to
               describe the build run.
        :param str name: The name of the build run.
        :param str output_image: (optional) The name of the image.
        :param str output_secret: (optional) The secret that is required to access
               the image registry. Make sure that the secret is granted with push
               permissions towards the specified container registry namespace.
        :param str service_account: (optional) Optional service account, which is
               used for resource control.” or “Optional service account that is used for
               resource control.
        :param str source_context_dir: (optional) Optional directory in the
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
               `large`, `xlarge`, `xxlarge`.
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
        self.region = region
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
        if (build_name := _dict.get('build_name')) is not None:
            args['build_name'] = build_name
        else:
            raise ValueError('Required property \'build_name\' not present in BuildRun JSON')
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = created_at
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in BuildRun JSON')
        if (output_image := _dict.get('output_image')) is not None:
            args['output_image'] = output_image
        if (output_secret := _dict.get('output_secret')) is not None:
            args['output_secret'] = output_secret
        if (project_id := _dict.get('project_id')) is not None:
            args['project_id'] = project_id
        if (region := _dict.get('region')) is not None:
            args['region'] = region
        if (resource_type := _dict.get('resource_type')) is not None:
            args['resource_type'] = resource_type
        if (service_account := _dict.get('service_account')) is not None:
            args['service_account'] = service_account
        if (source_context_dir := _dict.get('source_context_dir')) is not None:
            args['source_context_dir'] = source_context_dir
        if (source_revision := _dict.get('source_revision')) is not None:
            args['source_revision'] = source_revision
        if (source_secret := _dict.get('source_secret')) is not None:
            args['source_secret'] = source_secret
        if (source_type := _dict.get('source_type')) is not None:
            args['source_type'] = source_type
        if (source_url := _dict.get('source_url')) is not None:
            args['source_url'] = source_url
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (status_details := _dict.get('status_details')) is not None:
            args['status_details'] = BuildRunStatus.from_dict(status_details)
        if (strategy_size := _dict.get('strategy_size')) is not None:
            args['strategy_size'] = strategy_size
        if (strategy_spec_file := _dict.get('strategy_spec_file')) is not None:
            args['strategy_spec_file'] = strategy_spec_file
        if (strategy_type := _dict.get('strategy_type')) is not None:
            args['strategy_type'] = strategy_type
        if (timeout := _dict.get('timeout')) is not None:
            args['timeout'] = timeout
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
        if hasattr(self, 'created_at') and getattr(self, 'created_at') is not None:
            _dict['created_at'] = getattr(self, 'created_at')
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'output_image') and self.output_image is not None:
            _dict['output_image'] = self.output_image
        if hasattr(self, 'output_secret') and self.output_secret is not None:
            _dict['output_secret'] = self.output_secret
        if hasattr(self, 'project_id') and getattr(self, 'project_id') is not None:
            _dict['project_id'] = getattr(self, 'project_id')
        if hasattr(self, 'region') and getattr(self, 'region') is not None:
            _dict['region'] = getattr(self, 'region')
        if hasattr(self, 'resource_type') and getattr(self, 'resource_type') is not None:
            _dict['resource_type'] = getattr(self, 'resource_type')
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
        if hasattr(self, 'status') and getattr(self, 'status') is not None:
            _dict['status'] = getattr(self, 'status')
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
        Optional service account, which is used for resource control.” or “Optional
        service account that is used for resource control.
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

    :param List[BuildRun] build_runs: List of all build runs.
    :param ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :param int limit: Maximum number of resources per page.
    :param ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    """

    def __init__(
        self,
        build_runs: List['BuildRun'],
        limit: int,
        *,
        first: Optional['ListFirstMetadata'] = None,
        next: Optional['ListNextMetadata'] = None,
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
        if (build_runs := _dict.get('build_runs')) is not None:
            args['build_runs'] = [BuildRun.from_dict(v) for v in build_runs]
        else:
            raise ValueError('Required property \'build_runs\' not present in BuildRunList JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = ListFirstMetadata.from_dict(first)
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in BuildRunList JSON')
        if (next := _dict.get('next')) is not None:
            args['next'] = ListNextMetadata.from_dict(next)
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

    :param str completion_time: (optional) Time the build run completed.
    :param str git_branch_name: (optional) The default branch name of the git
          source.
    :param str git_commit_author: (optional) The commit author of a git source.
    :param str git_commit_sha: (optional) The commit sha of the git source.
    :param str output_digest: (optional) Describes the time the build run completed.
    :param str reason: (optional) Optional information to provide more context in
          case of a 'failed' or 'warning' status.
    :param str source_timestamp: (optional) The timestamp of the source.
    :param str start_time: (optional) Time the build run started.
    """

    def __init__(
        self,
        *,
        completion_time: Optional[str] = None,
        git_branch_name: Optional[str] = None,
        git_commit_author: Optional[str] = None,
        git_commit_sha: Optional[str] = None,
        output_digest: Optional[str] = None,
        reason: Optional[str] = None,
        source_timestamp: Optional[str] = None,
        start_time: Optional[str] = None,
    ) -> None:
        """
        Initialize a BuildRunStatus object.

        """
        self.completion_time = completion_time
        self.git_branch_name = git_branch_name
        self.git_commit_author = git_commit_author
        self.git_commit_sha = git_commit_sha
        self.output_digest = output_digest
        self.reason = reason
        self.source_timestamp = source_timestamp
        self.start_time = start_time

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BuildRunStatus':
        """Initialize a BuildRunStatus object from a json dictionary."""
        args = {}
        if (completion_time := _dict.get('completion_time')) is not None:
            args['completion_time'] = completion_time
        if (git_branch_name := _dict.get('git_branch_name')) is not None:
            args['git_branch_name'] = git_branch_name
        if (git_commit_author := _dict.get('git_commit_author')) is not None:
            args['git_commit_author'] = git_commit_author
        if (git_commit_sha := _dict.get('git_commit_sha')) is not None:
            args['git_commit_sha'] = git_commit_sha
        if (output_digest := _dict.get('output_digest')) is not None:
            args['output_digest'] = output_digest
        if (reason := _dict.get('reason')) is not None:
            args['reason'] = reason
        if (source_timestamp := _dict.get('source_timestamp')) is not None:
            args['source_timestamp'] = source_timestamp
        if (start_time := _dict.get('start_time')) is not None:
            args['start_time'] = start_time
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BuildRunStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'completion_time') and getattr(self, 'completion_time') is not None:
            _dict['completion_time'] = getattr(self, 'completion_time')
        if hasattr(self, 'git_branch_name') and getattr(self, 'git_branch_name') is not None:
            _dict['git_branch_name'] = getattr(self, 'git_branch_name')
        if hasattr(self, 'git_commit_author') and getattr(self, 'git_commit_author') is not None:
            _dict['git_commit_author'] = getattr(self, 'git_commit_author')
        if hasattr(self, 'git_commit_sha') and getattr(self, 'git_commit_sha') is not None:
            _dict['git_commit_sha'] = getattr(self, 'git_commit_sha')
        if hasattr(self, 'output_digest') and getattr(self, 'output_digest') is not None:
            _dict['output_digest'] = getattr(self, 'output_digest')
        if hasattr(self, 'reason') and getattr(self, 'reason') is not None:
            _dict['reason'] = getattr(self, 'reason')
        if hasattr(self, 'source_timestamp') and getattr(self, 'source_timestamp') is not None:
            _dict['source_timestamp'] = getattr(self, 'source_timestamp')
        if hasattr(self, 'start_time') and getattr(self, 'start_time') is not None:
            _dict['start_time'] = getattr(self, 'start_time')
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

    :param str reason: (optional) Optional information to provide more context in
          case of a 'failed' or 'warning' status.
    """

    def __init__(
        self,
        *,
        reason: Optional[str] = None,
    ) -> None:
        """
        Initialize a BuildStatus object.

        """
        self.reason = reason

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BuildStatus':
        """Initialize a BuildStatus object from a json dictionary."""
        args = {}
        if (reason := _dict.get('reason')) is not None:
            args['reason'] = reason
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BuildStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'reason') and getattr(self, 'reason') is not None:
            _dict['reason'] = getattr(self, 'reason')
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


class ComponentRef:
    """
    A reference to another component.

    :param str name: The name of the referenced component.
    :param str resource_type: The type of the referenced resource.
    """

    def __init__(
        self,
        name: str,
        resource_type: str,
    ) -> None:
        """
        Initialize a ComponentRef object.

        :param str name: The name of the referenced component.
        :param str resource_type: The type of the referenced resource.
        """
        self.name = name
        self.resource_type = resource_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ComponentRef':
        """Initialize a ComponentRef object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in ComponentRef JSON')
        if (resource_type := _dict.get('resource_type')) is not None:
            args['resource_type'] = resource_type
        else:
            raise ValueError('Required property \'resource_type\' not present in ComponentRef JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ComponentRef object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'resource_type') and self.resource_type is not None:
            _dict['resource_type'] = self.resource_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ComponentRef object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ComponentRef') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ComponentRef') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ConfigMap:
    """
    Describes the model of a configmap.

    :param str created_at: (optional) The timestamp when the resource was created.
    :param dict data: (optional) The key-value pair for the config map. Values must
          be specified in `KEY=VALUE` format.
    :param str entity_tag: The version of the config map instance, which is used to
          achieve optimistic locking.
    :param str href: (optional) When you provision a new config map,  a URL is
          created identifying the location of the instance.
    :param str id: (optional) The identifier of the resource.
    :param str name: The name of the config map.
    :param str project_id: (optional) The ID of the project in which the resource is
          located.
    :param str region: (optional) The region of the project the resource is located
          in. Possible values: 'au-syd', 'br-sao', 'ca-tor', 'eu-de', 'eu-gb', 'jp-osa',
          'jp-tok', 'us-east', 'us-south'.
    :param str resource_type: (optional) The type of the config map.
    """

    def __init__(
        self,
        entity_tag: str,
        name: str,
        *,
        created_at: Optional[str] = None,
        data: Optional[dict] = None,
        href: Optional[str] = None,
        id: Optional[str] = None,
        project_id: Optional[str] = None,
        region: Optional[str] = None,
        resource_type: Optional[str] = None,
    ) -> None:
        """
        Initialize a ConfigMap object.

        :param str entity_tag: The version of the config map instance, which is
               used to achieve optimistic locking.
        :param str name: The name of the config map.
        :param dict data: (optional) The key-value pair for the config map. Values
               must be specified in `KEY=VALUE` format.
        """
        self.created_at = created_at
        self.data = data
        self.entity_tag = entity_tag
        self.href = href
        self.id = id
        self.name = name
        self.project_id = project_id
        self.region = region
        self.resource_type = resource_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConfigMap':
        """Initialize a ConfigMap object from a json dictionary."""
        args = {}
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = created_at
        if (data := _dict.get('data')) is not None:
            args['data'] = data
        if (entity_tag := _dict.get('entity_tag')) is not None:
            args['entity_tag'] = entity_tag
        else:
            raise ValueError('Required property \'entity_tag\' not present in ConfigMap JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in ConfigMap JSON')
        if (project_id := _dict.get('project_id')) is not None:
            args['project_id'] = project_id
        if (region := _dict.get('region')) is not None:
            args['region'] = region
        if (resource_type := _dict.get('resource_type')) is not None:
            args['resource_type'] = resource_type
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConfigMap object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'created_at') and getattr(self, 'created_at') is not None:
            _dict['created_at'] = getattr(self, 'created_at')
        if hasattr(self, 'data') and self.data is not None:
            _dict['data'] = self.data
        if hasattr(self, 'entity_tag') and self.entity_tag is not None:
            _dict['entity_tag'] = self.entity_tag
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'project_id') and getattr(self, 'project_id') is not None:
            _dict['project_id'] = getattr(self, 'project_id')
        if hasattr(self, 'region') and getattr(self, 'region') is not None:
            _dict['region'] = getattr(self, 'region')
        if hasattr(self, 'resource_type') and getattr(self, 'resource_type') is not None:
            _dict['resource_type'] = getattr(self, 'resource_type')
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
    Contains a list of config maps and pagination information.

    :param List[ConfigMap] config_maps: List of all config maps.
    :param ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :param int limit: Maximum number of resources per page.
    :param ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    """

    def __init__(
        self,
        config_maps: List['ConfigMap'],
        limit: int,
        *,
        first: Optional['ListFirstMetadata'] = None,
        next: Optional['ListNextMetadata'] = None,
    ) -> None:
        """
        Initialize a ConfigMapList object.

        :param List[ConfigMap] config_maps: List of all config maps.
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
        if (config_maps := _dict.get('config_maps')) is not None:
            args['config_maps'] = [ConfigMap.from_dict(v) for v in config_maps]
        else:
            raise ValueError('Required property \'config_maps\' not present in ConfigMapList JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = ListFirstMetadata.from_dict(first)
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in ConfigMapList JSON')
        if (next := _dict.get('next')) is not None:
            args['next'] = ListNextMetadata.from_dict(next)
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


class ContainerStatus:
    """
    The status of a container.

    :param ContainerStatusDetails current_state: (optional) Details of the observed
          container status.
    :param ContainerStatusDetails last_observed_state: (optional) Details of the
          observed container status.
    """

    def __init__(
        self,
        *,
        current_state: Optional['ContainerStatusDetails'] = None,
        last_observed_state: Optional['ContainerStatusDetails'] = None,
    ) -> None:
        """
        Initialize a ContainerStatus object.

        :param ContainerStatusDetails current_state: (optional) Details of the
               observed container status.
        :param ContainerStatusDetails last_observed_state: (optional) Details of
               the observed container status.
        """
        self.current_state = current_state
        self.last_observed_state = last_observed_state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContainerStatus':
        """Initialize a ContainerStatus object from a json dictionary."""
        args = {}
        if (current_state := _dict.get('current_state')) is not None:
            args['current_state'] = ContainerStatusDetails.from_dict(current_state)
        if (last_observed_state := _dict.get('last_observed_state')) is not None:
            args['last_observed_state'] = ContainerStatusDetails.from_dict(last_observed_state)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContainerStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'current_state') and self.current_state is not None:
            if isinstance(self.current_state, dict):
                _dict['current_state'] = self.current_state
            else:
                _dict['current_state'] = self.current_state.to_dict()
        if hasattr(self, 'last_observed_state') and self.last_observed_state is not None:
            if isinstance(self.last_observed_state, dict):
                _dict['last_observed_state'] = self.last_observed_state
            else:
                _dict['last_observed_state'] = self.last_observed_state.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContainerStatus object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ContainerStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContainerStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ContainerStatusDetails:
    """
    Details of the observed container status.

    :param str completed_at: (optional) The time the container terminated. Only
          populated in an observed failure state.
    :param str container_status: (optional) The status of the container.
    :param int exit_code: (optional) The exit code of the last termination of the
          container. Only populated in an observed failure state.
    :param str reason: (optional) The reason the container is not yet running or has
          failed. Only populated in non-running states.
    :param str started_at: (optional) The time the container started.
    """

    def __init__(
        self,
        *,
        completed_at: Optional[str] = None,
        container_status: Optional[str] = None,
        exit_code: Optional[int] = None,
        reason: Optional[str] = None,
        started_at: Optional[str] = None,
    ) -> None:
        """
        Initialize a ContainerStatusDetails object.

        """
        self.completed_at = completed_at
        self.container_status = container_status
        self.exit_code = exit_code
        self.reason = reason
        self.started_at = started_at

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContainerStatusDetails':
        """Initialize a ContainerStatusDetails object from a json dictionary."""
        args = {}
        if (completed_at := _dict.get('completed_at')) is not None:
            args['completed_at'] = completed_at
        if (container_status := _dict.get('container_status')) is not None:
            args['container_status'] = container_status
        if (exit_code := _dict.get('exit_code')) is not None:
            args['exit_code'] = exit_code
        if (reason := _dict.get('reason')) is not None:
            args['reason'] = reason
        if (started_at := _dict.get('started_at')) is not None:
            args['started_at'] = started_at
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContainerStatusDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'completed_at') and getattr(self, 'completed_at') is not None:
            _dict['completed_at'] = getattr(self, 'completed_at')
        if hasattr(self, 'container_status') and getattr(self, 'container_status') is not None:
            _dict['container_status'] = getattr(self, 'container_status')
        if hasattr(self, 'exit_code') and getattr(self, 'exit_code') is not None:
            _dict['exit_code'] = getattr(self, 'exit_code')
        if hasattr(self, 'reason') and getattr(self, 'reason') is not None:
            _dict['reason'] = getattr(self, 'reason')
        if hasattr(self, 'started_at') and getattr(self, 'started_at') is not None:
            _dict['started_at'] = getattr(self, 'started_at')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContainerStatusDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ContainerStatusDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContainerStatusDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ReasonEnum(str, Enum):
        """
        The reason the container is not yet running or has failed. Only populated in
        non-running states.
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


class DomainMapping:
    """
    Response model for domain mapping definitions.

    :param str cname_target: (optional) The value of the CNAME record that must be
          configured in the DNS settings of the domain, to route traffic properly to the
          target Code Engine region.
    :param ComponentRef component: A reference to another component.
    :param str created_at: (optional) The timestamp when the resource was created.
    :param str entity_tag: The version of the domain mapping instance, which is used
          to achieve optimistic locking.
    :param str href: (optional) When you provision a new domain mapping, a URL is
          created identifying the location of the instance.
    :param str id: (optional) The identifier of the resource.
    :param str name: The name of the domain mapping.
    :param str project_id: (optional) The ID of the project in which the resource is
          located.
    :param str region: (optional) The region of the project the resource is located
          in. Possible values: 'au-syd', 'br-sao', 'ca-tor', 'eu-de', 'eu-gb', 'jp-osa',
          'jp-tok', 'us-east', 'us-south'.
    :param str resource_type: (optional) The type of the Code Engine resource.
    :param str status: (optional) The current status of the domain mapping.
    :param DomainMappingStatus status_details: (optional) The detailed status of the
          domain mapping.
    :param str tls_secret: The name of the TLS secret that includes the certificate
          and private key of this domain mapping.
    :param bool user_managed: (optional) Specifies whether the domain mapping is
          managed by the user or by Code Engine.
    :param str visibility: (optional) Specifies whether the domain mapping is
          reachable through the public internet, or private IBM network, or only through
          other components within the same Code Engine project.
    """

    def __init__(
        self,
        component: 'ComponentRef',
        entity_tag: str,
        name: str,
        tls_secret: str,
        *,
        cname_target: Optional[str] = None,
        created_at: Optional[str] = None,
        href: Optional[str] = None,
        id: Optional[str] = None,
        project_id: Optional[str] = None,
        region: Optional[str] = None,
        resource_type: Optional[str] = None,
        status: Optional[str] = None,
        status_details: Optional['DomainMappingStatus'] = None,
        user_managed: Optional[bool] = None,
        visibility: Optional[str] = None,
    ) -> None:
        """
        Initialize a DomainMapping object.

        :param ComponentRef component: A reference to another component.
        :param str entity_tag: The version of the domain mapping instance, which is
               used to achieve optimistic locking.
        :param str name: The name of the domain mapping.
        :param str tls_secret: The name of the TLS secret that includes the
               certificate and private key of this domain mapping.
        :param DomainMappingStatus status_details: (optional) The detailed status
               of the domain mapping.
        """
        self.cname_target = cname_target
        self.component = component
        self.created_at = created_at
        self.entity_tag = entity_tag
        self.href = href
        self.id = id
        self.name = name
        self.project_id = project_id
        self.region = region
        self.resource_type = resource_type
        self.status = status
        self.status_details = status_details
        self.tls_secret = tls_secret
        self.user_managed = user_managed
        self.visibility = visibility

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DomainMapping':
        """Initialize a DomainMapping object from a json dictionary."""
        args = {}
        if (cname_target := _dict.get('cname_target')) is not None:
            args['cname_target'] = cname_target
        if (component := _dict.get('component')) is not None:
            args['component'] = ComponentRef.from_dict(component)
        else:
            raise ValueError('Required property \'component\' not present in DomainMapping JSON')
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = created_at
        if (entity_tag := _dict.get('entity_tag')) is not None:
            args['entity_tag'] = entity_tag
        else:
            raise ValueError('Required property \'entity_tag\' not present in DomainMapping JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in DomainMapping JSON')
        if (project_id := _dict.get('project_id')) is not None:
            args['project_id'] = project_id
        if (region := _dict.get('region')) is not None:
            args['region'] = region
        if (resource_type := _dict.get('resource_type')) is not None:
            args['resource_type'] = resource_type
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (status_details := _dict.get('status_details')) is not None:
            args['status_details'] = DomainMappingStatus.from_dict(status_details)
        if (tls_secret := _dict.get('tls_secret')) is not None:
            args['tls_secret'] = tls_secret
        else:
            raise ValueError('Required property \'tls_secret\' not present in DomainMapping JSON')
        if (user_managed := _dict.get('user_managed')) is not None:
            args['user_managed'] = user_managed
        if (visibility := _dict.get('visibility')) is not None:
            args['visibility'] = visibility
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DomainMapping object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cname_target') and getattr(self, 'cname_target') is not None:
            _dict['cname_target'] = getattr(self, 'cname_target')
        if hasattr(self, 'component') and self.component is not None:
            if isinstance(self.component, dict):
                _dict['component'] = self.component
            else:
                _dict['component'] = self.component.to_dict()
        if hasattr(self, 'created_at') and getattr(self, 'created_at') is not None:
            _dict['created_at'] = getattr(self, 'created_at')
        if hasattr(self, 'entity_tag') and self.entity_tag is not None:
            _dict['entity_tag'] = self.entity_tag
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'project_id') and getattr(self, 'project_id') is not None:
            _dict['project_id'] = getattr(self, 'project_id')
        if hasattr(self, 'region') and getattr(self, 'region') is not None:
            _dict['region'] = getattr(self, 'region')
        if hasattr(self, 'resource_type') and getattr(self, 'resource_type') is not None:
            _dict['resource_type'] = getattr(self, 'resource_type')
        if hasattr(self, 'status') and getattr(self, 'status') is not None:
            _dict['status'] = getattr(self, 'status')
        if hasattr(self, 'status_details') and self.status_details is not None:
            if isinstance(self.status_details, dict):
                _dict['status_details'] = self.status_details
            else:
                _dict['status_details'] = self.status_details.to_dict()
        if hasattr(self, 'tls_secret') and self.tls_secret is not None:
            _dict['tls_secret'] = self.tls_secret
        if hasattr(self, 'user_managed') and getattr(self, 'user_managed') is not None:
            _dict['user_managed'] = getattr(self, 'user_managed')
        if hasattr(self, 'visibility') and getattr(self, 'visibility') is not None:
            _dict['visibility'] = getattr(self, 'visibility')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DomainMapping object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DomainMapping') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DomainMapping') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ResourceTypeEnum(str, Enum):
        """
        The type of the Code Engine resource.
        """

        DOMAIN_MAPPING_V2 = 'domain_mapping_v2'

    class StatusEnum(str, Enum):
        """
        The current status of the domain mapping.
        """

        READY = 'ready'
        FAILED = 'failed'
        DEPLOYING = 'deploying'

    class VisibilityEnum(str, Enum):
        """
        Specifies whether the domain mapping is reachable through the public internet, or
        private IBM network, or only through other components within the same Code Engine
        project.
        """

        CUSTOM = 'custom'
        PRIVATE = 'private'
        PROJECT = 'project'
        PUBLIC = 'public'


class DomainMappingList:
    """
    Contains a list of domain mappings and pagination information.

    :param List[DomainMapping] domain_mappings: List of all domain mappings.
    :param ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :param int limit: Maximum number of resources per page.
    :param ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    """

    def __init__(
        self,
        domain_mappings: List['DomainMapping'],
        limit: int,
        *,
        first: Optional['ListFirstMetadata'] = None,
        next: Optional['ListNextMetadata'] = None,
    ) -> None:
        """
        Initialize a DomainMappingList object.

        :param List[DomainMapping] domain_mappings: List of all domain mappings.
        :param int limit: Maximum number of resources per page.
        :param ListFirstMetadata first: (optional) Describes properties needed to
               retrieve the first page of a result list.
        :param ListNextMetadata next: (optional) Describes properties needed to
               retrieve the next page of a result list.
        """
        self.domain_mappings = domain_mappings
        self.first = first
        self.limit = limit
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DomainMappingList':
        """Initialize a DomainMappingList object from a json dictionary."""
        args = {}
        if (domain_mappings := _dict.get('domain_mappings')) is not None:
            args['domain_mappings'] = [DomainMapping.from_dict(v) for v in domain_mappings]
        else:
            raise ValueError('Required property \'domain_mappings\' not present in DomainMappingList JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = ListFirstMetadata.from_dict(first)
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in DomainMappingList JSON')
        if (next := _dict.get('next')) is not None:
            args['next'] = ListNextMetadata.from_dict(next)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DomainMappingList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'domain_mappings') and self.domain_mappings is not None:
            domain_mappings_list = []
            for v in self.domain_mappings:
                if isinstance(v, dict):
                    domain_mappings_list.append(v)
                else:
                    domain_mappings_list.append(v.to_dict())
            _dict['domain_mappings'] = domain_mappings_list
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
        """Return a `str` version of this DomainMappingList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DomainMappingList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DomainMappingList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DomainMappingPatch:
    """
    Patch a domain mappings object.

    :param ComponentRef component: (optional) A reference to another component.
    :param str tls_secret: (optional) The name of the TLS secret that includes the
          certificate and private key of this domain mapping.
    """

    def __init__(
        self,
        *,
        component: Optional['ComponentRef'] = None,
        tls_secret: Optional[str] = None,
    ) -> None:
        """
        Initialize a DomainMappingPatch object.

        :param ComponentRef component: (optional) A reference to another component.
        :param str tls_secret: (optional) The name of the TLS secret that includes
               the certificate and private key of this domain mapping.
        """
        self.component = component
        self.tls_secret = tls_secret

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DomainMappingPatch':
        """Initialize a DomainMappingPatch object from a json dictionary."""
        args = {}
        if (component := _dict.get('component')) is not None:
            args['component'] = ComponentRef.from_dict(component)
        if (tls_secret := _dict.get('tls_secret')) is not None:
            args['tls_secret'] = tls_secret
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DomainMappingPatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'component') and self.component is not None:
            if isinstance(self.component, dict):
                _dict['component'] = self.component
            else:
                _dict['component'] = self.component.to_dict()
        if hasattr(self, 'tls_secret') and self.tls_secret is not None:
            _dict['tls_secret'] = self.tls_secret
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DomainMappingPatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DomainMappingPatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DomainMappingPatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DomainMappingStatus:
    """
    The detailed status of the domain mapping.

    :param str reason: (optional) Optional information to provide more context in
          case of a 'failed' or 'warning' status.
    """

    def __init__(
        self,
        *,
        reason: Optional[str] = None,
    ) -> None:
        """
        Initialize a DomainMappingStatus object.

        """
        self.reason = reason

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DomainMappingStatus':
        """Initialize a DomainMappingStatus object from a json dictionary."""
        args = {}
        if (reason := _dict.get('reason')) is not None:
            args['reason'] = reason
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DomainMappingStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'reason') and getattr(self, 'reason') is not None:
            _dict['reason'] = getattr(self, 'reason')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DomainMappingStatus object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DomainMappingStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DomainMappingStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ReasonEnum(str, Enum):
        """
        Optional information to provide more context in case of a 'failed' or 'warning'
        status.
        """

        READY = 'ready'
        DOMAIN_ALREADY_CLAIMED = 'domain_already_claimed'
        APP_REF_FAILED = 'app_ref_failed'
        FAILED_RECONCILE_INGRESS = 'failed_reconcile_ingress'
        DEPLOYING = 'deploying'
        FAILED = 'failed'


class EnvVar:
    """
    Response model for environment variables.

    :param str key: (optional) The key to reference as environment variable.
    :param str name: (optional) The name of the environment variable.
    :param str prefix: (optional) A prefix that can be added to all keys of a full
          secret or config map reference.
    :param str reference: (optional) The name of the secret or config map.
    :param str type: Specify the type of the environment variable.
    :param str value: (optional) The literal value of the environment variable.
    """

    def __init__(
        self,
        type: str,
        *,
        key: Optional[str] = None,
        name: Optional[str] = None,
        prefix: Optional[str] = None,
        reference: Optional[str] = None,
        value: Optional[str] = None,
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
        if (key := _dict.get('key')) is not None:
            args['key'] = key
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (prefix := _dict.get('prefix')) is not None:
            args['prefix'] = prefix
        if (reference := _dict.get('reference')) is not None:
            args['reference'] = reference
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in EnvVar JSON')
        if (value := _dict.get('value')) is not None:
            args['value'] = value
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

    :param str key: (optional) The key to reference as environment variable.
    :param str name: (optional) The name of the environment variable.
    :param str prefix: (optional) A prefix that can be added to all keys of a full
          secret or config map reference.
    :param str reference: (optional) The name of the secret or config map.
    :param str type: (optional) Specify the type of the environment variable.
    :param str value: (optional) The literal value of the environment variable.
    """

    def __init__(
        self,
        *,
        key: Optional[str] = None,
        name: Optional[str] = None,
        prefix: Optional[str] = None,
        reference: Optional[str] = None,
        type: Optional[str] = None,
        value: Optional[str] = None,
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
        if (key := _dict.get('key')) is not None:
            args['key'] = key
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (prefix := _dict.get('prefix')) is not None:
            args['prefix'] = prefix
        if (reference := _dict.get('reference')) is not None:
            args['reference'] = reference
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (value := _dict.get('value')) is not None:
            args['value'] = value
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


class Function:
    """
    Function is the response model for function resources.

    :param bool code_binary: Specifies whether the code is binary or not. Defaults
          to false when `code_reference` is set to a data URL. When `code_reference` is
          set to a code bundle URL, this field is always true.
    :param str code_main: (optional) Specifies the name of the function that should
          be invoked.
    :param str code_reference: Specifies either a reference to a code bundle or the
          source code itself. To specify the source code, use the data URL scheme and
          include the source code as base64 encoded. The data URL scheme is defined in
          [RFC 2397](https://tools.ietf.org/html/rfc2397).
    :param str code_secret: (optional) The name of the secret that is used to access
          the specified `code_reference`. The secret is used to authenticate with a
          non-public endpoint that is specified as`code_reference`.
    :param List[EnvVar] computed_env_variables: (optional) References to config
          maps, secrets or literal values, which are defined and set by Code Engine and
          are exposed as environment variables in the function.
    :param str created_at: (optional) The timestamp when the resource was created.
    :param str endpoint: (optional) URL to invoke the function.
    :param str endpoint_internal: (optional) URL to function that is only visible
          within the project.
    :param str entity_tag: The version of the function instance, which is used to
          achieve optimistic locking.
    :param str href: (optional) When you provision a new function, a relative URL
          path is created identifying the location of the instance.
    :param str id: (optional) The identifier of the resource.
    :param str managed_domain_mappings: Optional value controlling which of the
          system managed domain mappings will be setup for the function. Valid values are
          'local_public', 'local_private' and 'local'. Visibility can only be
          'local_private' if the project supports function private visibility.
    :param str name: The name of the function.
    :param str project_id: (optional) The ID of the project in which the resource is
          located.
    :param str region: (optional) The region of the project the resource is located
          in. Possible values: 'au-syd', 'br-sao', 'ca-tor', 'eu-de', 'eu-gb', 'jp-osa',
          'jp-tok', 'us-east', 'us-south'.
    :param str resource_type: (optional) The type of the function.
    :param List[EnvVar] run_env_variables: References to config maps, secrets or
          literal values, which are defined by the function owner and are exposed as
          environment variables in the function.
    :param str runtime: The managed runtime used to execute the injected code.
    :param int scale_concurrency: Number of parallel requests handled by a single
          instance, supported only by Node.js, default is `1`.
    :param str scale_cpu_limit: Optional amount of CPU set for the instance of the
          function. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
    :param int scale_down_delay: Optional amount of time in seconds that delays the
          scale down behavior for a function.
    :param int scale_max_execution_time: Timeout in secs after which the function is
          terminated.
    :param str scale_memory_limit: Optional amount of memory set for the instance of
          the function. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
          The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and
          M are the shorthand expressions for GB and MB. For more information see [Units
          of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :param str status: (optional) The current status of the function.
    :param FunctionStatus status_details: The detailed status of the function.
    """

    def __init__(
        self,
        code_binary: bool,
        code_reference: str,
        entity_tag: str,
        managed_domain_mappings: str,
        name: str,
        run_env_variables: List['EnvVar'],
        runtime: str,
        scale_concurrency: int,
        scale_cpu_limit: str,
        scale_down_delay: int,
        scale_max_execution_time: int,
        scale_memory_limit: str,
        status_details: 'FunctionStatus',
        *,
        code_main: Optional[str] = None,
        code_secret: Optional[str] = None,
        computed_env_variables: Optional[List['EnvVar']] = None,
        created_at: Optional[str] = None,
        endpoint: Optional[str] = None,
        endpoint_internal: Optional[str] = None,
        href: Optional[str] = None,
        id: Optional[str] = None,
        project_id: Optional[str] = None,
        region: Optional[str] = None,
        resource_type: Optional[str] = None,
        status: Optional[str] = None,
    ) -> None:
        """
        Initialize a Function object.

        :param bool code_binary: Specifies whether the code is binary or not.
               Defaults to false when `code_reference` is set to a data URL. When
               `code_reference` is set to a code bundle URL, this field is always true.
        :param str code_reference: Specifies either a reference to a code bundle or
               the source code itself. To specify the source code, use the data URL scheme
               and include the source code as base64 encoded. The data URL scheme is
               defined in [RFC 2397](https://tools.ietf.org/html/rfc2397).
        :param str entity_tag: The version of the function instance, which is used
               to achieve optimistic locking.
        :param str managed_domain_mappings: Optional value controlling which of the
               system managed domain mappings will be setup for the function. Valid values
               are 'local_public', 'local_private' and 'local'. Visibility can only be
               'local_private' if the project supports function private visibility.
        :param str name: The name of the function.
        :param List[EnvVar] run_env_variables: References to config maps, secrets
               or literal values, which are defined by the function owner and are exposed
               as environment variables in the function.
        :param str runtime: The managed runtime used to execute the injected code.
        :param int scale_concurrency: Number of parallel requests handled by a
               single instance, supported only by Node.js, default is `1`.
        :param str scale_cpu_limit: Optional amount of CPU set for the instance of
               the function. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
        :param int scale_down_delay: Optional amount of time in seconds that delays
               the scale down behavior for a function.
        :param int scale_max_execution_time: Timeout in secs after which the
               function is terminated.
        :param str scale_memory_limit: Optional amount of memory set for the
               instance of the function. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
               The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G
               and M are the shorthand expressions for GB and MB. For more information see
               [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param FunctionStatus status_details: The detailed status of the function.
        :param str code_main: (optional) Specifies the name of the function that
               should be invoked.
        :param str code_secret: (optional) The name of the secret that is used to
               access the specified `code_reference`. The secret is used to authenticate
               with a non-public endpoint that is specified as`code_reference`.
        :param List[EnvVar] computed_env_variables: (optional) References to config
               maps, secrets or literal values, which are defined and set by Code Engine
               and are exposed as environment variables in the function.
        """
        self.code_binary = code_binary
        self.code_main = code_main
        self.code_reference = code_reference
        self.code_secret = code_secret
        self.computed_env_variables = computed_env_variables
        self.created_at = created_at
        self.endpoint = endpoint
        self.endpoint_internal = endpoint_internal
        self.entity_tag = entity_tag
        self.href = href
        self.id = id
        self.managed_domain_mappings = managed_domain_mappings
        self.name = name
        self.project_id = project_id
        self.region = region
        self.resource_type = resource_type
        self.run_env_variables = run_env_variables
        self.runtime = runtime
        self.scale_concurrency = scale_concurrency
        self.scale_cpu_limit = scale_cpu_limit
        self.scale_down_delay = scale_down_delay
        self.scale_max_execution_time = scale_max_execution_time
        self.scale_memory_limit = scale_memory_limit
        self.status = status
        self.status_details = status_details

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Function':
        """Initialize a Function object from a json dictionary."""
        args = {}
        if (code_binary := _dict.get('code_binary')) is not None:
            args['code_binary'] = code_binary
        else:
            raise ValueError('Required property \'code_binary\' not present in Function JSON')
        if (code_main := _dict.get('code_main')) is not None:
            args['code_main'] = code_main
        if (code_reference := _dict.get('code_reference')) is not None:
            args['code_reference'] = code_reference
        else:
            raise ValueError('Required property \'code_reference\' not present in Function JSON')
        if (code_secret := _dict.get('code_secret')) is not None:
            args['code_secret'] = code_secret
        if (computed_env_variables := _dict.get('computed_env_variables')) is not None:
            args['computed_env_variables'] = [EnvVar.from_dict(v) for v in computed_env_variables]
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = created_at
        if (endpoint := _dict.get('endpoint')) is not None:
            args['endpoint'] = endpoint
        if (endpoint_internal := _dict.get('endpoint_internal')) is not None:
            args['endpoint_internal'] = endpoint_internal
        if (entity_tag := _dict.get('entity_tag')) is not None:
            args['entity_tag'] = entity_tag
        else:
            raise ValueError('Required property \'entity_tag\' not present in Function JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (managed_domain_mappings := _dict.get('managed_domain_mappings')) is not None:
            args['managed_domain_mappings'] = managed_domain_mappings
        else:
            raise ValueError('Required property \'managed_domain_mappings\' not present in Function JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in Function JSON')
        if (project_id := _dict.get('project_id')) is not None:
            args['project_id'] = project_id
        if (region := _dict.get('region')) is not None:
            args['region'] = region
        if (resource_type := _dict.get('resource_type')) is not None:
            args['resource_type'] = resource_type
        if (run_env_variables := _dict.get('run_env_variables')) is not None:
            args['run_env_variables'] = [EnvVar.from_dict(v) for v in run_env_variables]
        else:
            raise ValueError('Required property \'run_env_variables\' not present in Function JSON')
        if (runtime := _dict.get('runtime')) is not None:
            args['runtime'] = runtime
        else:
            raise ValueError('Required property \'runtime\' not present in Function JSON')
        if (scale_concurrency := _dict.get('scale_concurrency')) is not None:
            args['scale_concurrency'] = scale_concurrency
        else:
            raise ValueError('Required property \'scale_concurrency\' not present in Function JSON')
        if (scale_cpu_limit := _dict.get('scale_cpu_limit')) is not None:
            args['scale_cpu_limit'] = scale_cpu_limit
        else:
            raise ValueError('Required property \'scale_cpu_limit\' not present in Function JSON')
        if (scale_down_delay := _dict.get('scale_down_delay')) is not None:
            args['scale_down_delay'] = scale_down_delay
        else:
            raise ValueError('Required property \'scale_down_delay\' not present in Function JSON')
        if (scale_max_execution_time := _dict.get('scale_max_execution_time')) is not None:
            args['scale_max_execution_time'] = scale_max_execution_time
        else:
            raise ValueError('Required property \'scale_max_execution_time\' not present in Function JSON')
        if (scale_memory_limit := _dict.get('scale_memory_limit')) is not None:
            args['scale_memory_limit'] = scale_memory_limit
        else:
            raise ValueError('Required property \'scale_memory_limit\' not present in Function JSON')
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (status_details := _dict.get('status_details')) is not None:
            args['status_details'] = FunctionStatus.from_dict(status_details)
        else:
            raise ValueError('Required property \'status_details\' not present in Function JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Function object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'code_binary') and self.code_binary is not None:
            _dict['code_binary'] = self.code_binary
        if hasattr(self, 'code_main') and self.code_main is not None:
            _dict['code_main'] = self.code_main
        if hasattr(self, 'code_reference') and self.code_reference is not None:
            _dict['code_reference'] = self.code_reference
        if hasattr(self, 'code_secret') and self.code_secret is not None:
            _dict['code_secret'] = self.code_secret
        if hasattr(self, 'computed_env_variables') and self.computed_env_variables is not None:
            computed_env_variables_list = []
            for v in self.computed_env_variables:
                if isinstance(v, dict):
                    computed_env_variables_list.append(v)
                else:
                    computed_env_variables_list.append(v.to_dict())
            _dict['computed_env_variables'] = computed_env_variables_list
        if hasattr(self, 'created_at') and getattr(self, 'created_at') is not None:
            _dict['created_at'] = getattr(self, 'created_at')
        if hasattr(self, 'endpoint') and getattr(self, 'endpoint') is not None:
            _dict['endpoint'] = getattr(self, 'endpoint')
        if hasattr(self, 'endpoint_internal') and getattr(self, 'endpoint_internal') is not None:
            _dict['endpoint_internal'] = getattr(self, 'endpoint_internal')
        if hasattr(self, 'entity_tag') and self.entity_tag is not None:
            _dict['entity_tag'] = self.entity_tag
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'managed_domain_mappings') and self.managed_domain_mappings is not None:
            _dict['managed_domain_mappings'] = self.managed_domain_mappings
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'project_id') and getattr(self, 'project_id') is not None:
            _dict['project_id'] = getattr(self, 'project_id')
        if hasattr(self, 'region') and getattr(self, 'region') is not None:
            _dict['region'] = getattr(self, 'region')
        if hasattr(self, 'resource_type') and getattr(self, 'resource_type') is not None:
            _dict['resource_type'] = getattr(self, 'resource_type')
        if hasattr(self, 'run_env_variables') and self.run_env_variables is not None:
            run_env_variables_list = []
            for v in self.run_env_variables:
                if isinstance(v, dict):
                    run_env_variables_list.append(v)
                else:
                    run_env_variables_list.append(v.to_dict())
            _dict['run_env_variables'] = run_env_variables_list
        if hasattr(self, 'runtime') and self.runtime is not None:
            _dict['runtime'] = self.runtime
        if hasattr(self, 'scale_concurrency') and self.scale_concurrency is not None:
            _dict['scale_concurrency'] = self.scale_concurrency
        if hasattr(self, 'scale_cpu_limit') and self.scale_cpu_limit is not None:
            _dict['scale_cpu_limit'] = self.scale_cpu_limit
        if hasattr(self, 'scale_down_delay') and self.scale_down_delay is not None:
            _dict['scale_down_delay'] = self.scale_down_delay
        if hasattr(self, 'scale_max_execution_time') and self.scale_max_execution_time is not None:
            _dict['scale_max_execution_time'] = self.scale_max_execution_time
        if hasattr(self, 'scale_memory_limit') and self.scale_memory_limit is not None:
            _dict['scale_memory_limit'] = self.scale_memory_limit
        if hasattr(self, 'status') and getattr(self, 'status') is not None:
            _dict['status'] = getattr(self, 'status')
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
        """Return a `str` version of this Function object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Function') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Function') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ManagedDomainMappingsEnum(str, Enum):
        """
        Optional value controlling which of the system managed domain mappings will be
        setup for the function. Valid values are 'local_public', 'local_private' and
        'local'. Visibility can only be 'local_private' if the project supports function
        private visibility.
        """

        LOCAL = 'local'
        LOCAL_PRIVATE = 'local_private'
        LOCAL_PUBLIC = 'local_public'

    class ResourceTypeEnum(str, Enum):
        """
        The type of the function.
        """

        FUNCTION_V2 = 'function_v2'

    class StatusEnum(str, Enum):
        """
        The current status of the function.
        """

        OFFLINE = 'offline'
        DEPLOYING = 'deploying'
        READY = 'ready'
        FAILED = 'failed'


class FunctionList:
    """
    Contains a list of functions and pagination information.

    :param ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :param List[Function] functions: List of all functions.
    :param int limit: Maximum number of resources per page.
    :param ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    """

    def __init__(
        self,
        functions: List['Function'],
        limit: int,
        *,
        first: Optional['ListFirstMetadata'] = None,
        next: Optional['ListNextMetadata'] = None,
    ) -> None:
        """
        Initialize a FunctionList object.

        :param List[Function] functions: List of all functions.
        :param int limit: Maximum number of resources per page.
        :param ListFirstMetadata first: (optional) Describes properties needed to
               retrieve the first page of a result list.
        :param ListNextMetadata next: (optional) Describes properties needed to
               retrieve the next page of a result list.
        """
        self.first = first
        self.functions = functions
        self.limit = limit
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FunctionList':
        """Initialize a FunctionList object from a json dictionary."""
        args = {}
        if (first := _dict.get('first')) is not None:
            args['first'] = ListFirstMetadata.from_dict(first)
        if (functions := _dict.get('functions')) is not None:
            args['functions'] = [Function.from_dict(v) for v in functions]
        else:
            raise ValueError('Required property \'functions\' not present in FunctionList JSON')
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in FunctionList JSON')
        if (next := _dict.get('next')) is not None:
            args['next'] = ListNextMetadata.from_dict(next)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FunctionList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'functions') and self.functions is not None:
            functions_list = []
            for v in self.functions:
                if isinstance(v, dict):
                    functions_list.append(v)
                else:
                    functions_list.append(v.to_dict())
            _dict['functions'] = functions_list
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
        """Return a `str` version of this FunctionList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FunctionList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FunctionList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FunctionPatch:
    """
    Request model for function update operations.

    :param bool code_binary: (optional) Specifies whether the code is binary or not.
          Defaults to false when `code_reference` is set to a data URL. When
          `code_reference` is set to a code bundle URL, this field is always true.
    :param str code_main: (optional) Specifies the name of the function that should
          be invoked.
    :param str code_reference: (optional) Specifies either a reference to a code
          bundle or the source code itself. To specify the source code, use the data URL
          scheme and include the source code as base64 encoded. The data URL scheme is
          defined in [RFC 2397](https://tools.ietf.org/html/rfc2397).
    :param str code_secret: (optional) The name of the secret that is used to access
          the specified `code_reference`. The secret is used to authenticate with a
          non-public endpoint that is specified as`code_reference`.
    :param str managed_domain_mappings: (optional) Optional value controlling which
          of the system managed domain mappings will be setup for the function. Valid
          values are 'local_public', 'local_private' and 'local'. Visibility can only be
          'local_private' if the project supports function private visibility.
    :param List[EnvVarPrototype] run_env_variables: (optional) Optional references
          to config maps, secrets or literal values.
    :param str runtime: (optional) The managed runtime used to execute the injected
          code.
    :param int scale_concurrency: (optional) Number of parallel requests handled by
          a single instance, supported only by Node.js, default is `1`.
    :param str scale_cpu_limit: (optional) Optional amount of CPU set for the
          instance of the function. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
    :param int scale_down_delay: (optional) Optional amount of time in seconds that
          delays the scale down behavior for a function.
    :param int scale_max_execution_time: (optional) Timeout in secs after which the
          function is terminated.
    :param str scale_memory_limit: (optional) Optional amount of memory set for the
          instance of the function. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
          The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and
          M are the shorthand expressions for GB and MB. For more information see [Units
          of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    """

    def __init__(
        self,
        *,
        code_binary: Optional[bool] = None,
        code_main: Optional[str] = None,
        code_reference: Optional[str] = None,
        code_secret: Optional[str] = None,
        managed_domain_mappings: Optional[str] = None,
        run_env_variables: Optional[List['EnvVarPrototype']] = None,
        runtime: Optional[str] = None,
        scale_concurrency: Optional[int] = None,
        scale_cpu_limit: Optional[str] = None,
        scale_down_delay: Optional[int] = None,
        scale_max_execution_time: Optional[int] = None,
        scale_memory_limit: Optional[str] = None,
    ) -> None:
        """
        Initialize a FunctionPatch object.

        :param bool code_binary: (optional) Specifies whether the code is binary or
               not. Defaults to false when `code_reference` is set to a data URL. When
               `code_reference` is set to a code bundle URL, this field is always true.
        :param str code_main: (optional) Specifies the name of the function that
               should be invoked.
        :param str code_reference: (optional) Specifies either a reference to a
               code bundle or the source code itself. To specify the source code, use the
               data URL scheme and include the source code as base64 encoded. The data URL
               scheme is defined in [RFC 2397](https://tools.ietf.org/html/rfc2397).
        :param str code_secret: (optional) The name of the secret that is used to
               access the specified `code_reference`. The secret is used to authenticate
               with a non-public endpoint that is specified as`code_reference`.
        :param str managed_domain_mappings: (optional) Optional value controlling
               which of the system managed domain mappings will be setup for the function.
               Valid values are 'local_public', 'local_private' and 'local'. Visibility
               can only be 'local_private' if the project supports function private
               visibility.
        :param List[EnvVarPrototype] run_env_variables: (optional) Optional
               references to config maps, secrets or literal values.
        :param str runtime: (optional) The managed runtime used to execute the
               injected code.
        :param int scale_concurrency: (optional) Number of parallel requests
               handled by a single instance, supported only by Node.js, default is `1`.
        :param str scale_cpu_limit: (optional) Optional amount of CPU set for the
               instance of the function. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
        :param int scale_down_delay: (optional) Optional amount of time in seconds
               that delays the scale down behavior for a function.
        :param int scale_max_execution_time: (optional) Timeout in secs after which
               the function is terminated.
        :param str scale_memory_limit: (optional) Optional amount of memory set for
               the instance of the function. For valid values see [Supported memory and
               CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
               The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G
               and M are the shorthand expressions for GB and MB. For more information see
               [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        """
        self.code_binary = code_binary
        self.code_main = code_main
        self.code_reference = code_reference
        self.code_secret = code_secret
        self.managed_domain_mappings = managed_domain_mappings
        self.run_env_variables = run_env_variables
        self.runtime = runtime
        self.scale_concurrency = scale_concurrency
        self.scale_cpu_limit = scale_cpu_limit
        self.scale_down_delay = scale_down_delay
        self.scale_max_execution_time = scale_max_execution_time
        self.scale_memory_limit = scale_memory_limit

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FunctionPatch':
        """Initialize a FunctionPatch object from a json dictionary."""
        args = {}
        if (code_binary := _dict.get('code_binary')) is not None:
            args['code_binary'] = code_binary
        if (code_main := _dict.get('code_main')) is not None:
            args['code_main'] = code_main
        if (code_reference := _dict.get('code_reference')) is not None:
            args['code_reference'] = code_reference
        if (code_secret := _dict.get('code_secret')) is not None:
            args['code_secret'] = code_secret
        if (managed_domain_mappings := _dict.get('managed_domain_mappings')) is not None:
            args['managed_domain_mappings'] = managed_domain_mappings
        if (run_env_variables := _dict.get('run_env_variables')) is not None:
            args['run_env_variables'] = [EnvVarPrototype.from_dict(v) for v in run_env_variables]
        if (runtime := _dict.get('runtime')) is not None:
            args['runtime'] = runtime
        if (scale_concurrency := _dict.get('scale_concurrency')) is not None:
            args['scale_concurrency'] = scale_concurrency
        if (scale_cpu_limit := _dict.get('scale_cpu_limit')) is not None:
            args['scale_cpu_limit'] = scale_cpu_limit
        if (scale_down_delay := _dict.get('scale_down_delay')) is not None:
            args['scale_down_delay'] = scale_down_delay
        if (scale_max_execution_time := _dict.get('scale_max_execution_time')) is not None:
            args['scale_max_execution_time'] = scale_max_execution_time
        if (scale_memory_limit := _dict.get('scale_memory_limit')) is not None:
            args['scale_memory_limit'] = scale_memory_limit
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FunctionPatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'code_binary') and self.code_binary is not None:
            _dict['code_binary'] = self.code_binary
        if hasattr(self, 'code_main') and self.code_main is not None:
            _dict['code_main'] = self.code_main
        if hasattr(self, 'code_reference') and self.code_reference is not None:
            _dict['code_reference'] = self.code_reference
        if hasattr(self, 'code_secret') and self.code_secret is not None:
            _dict['code_secret'] = self.code_secret
        if hasattr(self, 'managed_domain_mappings') and self.managed_domain_mappings is not None:
            _dict['managed_domain_mappings'] = self.managed_domain_mappings
        if hasattr(self, 'run_env_variables') and self.run_env_variables is not None:
            run_env_variables_list = []
            for v in self.run_env_variables:
                if isinstance(v, dict):
                    run_env_variables_list.append(v)
                else:
                    run_env_variables_list.append(v.to_dict())
            _dict['run_env_variables'] = run_env_variables_list
        if hasattr(self, 'runtime') and self.runtime is not None:
            _dict['runtime'] = self.runtime
        if hasattr(self, 'scale_concurrency') and self.scale_concurrency is not None:
            _dict['scale_concurrency'] = self.scale_concurrency
        if hasattr(self, 'scale_cpu_limit') and self.scale_cpu_limit is not None:
            _dict['scale_cpu_limit'] = self.scale_cpu_limit
        if hasattr(self, 'scale_down_delay') and self.scale_down_delay is not None:
            _dict['scale_down_delay'] = self.scale_down_delay
        if hasattr(self, 'scale_max_execution_time') and self.scale_max_execution_time is not None:
            _dict['scale_max_execution_time'] = self.scale_max_execution_time
        if hasattr(self, 'scale_memory_limit') and self.scale_memory_limit is not None:
            _dict['scale_memory_limit'] = self.scale_memory_limit
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FunctionPatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FunctionPatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FunctionPatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ManagedDomainMappingsEnum(str, Enum):
        """
        Optional value controlling which of the system managed domain mappings will be
        setup for the function. Valid values are 'local_public', 'local_private' and
        'local'. Visibility can only be 'local_private' if the project supports function
        private visibility.
        """

        LOCAL = 'local'
        LOCAL_PRIVATE = 'local_private'
        LOCAL_PUBLIC = 'local_public'


class FunctionRuntime:
    """
    Response model for Function runtime objects.

    :param bool default: (optional) Whether the function runtime is the default for
          the code bundle family.
    :param bool deprecated: (optional) Whether the function runtime is deprecated.
    :param str family: (optional) The code bundle family of the function runtime.
    :param str id: (optional) The ID of the function runtime.
    :param str name: (optional) The name of the function runtime.
    :param bool optimized: (optional) Whether the function runtime is optimized.
    """

    def __init__(
        self,
        *,
        default: Optional[bool] = None,
        deprecated: Optional[bool] = None,
        family: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        optimized: Optional[bool] = None,
    ) -> None:
        """
        Initialize a FunctionRuntime object.

        """
        self.default = default
        self.deprecated = deprecated
        self.family = family
        self.id = id
        self.name = name
        self.optimized = optimized

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FunctionRuntime':
        """Initialize a FunctionRuntime object from a json dictionary."""
        args = {}
        if (default := _dict.get('default')) is not None:
            args['default'] = default
        if (deprecated := _dict.get('deprecated')) is not None:
            args['deprecated'] = deprecated
        if (family := _dict.get('family')) is not None:
            args['family'] = family
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (optimized := _dict.get('optimized')) is not None:
            args['optimized'] = optimized
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FunctionRuntime object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'default') and getattr(self, 'default') is not None:
            _dict['default'] = getattr(self, 'default')
        if hasattr(self, 'deprecated') and getattr(self, 'deprecated') is not None:
            _dict['deprecated'] = getattr(self, 'deprecated')
        if hasattr(self, 'family') and getattr(self, 'family') is not None:
            _dict['family'] = getattr(self, 'family')
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'name') and getattr(self, 'name') is not None:
            _dict['name'] = getattr(self, 'name')
        if hasattr(self, 'optimized') and getattr(self, 'optimized') is not None:
            _dict['optimized'] = getattr(self, 'optimized')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FunctionRuntime object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FunctionRuntime') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FunctionRuntime') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FunctionRuntimeList:
    """
    Contains a list of Function runtimes.

    :param List[FunctionRuntime] function_runtimes: (optional) List of all Function
          runtimes.
    """

    def __init__(
        self,
        *,
        function_runtimes: Optional[List['FunctionRuntime']] = None,
    ) -> None:
        """
        Initialize a FunctionRuntimeList object.

        :param List[FunctionRuntime] function_runtimes: (optional) List of all
               Function runtimes.
        """
        self.function_runtimes = function_runtimes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FunctionRuntimeList':
        """Initialize a FunctionRuntimeList object from a json dictionary."""
        args = {}
        if (function_runtimes := _dict.get('function_runtimes')) is not None:
            args['function_runtimes'] = [FunctionRuntime.from_dict(v) for v in function_runtimes]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FunctionRuntimeList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'function_runtimes') and self.function_runtimes is not None:
            function_runtimes_list = []
            for v in self.function_runtimes:
                if isinstance(v, dict):
                    function_runtimes_list.append(v)
                else:
                    function_runtimes_list.append(v.to_dict())
            _dict['function_runtimes'] = function_runtimes_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FunctionRuntimeList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FunctionRuntimeList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FunctionRuntimeList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FunctionStatus:
    """
    The detailed status of the function.

    :param str reason: (optional) Provides additional information about the status
          of the function.
    """

    def __init__(
        self,
        *,
        reason: Optional[str] = None,
    ) -> None:
        """
        Initialize a FunctionStatus object.

        """
        self.reason = reason

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FunctionStatus':
        """Initialize a FunctionStatus object from a json dictionary."""
        args = {}
        if (reason := _dict.get('reason')) is not None:
            args['reason'] = reason
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FunctionStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'reason') and getattr(self, 'reason') is not None:
            _dict['reason'] = getattr(self, 'reason')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FunctionStatus object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FunctionStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FunctionStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ReasonEnum(str, Enum):
        """
        Provides additional information about the status of the function.
        """

        OFFLINE = 'offline'
        DEPLOYING_CONFIGURING_ROUTES = 'deploying_configuring_routes'
        READY_UPDATE_IN_PROGRESS = 'ready_update_in_progress'
        DEPLOYING = 'deploying'
        READY_LAST_UPDATE_FAILED = 'ready_last_update_failed'
        READY = 'ready'
        UNKNOWN_REASON = 'unknown_reason'
        NO_CODE_BUNDLE = 'no_code_bundle'


class Job:
    """
    Job is the response model for job resources.

    :param str build: (optional) Reference to a build that is associated with the
          job.
    :param str build_run: (optional) Reference to a build run that is associated
          with the job.
    :param List[EnvVar] computed_env_variables: (optional) References to config
          maps, secrets or literal values, which are defined and set by Code Engine and
          are exposed as environment variables in the job run.
    :param str created_at: (optional) The timestamp when the resource was created.
    :param str entity_tag: The version of the job instance, which is used to achieve
          optimistic locking.
    :param str href: (optional) When you provision a new job,  a URL is created
          identifying the location of the instance.
    :param str id: (optional) The identifier of the resource.
    :param str image_reference: The name of the image that is used for this job. The
          format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and `TAG` are
          optional. If `REGISTRY` is not specified, the default is `docker.io`. If `TAG`
          is not specified, the default is `latest`. If the image reference points to a
          registry that requires authentication, make sure to also specify the property
          `image_secret`.
    :param str image_secret: (optional) The name of the image registry access
          secret. The image registry access secret is used to authenticate with a private
          registry when you download the container image. If the image reference points to
          a registry that requires authentication, the job / job runs will be created but
          submitted job runs will fail, until this property is provided, too. This
          property must not be set on a job run, which references a job template.
    :param str name: The name of the job.
    :param str project_id: (optional) The ID of the project in which the resource is
          located.
    :param str region: (optional) The region of the project the resource is located
          in. Possible values: 'au-syd', 'br-sao', 'ca-tor', 'eu-de', 'eu-gb', 'jp-osa',
          'jp-tok', 'us-east', 'us-south'.
    :param str resource_type: (optional) The type of the job.
    :param List[str] run_arguments: Set arguments for the job that are passed to
          start job run containers. If not specified an empty string array will be applied
          and the arguments specified by the container image, will be used to start the
          container.
    :param int run_as_user: (optional) The user ID (UID) to run the job.
    :param List[str] run_commands: Set commands for the job that are passed to start
          job run containers. If not specified an empty string array will be applied and
          the command specified by the container image, will be used to start the
          container.
    :param List[EnvVar] run_env_variables: References to config maps, secrets or
          literal values, which are defined by the function owner and are exposed as
          environment variables in the job run.
    :param str run_mode: The mode for runs of the job. Valid values are `task` and
          `daemon`. In `task` mode, the `max_execution_time` and `retry_limit` properties
          apply. In `daemon` mode, since there is no timeout and failed instances are
          restarted indefinitely, the `max_execution_time` and `retry_limit` properties
          are not allowed.
    :param str run_service_account: (optional) The name of the service account. For
          built-in service accounts, you can use the shortened names `manager`, `none`,
          `reader`, and `writer`. This property must not be set on a job run, which
          references a job template.
    :param List[VolumeMount] run_volume_mounts: Optional mounts of config maps or
          secrets.
    :param str scale_array_spec: Define a custom set of array indices as a
          comma-separated list containing single values and hyphen-separated ranges, such
          as  5,12-14,23,27. Each instance gets its array index value from the environment
          variable JOB_INDEX. The number of unique array indices that you specify with
          this parameter determines the number of job instances to run.
    :param str scale_cpu_limit: Optional amount of CPU set for the instance of the
          job. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
    :param str scale_ephemeral_storage_limit: Optional amount of ephemeral storage
          to set for the instance of the job. The amount specified as ephemeral storage,
          must not exceed the amount of `scale_memory_limit`. The units for specifying
          ephemeral storage are Megabyte (M) or Gigabyte (G), whereas G and M are the
          shorthand expressions for GB and MB. For more information see [Units of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :param int scale_max_execution_time: (optional) The maximum execution time in
          seconds for runs of the job. This property can only be specified if `run_mode`
          is `task`.
    :param str scale_memory_limit: Optional amount of memory set for the instance of
          the job. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
          The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and
          M are the shorthand expressions for GB and MB. For more information see [Units
          of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :param int scale_retry_limit: (optional) The number of times to rerun an
          instance of the job before the job is marked as failed. This property can only
          be specified if `run_mode` is `task`.
    """

    def __init__(
        self,
        entity_tag: str,
        image_reference: str,
        name: str,
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
        build: Optional[str] = None,
        build_run: Optional[str] = None,
        computed_env_variables: Optional[List['EnvVar']] = None,
        created_at: Optional[str] = None,
        href: Optional[str] = None,
        id: Optional[str] = None,
        image_secret: Optional[str] = None,
        project_id: Optional[str] = None,
        region: Optional[str] = None,
        resource_type: Optional[str] = None,
        run_as_user: Optional[int] = None,
        run_service_account: Optional[str] = None,
        scale_max_execution_time: Optional[int] = None,
        scale_retry_limit: Optional[int] = None,
    ) -> None:
        """
        Initialize a Job object.

        :param str entity_tag: The version of the job instance, which is used to
               achieve optimistic locking.
        :param str image_reference: The name of the image that is used for this
               job. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and
               `TAG` are optional. If `REGISTRY` is not specified, the default is
               `docker.io`. If `TAG` is not specified, the default is `latest`. If the
               image reference points to a registry that requires authentication, make
               sure to also specify the property `image_secret`.
        :param str name: The name of the job.
        :param List[str] run_arguments: Set arguments for the job that are passed
               to start job run containers. If not specified an empty string array will be
               applied and the arguments specified by the container image, will be used to
               start the container.
        :param List[str] run_commands: Set commands for the job that are passed to
               start job run containers. If not specified an empty string array will be
               applied and the command specified by the container image, will be used to
               start the container.
        :param List[EnvVar] run_env_variables: References to config maps, secrets
               or literal values, which are defined by the function owner and are exposed
               as environment variables in the job run.
        :param str run_mode: The mode for runs of the job. Valid values are `task`
               and `daemon`. In `task` mode, the `max_execution_time` and `retry_limit`
               properties apply. In `daemon` mode, since there is no timeout and failed
               instances are restarted indefinitely, the `max_execution_time` and
               `retry_limit` properties are not allowed.
        :param List[VolumeMount] run_volume_mounts: Optional mounts of config maps
               or secrets.
        :param str scale_array_spec: Define a custom set of array indices as a
               comma-separated list containing single values and hyphen-separated ranges,
               such as  5,12-14,23,27. Each instance gets its array index value from the
               environment variable JOB_INDEX. The number of unique array indices that you
               specify with this parameter determines the number of job instances to run.
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
        :param List[EnvVar] computed_env_variables: (optional) References to config
               maps, secrets or literal values, which are defined and set by Code Engine
               and are exposed as environment variables in the job run.
        :param str image_secret: (optional) The name of the image registry access
               secret. The image registry access secret is used to authenticate with a
               private registry when you download the container image. If the image
               reference points to a registry that requires authentication, the job / job
               runs will be created but submitted job runs will fail, until this property
               is provided, too. This property must not be set on a job run, which
               references a job template.
        :param int run_as_user: (optional) The user ID (UID) to run the job.
        :param str run_service_account: (optional) The name of the service account.
               For built-in service accounts, you can use the shortened names `manager`,
               `none`, `reader`, and `writer`. This property must not be set on a job run,
               which references a job template.
        :param int scale_max_execution_time: (optional) The maximum execution time
               in seconds for runs of the job. This property can only be specified if
               `run_mode` is `task`.
        :param int scale_retry_limit: (optional) The number of times to rerun an
               instance of the job before the job is marked as failed. This property can
               only be specified if `run_mode` is `task`.
        """
        self.build = build
        self.build_run = build_run
        self.computed_env_variables = computed_env_variables
        self.created_at = created_at
        self.entity_tag = entity_tag
        self.href = href
        self.id = id
        self.image_reference = image_reference
        self.image_secret = image_secret
        self.name = name
        self.project_id = project_id
        self.region = region
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
        if (build := _dict.get('build')) is not None:
            args['build'] = build
        if (build_run := _dict.get('build_run')) is not None:
            args['build_run'] = build_run
        if (computed_env_variables := _dict.get('computed_env_variables')) is not None:
            args['computed_env_variables'] = [EnvVar.from_dict(v) for v in computed_env_variables]
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = created_at
        if (entity_tag := _dict.get('entity_tag')) is not None:
            args['entity_tag'] = entity_tag
        else:
            raise ValueError('Required property \'entity_tag\' not present in Job JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (image_reference := _dict.get('image_reference')) is not None:
            args['image_reference'] = image_reference
        else:
            raise ValueError('Required property \'image_reference\' not present in Job JSON')
        if (image_secret := _dict.get('image_secret')) is not None:
            args['image_secret'] = image_secret
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in Job JSON')
        if (project_id := _dict.get('project_id')) is not None:
            args['project_id'] = project_id
        if (region := _dict.get('region')) is not None:
            args['region'] = region
        if (resource_type := _dict.get('resource_type')) is not None:
            args['resource_type'] = resource_type
        if (run_arguments := _dict.get('run_arguments')) is not None:
            args['run_arguments'] = run_arguments
        else:
            raise ValueError('Required property \'run_arguments\' not present in Job JSON')
        if (run_as_user := _dict.get('run_as_user')) is not None:
            args['run_as_user'] = run_as_user
        if (run_commands := _dict.get('run_commands')) is not None:
            args['run_commands'] = run_commands
        else:
            raise ValueError('Required property \'run_commands\' not present in Job JSON')
        if (run_env_variables := _dict.get('run_env_variables')) is not None:
            args['run_env_variables'] = [EnvVar.from_dict(v) for v in run_env_variables]
        else:
            raise ValueError('Required property \'run_env_variables\' not present in Job JSON')
        if (run_mode := _dict.get('run_mode')) is not None:
            args['run_mode'] = run_mode
        else:
            raise ValueError('Required property \'run_mode\' not present in Job JSON')
        if (run_service_account := _dict.get('run_service_account')) is not None:
            args['run_service_account'] = run_service_account
        if (run_volume_mounts := _dict.get('run_volume_mounts')) is not None:
            args['run_volume_mounts'] = [VolumeMount.from_dict(v) for v in run_volume_mounts]
        else:
            raise ValueError('Required property \'run_volume_mounts\' not present in Job JSON')
        if (scale_array_spec := _dict.get('scale_array_spec')) is not None:
            args['scale_array_spec'] = scale_array_spec
        else:
            raise ValueError('Required property \'scale_array_spec\' not present in Job JSON')
        if (scale_cpu_limit := _dict.get('scale_cpu_limit')) is not None:
            args['scale_cpu_limit'] = scale_cpu_limit
        else:
            raise ValueError('Required property \'scale_cpu_limit\' not present in Job JSON')
        if (scale_ephemeral_storage_limit := _dict.get('scale_ephemeral_storage_limit')) is not None:
            args['scale_ephemeral_storage_limit'] = scale_ephemeral_storage_limit
        else:
            raise ValueError('Required property \'scale_ephemeral_storage_limit\' not present in Job JSON')
        if (scale_max_execution_time := _dict.get('scale_max_execution_time')) is not None:
            args['scale_max_execution_time'] = scale_max_execution_time
        if (scale_memory_limit := _dict.get('scale_memory_limit')) is not None:
            args['scale_memory_limit'] = scale_memory_limit
        else:
            raise ValueError('Required property \'scale_memory_limit\' not present in Job JSON')
        if (scale_retry_limit := _dict.get('scale_retry_limit')) is not None:
            args['scale_retry_limit'] = scale_retry_limit
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Job object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'build') and getattr(self, 'build') is not None:
            _dict['build'] = getattr(self, 'build')
        if hasattr(self, 'build_run') and getattr(self, 'build_run') is not None:
            _dict['build_run'] = getattr(self, 'build_run')
        if hasattr(self, 'computed_env_variables') and self.computed_env_variables is not None:
            computed_env_variables_list = []
            for v in self.computed_env_variables:
                if isinstance(v, dict):
                    computed_env_variables_list.append(v)
                else:
                    computed_env_variables_list.append(v.to_dict())
            _dict['computed_env_variables'] = computed_env_variables_list
        if hasattr(self, 'created_at') and getattr(self, 'created_at') is not None:
            _dict['created_at'] = getattr(self, 'created_at')
        if hasattr(self, 'entity_tag') and self.entity_tag is not None:
            _dict['entity_tag'] = self.entity_tag
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'image_reference') and self.image_reference is not None:
            _dict['image_reference'] = self.image_reference
        if hasattr(self, 'image_secret') and self.image_secret is not None:
            _dict['image_secret'] = self.image_secret
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'project_id') and getattr(self, 'project_id') is not None:
            _dict['project_id'] = getattr(self, 'project_id')
        if hasattr(self, 'region') and getattr(self, 'region') is not None:
            _dict['region'] = getattr(self, 'region')
        if hasattr(self, 'resource_type') and getattr(self, 'resource_type') is not None:
            _dict['resource_type'] = getattr(self, 'resource_type')
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
        mode, the `max_execution_time` and `retry_limit` properties apply. In `daemon`
        mode, since there is no timeout and failed instances are restarted indefinitely,
        the `max_execution_time` and `retry_limit` properties are not allowed.
        """

        TASK = 'task'
        DAEMON = 'daemon'

    class RunServiceAccountEnum(str, Enum):
        """
        The name of the service account. For built-in service accounts, you can use the
        shortened names `manager`, `none`, `reader`, and `writer`. This property must not
        be set on a job run, which references a job template.
        """

        DEFAULT = 'default'
        MANAGER = 'manager'
        READER = 'reader'
        WRITER = 'writer'
        NONE = 'none'


class JobList:
    """
    Contains a list of jobs and pagination information.

    :param ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :param List[Job] jobs: List of all jobs.
    :param int limit: Maximum number of resources per page.
    :param ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    """

    def __init__(
        self,
        jobs: List['Job'],
        limit: int,
        *,
        first: Optional['ListFirstMetadata'] = None,
        next: Optional['ListNextMetadata'] = None,
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
        if (first := _dict.get('first')) is not None:
            args['first'] = ListFirstMetadata.from_dict(first)
        if (jobs := _dict.get('jobs')) is not None:
            args['jobs'] = [Job.from_dict(v) for v in jobs]
        else:
            raise ValueError('Required property \'jobs\' not present in JobList JSON')
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in JobList JSON')
        if (next := _dict.get('next')) is not None:
            args['next'] = ListNextMetadata.from_dict(next)
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

    :param str image_reference: (optional) The name of the image that is used for
          this job. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and
          `TAG` are optional. If `REGISTRY` is not specified, the default is `docker.io`.
          If `TAG` is not specified, the default is `latest`. If the image reference
          points to a registry that requires authentication, make sure to also specify the
          property `image_secret`.
    :param str image_secret: (optional) The name of the image registry access
          secret. The image registry access secret is used to authenticate with a private
          registry when you download the container image. If the image reference points to
          a registry that requires authentication, the job / job runs will be created but
          submitted job runs will fail, until this property is provided, too. This
          property must not be set on a job run, which references a job template.
    :param List[str] run_arguments: (optional) Set arguments for the job that are
          passed to start job run containers. If not specified an empty string array will
          be applied and the arguments specified by the container image, will be used to
          start the container.
    :param int run_as_user: (optional) The user ID (UID) to run the job.
    :param List[str] run_commands: (optional) Set commands for the job that are
          passed to start job run containers. If not specified an empty string array will
          be applied and the command specified by the container image, will be used to
          start the container.
    :param List[EnvVarPrototype] run_env_variables: (optional) Optional references
          to config maps, secrets or literal values.
    :param str run_mode: (optional) The mode for runs of the job. Valid values are
          `task` and `daemon`. In `task` mode, the `max_execution_time` and `retry_limit`
          properties apply. In `daemon` mode, since there is no timeout and failed
          instances are restarted indefinitely, the `max_execution_time` and `retry_limit`
          properties are not allowed.
    :param str run_service_account: (optional) The name of the service account. For
          built-in service accounts, you can use the shortened names `manager`, `none`,
          `reader`, and `writer`. This property must not be set on a job run, which
          references a job template.
    :param List[VolumeMountPrototype] run_volume_mounts: (optional) Optional mounts
          of config maps or a secrets. In case this is provided, existing
          `run_volume_mounts` will be overwritten.
    :param str scale_array_spec: (optional) Define a custom set of array indices as
          a comma-separated list containing single values and hyphen-separated ranges,
          such as  5,12-14,23,27. Each instance gets its array index value from the
          environment variable JOB_INDEX. The number of unique array indices that you
          specify with this parameter determines the number of job instances to run.
    :param str scale_cpu_limit: (optional) Optional amount of CPU set for the
          instance of the job. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
    :param str scale_ephemeral_storage_limit: (optional) Optional amount of
          ephemeral storage to set for the instance of the job. The amount specified as
          ephemeral storage, must not exceed the amount of `scale_memory_limit`. The units
          for specifying ephemeral storage are Megabyte (M) or Gigabyte (G), whereas G and
          M are the shorthand expressions for GB and MB. For more information see [Units
          of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :param int scale_max_execution_time: (optional) The maximum execution time in
          seconds for runs of the job. This property can only be specified if `run_mode`
          is `task`.
    :param str scale_memory_limit: (optional) Optional amount of memory set for the
          instance of the job. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
          The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and
          M are the shorthand expressions for GB and MB. For more information see [Units
          of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :param int scale_retry_limit: (optional) The number of times to rerun an
          instance of the job before the job is marked as failed. This property can only
          be specified if `run_mode` is `task`.
    """

    def __init__(
        self,
        *,
        image_reference: Optional[str] = None,
        image_secret: Optional[str] = None,
        run_arguments: Optional[List[str]] = None,
        run_as_user: Optional[int] = None,
        run_commands: Optional[List[str]] = None,
        run_env_variables: Optional[List['EnvVarPrototype']] = None,
        run_mode: Optional[str] = None,
        run_service_account: Optional[str] = None,
        run_volume_mounts: Optional[List['VolumeMountPrototype']] = None,
        scale_array_spec: Optional[str] = None,
        scale_cpu_limit: Optional[str] = None,
        scale_ephemeral_storage_limit: Optional[str] = None,
        scale_max_execution_time: Optional[int] = None,
        scale_memory_limit: Optional[str] = None,
        scale_retry_limit: Optional[int] = None,
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
               is provided, too. This property must not be set on a job run, which
               references a job template.
        :param List[str] run_arguments: (optional) Set arguments for the job that
               are passed to start job run containers. If not specified an empty string
               array will be applied and the arguments specified by the container image,
               will be used to start the container.
        :param int run_as_user: (optional) The user ID (UID) to run the job.
        :param List[str] run_commands: (optional) Set commands for the job that are
               passed to start job run containers. If not specified an empty string array
               will be applied and the command specified by the container image, will be
               used to start the container.
        :param List[EnvVarPrototype] run_env_variables: (optional) Optional
               references to config maps, secrets or literal values.
        :param str run_mode: (optional) The mode for runs of the job. Valid values
               are `task` and `daemon`. In `task` mode, the `max_execution_time` and
               `retry_limit` properties apply. In `daemon` mode, since there is no timeout
               and failed instances are restarted indefinitely, the `max_execution_time`
               and `retry_limit` properties are not allowed.
        :param str run_service_account: (optional) The name of the service account.
               For built-in service accounts, you can use the shortened names `manager`,
               `none`, `reader`, and `writer`. This property must not be set on a job run,
               which references a job template.
        :param List[VolumeMountPrototype] run_volume_mounts: (optional) Optional
               mounts of config maps or a secrets. In case this is provided, existing
               `run_volume_mounts` will be overwritten.
        :param str scale_array_spec: (optional) Define a custom set of array
               indices as a comma-separated list containing single values and
               hyphen-separated ranges, such as  5,12-14,23,27. Each instance gets its
               array index value from the environment variable JOB_INDEX. The number of
               unique array indices that you specify with this parameter determines the
               number of job instances to run.
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
               in seconds for runs of the job. This property can only be specified if
               `run_mode` is `task`.
        :param str scale_memory_limit: (optional) Optional amount of memory set for
               the instance of the job. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
               The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G
               and M are the shorthand expressions for GB and MB. For more information see
               [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param int scale_retry_limit: (optional) The number of times to rerun an
               instance of the job before the job is marked as failed. This property can
               only be specified if `run_mode` is `task`.
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
        if (image_reference := _dict.get('image_reference')) is not None:
            args['image_reference'] = image_reference
        if (image_secret := _dict.get('image_secret')) is not None:
            args['image_secret'] = image_secret
        if (run_arguments := _dict.get('run_arguments')) is not None:
            args['run_arguments'] = run_arguments
        if (run_as_user := _dict.get('run_as_user')) is not None:
            args['run_as_user'] = run_as_user
        if (run_commands := _dict.get('run_commands')) is not None:
            args['run_commands'] = run_commands
        if (run_env_variables := _dict.get('run_env_variables')) is not None:
            args['run_env_variables'] = [EnvVarPrototype.from_dict(v) for v in run_env_variables]
        if (run_mode := _dict.get('run_mode')) is not None:
            args['run_mode'] = run_mode
        if (run_service_account := _dict.get('run_service_account')) is not None:
            args['run_service_account'] = run_service_account
        if (run_volume_mounts := _dict.get('run_volume_mounts')) is not None:
            args['run_volume_mounts'] = [VolumeMountPrototype.from_dict(v) for v in run_volume_mounts]
        if (scale_array_spec := _dict.get('scale_array_spec')) is not None:
            args['scale_array_spec'] = scale_array_spec
        if (scale_cpu_limit := _dict.get('scale_cpu_limit')) is not None:
            args['scale_cpu_limit'] = scale_cpu_limit
        if (scale_ephemeral_storage_limit := _dict.get('scale_ephemeral_storage_limit')) is not None:
            args['scale_ephemeral_storage_limit'] = scale_ephemeral_storage_limit
        if (scale_max_execution_time := _dict.get('scale_max_execution_time')) is not None:
            args['scale_max_execution_time'] = scale_max_execution_time
        if (scale_memory_limit := _dict.get('scale_memory_limit')) is not None:
            args['scale_memory_limit'] = scale_memory_limit
        if (scale_retry_limit := _dict.get('scale_retry_limit')) is not None:
            args['scale_retry_limit'] = scale_retry_limit
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
        mode, the `max_execution_time` and `retry_limit` properties apply. In `daemon`
        mode, since there is no timeout and failed instances are restarted indefinitely,
        the `max_execution_time` and `retry_limit` properties are not allowed.
        """

        TASK = 'task'
        DAEMON = 'daemon'

    class RunServiceAccountEnum(str, Enum):
        """
        The name of the service account. For built-in service accounts, you can use the
        shortened names `manager`, `none`, `reader`, and `writer`. This property must not
        be set on a job run, which references a job template.
        """

        DEFAULT = 'default'
        MANAGER = 'manager'
        READER = 'reader'
        WRITER = 'writer'
        NONE = 'none'


class JobRun:
    """
    Response model for job run resources.

    :param List[EnvVar] computed_env_variables: (optional) References to config
          maps, secrets or literal values, which are defined and set by Code Engine and
          are exposed as environment variables in the job run.
    :param str created_at: (optional) The timestamp when the resource was created.
    :param str href: (optional) When you provision a new job run,  a URL is created
          identifying the location of the instance.
    :param str id: (optional) The identifier of the resource.
    :param str image_reference: (optional) The name of the image that is used for
          this job. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and
          `TAG` are optional. If `REGISTRY` is not specified, the default is `docker.io`.
          If `TAG` is not specified, the default is `latest`. If the image reference
          points to a registry that requires authentication, make sure to also specify the
          property `image_secret`.
    :param str image_secret: (optional) The name of the image registry access
          secret. The image registry access secret is used to authenticate with a private
          registry when you download the container image. If the image reference points to
          a registry that requires authentication, the job / job runs will be created but
          submitted job runs will fail, until this property is provided, too. This
          property must not be set on a job run, which references a job template.
    :param str job_name: (optional) Optional name of the job reference of this job
          run. If specified, the job run will inherit the configuration of the referenced
          job.
    :param str name: (optional) The name of the job run.
    :param str project_id: (optional) The ID of the project in which the resource is
          located.
    :param str region: (optional) The region of the project the resource is located
          in. Possible values: 'au-syd', 'br-sao', 'ca-tor', 'eu-de', 'eu-gb', 'jp-osa',
          'jp-tok', 'us-east', 'us-south'.
    :param str resource_type: (optional) The type of the job run.
    :param List[str] run_arguments: Set arguments for the job that are passed to
          start job run containers. If not specified an empty string array will be applied
          and the arguments specified by the container image, will be used to start the
          container.
    :param int run_as_user: (optional) The user ID (UID) to run the job.
    :param List[str] run_commands: Set commands for the job that are passed to start
          job run containers. If not specified an empty string array will be applied and
          the command specified by the container image, will be used to start the
          container.
    :param List[EnvVar] run_env_variables: References to config maps, secrets or
          literal values, which are defined by the function owner and are exposed as
          environment variables in the job run.
    :param str run_mode: (optional) The mode for runs of the job. Valid values are
          `task` and `daemon`. In `task` mode, the `max_execution_time` and `retry_limit`
          properties apply. In `daemon` mode, since there is no timeout and failed
          instances are restarted indefinitely, the `max_execution_time` and `retry_limit`
          properties are not allowed.
    :param str run_service_account: (optional) The name of the service account. For
          built-in service accounts, you can use the shortened names `manager`, `none`,
          `reader`, and `writer`. This property must not be set on a job run, which
          references a job template.
    :param List[VolumeMount] run_volume_mounts: Optional mounts of config maps or
          secrets.
    :param int scale_array_size_variable_override: (optional) Optional value to
          override the JOB_ARRAY_SIZE environment variable for a job run.
    :param str scale_array_spec: (optional) Define a custom set of array indices as
          a comma-separated list containing single values and hyphen-separated ranges,
          such as  5,12-14,23,27. Each instance gets its array index value from the
          environment variable JOB_INDEX. The number of unique array indices that you
          specify with this parameter determines the number of job instances to run.
    :param str scale_cpu_limit: (optional) Optional amount of CPU set for the
          instance of the job. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
    :param str scale_ephemeral_storage_limit: (optional) Optional amount of
          ephemeral storage to set for the instance of the job. The amount specified as
          ephemeral storage, must not exceed the amount of `scale_memory_limit`. The units
          for specifying ephemeral storage are Megabyte (M) or Gigabyte (G), whereas G and
          M are the shorthand expressions for GB and MB. For more information see [Units
          of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :param int scale_max_execution_time: (optional) The maximum execution time in
          seconds for runs of the job. This property can only be specified if `run_mode`
          is `task`.
    :param str scale_memory_limit: (optional) Optional amount of memory set for the
          instance of the job. For valid values see [Supported memory and CPU
          combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
          The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and
          M are the shorthand expressions for GB and MB. For more information see [Units
          of
          measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
    :param int scale_retry_limit: (optional) The number of times to rerun an
          instance of the job before the job is marked as failed. This property can only
          be specified if `run_mode` is `task`.
    :param str status: (optional) The current status of the job run.
    :param JobRunStatus status_details: (optional) The detailed status of the job
          run.
    """

    def __init__(
        self,
        run_arguments: List[str],
        run_commands: List[str],
        run_env_variables: List['EnvVar'],
        run_volume_mounts: List['VolumeMount'],
        *,
        computed_env_variables: Optional[List['EnvVar']] = None,
        created_at: Optional[str] = None,
        href: Optional[str] = None,
        id: Optional[str] = None,
        image_reference: Optional[str] = None,
        image_secret: Optional[str] = None,
        job_name: Optional[str] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        region: Optional[str] = None,
        resource_type: Optional[str] = None,
        run_as_user: Optional[int] = None,
        run_mode: Optional[str] = None,
        run_service_account: Optional[str] = None,
        scale_array_size_variable_override: Optional[int] = None,
        scale_array_spec: Optional[str] = None,
        scale_cpu_limit: Optional[str] = None,
        scale_ephemeral_storage_limit: Optional[str] = None,
        scale_max_execution_time: Optional[int] = None,
        scale_memory_limit: Optional[str] = None,
        scale_retry_limit: Optional[int] = None,
        status: Optional[str] = None,
        status_details: Optional['JobRunStatus'] = None,
    ) -> None:
        """
        Initialize a JobRun object.

        :param List[str] run_arguments: Set arguments for the job that are passed
               to start job run containers. If not specified an empty string array will be
               applied and the arguments specified by the container image, will be used to
               start the container.
        :param List[str] run_commands: Set commands for the job that are passed to
               start job run containers. If not specified an empty string array will be
               applied and the command specified by the container image, will be used to
               start the container.
        :param List[EnvVar] run_env_variables: References to config maps, secrets
               or literal values, which are defined by the function owner and are exposed
               as environment variables in the job run.
        :param List[VolumeMount] run_volume_mounts: Optional mounts of config maps
               or secrets.
        :param List[EnvVar] computed_env_variables: (optional) References to config
               maps, secrets or literal values, which are defined and set by Code Engine
               and are exposed as environment variables in the job run.
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
               is provided, too. This property must not be set on a job run, which
               references a job template.
        :param str job_name: (optional) Optional name of the job reference of this
               job run. If specified, the job run will inherit the configuration of the
               referenced job.
        :param str name: (optional) The name of the job run.
        :param int run_as_user: (optional) The user ID (UID) to run the job.
        :param str run_mode: (optional) The mode for runs of the job. Valid values
               are `task` and `daemon`. In `task` mode, the `max_execution_time` and
               `retry_limit` properties apply. In `daemon` mode, since there is no timeout
               and failed instances are restarted indefinitely, the `max_execution_time`
               and `retry_limit` properties are not allowed.
        :param str run_service_account: (optional) The name of the service account.
               For built-in service accounts, you can use the shortened names `manager`,
               `none`, `reader`, and `writer`. This property must not be set on a job run,
               which references a job template.
        :param int scale_array_size_variable_override: (optional) Optional value to
               override the JOB_ARRAY_SIZE environment variable for a job run.
        :param str scale_array_spec: (optional) Define a custom set of array
               indices as a comma-separated list containing single values and
               hyphen-separated ranges, such as  5,12-14,23,27. Each instance gets its
               array index value from the environment variable JOB_INDEX. The number of
               unique array indices that you specify with this parameter determines the
               number of job instances to run.
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
               in seconds for runs of the job. This property can only be specified if
               `run_mode` is `task`.
        :param str scale_memory_limit: (optional) Optional amount of memory set for
               the instance of the job. For valid values see [Supported memory and CPU
               combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
               The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G
               and M are the shorthand expressions for GB and MB. For more information see
               [Units of
               measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        :param int scale_retry_limit: (optional) The number of times to rerun an
               instance of the job before the job is marked as failed. This property can
               only be specified if `run_mode` is `task`.
        :param JobRunStatus status_details: (optional) The detailed status of the
               job run.
        """
        self.computed_env_variables = computed_env_variables
        self.created_at = created_at
        self.href = href
        self.id = id
        self.image_reference = image_reference
        self.image_secret = image_secret
        self.job_name = job_name
        self.name = name
        self.project_id = project_id
        self.region = region
        self.resource_type = resource_type
        self.run_arguments = run_arguments
        self.run_as_user = run_as_user
        self.run_commands = run_commands
        self.run_env_variables = run_env_variables
        self.run_mode = run_mode
        self.run_service_account = run_service_account
        self.run_volume_mounts = run_volume_mounts
        self.scale_array_size_variable_override = scale_array_size_variable_override
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
        if (computed_env_variables := _dict.get('computed_env_variables')) is not None:
            args['computed_env_variables'] = [EnvVar.from_dict(v) for v in computed_env_variables]
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = created_at
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (image_reference := _dict.get('image_reference')) is not None:
            args['image_reference'] = image_reference
        if (image_secret := _dict.get('image_secret')) is not None:
            args['image_secret'] = image_secret
        if (job_name := _dict.get('job_name')) is not None:
            args['job_name'] = job_name
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (project_id := _dict.get('project_id')) is not None:
            args['project_id'] = project_id
        if (region := _dict.get('region')) is not None:
            args['region'] = region
        if (resource_type := _dict.get('resource_type')) is not None:
            args['resource_type'] = resource_type
        if (run_arguments := _dict.get('run_arguments')) is not None:
            args['run_arguments'] = run_arguments
        else:
            raise ValueError('Required property \'run_arguments\' not present in JobRun JSON')
        if (run_as_user := _dict.get('run_as_user')) is not None:
            args['run_as_user'] = run_as_user
        if (run_commands := _dict.get('run_commands')) is not None:
            args['run_commands'] = run_commands
        else:
            raise ValueError('Required property \'run_commands\' not present in JobRun JSON')
        if (run_env_variables := _dict.get('run_env_variables')) is not None:
            args['run_env_variables'] = [EnvVar.from_dict(v) for v in run_env_variables]
        else:
            raise ValueError('Required property \'run_env_variables\' not present in JobRun JSON')
        if (run_mode := _dict.get('run_mode')) is not None:
            args['run_mode'] = run_mode
        if (run_service_account := _dict.get('run_service_account')) is not None:
            args['run_service_account'] = run_service_account
        if (run_volume_mounts := _dict.get('run_volume_mounts')) is not None:
            args['run_volume_mounts'] = [VolumeMount.from_dict(v) for v in run_volume_mounts]
        else:
            raise ValueError('Required property \'run_volume_mounts\' not present in JobRun JSON')
        if (scale_array_size_variable_override := _dict.get('scale_array_size_variable_override')) is not None:
            args['scale_array_size_variable_override'] = scale_array_size_variable_override
        if (scale_array_spec := _dict.get('scale_array_spec')) is not None:
            args['scale_array_spec'] = scale_array_spec
        if (scale_cpu_limit := _dict.get('scale_cpu_limit')) is not None:
            args['scale_cpu_limit'] = scale_cpu_limit
        if (scale_ephemeral_storage_limit := _dict.get('scale_ephemeral_storage_limit')) is not None:
            args['scale_ephemeral_storage_limit'] = scale_ephemeral_storage_limit
        if (scale_max_execution_time := _dict.get('scale_max_execution_time')) is not None:
            args['scale_max_execution_time'] = scale_max_execution_time
        if (scale_memory_limit := _dict.get('scale_memory_limit')) is not None:
            args['scale_memory_limit'] = scale_memory_limit
        if (scale_retry_limit := _dict.get('scale_retry_limit')) is not None:
            args['scale_retry_limit'] = scale_retry_limit
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (status_details := _dict.get('status_details')) is not None:
            args['status_details'] = JobRunStatus.from_dict(status_details)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a JobRun object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'computed_env_variables') and self.computed_env_variables is not None:
            computed_env_variables_list = []
            for v in self.computed_env_variables:
                if isinstance(v, dict):
                    computed_env_variables_list.append(v)
                else:
                    computed_env_variables_list.append(v.to_dict())
            _dict['computed_env_variables'] = computed_env_variables_list
        if hasattr(self, 'created_at') and getattr(self, 'created_at') is not None:
            _dict['created_at'] = getattr(self, 'created_at')
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'image_reference') and self.image_reference is not None:
            _dict['image_reference'] = self.image_reference
        if hasattr(self, 'image_secret') and self.image_secret is not None:
            _dict['image_secret'] = self.image_secret
        if hasattr(self, 'job_name') and self.job_name is not None:
            _dict['job_name'] = self.job_name
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'project_id') and getattr(self, 'project_id') is not None:
            _dict['project_id'] = getattr(self, 'project_id')
        if hasattr(self, 'region') and getattr(self, 'region') is not None:
            _dict['region'] = getattr(self, 'region')
        if hasattr(self, 'resource_type') and getattr(self, 'resource_type') is not None:
            _dict['resource_type'] = getattr(self, 'resource_type')
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
        if hasattr(self, 'scale_array_size_variable_override') and self.scale_array_size_variable_override is not None:
            _dict['scale_array_size_variable_override'] = self.scale_array_size_variable_override
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
        if hasattr(self, 'status') and getattr(self, 'status') is not None:
            _dict['status'] = getattr(self, 'status')
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
        mode, the `max_execution_time` and `retry_limit` properties apply. In `daemon`
        mode, since there is no timeout and failed instances are restarted indefinitely,
        the `max_execution_time` and `retry_limit` properties are not allowed.
        """

        TASK = 'task'
        DAEMON = 'daemon'

    class RunServiceAccountEnum(str, Enum):
        """
        The name of the service account. For built-in service accounts, you can use the
        shortened names `manager`, `none`, `reader`, and `writer`. This property must not
        be set on a job run, which references a job template.
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

        FAILED = 'failed'
        COMPLETED = 'completed'
        RUNNING = 'running'
        PENDING = 'pending'


class JobRunList:
    """
    Contains a list of job runs and pagination information.

    :param ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :param List[JobRun] job_runs: List of all jobs.
    :param int limit: Maximum number of resources per page.
    :param ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    """

    def __init__(
        self,
        job_runs: List['JobRun'],
        limit: int,
        *,
        first: Optional['ListFirstMetadata'] = None,
        next: Optional['ListNextMetadata'] = None,
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
        if (first := _dict.get('first')) is not None:
            args['first'] = ListFirstMetadata.from_dict(first)
        if (job_runs := _dict.get('job_runs')) is not None:
            args['job_runs'] = [JobRun.from_dict(v) for v in job_runs]
        else:
            raise ValueError('Required property \'job_runs\' not present in JobRunList JSON')
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in JobRunList JSON')
        if (next := _dict.get('next')) is not None:
            args['next'] = ListNextMetadata.from_dict(next)
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

    :param str completion_time: (optional) Time the job run completed.
    :param int failed: (optional) Number of failed job run instances.
    :param str failed_indices: (optional) List of job run indices that failed.
    :param int pending: (optional) Number of pending job run instances.
    :param str pending_indices: (optional) List of job run indices that are pending.
    :param int requested: (optional) Number of requested job run instances.
    :param int running: (optional) Number of running job run instances.
    :param str running_indices: (optional) List of job run indices that are running.
    :param str start_time: (optional) Time the job run started.
    :param int succeeded: (optional) Number of succeeded job run instances.
    :param str succeeded_indices: (optional) List of job run indices that succeeded.
    :param int unknown: (optional) Number of job run instances with unknown state.
    """

    def __init__(
        self,
        *,
        completion_time: Optional[str] = None,
        failed: Optional[int] = None,
        failed_indices: Optional[str] = None,
        pending: Optional[int] = None,
        pending_indices: Optional[str] = None,
        requested: Optional[int] = None,
        running: Optional[int] = None,
        running_indices: Optional[str] = None,
        start_time: Optional[str] = None,
        succeeded: Optional[int] = None,
        succeeded_indices: Optional[str] = None,
        unknown: Optional[int] = None,
    ) -> None:
        """
        Initialize a JobRunStatus object.

        """
        self.completion_time = completion_time
        self.failed = failed
        self.failed_indices = failed_indices
        self.pending = pending
        self.pending_indices = pending_indices
        self.requested = requested
        self.running = running
        self.running_indices = running_indices
        self.start_time = start_time
        self.succeeded = succeeded
        self.succeeded_indices = succeeded_indices
        self.unknown = unknown

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'JobRunStatus':
        """Initialize a JobRunStatus object from a json dictionary."""
        args = {}
        if (completion_time := _dict.get('completion_time')) is not None:
            args['completion_time'] = completion_time
        if (failed := _dict.get('failed')) is not None:
            args['failed'] = failed
        if (failed_indices := _dict.get('failed_indices')) is not None:
            args['failed_indices'] = failed_indices
        if (pending := _dict.get('pending')) is not None:
            args['pending'] = pending
        if (pending_indices := _dict.get('pending_indices')) is not None:
            args['pending_indices'] = pending_indices
        if (requested := _dict.get('requested')) is not None:
            args['requested'] = requested
        if (running := _dict.get('running')) is not None:
            args['running'] = running
        if (running_indices := _dict.get('running_indices')) is not None:
            args['running_indices'] = running_indices
        if (start_time := _dict.get('start_time')) is not None:
            args['start_time'] = start_time
        if (succeeded := _dict.get('succeeded')) is not None:
            args['succeeded'] = succeeded
        if (succeeded_indices := _dict.get('succeeded_indices')) is not None:
            args['succeeded_indices'] = succeeded_indices
        if (unknown := _dict.get('unknown')) is not None:
            args['unknown'] = unknown
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a JobRunStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'completion_time') and getattr(self, 'completion_time') is not None:
            _dict['completion_time'] = getattr(self, 'completion_time')
        if hasattr(self, 'failed') and getattr(self, 'failed') is not None:
            _dict['failed'] = getattr(self, 'failed')
        if hasattr(self, 'failed_indices') and getattr(self, 'failed_indices') is not None:
            _dict['failed_indices'] = getattr(self, 'failed_indices')
        if hasattr(self, 'pending') and getattr(self, 'pending') is not None:
            _dict['pending'] = getattr(self, 'pending')
        if hasattr(self, 'pending_indices') and getattr(self, 'pending_indices') is not None:
            _dict['pending_indices'] = getattr(self, 'pending_indices')
        if hasattr(self, 'requested') and getattr(self, 'requested') is not None:
            _dict['requested'] = getattr(self, 'requested')
        if hasattr(self, 'running') and getattr(self, 'running') is not None:
            _dict['running'] = getattr(self, 'running')
        if hasattr(self, 'running_indices') and getattr(self, 'running_indices') is not None:
            _dict['running_indices'] = getattr(self, 'running_indices')
        if hasattr(self, 'start_time') and getattr(self, 'start_time') is not None:
            _dict['start_time'] = getattr(self, 'start_time')
        if hasattr(self, 'succeeded') and getattr(self, 'succeeded') is not None:
            _dict['succeeded'] = getattr(self, 'succeeded')
        if hasattr(self, 'succeeded_indices') and getattr(self, 'succeeded_indices') is not None:
            _dict['succeeded_indices'] = getattr(self, 'succeeded_indices')
        if hasattr(self, 'unknown') and getattr(self, 'unknown') is not None:
            _dict['unknown'] = getattr(self, 'unknown')
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

    :param str href: (optional) Href that points to the first page.
    """

    def __init__(
        self,
        *,
        href: Optional[str] = None,
    ) -> None:
        """
        Initialize a ListFirstMetadata object.

        :param str href: (optional) Href that points to the first page.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListFirstMetadata':
        """Initialize a ListFirstMetadata object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
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

    :param str href: (optional) Href that points to the next page.
    :param str start: (optional) Token.
    """

    def __init__(
        self,
        *,
        href: Optional[str] = None,
        start: Optional[str] = None,
    ) -> None:
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
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (start := _dict.get('start')) is not None:
            args['start'] = start
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


class OperatorSecretProps:
    """
    Properties for the IBM Cloud Operator Secret.

    :param str apikey_id: The ID of the apikey associated with the operator secret.
    :param List[str] resource_group_ids: The list of resource groups (by ID) that
          the operator secret can bind services in.
    :param ServiceIDRef serviceid: A reference to a Service ID.
    :param bool user_managed: Specifies whether the operator secret is user managed.
    """

    def __init__(
        self,
        apikey_id: str,
        resource_group_ids: List[str],
        serviceid: 'ServiceIDRef',
        user_managed: bool,
    ) -> None:
        """
        Initialize a OperatorSecretProps object.

        :param str apikey_id: The ID of the apikey associated with the operator
               secret.
        :param List[str] resource_group_ids: The list of resource groups (by ID)
               that the operator secret can bind services in.
        :param ServiceIDRef serviceid: A reference to a Service ID.
        :param bool user_managed: Specifies whether the operator secret is user
               managed.
        """
        self.apikey_id = apikey_id
        self.resource_group_ids = resource_group_ids
        self.serviceid = serviceid
        self.user_managed = user_managed

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OperatorSecretProps':
        """Initialize a OperatorSecretProps object from a json dictionary."""
        args = {}
        if (apikey_id := _dict.get('apikey_id')) is not None:
            args['apikey_id'] = apikey_id
        else:
            raise ValueError('Required property \'apikey_id\' not present in OperatorSecretProps JSON')
        if (resource_group_ids := _dict.get('resource_group_ids')) is not None:
            args['resource_group_ids'] = resource_group_ids
        else:
            raise ValueError('Required property \'resource_group_ids\' not present in OperatorSecretProps JSON')
        if (serviceid := _dict.get('serviceid')) is not None:
            args['serviceid'] = ServiceIDRef.from_dict(serviceid)
        else:
            raise ValueError('Required property \'serviceid\' not present in OperatorSecretProps JSON')
        if (user_managed := _dict.get('user_managed')) is not None:
            args['user_managed'] = user_managed
        else:
            raise ValueError('Required property \'user_managed\' not present in OperatorSecretProps JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OperatorSecretProps object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'apikey_id') and self.apikey_id is not None:
            _dict['apikey_id'] = self.apikey_id
        if hasattr(self, 'resource_group_ids') and self.resource_group_ids is not None:
            _dict['resource_group_ids'] = self.resource_group_ids
        if hasattr(self, 'serviceid') and self.serviceid is not None:
            if isinstance(self.serviceid, dict):
                _dict['serviceid'] = self.serviceid
            else:
                _dict['serviceid'] = self.serviceid.to_dict()
        if hasattr(self, 'user_managed') and self.user_managed is not None:
            _dict['user_managed'] = self.user_managed
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this OperatorSecretProps object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'OperatorSecretProps') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OperatorSecretProps') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class OperatorSecretPrototypeProps:
    """
    Properties for the IBM Cloud Operator Secrets.

    :param List[str] resource_group_ids: (optional) The list of resource groups (by
          ID) that the operator secret can bind services in.
    :param ServiceIDRefPrototype serviceid: (optional) A reference to the Service
          ID.
    """

    def __init__(
        self,
        *,
        resource_group_ids: Optional[List[str]] = None,
        serviceid: Optional['ServiceIDRefPrototype'] = None,
    ) -> None:
        """
        Initialize a OperatorSecretPrototypeProps object.

        :param List[str] resource_group_ids: (optional) The list of resource groups
               (by ID) that the operator secret can bind services in.
        :param ServiceIDRefPrototype serviceid: (optional) A reference to the
               Service ID.
        """
        self.resource_group_ids = resource_group_ids
        self.serviceid = serviceid

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OperatorSecretPrototypeProps':
        """Initialize a OperatorSecretPrototypeProps object from a json dictionary."""
        args = {}
        if (resource_group_ids := _dict.get('resource_group_ids')) is not None:
            args['resource_group_ids'] = resource_group_ids
        if (serviceid := _dict.get('serviceid')) is not None:
            args['serviceid'] = ServiceIDRefPrototype.from_dict(serviceid)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OperatorSecretPrototypeProps object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resource_group_ids') and self.resource_group_ids is not None:
            _dict['resource_group_ids'] = self.resource_group_ids
        if hasattr(self, 'serviceid') and self.serviceid is not None:
            if isinstance(self.serviceid, dict):
                _dict['serviceid'] = self.serviceid
            else:
                _dict['serviceid'] = self.serviceid.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this OperatorSecretPrototypeProps object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'OperatorSecretPrototypeProps') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OperatorSecretPrototypeProps') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Probe:
    """
    Response model for probes.

    :param int failure_threshold: (optional) The number of consecutive, unsuccessful
          checks for the probe to be considered failed.
    :param int initial_delay: (optional) The amount of time in seconds to wait
          before the first probe check is performed.
    :param int interval: (optional) The amount of time in seconds between probe
          checks.
    :param str path: (optional) The path of the HTTP request to the resource. A path
          is only supported for a probe with a `type` of `http`.
    :param int port: (optional) The port on which to probe the resource.
    :param int timeout: (optional) The amount of time in seconds that the probe
          waits for a response from the application before it times out and fails.
    :param str type: (optional) Specifies whether to use HTTP or TCP for the probe
          checks. The default is TCP.
    """

    def __init__(
        self,
        *,
        failure_threshold: Optional[int] = None,
        initial_delay: Optional[int] = None,
        interval: Optional[int] = None,
        path: Optional[str] = None,
        port: Optional[int] = None,
        timeout: Optional[int] = None,
        type: Optional[str] = None,
    ) -> None:
        """
        Initialize a Probe object.

        :param int failure_threshold: (optional) The number of consecutive,
               unsuccessful checks for the probe to be considered failed.
        :param int initial_delay: (optional) The amount of time in seconds to wait
               before the first probe check is performed.
        :param int interval: (optional) The amount of time in seconds between probe
               checks.
        :param str path: (optional) The path of the HTTP request to the resource. A
               path is only supported for a probe with a `type` of `http`.
        :param int port: (optional) The port on which to probe the resource.
        :param int timeout: (optional) The amount of time in seconds that the probe
               waits for a response from the application before it times out and fails.
        :param str type: (optional) Specifies whether to use HTTP or TCP for the
               probe checks. The default is TCP.
        """
        self.failure_threshold = failure_threshold
        self.initial_delay = initial_delay
        self.interval = interval
        self.path = path
        self.port = port
        self.timeout = timeout
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Probe':
        """Initialize a Probe object from a json dictionary."""
        args = {}
        if (failure_threshold := _dict.get('failure_threshold')) is not None:
            args['failure_threshold'] = failure_threshold
        if (initial_delay := _dict.get('initial_delay')) is not None:
            args['initial_delay'] = initial_delay
        if (interval := _dict.get('interval')) is not None:
            args['interval'] = interval
        if (path := _dict.get('path')) is not None:
            args['path'] = path
        if (port := _dict.get('port')) is not None:
            args['port'] = port
        if (timeout := _dict.get('timeout')) is not None:
            args['timeout'] = timeout
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Probe object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'failure_threshold') and self.failure_threshold is not None:
            _dict['failure_threshold'] = self.failure_threshold
        if hasattr(self, 'initial_delay') and self.initial_delay is not None:
            _dict['initial_delay'] = self.initial_delay
        if hasattr(self, 'interval') and self.interval is not None:
            _dict['interval'] = self.interval
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        if hasattr(self, 'timeout') and self.timeout is not None:
            _dict['timeout'] = self.timeout
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Probe object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Probe') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Probe') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Specifies whether to use HTTP or TCP for the probe checks. The default is TCP.
        """

        TCP = 'tcp'
        HTTP = 'http'


class ProbePrototype:
    """
    Request model for probes.

    :param int failure_threshold: (optional) The number of consecutive, unsuccessful
          checks for the probe to be considered failed.
    :param int initial_delay: (optional) The amount of time in seconds to wait
          before the first probe check is performed.
    :param int interval: (optional) The amount of time in seconds between probe
          checks.
    :param str path: (optional) The path of the HTTP request to the resource. A path
          is only supported for a probe with a `type` of `http`.
    :param int port: (optional) The port on which to probe the resource.
    :param int timeout: (optional) The amount of time in seconds that the probe
          waits for a response from the application before it times out and fails.
    :param str type: (optional) Specifies whether to use HTTP or TCP for the probe
          checks. The default is TCP.
    """

    def __init__(
        self,
        *,
        failure_threshold: Optional[int] = None,
        initial_delay: Optional[int] = None,
        interval: Optional[int] = None,
        path: Optional[str] = None,
        port: Optional[int] = None,
        timeout: Optional[int] = None,
        type: Optional[str] = None,
    ) -> None:
        """
        Initialize a ProbePrototype object.

        :param int failure_threshold: (optional) The number of consecutive,
               unsuccessful checks for the probe to be considered failed.
        :param int initial_delay: (optional) The amount of time in seconds to wait
               before the first probe check is performed.
        :param int interval: (optional) The amount of time in seconds between probe
               checks.
        :param str path: (optional) The path of the HTTP request to the resource. A
               path is only supported for a probe with a `type` of `http`.
        :param int port: (optional) The port on which to probe the resource.
        :param int timeout: (optional) The amount of time in seconds that the probe
               waits for a response from the application before it times out and fails.
        :param str type: (optional) Specifies whether to use HTTP or TCP for the
               probe checks. The default is TCP.
        """
        self.failure_threshold = failure_threshold
        self.initial_delay = initial_delay
        self.interval = interval
        self.path = path
        self.port = port
        self.timeout = timeout
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProbePrototype':
        """Initialize a ProbePrototype object from a json dictionary."""
        args = {}
        if (failure_threshold := _dict.get('failure_threshold')) is not None:
            args['failure_threshold'] = failure_threshold
        if (initial_delay := _dict.get('initial_delay')) is not None:
            args['initial_delay'] = initial_delay
        if (interval := _dict.get('interval')) is not None:
            args['interval'] = interval
        if (path := _dict.get('path')) is not None:
            args['path'] = path
        if (port := _dict.get('port')) is not None:
            args['port'] = port
        if (timeout := _dict.get('timeout')) is not None:
            args['timeout'] = timeout
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProbePrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'failure_threshold') and self.failure_threshold is not None:
            _dict['failure_threshold'] = self.failure_threshold
        if hasattr(self, 'initial_delay') and self.initial_delay is not None:
            _dict['initial_delay'] = self.initial_delay
        if hasattr(self, 'interval') and self.interval is not None:
            _dict['interval'] = self.interval
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        if hasattr(self, 'timeout') and self.timeout is not None:
            _dict['timeout'] = self.timeout
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProbePrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProbePrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProbePrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Specifies whether to use HTTP or TCP for the probe checks. The default is TCP.
        """

        TCP = 'tcp'
        HTTP = 'http'


class Project:
    """
    Describes the model of a project.

    :param str account_id: (optional) An alphanumeric value identifying the account
          ID.
    :param str created_at: (optional) The timestamp when the project was created.
    :param str crn: (optional) The CRN of the project.
    :param str href: (optional) When you provision a new resource, a URL is created
          identifying the location of the instance.
    :param str id: (optional) The ID of the project.
    :param str name: The name of the project.
    :param str region: (optional) The region for your project deployment. Possible
          values: 'au-syd', 'br-sao', 'ca-tor', 'eu-de', 'eu-gb', 'jp-osa', 'jp-tok',
          'us-east', 'us-south'.
    :param str resource_group_id: The ID of the resource group.
    :param str resource_type: (optional) The type of the project.
    :param str status: (optional) The current state of the project. For example,
          when the project is created and is ready for use, the status of the project is
          active.
    """

    def __init__(
        self,
        name: str,
        resource_group_id: str,
        *,
        account_id: Optional[str] = None,
        created_at: Optional[str] = None,
        crn: Optional[str] = None,
        href: Optional[str] = None,
        id: Optional[str] = None,
        region: Optional[str] = None,
        resource_type: Optional[str] = None,
        status: Optional[str] = None,
    ) -> None:
        """
        Initialize a Project object.

        :param str name: The name of the project.
        :param str resource_group_id: The ID of the resource group.
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
        if (account_id := _dict.get('account_id')) is not None:
            args['account_id'] = account_id
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = created_at
        if (crn := _dict.get('crn')) is not None:
            args['crn'] = crn
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in Project JSON')
        if (region := _dict.get('region')) is not None:
            args['region'] = region
        if (resource_group_id := _dict.get('resource_group_id')) is not None:
            args['resource_group_id'] = resource_group_id
        else:
            raise ValueError('Required property \'resource_group_id\' not present in Project JSON')
        if (resource_type := _dict.get('resource_type')) is not None:
            args['resource_type'] = resource_type
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Project object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'account_id') and getattr(self, 'account_id') is not None:
            _dict['account_id'] = getattr(self, 'account_id')
        if hasattr(self, 'created_at') and getattr(self, 'created_at') is not None:
            _dict['created_at'] = getattr(self, 'created_at')
        if hasattr(self, 'crn') and getattr(self, 'crn') is not None:
            _dict['crn'] = getattr(self, 'crn')
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'region') and getattr(self, 'region') is not None:
            _dict['region'] = getattr(self, 'region')
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'resource_type') and getattr(self, 'resource_type') is not None:
            _dict['resource_type'] = getattr(self, 'resource_type')
        if hasattr(self, 'status') and getattr(self, 'status') is not None:
            _dict['status'] = getattr(self, 'status')
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
        The current state of the project. For example, when the project is created and is
        ready for use, the status of the project is active.
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


class ProjectEgressIPAddresses:
    """
    Describes the model of egress IP addresses.

    :param List[str] private: (optional) List of IBM private network IP addresses.
    :param List[str] public: (optional) List of public IP addresses.
    """

    def __init__(
        self,
        *,
        private: Optional[List[str]] = None,
        public: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a ProjectEgressIPAddresses object.

        :param List[str] private: (optional) List of IBM private network IP
               addresses.
        :param List[str] public: (optional) List of public IP addresses.
        """
        self.private = private
        self.public = public

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectEgressIPAddresses':
        """Initialize a ProjectEgressIPAddresses object from a json dictionary."""
        args = {}
        if (private := _dict.get('private')) is not None:
            args['private'] = private
        if (public := _dict.get('public')) is not None:
            args['public'] = public
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectEgressIPAddresses object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'private') and self.private is not None:
            _dict['private'] = self.private
        if hasattr(self, 'public') and self.public is not None:
            _dict['public'] = self.public
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectEgressIPAddresses object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectEgressIPAddresses') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectEgressIPAddresses') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectList:
    """
    Contains a list of projects and pagination information.

    :param ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :param int limit: Maximum number of resources per page.
    :param ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    :param List[Project] projects: List of projects.
    """

    def __init__(
        self,
        limit: int,
        projects: List['Project'],
        *,
        first: Optional['ListFirstMetadata'] = None,
        next: Optional['ListNextMetadata'] = None,
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
        if (first := _dict.get('first')) is not None:
            args['first'] = ListFirstMetadata.from_dict(first)
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in ProjectList JSON')
        if (next := _dict.get('next')) is not None:
            args['next'] = ListNextMetadata.from_dict(next)
        if (projects := _dict.get('projects')) is not None:
            args['projects'] = [Project.from_dict(v) for v in projects]
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


class ProjectStatusDetails:
    """
    Describes the model of a project status details.

    :param str domain: Status of the domain created for the project.
    :param str project: Defines whether a project is enabled for management and
          consumption.
    :param bool vpe_not_enabled: (optional) Return true when project is not VPE
          enabled.
    """

    def __init__(
        self,
        domain: str,
        project: str,
        *,
        vpe_not_enabled: Optional[bool] = None,
    ) -> None:
        """
        Initialize a ProjectStatusDetails object.

        :param str domain: Status of the domain created for the project.
        :param str project: Defines whether a project is enabled for management and
               consumption.
        :param bool vpe_not_enabled: (optional) Return true when project is not VPE
               enabled.
        """
        self.domain = domain
        self.project = project
        self.vpe_not_enabled = vpe_not_enabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectStatusDetails':
        """Initialize a ProjectStatusDetails object from a json dictionary."""
        args = {}
        if (domain := _dict.get('domain')) is not None:
            args['domain'] = domain
        else:
            raise ValueError('Required property \'domain\' not present in ProjectStatusDetails JSON')
        if (project := _dict.get('project')) is not None:
            args['project'] = project
        else:
            raise ValueError('Required property \'project\' not present in ProjectStatusDetails JSON')
        if (vpe_not_enabled := _dict.get('vpe_not_enabled')) is not None:
            args['vpe_not_enabled'] = vpe_not_enabled
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectStatusDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'domain') and self.domain is not None:
            _dict['domain'] = self.domain
        if hasattr(self, 'project') and self.project is not None:
            _dict['project'] = self.project
        if hasattr(self, 'vpe_not_enabled') and self.vpe_not_enabled is not None:
            _dict['vpe_not_enabled'] = self.vpe_not_enabled
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectStatusDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectStatusDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectStatusDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class DomainEnum(str, Enum):
        """
        Status of the domain created for the project.
        """

        UNKNOWN = 'unknown'
        READY = 'ready'

    class ProjectEnum(str, Enum):
        """
        Defines whether a project is enabled for management and consumption.
        """

        ENABLED = 'enabled'
        DISABLED = 'disabled'


class ResourceKeyRef:
    """
    The service credential associated with the secret.

    :param str id: (optional) ID of the service credential associated with the
          secret.
    :param str name: (optional) Name of the service credential associated with the
          secret.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> None:
        """
        Initialize a ResourceKeyRef object.

        :param str id: (optional) ID of the service credential associated with the
               secret.
        :param str name: (optional) Name of the service credential associated with
               the secret.
        """
        self.id = id
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceKeyRef':
        """Initialize a ResourceKeyRef object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceKeyRef object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceKeyRef object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceKeyRef') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceKeyRef') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ResourceKeyRefPrototype:
    """
    The service credential associated with the secret.

    :param str id: (optional) ID of the service credential associated with the
          secret.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a ResourceKeyRefPrototype object.

        :param str id: (optional) ID of the service credential associated with the
               secret.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceKeyRefPrototype':
        """Initialize a ResourceKeyRefPrototype object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceKeyRefPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceKeyRefPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceKeyRefPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceKeyRefPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RoleRef:
    """
    A reference to the Role and Role CRN for service binding.

    :param str crn: (optional) CRN of the IAM Role for this service access secret.
    :param str name: (optional) Role of the service credential.
    """

    def __init__(
        self,
        *,
        crn: Optional[str] = None,
        name: Optional[str] = None,
    ) -> None:
        """
        Initialize a RoleRef object.

        :param str crn: (optional) CRN of the IAM Role for this service access
               secret.
        :param str name: (optional) Role of the service credential.
        """
        self.crn = crn
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RoleRef':
        """Initialize a RoleRef object from a json dictionary."""
        args = {}
        if (crn := _dict.get('crn')) is not None:
            args['crn'] = crn
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RoleRef object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RoleRef object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RoleRef') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RoleRef') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RoleRefPrototype:
    """
    A reference to the Role and Role CRN for service binding.

    :param str crn: (optional) CRN of the IAM Role for this service access secret.
    """

    def __init__(
        self,
        *,
        crn: Optional[str] = None,
    ) -> None:
        """
        Initialize a RoleRefPrototype object.

        :param str crn: (optional) CRN of the IAM Role for this service access
               secret.
        """
        self.crn = crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RoleRefPrototype':
        """Initialize a RoleRefPrototype object from a json dictionary."""
        args = {}
        if (crn := _dict.get('crn')) is not None:
            args['crn'] = crn
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RoleRefPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RoleRefPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RoleRefPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RoleRefPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Secret:
    """
    Describes the model of a secret.

    :param str created_at: (optional) The timestamp when the resource was created.
    :param dict data: (optional) Data container that allows to specify config
          parameters and their values as a key-value map. Each key field must consist of
          alphanumeric characters, `-`, `_` or `.` and must not exceed a max length of 253
          characters. Each value field can consists of any character and must not exceed a
          max length of 1048576 characters.
    :param str entity_tag: The version of the secret instance, which is used to
          achieve optimistic locking.
    :param str format: (optional) Specify the format of the secret.
    :param str href: (optional) When you provision a new secret,  a URL is created
          identifying the location of the instance.
    :param str id: (optional) The identifier of the resource.
    :param str name: The name of the secret.
    :param str project_id: (optional) The ID of the project in which the resource is
          located.
    :param str region: (optional) The region of the project the resource is located
          in. Possible values: 'au-syd', 'br-sao', 'ca-tor', 'eu-de', 'eu-gb', 'jp-osa',
          'jp-tok', 'us-east', 'us-south'.
    :param str resource_type: (optional) The type of the secret.
    :param ServiceAccessSecretProps service_access: (optional) Properties for
          Service Access Secrets.
    :param OperatorSecretProps service_operator: (optional) Properties for the IBM
          Cloud Operator Secret.
    """

    def __init__(
        self,
        entity_tag: str,
        name: str,
        *,
        created_at: Optional[str] = None,
        data: Optional[dict] = None,
        format: Optional[str] = None,
        href: Optional[str] = None,
        id: Optional[str] = None,
        project_id: Optional[str] = None,
        region: Optional[str] = None,
        resource_type: Optional[str] = None,
        service_access: Optional['ServiceAccessSecretProps'] = None,
        service_operator: Optional['OperatorSecretProps'] = None,
    ) -> None:
        """
        Initialize a Secret object.

        :param str entity_tag: The version of the secret instance, which is used to
               achieve optimistic locking.
        :param str name: The name of the secret.
        :param dict data: (optional) Data container that allows to specify config
               parameters and their values as a key-value map. Each key field must consist
               of alphanumeric characters, `-`, `_` or `.` and must not exceed a max
               length of 253 characters. Each value field can consists of any character
               and must not exceed a max length of 1048576 characters.
        :param str format: (optional) Specify the format of the secret.
        :param ServiceAccessSecretProps service_access: (optional) Properties for
               Service Access Secrets.
        :param OperatorSecretProps service_operator: (optional) Properties for the
               IBM Cloud Operator Secret.
        """
        self.created_at = created_at
        self.data = data
        self.entity_tag = entity_tag
        self.format = format
        self.href = href
        self.id = id
        self.name = name
        self.project_id = project_id
        self.region = region
        self.resource_type = resource_type
        self.service_access = service_access
        self.service_operator = service_operator

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Secret':
        """Initialize a Secret object from a json dictionary."""
        args = {}
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = created_at
        if (data := _dict.get('data')) is not None:
            args['data'] = data
        if (entity_tag := _dict.get('entity_tag')) is not None:
            args['entity_tag'] = entity_tag
        else:
            raise ValueError('Required property \'entity_tag\' not present in Secret JSON')
        if (format := _dict.get('format')) is not None:
            args['format'] = format
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in Secret JSON')
        if (project_id := _dict.get('project_id')) is not None:
            args['project_id'] = project_id
        if (region := _dict.get('region')) is not None:
            args['region'] = region
        if (resource_type := _dict.get('resource_type')) is not None:
            args['resource_type'] = resource_type
        if (service_access := _dict.get('service_access')) is not None:
            args['service_access'] = ServiceAccessSecretProps.from_dict(service_access)
        if (service_operator := _dict.get('service_operator')) is not None:
            args['service_operator'] = OperatorSecretProps.from_dict(service_operator)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Secret object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'created_at') and getattr(self, 'created_at') is not None:
            _dict['created_at'] = getattr(self, 'created_at')
        if hasattr(self, 'data') and self.data is not None:
            _dict['data'] = self.data
        if hasattr(self, 'entity_tag') and self.entity_tag is not None:
            _dict['entity_tag'] = self.entity_tag
        if hasattr(self, 'format') and self.format is not None:
            _dict['format'] = self.format
        if hasattr(self, 'href') and getattr(self, 'href') is not None:
            _dict['href'] = getattr(self, 'href')
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            _dict['id'] = getattr(self, 'id')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'project_id') and getattr(self, 'project_id') is not None:
            _dict['project_id'] = getattr(self, 'project_id')
        if hasattr(self, 'region') and getattr(self, 'region') is not None:
            _dict['region'] = getattr(self, 'region')
        if hasattr(self, 'resource_type') and getattr(self, 'resource_type') is not None:
            _dict['resource_type'] = getattr(self, 'resource_type')
        if hasattr(self, 'service_access') and self.service_access is not None:
            if isinstance(self.service_access, dict):
                _dict['service_access'] = self.service_access
            else:
                _dict['service_access'] = self.service_access.to_dict()
        if hasattr(self, 'service_operator') and self.service_operator is not None:
            if isinstance(self.service_operator, dict):
                _dict['service_operator'] = self.service_operator
            else:
                _dict['service_operator'] = self.service_operator.to_dict()
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
        SERVICE_OPERATOR = 'service_operator'
        OTHER = 'other'


class SecretData:
    """
    Data container that allows to specify config parameters and their values as a
    key-value map. Each key field must consist of alphanumeric characters, `-`, `_` or `.`
    and must not exceed a max length of 253 characters. Each value field can consists of
    any character and must not exceed a max length of 1048576 characters.


    This type supports additional properties of type str.
    """

    def __init__(
        self,
        **kwargs: Optional[str],
    ) -> None:
        """
        Initialize a SecretData object.

        :param str **kwargs: (optional) Additional properties of type str
        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(
                [
                    'SecretDataGenericSecretData',
                    'SecretDataBasicAuthSecretData',
                    'SecretDataRegistrySecretData',
                    'SecretDataSSHSecretData',
                    'SecretDataTLSSecretData',
                ]
            )
        )
        raise Exception(msg)


class SecretList:
    """
    List of secret resources.

    :param ListFirstMetadata first: (optional) Describes properties needed to
          retrieve the first page of a result list.
    :param int limit: Maximum number of resources per page.
    :param ListNextMetadata next: (optional) Describes properties needed to retrieve
          the next page of a result list.
    :param List[Secret] secrets: List of secrets.
    """

    def __init__(
        self,
        limit: int,
        secrets: List['Secret'],
        *,
        first: Optional['ListFirstMetadata'] = None,
        next: Optional['ListNextMetadata'] = None,
    ) -> None:
        """
        Initialize a SecretList object.

        :param int limit: Maximum number of resources per page.
        :param List[Secret] secrets: List of secrets.
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
        if (first := _dict.get('first')) is not None:
            args['first'] = ListFirstMetadata.from_dict(first)
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in SecretList JSON')
        if (next := _dict.get('next')) is not None:
            args['next'] = ListNextMetadata.from_dict(next)
        if (secrets := _dict.get('secrets')) is not None:
            args['secrets'] = [Secret.from_dict(v) for v in secrets]
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


class ServiceAccessSecretProps:
    """
    Properties for Service Access Secrets.

    :param ResourceKeyRef resource_key: The service credential associated with the
          secret.
    :param RoleRef role: (optional) A reference to the Role and Role CRN for service
          binding.
    :param ServiceInstanceRef service_instance: The IBM Cloud service instance
          associated with the secret.
    :param ServiceIDRef serviceid: (optional) A reference to a Service ID.
    """

    def __init__(
        self,
        resource_key: 'ResourceKeyRef',
        service_instance: 'ServiceInstanceRef',
        *,
        role: Optional['RoleRef'] = None,
        serviceid: Optional['ServiceIDRef'] = None,
    ) -> None:
        """
        Initialize a ServiceAccessSecretProps object.

        :param ResourceKeyRef resource_key: The service credential associated with
               the secret.
        :param ServiceInstanceRef service_instance: The IBM Cloud service instance
               associated with the secret.
        :param RoleRef role: (optional) A reference to the Role and Role CRN for
               service binding.
        :param ServiceIDRef serviceid: (optional) A reference to a Service ID.
        """
        self.resource_key = resource_key
        self.role = role
        self.service_instance = service_instance
        self.serviceid = serviceid

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServiceAccessSecretProps':
        """Initialize a ServiceAccessSecretProps object from a json dictionary."""
        args = {}
        if (resource_key := _dict.get('resource_key')) is not None:
            args['resource_key'] = ResourceKeyRef.from_dict(resource_key)
        else:
            raise ValueError('Required property \'resource_key\' not present in ServiceAccessSecretProps JSON')
        if (role := _dict.get('role')) is not None:
            args['role'] = RoleRef.from_dict(role)
        if (service_instance := _dict.get('service_instance')) is not None:
            args['service_instance'] = ServiceInstanceRef.from_dict(service_instance)
        else:
            raise ValueError('Required property \'service_instance\' not present in ServiceAccessSecretProps JSON')
        if (serviceid := _dict.get('serviceid')) is not None:
            args['serviceid'] = ServiceIDRef.from_dict(serviceid)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServiceAccessSecretProps object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resource_key') and self.resource_key is not None:
            if isinstance(self.resource_key, dict):
                _dict['resource_key'] = self.resource_key
            else:
                _dict['resource_key'] = self.resource_key.to_dict()
        if hasattr(self, 'role') and self.role is not None:
            if isinstance(self.role, dict):
                _dict['role'] = self.role
            else:
                _dict['role'] = self.role.to_dict()
        if hasattr(self, 'service_instance') and self.service_instance is not None:
            if isinstance(self.service_instance, dict):
                _dict['service_instance'] = self.service_instance
            else:
                _dict['service_instance'] = self.service_instance.to_dict()
        if hasattr(self, 'serviceid') and self.serviceid is not None:
            if isinstance(self.serviceid, dict):
                _dict['serviceid'] = self.serviceid
            else:
                _dict['serviceid'] = self.serviceid.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ServiceAccessSecretProps object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServiceAccessSecretProps') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServiceAccessSecretProps') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ServiceAccessSecretPrototypeProps:
    """
    Properties for Service Access Secrets.

    :param ResourceKeyRefPrototype resource_key: The service credential associated
          with the secret.
    :param RoleRefPrototype role: (optional) A reference to the Role and Role CRN
          for service binding.
    :param ServiceInstanceRefPrototype service_instance: The IBM Cloud service
          instance associated with the secret.
    :param ServiceIDRef serviceid: (optional) A reference to a Service ID.
    """

    def __init__(
        self,
        resource_key: 'ResourceKeyRefPrototype',
        service_instance: 'ServiceInstanceRefPrototype',
        *,
        role: Optional['RoleRefPrototype'] = None,
        serviceid: Optional['ServiceIDRef'] = None,
    ) -> None:
        """
        Initialize a ServiceAccessSecretPrototypeProps object.

        :param ResourceKeyRefPrototype resource_key: The service credential
               associated with the secret.
        :param ServiceInstanceRefPrototype service_instance: The IBM Cloud service
               instance associated with the secret.
        :param RoleRefPrototype role: (optional) A reference to the Role and Role
               CRN for service binding.
        :param ServiceIDRef serviceid: (optional) A reference to a Service ID.
        """
        self.resource_key = resource_key
        self.role = role
        self.service_instance = service_instance
        self.serviceid = serviceid

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServiceAccessSecretPrototypeProps':
        """Initialize a ServiceAccessSecretPrototypeProps object from a json dictionary."""
        args = {}
        if (resource_key := _dict.get('resource_key')) is not None:
            args['resource_key'] = ResourceKeyRefPrototype.from_dict(resource_key)
        else:
            raise ValueError('Required property \'resource_key\' not present in ServiceAccessSecretPrototypeProps JSON')
        if (role := _dict.get('role')) is not None:
            args['role'] = RoleRefPrototype.from_dict(role)
        if (service_instance := _dict.get('service_instance')) is not None:
            args['service_instance'] = ServiceInstanceRefPrototype.from_dict(service_instance)
        else:
            raise ValueError(
                'Required property \'service_instance\' not present in ServiceAccessSecretPrototypeProps JSON'
            )
        if (serviceid := _dict.get('serviceid')) is not None:
            args['serviceid'] = ServiceIDRef.from_dict(serviceid)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServiceAccessSecretPrototypeProps object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resource_key') and self.resource_key is not None:
            if isinstance(self.resource_key, dict):
                _dict['resource_key'] = self.resource_key
            else:
                _dict['resource_key'] = self.resource_key.to_dict()
        if hasattr(self, 'role') and self.role is not None:
            if isinstance(self.role, dict):
                _dict['role'] = self.role
            else:
                _dict['role'] = self.role.to_dict()
        if hasattr(self, 'service_instance') and self.service_instance is not None:
            if isinstance(self.service_instance, dict):
                _dict['service_instance'] = self.service_instance
            else:
                _dict['service_instance'] = self.service_instance.to_dict()
        if hasattr(self, 'serviceid') and self.serviceid is not None:
            if isinstance(self.serviceid, dict):
                _dict['serviceid'] = self.serviceid
            else:
                _dict['serviceid'] = self.serviceid.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ServiceAccessSecretPrototypeProps object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServiceAccessSecretPrototypeProps') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServiceAccessSecretPrototypeProps') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ServiceIDRef:
    """
    A reference to a Service ID.

    :param str crn: (optional) CRN value of a Service ID.
    :param str id: (optional) The ID of the Service ID.
    """

    def __init__(
        self,
        *,
        crn: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a ServiceIDRef object.

        :param str crn: (optional) CRN value of a Service ID.
        :param str id: (optional) The ID of the Service ID.
        """
        self.crn = crn
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServiceIDRef':
        """Initialize a ServiceIDRef object from a json dictionary."""
        args = {}
        if (crn := _dict.get('crn')) is not None:
            args['crn'] = crn
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServiceIDRef object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ServiceIDRef object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServiceIDRef') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServiceIDRef') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ServiceIDRefPrototype:
    """
    A reference to the Service ID.

    :param str id: (optional) The ID of the Service ID.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a ServiceIDRefPrototype object.

        :param str id: (optional) The ID of the Service ID.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServiceIDRefPrototype':
        """Initialize a ServiceIDRefPrototype object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServiceIDRefPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ServiceIDRefPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServiceIDRefPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServiceIDRefPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ServiceInstanceRef:
    """
    The IBM Cloud service instance associated with the secret.

    :param str id: (optional) ID of the IBM Cloud service instance associated with
          the secret.
    :param str type: (optional) Type of IBM Cloud service associated with the
          secret.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        type: Optional[str] = None,
    ) -> None:
        """
        Initialize a ServiceInstanceRef object.

        :param str id: (optional) ID of the IBM Cloud service instance associated
               with the secret.
        :param str type: (optional) Type of IBM Cloud service associated with the
               secret.
        """
        self.id = id
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServiceInstanceRef':
        """Initialize a ServiceInstanceRef object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServiceInstanceRef object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ServiceInstanceRef object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServiceInstanceRef') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServiceInstanceRef') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ServiceInstanceRefPrototype:
    """
    The IBM Cloud service instance associated with the secret.

    :param str id: (optional) ID of the IBM Cloud service instance associated with
          the secret.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a ServiceInstanceRefPrototype object.

        :param str id: (optional) ID of the IBM Cloud service instance associated
               with the secret.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServiceInstanceRefPrototype':
        """Initialize a ServiceInstanceRefPrototype object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServiceInstanceRefPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ServiceInstanceRefPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServiceInstanceRefPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServiceInstanceRefPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class VolumeMount:
    """
    Response model of a volume mount.

    :param str mount_path: The path that should be mounted.
    :param str name: The name of the mount.
    :param str reference: The name of the referenced secret or config map.
    :param str type: Specify the type of the volume mount. Allowed types are:
          'config_map', 'secret'.
    """

    def __init__(
        self,
        mount_path: str,
        name: str,
        reference: str,
        type: str,
    ) -> None:
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
        if (mount_path := _dict.get('mount_path')) is not None:
            args['mount_path'] = mount_path
        else:
            raise ValueError('Required property \'mount_path\' not present in VolumeMount JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in VolumeMount JSON')
        if (reference := _dict.get('reference')) is not None:
            args['reference'] = reference
        else:
            raise ValueError('Required property \'reference\' not present in VolumeMount JSON')
        if (type := _dict.get('type')) is not None:
            args['type'] = type
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

    :param str mount_path: The path that should be mounted.
    :param str name: (optional) Optional name of the mount. If not set, it will be
          generated based on the `ref` and a random ID. In case the `ref` is longer than
          58 characters, it will be cut off.
    :param str reference: The name of the referenced secret or config map.
    :param str type: Specify the type of the volume mount. Allowed types are:
          'config_map', 'secret'.
    """

    def __init__(
        self,
        mount_path: str,
        reference: str,
        type: str,
        *,
        name: Optional[str] = None,
    ) -> None:
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
        if (mount_path := _dict.get('mount_path')) is not None:
            args['mount_path'] = mount_path
        else:
            raise ValueError('Required property \'mount_path\' not present in VolumeMountPrototype JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (reference := _dict.get('reference')) is not None:
            args['reference'] = reference
        else:
            raise ValueError('Required property \'reference\' not present in VolumeMountPrototype JSON')
        if (type := _dict.get('type')) is not None:
            args['type'] = type
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


class AllowedOutboundDestinationPatchCidrBlockDataPatch(AllowedOutboundDestinationPatch):
    """
    Update an allowed outbound destination by using a CIDR block.

    :param str type: (optional) Specify the type of the allowed outbound
          destination. Allowed types are: 'cidr_block'.
    :param str cidr_block: (optional) The IP address range.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        cidr_block: Optional[str] = None,
    ) -> None:
        """
        Initialize a AllowedOutboundDestinationPatchCidrBlockDataPatch object.

        :param str type: (optional) Specify the type of the allowed outbound
               destination. Allowed types are: 'cidr_block'.
        :param str cidr_block: (optional) The IP address range.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.cidr_block = cidr_block

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AllowedOutboundDestinationPatchCidrBlockDataPatch':
        """Initialize a AllowedOutboundDestinationPatchCidrBlockDataPatch object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (cidr_block := _dict.get('cidr_block')) is not None:
            args['cidr_block'] = cidr_block
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AllowedOutboundDestinationPatchCidrBlockDataPatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'cidr_block') and self.cidr_block is not None:
            _dict['cidr_block'] = self.cidr_block
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AllowedOutboundDestinationPatchCidrBlockDataPatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AllowedOutboundDestinationPatchCidrBlockDataPatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AllowedOutboundDestinationPatchCidrBlockDataPatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Specify the type of the allowed outbound destination. Allowed types are:
        'cidr_block'.
        """

        CIDR_BLOCK = 'cidr_block'


class AllowedOutboundDestinationPrototypeCidrBlockDataPrototype(AllowedOutboundDestinationPrototype):
    """
    Create an allowed outbound destination by using a CIDR block.

    :param str type: Specify the type of the allowed outbound destination. Allowed
          types are: 'cidr_block'.
    :param str cidr_block: The IP address range.
    :param str name: The name of the CIDR block.
    """

    def __init__(
        self,
        type: str,
        cidr_block: str,
        name: str,
    ) -> None:
        """
        Initialize a AllowedOutboundDestinationPrototypeCidrBlockDataPrototype object.

        :param str type: Specify the type of the allowed outbound destination.
               Allowed types are: 'cidr_block'.
        :param str cidr_block: The IP address range.
        :param str name: The name of the CIDR block.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.cidr_block = cidr_block
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AllowedOutboundDestinationPrototypeCidrBlockDataPrototype':
        """Initialize a AllowedOutboundDestinationPrototypeCidrBlockDataPrototype object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError(
                'Required property \'type\' not present in AllowedOutboundDestinationPrototypeCidrBlockDataPrototype JSON'
            )
        if (cidr_block := _dict.get('cidr_block')) is not None:
            args['cidr_block'] = cidr_block
        else:
            raise ValueError(
                'Required property \'cidr_block\' not present in AllowedOutboundDestinationPrototypeCidrBlockDataPrototype JSON'
            )
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError(
                'Required property \'name\' not present in AllowedOutboundDestinationPrototypeCidrBlockDataPrototype JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AllowedOutboundDestinationPrototypeCidrBlockDataPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'cidr_block') and self.cidr_block is not None:
            _dict['cidr_block'] = self.cidr_block
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AllowedOutboundDestinationPrototypeCidrBlockDataPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AllowedOutboundDestinationPrototypeCidrBlockDataPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AllowedOutboundDestinationPrototypeCidrBlockDataPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Specify the type of the allowed outbound destination. Allowed types are:
        'cidr_block'.
        """

        CIDR_BLOCK = 'cidr_block'


class AllowedOutboundDestinationCidrBlockData(AllowedOutboundDestination):
    """
    Allowed outbound destination CIDR block.

    :param str entity_tag: The version of the allowed outbound destination, which is
          used to achieve optimistic locking.
    :param str type: Specify the type of the allowed outbound destination. Allowed
          types are: 'cidr_block'.
    :param str cidr_block: The IP address range.
    :param str name: The name of the CIDR block.
    """

    def __init__(
        self,
        entity_tag: str,
        type: str,
        cidr_block: str,
        name: str,
    ) -> None:
        """
        Initialize a AllowedOutboundDestinationCidrBlockData object.

        :param str entity_tag: The version of the allowed outbound destination,
               which is used to achieve optimistic locking.
        :param str type: Specify the type of the allowed outbound destination.
               Allowed types are: 'cidr_block'.
        :param str cidr_block: The IP address range.
        :param str name: The name of the CIDR block.
        """
        # pylint: disable=super-init-not-called
        self.entity_tag = entity_tag
        self.type = type
        self.cidr_block = cidr_block
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AllowedOutboundDestinationCidrBlockData':
        """Initialize a AllowedOutboundDestinationCidrBlockData object from a json dictionary."""
        args = {}
        if (entity_tag := _dict.get('entity_tag')) is not None:
            args['entity_tag'] = entity_tag
        else:
            raise ValueError(
                'Required property \'entity_tag\' not present in AllowedOutboundDestinationCidrBlockData JSON'
            )
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in AllowedOutboundDestinationCidrBlockData JSON')
        if (cidr_block := _dict.get('cidr_block')) is not None:
            args['cidr_block'] = cidr_block
        else:
            raise ValueError(
                'Required property \'cidr_block\' not present in AllowedOutboundDestinationCidrBlockData JSON'
            )
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in AllowedOutboundDestinationCidrBlockData JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AllowedOutboundDestinationCidrBlockData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entity_tag') and self.entity_tag is not None:
            _dict['entity_tag'] = self.entity_tag
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'cidr_block') and self.cidr_block is not None:
            _dict['cidr_block'] = self.cidr_block
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AllowedOutboundDestinationCidrBlockData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AllowedOutboundDestinationCidrBlockData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AllowedOutboundDestinationCidrBlockData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Specify the type of the allowed outbound destination. Allowed types are:
        'cidr_block'.
        """

        CIDR_BLOCK = 'cidr_block'


class SecretDataBasicAuthSecretData(SecretData):
    """
    SecretDataBasicAuthSecretData.

    :param str username: Basic auth username.
    :param str password: Basic auth password.

    This type supports additional properties of type str.
    """

    # The set of defined properties for the class
    _properties = frozenset(['username', 'password'])

    def __init__(
        self,
        username: str,
        password: str,
        **kwargs: Optional[str],
    ) -> None:
        """
        Initialize a SecretDataBasicAuthSecretData object.

        :param str username: Basic auth username.
        :param str password: Basic auth password.
        :param str **kwargs: (optional) Additional properties of type str
        """
        # pylint: disable=super-init-not-called
        self.username = username
        self.password = password
        for k, v in kwargs.items():
            if k not in SecretDataBasicAuthSecretData._properties:
                if not isinstance(v, str):
                    raise ValueError('Value for additional property {} must be of type str'.format(k))
                setattr(self, k, v)
            else:
                raise ValueError('Property {} cannot be specified as an additional property'.format(k))

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecretDataBasicAuthSecretData':
        """Initialize a SecretDataBasicAuthSecretData object from a json dictionary."""
        args = {}
        if (username := _dict.get('username')) is not None:
            args['username'] = username
        else:
            raise ValueError('Required property \'username\' not present in SecretDataBasicAuthSecretData JSON')
        if (password := _dict.get('password')) is not None:
            args['password'] = password
        else:
            raise ValueError('Required property \'password\' not present in SecretDataBasicAuthSecretData JSON')
        for k, v in _dict.items():
            if k not in cls._properties:
                if not isinstance(v, str):
                    raise ValueError('Value for additional property {} must be of type str'.format(k))
                args[k] = v
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecretDataBasicAuthSecretData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'username') and self.username is not None:
            _dict['username'] = self.username
        if hasattr(self, 'password') and self.password is not None:
            _dict['password'] = self.password
        for k in [_k for _k in vars(self).keys() if _k not in SecretDataBasicAuthSecretData._properties]:
            _dict[k] = getattr(self, k)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return the additional properties from this instance of SecretDataBasicAuthSecretData in the form of a dict."""
        _dict = {}
        for k in [_k for _k in vars(self).keys() if _k not in SecretDataBasicAuthSecretData._properties]:
            _dict[k] = getattr(self, k)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of additional properties in this instance of SecretDataBasicAuthSecretData"""
        for k in [_k for _k in vars(self).keys() if _k not in SecretDataBasicAuthSecretData._properties]:
            delattr(self, k)
        for k, v in _dict.items():
            if k not in SecretDataBasicAuthSecretData._properties:
                if not isinstance(v, str):
                    raise ValueError('Value for additional property {} must be of type str'.format(k))
                setattr(self, k, v)
            else:
                raise ValueError('Property {} cannot be specified as an additional property'.format(_key))

    def __str__(self) -> str:
        """Return a `str` version of this SecretDataBasicAuthSecretData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecretDataBasicAuthSecretData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecretDataBasicAuthSecretData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SecretDataGenericSecretData(SecretData):
    """
    Data container that allows to specify config parameters and their values as a
    key-value map. Each key field must consist of alphanumeric characters, `-`, `_` or `.`
    and must not be exceed a max length of 253 characters. Each value field can consists
    of any character and must not be exceed a max length of 1048576 characters.


    This type supports additional properties of type str.
    """

    def __init__(
        self,
        **kwargs: Optional[str],
    ) -> None:
        """
        Initialize a SecretDataGenericSecretData object.

        :param str **kwargs: (optional) Additional properties of type str
        """
        # pylint: disable=super-init-not-called
        for k, v in kwargs.items():
            if not isinstance(v, str):
                raise ValueError('Value for additional property {} must be of type str'.format(k))
            setattr(self, k, v)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecretDataGenericSecretData':
        """Initialize a SecretDataGenericSecretData object from a json dictionary."""
        args = {}
        for k, v in _dict.items():
            if not isinstance(v, str):
                raise ValueError('Value for additional property {} must be of type str'.format(k))
            args[k] = v
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecretDataGenericSecretData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        for k in [_k for _k in vars(self).keys()]:
            _dict[k] = getattr(self, k)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return the additional properties from this instance of SecretDataGenericSecretData in the form of a dict."""
        _dict = {}
        for k in [_k for _k in vars(self).keys()]:
            _dict[k] = getattr(self, k)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of additional properties in this instance of SecretDataGenericSecretData"""
        for k in [_k for _k in vars(self).keys()]:
            delattr(self, k)
        for k, v in _dict.items():
            if not isinstance(v, str):
                raise ValueError('Value for additional property {} must be of type str'.format(k))
            setattr(self, k, v)

    def __str__(self) -> str:
        """Return a `str` version of this SecretDataGenericSecretData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecretDataGenericSecretData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecretDataGenericSecretData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SecretDataRegistrySecretData(SecretData):
    """
    SecretDataRegistrySecretData.

    :param str username: Registry username.
    :param str password: Registry password.
    :param str server: Registry server.
    :param str email: (optional) Registry email address.

    This type supports additional properties of type str.
    """

    # The set of defined properties for the class
    _properties = frozenset(['username', 'password', 'server', 'email'])

    def __init__(
        self,
        username: str,
        password: str,
        server: str,
        *,
        email: Optional[str] = None,
        **kwargs: Optional[str],
    ) -> None:
        """
        Initialize a SecretDataRegistrySecretData object.

        :param str username: Registry username.
        :param str password: Registry password.
        :param str server: Registry server.
        :param str email: (optional) Registry email address.
        :param str **kwargs: (optional) Additional properties of type str
        """
        # pylint: disable=super-init-not-called
        self.username = username
        self.password = password
        self.server = server
        self.email = email
        for k, v in kwargs.items():
            if k not in SecretDataRegistrySecretData._properties:
                if not isinstance(v, str):
                    raise ValueError('Value for additional property {} must be of type str'.format(k))
                setattr(self, k, v)
            else:
                raise ValueError('Property {} cannot be specified as an additional property'.format(k))

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecretDataRegistrySecretData':
        """Initialize a SecretDataRegistrySecretData object from a json dictionary."""
        args = {}
        if (username := _dict.get('username')) is not None:
            args['username'] = username
        else:
            raise ValueError('Required property \'username\' not present in SecretDataRegistrySecretData JSON')
        if (password := _dict.get('password')) is not None:
            args['password'] = password
        else:
            raise ValueError('Required property \'password\' not present in SecretDataRegistrySecretData JSON')
        if (server := _dict.get('server')) is not None:
            args['server'] = server
        else:
            raise ValueError('Required property \'server\' not present in SecretDataRegistrySecretData JSON')
        if (email := _dict.get('email')) is not None:
            args['email'] = email
        for k, v in _dict.items():
            if k not in cls._properties:
                if not isinstance(v, str):
                    raise ValueError('Value for additional property {} must be of type str'.format(k))
                args[k] = v
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecretDataRegistrySecretData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'username') and self.username is not None:
            _dict['username'] = self.username
        if hasattr(self, 'password') and self.password is not None:
            _dict['password'] = self.password
        if hasattr(self, 'server') and self.server is not None:
            _dict['server'] = self.server
        if hasattr(self, 'email') and self.email is not None:
            _dict['email'] = self.email
        for k in [_k for _k in vars(self).keys() if _k not in SecretDataRegistrySecretData._properties]:
            _dict[k] = getattr(self, k)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return the additional properties from this instance of SecretDataRegistrySecretData in the form of a dict."""
        _dict = {}
        for k in [_k for _k in vars(self).keys() if _k not in SecretDataRegistrySecretData._properties]:
            _dict[k] = getattr(self, k)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of additional properties in this instance of SecretDataRegistrySecretData"""
        for k in [_k for _k in vars(self).keys() if _k not in SecretDataRegistrySecretData._properties]:
            delattr(self, k)
        for k, v in _dict.items():
            if k not in SecretDataRegistrySecretData._properties:
                if not isinstance(v, str):
                    raise ValueError('Value for additional property {} must be of type str'.format(k))
                setattr(self, k, v)
            else:
                raise ValueError('Property {} cannot be specified as an additional property'.format(_key))

    def __str__(self) -> str:
        """Return a `str` version of this SecretDataRegistrySecretData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecretDataRegistrySecretData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecretDataRegistrySecretData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SecretDataSSHSecretData(SecretData):
    """
    Secret Data field used by SSH secrets.

    :param str ssh_key: SSH key.
    :param str known_hosts: (optional) Known hosts.

    This type supports additional properties of type str.
    """

    # The set of defined properties for the class
    _properties = frozenset(['ssh_key', 'known_hosts'])

    def __init__(
        self,
        ssh_key: str,
        *,
        known_hosts: Optional[str] = None,
        **kwargs: Optional[str],
    ) -> None:
        """
        Initialize a SecretDataSSHSecretData object.

        :param str ssh_key: SSH key.
        :param str known_hosts: (optional) Known hosts.
        :param str **kwargs: (optional) Additional properties of type str
        """
        # pylint: disable=super-init-not-called
        self.ssh_key = ssh_key
        self.known_hosts = known_hosts
        for k, v in kwargs.items():
            if k not in SecretDataSSHSecretData._properties:
                if not isinstance(v, str):
                    raise ValueError('Value for additional property {} must be of type str'.format(k))
                setattr(self, k, v)
            else:
                raise ValueError('Property {} cannot be specified as an additional property'.format(k))

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecretDataSSHSecretData':
        """Initialize a SecretDataSSHSecretData object from a json dictionary."""
        args = {}
        if (ssh_key := _dict.get('ssh_key')) is not None:
            args['ssh_key'] = ssh_key
        else:
            raise ValueError('Required property \'ssh_key\' not present in SecretDataSSHSecretData JSON')
        if (known_hosts := _dict.get('known_hosts')) is not None:
            args['known_hosts'] = known_hosts
        for k, v in _dict.items():
            if k not in cls._properties:
                if not isinstance(v, str):
                    raise ValueError('Value for additional property {} must be of type str'.format(k))
                args[k] = v
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecretDataSSHSecretData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ssh_key') and self.ssh_key is not None:
            _dict['ssh_key'] = self.ssh_key
        if hasattr(self, 'known_hosts') and self.known_hosts is not None:
            _dict['known_hosts'] = self.known_hosts
        for k in [_k for _k in vars(self).keys() if _k not in SecretDataSSHSecretData._properties]:
            _dict[k] = getattr(self, k)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return the additional properties from this instance of SecretDataSSHSecretData in the form of a dict."""
        _dict = {}
        for k in [_k for _k in vars(self).keys() if _k not in SecretDataSSHSecretData._properties]:
            _dict[k] = getattr(self, k)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of additional properties in this instance of SecretDataSSHSecretData"""
        for k in [_k for _k in vars(self).keys() if _k not in SecretDataSSHSecretData._properties]:
            delattr(self, k)
        for k, v in _dict.items():
            if k not in SecretDataSSHSecretData._properties:
                if not isinstance(v, str):
                    raise ValueError('Value for additional property {} must be of type str'.format(k))
                setattr(self, k, v)
            else:
                raise ValueError('Property {} cannot be specified as an additional property'.format(_key))

    def __str__(self) -> str:
        """Return a `str` version of this SecretDataSSHSecretData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecretDataSSHSecretData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecretDataSSHSecretData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SecretDataTLSSecretData(SecretData):
    """
    SecretDataTLSSecretData.

    :param str tls_cert: The TLS certificate used in a TLS secret.
    :param str tls_key: The TLS key used in a TLS secret.

    This type supports additional properties of type str.
    """

    # The set of defined properties for the class
    _properties = frozenset(['tls_cert', 'tls_key'])

    def __init__(
        self,
        tls_cert: str,
        tls_key: str,
        **kwargs: Optional[str],
    ) -> None:
        """
        Initialize a SecretDataTLSSecretData object.

        :param str tls_cert: The TLS certificate used in a TLS secret.
        :param str tls_key: The TLS key used in a TLS secret.
        :param str **kwargs: (optional) Additional properties of type str
        """
        # pylint: disable=super-init-not-called
        self.tls_cert = tls_cert
        self.tls_key = tls_key
        for k, v in kwargs.items():
            if k not in SecretDataTLSSecretData._properties:
                if not isinstance(v, str):
                    raise ValueError('Value for additional property {} must be of type str'.format(k))
                setattr(self, k, v)
            else:
                raise ValueError('Property {} cannot be specified as an additional property'.format(k))

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecretDataTLSSecretData':
        """Initialize a SecretDataTLSSecretData object from a json dictionary."""
        args = {}
        if (tls_cert := _dict.get('tls_cert')) is not None:
            args['tls_cert'] = tls_cert
        else:
            raise ValueError('Required property \'tls_cert\' not present in SecretDataTLSSecretData JSON')
        if (tls_key := _dict.get('tls_key')) is not None:
            args['tls_key'] = tls_key
        else:
            raise ValueError('Required property \'tls_key\' not present in SecretDataTLSSecretData JSON')
        for k, v in _dict.items():
            if k not in cls._properties:
                if not isinstance(v, str):
                    raise ValueError('Value for additional property {} must be of type str'.format(k))
                args[k] = v
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecretDataTLSSecretData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'tls_cert') and self.tls_cert is not None:
            _dict['tls_cert'] = self.tls_cert
        if hasattr(self, 'tls_key') and self.tls_key is not None:
            _dict['tls_key'] = self.tls_key
        for k in [_k for _k in vars(self).keys() if _k not in SecretDataTLSSecretData._properties]:
            _dict[k] = getattr(self, k)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return the additional properties from this instance of SecretDataTLSSecretData in the form of a dict."""
        _dict = {}
        for k in [_k for _k in vars(self).keys() if _k not in SecretDataTLSSecretData._properties]:
            _dict[k] = getattr(self, k)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of additional properties in this instance of SecretDataTLSSecretData"""
        for k in [_k for _k in vars(self).keys() if _k not in SecretDataTLSSecretData._properties]:
            delattr(self, k)
        for k, v in _dict.items():
            if k not in SecretDataTLSSecretData._properties:
                if not isinstance(v, str):
                    raise ValueError('Value for additional property {} must be of type str'.format(k))
                setattr(self, k, v)
            else:
                raise ValueError('Property {} cannot be specified as an additional property'.format(_key))

    def __str__(self) -> str:
        """Return a `str` version of this SecretDataTLSSecretData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecretDataTLSSecretData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecretDataTLSSecretData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


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


class AllowedOutboundDestinationPager:
    """
    AllowedOutboundDestinationPager can be used to simplify the use of the "list_allowed_outbound_destination" method.
    """

    def __init__(
        self,
        *,
        client: CodeEngineV2,
        project_id: str,
        limit: int = None,
    ) -> None:
        """
        Initialize a AllowedOutboundDestinationPager object.
        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of allowed outbound
               destinations per page.
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
        :return: A List[dict], where each element is a dict that represents an instance of AllowedOutboundDestination.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_allowed_outbound_destination(
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

        return result.get('allowed_outbound_destinations')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of AllowedOutboundDestination.
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


class AppInstancesPager:
    """
    AppInstancesPager can be used to simplify the use of the "list_app_instances" method.
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
        Initialize a AppInstancesPager object.
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
        :return: A List[dict], where each element is a dict that represents an instance of AppInstance.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_app_instances(
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

        return result.get('instances')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of AppInstance.
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
        :param str job_name: (optional) Optional name of the job that you want to
               use to filter.
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


class FunctionsPager:
    """
    FunctionsPager can be used to simplify the use of the "list_functions" method.
    """

    def __init__(
        self,
        *,
        client: CodeEngineV2,
        project_id: str,
        limit: int = None,
    ) -> None:
        """
        Initialize a FunctionsPager object.
        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of functions per page.
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
        :return: A List[dict], where each element is a dict that represents an instance of Function.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_functions(
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

        return result.get('functions')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of Function.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class BindingsPager:
    """
    BindingsPager can be used to simplify the use of the "list_bindings" method.
    """

    def __init__(
        self,
        *,
        client: CodeEngineV2,
        project_id: str,
        limit: int = None,
    ) -> None:
        """
        Initialize a BindingsPager object.
        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of bindings per page.
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
        :return: A List[dict], where each element is a dict that represents an instance of Binding.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_bindings(
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

        return result.get('bindings')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of Binding.
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


class DomainMappingsPager:
    """
    DomainMappingsPager can be used to simplify the use of the "list_domain_mappings" method.
    """

    def __init__(
        self,
        *,
        client: CodeEngineV2,
        project_id: str,
        limit: int = None,
    ) -> None:
        """
        Initialize a DomainMappingsPager object.
        :param str project_id: The ID of the project.
        :param int limit: (optional) Optional maximum number of domain mappings per
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
        :return: A List[dict], where each element is a dict that represents an instance of DomainMapping.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_domain_mappings(
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

        return result.get('domain_mappings')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of DomainMapping.
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

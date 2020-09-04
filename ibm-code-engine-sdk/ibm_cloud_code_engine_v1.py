# coding: utf-8

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

# IBM OpenAPI SDK Code Generator Version: 3.12.0-64fe8d3f-20200820-144050
 
"""
The purpose is to provide an API to get Kubeconfig for IBM Cloud Code Engine Project
"""

from enum import Enum

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class IbmCloudCodeEngineV1(BaseService):
    """The IBM Cloud Code Engine V1 service."""

    DEFAULT_SERVICE_URL = 'https://ibm-cloud-code-engine.cloud.ibm.com/api/v1'
    DEFAULT_SERVICE_NAME = 'ibm_cloud_code_engine'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'IbmCloudCodeEngineV1':
        """
        Return a new client for the IBM Cloud Code Engine service using the
               specified parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the IBM Cloud Code Engine service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # getKubeconfig
    #########################


    def list_kubeconfig(self,
        refresh_token: str,
        id: str,
        *,
        accept: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve KUBECONFIG for a specified project.

        Returns the KUBECONFIG, similar to the output of `kubectl config view
        --minify=true`.

        :param str refresh_token: The IAM Refresh token associated with the IBM
               Cloud account.
        :param str id: The id of the IBM Cloud Code Engine project.
        :param str accept: (optional) The type of the response: application/json or
               text/html. A character encoding can be specified by including a `charset`
               parameter. For example, 'text/html;charset=utf-8'.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if refresh_token is None:
            raise ValueError('refresh_token must be provided')
        if id is None:
            raise ValueError('id must be provided')
        headers = {
            'Refresh-Token': refresh_token,
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_kubeconfig')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/namespaces/{0}/config'.format(
            *self.encode_path_vars(id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


class ListKubeconfigEnums:
    """
    Enums for list_kubeconfig parameters.
    """

    class Accept(str, Enum):
        """
        The type of the response: application/json or text/html. A character encoding can
        be specified by including a `charset` parameter. For example,
        'text/html;charset=utf-8'.
        """
        APPLICATION_JSON = 'application/json'
        TEXT_HTML = 'text/html'


##############################################################################
# Models
##############################################################################


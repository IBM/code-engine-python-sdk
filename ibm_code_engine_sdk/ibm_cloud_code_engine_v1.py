# coding: utf-8

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

# IBM OpenAPI SDK Code Generator Version: 3.15.0-45841b53-20201019-214802

"""
The purpose is to provide an API to get Kubeconfig file for IBM Cloud Code Engine Project
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
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'IbmCloudCodeEngineV1':
        """
        Return a new client for the IBM Cloud Code Engine service using the
               specified parameters and external configuration.
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
        Construct a new client for the IBM Cloud Code Engine service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)

    #########################
    # getKubeconfig
    #########################

    def list_kubeconfig(self, refresh_token: str, id: str, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Deprecated soon: Retrieve KUBECONFIG for a specified project.

        **Deprecated soon**: This API will be deprecated soon. Use the [GET
        /project/{id}/config](#get-kubeconfig) API instead. Returns the KUBECONFIG file,
        similar to the output of `kubectl config view --minify=true`.

        :param str refresh_token: The IAM Refresh token associated with the IBM
               Cloud account. To retrieve your IAM token, run `ibmcloud iam oauth-tokens`.
        :param str id: The id of the IBM Cloud Code Engine project. To retrieve
               your project ID, run `ibmcloud ce project get -n <PROJECT_NAME>`.
        :param str accept: (optional) The type of the response: text/plain or
               application/json. A character encoding can be specified by including a
               `charset` parameter. For example, 'text/plain;charset=utf-8'.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `str` result
        """

        if refresh_token is None:
            raise ValueError('refresh_token must be provided')
        if id is None:
            raise ValueError('id must be provided')
        headers = {'Refresh-Token': refresh_token, 'Accept': accept}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_kubeconfig'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/namespaces/{id}/config'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request)
        return response

    def get_kubeconfig(
        self, x_delegated_refresh_token: str, id: str, *, accept: str = None, **kwargs
    ) -> DetailedResponse:
        """
        Retrieve KUBECONFIG for a specified project.

        Returns the KUBECONFIG, similar to the output of `kubectl config view
        --minify=true`. There are 2 tokens in the Request Header and a query parameter
        that you must provide.
         These values can be generated as follows: 1. Auth Header Pass the generated IAM
        Token as the Authorization header from the CLI as `token=cat
        $HOME/.bluemix/config.json | jq .IAMToken -r`. Generate the token with the [Create
        an IAM access token for a user or service ID using an API
        key](https://cloud.ibm.com/apidocs/iam-identity-token-api#gettoken-apikey) API.
        2. X-Delegated-Refresh-Token Header Generate an IAM Delegated Refresh Token for
        Code Engine with the [Create an IAM access token and delegated refresh token for a
        user or service
        ID](https://cloud.ibm.com/apidocs/iam-identity-token-api#gettoken-apikey-delegatedrefreshtoken)
        API. Specify the `receiver_client_ids` value to be `ce` and the
        `delegated_refresh_token_expiry` value to be `3600`.
        3. Project ID In order to retrieve the Kubeconfig file for a specific Code Engine
        project, use the CLI to extract the ID
        `id=ibmcloud ce project get -n ${CE_PROJECT_NAME} -o jsonpath={.guid}` You must be
        logged into the account where the project was created to retrieve the ID.

        :param str x_delegated_refresh_token: This IAM Delegated Refresh Token is
               specifically valid for Code Engine. Generate this token with the [Create an
               IAM access token and delegated refresh token for a user or service
               ID](https://cloud.ibm.com/apidocs/iam-identity-token-api#gettoken-apikey-delegatedrefreshtoken)
               API. Specify the `receiver_client_ids` value to be `ce` and the
               `delegated_refresh_token_expiry` value to be `3600`.
        :param str id: The id of the IBM Cloud Code Engine project.
        :param str accept: (optional) The type of the response: text/plain or
               application/json. A character encoding can be specified by including a
               `charset` parameter. For example, 'text/plain;charset=utf-8'.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `str` result
        """

        if x_delegated_refresh_token is None:
            raise ValueError('x_delegated_refresh_token must be provided')
        if id is None:
            raise ValueError('id must be provided')
        headers = {'X-Delegated-Refresh-Token': x_delegated_refresh_token, 'Accept': accept}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_kubeconfig'
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/project/{id}/config'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request)
        return response


class ListKubeconfigEnums:
    """
    Enums for list_kubeconfig parameters.
    """

    class Accept(str, Enum):
        """
        The type of the response: text/plain or application/json. A character encoding can
        be specified by including a `charset` parameter. For example,
        'text/plain;charset=utf-8'.
        """

        TEXT_PLAIN = 'text/plain'
        APPLICATION_JSON = 'application/json'


class GetKubeconfigEnums:
    """
    Enums for get_kubeconfig parameters.
    """

    class Accept(str, Enum):
        """
        The type of the response: text/plain or application/json. A character encoding can
        be specified by including a `charset` parameter. For example,
        'text/plain;charset=utf-8'.
        """

        TEXT_PLAIN = 'text/plain'
        APPLICATION_JSON = 'application/json'


##############################################################################
# Models
##############################################################################

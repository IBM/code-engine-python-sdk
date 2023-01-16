"""
Example of IBM Cloud Code Engine SDK usage
"""

import os
import tempfile
import kubernetes
import requests
import json
from ibm_code_engine_sdk.ibm_cloud_code_engine_v1 import IbmCloudCodeEngineV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

if (
    os.environ.get('CE_API_KEY') == None
    or os.environ.get('CE_PROJECT_REGION') == None
    or os.environ.get('CE_PROJECT_ID') == None
):
    print(
        'You must set the envrionment variables CE_API_KEY, CE_PROJECT_REGION and CE_PROJECT_ID '
        + 'before using the example.'
    )

# Create an IAM authenticator.
authenticator = IAMAuthenticator(
    apikey=os.environ.get('CE_API_KEY'),
    client_id='bx',
    client_secret='bx',
)

# Construct the Code Engine client.
ce_client = IbmCloudCodeEngineV1(authenticator=authenticator)
ce_client.set_service_url('https://api.' + os.environ.get('CE_PROJECT_REGION') + '.codeengine.cloud.ibm.com/api/v1')

# Get a Delegated Refresh Token from IAM
iam_response = requests.post(
    'https://iam.cloud.ibm.com/identity/token',
    headers={'Content-Type': 'application/x-www-form-urlencoded'},
    data={
        'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
        'apikey': os.environ.get('CE_API_KEY'),
        'response_type': 'delegated_refresh_token',
        'receiver_client_ids': 'ce',
        'delegated_refresh_token_expiry': '3600',
    },
)
delegated_refresh_token = iam_response.json()['delegated_refresh_token']

# Get Code Engine project config using the Code Engine client.
kubeconfig_response = ce_client.get_kubeconfig(
    x_delegated_refresh_token=delegated_refresh_token,
    id=os.environ.get('CE_PROJECT_ID'),
)
kubeconfig_string = kubeconfig_response.get_result().content

# Setup Kubernetes client using project config
kubeconfig_file, kubeconfig_filename = tempfile.mkstemp()
os.write(kubeconfig_file, kubeconfig_string)
kubernetes.config.load_kube_config(config_file=kubeconfig_filename)
kube_client = kubernetes.client.CoreV1Api()

# Get something from project.
contexts = kubernetes.config.list_kube_config_contexts(config_file=kubeconfig_filename)[0][0]
namespace = contexts.get('context').get('namespace')
configmaps = kube_client.list_namespaced_config_map(namespace)
print('Project ' + os.environ.get('CE_PROJECT_ID') + ' has ' + str(len(configmaps.items)) + ' configmaps.')

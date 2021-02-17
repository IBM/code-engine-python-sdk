# Code Engine Python SDK Example

## Running example.py

To run the example, create a Code Engine project from the Console or Code Engine CLI, and run the following commands from this directory:
1. `pip install kubernetes`
2. `export CE_API_KEY=<Your IBM Cloud API key>`
3. `export CE_PROJECT_ID=<Your Code Engine project ID>`
4. `export CE_PROJECT_REGION=<The region (e.g. 'us-south') of your Code Engine project>`
5. `python example.py`

Note: Requires Python 3.6 or later.

## How-to

### Set up an authenticator
```python
authenticator = IAMAuthenticator(
    apikey=os.environ.get('CE_API_KEY'),
    client_id='bx',
    client_secret='bx',
)
```

### Set up a Code Engine client
```python
ce_client = IbmCloudCodeEngineV1(authenticator=authenticator)
ce_client.set_service_url(
    'https://api.' + os.environ.get('CE_PROJECT_REGION') + '.codeengine.cloud.ibm.com/api/v1'
)
```

### Use an HTTP library to get a Delegated Refresh Token from IAM
```python
iam_response = requests.post('https://iam.cloud.ibm.com/identity/token', headers={
    'Content-Type': 'application/x-www-form-urlencoded'
}, data={
    'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
    'apikey': os.environ.get('CE_API_KEY'),
    'response_type': 'delegated_refresh_token',
    'receiver_client_ids': 'ce',
    'delegated_refresh_token_expiry': '3600'
})
delegated_refresh_token = iam_response.json()['delegated_refresh_token']
```

### Use the Code Engine client to get a Kubernetes config
```python
kubeconfig_response = ce_client.get_kubeconfig(
    x_delegated_refresh_token=delegated_refresh_token,
    id=os.environ.get('CE_PROJECT_ID'),
)
kubeconfig_string = kubeconfig_response.get_result().content
```

## Deprecated endpoint
The `/namespaces/{id}/config` endpoint function, `list_kubeconfig()`, is deprecated, and will be removed before Code Engine is out of Beta. Please use the `get_kubeconfig()` function, demonstrated in the example above.

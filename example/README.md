# Code Engine Python SDK Example

## Running example.py

To run the example, create a Code Engine project from the Console or Code Engine CLI, and run the following commands from this directory:
1. `pip3 install kubernetes`
2. `export CE_API_KEY=<Your IBM Cloud API key>`
3. `export CE_PROJECT_ID=<Your Code Engine project ID>`
4. `export CE_PROJECT_REGION=<The region (e.g. 'us-south') of your Code Engine project>`
5. `python3 example.py`

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

### Use the Code Engine client to get a Kubernetes config
```python
refresh_token = authenticator.token_manager.request_token().get('refresh_token')
kubeconfig_response = ce_client.list_kubeconfig(
    refresh_token=refresh_token,
    id=os.environ.get('CE_PROJECT_ID'),
)
```

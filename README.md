# Example README - MYSDK

Python client library to use the [mysdk](mysdk-service-link-documention).

<details>
<summary>Table of Contents</summary>

* [Overview](#overview)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Authentication](#authentication)
* [Usage](#using-the-sdk)
* [Sample Code](#sample-code)
* [License](#license)

</details>

## Overview

The mysdk Python SDK allows developers to programmatically interact with the mysdk services, in the following ways:

* mysdk subclasses

## Prerequisites

[ibm-cloud-onboarding]: https://cloud.ibm.com/registration?target=%2Fdeveloper%2Fwatson&

* An [IBM Cloud][ibm-cloud-onboarding] account.
* An IAM API key to allow the SDK to access your account. Create one [here](https://cloud.ibm.com/iam/apikeys).
* An installation of Python >=3.5 on your local machine.

## Installation

To install, use `pip` or `easy_install`:

```bash
pip install --upgrade "mysdk>=0.0.1"
```

or

```bash
easy_install --upgrade "mysdk>=0.0.1"
```

## Authentication

mysdk uses token-based [Identity and Access Management (IAM) authentication](https://cloud.ibm.com/docs/iam?topic=iam-getstarted).

IAM authentication uses a service API key to get an access token that is passed with the call.
Access tokens are valid for a limited amount of time and must be regenerated.

To provide credentials to the SDK, you supply either an IAM service **API key** or an **access token**:

- Use the API key to have the SDK manage the lifecycle of the access token. The SDK requests an access token, ensures that the access token is valid, and refreshes it if necessary.
- Use the access token if you want to manage the lifecycle yourself. For details, see [Authenticating with IAM tokens](https://cloud.ibm.com/docs/services/watson/getting-started-iam.html).


#### Supplying the IAM API key:

```python
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('apikey')
mysdk_service = mysdk(authenticator=authenticator)
```

#### Generating bearer tokens using the IAM API key:

```python
from mysdk import IAMAuthenticator

# In your API endpoint use this to generate new bearer tokens
iam_token_manager = IAMAuthenticator('<apikey>')
token = iam_token_manager.get_token()
```

#### Supplying the access token:

```python
from mysdk import mysdk
from ibm_cloud_sdk_core.authenticators import BearerTokenAuthenticator

# in the constructor, assuming control of managing the token
authenticator = BearerTokenAuthenticator('your token')
mysdk_service = mysdk(authenticator=authenticator)
```

## Using the SDK

The mysdk Python SDK supports only synchronous (blocking) execution of service methods. The return value from all service methods is a DetailedResponse object. Use this SDK to perform the basic mysdk creation operation as follows, with the installation and initialization instructions from above:

```python
from mysdk import mysdk
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('your apikey')
mysdk_data = mysdk(authenticator=authenticator)

response = mysdk_data.list_data()
print(response)
```

This would give an output of `DetailedResponse` having the structure:

```
{
    'result': <response returned by service>,
    'headers': { <http response headers> },
    'status_code': <http status code>
}
```

You can use the `get_result()`, `get_headers()`, and `get_status_code()` to return the result, headers, and status code respectively.

### Sending request headers

Custom headers can be passed in any request in the form of a `dict` as:
```python
headers = {
    'Custom-Header': 'custom_value'
}
```
For example, to send a header called `Custom-Header` to a call in mysdk, pass the headers parameter as:

```python
from mysdk import mysdk
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('your apikey')
mysdk_service = mysdk(authenticator=authenticator)

response = mysdk_service.list_data(headers={'Custom-Header': 'custom_value'}).get_result()
```

### Transaction IDs

Every call from the SDK will receive a response which will contain a transaction ID, accessible via the `x-global-transaction-id` header.  This transaction ID is useful for troubleshooting and accessing relevant logs from your service instance.

### Error Handling

The mysdk Python SDK generates an exception for any unsuccessful method invocation.
If the method receives an error response from an API call to the service, it will generate an
`ApiException` with the following fields.

| NAME | DESCRIPTION |
| ----- | ----------- |
| code | The HTTP response code that is returned. |
| message	| A message that describes the error. |
| info	| A dictionary of additional information about the error. |


Exceptions that may be returned from a mysdk Python SDK method can be handled in the following way:

```python
from mysdk import ApiException
try:
  # Invoke an SDK method
  self.mysdk.method('does not exist')
except ApiException as e:
  # Handle exception
  print "Method failed with status code " + str(e.code) + ": " + e.message)
```

## Sample Code

See [Samples](Samples).

## License

The mysdk Python SDK is released under the Apache 2.0 license. The license's full text can be found in [LICENSE](LICENSE).

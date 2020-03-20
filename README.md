[![Build Status](https://travis.ibm.com/CloudEngineering/python-sdk-template.svg?token=eW5FVD71iyte6tTby8gr&branch=master)](https://travis.ibm.com/CloudEngineering/python-sdk-template)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)
# IBM Cloud MySDK Python SDK Version 0.0.1

Python client library to interact with various [MySDK Service APIs](https://cloud.ibm.com/apidocs?category=<service-category>).

## Table of Contents

<!--
  The TOC below is generated using the `markdown-toc` node package.

      https://github.com/jonschlinkert/markdown-toc

  You should regenerate the TOC after making changes to this file.

      npx markdown-toc -i README.md
  -->

<!-- toc -->

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Using the SDK](#using-the-sdk)
  * [Constructing service clients](#constructing-service-clients)
    + [Setting service client options programmatically](#setting-service-client-options-programmatically)
    + [Constructing a service client using external configuration](#constructing-a-service-client-using-external-configuration)
  * [Authentication](#authentication)
    + [Example: construct IAMAuthenticator with an IAM api key](#example-construct-iamauthenticator-with-an-iam-api-key)
    + [Example: construct BearerTokenAuthenticator with an access token](#example-construct-bearertokenauthenticator-with-an-access-token)
  * [Receiving operation responses](#receiving-operation-responses)
  * [Sending HTTP headers](#sending-http-headers)
    + [Sending HTTP headers with all requests](#sending-http-headers-with-all-requests)
    + [Sending request HTTP headers](#sending-request-http-headers)
  * [Transaction IDs](#transaction-ids)
  * [Error Handling](#error-handling)
  * [Configuring the http client](#configuring-the-http-client)
  * [Disable SSL certificate verification - Discouraged](#disable-ssl-certificate-verification---discouraged)
  * [Logging](#logging)
    + [Debug logging](#debug-logging)
    + [Detailed Request/Response Logging](#detailed-requestresponse-logging)
- [Questions](#questions)
- [Open source @ IBM](#open-source--ibm)
- [Contributing](#contributing)
- [License](#license)

<!-- tocstop -->

## Overview

The IBM Cloud MySDK Python SDK allows developers to programmatically interact with the following 
IBM Cloud services:

Service Name | Imported Class Name
--- | --- 
[Example Service](https://cloud.ibm.com/apidocs/example-service) | ExampleServiceV1

## Prerequisites

[ibm-cloud-onboarding]: https://cloud.ibm.com/registration?target=%2Fdeveloper%2Fwatson&

* An [IBM Cloud][ibm-cloud-onboarding] account.
* An IAM API key to allow the SDK to access your account. Create one [here](https://cloud.ibm.com/iam/apikeys).
* Python 3.5 or above.

## Installation

To install, use `pip` or `easy_install`:

```bash
pip install --upgrade "mysdk>=0.0.1"
```

or

```bash
easy_install --upgrade "mysdk>=0.0.1"
```

## Using the SDK
This section provides general information on how to use the services contained in this SDK.

### Constructing service clients
Each service is implemented as a class within the `mysdk` package
(e.g. class `ExampleServiceV1` within the `mysdk` package).
These "service client" classes provide a client-side representation of the service.

#### Setting service client options programmatically
Here's an example of how to construct an instance of a service (ExampleServiceV1) while specifying service
client options (authenticator, service endpoint URL, etc.) programmatically:

```python
from mysdk import ExampleServiceV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('my-iam-apikey')
my_service = ExampleServiceV1(authenticator=authenticator)
my_service.set_service_url('https://example-service.cloud.ibm.com/v1')

# Service operations can now be called using the "my_service" variable.
```

#### Constructing a service client using external configuration
For a typical application deployed to the IBM Cloud, it might be convenient to avoid hard-coding
certain service client options (IAM API Key, service endpoint URL, etc.).
Instead, the SDK allows you to store these values in configuration properties external to your
application.

##### Define configuration properties
First, define the configuration properties to be used by your application.  These properties
can be implemented as either (1) exported environment variables or (2) stored in a *credentials* file.
In the examples that follow, we'll use environment variables to implement our configuration properties.
Each property name is of the form: `<serviceName>_<propertyKey>`.
Here is an example of some configuration properties for the Resource Controller service:

```
export EXAMPLE_SERVICE_URL=https://example-service.cloud.ibm.com/v1
export EXAMPLE_SERVICE_AUTH_TYPE=iam
export EXAMPLE_SERVICE_APIKEY=my-iam-apikey
```

The service name "example_service" is the default service name for the "Example Service" service,
so the SDK will (by default) look for properties that start with this prefix folded to upper case.

##### Construct service client
After you have defined the configuration properties for your application, you can
construct an instance of the service client like this:

```python
from mysdk import ExampleServiceV1
my_service = ExampleServiceV1.new_instance()
```

The `ExampleServiceV1.new_instance()` method will:
1. construct an authenticator using the environment variables above (an IAM authenticator using "my-iam-apikey" as the api key).
2. initialize the service client to use a base endpoint URL of "https://example-service.cloud.ibm.com/v1" rather than the default URL.

##### Storing configuration properties in a file
Instead of exporting your configuration properties as environment variables, you can store the properties
in a *credentials* file.   Here is an example of a credentials file that contains the properties from the example above:

```
# Contents of "resource-controller.env"
EXAMPLE_SERVICE_URL=https://example-service.cloud.ibm.com/v1
EXAMPLE_SERVICE_AUTH_TYPE=iam
EXAMPLE_SERVICE_APIKEY=my-iam-apikey

```

You would then provide the name of the credentials file via the `IBM_CREDENTIALS_FILE` environment variable:

```
export IBM_CREDENTIALS_FILE=/myfolder/example-service.env
```

When the SDK needs to look for configuration properties, it will detect the `IBM_CREDENTIALS_FILE` environment
variable, then load the properties from the specified file.

##### Complete configuration-loading process
The above examples provide a glimpse of two specific ways to provide external configuration to the SDK
(environment variables and credentials file specified via the `IBM_CREDENTIALS_FILE` environment variable).

The complete configuration-loading process supported by the SDK is as follows:
1. Look for a credentials file whose name is specified by the `IBM_CREDENTIALS_FILE` environment variable
2. Look for a credentials file at `<current-working-director>/ibm-credentials.env`
3. Look for a credentials file at `<user-home-directory>/ibm-credentials.env`
4. Look for environment variables whose names start with `<upper-case-service-name>_` (e.g. `EXAMPLE_SERVICE_`)

At each of the above steps, if one or more configuration properties are found for the specified service,
those properties are then returned to the SDK and any subsequent steps are bypassed.


### Authentication
IBM Cloud services use token-based Identity and Access Management (IAM) authentication.

IAM authentication uses an API key to obtain an access token, which is then used to authenticate
each API request.  Access tokens are valid for a limited amount of time and must be refreshed or reacquired.

To provide credentials to the SDK, you can do one of the following:
1. Construct or configure an `IAMAuthenticator` instance with your IAM api key - in this case,
the SDK's IAMAuthenticator implementation will use your API key to obtain an access token, ensure that it is valid,
and will then include the access token in each outgoing request, refreshing it as needed.

2. Construct or configure a `BearerTokenAuthenticator` instance using an access token that you obtain yourself -
in this case, you are responsible for obtaining the access token and refreshing it as needed.

For more details about authentication, including the full set of authentication schemes supported by
the underlying Python Core library, see
[Authentication](https://github.com/IBM/python-sdk-core/blob/master/Authentication.md)

#### Example: construct IAMAuthenticator with an IAM api key

```python
from mysdk import ExampleServiceV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Let the SDK manage the IAM token
authenticator = IAMAuthenticator('apikey')
my_service = ExampleServiceV1(authenticator=authenticator)
```

#### Example: construct BearerTokenAuthenticator with an access token

```python
from mysdk import ExampleServiceV1
from ibm_cloud_sdk_core.authenticators import BearerTokenAuthenticator

# Manage the IAM access token within the application
authenticator = BearerTokenAuthenticator('<access token>')
my_service = ExampleServiceV1(authenticator=authenticator)

...

// Later when the access token expires, the application must refresh the access token,
// then set the new access token on the authenticator.
// Subsequent request invocations will include the new access token.
authenticator.set_bearer_token = /* new access token */
```

### Receiving operation responses

Each operation will return a DetailedResponse instance which encapsulates the operation response
object (if applicable), the HTTP status code and response headers.

Here's an example of how to access that response and get additional information beyond the response object:

```python
detailedResponse = my_service.get_resource(resource_id='resource-id-1')
print(detailedResponse)
```
This would display a `DetailedResponse` instance having the structure:
```
{
    'result': <response object returned by operation>,
    'headers': { <http response headers> },
    'status_code': <http status code>
}
```

### Sending HTTP headers

#### Sending HTTP headers with all requests

A set of default HTTP headers can be included with all requests by using the `set_default_headers()` 
method of the service client.

Here's an example that includes `Custom-Header` with each request invocation:

```python

headers = {
    'Custom-Header': 'custom_value'
}

my_service.set_default_headers(headers)

# "Custom-Header" will now be included with all subsequent requests invoked from "my_service".
```


#### Sending request HTTP headers
Custom HTTP headers can also be passed with any individual request.
Just pass the optional `headers` parameter when invoking the operation.

Here's an example that includes `Custom-Header` along with the `get_resource_instance` operation invocation:

```python
resourceInstance = my_service.get_resource(resource_id='resource-id-1', headers={'Custom-Header': 'custom_value'}).get_result()
```

### Transaction IDs
Every API invocation will receive a response that contains a transaction ID in the `x-global-transaction-id` HTTP header.
This transaction ID is useful for troubleshooting and accessing relevant logs from your service instance.
Here's an example of how to retrieve the `x-global-transaction-id` response header:

```python
try:
    response = my_service.get_resource(resource_id='resource-id-1')
    resourceInstance = response.get_result()
    response_headers = response.get_headers()
    transaction_id = response_headers.get('x-global-transaction-id')
except ApiException as e:
    transaction_id = e.http_response.headers.get('x-global-transaction-id')
```

### Error Handling

The IBM Cloud MySDK Python SDK generates an exception for any unsuccessful method invocation.
If the method receives an error response from an API call to the service, it will generate an
`ApiException` with the following fields.

| NAME | DESCRIPTION |
| ----- | ----------- |
| code | The HTTP response code that is returned. |
| message	| A message that describes the error. |
| info	| A dictionary of additional information about the error. |


Exceptions that may be returned from an IBM Cloud MySDK Python SDK method can be handled in the following way:

```python
try:
  my_service.get_resource(resource_id='does not exist')
except ApiException as e:
  print("Method failed with status code " + str(e.code) + ": " + e.message)
```
### Configuring the http client
To configure certain options in the underlying http client used to invoke requests (e.g. timeout), you can use the `set_http_config()` method, like this:

```python
my_service.set_http_config({'timeout': 120})
response = my_service.get_resource(resource_id='resource-id-1').get_result()
```

Here is a list of some of the configuration properties that can be set with the `set_http_config()` method:
- [timeout](https://requests.readthedocs.io/en/master/user/quickstart/#timeouts)
- [allow_redirects](https://requests.readthedocs.io/en/master/user/quickstart/#redirection-and-history)
- [proxies](https://requests.readthedocs.io/en/master/user/advanced/#proxies)
- [verify](https://requests.readthedocs.io/en/master/user/advanced/#ssl-cert-verification)
- [cert](https://requests.readthedocs.io/en/master/user/advanced/#client-side-certificates)

For more information regarding http client configuration, please see [this link](https://requests.readthedocs.io/en/master/).

### Disable SSL certificate verification - Discouraged
In certain circumstances, you might want to disable the verification of the server's SSL certificate.
While we recommend against this, you can use the `set_disable_ssl_verification()` method to do this:

```python
service.set_disable_ssl_verification(True)
```

Alternatively, you can configure the <service_name>_DISABLE_SSL external configuration property.   Here's an example that shows
how to do this for the "Example Service" service:

```
export EXAMPLE_SERVICE_DISABLE_SSL=True
```

### Logging
#### Debug logging
You can enable debug logging by importing the `logging` package and then setting the log level to DEBUG as in this example:

```
import logging
logging.basicConfig(level=logging.DEBUG)

```

This will cause messages like the following to be logged as your application invokes various operations:

```
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): iam.cloud.ibm.com:443
DEBUG:urllib3.connectionpool:https://iam.cloud.ibm.com:443 "POST /identity/token HTTP/1.1" 200 1809
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): example-service.cloud.ibm.com:443
DEBUG:urllib3.connectionpool:https://example-service.cloud.ibm.com:443 "POST /example/api/v1/resource HTTP/1.1" 201 None
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): example-service.cloud.ibm.com:443
DEBUG:urllib3.connectionpool:https://example-service.cloud.ibm.com:443 "GET /example/api/v1/resource/resource-id-1 HTTP/1.1" 200 None
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): example-service.cloud.ibm.com:443
DEBUG:urllib3.connectionpool:https://example-service.cloud.ibm.com:443 "DELETE /example/api/v1/resource/resource-id-1 HTTP/1.1" 204 None
```

#### Detailed Request/Response Logging
To enable detailed logging of request and response messages, you can import the `http.client` package, and then enable debug
logging within HTTP connections like this:
```
from http.client import HTTPConnection
HTTPConnection.debuglevel = 1
```

## Questions

If you are having difficulties using this SDK or have a question about the IBM Cloud services,
please ask a question at [dW Answers](https://developer.ibm.com/answers/questions/ask/?topics=ibm-cloud) or
[Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-cloud).

## Open source @ IBM
Find more open source projects on the [IBM Github Page](http://ibm.github.io/)

## Contributing
See [CONTRIBUTING](CONTRIBUTING.md).

## License

This SDK is released under the Apache 2.0 license.
The license's full text can be found in [LICENSE](LICENSE).

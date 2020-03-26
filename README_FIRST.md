# IBM Cloud Python SDK Template
This repository serves as a template for Python SDKs that are produced with the
[IBM OpenAPI SDK Generator](https://github.ibm.com/CloudEngineering/openapi-sdkgen).

You can use the contents of this repository to create your Python SDKs.

## How to use this repository

#### 1. Copy the repository
Copy the files contained in this repository as a starting point when building your Python SDK
for one or more IBM Cloud services.

#### 2. Modify the copied files to reflect your SDK

This template uses "mysdk" as the SDK/Package name.  You will need to change that to something
more meaningful for your service(s). Do a search in the template files for "mysdk" and replace with your
SDK/Package name.  In particular, you will need to update `setup.py` to reflect your package name using Python conventions.

You will need to add the `apiPackage` [configuration option](https://github.ibm.com/CloudEngineering/openapi-sdkgen/wiki/Config-Options)
to your API definition. Configuration options are added to the `info` section of the API definition using the `x-codegen-config` property.
Using the example below, replace "mysdk" with your SDK/Package name.

    info:
        x-codegen-config:
            python:
                apiPackage: 'mysdk'

The following specific files will need to be modified after copying them from this template repository:
* .travis.yml - Update this file as needed to incorporate any required steps for your SDK.

* setup.py - The name and definitions for your package need to be updated.

* common.py - Python SDKs built with the IBM OpenAPI SDK Generator need to include a common.py file, which contains a function called `get_sdk_headers`.  The `get_sdk_headers` function is invoked by the generated service methods and should be modified to suit the needs of your particular SDK.

* README.md - This file has most of the overarching topics you will need to cover.  Help your users by providing the basic CRUD operations in the usage sections and more advanced interactions in a `/samples` directory.

* __init__.py - This will need to be updated to reference the source code that you generate in Step #3.

* test/unit/ - Put your unit tests for your services here. Basic unit tests will be generated

* test/integration/ - Put your integration tests for your services here.

If needed, update your dependencies in the `requirements.txt` or `requirements-dev.text`

#### 3. Generate the Python code with the IBM OpenAPI SDK Generator
This is the step that you've been waiting for!

In this step, you'll invoke the IBM OpenAPI SDK Generator to process your API definition.

This will generate a collection of Python source files which you will need to include in your SDK project, in a directory with your package name.

You'll find instructions on how to do this on the [generator repository wiki](https://github.ibm.com/CloudEngineering/openapi-sdkgen/wiki/Usage-Instructions).

Set the output location for the generated files to the root directory of the project. If the `apiPackage` configuration option in your API definition matches the SDK/Package name of the directory
that holds your services (initially named "mysdk"), the generated files will be generated in that directory.

#### 4. Test your SDK
SDK tests are organized into *unit* and *integration* tests, which live in `test/unit/` and `test/integration/`, respectively. Unit tests mock the request framework and test that request objects are constructed properly. Integration tests make requests to live service instances and test that the SDK works as intended from end to end.

This repository uses [Pytest](https://docs.pytest.org/en/latest/) for its testing and mocking framework. To use the tests, use the following commands:

```bash
pip3 install -r requirements.txt
pip3 install .
python3 setup.py test
```

#### Integration tests
Integration tests must be developed by hand.
For integration tests to run properly with an actual running instance of the service,
credentials (e.g. IAM api key, etc.) must be provided as external configuration properties.
Details about this can be found
[here](https://github.com/IBM/ibm-cloud-sdk-common/blob/master/README.md#using-external-configuration).

An example integration test is located at `test/integration/test_example_service_v1.py`.
In order to run the "example service" integration test,
you'll need an actual running instance of the example service.
To run this service, clone the [Example Service repo](https://github.ibm.com/CloudEngineering/example-service)
and follow the instructions there for how to start up an instance of the example service.

Any additional files needed for testing (such as an image to send to a visual recognition service)
should be placed in `test/resources/`.

#### Continuous Integration
This repository is set up to use [Travis](https://travis-ci.com/)
or [Travis Enterprise](https://travis.ibm.com) for continuous integration.

The `.travis.yml` file contains all the instructions necessary to run the build.
An example `.travis.yml` file is supplied with this template repository.

For details related to the `travis.yml` file, see
[this](https://docs.travis-ci.com/user/customizing-the-build/)

##### Release management with semantic-release
The `.travis.yml` file included in this template repository is configured to
perform automated release management with
[semantic-release](https://semantic-release.gitbook.io/semantic-release/).

When you configure your SDK project in Travis, be sure to set this environment variable in your
Travis build settings:  
- `GH_TOKEN`: set this to the Github oauth token for a user having "push" access to your repository

If you are using Travis Enterprise (travis.ibm.com), you'll need to add these environment variables
as well:  
- `GH_URL`: set this to the string `https://github.ibm.com`
- `GH_PREFIX`: set this to the string `/api/v3`

##### Publishing build outputs to PyPI
If you will be publishing your build outputs to
[PyPI](https://pypi.org/), you'll need to add these environment variables to your
Travis build settings:  
- `PYPI_USER`: set this to the string `__token__`
- `PYPI_PASSWORD`: set this to your [PyPI API token](https://pypi.org/help/#apitoken)

## Encrypting secrets
To run integration tests within a Travis build, you'll need to encrypt the file containing the
required external configuration properties.
For details on how to do this, please see
[this](https://github.com/IBM/ibm-cloud-sdk-common/blob/master/EncryptingSecrets.md)


## Setting the ``User-Agent`` Header In Preparation for SDK Metrics Gathering

If you plan to gather metrics for your SDK, the `User-Agent` header value must be
a string similar to the following:
   `my-python-sdk/0.0.1 (lang=python; arch=x86_64; os=Linux; python.version=3.7.4)`

The key parts are the sdk name (`my-python-sdk`), version (`0.0.1`) and the
language name (`lang=python`).
This is required because the analytics data collector uses the User-Agent header included
with each request to gather usage data for IBM Cloud services.

The default implementation of the `get_sdk_headers` method provided in this SDK template
repository will need to be modified slightly for your SDK.
Replace the `my-python-sdk/0.0.1` part with the name and version of your
Python SDK. The rest of the system information should remain as-is.

For example, suppose your Python SDK project is called `platform-services-python-sdk` and its
version is `2.3.1`.
The `User-Agent` header value should be:
   `platform-services-python-sdk/2.3.1 (lang=python; arch=x86_64; os=Linux; python.version=3.7.4)`

__Note__: It is very important that the sdk name ends with the string `-sdk`,
as the analytics data collector uses this to gather usage data.

More information about the analytics tool, and other steps you should take to start gathering
metrics for your SDK can be found [here](https://github.ibm.com/CloudEngineering/sdk-analytics).

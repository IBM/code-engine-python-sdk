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
Integration tests must be written by hand for each service, if desired. For integration tests to run,
service credentials must be provided as external configuration properties.
Please see the [README.md](README.md) file for examples.

To set up and run the integration tests, clone the [Example Service repo](https://github.ibm.com/CloudEngineering/example-service)
and follow the instructions there for how to start up an instance of the example service.

An example integration test is located at `test/integration/test_example_service_v1.py`.
This example contains the imports necessary to run an integration test suite, including the **setUp** and **tearDown** functions.

Any additional files needed for testing (like an image to send to a visual recognition service) should be placed in `test/resources/`.

#### Continuous Integration
This repository is set up to use [Travis](https://travis-ci.org/) for continuous integration.

Note - to run integration tests on Travis, the `.env` file must be encrypted and the key stored in the
Travis settings as an environment variable.
Run the script `scripts/update-auth-file.sh` to generate an encrypted file and automatically set the key in Travis.
To do this:

1. Enable Travis-CI for your repository in Travis.
2. Make sure Ruby and Ruby Gem are installed and up to date on your local machine. You can [install Ruby here](https://www.ruby-lang.org/en/documentation/installation/)
3. Install Travis CLI (`gem install travis`). To verify installation, type `travis -v`
4. Log into Travis through CLI. Depending on whether you're trying to connect to Travis Enterprise or Public Travis, the commands will be different.

Here's the command for logging into Travis Enterprise:
```sh
travis login -X --github-token <your-github-enterprise-token> --api-endpoint https://travis.ibm.com/api
```

Here's the command for logging into Public Travis
```sh
travis login --github-token <your-public-github-token> --com
```

5. From the root of your SDK project, run the script in `scripts/update-auth-file.sh`
6. The script will generate a file called `.env.enc` in the project folder root directory. Commit the file to your repository
7. Terminal should print out a command to add to your build script. In that command is a string with the format similar to `encrypted_12345_key`. Copy that string
8. Replace the string `encrypted_12345_key` with the name of your generated environment variable from the last step
9. Replace the string `encrypted_12345_iv` with the name of your generated environment variable, but modify the string from `_key` to `_iv`
10. Commit the changes you made to the `.travis.yml` file and push to Github. Travis-CI pipeline should automatically start running

The config file `.travis.yml` contains all the instructions necessary to run the recommended build. Each step is described below.

The `before_script` step runs the instructions to decrypt the `.env.enc` file and run the `.env` file to set configuration properties as environment variables.
It only does for *pushes* to a branch. This is done so that integration tests only run on *push* builds and not on *pull request* builds.
The mechanism works because if there are no credentials defined via external configuration, the example integration test in `test_example_service_v1.py`
skips all of the tests.

The `script` section runs the instructions needed to verify the quality of the code by running unit tests,
integration tests and reporting code coverage. It first installs and upgrades `python-dotenv`.
Then, it runs the command to set up the python environment for python 3.5, 3.6, 3.7, and 3.8 and run tests using pytest and codecov.
For more details please see the [tox.ini](tox.ini) file.

The `deploy` section is the last step of the build and triggers the automated release management.
The repository uses [semantic-release](https://semantic-release.gitbook.io/semantic-release/) for automated release management.
The tool will determine if a release is warranted or not using the
[commit messages](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#commit).
Note that the format of your commit messages must comply with the requirements defined in the referenced page,
or the release will not work as intended.
If a release is warranted, the tool will determine what kind of release (patch, minor, or major) and proceed with the deployment.
The tool is configured in this repository to publish to [PyPI](https://pypi.org/) and update the changelog.
To run these deployments, you must add a `GH_TOKEN`, `PYPI_USER` and `PYPI_PASSWORD` as environment variables to the Travis settings.

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

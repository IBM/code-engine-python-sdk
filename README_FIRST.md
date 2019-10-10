# IBM Cloud Python SDK Template
This repository serves as a template for Python SDKs that are produced with the
[IBM OpenAPI SDK Generator](https://github.ibm.com/CloudEngineering/openapi-sdkgen).

You can use the contents of this repository to create your own Python SDKs.

## How to use this repository

##### 1. Copy the repository
Copy the files contained in this repository as a starting point when building your own Python SDK
for one or more IBM Cloud services.

##### 2. Modify the copied files to reflect your SDK

This template uses "mysdk" as the SDK/Package name.  You will need to change that to something
more meaningful for your service(s).  Do a search in the template files for "mysdk" and replace with your
SDK/Package name.  In particular, you will need to update `setup.py` to reflect your package name using Python conventions.

The following specific files will need to be modified after copying them from this template repository:
* .travis.yml - Update this file as needed to incorporate any required steps for your SDK.

* setup.py - The name and definitions for your package need to be updated.

* common.py - Python SDKs built with the IBM OpenAPI SDK Generator need to include a common.py file which contains a function called `get_sdk_headers`.  The `get_sdk_headers` function is invoked by the generated service methods and should be modified to suit the needs of your particular SDK.

* README.md - This file has most of the overarching topics you will need to cover.  Help your users by providing the basic CRUD operations in the usage sections and more advanced interactions in a `/samples` directory.

* __init__.py - This will need to be updated to reference the source code that you generate in Step #3.

* test/unit/test_common.py - put your unit tests for your services in here.

If needed, update your dependencies in the `requirements.txt` or `requirements-dev.text`

##### 3. Generate the Python code with the IBM OpenAPI SDK Generator
This is the step that you've been waiting for!

In this step, you'll invoke the IBM OpenAPI SDK Generator to process your API definition.

This will generate a collection of Python source files which you will need to include in your SDK project, in a directory with your package name.

You'll find instructions on how to do this on the [generator repository wiki](https://github.ibm.com/CloudEngineering/openapi-sdkgen/wiki/Usage-Instructions).

##### 4. Test your SDK
Install the dev requirements using `pip3 install requirements.txt` and use `pytest` to run your unit tests.

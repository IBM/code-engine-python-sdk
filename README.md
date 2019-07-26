# IBM Cloud Python SDK Template
This repository serves as a template for Python SDKs that are produced with the
[IBM OpenAPI SDK Generator](https://github.ibm.com/CloudEngineering/openapi-sdkgen).

You can use the contents of this repository to create your own Python SDKs.

## How to use this repository

##### 1. Copy the repository
Copy the files contained in this repository as a starting point when building your own Python SDK
for one or more IBM Cloud services.

##### 2. Modify the copied files to reflect your SDK

This template uses "mysdk" as the SDK/Package name.  You probably will want to change that to something
more meaningful for your service(s).  Do a search in the template files for "mysdk" and replace with your
SDK/Package name.

The following specific files will need to be modified after copying them from this template repository:
* .travis.yml - Update this file as needed to incorporate any required steps for your SDK


* common.py - Python SDKs built with the IBM OpenAPI SDK Generator
need to include a common.py file which contains a function called `get_sdk_headers`.  
The `get_sdk_headers` function is invoked by the generated service methods and should be modified to suit the
needs of your particular SDK.

##### 3. Generate the Python code with the IBM OpenAPI SDK Generator
This is the step that you've been waiting for!

In this step, you'll invoke the IBM OpenAPI SDK Generator to process your API definition.

This will generate a collection of Go source files which will be included in your SDK project.
You'll find instructions on how to do this [here](https://github.ibm.com/CloudEngineering/openapi-sdkgen/wiki).
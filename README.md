<!-- 
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)
-->
# Python SDK for IBM Cloud Code Engine 6.0.0

Python client library to interact with the [IBM Cloud Code Engine API](https://cloud.ibm.com/apidocs/codeengine).

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
- [Breaking Changes (April 2026)](#breaking-changes-april-2026)
- [Breaking Changes (March 2026)](#breaking-changes-march-2026)
- [Installation](#installation)
- [Using the SDK](#using-the-sdk)
- [Questions](#questions)
- [Issues](#issues)
- [Open source @ IBM](#open-source--ibm)
- [Contributing](#contributing)
- [License](#license)

<!-- tocstop -->

## Overview

The IBM Cloud Code Engine Python SDK allows developers to programmatically interact with the following
IBM Cloud services:

Service Name | Imported Class Name
--- | ---
[IBM Cloud Code Engine V2](https://cloud.ibm.com/apidocs/codeengine/codeengine-v6.0.0) | CodeEngineV2
[IBM Cloud Code Engine V1](https://cloud.ibm.com/apidocs/codeengine/codeengine-v6.0.0) | IbmCloudCodeEngineV1

## Prerequisites

[ibm-cloud-onboarding]: https://cloud.ibm.com/registration

* An [IBM Cloud][ibm-cloud-onboarding] account.
* An IAM API key to allow the SDK to access your account. Create one [here](https://cloud.ibm.com/iam/apikeys).
* Python 3.9 or above.

## Breaking Changes (April 2026)

As part of the introduction of `persistent_data_stores` as a Volume Mount type for **apps** and **jobs**, the optional `name` property of entries in `run_volume_mounts` is no longer supported.

If you used the optional `name` property, remove it from the prototype of the **app** or **job**.

## Breaking Changes (March 2026)

- **Service method renames (pluralization)**
    Update list methods and their `operation_id`s accordingly:

    ```python
    # before
    ce.list_allowed_outbound_destination(project_id, limit=100, start=token)

    # after
    ce.list_allowed_outbound_destinations(project_id, limit=100, start=token)
    ```

    ```python
    # before
    ce.list_persistent_data_store(project_id, limit=100, start=token)

    # after
    ce.list_persistent_data_stores(project_id, limit=100, start=token)
    ```

- **Pager class renames**
    Use the new pluralized pager classes and doc tag strings:

    ```python
    # before
    pager = ibm_code_engine_sdk.code_engine_v2.AllowedOutboundDestinationPager(ce, project_id, limit=100)

    # after
    pager = ibm_code_engine_sdk.code_engine_v2.AllowedOutboundDestinationsPager(ce, project_id, limit=100)
    ```

    ```python
    # before
    pager = ibm_code_engine_sdk.code_engine_v2.PersistentDataStorePager(ce, project_id, limit=100)

    # after
    pager = ibm_code_engine_sdk.code_engine_v2.PersistentDataStoresPager(ce, project_id, limit=100)
    ```

- **Allowed outbound destinations: new type & fields; constructor shape changes**
  - New type supported: `"private_path_service_gateway"` (in addition to `"cidr_block"`). Update any branching/validation on `type`.
  - New optional fields on `AllowedOutboundDestination` and subclasses:
    - `name`, `status`, `status_details`
    - Private Path specific: `private_path_service_gateway_crn`, `isolation_policy`
  - Base classes `AllowedOutboundDestination`, `AllowedOutboundDestinationPatch`, `AllowedOutboundDestinationPrototype`, `AllowedOutboundStatusDetails` are now **abstract** with expanded subclass sets. Instantiate the specific subclass instead, as before, but note the extended list.

- **Creation prototypes changed**
  - `AllowedOutboundDestinationPrototype` now **requires** `name`.
  - **CIDR prototype constructor order changed**:

      ```python
      from ibm_code_engine_sdk.code_engine_v2 import AllowedOutboundDestinationPrototypeCidrBlockDataPrototype
      # before: (type, cidr_block, name)
      # after:  (type, name, cidr_block)
      cidr_proto = AllowedOutboundDestinationPrototypeCidrBlockDataPrototype(
          type="cidr_block",
          name="allow-egress",
          cidr_block="10.0.0.0/24",
      )
      ```
  - **New prototype for Private Path service**:

      ```python
      from ibm_code_engine_sdk.code_engine_v2 import (
          AllowedOutboundDestinationPrototypePrivatePathServiceGatewayDataPrototype as PPSGProto
      )
      ppsg_proto = PPSGProto(
          type="private_path_service_gateway",
          name="pps-to-service-x",
          private_path_service_gateway_crn="<pps_gateway_crn>",
          isolation_policy="shared",  # optional: "shared" | "dedicated"
      )
      ```

- **Patch models changed (do not send `type`)**
  - Remove `type` from CIDR patch payloads; field and serialization removed:

    ```python
    from ibm_code_engine_sdk.code_engine_v2 import AllowedOutboundDestinationPatchCidrBlockDataPatch

    patch = AllowedOutboundDestinationPatchCidrBlockDataPatch(cidr_block="10.0.1.0/24")
    ```

  - New patch model for Private Path destinations:

    ```python
    from ibm_code_engine_sdk.code_engine_v2 import AllowedOutboundDestinationPatchPrivatePathServiceGatewayDataPatch

    pp_patch = AllowedOutboundDestinationPatchPrivatePathServiceGatewayDataPatch(
        isolation_policy="dedicated"  # "shared" | "dedicated"
    )
    ```

- **Probe model: `type` is now required**
  When constructing `Probe`, set the protocol explicitly:

  ```python
  from ibm_code_engine_sdk.code_engine_v2 import Probe

  # before (omitted `type`)
  # after (required)
  probe = Probe(
      type="http",  # "http" or "tcp"
      initial_delay=5,
      timeout=2,
  )
  ```

- **Secret model: `format` is now required**
  If you build `Secret` instances (e.g., in replace flows), you must set `format`:

  ```python
  from ibm_code_engine_sdk.code_engine_v2 import Secret

  secret = Secret(
      entity_tag=etag,
      format="generic",  # set the appropriate format value
      name="my-secret",
      data={"key": "value"},
  )
  ```

- **Previously-optional fields are now required in several response models (affects re-use of response as request)**
  These fields are validated as required in model deserialization; if you reuse response objects to send updates, you must provide them:

  - `App`: `computed_env_variables`, `run_service_account`, `run_volume_mounts`
  - `AppRevision`: `computed_env_variables`, `run_service_account`, `run_volume_mounts`
  - `Build`: `run_build_params`
  - `BuildRun`: `run_build_params`, `service_account`, `source_type`, `strategy_size`, `strategy_type`
  - `Function`: `computed_env_variables`
  - `FunctionRuntimeList`: `function_runtimes`
  - `Job`: `computed_env_variables`, `run_service_account`, `run_volume_mounts`
  - `JobRun`: `computed_env_variables`

  **Example (BuildRun)**

  ```python
  from ibm_code_engine_sdk.code_engine_v2 import BuildRun, BuildParam

  build_run = BuildRun(
      build_name="my-build",
      name="run-1",
      run_build_params=[BuildParam(name="ARG1", value="v")],
      service_account="default",
      source_type="git",
      strategy_size="small",
      strategy_type="buildpacks",
      source_url="https://github.com/org/repo",
  )
  ```

- **Allowed outbound destination CIDR model loosened & enriched**
  - `entity_tag` and `name` are no longer required at construction time; they may be absent in incoming JSON.
  - New status fields added (`status`, `status_details`). Update your parsing/logic if you inspect readiness.

- **New status details and helper models (if you consume detailed status)**
  - `AllowedOutboundStatusDetails` base plus:
    - `AllowedOutboundStatusDetailsPrivatePathServiceGatewayStatusDetails`
  - Helper models:
    - `EndpointGatewayDetails`
    - `PrivatePathServiceGatewayDetails`
      If you serialize/deserialize status detail trees, include these types.

- **Volume mount doc clarifications (no code changes)**
  - `read_only` description now explicitly applies to mounts of type `'persistent_data_store'`.
  - Name generation references `reference` (was `ref` in docstring).

- **Storage data enum expansion & doc update**
  - `StorageData`/`StorageDataObjectStorageData` now enumerate more `bucket_location` values (regional/zone shorthands). If you validate these values client-side, include the new options.
  - `StorageDataObjectStorageData` doc now specifies key/value constraints.

> **Migration checklist**
>
> - [ ] Rename `list_allowed_outbound_destination` → `list_allowed_outbound_destinations`.
> - [ ] Rename `list_persistent_data_store` → `list_persistent_data_stores`.
> - [ ] Switch pagers to pluralized classes.
> - [ ] Update API `version` upper bound if you set it.
> - [ ] For outbound destination **create**:
>   - [ ] Provide `name` in prototypes.
>   - [ ] For CIDR prototype, adjust constructor order to `(type, name, cidr_block)`.
>   - [ ] Use new Private Path prototype when needed.
> - [ ] For outbound destination **patch**: remove `type`; use CIDR/Private Path specific patch models.
> - [ ] Set required fields now enforced in models (`Probe.type`, `Secret.format`, and the required lists/fields in `App`, `Build`, `BuildRun`, `Function`, `Job`, `JobRun`, etc.).
> - [ ] Include handling for new enum values: `private_path_service_gateway`, `status` values (`ready|failed|deploying`), and `isolation_policy` (`shared|dedicated`).

## Installation

To install, use `pip` or `easy_install`:

```bash
pip install --upgrade "ibm_code_engine_sdk>=6.0.0"
```

or

```bash
easy_install --upgrade "ibm_code_engine_sdk>=6.0.0"
```

## Using the SDK
Examples and a demo are available in the [examples](/examples) folder.

For general SDK usage information, please see [this link](https://github.com/IBM/ibm-cloud-sdk-common/blob/main/README.md)

## Questions

If you are having difficulties using this SDK or have a question about the IBM Cloud services,
please ask a question
[Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-cloud).

## Issues
If you encounter an issue with the project, you are welcome to submit a
[bug report](https://github.com/IBM/code-engine-python-sdk/issues).
Before that, please search for similar issues. It's possible that someone has already reported the problem.

## Open source @ IBM
Find more open source projects on the [IBM Github Page](http://ibm.github.io/)

## Contributing
See [CONTRIBUTING.md](https://github.com/IBM/code-engine-python-sdk/blob/main/CONTRIBUTING.md).

## License

This SDK is released under the Apache 2.0 license.
The license's full text can be found in [LICENSE](https://github.com/IBM/code-engine-python-sdk/blob/main/LICENSE).

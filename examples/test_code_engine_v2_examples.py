# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2025.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Examples for CodeEngineV2
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from ibm_code_engine_sdk.code_engine_v2 import *

version = '2025-02-20'

#
# This file provides an example of how to use the Code Engine service.
#
# The following configuration properties are assumed to be defined:
# CODE_ENGINE_URL=<service base url>
# CODE_ENGINE_AUTH_TYPE=iam
# CODE_ENGINE_APIKEY=<IAM apikey>
# CODE_ENGINE_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'code_engine_v2.env'

code_engine_service = None

config = None


##############################################################################
# Start of Examples for Service: CodeEngineV2
##############################################################################
# region
class TestCodeEngineV2Examples:
    """
    Example Test Class for CodeEngineV2
    """

    @classmethod
    def setup_class(cls):
        global code_engine_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            code_engine_service = CodeEngineV2.new_instance()

            # end-common
            assert code_engine_service is not None

            # Load the configuration
            global config
            config = read_external_sources(CodeEngineV2.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_list_projects_example(self):
        """
        list_projects request example
        """
        try:
            print('\nlist_projects() result:')

            # begin-list_projects

            all_results = []
            pager = ProjectsPager(
                client=code_engine_service,
                limit=100,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_projects
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_project_example(self):
        """
        create_project request example
        """
        try:
            print('\ncreate_project() result:')

            # begin-create_project

            response = code_engine_service.create_project(
                name='my-project',
            )
            project = response.get_result()

            print(json.dumps(project, indent=2))

            # end-create_project

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_project_example(self):
        """
        get_project request example
        """
        try:
            print('\nget_project() result:')

            # begin-get_project

            response = code_engine_service.get_project(
                id='15314cc3-85b4-4338-903f-c28cdee6d005',
            )
            project = response.get_result()

            print(json.dumps(project, indent=2))

            # end-get_project

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_allowed_outbound_destination_example(self):
        """
        list_allowed_outbound_destination request example
        """
        try:
            print('\nlist_allowed_outbound_destination() result:')

            # begin-list_allowed_outbound_destination

            all_results = []
            pager = AllowedOutboundDestinationPager(
                client=code_engine_service,
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                limit=100,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_allowed_outbound_destination
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_allowed_outbound_destination_example(self):
        """
        create_allowed_outbound_destination request example
        """
        try:
            print('\ncreate_allowed_outbound_destination() result:')

            # begin-create_allowed_outbound_destination

            allowed_outbound_destination_prototype_model = {
                'type': 'cidr_block',
                'cidr_block': 'testString',
                'name': 'testString',
            }

            response = code_engine_service.create_allowed_outbound_destination(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                allowed_outbound_destination=allowed_outbound_destination_prototype_model,
            )
            allowed_outbound_destination = response.get_result()

            print(json.dumps(allowed_outbound_destination, indent=2))

            # end-create_allowed_outbound_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_allowed_outbound_destination_example(self):
        """
        get_allowed_outbound_destination request example
        """
        try:
            print('\nget_allowed_outbound_destination() result:')

            # begin-get_allowed_outbound_destination

            response = code_engine_service.get_allowed_outbound_destination(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-allowed-outbound-destination',
            )
            allowed_outbound_destination = response.get_result()

            print(json.dumps(allowed_outbound_destination, indent=2))

            # end-get_allowed_outbound_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_allowed_outbound_destination_example(self):
        """
        update_allowed_outbound_destination request example
        """
        try:
            print('\nupdate_allowed_outbound_destination() result:')

            # begin-update_allowed_outbound_destination

            allowed_outbound_destination_patch_model = {}

            response = code_engine_service.update_allowed_outbound_destination(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-allowed-outbound-destination',
                if_match='testString',
                allowed_outbound_destination=allowed_outbound_destination_patch_model,
            )
            allowed_outbound_destination = response.get_result()

            print(json.dumps(allowed_outbound_destination, indent=2))

            # end-update_allowed_outbound_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_project_egress_ips_example(self):
        """
        get_project_egress_ips request example
        """
        try:
            print('\nget_project_egress_ips() result:')

            # begin-get_project_egress_ips

            response = code_engine_service.get_project_egress_ips(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            )
            project_egress_ip_addresses = response.get_result()

            print(json.dumps(project_egress_ip_addresses, indent=2))

            # end-get_project_egress_ips

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_project_status_details_example(self):
        """
        get_project_status_details request example
        """
        try:
            print('\nget_project_status_details() result:')

            # begin-get_project_status_details

            response = code_engine_service.get_project_status_details(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            )
            project_status_details = response.get_result()

            print(json.dumps(project_status_details, indent=2))

            # end-get_project_status_details

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_apps_example(self):
        """
        list_apps request example
        """
        try:
            print('\nlist_apps() result:')

            # begin-list_apps

            all_results = []
            pager = AppsPager(
                client=code_engine_service,
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                limit=100,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_apps
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_app_example(self):
        """
        create_app request example
        """
        try:
            print('\ncreate_app() result:')

            # begin-create_app

            response = code_engine_service.create_app(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                image_reference='icr.io/codeengine/helloworld',
                name='my-app',
            )
            app = response.get_result()

            print(json.dumps(app, indent=2))

            # end-create_app

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_app_example(self):
        """
        get_app request example
        """
        try:
            print('\nget_app() result:')

            # begin-get_app

            response = code_engine_service.get_app(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-app',
            )
            app = response.get_result()

            print(json.dumps(app, indent=2))

            # end-get_app

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_app_example(self):
        """
        update_app request example
        """
        try:
            print('\nupdate_app() result:')

            # begin-update_app

            app_patch_model = {}

            response = code_engine_service.update_app(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-app',
                if_match='testString',
                app=app_patch_model,
            )
            app = response.get_result()

            print(json.dumps(app, indent=2))

            # end-update_app

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_app_revisions_example(self):
        """
        list_app_revisions request example
        """
        try:
            print('\nlist_app_revisions() result:')

            # begin-list_app_revisions

            all_results = []
            pager = AppRevisionsPager(
                client=code_engine_service,
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                app_name='my-app',
                limit=100,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_app_revisions
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_app_revision_example(self):
        """
        get_app_revision request example
        """
        try:
            print('\nget_app_revision() result:')

            # begin-get_app_revision

            response = code_engine_service.get_app_revision(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                app_name='my-app',
                name='my-app-00001',
            )
            app_revision = response.get_result()

            print(json.dumps(app_revision, indent=2))

            # end-get_app_revision

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_app_instances_example(self):
        """
        list_app_instances request example
        """
        try:
            print('\nlist_app_instances() result:')

            # begin-list_app_instances

            all_results = []
            pager = AppInstancesPager(
                client=code_engine_service,
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                app_name='my-app',
                limit=100,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_app_instances
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_jobs_example(self):
        """
        list_jobs request example
        """
        try:
            print('\nlist_jobs() result:')

            # begin-list_jobs

            all_results = []
            pager = JobsPager(
                client=code_engine_service,
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                limit=100,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_jobs
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_job_example(self):
        """
        create_job request example
        """
        try:
            print('\ncreate_job() result:')

            # begin-create_job

            response = code_engine_service.create_job(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                image_reference='icr.io/codeengine/helloworld',
                name='my-job',
            )
            job = response.get_result()

            print(json.dumps(job, indent=2))

            # end-create_job

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_job_example(self):
        """
        get_job request example
        """
        try:
            print('\nget_job() result:')

            # begin-get_job

            response = code_engine_service.get_job(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-job',
            )
            job = response.get_result()

            print(json.dumps(job, indent=2))

            # end-get_job

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_job_example(self):
        """
        update_job request example
        """
        try:
            print('\nupdate_job() result:')

            # begin-update_job

            job_patch_model = {}

            response = code_engine_service.update_job(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-job',
                if_match='testString',
                job=job_patch_model,
            )
            job = response.get_result()

            print(json.dumps(job, indent=2))

            # end-update_job

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_job_runs_example(self):
        """
        list_job_runs request example
        """
        try:
            print('\nlist_job_runs() result:')

            # begin-list_job_runs

            all_results = []
            pager = JobRunsPager(
                client=code_engine_service,
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                job_name='my-job',
                limit=100,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_job_runs
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_job_run_example(self):
        """
        create_job_run request example
        """
        try:
            print('\ncreate_job_run() result:')

            # begin-create_job_run

            response = code_engine_service.create_job_run(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            )
            job_run = response.get_result()

            print(json.dumps(job_run, indent=2))

            # end-create_job_run

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_job_run_example(self):
        """
        get_job_run request example
        """
        try:
            print('\nget_job_run() result:')

            # begin-get_job_run

            response = code_engine_service.get_job_run(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-job-run',
            )
            job_run = response.get_result()

            print(json.dumps(job_run, indent=2))

            # end-get_job_run

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_function_runtimes_example(self):
        """
        list_function_runtimes request example
        """
        try:
            print('\nlist_function_runtimes() result:')

            # begin-list_function_runtimes

            response = code_engine_service.list_function_runtimes()
            function_runtime_list = response.get_result()

            print(json.dumps(function_runtime_list, indent=2))

            # end-list_function_runtimes

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_functions_example(self):
        """
        list_functions request example
        """
        try:
            print('\nlist_functions() result:')

            # begin-list_functions

            all_results = []
            pager = FunctionsPager(
                client=code_engine_service,
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                limit=100,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_functions
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_function_example(self):
        """
        create_function request example
        """
        try:
            print('\ncreate_function() result:')

            # begin-create_function

            response = code_engine_service.create_function(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                code_reference='data:text/plain;base64,<base64encoded-source-code>',
                name='my-function',
                runtime='nodejs-18',
            )
            function = response.get_result()

            print(json.dumps(function, indent=2))

            # end-create_function

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_function_example(self):
        """
        get_function request example
        """
        try:
            print('\nget_function() result:')

            # begin-get_function

            response = code_engine_service.get_function(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-function',
            )
            function = response.get_result()

            print(json.dumps(function, indent=2))

            # end-get_function

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_function_example(self):
        """
        update_function request example
        """
        try:
            print('\nupdate_function() result:')

            # begin-update_function

            function_patch_model = {}

            response = code_engine_service.update_function(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-function',
                if_match='testString',
                function=function_patch_model,
            )
            function = response.get_result()

            print(json.dumps(function, indent=2))

            # end-update_function

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_bindings_example(self):
        """
        list_bindings request example
        """
        try:
            print('\nlist_bindings() result:')

            # begin-list_bindings

            all_results = []
            pager = BindingsPager(
                client=code_engine_service,
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                limit=100,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_bindings
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_binding_example(self):
        """
        create_binding request example
        """
        try:
            print('\ncreate_binding() result:')

            # begin-create_binding

            component_ref_model = {
                'name': 'my-app-1',
                'resource_type': 'app_v2',
            }

            response = code_engine_service.create_binding(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                component=component_ref_model,
                prefix='MY_COS',
                secret_name='my-service-access',
            )
            binding = response.get_result()

            print(json.dumps(binding, indent=2))

            # end-create_binding

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_binding_example(self):
        """
        get_binding request example
        """
        try:
            print('\nget_binding() result:')

            # begin-get_binding

            response = code_engine_service.get_binding(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                id='a172ced-b5f21bc-71ba50c-1638604',
            )
            binding = response.get_result()

            print(json.dumps(binding, indent=2))

            # end-get_binding

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_builds_example(self):
        """
        list_builds request example
        """
        try:
            print('\nlist_builds() result:')

            # begin-list_builds

            all_results = []
            pager = BuildsPager(
                client=code_engine_service,
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                limit=100,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_builds
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_build_example(self):
        """
        create_build request example
        """
        try:
            print('\ncreate_build() result:')

            # begin-create_build

            response = code_engine_service.create_build(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-build',
                output_image='private.de.icr.io/icr_namespace/image-name',
                output_secret='ce-auto-icr-private-eu-de',
                strategy_type='dockerfile',
            )
            build = response.get_result()

            print(json.dumps(build, indent=2))

            # end-create_build

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_build_example(self):
        """
        get_build request example
        """
        try:
            print('\nget_build() result:')

            # begin-get_build

            response = code_engine_service.get_build(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-build',
            )
            build = response.get_result()

            print(json.dumps(build, indent=2))

            # end-get_build

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_build_example(self):
        """
        update_build request example
        """
        try:
            print('\nupdate_build() result:')

            # begin-update_build

            build_patch_model = {}

            response = code_engine_service.update_build(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-build',
                if_match='testString',
                build=build_patch_model,
            )
            build = response.get_result()

            print(json.dumps(build, indent=2))

            # end-update_build

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_build_runs_example(self):
        """
        list_build_runs request example
        """
        try:
            print('\nlist_build_runs() result:')

            # begin-list_build_runs

            all_results = []
            pager = BuildRunsPager(
                client=code_engine_service,
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                build_name='my-build',
                limit=100,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_build_runs
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_build_run_example(self):
        """
        create_build_run request example
        """
        try:
            print('\ncreate_build_run() result:')

            # begin-create_build_run

            response = code_engine_service.create_build_run(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
            )
            build_run = response.get_result()

            print(json.dumps(build_run, indent=2))

            # end-create_build_run

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_build_run_example(self):
        """
        get_build_run request example
        """
        try:
            print('\nget_build_run() result:')

            # begin-get_build_run

            response = code_engine_service.get_build_run(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-build-run',
            )
            build_run = response.get_result()

            print(json.dumps(build_run, indent=2))

            # end-get_build_run

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_domain_mappings_example(self):
        """
        list_domain_mappings request example
        """
        try:
            print('\nlist_domain_mappings() result:')

            # begin-list_domain_mappings

            all_results = []
            pager = DomainMappingsPager(
                client=code_engine_service,
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                limit=100,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_domain_mappings
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_domain_mapping_example(self):
        """
        create_domain_mapping request example
        """
        try:
            print('\ncreate_domain_mapping() result:')

            # begin-create_domain_mapping

            component_ref_model = {
                'name': 'my-app-1',
                'resource_type': 'app_v2',
            }

            response = code_engine_service.create_domain_mapping(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                component=component_ref_model,
                name='www.example.com',
                tls_secret='my-tls-secret',
            )
            domain_mapping = response.get_result()

            print(json.dumps(domain_mapping, indent=2))

            # end-create_domain_mapping

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_domain_mapping_example(self):
        """
        get_domain_mapping request example
        """
        try:
            print('\nget_domain_mapping() result:')

            # begin-get_domain_mapping

            response = code_engine_service.get_domain_mapping(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='www.example.com',
            )
            domain_mapping = response.get_result()

            print(json.dumps(domain_mapping, indent=2))

            # end-get_domain_mapping

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_domain_mapping_example(self):
        """
        update_domain_mapping request example
        """
        try:
            print('\nupdate_domain_mapping() result:')

            # begin-update_domain_mapping

            domain_mapping_patch_model = {}

            response = code_engine_service.update_domain_mapping(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='www.example.com',
                if_match='testString',
                domain_mapping=domain_mapping_patch_model,
            )
            domain_mapping = response.get_result()

            print(json.dumps(domain_mapping, indent=2))

            # end-update_domain_mapping

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_config_maps_example(self):
        """
        list_config_maps request example
        """
        try:
            print('\nlist_config_maps() result:')

            # begin-list_config_maps

            all_results = []
            pager = ConfigMapsPager(
                client=code_engine_service,
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                limit=100,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_config_maps
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_config_map_example(self):
        """
        create_config_map request example
        """
        try:
            print('\ncreate_config_map() result:')

            # begin-create_config_map

            response = code_engine_service.create_config_map(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-config-map',
            )
            config_map = response.get_result()

            print(json.dumps(config_map, indent=2))

            # end-create_config_map

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_config_map_example(self):
        """
        get_config_map request example
        """
        try:
            print('\nget_config_map() result:')

            # begin-get_config_map

            response = code_engine_service.get_config_map(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-config-map',
            )
            config_map = response.get_result()

            print(json.dumps(config_map, indent=2))

            # end-get_config_map

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_config_map_example(self):
        """
        replace_config_map request example
        """
        try:
            print('\nreplace_config_map() result:')

            # begin-replace_config_map

            response = code_engine_service.replace_config_map(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-config-map',
                if_match='testString',
            )
            config_map = response.get_result()

            print(json.dumps(config_map, indent=2))

            # end-replace_config_map

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_secrets_example(self):
        """
        list_secrets request example
        """
        try:
            print('\nlist_secrets() result:')

            # begin-list_secrets

            all_results = []
            pager = SecretsPager(
                client=code_engine_service,
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                format='ssh_auth',
                limit=100,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_secrets
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_secret_example(self):
        """
        create_secret request example
        """
        try:
            print('\ncreate_secret() result:')

            # begin-create_secret

            response = code_engine_service.create_secret(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                format='generic',
                name='my-secret',
            )
            secret = response.get_result()

            print(json.dumps(secret, indent=2))

            # end-create_secret

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_secret_example(self):
        """
        get_secret request example
        """
        try:
            print('\nget_secret() result:')

            # begin-get_secret

            response = code_engine_service.get_secret(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-secret',
            )
            secret = response.get_result()

            print(json.dumps(secret, indent=2))

            # end-get_secret

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_secret_example(self):
        """
        replace_secret request example
        """
        try:
            print('\nreplace_secret() result:')

            # begin-replace_secret

            response = code_engine_service.replace_secret(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-secret',
                if_match='testString',
                format='generic',
            )
            secret = response.get_result()

            print(json.dumps(secret, indent=2))

            # end-replace_secret

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_project_example(self):
        """
        delete_project request example
        """
        try:
            # begin-delete_project

            response = code_engine_service.delete_project(
                id='15314cc3-85b4-4338-903f-c28cdee6d005',
            )

            # end-delete_project
            print('\ndelete_project() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_allowed_outbound_destination_example(self):
        """
        delete_allowed_outbound_destination request example
        """
        try:
            # begin-delete_allowed_outbound_destination

            response = code_engine_service.delete_allowed_outbound_destination(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-allowed-outbound-destination',
            )

            # end-delete_allowed_outbound_destination
            print('\ndelete_allowed_outbound_destination() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_app_example(self):
        """
        delete_app request example
        """
        try:
            # begin-delete_app

            response = code_engine_service.delete_app(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-app',
            )

            # end-delete_app
            print('\ndelete_app() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_app_revision_example(self):
        """
        delete_app_revision request example
        """
        try:
            # begin-delete_app_revision

            response = code_engine_service.delete_app_revision(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                app_name='my-app',
                name='my-app-00001',
            )

            # end-delete_app_revision
            print('\ndelete_app_revision() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_job_example(self):
        """
        delete_job request example
        """
        try:
            # begin-delete_job

            response = code_engine_service.delete_job(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-job',
            )

            # end-delete_job
            print('\ndelete_job() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_job_run_example(self):
        """
        delete_job_run request example
        """
        try:
            # begin-delete_job_run

            response = code_engine_service.delete_job_run(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-job-run',
            )

            # end-delete_job_run
            print('\ndelete_job_run() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_function_example(self):
        """
        delete_function request example
        """
        try:
            # begin-delete_function

            response = code_engine_service.delete_function(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-function',
            )

            # end-delete_function
            print('\ndelete_function() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_binding_example(self):
        """
        delete_binding request example
        """
        try:
            # begin-delete_binding

            response = code_engine_service.delete_binding(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                id='a172ced-b5f21bc-71ba50c-1638604',
            )

            # end-delete_binding
            print('\ndelete_binding() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_build_example(self):
        """
        delete_build request example
        """
        try:
            # begin-delete_build

            response = code_engine_service.delete_build(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-build',
            )

            # end-delete_build
            print('\ndelete_build() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_build_run_example(self):
        """
        delete_build_run request example
        """
        try:
            # begin-delete_build_run

            response = code_engine_service.delete_build_run(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-build-run',
            )

            # end-delete_build_run
            print('\ndelete_build_run() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_domain_mapping_example(self):
        """
        delete_domain_mapping request example
        """
        try:
            # begin-delete_domain_mapping

            response = code_engine_service.delete_domain_mapping(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='www.example.com',
            )

            # end-delete_domain_mapping
            print('\ndelete_domain_mapping() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_config_map_example(self):
        """
        delete_config_map request example
        """
        try:
            # begin-delete_config_map

            response = code_engine_service.delete_config_map(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-config-map',
            )

            # end-delete_config_map
            print('\ndelete_config_map() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_secret_example(self):
        """
        delete_secret request example
        """
        try:
            # begin-delete_secret

            response = code_engine_service.delete_secret(
                project_id='15314cc3-85b4-4338-903f-c28cdee6d005',
                name='my-secret',
            )

            # end-delete_secret
            print('\ndelete_secret() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: CodeEngineV2
##############################################################################

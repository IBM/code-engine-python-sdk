# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2023.
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
Integration Tests for CodeEngineV2
"""

import time
from ibm_cloud_sdk_core import *
import os
import pytest
from ibm_code_engine_sdk.code_engine_v2 import *

# Config file name
config_file = 'code_engine_v2.env'


class TestCodeEngineV2:
    """
    Integration Test Class for CodeEngineV2
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.code_engine_service = CodeEngineV2.new_instance()
            assert cls.code_engine_service is not None

            cls.config = read_external_sources(CodeEngineV2.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.code_engine_service.enable_retries(max_retries=0, retry_interval=10)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_list_projects(self):
        response = self.code_engine_service.list_projects(
            limit=100,
        )

        assert response.get_status_code() == 200
        project_list = response.get_result()
        assert project_list is not None

    @needscredentials
    def test_list_projects_with_pager(self):
        all_results = []

        # Test get_next().
        pager = ProjectsPager(
            client=self.code_engine_service,
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = ProjectsPager(
            client=self.code_engine_service,
            limit=100,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_projects() returned a total of {len(all_results)} items(s) using ProjectsPager.')

    @needscredentials
    def test_create_project(self):
        response = self.code_engine_service.create_project(
            name=f'sdk-e2e-python-{int(time.time())}',
            tags=['testString'],
        )

        assert response.get_status_code() == 202
        project = response.get_result()
        assert project is not None

        # store the id of the project in the pytest context to be able to share it acress tests
        pytest.e2e_test_project_id = project['id']
        print(f'\nCreated project {pytest.e2e_test_project_id}')

    @needscredentials
    def test_get_project(self):
        time.sleep(120)
        response = self.code_engine_service.get_project(
            id=pytest.e2e_test_project_id,
        )

        assert response.get_status_code() == 200
        project = response.get_result()
        assert project is not None

        # Assume that the project creation takes some time
        i = 0
        obtained_project = []
        while i < 30:
            time.sleep(15)
            proj_res = self.code_engine_service.get_project(
                id=pytest.e2e_test_project_id,
            )
            obtained_project = proj_res.get_result()
            proj_name = obtained_project['name']
            proj_id = obtained_project['id']
            proj_status = obtained_project['status']
            print(f'\nObtained status of project {proj_name} (guid: {proj_id}): {proj_status}.')
            if proj_status == 'active':
                break

            i += 1

        assert obtained_project['status'] == 'active'

    @needscredentials
    def test_get_project_egress_ips(self):
        response = self.code_engine_service.get_project_egress_ips(
            project_id=pytest.e2e_test_project_id,
        )

        assert response.get_status_code() == 200
        project_egress_ip_addresses = response.get_result()
        assert project_egress_ip_addresses is not None

    @needscredentials
    def test_list_apps(self):
        response = self.code_engine_service.list_apps(
            project_id=pytest.e2e_test_project_id,
            limit=100,
        )

        assert response.get_status_code() == 200
        app_list = response.get_result()
        assert app_list is not None

    @needscredentials
    def test_list_apps_with_pager(self):
        all_results = []

        # Test get_next().
        pager = AppsPager(
            client=self.code_engine_service,
            project_id=pytest.e2e_test_project_id,
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = AppsPager(
            client=self.code_engine_service,
            project_id=pytest.e2e_test_project_id,
            limit=100,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_apps() returned a total of {len(all_results)} items(s) using AppsPager.')

    @needscredentials
    def test_create_app(self):
        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {
            'key': 'MY_VARIABLE',
            'name': 'SOME',
            'prefix': 'PREFIX_',
            'reference': 'my-secret',
            'type': 'literal',
            'value': 'VALUE',
        }

        # Construct a dict representation of a VolumeMountPrototype model
        volume_mount_prototype_model = {
            'mount_path': '/app',
            'name': 'codeengine-mount-b69u90',
            'reference': 'my-secret',
            'type': 'secret',
        }

        response = self.code_engine_service.create_app(
            project_id=pytest.e2e_test_project_id,
            image_reference='icr.io/codeengine/helloworld',
            name='my-app',
            image_port=8080,
            image_secret='my-secret',
            managed_domain_mappings='local_public',
            run_arguments=['testString'],
            run_as_user=1001,
            run_commands=['testString'],
            run_env_variables=[env_var_prototype_model],
            run_service_account='default',
            run_volume_mounts=[volume_mount_prototype_model],
            scale_concurrency=100,
            scale_concurrency_target=80,
            scale_cpu_limit='1',
            scale_ephemeral_storage_limit='4G',
            scale_initial_instances=1,
            scale_max_instances=10,
            scale_memory_limit='4G',
            scale_min_instances=0,
            scale_request_timeout=300,
        )

        assert response.get_status_code() == 201
        app = response.get_result()
        assert app is not None

    @needscredentials
    def test_get_app(self):
        response = self.code_engine_service.get_app(
            project_id=pytest.e2e_test_project_id,
            name='my-app',
        )

        assert response.get_status_code() == 200
        app = response.get_result()
        assert app is not None

    @needscredentials
    def test_update_app(self):
        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {
            'key': 'MY_VARIABLE',
            'name': 'SOME',
            'prefix': 'PREFIX_',
            'reference': 'my-secret',
            'type': 'literal',
            'value': 'VALUE',
        }

        # Construct a dict representation of a VolumeMountPrototype model
        volume_mount_prototype_model = {
            'mount_path': '/app',
            'name': 'codeengine-mount-b69u90',
            'reference': 'my-secret',
            'type': 'secret',
        }

        # Construct a dict representation of a AppPatch model
        app_patch_model = {
            'image_port': 8080,
            'image_reference': 'icr.io/codeengine/helloworld',
            'image_secret': 'my-secret',
            'managed_domain_mappings': 'local_public',
            'run_arguments': ['testString'],
            'run_as_user': 1001,
            'run_commands': ['testString'],
            'run_env_variables': [env_var_prototype_model],
            'run_service_account': 'default',
            'run_volume_mounts': [volume_mount_prototype_model],
            'scale_concurrency': 100,
            'scale_concurrency_target': 80,
            'scale_cpu_limit': '1',
            'scale_ephemeral_storage_limit': '4G',
            'scale_initial_instances': 1,
            'scale_max_instances': 10,
            'scale_memory_limit': '4G',
            'scale_min_instances': 0,
            'scale_request_timeout': 300,
        }

        response = self.code_engine_service.update_app(
            project_id=pytest.e2e_test_project_id,
            name='my-app',
            if_match='*',
            app=app_patch_model,
        )

        assert response.get_status_code() == 200
        app = response.get_result()
        assert app is not None

    @needscredentials
    def test_list_app_revisions(self):
        response = self.code_engine_service.list_app_revisions(
            project_id=pytest.e2e_test_project_id,
            app_name='my-app',
            limit=100,
        )

        assert response.get_status_code() == 200
        app_revision_list = response.get_result()
        assert app_revision_list is not None

    @needscredentials
    def test_list_app_revisions_with_pager(self):
        all_results = []

        # Test get_next().
        pager = AppRevisionsPager(
            client=self.code_engine_service,
            project_id=pytest.e2e_test_project_id,
            app_name='my-app',
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = AppRevisionsPager(
            client=self.code_engine_service,
            project_id=pytest.e2e_test_project_id,
            app_name='my-app',
            limit=100,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_app_revisions() returned a total of {len(all_results)} items(s) using AppRevisionsPager.')

    @needscredentials
    def test_get_app_revision(self):
        response = self.code_engine_service.get_app_revision(
            project_id=pytest.e2e_test_project_id,
            app_name='my-app',
            name='my-app-00001',
        )

        assert response.get_status_code() == 200
        app_revision = response.get_result()
        assert app_revision is not None

    @needscredentials
    def test_list_jobs(self):
        response = self.code_engine_service.list_jobs(
            project_id=pytest.e2e_test_project_id,
            limit=100,
        )

        assert response.get_status_code() == 200
        job_list = response.get_result()
        assert job_list is not None

    @needscredentials
    def test_list_jobs_with_pager(self):
        all_results = []

        # Test get_next().
        pager = JobsPager(
            client=self.code_engine_service,
            project_id=pytest.e2e_test_project_id,
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = JobsPager(
            client=self.code_engine_service,
            project_id=pytest.e2e_test_project_id,
            limit=100,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_jobs() returned a total of {len(all_results)} items(s) using JobsPager.')

    @needscredentials
    def test_create_job(self):
        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {
            'key': 'MY_VARIABLE',
            'name': 'SOME',
            'prefix': 'PREFIX_',
            'reference': 'my-secret',
            'type': 'literal',
            'value': 'VALUE',
        }

        # Construct a dict representation of a VolumeMountPrototype model
        volume_mount_prototype_model = {
            'mount_path': '/app',
            'name': 'codeengine-mount-b69u90',
            'reference': 'my-secret',
            'type': 'secret',
        }

        response = self.code_engine_service.create_job(
            project_id=pytest.e2e_test_project_id,
            image_reference='icr.io/codeengine/helloworld',
            name='my-job',
            image_secret='my-secret',
            run_arguments=['testString'],
            run_as_user=1001,
            run_commands=['testString'],
            run_env_variables=[env_var_prototype_model],
            run_mode='task',
            run_service_account='default',
            run_volume_mounts=[volume_mount_prototype_model],
            scale_array_spec='1-5,7-8,10',
            scale_cpu_limit='1',
            scale_ephemeral_storage_limit='4G',
            scale_max_execution_time=7200,
            scale_memory_limit='4G',
            scale_retry_limit=3,
        )

        assert response.get_status_code() == 201
        job = response.get_result()
        assert job is not None

    @needscredentials
    def test_get_job(self):
        response = self.code_engine_service.get_job(
            project_id=pytest.e2e_test_project_id,
            name='my-job',
        )

        assert response.get_status_code() == 200
        job = response.get_result()
        assert job is not None

    @needscredentials
    def test_update_job(self):
        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {
            'key': 'MY_VARIABLE',
            'name': 'SOME',
            'prefix': 'PREFIX_',
            'reference': 'my-secret',
            'type': 'literal',
            'value': 'VALUE',
        }

        # Construct a dict representation of a VolumeMountPrototype model
        volume_mount_prototype_model = {
            'mount_path': '/app',
            'name': 'codeengine-mount-b69u90',
            'reference': 'my-secret',
            'type': 'secret',
        }

        # Construct a dict representation of a JobPatch model
        job_patch_model = {
            'image_reference': 'icr.io/codeengine/helloworld',
            'image_secret': 'my-secret',
            'run_arguments': ['testString'],
            'run_as_user': 1001,
            'run_commands': ['testString'],
            'run_env_variables': [env_var_prototype_model],
            'run_mode': 'task',
            'run_service_account': 'default',
            'run_volume_mounts': [volume_mount_prototype_model],
            'scale_array_spec': '1-5,7-8,10',
            'scale_cpu_limit': '1',
            'scale_ephemeral_storage_limit': '4G',
            'scale_max_execution_time': 7200,
            'scale_memory_limit': '4G',
            'scale_retry_limit': 3,
        }

        response = self.code_engine_service.update_job(
            project_id=pytest.e2e_test_project_id,
            name='my-job',
            if_match='*',
            job=job_patch_model,
        )

        assert response.get_status_code() == 200
        job = response.get_result()
        assert job is not None

    @needscredentials
    def test_list_job_runs(self):
        response = self.code_engine_service.list_job_runs(
            project_id=pytest.e2e_test_project_id,
            job_name='my-job',
            limit=100,
        )

        assert response.get_status_code() == 200
        job_run_list = response.get_result()
        assert job_run_list is not None

    @needscredentials
    def test_list_job_runs_with_pager(self):
        all_results = []

        # Test get_next().
        pager = JobRunsPager(
            client=self.code_engine_service,
            project_id=pytest.e2e_test_project_id,
            job_name='my-job',
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = JobRunsPager(
            client=self.code_engine_service,
            project_id=pytest.e2e_test_project_id,
            job_name='my-job',
            limit=100,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_job_runs() returned a total of {len(all_results)} items(s) using JobRunsPager.')

    @needscredentials
    def test_create_job_run(self):
        # Construct a dict representation of a EnvVarPrototype model
        env_var_prototype_model = {
            'key': 'MY_VARIABLE',
            'name': 'SOME',
            'prefix': 'PREFIX_',
            'reference': 'my-secret',
            'type': 'literal',
            'value': 'VALUE',
        }

        # Construct a dict representation of a VolumeMountPrototype model
        volume_mount_prototype_model = {
            'mount_path': '/app',
            'name': 'codeengine-mount-b69u90',
            'reference': 'my-secret',
            'type': 'secret',
        }

        response = self.code_engine_service.create_job_run(
            project_id=pytest.e2e_test_project_id,
            image_reference='icr.io/codeengine/helloworld',
            job_name='my-job',
            name='my-job-run',
            run_arguments=['testString'],
            run_as_user=1001,
            run_commands=['testString'],
            run_env_variables=[env_var_prototype_model],
            run_mode='task',
            run_volume_mounts=[volume_mount_prototype_model],
            scale_array_spec='1-5,7-8,10',
            scale_cpu_limit='1',
            scale_ephemeral_storage_limit='4G',
            scale_max_execution_time=7200,
            scale_memory_limit='4G',
            scale_retry_limit=3,
        )

        assert response.get_status_code() == 202
        job_run = response.get_result()
        assert job_run is not None

    @needscredentials
    def test_get_job_run(self):
        response = self.code_engine_service.get_job_run(
            project_id=pytest.e2e_test_project_id,
            name='my-job-run',
        )

        assert response.get_status_code() == 200
        job_run = response.get_result()
        assert job_run is not None

    @needscredentials
    def test_list_builds(self):
        response = self.code_engine_service.list_builds(
            project_id=pytest.e2e_test_project_id,
            limit=100,
        )

        assert response.get_status_code() == 200
        build_list = response.get_result()
        assert build_list is not None

    @needscredentials
    def test_list_builds_with_pager(self):
        all_results = []

        # Test get_next().
        pager = BuildsPager(
            client=self.code_engine_service,
            project_id=pytest.e2e_test_project_id,
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = BuildsPager(
            client=self.code_engine_service,
            project_id=pytest.e2e_test_project_id,
            limit=100,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_builds() returned a total of {len(all_results)} items(s) using BuildsPager.')

    @needscredentials
    def test_create_build(self):
        build_param_prototype_model = {
            'name': 'SOME',
            'type': 'literal',
            'value': 'VALUE',
        }

        response = self.code_engine_service.create_build(
            project_id=pytest.e2e_test_project_id,
            name='my-build',
            run_build_params=[build_param_prototype_model],
            output_image='private.de.icr.io/icr_namespace/image-name',
            output_secret='ce-auto-icr-private-eu-de',
            source_url='https://github.com/IBM/CodeEngine',
            strategy_type='dockerfile',
            source_context_dir='some/subfolder',
            source_revision='main',
            source_secret='my-secret',
            source_type='git',
            strategy_size='medium',
            strategy_spec_file='Dockerfile',
            timeout=600,
        )

        assert response.get_status_code() == 201
        build = response.get_result()
        assert build is not None

    @needscredentials
    def test_get_build(self):
        response = self.code_engine_service.get_build(
            project_id=pytest.e2e_test_project_id,
            name='my-build',
        )

        assert response.get_status_code() == 200
        build = response.get_result()
        assert build is not None

    @needscredentials
    def test_update_build(self):
        build_param_prototype_model = {
            'name': 'ANOTHER',
            'type': 'literal',
            'value': 'ANOTHER_VALUE',
        }

        # Construct a dict representation of a BuildPatch model
        build_patch_model = {
            'run_build_params': [build_param_prototype_model],
            'output_image': 'private.de.icr.io/icr_namespace/image-name',
            'output_secret': 'ce-auto-icr-private-eu-de',
            'source_context_dir': 'some/subfolder',
            'source_revision': 'main',
            'source_secret': 'my-secret',
            'source_type': 'git',
            'source_url': 'https://github.com/IBM/CodeEngine',
            'strategy_size': 'medium',
            'strategy_spec_file': 'Dockerfile',
            'strategy_type': 'dockerfile',
            'timeout': 600,
        }

        response = self.code_engine_service.update_build(
            project_id=pytest.e2e_test_project_id,
            name='my-build',
            if_match='*',
            build=build_patch_model,
        )

        assert response.get_status_code() == 200
        build = response.get_result()
        assert build is not None

    @needscredentials
    def test_list_build_runs(self):
        response = self.code_engine_service.list_build_runs(
            project_id=pytest.e2e_test_project_id,
            build_name='my-build',
            limit=100,
        )

        assert response.get_status_code() == 200
        build_run_list = response.get_result()
        assert build_run_list is not None

    @needscredentials
    def test_list_build_runs_with_pager(self):
        all_results = []

        # Test get_next().
        pager = BuildRunsPager(
            client=self.code_engine_service,
            project_id=pytest.e2e_test_project_id,
            build_name='my-build',
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = BuildRunsPager(
            client=self.code_engine_service,
            project_id=pytest.e2e_test_project_id,
            build_name='my-build',
            limit=100,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_build_runs() returned a total of {len(all_results)} items(s) using BuildRunsPager.')

    @needscredentials
    def test_create_build_run(self):
        build_param_prototype_model = {
            'name': 'SOME',
            'type': 'literal',
            'value': 'VALUE',
        }

        response = self.code_engine_service.create_build_run(
            project_id=pytest.e2e_test_project_id,
            build_name='my-build',
            name='my-build-run',
            run_build_params=[build_param_prototype_model],
            output_image='private.de.icr.io/icr_namespace/image-name',
            output_secret='ce-auto-icr-private-eu-de',
            service_account='default',
            source_context_dir='some/subfolder',
            source_revision='main',
            source_secret='my-secret',
            source_type='git',
            source_url='https://github.com/IBM/CodeEngine',
            strategy_size='medium',
            strategy_spec_file='Dockerfile',
            strategy_type='dockerfile',
            timeout=600,
        )

        assert response.get_status_code() == 202
        build_run = response.get_result()
        assert build_run is not None

    @needscredentials
    def test_get_build_run(self):
        response = self.code_engine_service.get_build_run(
            project_id=pytest.e2e_test_project_id,
            name='my-build-run',
        )

        assert response.get_status_code() == 200
        build_run = response.get_result()
        assert build_run is not None

    @needscredentials
    def test_list_config_maps(self):
        response = self.code_engine_service.list_config_maps(
            project_id=pytest.e2e_test_project_id,
            limit=100,
        )

        assert response.get_status_code() == 200
        config_map_list = response.get_result()
        assert config_map_list is not None

    @needscredentials
    def test_list_config_maps_with_pager(self):
        all_results = []

        # Test get_next().
        pager = ConfigMapsPager(
            client=self.code_engine_service,
            project_id=pytest.e2e_test_project_id,
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = ConfigMapsPager(
            client=self.code_engine_service,
            project_id=pytest.e2e_test_project_id,
            limit=100,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_config_maps() returned a total of {len(all_results)} items(s) using ConfigMapsPager.')

    @needscredentials
    def test_create_config_map(self):
        response = self.code_engine_service.create_config_map(
            project_id=pytest.e2e_test_project_id,
            name='my-config-map',
            data={'key1': 'testString'},
        )

        assert response.get_status_code() == 201
        config_map = response.get_result()
        assert config_map is not None

    @needscredentials
    def test_get_config_map(self):
        response = self.code_engine_service.get_config_map(
            project_id=pytest.e2e_test_project_id,
            name='my-config-map',
        )

        assert response.get_status_code() == 200
        config_map = response.get_result()
        assert config_map is not None

    @needscredentials
    def test_replace_config_map(self):
        response = self.code_engine_service.replace_config_map(
            project_id=pytest.e2e_test_project_id,
            name='my-config-map',
            if_match='*',
            data={'key1': 'testString'},
        )

        assert response.get_status_code() == 200
        config_map = response.get_result()
        assert config_map is not None

    @needscredentials
    def test_list_secrets(self):
        response = self.code_engine_service.list_secrets(
            project_id=pytest.e2e_test_project_id,
            limit=100,
        )

        assert response.get_status_code() == 200
        secret_list = response.get_result()
        assert secret_list is not None

    @needscredentials
    def test_list_secrets_with_pager(self):
        all_results = []

        # Test get_next().
        pager = SecretsPager(
            client=self.code_engine_service,
            project_id=pytest.e2e_test_project_id,
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = SecretsPager(
            client=self.code_engine_service,
            project_id=pytest.e2e_test_project_id,
            limit=100,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_secrets() returned a total of {len(all_results)} items(s) using SecretsPager.')

    @needscredentials
    def test_create_secret(self):
        response = self.code_engine_service.create_secret(
            project_id=pytest.e2e_test_project_id,
            format='generic',
            name='my-secret',
            data={'key1': 'testString'},
        )

        assert response.get_status_code() == 201
        secret = response.get_result()
        assert secret is not None

    @needscredentials
    def test_create_ssh_secret(self):
        file = open("test/integration/sshkey.pem", "r")
        sshKeyContent = file.read()
        file.close()
        response = self.code_engine_service.create_secret(
            project_id=pytest.e2e_test_project_id,
            format='ssh_auth',
            name='my-ssh-secret',
            data={'ssh_key': sshKeyContent},
        )

        assert response.get_status_code() == 201
        secret = response.get_result()
        assert secret is not None

    @needscredentials
    def test_create_tls_secret(self):
        tlsKeyFilePath = self.config.get('TLS_KEY_FILE_PATH')
        assert tlsKeyFilePath is not None
        tlsCertFilePath = self.config.get('TLS_CERT_FILE_PATH')
        assert tlsCertFilePath is not None

        tlsKeyFile = open(tlsKeyFilePath, "r")
        tlsKeyContent = tlsKeyFile.read()
        tlsKeyFile.close()
        tlsCertFile = open(tlsCertFilePath, "r")
        tlsCertContent = tlsCertFile.read()
        tlsCertFile.close()
        response = self.code_engine_service.create_secret(
            project_id=pytest.e2e_test_project_id,
            format='tls',
            name='my-tls-secret',
            data={
                'tls_key': tlsKeyContent,
                'tls_cert': tlsCertContent,
            },
        )

        assert response.get_status_code() == 201
        secret = response.get_result()
        assert secret is not None

    @needscredentials
    def test_create_domain_mapping(self):
        # store the domainMappingName in the pytest context to be able to share it across tests
        pytest.e2e_test_domain_mapping_name = self.config.get('DOMAIN_MAPPING_NAME')

        component_ref_model = {
            'name': 'my-app',
            'resource_type': 'app_v2',
        }
        response = self.code_engine_service.create_domain_mapping(
            project_id=pytest.e2e_test_project_id,
            component=component_ref_model,
            name=pytest.e2e_test_domain_mapping_name,
            tls_secret='my-tls-secret',
        )
        assert response.get_status_code() == 201
        domain_mapping = response.get_result()
        assert domain_mapping is not None

    @needscredentials
    def test_get_domain_mapping(self):
        response = self.code_engine_service.get_domain_mapping(
            project_id=pytest.e2e_test_project_id,
            name=pytest.e2e_test_domain_mapping_name,
        )
        assert response.get_status_code() == 200
        domain_mapping = response.get_result()
        assert domain_mapping is not None

    @needscredentials
    def test_create_app_2(self):
        response = self.code_engine_service.create_app(
            project_id=pytest.e2e_test_project_id,
            image_reference='icr.io/codeengine/helloworld',
            name='my-app-2',
        )

        assert response.get_status_code() == 201
        app = response.get_result()
        assert app is not None

    @needscredentials
    def test_update_domain_mapping(self):
        component_ref_model = {
            'name': 'my-app-2',
            'resource_type': 'app_v2',
        }
        domain_mapping_patch_model = {
            'name': component_ref_model,
        }
        response = self.code_engine_service.update_domain_mapping(
            project_id=pytest.e2e_test_project_id,
            name=pytest.e2e_test_domain_mapping_name,
            if_match='*',
            domain_mapping=domain_mapping_patch_model,
        )

        assert response.get_status_code() == 200
        domain_mapping = response.get_result()
        assert domain_mapping is not None

    @needscredentials
    def test_delete_domain_mapping_example(self):
        response = self.code_engine_service.delete_domain_mapping(
            project_id=pytest.e2e_test_project_id,
            name=pytest.e2e_test_domain_mapping_name,
        )

        assert response.get_status_code() == 202

    @needscredentials
    def test_create_basic_auth_secret(self):
        response = self.code_engine_service.create_secret(
            project_id=pytest.e2e_test_project_id,
            format='basic_auth',
            name='my-basic-auth-secret',
            data={'username': 'user1', 'password': 'pass1'},
        )

        assert response.get_status_code() == 201
        secret = response.get_result()
        assert secret is not None

    @needscredentials
    def test_create_hmac_auth_secret(self):
        # store the hmac credentials in the pytest context to be able to share it across tests
        pytest.e2e_test_access_key_id = os.environ['COS_ACCESS_KEY_ID']
        pytest.e2e_test_secret_access_key = os.environ['COS_SECRET_ACCESS_KEY']

        response = self.code_engine_service.create_secret(
            project_id=pytest.e2e_test_project_id,
            format='hmac_auth',
            name='ce-api-int-test-hmac-secret',
            data={
                'access_key_id': pytest.e2e_test_access_key_id,
                'secret_access_key': pytest.e2e_test_secret_access_key,
            },
        )

        assert response.get_status_code() == 201
        secret = response.get_result()
        assert secret is not None

    @needscredentials
    def test_create_registry_secret(self):
        response = self.code_engine_service.create_secret(
            project_id=pytest.e2e_test_project_id,
            format='registry',
            name='my-registry-secret',
            data={'username': 'user1', 'password': 'pass1', 'server': 'github.com', 'email': 'myemail@email.com'},
        )

        assert response.get_status_code() == 201
        secret = response.get_result()
        assert secret is not None

    @needscredentials
    def test_get_secret(self):
        response = self.code_engine_service.get_secret(
            project_id=pytest.e2e_test_project_id,
            name='my-secret',
        )

        assert response.get_status_code() == 200
        secret = response.get_result()
        assert secret is not None

    @needscredentials
    def test_get_ssh_secret(self):
        response = self.code_engine_service.get_secret(
            project_id=pytest.e2e_test_project_id,
            name='my-ssh-secret',
        )

        assert response.get_status_code() == 200
        secret = response.get_result()
        assert secret is not None

    @needscredentials
    def test_get_tls_secret(self):
        response = self.code_engine_service.get_secret(
            project_id=pytest.e2e_test_project_id,
            name='my-tls-secret',
        )

        assert response.get_status_code() == 200
        secret = response.get_result()
        assert secret is not None

    @needscredentials
    def test_get_basic_auth_secret(self):
        response = self.code_engine_service.get_secret(
            project_id=pytest.e2e_test_project_id,
            name='my-basic-auth-secret',
        )

        assert response.get_status_code() == 200
        secret = response.get_result()
        assert secret is not None

    @needscredentials
    def test_get_hmac_auth_secret(self):
        response = self.code_engine_service.get_secret(
            project_id=pytest.e2e_test_project_id,
            name='ce-api-int-test-hmac-secret',
        )

        assert response.get_status_code() == 200
        secret = response.get_result()
        assert secret is not None

    @needscredentials
    def test_get_registry_secret(self):
        response = self.code_engine_service.get_secret(
            project_id=pytest.e2e_test_project_id,
            name='my-registry-secret',
        )

        assert response.get_status_code() == 200
        secret = response.get_result()
        assert secret is not None

    @needscredentials
    def test_replace_secret(self):
        response = self.code_engine_service.replace_secret(
            project_id=pytest.e2e_test_project_id,
            name='my-secret',
            if_match='*',
            data={'key1': 'testString'},
            format='generic',
        )

        assert response.get_status_code() == 200
        secret = response.get_result()
        assert secret is not None

    @needscredentials
    def test_replace_ssh_secret(self):
        file = open("test/integration/sshkey.pem", "r")
        sshKeyContent = file.read()
        file.close()
        response = self.code_engine_service.replace_secret(
            project_id=pytest.e2e_test_project_id,
            name='my-ssh-secret',
            if_match='*',
            data={'ssh_key': sshKeyContent},
            format='ssh_auth',
        )

        assert response.get_status_code() == 200
        secret = response.get_result()
        assert secret is not None

    @needscredentials
    def test_replace_tls_secret(self):
        tlsKeyFile = open("test/integration/domain.key", "r")
        tlsKeyContent = tlsKeyFile.read()
        tlsKeyFile.close()
        tlsCertFile = open("test/integration/domain.crt", "r")
        tlsCertContent = tlsCertFile.read()
        tlsCertFile.close()
        response = self.code_engine_service.replace_secret(
            project_id=pytest.e2e_test_project_id,
            name='my-tls-secret',
            if_match='*',
            data={
                'tls_key': tlsKeyContent,
                'tls_cert': tlsCertContent,
            },
            format='tls',
        )

        assert response.get_status_code() == 200
        secret = response.get_result()
        assert secret is not None

    @needscredentials
    def test_replace_basic_auth_secret(self):
        response = self.code_engine_service.replace_secret(
            project_id=pytest.e2e_test_project_id,
            name='my-basic-auth-secret',
            if_match='*',
            data={'username': 'user2', 'password': 'pass2'},
            format='basic_auth',
        )

        assert response.get_status_code() == 200
        secret = response.get_result()
        assert secret is not None

    @needscredentials
    def test_create_persistent_data_store(self):
        response = self.code_engine_service.create_persistent_data_store(
            project_id=pytest.e2e_test_project_id,
            storage_type='object_storage',
            name='my-persistent-data-store',
            data={
                'bucket_location': 'eu-de',
                'bucket_name': 'e2e-api-bucket-eu-de',
                'secret_name': 'ce-api-int-test-hmac-secret',
            },
        )

        assert response.get_status_code() == 201
        persistent_data_store = response.get_result()
        assert persistent_data_store is not None

    @needscredentials
    def test_get_persistent_data_store(self):
        response = self.code_engine_service.get_persistent_data_store(
            project_id=pytest.e2e_test_project_id,
            name='my-persistent-data-store',
        )

        assert response.get_status_code() == 200
        persistent_data_store = response.get_result()
        assert persistent_data_store is not None

    @needscredentials
    def test_list_persistent_data_store(self):
        response = self.code_engine_service.list_persistent_data_store(
            project_id=pytest.e2e_test_project_id,
            limit=100,
        )

        assert response.get_status_code() == 200
        persistent_data_store_list = response.get_result()
        assert persistent_data_store_list is not None

    @needscredentials
    def test_list_persistent_data_store_with_pager(self):
        all_results = []

        # Test get_next().
        pager = PersistentDataStorePager(
            client=self.code_engine_service,
            project_id=pytest.e2e_test_project_id,
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = PersistentDataStorePager(
            client=self.code_engine_service,
            project_id=pytest.e2e_test_project_id,
            limit=100,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(
            f'\nlist_persistent_data_store() returned a total of {len(all_results)} items(s) using PersistentDataStorePager.'
        )

    @needscredentials
    def test_replace_hmac_auth_secret(self):
        response = self.code_engine_service.replace_secret(
            project_id=pytest.e2e_test_project_id,
            name='ce-api-int-test-hmac-secret',
            if_match='*',
            data={'access_key_id': 'access-key-id-2', 'secret_access_key': 'secret-access-key-2'},
            format='hmac_auth',
        )

        assert response.get_status_code() == 200
        secret = response.get_result()
        assert secret is not None

    @needscredentials
    def test_replace_registry_secret(self):
        response = self.code_engine_service.replace_secret(
            project_id=pytest.e2e_test_project_id,
            name='my-registry-secret',
            if_match='*',
            data={'username': 'user2', 'password': 'pass2', 'server': 'github.com', 'email': 'myemail@email.com'},
            format='registry',
        )

        assert response.get_status_code() == 200
        secret = response.get_result()
        assert secret is not None

    @needscredentials
    def test_create_function(self):
        response = self.code_engine_service.create_function(
            project_id=pytest.e2e_test_project_id,
            code_reference='data:text/plain;base64,YXN5bmMgZnVuY3Rpb24gbWFpbihwYXJhbXMpIHsKICByZXR1cm4gewogICAgICBzdGF0dXNDb2RlOiAyMDAsCiAgICAgIGhlYWRlcnM6IHsgJ0NvbnRlbnQtVHlwZSc6ICdhcHBsaWNhdGlvbi9qc29uJyB9LAogICAgICBib2R5OiBwYXJhbXMgfTsKfQptb2R1bGUuZXhwb3J0cy5tYWluID0gbWFpbjs=',
            name='my-function',
            runtime='nodejs-20',
        )

        assert response.get_status_code() == 201
        function = response.get_result()
        assert function is not None

    @needscredentials
    def test_get_function(self):
        response = self.code_engine_service.get_function(
            project_id=pytest.e2e_test_project_id,
            name='my-function',
        )

        assert response.get_status_code() == 200
        function = response.get_result()
        assert function is not None

    @needscredentials
    def test_update_function(self):
        function_patch_model = {
            'ScaleMaxExecutionTime': 30,
        }
        response = self.code_engine_service.update_function(
            project_id=pytest.e2e_test_project_id,
            name='my-function',
            if_match='*',
            function=function_patch_model,
        )

        assert response.get_status_code() == 200
        function = response.get_result()
        assert function is not None

    @needscredentials
    def test_list_functions(self):
        response = self.code_engine_service.list_functions(
            project_id=pytest.e2e_test_project_id,
            limit=100,
        )

        assert response.get_status_code() == 200
        function_list = response.get_result()
        assert function_list is not None

    @needscredentials
    def test_list_function_runtimes(self):
        response = self.code_engine_service.list_function_runtimes()

        assert response.get_status_code() == 200
        function_runtime_list = response.get_result()
        assert function_runtime_list is not None

    @needscredentials
    def test_list_allowed_outbound_destination(self):
        response = self.code_engine_service.list_allowed_outbound_destination(
            project_id=pytest.e2e_test_project_id,
            limit=100,
        )

        assert response.get_status_code() == 200
        allowed_outbound_destination = response.get_result()
        assert allowed_outbound_destination is not None

    @needscredentials
    def test_create_allowed_outbound_destination(self):
        allowed_outbound_destination_prototype_model = {
            'type': 'cidr_block',
            'cidr_block': '192.68.3.0/24',
            'name': 'test-cidr',
        }

        response = self.code_engine_service.create_allowed_outbound_destination(
            project_id=pytest.e2e_test_project_id,
            allowed_outbound_destination=allowed_outbound_destination_prototype_model,
        )

        assert 200 <= response.get_status_code() <= 299
        allowed_outbound_destination = response.get_result()
        assert allowed_outbound_destination is not None

    @needscredentials
    def test_get_allowed_outbound_destination(self):
        response = self.code_engine_service.get_allowed_outbound_destination(
            project_id=pytest.e2e_test_project_id,
            name='test-cidr',
        )

        assert response.get_status_code() == 200
        allowed_outbound_destination = response.get_result()
        assert allowed_outbound_destination is not None

    @needscredentials
    def test_update_allowed_outbound_destination(self):
        allowed_outbound_destination_patch_model = {
            'type': 'cidr_block',
            'cidr_block': '192.68.2.0/24',
        }
        response = self.code_engine_service.update_allowed_outbound_destination(
            project_id=pytest.e2e_test_project_id,
            name='test-cidr',
            if_match='*',
            allowed_outbound_destination=allowed_outbound_destination_patch_model,
        )

        assert response.get_status_code() == 200
        allowed_outbound_destination = response.get_result()
        assert allowed_outbound_destination is not None

    @needscredentials
    def test_delete_allowed_outbound_destination(self):
        response = self.code_engine_service.delete_allowed_outbound_destination(
            project_id=pytest.e2e_test_project_id,
            name='test-cidr',
        )

        assert response.get_status_code() == 202

    @needscredentials
    def test_delete_function(self):
        response = self.code_engine_service.delete_function(
            project_id=pytest.e2e_test_project_id,
            name='my-function',
        )

        assert response.get_status_code() == 202

    @needscredentials
    def test_delete_app_revision(self):
        response = self.code_engine_service.delete_app_revision(
            project_id=pytest.e2e_test_project_id,
            app_name='my-app',
            name='my-app-00001',
        )

        assert response.get_status_code() == 202

    @needscredentials
    def test_delete_app(self):
        response = self.code_engine_service.delete_app(
            project_id=pytest.e2e_test_project_id,
            name='my-app',
        )

        assert response.get_status_code() == 202

    @needscredentials
    def test_delete_job_run(self):
        response = self.code_engine_service.delete_job_run(
            project_id=pytest.e2e_test_project_id,
            name='my-job-run',
        )

        assert response.get_status_code() == 202

    @needscredentials
    def test_delete_job(self):
        response = self.code_engine_service.delete_job(
            project_id=pytest.e2e_test_project_id,
            name='my-job',
        )

        assert response.get_status_code() == 202

    @needscredentials
    def test_delete_build_run(self):
        response = self.code_engine_service.delete_build_run(
            project_id=pytest.e2e_test_project_id,
            name='my-build-run',
        )

        assert response.get_status_code() == 202

    @needscredentials
    def test_delete_build(self):
        response = self.code_engine_service.delete_build(
            project_id=pytest.e2e_test_project_id,
            name='my-build',
        )

        assert response.get_status_code() == 202

    @needscredentials
    def test_delete_persistent_data_store(self):
        response = self.code_engine_service.delete_persistent_data_store(
            project_id=pytest.e2e_test_project_id,
            name='my-persistent-data-store',
        )

        assert response.get_status_code() == 202

    @needscredentials
    def test_delete_config_map(self):
        response = self.code_engine_service.delete_config_map(
            project_id=pytest.e2e_test_project_id,
            name='my-config-map',
        )

        assert response.get_status_code() == 202

    @needscredentials
    def test_delete_secret(self):
        response = self.code_engine_service.delete_secret(
            project_id=pytest.e2e_test_project_id,
            name='my-secret',
        )

        assert response.get_status_code() == 202

    @needscredentials
    def test_delete_ssh_secret(self):
        response = self.code_engine_service.delete_secret(
            project_id=pytest.e2e_test_project_id,
            name='my-ssh-secret',
        )

        assert response.get_status_code() == 202

    @needscredentials
    def test_delete_tls_secret(self):
        response = self.code_engine_service.delete_secret(
            project_id=pytest.e2e_test_project_id,
            name='my-tls-secret',
        )

        assert response.get_status_code() == 202

    @needscredentials
    def test_delete_basic_auth_secret(self):
        response = self.code_engine_service.delete_secret(
            project_id=pytest.e2e_test_project_id,
            name='my-basic-auth-secret',
        )

        assert response.get_status_code() == 202

    @needscredentials
    def test_delete_hmac_auth_secret(self):
        response = self.code_engine_service.delete_secret(
            project_id=pytest.e2e_test_project_id,
            name='ce-api-int-test-hmac-secret',
        )

        assert response.get_status_code() == 202

    @needscredentials
    def test_delete_registry_secret(self):
        response = self.code_engine_service.delete_secret(
            project_id=pytest.e2e_test_project_id,
            name='my-registry-secret',
        )

        assert response.get_status_code() == 202

    @needscredentials
    def test_delete_project(self):
        response = self.code_engine_service.delete_project(
            id=pytest.e2e_test_project_id,
        )

        assert response.get_status_code() == 202

# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azext_devops.action import (
    AddOrganization,
    AddProject,
    AddBootstrapConfigurationTemplateParameters,
    AddBootstrapConfigurationRepositoryProperties,
    AddBootstrapConfigurationRepositoryAuthorizationParameters
)


def load_arguments(self, _):

    with self.argument_context('devops pipeline-template-definition list') as c:
        pass

    with self.argument_context('devops pipeline list') as c:
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('devops pipeline show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('pipeline_name', help='The name of the Azure Pipeline resource in ARM.')

    with self.argument_context('devops pipeline create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('pipeline_name', help='The name of the Azure Pipeline resource in ARM.')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('organization', action=AddOrganization, nargs='+', help='Reference to the Azure DevOps Organization '
                   'containing the Pipeline. Expect value: name=xx.')
        c.argument('project', action=AddProject, nargs='+', help='Reference to the Azure DevOps Project containing the '
                   'Pipeline. Expect value: name=xx.')
        c.argument('bootstrap_configuration_template_id', help='Unique identifier of the pipeline template.')
        c.argument('bootstrap_configuration_template_parameters', action=AddBootstrapConfigurationTemplateParameters,
                   nargs='+', help='Dictionary of input parameters used in the pipeline template. Expect value: KEY1=VA'
                   'LUE1 KEY2=VALUE2 ...')
        c.argument('bootstrap_configuration_repository_repository_type', arg_type=get_enum_type(['gitHub', 'vstsGit']),
                    help='Type of code repository.')
        c.argument('bootstrap_configuration_repository_id',
                   help='Unique immutable identifier of the code repository.')
        c.argument('bootstrap_configuration_repository_default_branch', help='Default branch used to configure Continuo'
                   'us Integration (CI) in the pipeline.')
        c.argument('bootstrap_configuration_repository_properties',
                   action=AddBootstrapConfigurationRepositoryProperties, nargs='+', help='Repository-specific propertie'
                   's. Expect value: KEY1=VALUE1 KEY2=VALUE2 ...')
        c.argument('bootstrap_configuration_repository_authorization_parameters',
                   action=AddBootstrapConfigurationRepositoryAuthorizationParameters, nargs='+', help='Authorization pa'
                   'rameters corresponding to the authorization type. Expect value: KEY1=VALUE1 KEY2=VALUE2 ...')

    with self.argument_context('devops pipeline update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('pipeline_name', help='The name of the Azure Pipeline resource.')
        c.argument('tags', tags_type)

    with self.argument_context('devops pipeline delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('pipeline_name', help='The name of the Azure Pipeline resource.')

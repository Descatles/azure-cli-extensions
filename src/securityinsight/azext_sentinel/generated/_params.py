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
    get_enum_type,
    resource_group_name_type
)
from azext_sentinel.action import (
    AddCreatedBy,
    AddIncidentInfo,
    AddLabels,
    AddOwner
)


def load_arguments(self, _):

    with self.argument_context('sentinel alert-rule list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')

    with self.argument_context('sentinel alert-rule show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('rule_id', help='Alert rule ID')
        c.argument('action_id', help='Action ID')

    with self.argument_context('sentinel alert-rule create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('rule_id', help='Alert rule ID')
        c.argument('action_id', help='Action ID')
        c.argument('etag', help='Etag of the azure resource')
        c.argument('logic_app_resource_id', help='Logic App Resource Id, /subscriptions/{my-subscription}/resourceGroup'
                   's/{my-resource-group}/providers/Microsoft.Logic/workflows/{my-workflow-id}.')
        c.argument('trigger_uri', help='Logic App Callback URL for this specific workflow.')
        c.argument('kind', arg_type=get_enum_type(['Scheduled', 'MicrosoftSecurityIncidentCreation', 'Fusion']), help=
                   'The kind of the alert rule')

    with self.argument_context('sentinel alert-rule delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('rule_id', help='Alert rule ID')
        c.argument('action_id', help='Action ID')

    with self.argument_context('sentinel action list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('rule_id', help='Alert rule ID')

    with self.argument_context('sentinel alert-rule-template list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')

    with self.argument_context('sentinel alert-rule-template show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('alert_rule_template_id', help='Alert rule template ID')

    with self.argument_context('sentinel bookmark list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')

    with self.argument_context('sentinel bookmark show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('bookmark_id', help='Bookmark ID')

    with self.argument_context('sentinel bookmark create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('bookmark_id', help='Bookmark ID')
        c.argument('etag', help='Etag of the azure resource')
        c.argument('created', help='The time the bookmark was created')
        c.argument('created_by', action=AddCreatedBy, nargs='+', help='Describes a user that created the bookmark Expec'
                   't value: object-id=xx.')
        c.argument('display_name', help='The display name of the bookmark')
        c.argument('labels', nargs='+', help='List of labels relevant to this bookmark Expected value: json-string/@jso'
                   'n-file.')
        c.argument('notes', help='The notes of the bookmark')
        c.argument('query', help='The query of the bookmark.')
        c.argument('query_result', help='The query result of the bookmark.')
        c.argument('updated', help='The last time the bookmark was updated')
        c.argument('updated_by', action=AddCreatedBy, nargs='+', help='Describes a user that updated the bookmark Expec'
                   't value: object-id=xx.')
        c.argument('incident_info', action=AddIncidentInfo, nargs='+', help='Describes an incident that relates to book'
                   'mark Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: incident-id, severity, title, '
                   'relation-name.')

    with self.argument_context('sentinel bookmark update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('bookmark_id', help='Bookmark ID')
        c.argument('etag', help='Etag of the azure resource')
        c.argument('created', help='The time the bookmark was created')
        c.argument('created_by', action=AddCreatedBy, nargs='+', help='Describes a user that created the bookmark Expec'
                   't value: object-id=xx.')
        c.argument('display_name', help='The display name of the bookmark')
        c.argument('labels', nargs='+', help='List of labels relevant to this bookmark Expected value: json-string/@jso'
                   'n-file.')
        c.argument('notes', help='The notes of the bookmark')
        c.argument('query', help='The query of the bookmark.')
        c.argument('query_result', help='The query result of the bookmark.')
        c.argument('updated', help='The last time the bookmark was updated')
        c.argument('updated_by', action=AddCreatedBy, nargs='+', help='Describes a user that updated the bookmark Expec'
                   't value: object-id=xx.')
        c.argument('incident_info', action=AddIncidentInfo, nargs='+', help='Describes an incident that relates to book'
                   'mark Expect value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: incident-id, severity, title, '
                   'relation-name.')

    with self.argument_context('sentinel bookmark delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('bookmark_id', help='Bookmark ID')

    with self.argument_context('sentinel data-connector list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')

    with self.argument_context('sentinel data-connector show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('data_connector_id', help='Connector ID')

    with self.argument_context('sentinel data-connector create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('data_connector_id', help='Connector ID')
        c.argument('etag', help='Etag of the azure resource')
        c.argument('kind', arg_type=get_enum_type(['AzureActiveDirectory', 'AzureSecurityCenter', 'MicrosoftCloudAppSec'
                   'urity', 'ThreatIntelligence', 'Office365', 'AmazonWebServicesCloudTrail', 'AzureAdvancedThreatProte'
                   'ction', 'MicrosoftDefenderAdvancedThreatProtection']), help='The kind of the data connector')

    with self.argument_context('sentinel data-connector update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('data_connector_id', help='Connector ID')
        c.argument('etag', help='Etag of the azure resource')
        c.argument('kind', arg_type=get_enum_type(['AzureActiveDirectory', 'AzureSecurityCenter', 'MicrosoftCloudAppSec'
                   'urity', 'ThreatIntelligence', 'Office365', 'AmazonWebServicesCloudTrail', 'AzureAdvancedThreatProte'
                   'ction', 'MicrosoftDefenderAdvancedThreatProtection']), help='The kind of the data connector')

    with self.argument_context('sentinel data-connector delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('data_connector_id', help='Connector ID')

    with self.argument_context('sentinel incident list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('filter', help='Filters the results, based on a Boolean condition. Optional.')
        c.argument('orderby', help='Sorts the results. Optional.')
        c.argument('top', help='Returns only the first n results. Optional.')
        c.argument('skip_token', help='Skiptoken is only used if a previous operation returned a partial result. If a p'
                   'revious response contains a nextLink element, the value of the nextLink element will include a skip'
                   'token parameter that specifies a starting point to use for subsequent calls. Optional.')

    with self.argument_context('sentinel incident show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('incident_id', help='Incident ID')

    with self.argument_context('sentinel incident create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('incident_id', help='Incident ID')
        c.argument('etag', help='Etag of the azure resource')
        c.argument('classification', arg_type=get_enum_type(['Undetermined', 'TruePositive', 'BenignPositive', 'FalsePo'
                   'sitive']), help='The reason the incident was closed')
        c.argument('classification_comment', help='Describes the reason the incident was closed')
        c.argument('classification_reason', arg_type=get_enum_type(['SuspiciousActivity', 'SuspiciousButExpected', 'Inc'
                   'orrectAlertLogic', 'InaccurateData']), help='The classification reason the incident was closed with'
                   '')
        c.argument('description', help='The description of the incident')
        c.argument('first_activity_time_utc', help='The time of the first activity in the incident')
        c.argument('labels', action=AddLabels, nargs='+', help='List of labels relevant to this incident Expect value: '
                   'label-name=xx.')
        c.argument('last_activity_time_utc', help='The time of the last activity in the incident')
        c.argument('owner', action=AddOwner, nargs='+', help='Describes a user that the incident is assigned to Expect '
                   'value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: email, assigned-to, object-id, user-princi'
                   'pal-name.')
        c.argument('severity', arg_type=get_enum_type(['High', 'Medium', 'Low', 'Informational']), help='The severity o'
                   'f the incident')
        c.argument('status', arg_type=get_enum_type(['New', 'Active', 'Closed']), help='The status of the incident')
        c.argument('title', help='The title of the incident')

    with self.argument_context('sentinel incident update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('incident_id', help='Incident ID')
        c.argument('etag', help='Etag of the azure resource')
        c.argument('classification', arg_type=get_enum_type(['Undetermined', 'TruePositive', 'BenignPositive', 'FalsePo'
                   'sitive']), help='The reason the incident was closed')
        c.argument('classification_comment', help='Describes the reason the incident was closed')
        c.argument('classification_reason', arg_type=get_enum_type(['SuspiciousActivity', 'SuspiciousButExpected', 'Inc'
                   'orrectAlertLogic', 'InaccurateData']), help='The classification reason the incident was closed with'
                   '')
        c.argument('description', help='The description of the incident')
        c.argument('first_activity_time_utc', help='The time of the first activity in the incident')
        c.argument('labels', action=AddLabels, nargs='+', help='List of labels relevant to this incident Expect value: '
                   'label-name=xx.')
        c.argument('last_activity_time_utc', help='The time of the last activity in the incident')
        c.argument('owner', action=AddOwner, nargs='+', help='Describes a user that the incident is assigned to Expect '
                   'value: KEY1=VALUE1 KEY2=VALUE2 ... , available KEYs are: email, assigned-to, object-id, user-princi'
                   'pal-name.')
        c.argument('severity', arg_type=get_enum_type(['High', 'Medium', 'Low', 'Informational']), help='The severity o'
                   'f the incident')
        c.argument('status', arg_type=get_enum_type(['New', 'Active', 'Closed']), help='The status of the incident')
        c.argument('title', help='The title of the incident')

    with self.argument_context('sentinel incident delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('incident_id', help='Incident ID')

    with self.argument_context('sentinel incident-comment list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('incident_id', help='Incident ID')
        c.argument('filter', help='Filters the results, based on a Boolean condition. Optional.')
        c.argument('orderby', help='Sorts the results. Optional.')
        c.argument('top', help='Returns only the first n results. Optional.')
        c.argument('skip_token', help='Skiptoken is only used if a previous operation returned a partial result. If a p'
                   'revious response contains a nextLink element, the value of the nextLink element will include a skip'
                   'token parameter that specifies a starting point to use for subsequent calls. Optional.')

    with self.argument_context('sentinel incident-comment show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('incident_id', help='Incident ID')
        c.argument('incident_comment_id', help='Incident comment ID')

    with self.argument_context('sentinel incident-comment create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', help='The name of the workspace.')
        c.argument('incident_id', help='Incident ID')
        c.argument('incident_comment_id', help='Incident comment ID')
        c.argument('message', help='The comment message')
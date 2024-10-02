# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network manager verifier-workspace reachability-analysis-run show",
    is_preview=True,
)
class Show(AAZCommand):
    """Get Reachability Analysis Run.

    :example: ReachabilityAnalysisRunGet
        az network manager verifier-workspace reachability-analysis-run show --name "myAnalysisRun" --workspace-name "myVerifierWorkspace" --network-manager-name "myAVNM" --resource-group "myAVNMResourceGroup" --subscription "00000000-0000-0000-0000-000000000000"
    """

    _aaz_info = {
        "version": "2024-01-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networkmanagers/{}/verifierworkspaces/{}/reachabilityanalysisruns/{}", "2024-01-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.network_manager_name = AAZStrArg(
            options=["--manager-name", "--network-manager-name"],
            help="The name of the network manager.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]*$",
            ),
        )
        _args_schema.reachability_analysis_run_name = AAZStrArg(
            options=["-n", "--name", "--reachability-analysis-run-name"],
            help="Reachability Analysis Run name.",
            required=True,
            id_part="child_name_2",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9_.-]*$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.workspace_name = AAZStrArg(
            options=["--workspace-name"],
            help="Workspace name.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9_.-]*$",
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ReachabilityAnalysisRunsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ReachabilityAnalysisRunsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkManagers/{networkManagerName}/verifierWorkspaces/{workspaceName}/reachabilityAnalysisRuns/{reachabilityAnalysisRunName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "networkManagerName", self.ctx.args.network_manager_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "reachabilityAnalysisRunName", self.ctx.args.reachability_analysis_run_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-01-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.analysis_result = AAZStrType(
                serialized_name="analysisResult",
                flags={"read_only": True},
            )
            properties.description = AAZStrType()
            properties.error_message = AAZStrType(
                serialized_name="errorMessage",
                flags={"read_only": True},
            )
            properties.intent_content = AAZObjectType(
                serialized_name="intentContent",
                flags={"read_only": True},
            )
            properties.intent_id = AAZStrType(
                serialized_name="intentId",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            intent_content = cls._schema_on_200.properties.intent_content
            intent_content.description = AAZStrType()
            intent_content.destination_resource_id = AAZStrType(
                serialized_name="destinationResourceId",
                flags={"required": True},
            )
            intent_content.ip_traffic = AAZObjectType(
                serialized_name="ipTraffic",
                flags={"required": True},
            )
            intent_content.source_resource_id = AAZStrType(
                serialized_name="sourceResourceId",
                flags={"required": True},
            )

            ip_traffic = cls._schema_on_200.properties.intent_content.ip_traffic
            ip_traffic.destination_ips = AAZListType(
                serialized_name="destinationIps",
                flags={"required": True},
            )
            ip_traffic.destination_ports = AAZListType(
                serialized_name="destinationPorts",
                flags={"required": True},
            )
            ip_traffic.protocols = AAZListType(
                flags={"required": True},
            )
            ip_traffic.source_ips = AAZListType(
                serialized_name="sourceIps",
                flags={"required": True},
            )
            ip_traffic.source_ports = AAZListType(
                serialized_name="sourcePorts",
                flags={"required": True},
            )

            destination_ips = cls._schema_on_200.properties.intent_content.ip_traffic.destination_ips
            destination_ips.Element = AAZStrType()

            destination_ports = cls._schema_on_200.properties.intent_content.ip_traffic.destination_ports
            destination_ports.Element = AAZStrType()

            protocols = cls._schema_on_200.properties.intent_content.ip_traffic.protocols
            protocols.Element = AAZStrType()

            source_ips = cls._schema_on_200.properties.intent_content.ip_traffic.source_ips
            source_ips.Element = AAZStrType()

            source_ports = cls._schema_on_200.properties.intent_content.ip_traffic.source_ports
            source_ports.Element = AAZStrType()

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""


__all__ = ["Show"]

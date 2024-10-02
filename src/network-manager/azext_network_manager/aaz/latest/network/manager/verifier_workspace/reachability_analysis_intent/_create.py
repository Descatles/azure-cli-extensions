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
    "network manager verifier-workspace reachability-analysis-intent create",
    is_preview=True,
)
class Create(AAZCommand):
    """Create Reachability Analysis Intent.

    :example: ReachabilityAnalysisIntentCreate
        az network manager verifier-workspace reachability-analysis-intent create --name "myAnalysisIntent” --workspace-name "myVerifierWorkspace" --network-manager-name "myAVNM" --resource-group "myAVNMResourceGroup" --subscription "00000000-0000-0000-0000-000000000000" --description “hello world intent” --source-resource-id “/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.Compute/virtualMachines/testVmSrc” --destination-resource-id “/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.Compute/virtualMachines/testVmDest” --ip-traffic "{source-ips:["10.0.0.0/16”, “12.0.0.0”],destination-ips:["12.0.0.0/8”, “10.0.0.0”],source-ports:["20”, “23”],destination-ports:["80”, “81”],protocols:["TCP”, “UDP”]}"
    """

    _aaz_info = {
        "version": "2024-01-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networkmanagers/{}/verifierworkspaces/{}/reachabilityanalysisintents/{}", "2024-01-01-preview"],
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
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]*$",
            ),
        )
        _args_schema.reachability_analysis_intent_name = AAZStrArg(
            options=["-n", "--name", "--reachability-analysis-intent-name"],
            help="Reachability Analysis Intent name.",
            required=True,
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
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9_.-]*$",
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.description = AAZStrArg(
            options=["--description"],
            arg_group="Properties",
            help="Description of the resource.",
        )
        _args_schema.destination_resource_id = AAZResourceIdArg(
            options=["--dest-resource-id", "--destination-resource-id"],
            arg_group="Properties",
            help="Destination resource id to verify the reachability path of.",
            required=True,
        )
        _args_schema.ip_traffic = AAZObjectArg(
            options=["--ip-traffic"],
            arg_group="Properties",
            help="IP traffic information.",
            required=True,
        )
        _args_schema.source_resource_id = AAZResourceIdArg(
            options=["--source-resource-id"],
            arg_group="Properties",
            help="Source resource id to verify the reachability path of.",
            required=True,
        )

        ip_traffic = cls._args_schema.ip_traffic
        ip_traffic.destination_ips = AAZListArg(
            options=["destination-ips"],
            help="List of destination IP addresses of the traffic..",
            required=True,
        )
        ip_traffic.destination_ports = AAZListArg(
            options=["destination-ports"],
            help="The destination ports of the traffic.",
            required=True,
        )
        ip_traffic.protocols = AAZListArg(
            options=["protocols"],
            required=True,
        )
        ip_traffic.source_ips = AAZListArg(
            options=["source-ips"],
            help="List of source IP addresses of the traffic..",
            required=True,
        )
        ip_traffic.source_ports = AAZListArg(
            options=["source-ports"],
            help="The source ports of the traffic.",
            required=True,
        )

        destination_ips = cls._args_schema.ip_traffic.destination_ips
        destination_ips.Element = AAZStrArg()

        destination_ports = cls._args_schema.ip_traffic.destination_ports
        destination_ports.Element = AAZStrArg()

        protocols = cls._args_schema.ip_traffic.protocols
        protocols.Element = AAZStrArg(
            enum={"Any": "Any", "ICMP": "ICMP", "TCP": "TCP", "UDP": "UDP"},
        )

        source_ips = cls._args_schema.ip_traffic.source_ips
        source_ips.Element = AAZStrArg()

        source_ports = cls._args_schema.ip_traffic.source_ports
        source_ports.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ReachabilityAnalysisIntentsCreate(ctx=self.ctx)()
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

    class ReachabilityAnalysisIntentsCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkManagers/{networkManagerName}/verifierWorkspaces/{workspaceName}/reachabilityAnalysisIntents/{reachabilityAnalysisIntentName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

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
                    "reachabilityAnalysisIntentName", self.ctx.args.reachability_analysis_intent_name,
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
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("description", AAZStrType, ".description")
                properties.set_prop("destinationResourceId", AAZStrType, ".destination_resource_id", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("ipTraffic", AAZObjectType, ".ip_traffic", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("sourceResourceId", AAZStrType, ".source_resource_id", typ_kwargs={"flags": {"required": True}})

            ip_traffic = _builder.get(".properties.ipTraffic")
            if ip_traffic is not None:
                ip_traffic.set_prop("destinationIps", AAZListType, ".destination_ips", typ_kwargs={"flags": {"required": True}})
                ip_traffic.set_prop("destinationPorts", AAZListType, ".destination_ports", typ_kwargs={"flags": {"required": True}})
                ip_traffic.set_prop("protocols", AAZListType, ".protocols", typ_kwargs={"flags": {"required": True}})
                ip_traffic.set_prop("sourceIps", AAZListType, ".source_ips", typ_kwargs={"flags": {"required": True}})
                ip_traffic.set_prop("sourcePorts", AAZListType, ".source_ports", typ_kwargs={"flags": {"required": True}})

            destination_ips = _builder.get(".properties.ipTraffic.destinationIps")
            if destination_ips is not None:
                destination_ips.set_elements(AAZStrType, ".")

            destination_ports = _builder.get(".properties.ipTraffic.destinationPorts")
            if destination_ports is not None:
                destination_ports.set_elements(AAZStrType, ".")

            protocols = _builder.get(".properties.ipTraffic.protocols")
            if protocols is not None:
                protocols.set_elements(AAZStrType, ".")

            source_ips = _builder.get(".properties.ipTraffic.sourceIps")
            if source_ips is not None:
                source_ips.set_elements(AAZStrType, ".")

            source_ports = _builder.get(".properties.ipTraffic.sourcePorts")
            if source_ports is not None:
                source_ports.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"required": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.description = AAZStrType()
            properties.destination_resource_id = AAZStrType(
                serialized_name="destinationResourceId",
                flags={"required": True},
            )
            properties.ip_traffic = AAZObjectType(
                serialized_name="ipTraffic",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.source_resource_id = AAZStrType(
                serialized_name="sourceResourceId",
                flags={"required": True},
            )

            ip_traffic = cls._schema_on_200_201.properties.ip_traffic
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

            destination_ips = cls._schema_on_200_201.properties.ip_traffic.destination_ips
            destination_ips.Element = AAZStrType()

            destination_ports = cls._schema_on_200_201.properties.ip_traffic.destination_ports
            destination_ports.Element = AAZStrType()

            protocols = cls._schema_on_200_201.properties.ip_traffic.protocols
            protocols.Element = AAZStrType()

            source_ips = cls._schema_on_200_201.properties.ip_traffic.source_ips
            source_ips.Element = AAZStrType()

            source_ports = cls._schema_on_200_201.properties.ip_traffic.source_ports
            source_ports.Element = AAZStrType()

            system_data = cls._schema_on_200_201.system_data
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

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]

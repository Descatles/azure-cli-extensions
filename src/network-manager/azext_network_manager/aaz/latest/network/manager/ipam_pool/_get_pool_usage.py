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
    "network manager ipam-pool get-pool-usage",
    is_preview=True,
)
class GetPoolUsage(AAZCommand):
    """Get the Pool Usage.

    :example: IpamPools_GetPoolUsage
        az network manager ipam-pool get-pool-usage --name "myIpamPool" --network-manager-name "myAVNM" --resource-group "myAVNMResourceGroup" --subscription "00000000-0000-0000-0000-000000000000"
    """

    _aaz_info = {
        "version": "2024-01-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networkmanagers/{}/ipampools/{}/getpoolusage", "2024-01-01-preview"],
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
        _args_schema.pool_name = AAZStrArg(
            options=["-n", "--name", "--pool-name"],
            help="Pool resource name.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]*$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.IpamPoolsGetPoolUsage(ctx=self.ctx)()
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

    class IpamPoolsGetPoolUsage(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkManagers/{networkManagerName}/ipamPools/{poolName}/getPoolUsage",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

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
                    "poolName", self.ctx.args.pool_name,
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
            _schema_on_200.address_prefixes = AAZListType(
                serialized_name="addressPrefixes",
                flags={"read_only": True},
            )
            _schema_on_200.allocated_address_prefixes = AAZListType(
                serialized_name="allocatedAddressPrefixes",
                flags={"read_only": True},
            )
            _schema_on_200.available_address_prefixes = AAZListType(
                serialized_name="availableAddressPrefixes",
                flags={"read_only": True},
            )
            _schema_on_200.child_pools = AAZListType(
                serialized_name="childPools",
                flags={"read_only": True},
            )
            _schema_on_200.number_of_allocated_ip_addresses = AAZStrType(
                serialized_name="numberOfAllocatedIPAddresses",
                flags={"read_only": True},
            )
            _schema_on_200.number_of_available_ip_addresses = AAZStrType(
                serialized_name="numberOfAvailableIPAddresses",
                flags={"read_only": True},
            )
            _schema_on_200.number_of_reserved_ip_addresses = AAZStrType(
                serialized_name="numberOfReservedIPAddresses",
                flags={"read_only": True},
            )
            _schema_on_200.reserved_address_prefixes = AAZListType(
                serialized_name="reservedAddressPrefixes",
                flags={"read_only": True},
            )
            _schema_on_200.total_number_of_ip_addresses = AAZStrType(
                serialized_name="totalNumberOfIPAddresses",
                flags={"read_only": True},
            )

            address_prefixes = cls._schema_on_200.address_prefixes
            address_prefixes.Element = AAZStrType()

            allocated_address_prefixes = cls._schema_on_200.allocated_address_prefixes
            allocated_address_prefixes.Element = AAZStrType()

            available_address_prefixes = cls._schema_on_200.available_address_prefixes
            available_address_prefixes.Element = AAZStrType()

            child_pools = cls._schema_on_200.child_pools
            child_pools.Element = AAZObjectType()

            _element = cls._schema_on_200.child_pools.Element
            _element.address_prefixes = AAZListType(
                serialized_name="addressPrefixes",
            )
            _element.resource_id = AAZStrType(
                serialized_name="resourceId",
            )

            address_prefixes = cls._schema_on_200.child_pools.Element.address_prefixes
            address_prefixes.Element = AAZStrType()

            reserved_address_prefixes = cls._schema_on_200.reserved_address_prefixes
            reserved_address_prefixes.Element = AAZStrType()

            return cls._schema_on_200


class _GetPoolUsageHelper:
    """Helper class for GetPoolUsage"""


__all__ = ["GetPoolUsage"]

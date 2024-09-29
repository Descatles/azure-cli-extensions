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
    "elastic monitor open-ai-integration create",
)
class Create(AAZCommand):
    """Create a OpenAI integration rule for a given monitor resource.

    :example: OpenAI_CreateOrUpdate
        az elastic monitor open-ai-integration create --resource-group myResourceGroup --monitor-name myMonitor --integration-name default
    """

    _aaz_info = {
        "version": "2024-06-15-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.elastic/monitors/{}/openaiintegrations/{}", "2024-06-15-preview"],
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
        _args_schema.integration_name = AAZStrArg(
            options=["-n", "--name", "--integration-name"],
            help="OpenAI Integration name",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-z][a-z0-9]*$",
            ),
        )
        _args_schema.monitor_name = AAZStrArg(
            options=["--monitor-name"],
            help="Monitor resource name",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^.*$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.key = AAZStrArg(
            options=["--key"],
            arg_group="Properties",
            help="Value of API key for Open AI resource",
        )
        _args_schema.open_ai_connector_id = AAZStrArg(
            options=["--open-ai-connector-id"],
            arg_group="Properties",
            help="The connector id of Open AI resource",
        )
        _args_schema.open_ai_resource_endpoint = AAZStrArg(
            options=["-e","--open-ai-resource-endpoint"],
            arg_group="Properties",
            help="The API endpoint for Open AI resource",
        )
        _args_schema.open_ai_resource_id = AAZStrArg(
            options=["--open-ai-resource-id"],
            arg_group="Properties",
            help="The resource name of Open AI resource",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.OpenAICreateOrUpdate(ctx=self.ctx)()
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

    class OpenAICreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Elastic/monitors/{monitorName}/openAIIntegrations/{integrationName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "integrationName", self.ctx.args.integration_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "monitorName", self.ctx.args.monitor_name,
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
                    "api-version", "2024-06-15-preview",
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
                typ_kwargs={"flags": {"client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType)

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("key", AAZStrType, ".key", typ_kwargs={"flags": {"secret": True}})
                properties.set_prop("openAIConnectorId", AAZStrType, ".open_ai_connector_id")
                properties.set_prop("openAIResourceEndpoint", AAZStrType, ".open_ai_resource_endpoint")
                properties.set_prop("openAIResourceId", AAZStrType, ".open_ai_resource_id")

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
            _schema_on_200_201.properties = AAZObjectType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.key = AAZStrType(
                flags={"secret": True},
            )
            properties.last_refresh_at = AAZStrType(
                serialized_name="lastRefreshAt",
                flags={"read_only": True},
            )
            properties.open_ai_connector_id = AAZStrType(
                serialized_name="openAIConnectorId",
            )
            properties.open_ai_resource_endpoint = AAZStrType(
                serialized_name="openAIResourceEndpoint",
            )
            properties.open_ai_resource_id = AAZStrType(
                serialized_name="openAIResourceId",
            )

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]

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
    "acat report webhook create",
)
class Create(AAZCommand):
    """Create a new AppComplianceAutomation webhook or update an exiting AppComplianceAutomation webhook.

    :example: Webhook_CreateOrUpdate
        az acat report webhook create --report-name testReportName --webhook-name testWebhookName --content-type application/json --enable-ssl-verification true --events "[generate_snapshot_failed]" --payload-url https://example.com --send-all-events false --status Enabled --update-webhook-key true --webhook-key 00000000-0000-0000-0000-000000000000

    :example: Webhook_CreateOrUpdate
        az acat report webhook create --report-name testReportName --webhook-name testWebhookName --content-type application/json --enable-ssl true --events "[generate_snapshot_failed]" --payload-url https://example.com --send-all-events false --status Enabled --update-webhook-key true --secret 00000000-0000-0000-0000-000000000000
        az acat report webhook create --report-name testReportName --webhook-name testWebhookName --payload-url https://example.com  --secret 00000000-0000-0000-0000-000000000000
    """

    _aaz_info = {
        "version": "2024-06-27",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.appcomplianceautomation/reports/{}/webhooks/{}", "2024-06-27"],
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
        _args_schema.report_name = AAZStrArg(
            options=["--report-name"],
            help="Report Name.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[-a-zA-Z0-9_]{1,50}$",
            ),
        )
        _args_schema.webhook_name = AAZStrArg(
            options=["--webhook-name"],
            help="Webhook Name.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[-a-zA-Z0-9_]{1,50}$",
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.content_type = AAZStrArg(
            options=["--content-type"],
            arg_group="Properties",
            help="content type",
            default="application/json",
            enum={"application/json": "application/json"},
        )
        _args_schema.enable_ssl = AAZStrArg(
            options=["--enable-ssl"],
            arg_group="Properties",
            help="whether to enable ssl verification",
            default="true",
            enum={"false": "false", "true": "true"},
        )
        _args_schema.events = AAZListArg(
            options=["--events"],
            arg_group="Properties",
            help="under which event notification should be sent.",
            default=[],
        )
        _args_schema.payload_url = AAZStrArg(
            options=["--payload-url"],
            arg_group="Properties",
            help="webhook payload url",
            fmt=AAZStrArgFormat(
                pattern="^(http(s)?://)[\\S]{0,64994}$",
            ),
        )
        _args_schema.send_all_events = AAZStrArg(
            options=["--send-all-events"],
            arg_group="Properties",
            help="whether to send notification under any event.",
            enum={"false": "false", "true": "true"},
        )
        _args_schema.status = AAZStrArg(
            options=["--status"],
            arg_group="Properties",
            help="Webhook status.",
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        _args_schema.update_webhook_key = AAZStrArg(
            options=["--update-webhook-key"],
            arg_group="Properties",
            help="whether to update webhookKey.",
            enum={"false": "false", "true": "true"},
        )
        _args_schema.secret = AAZStrArg(
            options=["--secret"],
            arg_group="Properties",
            help="webhook secret token. If not set, this field value is null; otherwise, please set a string value.",
            fmt=AAZStrArgFormat(
                pattern="^.{0,2048}$",
            ),
        )

        events = cls._args_schema.events
        events.Element = AAZStrArg(
            enum={"assessment_failure": "assessment_failure", "generate_snapshot_failed": "generate_snapshot_failed", "generate_snapshot_success": "generate_snapshot_success", "report_configuration_changes": "report_configuration_changes", "report_deletion": "report_deletion"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.WebhookCreateOrUpdate(ctx=self.ctx)()
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

    class WebhookCreateOrUpdate(AAZHttpOperation):
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
                "/providers/Microsoft.AppComplianceAutomation/reports/{reportName}/webhooks/{webhookName}",
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
                    "reportName", self.ctx.args.report_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "webhookName", self.ctx.args.webhook_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-06-27",
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
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("contentType", AAZStrType, ".content_type")
                properties.set_prop("enableSslVerification", AAZStrType, ".enable_ssl")
                properties.set_prop("events", AAZListType, ".events")
                properties.set_prop("payloadUrl", AAZStrType, ".payload_url")
                properties.set_prop("sendAllEvents", AAZStrType, ".send_all_events")
                properties.set_prop("status", AAZStrType, ".status")
                properties.set_prop("updateWebhookKey", AAZStrType, ".update_webhook_key")
                properties.set_prop("webhookKey", AAZStrType, ".secret")

            events = _builder.get(".properties.events")
            if events is not None:
                events.set_elements(AAZStrType, ".")

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
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.content_type = AAZStrType(
                serialized_name="contentType",
            )
            properties.delivery_status = AAZStrType(
                serialized_name="deliveryStatus",
                flags={"read_only": True},
            )
            properties.enable_ssl_verification = AAZStrType(
                serialized_name="enableSslVerification",
            )
            properties.events = AAZListType()
            properties.payload_url = AAZStrType(
                serialized_name="payloadUrl",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.send_all_events = AAZStrType(
                serialized_name="sendAllEvents",
            )
            properties.status = AAZStrType()
            properties.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            properties.update_webhook_key = AAZStrType(
                serialized_name="updateWebhookKey",
            )
            properties.webhook_id = AAZStrType(
                serialized_name="webhookId",
                flags={"read_only": True},
            )
            properties.webhook_key = AAZStrType(
                serialized_name="webhookKey",
            )
            properties.webhook_key_enabled = AAZStrType(
                serialized_name="webhookKeyEnabled",
                flags={"read_only": True},
            )

            events = cls._schema_on_200_201.properties.events
            events.Element = AAZStrType()

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

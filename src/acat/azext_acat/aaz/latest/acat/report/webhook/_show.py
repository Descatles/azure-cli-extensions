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
    "acat report webhook show",
)
class Show(AAZCommand):
    """Get the AppComplianceAutomation webhook and its properties.

    :example: Webhook_Get
        az acat report webhook show --report-name testReportName --webhook-name testWebhookName
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
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.WebhookGet(ctx=self.ctx)()
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

    class WebhookGet(AAZHttpOperation):
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
                "/providers/Microsoft.AppComplianceAutomation/reports/{reportName}/webhooks/{webhookName}",
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
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
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

            events = cls._schema_on_200.properties.events
            events.Element = AAZStrType()

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

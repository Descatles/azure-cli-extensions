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
    "maintenance applyupdate update",
)
class Update(AAZCommand):
    """Update maintenance updates to resource
    """

    _aaz_info = {
        "version": "2023-10-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/{}/{}/{}/providers/microsoft.maintenance/applyupdates/{}", "2023-10-01-preview"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

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
        _args_schema.apply_update_name = AAZStrArg(
            options=["-n", "--name", "--apply-update-name"],
            help="applyUpdate Id",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.provider_name = AAZStrArg(
            options=["--provider-name"],
            help="Resource provider name",
            required=True,
            id_part="namespace",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.resource_name = AAZStrArg(
            options=["--resource-name"],
            help="Resource identifier",
            required=True,
            id_part="name",
        )
        _args_schema.resource_type = AAZStrArg(
            options=["--resource-type"],
            help="Resource type",
            required=True,
            id_part="type",
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.last_update_time = AAZDateTimeArg(
            options=["--last-update-time"],
            arg_group="Properties",
            help="Last Update time",
            nullable=True,
        )
        _args_schema.resource_id = AAZStrArg(
            options=["--resource-id"],
            arg_group="Properties",
            help="The resourceId",
            nullable=True,
        )
        _args_schema.status = AAZStrArg(
            options=["--status"],
            arg_group="Properties",
            help="The status",
            nullable=True,
            enum={"Cancel": "Cancel", "Cancelled": "Cancelled", "Completed": "Completed", "InProgress": "InProgress", "NoUpdatesPending": "NoUpdatesPending", "Pending": "Pending", "RetryLater": "RetryLater", "RetryNow": "RetryNow"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ApplyUpdatesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.ApplyUpdatesCreateOrUpdateOrCancel(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ApplyUpdatesGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{providerName}/{resourceType}/{resourceName}/providers/Microsoft.Maintenance/applyUpdates/{applyUpdateName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "applyUpdateName", self.ctx.args.apply_update_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "providerName", self.ctx.args.provider_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceName", self.ctx.args.resource_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceType", self.ctx.args.resource_type,
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
                    "api-version", "2023-10-01-preview",
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
            _UpdateHelper._build_schema_apply_update_read(cls._schema_on_200)

            return cls._schema_on_200

    class ApplyUpdatesCreateOrUpdateOrCancel(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{providerName}/{resourceType}/{resourceName}/providers/Microsoft.Maintenance/applyUpdates/{applyUpdateName}",
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
                    "applyUpdateName", self.ctx.args.apply_update_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "providerName", self.ctx.args.provider_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceName", self.ctx.args.resource_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceType", self.ctx.args.resource_type,
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
                    "api-version", "2023-10-01-preview",
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
                value=self.ctx.vars.instance,
            )

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
            _UpdateHelper._build_schema_apply_update_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("lastUpdateTime", AAZStrType, ".last_update_time")
                properties.set_prop("resourceId", AAZStrType, ".resource_id")
                properties.set_prop("status", AAZStrType, ".status")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_apply_update_read = None

    @classmethod
    def _build_schema_apply_update_read(cls, _schema):
        if cls._schema_apply_update_read is not None:
            _schema.id = cls._schema_apply_update_read.id
            _schema.name = cls._schema_apply_update_read.name
            _schema.properties = cls._schema_apply_update_read.properties
            _schema.system_data = cls._schema_apply_update_read.system_data
            _schema.type = cls._schema_apply_update_read.type
            return

        cls._schema_apply_update_read = _schema_apply_update_read = AAZObjectType()

        apply_update_read = _schema_apply_update_read
        apply_update_read.id = AAZStrType(
            flags={"read_only": True},
        )
        apply_update_read.name = AAZStrType(
            flags={"read_only": True},
        )
        apply_update_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        apply_update_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        apply_update_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_apply_update_read.properties
        properties.last_update_time = AAZStrType(
            serialized_name="lastUpdateTime",
        )
        properties.resource_id = AAZStrType(
            serialized_name="resourceId",
        )
        properties.status = AAZStrType()

        system_data = _schema_apply_update_read.system_data
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

        _schema.id = cls._schema_apply_update_read.id
        _schema.name = cls._schema_apply_update_read.name
        _schema.properties = cls._schema_apply_update_read.properties
        _schema.system_data = cls._schema_apply_update_read.system_data
        _schema.type = cls._schema_apply_update_read.type


__all__ = ["Update"]

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
    "maintenance assignment create-or-update-subscription",
    is_experimental=True,
)
class CreateOrUpdateSubscription(AAZCommand):
    """Create configuration for resource.

    :example: ConfigurationAssignments_CreateOrUpdateSubscription
        az maintenance assignment create-or-update-subscription  --maintenance-configuration-id "/subscriptions/00000000-0000-0000-0000-00000000/resourcegroups/exmaplerg2/providers/Microsoft. Maintenance/maintenanceConfigurations/config1"  --name assignmentname  --filter-locations eastus2euap centraluseuap  --filter-os-types windows linux  --filter-tags "{tagKey1:[tagKey1Val1,tagKey1Val2],tagKey2:[tagKey2Val1,tagKey2Val2]}"  --filter-tags-operator All
    """

    _aaz_info = {
        "version": "2023-04-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.maintenance/configurationassignments/{}", "2023-04-01"],
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
        _args_schema.configuration_assignment_name = AAZStrArg(
            options=["-n", "--name", "--configuration-assignment-name"],
            help="Configuration assignment name",
            required=True,
            id_part="name",
        )

        # define Arg Group "ConfigurationAssignment"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="ConfigurationAssignment",
            help="Location of the resource",
        )

        # define Arg Group "Filter"

        _args_schema = cls._args_schema
        _args_schema.filter_locations = AAZListArg(
            options=["--filter-locations"],
            arg_group="Filter",
            help="List of locations to scope the query to.",
        )
        _args_schema.filter_os_types = AAZListArg(
            options=["--filter-os-types"],
            arg_group="Filter",
            help="List of allowed operating systems.",
        )
        _args_schema.filter_resource_groups = AAZListArg(
            options=["--filter-resource-groups"],
            arg_group="Filter",
            help="List of allowed resource groups.",
        )
        _args_schema.filter_resource_types = AAZListArg(
            options=["--filter-resource-types"],
            arg_group="Filter",
            help="List of allowed resources.",
        )

        filter_locations = cls._args_schema.filter_locations
        filter_locations.Element = AAZStrArg()

        filter_os_types = cls._args_schema.filter_os_types
        filter_os_types.Element = AAZStrArg()

        filter_resource_groups = cls._args_schema.filter_resource_groups
        filter_resource_groups.Element = AAZStrArg()

        filter_resource_types = cls._args_schema.filter_resource_types
        filter_resource_types.Element = AAZStrArg()

        # define Arg Group "FilterTagSettings"

        _args_schema = cls._args_schema
        _args_schema.filter_tags_operator = AAZStrArg(
            options=["--filter-tags-operator"],
            arg_group="FilterTagSettings",
            help="Filter VMs by Any or All specified tags.",
            enum={"All": "All", "Any": "Any"},
        )
        _args_schema.filter_tags = AAZDictArg(
            options=["--filter-tags"],
            arg_group="FilterTagSettings",
            help="Dictionary of tags with its list of values.",
        )

        filter_tags = cls._args_schema.filter_tags
        filter_tags.Element = AAZListArg()

        _element = cls._args_schema.filter_tags.Element
        _element.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.maintenance_configuration_id = AAZStrArg(
            options=["--config-id", "--maintenance-configuration-id"],
            arg_group="Properties",
            help="The maintenance configuration Id",
        )
        _args_schema.resource_id = AAZStrArg(
            options=["--resource-id"],
            arg_group="Properties",
            help="The unique resourceId",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ConfigurationAssignmentsForSubscriptionsCreateOrUpdate(ctx=self.ctx)()
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

    class ConfigurationAssignmentsForSubscriptionsCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/providers/Microsoft.Maintenance/configurationAssignments/{configurationAssignmentName}",
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
                    "configurationAssignmentName", self.ctx.args.configuration_assignment_name,
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
                    "api-version", "2023-04-01",
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
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("filter", AAZObjectType)
                properties.set_prop("maintenanceConfigurationId", AAZStrType, ".maintenance_configuration_id")
                properties.set_prop("resourceId", AAZStrType, ".resource_id")

            filter = _builder.get(".properties.filter")
            if filter is not None:
                filter.set_prop("locations", AAZListType, ".filter_locations")
                filter.set_prop("osTypes", AAZListType, ".filter_os_types")
                filter.set_prop("resourceGroups", AAZListType, ".filter_resource_groups")
                filter.set_prop("resourceTypes", AAZListType, ".filter_resource_types")
                filter.set_prop("tagSettings", AAZObjectType)

            locations = _builder.get(".properties.filter.locations")
            if locations is not None:
                locations.set_elements(AAZStrType, ".")

            os_types = _builder.get(".properties.filter.osTypes")
            if os_types is not None:
                os_types.set_elements(AAZStrType, ".")

            resource_groups = _builder.get(".properties.filter.resourceGroups")
            if resource_groups is not None:
                resource_groups.set_elements(AAZStrType, ".")

            resource_types = _builder.get(".properties.filter.resourceTypes")
            if resource_types is not None:
                resource_types.set_elements(AAZStrType, ".")

            tag_settings = _builder.get(".properties.filter.tagSettings")
            if tag_settings is not None:
                tag_settings.set_prop("filterOperator", AAZStrType, ".filter_tags_operator")
                tag_settings.set_prop("tags", AAZDictType, ".filter_tags")

            tags = _builder.get(".properties.filter.tagSettings.tags")
            if tags is not None:
                tags.set_elements(AAZListType, ".")

            _elements = _builder.get(".properties.filter.tagSettings.tags{}")
            if _elements is not None:
                _elements.set_elements(AAZStrType, ".")

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
            _schema_on_200_201.location = AAZStrType()
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.filter = AAZObjectType()
            properties.maintenance_configuration_id = AAZStrType(
                serialized_name="maintenanceConfigurationId",
            )
            properties.resource_id = AAZStrType(
                serialized_name="resourceId",
            )

            filter = cls._schema_on_200_201.properties.filter
            filter.locations = AAZListType()
            filter.os_types = AAZListType(
                serialized_name="osTypes",
            )
            filter.resource_groups = AAZListType(
                serialized_name="resourceGroups",
            )
            filter.resource_types = AAZListType(
                serialized_name="resourceTypes",
            )
            filter.tag_settings = AAZObjectType(
                serialized_name="tagSettings",
            )

            locations = cls._schema_on_200_201.properties.filter.locations
            locations.Element = AAZStrType()

            os_types = cls._schema_on_200_201.properties.filter.os_types
            os_types.Element = AAZStrType()

            resource_groups = cls._schema_on_200_201.properties.filter.resource_groups
            resource_groups.Element = AAZStrType()

            resource_types = cls._schema_on_200_201.properties.filter.resource_types
            resource_types.Element = AAZStrType()

            tag_settings = cls._schema_on_200_201.properties.filter.tag_settings
            tag_settings.filter_operator = AAZStrType(
                serialized_name="filterOperator",
            )
            tag_settings.tags = AAZDictType()

            tags = cls._schema_on_200_201.properties.filter.tag_settings.tags
            tags.Element = AAZListType()

            _element = cls._schema_on_200_201.properties.filter.tag_settings.tags.Element
            _element.Element = AAZStrType()

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


class _CreateOrUpdateSubscriptionHelper:
    """Helper class for CreateOrUpdateSubscription"""


__all__ = ["CreateOrUpdateSubscription"]

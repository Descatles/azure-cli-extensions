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
    "redisenterprise database create",
)
class Create(AAZCommand):
    """Create a database
    """

    _aaz_info = {
        "version": "2024-09-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.cache/redisenterprise/{}/databases/{}", "2024-09-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.cluster_name = AAZStrArg(
            options=["--cluster-name"],
            help="The name of the RedisEnterprise cluster.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[A-Za-z0-9]+(-[A-Za-z0-9]+)*$",
            ),
        )
        _args_schema.database_name = AAZStrArg(
            options=["-n", "--name", "--database-name"],
            help="The name of the database.",
            required=True,
            default="default",
            fmt=AAZStrArgFormat(
                pattern="^[A-Za-z0-9]{1,60}$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "GeoReplication"

        _args_schema = cls._args_schema
        _args_schema.group_nickname = AAZStrArg(
            options=["--group-nickname"],
            arg_group="GeoReplication",
            help="Name for the group of linked database resources",
        )
        _args_schema.linkeddatabase = AAZListArg(
            options=["--linkeddatabase"],
            singular_options=["--linked-database", "--linked-databases"],
            arg_group="GeoReplication",
            help="List of database resources to link with this database",
        )

        linkeddatabase = cls._args_schema.linkeddatabase
        linkeddatabase.Element = AAZObjectArg()

        _element = cls._args_schema.linkeddatabase.Element
        _element.id = AAZResourceIdArg(
            options=["id"],
            help="Resource ID of a database resource to link with this database.",
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.access_keys_authentication = AAZStrArg(
            options=["--access-keys-auth", "--access-keys-authentication"],
            arg_group="Properties",
            help="Access database using keys - default is enabled. This property can be Enabled/Disabled to allow or deny access with the current access keys. Can be updated even after database is created.",
            is_preview=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        _args_schema.client_protocol = AAZStrArg(
            options=["--client-protocol"],
            arg_group="Properties",
            help="Specifies whether redis clients can connect using TLS-encrypted or plaintext redis protocols. Default is TLS-encrypted.",
            enum={"Encrypted": "Encrypted", "Plaintext": "Plaintext"},
        )
        _args_schema.clustering_policy = AAZStrArg(
            options=["--clustering-policy"],
            arg_group="Properties",
            help="Clustering policy - default is OSSCluster. Specified at create time.",
            enum={"EnterpriseCluster": "EnterpriseCluster", "OSSCluster": "OSSCluster"},
        )
        _args_schema.defer_upgrade = AAZStrArg(
            options=["--defer-upgrade"],
            arg_group="Properties",
            help="Option to defer upgrade when newest version is released - default is NotDeferred. Learn more: https://aka.ms/redisversionupgrade",
            enum={"Deferred": "Deferred", "NotDeferred": "NotDeferred"},
        )
        _args_schema.eviction_policy = AAZStrArg(
            options=["--eviction-policy"],
            arg_group="Properties",
            help="Redis eviction policy - default is VolatileLRU",
            enum={"AllKeysLFU": "AllKeysLFU", "AllKeysLRU": "AllKeysLRU", "AllKeysRandom": "AllKeysRandom", "NoEviction": "NoEviction", "VolatileLFU": "VolatileLFU", "VolatileLRU": "VolatileLRU", "VolatileRandom": "VolatileRandom", "VolatileTTL": "VolatileTTL"},
        )
        _args_schema.mods = AAZListArg(
            options=["--mods"],
            singular_options=["--module", "--modules"],
            arg_group="Properties",
            help="Optional set of redis modules to enable in this database - modules can only be added at creation time.",
        )
        _args_schema.persistence = AAZObjectArg(
            options=["--persistence"],
            arg_group="Properties",
            help="Persistence settings",
        )
        _args_schema.port = AAZIntArg(
            options=["--port"],
            arg_group="Properties",
            help="TCP port of the database endpoint. Specified at create time. Defaults to an available port.",
        )

        mods = cls._args_schema.mods
        mods.Element = AAZObjectArg()

        _element = cls._args_schema.mods.Element
        _element.args = AAZStrArg(
            options=["args"],
            help="Configuration options for the module, e.g. 'ERROR_RATE 0.01 INITIAL_SIZE 400'.",
        )
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the module, e.g. 'RedisBloom', 'RediSearch', 'RedisTimeSeries'",
            required=True,
        )

        persistence = cls._args_schema.persistence
        persistence.aof_enabled = AAZBoolArg(
            options=["aof-enabled"],
            help="Sets whether AOF is enabled.",
        )
        persistence.aof_frequency = AAZStrArg(
            options=["aof-frequency"],
            help="Sets the frequency at which data is written to disk.",
            enum={"1s": "1s", "always": "always"},
        )
        persistence.rdb_enabled = AAZBoolArg(
            options=["rdb-enabled"],
            help="Sets whether RDB is enabled.",
        )
        persistence.rdb_frequency = AAZStrArg(
            options=["rdb-frequency"],
            help="Sets the frequency at which a snapshot of the database is created.",
            enum={"12h": "12h", "1h": "1h", "6h": "6h"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.DatabasesCreate(ctx=self.ctx)()
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

    class DatabasesCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "original-uri"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "original-uri"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/redisEnterprise/{clusterName}/databases/{databaseName}",
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
                    "clusterName", self.ctx.args.cluster_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "databaseName", self.ctx.args.database_name,
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
                    "api-version", "2024-09-01-preview",
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
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("accessKeysAuthentication", AAZStrType, ".access_keys_authentication")
                properties.set_prop("clientProtocol", AAZStrType, ".client_protocol")
                properties.set_prop("clusteringPolicy", AAZStrType, ".clustering_policy")
                properties.set_prop("deferUpgrade", AAZStrType, ".defer_upgrade")
                properties.set_prop("evictionPolicy", AAZStrType, ".eviction_policy")
                properties.set_prop("geoReplication", AAZObjectType)
                properties.set_prop("modules", AAZListType, ".mods")
                properties.set_prop("persistence", AAZObjectType, ".persistence")
                properties.set_prop("port", AAZIntType, ".port")

            geo_replication = _builder.get(".properties.geoReplication")
            if geo_replication is not None:
                geo_replication.set_prop("groupNickname", AAZStrType, ".group_nickname")
                geo_replication.set_prop("linkedDatabases", AAZListType, ".linkeddatabase")

            linked_databases = _builder.get(".properties.geoReplication.linkedDatabases")
            if linked_databases is not None:
                linked_databases.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.geoReplication.linkedDatabases[]")
            if _elements is not None:
                _elements.set_prop("id", AAZStrType, ".id")

            modules = _builder.get(".properties.modules")
            if modules is not None:
                modules.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.modules[]")
            if _elements is not None:
                _elements.set_prop("args", AAZStrType, ".args")
                _elements.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})

            persistence = _builder.get(".properties.persistence")
            if persistence is not None:
                persistence.set_prop("aofEnabled", AAZBoolType, ".aof_enabled")
                persistence.set_prop("aofFrequency", AAZStrType, ".aof_frequency")
                persistence.set_prop("rdbEnabled", AAZBoolType, ".rdb_enabled")
                persistence.set_prop("rdbFrequency", AAZStrType, ".rdb_frequency")

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
            properties.access_keys_authentication = AAZStrType(
                serialized_name="accessKeysAuthentication",
            )
            properties.client_protocol = AAZStrType(
                serialized_name="clientProtocol",
            )
            properties.clustering_policy = AAZStrType(
                serialized_name="clusteringPolicy",
            )
            properties.defer_upgrade = AAZStrType(
                serialized_name="deferUpgrade",
            )
            properties.eviction_policy = AAZStrType(
                serialized_name="evictionPolicy",
            )
            properties.geo_replication = AAZObjectType(
                serialized_name="geoReplication",
            )
            properties.modules = AAZListType()
            properties.persistence = AAZObjectType()
            properties.port = AAZIntType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.redis_version = AAZStrType(
                serialized_name="redisVersion",
                flags={"read_only": True},
            )
            properties.resource_state = AAZStrType(
                serialized_name="resourceState",
                flags={"read_only": True},
            )

            geo_replication = cls._schema_on_200_201.properties.geo_replication
            geo_replication.group_nickname = AAZStrType(
                serialized_name="groupNickname",
            )
            geo_replication.linked_databases = AAZListType(
                serialized_name="linkedDatabases",
            )

            linked_databases = cls._schema_on_200_201.properties.geo_replication.linked_databases
            linked_databases.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.geo_replication.linked_databases.Element
            _element.id = AAZStrType()
            _element.state = AAZStrType(
                flags={"read_only": True},
            )

            modules = cls._schema_on_200_201.properties.modules
            modules.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.modules.Element
            _element.args = AAZStrType()
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.version = AAZStrType(
                flags={"read_only": True},
            )

            persistence = cls._schema_on_200_201.properties.persistence
            persistence.aof_enabled = AAZBoolType(
                serialized_name="aofEnabled",
            )
            persistence.aof_frequency = AAZStrType(
                serialized_name="aofFrequency",
            )
            persistence.rdb_enabled = AAZBoolType(
                serialized_name="rdbEnabled",
            )
            persistence.rdb_frequency = AAZStrType(
                serialized_name="rdbFrequency",
            )

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

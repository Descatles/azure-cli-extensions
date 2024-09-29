# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from email.policy import default
from multiprocessing import Value
from knack.log import get_logger
from .aaz.latest.redisenterprise.database import Flush as _DatabaseFlush
from .aaz.latest.redisenterprise.database import ForceUnlink as _DatabaseForceUnlink
from .aaz.latest.redisenterprise.database import Create as _DatabaseCreate
from .aaz.latest.redisenterprise.database import Delete as _DatabaseDelete
from .aaz.latest.redisenterprise.database import Export as _DatabaseExport
from .aaz.latest.redisenterprise.database import Import as _DatabaseImport
from .aaz.latest.redisenterprise.database import List as _DatabaseList
from .aaz.latest.redisenterprise.database import RegenerateKey as _DatabaseRegenerateKey
from .aaz.latest.redisenterprise.database import ListKeys as _DatabaseListKey
from .aaz.latest.redisenterprise.database import Show as _DatabaseShow
from .aaz.latest.redisenterprise.database import Update as _DatabaseUpdate
from .aaz.latest.redisenterprise.database import Wait as _DatabaseWait
from .aaz.latest.redisenterprise import List as _ClusterList
from .aaz.latest.redisenterprise import Show as _ClusterShow
from .aaz.latest.redisenterprise import Wait as _DatabaseWait
from azure.cli.core.azclierror import (
    MutuallyExclusiveArgumentError,
)

logger = get_logger(__name__)


class DatabaseFlush(_DatabaseFlush):

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.database_name._registered = False
        args_schema.database_name._required = False
        return args_schema

    def pre_operations(self):
        self.ctx.args.database_name = "default"


class DatabaseForceUnlink(_DatabaseForceUnlink):

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.database_name._registered = False
        args_schema.database_name._required = False
        return args_schema

    def pre_operations(self):
        self.ctx.args.database_name = "default"


class DatabaseCreate(_DatabaseCreate):

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.database_name._registered = False
        args_schema.database_name._required = False
        return args_schema

    def pre_operations(self):
        self.ctx.args.database_name = "default"


class DatabaseDelete(_DatabaseDelete):

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.database_name._registered = False
        args_schema.database_name._required = False
        return args_schema

    def pre_operations(self):
        self.ctx.args.database_name = "default"


class DatabaseExport(_DatabaseExport):

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.database_name._registered = False
        args_schema.database_name._required = False
        return args_schema

    def pre_operations(self):
        self.ctx.args.database_name = "default"


class DatabaseImport(_DatabaseImport):

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.database_name._registered = False
        args_schema.database_name._required = False
        return args_schema

    def pre_operations(self):
        self.ctx.args.database_name = "default"


class DatabaseRegenerateKey(_DatabaseRegenerateKey):

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.database_name._registered = False
        args_schema.database_name._required = False
        return args_schema

    def pre_operations(self):
        self.ctx.args.database_name = "default"


class DatabaseListKey(_DatabaseListKey):

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.database_name._registered = False
        args_schema.database_name._required = False
        return args_schema

    def pre_operations(self):
        self.ctx.args.database_name = "default"


class DatabaseShow(_DatabaseShow):

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.database_name._registered = False
        args_schema.database_name._required = False
        return args_schema

    def pre_operations(self):
        self.ctx.args.database_name = "default"


class DatabaseUpdate(_DatabaseUpdate):

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.database_name._registered = False
        args_schema.database_name._required = False
        return args_schema

    def pre_operations(self):
        self.ctx.args.database_name = "default"


class DatabaseWait(_DatabaseWait):

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.database_name._registered = False
        args_schema.database_name._required = False
        return args_schema

    def pre_operations(self):
        self.ctx.args.database_name = "default"


class DatabaseList(_DatabaseList):

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.database_name._registered = False
        args_schema.database_name._required = False
        return args_schema

    def pre_operations(self):
        self.ctx.args.database_name = "default"


def _get_cluster_with_databases(cluster,
                                databases):
    result = dict(cluster)
    # Restore select null cluster attributes that were removed by cluster.as_dict()
    if 'zones' not in cluster.keys() or cluster['zones'] is None:
        result['zones'] = None

    result['databases'] = []
    for database in databases:
        result['databases'].append(database)
    return result


def redisenterprise_list(cmd,
                         resource_group_name=None):
    if resource_group_name:
        clusters = _ClusterList(cli_ctx=cmd.cli_ctx)(command_args={"resource_group": resource_group_name})
    else:
        clusters = _ClusterList(cli_ctx=cmd.cli_ctx)(command_args={})

    result = []
    for cluster in clusters:
        cluster_resource_group = cluster['id'].split('/')[4]
        databases = _DatabaseList(cli_ctx=cmd.cli_ctx)(command_args={
            "cluster_name": cluster['name'],
            "resource_group": cluster_resource_group})
        result.append(_get_cluster_with_databases(cluster, databases))
    return result


def redisenterprise_show(cmd,
                         resource_group_name,
                         cluster_name):
    cluster = _ClusterShow(cli_ctx=cmd.cli_ctx)(command_args={
        "cluster_name": cluster_name,
        "resource_group": resource_group_name})

    databases = _DatabaseList(cli_ctx=cmd.cli_ctx)(command_args={
        "cluster_name": cluster_name,
        "resource_group": resource_group_name})

    return _get_cluster_with_databases(cluster, databases)


def redisenterprise_create(cmd,
                           resource_group_name,
                           cluster_name,
                           location,
                           sku,
                           tags=None,
                           capacity=None,
                           zones=None,
                           high_availability=None,
                           key_encryption_key_url=None,
                           identity_type=None,
                           user_assigned_identities=None,
                           key_encryption_identity_type=None,
                           user_assigned_identity_resource_id=None,
                           minimum_tls_version=None,
                           client_protocol=None,
                           port=None,
                           clustering_policy=None,
                           eviction_policy=None,
                           persistence=None,
                           modules=None,
                           no_database=False,
                           no_wait=False,
                           group_nickname=None,
                           access_keys_authentication=None,
                           linked_databases=None):
    if (no_database and any(x is not None for x in [client_protocol,
                                                    port,
                                                    clustering_policy,
                                                    eviction_policy,
                                                    persistence,
                                                    modules,
                                                    group_nickname,
                                                    access_keys_authentication,
                                                    linked_databases])):
        database_param_list_str = []
        if client_protocol is not None:
            database_param_list_str.append('--client-protocol')
        if port is not None:
            database_param_list_str.append('--port')
        if clustering_policy is not None:
            database_param_list_str.append('--clustering-policy')
        if eviction_policy is not None:
            database_param_list_str.append('--eviction-policy')
        if persistence is not None:
            database_param_list_str.append('--persistence')
        if modules is not None:
            database_param_list_str.append('--modules')
        if group_nickname is not None:
            database_param_list_str.append('--group-nickname')
        if linked_databases is not None:
            database_param_list_str.append('--linked-databases')
        if access_keys_authentication is not None:
            database_param_list_str.append('--access-keys-auth')
        error_msg = ('--no-database conflicts with the specified database parameter(s): '
                     '{}'.format(', '.join(database_param_list_str)))
        recommendation = ('Try to use --no-database without specifying database parameters, '
                          'or else try removing --no-database')
        raise MutuallyExclusiveArgumentError(error_msg, recommendation)

    from .aaz.latest.redisenterprise import Create as CacheCreate
    from azure.cli.core.commands import LongRunningOperation
    if (no_database and all(x is None for x in [client_protocol,
                                                port,
                                                clustering_policy,
                                                eviction_policy,
                                                persistence,
                                                modules,
                                                group_nickname,
                                                access_keys_authentication,
                                                linked_databases])):
        return CacheCreate(cli_ctx=cmd.cli_ctx)(command_args={
            "cluster_name": cluster_name,
            "resource_group": resource_group_name,
            "location": location,
            "tags": tags,
            "location": location,
            "sku": sku,
            "capacity": capacity,
            "zones": zones,
            "high_availability": high_availability,
            "minimum_tls_version": minimum_tls_version,
            "key_encryption_key_url": key_encryption_key_url,
            "identity_type": identity_type,
            "user_assigned_identities": user_assigned_identities,
            "key_encryption_identity_type": key_encryption_identity_type,
            "user_assigned_identity_resource_id": user_assigned_identity_resource_id,
            "no_wait": no_wait
        })

    poller = CacheCreate(cli_ctx=cmd.cli_ctx)(command_args={
        "cluster_name": cluster_name,
        "resource_group": resource_group_name,
        "location": location,
        "tags": tags,
        "location": location,
        "sku": sku,
        "capacity": capacity,
        "zones": zones,
        "high_availability": high_availability,
        "minimum_tls_version": minimum_tls_version,
        "key_encryption_key_url": key_encryption_key_url,
        "identity_type": identity_type,
        "user_assigned_identities": user_assigned_identities,
        "key_encryption_identity_type": key_encryption_identity_type,
        "user_assigned_identity_resource_id": user_assigned_identity_resource_id,
        "no_wait": no_wait
    })
    if poller:
        LongRunningOperation(cmd.cli_ctx)(poller)
    from .aaz.latest.redisenterprise.database import Create as DatabaseCreate
    return DatabaseCreate(cli_ctx=cmd.cli_ctx)(command_args={
        "cluster_name": cluster_name,
        "resource_group": resource_group_name,
        "client_protocol": client_protocol,
        "port": port,
        "clustering_policy": clustering_policy,
        "eviction_policy": eviction_policy,
        "persistence": persistence,
        "group_nickname": group_nickname,
        "linkeddatabase": linked_databases,
        "access_keys_authentication": access_keys_authentication,
        "mods": modules,
        "database_name": 'default',
        "no_wait": no_wait
    })

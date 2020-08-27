# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from azure.cli.core.util import sdk_no_wait


def account_subscription_list(client):
    return client.list()


def account_subscription_show(client,
                              subscription_id):
    return client.get(subscription_id=subscription_id)


def account_subscription_list_location(client,
                                       subscription_id):
    return client.list_location(subscription_id=subscription_id)


def account_tenant_list(client):
    return client.list()


def account_subscription_cancel(client,
                                subscription_id):
    return client.cancel(subscription_id=subscription_id)


def account_subscription_enable(client,
                                subscription_id):
    return client.enable(subscription_id=subscription_id)


def account_subscription_rename(client,
                                subscription_id,
                                subscription_name=None):
    return client.rename(subscription_id=subscription_id,
                         subscription_name=subscription_name)


def account_alias_list(client):
    return client.list()


def account_alias_show(client,
                       alias_name):
    return client.get(alias_name=alias_name)


def account_alias_create(client,
                         alias_name,
                         properties,
                         no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create,
                       alias_name=alias_name,
                       properties=properties)


def account_alias_delete(client,
                         alias_name):
    return client.delete(alias_name=alias_name)

# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=protected-access

import argparse
from knack.util import CLIError
from collections import defaultdict


class AddVstsConfiguration(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.vsts_configuration = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'project-name':
                d['project_name'] = v[0]
            elif kl == 'tenant-id':
                d['tenant_id'] = v[0]
            elif kl == 'account-name':
                d['account_name'] = v[0]
            elif kl == 'repository-name':
                d['repository_name'] = v[0]
            elif kl == 'collaboration-branch':
                d['collaboration_branch'] = v[0]
            elif kl == 'root-folder':
                d['root_folder'] = v[0]
            elif kl == 'last-commit-id':
                d['last_commit_id'] = v[0]
        d['type'] = 'FactoryVSTSConfiguration'
        return d


class AddGithubConfiguration(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.github_configuration = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'host-name':
                d['host_name'] = v[0]
            elif kl == 'account-name':
                d['account_name'] = v[0]
            elif kl == 'repository-name':
                d['repository_name'] = v[0]
            elif kl == 'collaboration-branch':
                d['collaboration_branch'] = v[0]
            elif kl == 'root-folder':
                d['root_folder'] = v[0]
            elif kl == 'last-commit-id':
                d['last_commit_id'] = v[0]
        d['type'] = 'FactoryGitHubConfiguration'
        return d


class AddFilters(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddFilters, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'operand':
                d['operand'] = v[0]
            elif kl == 'operator':
                d['operator'] = v[0]
            elif kl == 'values':
                d['values'] = v
        return d


class AddOrderBy(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddOrderBy, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'order-by':
                d['order_by'] = v[0]
            elif kl == 'order':
                d['order'] = v[0]
        return d


class AddDebugSettingsSourceSettings(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDebugSettingsSourceSettings, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'source-name':
                d['source_name'] = v[0]
            elif kl == 'row-limit':
                d['row_limit'] = v[0]
        return d


class AddCommandPayload(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.command_payload = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'stream-name':
                d['stream_name'] = v[0]
            elif kl == 'row-limits':
                d['row_limits'] = v[0]
            elif kl == 'columns':
                d['columns'] = v
            elif kl == 'expression':
                d['expression'] = v[0]
        return d

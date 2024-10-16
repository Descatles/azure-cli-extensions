# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_private_link_resource_list
from .example_steps import step_private_link_scope_create
from .example_steps import step_private_link_scope_update
from .example_steps import step_private_link_scope_show
from .example_steps import step_private_link_scope_list
from .example_steps import step_private_link_scope_list2
from .example_steps import step_private_link_scope_update_tag
from .example_steps import step_private_endpoint_connection_update
from .example_steps import step_private_endpoint_connection_list
from .example_steps import step_private_endpoint_connection_show
from .example_steps import step_private_endpoint_connection_delete
from .example_steps import step_private_link_scope_delete
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class PrivateLinkAndPrivateEndpointConnectionScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_privatelink')
    def test_private_link(self):
        rand_string = 'test4'
        self.kwargs.update({
            'machine': 'LAPTOP-S0HSJ7FB',
            'rg': 'ytongtest',
            'scope': 'scope-' + rand_string,
            'vnet': 'vnet-' + rand_string,
            'subnet': 'subnet-' + rand_string,
            'private_endpoint': 'pe-' + rand_string,
            'private_endpoint_connection': 'pec-' + rand_string,
            'location': 'eastus',
            'customScriptName': 'custom-' + rand_string,
        })

        # Prepare network
        self.cmd('az network vnet create -n {vnet} -g {rg} -l {location} --subnet-name {subnet}',
                    checks=self.check('length(newVNet.subnets)', 1))
        self.cmd('az network vnet subnet update -n {subnet} --vnet-name {vnet} -g {rg} '
                    '--disable-private-endpoint-network-policies true',
                    checks=self.check('privateEndpointNetworkPolicies', 'Disabled'))

        #  Create a private link scope
        self.cmd('az connectedmachine private-link-scope create '
                '--location "{location}" '
                '--resource-group "{rg}" '
                '--scope-name "{scope}"',
                checks=[
                    self.check('name','{scope}'),
                    self.check('properties.publicNetworkAccess','Disabled')
                ])

        # Update the private link scope
        self.cmd('az connectedmachine private-link-scope update '
                '--tags Tag1="Value1" '
                '--public-network-access Enabled '
                '--resource-group "{rg}" '
                '--scope-name "{scope}"',
                checks=[
                    self.check('name','{scope}'),
                    self.check('properties.publicNetworkAccess','Enabled')
                ])

        # Test private link scope list 
        self.cmd('az connectedmachine private-link-scope list '
                '--resource-group "{rg}"',
                checks=[])

        # Private link scope update tag
        self.cmd('az connectedmachine private-link-scope update-tag '
                '--tags Tag1="Value1" Tag2="Value2" '
                '--resource-group "{rg}" '
                '--scope-name "{scope}"',
                checks=[
                    self.check('length(tags)', 2)
                ])

        # Private link scope show
        private_link_scope = self.cmd('az connectedmachine private-link-scope show --scope-name {scope} -g {rg}').get_output_in_json()
        self.kwargs['scope_id'] = private_link_scope['id']

        # Test private link resource show
        self.cmd('az connectedmachine private-link-resource show --scope-name {scope} -g {rg} --group-name hybridcompute', checks=[
            # self.check('length(@)', 6)
        ])

        # Test private link resource list
        self.cmd('az connectedmachine private-link-resource list --scope-name {scope} -g {rg}', checks=[])
        
        # DO NOT remove --location, otherwise it will print out an error saying vnet-test not found
        result = self.cmd('az network private-endpoint create -g {rg} -n {private_endpoint} --vnet-name {vnet} --subnet {subnet} --private-connection-resource-id {scope_id} '
        '--connection-name {private_endpoint_connection} --group-id hybridcompute --location {location}').get_output_in_json()
        self.assertTrue(self.kwargs['private_endpoint'].lower() in result['name'].lower())

        connection_list = self.cmd('az connectedmachine private-endpoint-connection list '
                '--resource-group "{rg}" '
                '--scope-name "{scope}"').get_output_in_json()
        self.kwargs['private_endpoint_connection_name'] = connection_list[0]['name']

        self.cmd('az connectedmachine private-endpoint-connection update '
                '--description "Rejected by AZ CLI" '
                '--status "Rejected" '
                '--name "{private_endpoint_connection_name}" '
                '--resource-group "{rg}" '
                '--scope-name "{scope}"',
                checks=[
                    self.check('name', '{private_endpoint_connection_name}'),
                    self.check('properties.privateLinkServiceConnectionState.description', 'Rejected by AZ CLI'),
                    self.check('properties.privateLinkServiceConnectionState.status', 'Rejected')
                ])

        self.cmd('az connectedmachine private-endpoint-connection show '
                '--name "{private_endpoint_connection_name}" '
                '--resource-group "{rg}" '
                '--scope-name "{scope}"',
                checks=[
                    self.check('name', '{private_endpoint_connection_name}'),
                    self.check('properties.privateLinkServiceConnectionState.description', 'Rejected by AZ CLI'),
                    self.check('properties.privateLinkServiceConnectionState.status', 'Rejected')
                ])
        
        self.cmd('az connectedmachine private-endpoint-connection delete -y '
                '--name "{private_endpoint_connection_name}" '
                '--resource-group "{rg}" '
                '--scope-name "{scope}"',
                checks=[])
        
        self.cmd('az connectedmachine private-endpoint-connection list '
                '--resource-group "{rg}" '
                '--scope-name "{scope}"',
                checks=[
                    self.check('length(@)', 0)
                ])

        self.cmd('az connectedmachine private-link-scope delete -y '
                '--resource-group "{rg}" '
                '--scope-name "{scope}"',
                checks=[])
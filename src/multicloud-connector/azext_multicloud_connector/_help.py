# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-lines

from knack.help_files import helps  # pylint: disable=unused-import

helps['arc-multicloud generate-aws-template'] = """
    type: command
    short-summary: Retrieve AWS Cloud Formation template
    parameters:
      - name: --connector-id
        short-summary: "The fully qualified Azure Resource manager identifier of the public cloud connector"
    examples:
      - name: GenerateAwsTemplate_Post
        text: |-
               az arc-multicloud generate-aws-template --connector-id /subscriptions/{}/resourceGroups/{}/providers/Microsoft.HybridConnectivity/publicCloudConnectors/{} --output-directory example_folder/templates
"""

# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

from ._configuration import AzureDevOpsConfiguration
from .operations import OperationOperations
from .operations import PipelineTemplateDefinitionOperations
from .operations import PipelineOperations
from . import models


class AzureDevOps(object):
    """Azure DevOps Resource Provider.

    :ivar operation: OperationOperations operations
    :vartype operation: azure.mgmt.devops.operations.OperationOperations
    :ivar pipeline_template_definition: PipelineTemplateDefinitionOperations operations
    :vartype pipeline_template_definition: azure.mgmt.devops.operations.PipelineTemplateDefinitionOperations
    :ivar pipeline: PipelineOperations operations
    :vartype pipeline: azure.mgmt.devops.operations.PipelineOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = AzureDevOpsConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.pipeline_template_definition = PipelineTemplateDefinitionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.pipeline = PipelineOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AzureDevOps
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)

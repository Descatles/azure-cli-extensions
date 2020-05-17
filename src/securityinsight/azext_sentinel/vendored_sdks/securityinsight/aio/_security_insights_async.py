# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import SecurityInsightsConfiguration
from .operations_async import OperationOperations
from .operations_async import AlertRuleOperations
from .operations_async import ActionOperations
from .operations_async import AlertRuleTemplateOperations
from .operations_async import BookmarkOperations
from .operations_async import DataConnectorOperations
from .operations_async import IncidentOperations
from .operations_async import IncidentCommentOperations
from .. import models


class SecurityInsights(object):
    """API spec for Microsoft.SecurityInsights (Azure Security Insights) resource provider.

    :ivar operation: OperationOperations operations
    :vartype operation: azure.mgmt.securityinsight.aio.operations_async.OperationOperations
    :ivar alert_rule: AlertRuleOperations operations
    :vartype alert_rule: azure.mgmt.securityinsight.aio.operations_async.AlertRuleOperations
    :ivar action: ActionOperations operations
    :vartype action: azure.mgmt.securityinsight.aio.operations_async.ActionOperations
    :ivar alert_rule_template: AlertRuleTemplateOperations operations
    :vartype alert_rule_template: azure.mgmt.securityinsight.aio.operations_async.AlertRuleTemplateOperations
    :ivar bookmark: BookmarkOperations operations
    :vartype bookmark: azure.mgmt.securityinsight.aio.operations_async.BookmarkOperations
    :ivar data_connector: DataConnectorOperations operations
    :vartype data_connector: azure.mgmt.securityinsight.aio.operations_async.DataConnectorOperations
    :ivar incident: IncidentOperations operations
    :vartype incident: azure.mgmt.securityinsight.aio.operations_async.IncidentOperations
    :ivar incident_comment: IncidentCommentOperations operations
    :vartype incident_comment: azure.mgmt.securityinsight.aio.operations_async.IncidentCommentOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = SecurityInsightsConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.alert_rule = AlertRuleOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.action = ActionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.alert_rule_template = AlertRuleTemplateOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.bookmark = BookmarkOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_connector = DataConnectorOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.incident = IncidentOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.incident_comment = IncidentCommentOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "SecurityInsights":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)

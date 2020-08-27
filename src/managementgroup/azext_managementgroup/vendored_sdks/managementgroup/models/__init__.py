# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AzureAsyncOperationResults
    from ._models_py3 import CheckNameAvailabilityRequest
    from ._models_py3 import CheckNameAvailabilityResult
    from ._models_py3 import CreateManagementGroupChildInfo
    from ._models_py3 import CreateManagementGroupRequest
    from ._models_py3 import CreateOrUpdateSettingsRequest
    from ._models_py3 import DescendantInfo
    from ._models_py3 import DescendantListResult
    from ._models_py3 import DescendantParentGroupInfo
    from ._models_py3 import EntityHierarchyItem
    from ._models_py3 import EntityInfo
    from ._models_py3 import EntityListResult
    from ._models_py3 import EntityParentGroupInfo
    from ._models_py3 import ErrorDetails
    from ._models_py3 import ErrorResponse
    from ._models_py3 import HierarchySettings
    from ._models_py3 import HierarchySettingsInfo
    from ._models_py3 import HierarchySettingsList
    from ._models_py3 import ListSubscriptionUnderManagementGroup
    from ._models_py3 import ManagementGroup
    from ._models_py3 import ManagementGroupChildInfo
    from ._models_py3 import ManagementGroupDetails
    from ._models_py3 import ManagementGroupInfo
    from ._models_py3 import ManagementGroupListResult
    from ._models_py3 import ManagementGroupPathElement
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplayProperties
    from ._models_py3 import OperationListResult
    from ._models_py3 import OperationResults
    from ._models_py3 import ParentGroupInfo
    from ._models_py3 import PatchManagementGroupRequest
    from ._models_py3 import SubscriptionUnderManagementGroup
    from ._models_py3 import TenantBackfillStatusResult
except (SyntaxError, ImportError):
    from ._models import AzureAsyncOperationResults  # type: ignore
    from ._models import CheckNameAvailabilityRequest  # type: ignore
    from ._models import CheckNameAvailabilityResult  # type: ignore
    from ._models import CreateManagementGroupChildInfo  # type: ignore
    from ._models import CreateManagementGroupRequest  # type: ignore
    from ._models import CreateOrUpdateSettingsRequest  # type: ignore
    from ._models import DescendantInfo  # type: ignore
    from ._models import DescendantListResult  # type: ignore
    from ._models import DescendantParentGroupInfo  # type: ignore
    from ._models import EntityHierarchyItem  # type: ignore
    from ._models import EntityInfo  # type: ignore
    from ._models import EntityListResult  # type: ignore
    from ._models import EntityParentGroupInfo  # type: ignore
    from ._models import ErrorDetails  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import HierarchySettings  # type: ignore
    from ._models import HierarchySettingsInfo  # type: ignore
    from ._models import HierarchySettingsList  # type: ignore
    from ._models import ListSubscriptionUnderManagementGroup  # type: ignore
    from ._models import ManagementGroup  # type: ignore
    from ._models import ManagementGroupChildInfo  # type: ignore
    from ._models import ManagementGroupDetails  # type: ignore
    from ._models import ManagementGroupInfo  # type: ignore
    from ._models import ManagementGroupListResult  # type: ignore
    from ._models import ManagementGroupPathElement  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplayProperties  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import OperationResults  # type: ignore
    from ._models import ParentGroupInfo  # type: ignore
    from ._models import PatchManagementGroupRequest  # type: ignore
    from ._models import SubscriptionUnderManagementGroup  # type: ignore
    from ._models import TenantBackfillStatusResult  # type: ignore

from ._management_groups_api_enums import (
    Enum0,
    Enum2,
    Enum3,
    Enum5,
    ManagementGroupChildType,
    Permissions,
    Reason,
    Status,
)

__all__ = [
    'AzureAsyncOperationResults',
    'CheckNameAvailabilityRequest',
    'CheckNameAvailabilityResult',
    'CreateManagementGroupChildInfo',
    'CreateManagementGroupRequest',
    'CreateOrUpdateSettingsRequest',
    'DescendantInfo',
    'DescendantListResult',
    'DescendantParentGroupInfo',
    'EntityHierarchyItem',
    'EntityInfo',
    'EntityListResult',
    'EntityParentGroupInfo',
    'ErrorDetails',
    'ErrorResponse',
    'HierarchySettings',
    'HierarchySettingsInfo',
    'HierarchySettingsList',
    'ListSubscriptionUnderManagementGroup',
    'ManagementGroup',
    'ManagementGroupChildInfo',
    'ManagementGroupDetails',
    'ManagementGroupInfo',
    'ManagementGroupListResult',
    'ManagementGroupPathElement',
    'Operation',
    'OperationDisplayProperties',
    'OperationListResult',
    'OperationResults',
    'ParentGroupInfo',
    'PatchManagementGroupRequest',
    'SubscriptionUnderManagementGroup',
    'TenantBackfillStatusResult',
    'Enum0',
    'Enum2',
    'Enum3',
    'Enum5',
    'ManagementGroupChildType',
    'Permissions',
    'Reason',
    'Status',
]

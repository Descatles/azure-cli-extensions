# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class IncidentCommentOperations(object):
    """IncidentCommentOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.securityinsight.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_by_incident(
        self,
        resource_group_name,  # type: str
        workspace_name,  # type: str
        incident_id,  # type: str
        filter=None,  # type: Optional[str]
        orderby=None,  # type: Optional[str]
        top=None,  # type: Optional[int]
        skip_token=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.IncidentCommentList"
        """Gets all incident comments.

        :param resource_group_name: The name of the resource group within the user's subscription. The
     name is case insensitive.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param incident_id: Incident ID.
        :type incident_id: str
        :param filter: Filters the results, based on a Boolean condition. Optional.
        :type filter: str
        :param orderby: Sorts the results. Optional.
        :type orderby: str
        :param top: Returns only the first n results. Optional.
        :type top: int
        :param skip_token: Skiptoken is only used if a previous operation returned a partial result. If
     a previous response contains a nextLink element, the value of the nextLink element will include
     a skiptoken parameter that specifies a starting point to use for subsequent calls. Optional.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IncidentCommentList or the result of cls(response)
        :rtype: ~azure.mgmt.securityinsight.models.IncidentCommentList
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.IncidentCommentList"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2020-01-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_incident.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', pattern=r'^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                    'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', max_length=90, min_length=1),
                    'incidentId': self._serialize.url("incident_id", incident_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
            if filter is not None:
                query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
            if orderby is not None:
                query_parameters['$orderby'] = self._serialize.query("orderby", orderby, 'str')
            if top is not None:
                query_parameters['$top'] = self._serialize.query("top", top, 'int')
            if skip_token is not None:
                query_parameters['$skipToken'] = self._serialize.query("skip_token", skip_token, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('IncidentCommentList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_incident.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/incidents/{incidentId}/comments'}

    def get_comment(
        self,
        resource_group_name,  # type: str
        workspace_name,  # type: str
        incident_id,  # type: str
        incident_comment_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.IncidentComment"
        """Gets an incident comment.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param incident_id: Incident ID.
        :type incident_id: str
        :param incident_comment_id: Incident comment ID.
        :type incident_comment_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IncidentComment or the result of cls(response)
        :rtype: ~azure.mgmt.securityinsight.models.IncidentComment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.IncidentComment"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2020-01-01"

        # Construct URL
        url = self.get_comment.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', pattern=r'^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', max_length=90, min_length=1),
            'incidentId': self._serialize.url("incident_id", incident_id, 'str'),
            'incidentCommentId': self._serialize.url("incident_comment_id", incident_comment_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('IncidentComment', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_comment.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/incidents/{incidentId}/comments/{incidentCommentId}'}

    def create_comment(
        self,
        resource_group_name,  # type: str
        workspace_name,  # type: str
        incident_id,  # type: str
        incident_comment_id,  # type: str
        message=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.IncidentComment"
        """Creates the incident comment.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param incident_id: Incident ID.
        :type incident_id: str
        :param incident_comment_id: Incident comment ID.
        :type incident_comment_id: str
        :param message: The comment message.
        :type message: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IncidentComment or the result of cls(response)
        :rtype: ~azure.mgmt.securityinsight.models.IncidentComment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.IncidentComment"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _incident_comment = models.IncidentComment(message=message)
        api_version = "2020-01-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_comment.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', pattern=r'^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', max_length=90, min_length=1),
            'incidentId': self._serialize.url("incident_id", incident_id, 'str'),
            'incidentCommentId': self._serialize.url("incident_comment_id", incident_comment_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_incident_comment, 'IncidentComment')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('IncidentComment', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create_comment.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/incidents/{incidentId}/comments/{incidentCommentId}'}

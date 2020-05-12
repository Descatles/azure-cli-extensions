# Azure CLI Module Creation Report

### automation activity list

list a automation activity.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--module-name**|string|The name of module.|module_name|
### automation activity show

show a automation activity.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--module-name**|string|The name of module.|module_name|
|**--activity-name**|string|The name of activity.|activity_name|
### automation agent-registration-information regenerate-key

regenerate-key a automation agent-registration-information.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--key-name**|choice|Gets or sets the agent registration key name - primary or secondary.|key_name|
### automation agent-registration-information show

show a automation agent-registration-information.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
### automation automation-account create

create a automation automation-account.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--name**|string|Gets or sets name of the resource.|name|
|**--location**|string|Gets or sets the location of the resource.|location|
|**--tags**|dictionary|Gets or sets the tags attached to the resource.|tags|
|**--sku**|object|Gets or sets account SKU.|sku|
### automation automation-account delete

delete a automation automation-account.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
### automation automation-account list

list a automation automation-account.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
### automation automation-account show

show a automation automation-account.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
### automation automation-account update

update a automation automation-account.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--name**|string|Gets or sets the name of the resource.|name|
|**--location**|string|Gets or sets the location of the resource.|location|
|**--tags**|dictionary|Gets or sets the tags attached to the resource.|tags|
|**--sku**|object|Gets or sets account SKU.|sku|
### automation certificate create

create a automation certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--certificate-name**|string|The parameters supplied to the create or update certificate operation.|certificate_name|
|**--name**|string|Gets or sets the name of the certificate.|name|
|**--base64value**|string|Gets or sets the base64 encoded value of the certificate.|base64_value|
|**--description**|string|Gets or sets the description of the certificate.|description|
|**--thumbprint**|string|Gets or sets the thumbprint of the certificate.|thumbprint|
|**--is-exportable**|boolean|Gets or sets the is exportable flag of the certificate.|is_exportable|
### automation certificate delete

delete a automation certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--certificate-name**|string|The name of certificate.|certificate_name|
### automation certificate list

list a automation certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
### automation certificate show

show a automation certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--certificate-name**|string|The name of certificate.|certificate_name|
### automation certificate update

update a automation certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--certificate-name**|string|The parameters supplied to the update certificate operation.|certificate_name|
|**--name**|string|Gets or sets the name of the certificate.|name|
|**--description**|string|Gets or sets the description of the certificate.|description|
### automation connection create

create a automation connection.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--connection-name**|string|The parameters supplied to the create or update connection operation.|connection_name|
|**--name**|string|Gets or sets the name of the connection.|name|
|**--connection-type**|object|Gets or sets the connectionType of the connection.|connection_type|
|**--description**|string|Gets or sets the description of the connection.|description|
|**--field-definition-values**|dictionary|Gets or sets the field definition properties of the connection.|field_definition_values|
### automation connection delete

delete a automation connection.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--connection-name**|string|The name of connection.|connection_name|
### automation connection list

list a automation connection.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
### automation connection show

show a automation connection.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--connection-name**|string|The name of connection.|connection_name|
### automation connection update

update a automation connection.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--connection-name**|string|The parameters supplied to the update a connection operation.|connection_name|
|**--name**|string|Gets or sets the name of the connection.|name|
|**--description**|string|Gets or sets the description of the connection.|description|
|**--field-definition-values**|dictionary|Gets or sets the field definition values of the connection.|field_definition_values|
### automation connection-type create

create a automation connection-type.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--connection-type-name**|string|The parameters supplied to the create or update connection type operation.|connection_type_name|
|**--name**|string|Gets or sets the name of the connection type.|name|
|**--field-definitions**|dictionary|Gets or sets the field definitions of the connection type.|field_definitions|
|**--is-global**|boolean|Gets or sets a Boolean value to indicate if the connection type is global.|is_global|
### automation connection-type delete

delete a automation connection-type.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--connection-type-name**|string|The name of connection type.|connection_type_name|
### automation connection-type list

list a automation connection-type.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
### automation connection-type show

show a automation connection-type.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--connection-type-name**|string|The name of connection type.|connection_type_name|
### automation connection-type update

create a automation connection-type.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--connection-type-name**|string|The parameters supplied to the create or update connection type operation.|connection_type_name|
|**--name**|string|Gets or sets the name of the connection type.|name|
|**--field-definitions**|dictionary|Gets or sets the field definitions of the connection type.|field_definitions|
|**--is-global**|boolean|Gets or sets a Boolean value to indicate if the connection type is global.|is_global|
### automation credential create

create a automation credential.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--credential-name**|string|The parameters supplied to the create or update credential operation.|credential_name|
|**--name**|string|Gets or sets the name of the credential.|name|
|**--user-name**|string|Gets or sets the user name of the credential.|user_name|
|**--password**|string|Gets or sets the password of the credential.|password|
|**--description**|string|Gets or sets the description of the credential.|description|
### automation credential delete

delete a automation credential.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--credential-name**|string|The name of credential.|credential_name|
### automation credential list

list a automation credential.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
### automation credential show

show a automation credential.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--credential-name**|string|The name of credential.|credential_name|
### automation credential update

update a automation credential.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--credential-name**|string|The parameters supplied to the Update credential operation.|credential_name|
|**--name**|string|Gets or sets the name of the credential.|name|
|**--user-name**|string|Gets or sets the user name of the credential.|user_name|
|**--password**|string|Gets or sets the password of the credential.|password|
|**--description**|string|Gets or sets the description of the credential.|description|
### automation dsc-compilation-job create

create a automation dsc-compilation-job.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--compilation-job-name**|string|The DSC configuration Id.|compilation_job_name|
|**--configuration**|object|Gets or sets the configuration.|configuration|
|**--name**|string|Gets or sets name of the resource.|name|
|**--location**|string|Gets or sets the location of the resource.|location|
|**--tags**|dictionary|Gets or sets the tags attached to the resource.|tags|
|**--parameters**|dictionary|Gets or sets the parameters of the job.|parameters|
|**--increment-node-configuration-build**|boolean|If a new build version of NodeConfiguration is required.|increment_node_configuration_build|
### automation dsc-compilation-job list

list a automation dsc-compilation-job.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--filter**|string|The filter to apply on the operation.|filter|
### automation dsc-compilation-job show

show a automation dsc-compilation-job.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--job-id**|uuid|The job id.|job_id|
|**--job-stream-id**|string|The job stream id.|job_stream_id|
|**--compilation-job-name**|string|The DSC configuration Id.|compilation_job_name|
### automation dsc-compilation-job-stream list

list a automation dsc-compilation-job-stream.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--job-id**|uuid|The job id.|job_id|
### automation dsc-configuration create

create a automation dsc-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--configuration-name**|string|The create or update parameters for configuration.|configuration_name|
|**--source**|object|Gets or sets the source.|source|
|**--name**|string|Gets or sets name of the resource.|name|
|**--location**|string|Gets or sets the location of the resource.|location|
|**--tags**|dictionary|Gets or sets the tags attached to the resource.|tags|
|**--log-verbose**|boolean|Gets or sets verbose log option.|log_verbose|
|**--log-progress**|boolean|Gets or sets progress log option.|log_progress|
|**--parameters**|dictionary|Gets or sets the configuration parameters.|parameters|
|**--description**|string|Gets or sets the description of the configuration.|description|
### automation dsc-configuration delete

delete a automation dsc-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--configuration-name**|string|The configuration name.|configuration_name|
### automation dsc-configuration list

list a automation dsc-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--filter**|string|The filter to apply on the operation.|filter|
|**--skip**|integer|The number of rows to skip.|skip|
|**--top**|integer|The number of rows to take.|top|
|**--inlinecount**|string|Return total rows.|inlinecount|
### automation dsc-configuration show

show a automation dsc-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--configuration-name**|string|The configuration name.|configuration_name|
### automation dsc-configuration update

update a automation dsc-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--configuration-name**|string|The create or update parameters for configuration.|configuration_name|
|**--name**|string|Gets or sets name of the resource.|name|
|**--tags**|dictionary|Gets or sets the tags attached to the resource.|tags|
|**--log-verbose**|boolean|Gets or sets verbose log option.|log_verbose|
|**--log-progress**|boolean|Gets or sets progress log option.|log_progress|
|**--source**|object|Gets or sets the source.|source|
|**--parameters**|dictionary|Gets or sets the configuration parameters.|parameters|
|**--description**|string|Gets or sets the description of the configuration.|description|
### automation dsc-node delete

delete a automation dsc-node.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--node-id**|string|The node id.|node_id|
### automation dsc-node list

list a automation dsc-node.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--filter**|string|The filter to apply on the operation.|filter|
|**--skip**|integer|The number of rows to skip.|skip|
|**--top**|integer|The number of rows to take.|top|
|**--inlinecount**|string|Return total rows.|inlinecount|
### automation dsc-node show

show a automation dsc-node.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--node-id**|string|The node id.|node_id|
### automation dsc-node update

update a automation dsc-node.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--node-id**|string|Parameters supplied to the update dsc node.|node_id|
|**--node-id**|string|Gets or sets the id of the dsc node.|node_id|
|**--node-configuration-name**|string|Gets or sets the name of the dsc node configuration.|name_properties_node_configuration_name|
### automation dsc-node-configuration create

create a automation dsc-node-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--node-configuration-name**|string|The Dsc node configuration name.|node_configuration_name|
|**--name**|string|Name of the node configuration.|name|
|**--tags**|dictionary|Gets or sets the tags attached to the resource.|tags|
|**--source**|object|Gets or sets the source.|source|
|**--configuration**|object|Gets or sets the configuration of the node.|configuration|
|**--increment-node-configuration-build**|boolean|If a new build version of NodeConfiguration is required.|increment_node_configuration_build|
### automation dsc-node-configuration delete

delete a automation dsc-node-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--node-configuration-name**|string|The Dsc node configuration name.|node_configuration_name|
### automation dsc-node-configuration list

list a automation dsc-node-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--filter**|string|The filter to apply on the operation.|filter|
|**--skip**|integer|The number of rows to skip.|skip|
|**--top**|integer|The number of rows to take.|top|
|**--inlinecount**|string|Return total rows.|inlinecount|
### automation dsc-node-configuration show

show a automation dsc-node-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--node-configuration-name**|string|The Dsc node configuration name.|node_configuration_name|
### automation dsc-node-configuration update

create a automation dsc-node-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--node-configuration-name**|string|The Dsc node configuration name.|node_configuration_name|
|**--name**|string|Name of the node configuration.|name|
|**--tags**|dictionary|Gets or sets the tags attached to the resource.|tags|
|**--source**|object|Gets or sets the source.|source|
|**--configuration**|object|Gets or sets the configuration of the node.|configuration|
|**--increment-node-configuration-build**|boolean|If a new build version of NodeConfiguration is required.|increment_node_configuration_build|
### automation field list

list a automation field.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--module-name**|string|The name of module.|module_name|
|**--type-name**|string|The name of type.|type_name|
### automation hybrid-runbook-worker-group delete

delete a automation hybrid-runbook-worker-group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--hybrid-runbook-worker-group-name**|string|The hybrid runbook worker group name|hybrid_runbook_worker_group_name|
### automation hybrid-runbook-worker-group list

list a automation hybrid-runbook-worker-group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--filter**|string|The filter to apply on the operation.|filter|
### automation hybrid-runbook-worker-group show

show a automation hybrid-runbook-worker-group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--hybrid-runbook-worker-group-name**|string|The hybrid runbook worker group name|hybrid_runbook_worker_group_name|
### automation hybrid-runbook-worker-group update

update a automation hybrid-runbook-worker-group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--hybrid-runbook-worker-group-name**|string|The hybrid runbook worker group name|hybrid_runbook_worker_group_name|
|**--credential**|object|Sets the credential of a worker group.|credential|
### automation job create

create a automation job.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--job-name**|string|The job name.|job_name|
|**--client-request-id**|string|Identifies this specific client request.|client_request_id|
|**--runbook**|object|Gets or sets the runbook.|runbook|
|**--parameters**|dictionary|Gets or sets the parameters of the job.|parameters|
|**--run-on**|string|Gets or sets the runOn which specifies the group name where the job is to be executed.|run_on|
### automation job list

list a automation job.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--filter**|string|The filter to apply on the operation.|filter|
|**--client-request-id**|string|Identifies this specific client request.|client_request_id|
### automation job resume

resume a automation job.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--job-name**|string|The job name.|job_name|
|**--client-request-id**|string|Identifies this specific client request.|client_request_id|
### automation job show

show a automation job.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--job-name**|string|The name of the job to be created.|job_name|
|**--client-request-id**|string|Identifies this specific client request.|client_request_id|
### automation job stop

stop a automation job.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--job-name**|string|The job name.|job_name|
|**--client-request-id**|string|Identifies this specific client request.|client_request_id|
### automation job suspend

suspend a automation job.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--job-name**|string|The job name.|job_name|
|**--client-request-id**|string|Identifies this specific client request.|client_request_id|
### automation job-schedule create

create a automation job-schedule.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--job-schedule-id**|uuid|The job schedule name.|job_schedule_id|
|**--schedule**|object|Gets or sets the schedule.|schedule|
|**--runbook**|object|Gets or sets the runbook.|runbook|
|**--run-on**|string|Gets or sets the hybrid worker group that the scheduled job should run on.|run_on|
|**--parameters**|dictionary|Gets or sets a list of job properties.|parameters|
### automation job-schedule delete

delete a automation job-schedule.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--job-schedule-id**|uuid|The job schedule name.|job_schedule_id|
### automation job-schedule list

list a automation job-schedule.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--filter**|string|The filter to apply on the operation.|filter|
### automation job-schedule show

show a automation job-schedule.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--job-schedule-id**|uuid|The job schedule name.|job_schedule_id|
### automation job-stream list

list a automation job-stream.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--job-name**|string|The job name.|job_name|
|**--filter**|string|The filter to apply on the operation.|filter|
|**--client-request-id**|string|Identifies this specific client request.|client_request_id|
### automation job-stream show

show a automation job-stream.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--job-name**|string|The job name.|job_name|
|**--job-stream-id**|string|The job stream id.|job_stream_id|
|**--client-request-id**|string|Identifies this specific client request.|client_request_id|
### automation key list-by-automation-account

list-by-automation-account a automation key.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
### automation linked-workspace show

show a automation linked-workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
### automation module create

create a automation module.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--module-name**|string|The name of module.|module_name|
|**--content-link**|object|Gets or sets the module content link.|content_link|
|**--name**|string|Gets or sets name of the resource.|name|
|**--location**|string|Gets or sets the location of the resource.|location|
|**--tags**|dictionary|Gets or sets the tags attached to the resource.|tags|
### automation module delete

delete a automation module.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--module-name**|string|The module name.|module_name|
### automation module list

list a automation module.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
### automation module show

show a automation module.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--module-name**|string|The module name.|module_name|
### automation module update

update a automation module.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--module-name**|string|The name of module.|module_name|
|**--name**|string|Gets or sets name of the resource.|name|
|**--location**|string|Gets or sets the location of the resource.|location|
|**--tags**|dictionary|Gets or sets the tags attached to the resource.|tags|
|**--content-link**|object|Gets or sets the module content link.|content_link|
### automation node-count-information show

show a automation node-count-information.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--count-type**|choice|The type of counts to retrieve|count_type|
### automation node-report list

list a automation node-report.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--node-id**|string|The parameters supplied to the list operation.|node_id|
|**--filter**|string|The filter to apply on the operation.|filter|
### automation node-report show

show a automation node-report.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--node-id**|string|The Dsc node id.|node_id|
|**--report-id**|string|The report id.|report_id|
### automation object-data-type list-field

list-field a automation object-data-type.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--module-name**|string|The name of module.|module_name|
|**--type-name**|string|The name of type.|type_name|
### automation python2-package create

create a automation python2-package.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--package-name**|string|The name of python package.|package_name|
|**--content-link**|object|Gets or sets the module content link.|content_link|
|**--tags**|dictionary|Gets or sets the tags attached to the resource.|tags|
### automation python2-package delete

delete a automation python2-package.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--package-name**|string|The python package name.|package_name|
### automation python2-package list

list a automation python2-package.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
### automation python2-package show

show a automation python2-package.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--package-name**|string|The python package name.|package_name|
### automation python2-package update

update a automation python2-package.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--package-name**|string|The name of python package.|package_name|
|**--tags**|dictionary|Gets or sets the tags attached to the resource.|tags|
### automation runbook create

create a automation runbook.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--runbook-name**|string|The runbook name.|runbook_name|
|**--runbook-type**|choice|Gets or sets the type of the runbook.|runbook_type|
|**--name**|string|Gets or sets the name of the resource.|name|
|**--location**|string|Gets or sets the location of the resource.|location|
|**--tags**|dictionary|Gets or sets the tags attached to the resource.|tags|
|**--log-verbose**|boolean|Gets or sets verbose log option.|log_verbose|
|**--log-progress**|boolean|Gets or sets progress log option.|log_progress|
|**--draft**|object|Gets or sets the draft runbook properties.|draft|
|**--publish-content-link**|object|Gets or sets the published runbook content link.|publish_content_link|
|**--description**|string|Gets or sets the description of the runbook.|description|
|**--log-activity-trace**|integer|Gets or sets the activity-level tracing options of the runbook.|log_activity_trace|
### automation runbook delete

delete a automation runbook.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--runbook-name**|string|The runbook name.|runbook_name|
### automation runbook list

list a automation runbook.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
### automation runbook publish

publish a automation runbook.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--runbook-name**|string|The parameters supplied to the publish runbook operation.|runbook_name|
### automation runbook show

show a automation runbook.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--runbook-name**|string|The runbook name.|runbook_name|
### automation runbook update

update a automation runbook.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--runbook-name**|string|The runbook name.|runbook_name|
|**--name**|string|Gets or sets the name of the resource.|name|
|**--location**|string|Gets or sets the location of the resource.|location|
|**--tags**|dictionary|Gets or sets the tags attached to the resource.|tags|
|**--description**|string|Gets or sets the description of the runbook.|description|
|**--log-verbose**|boolean|Gets or sets verbose log option.|log_verbose|
|**--log-progress**|boolean|Gets or sets progress log option.|log_progress|
|**--log-activity-trace**|integer|Gets or sets the activity-level tracing options of the runbook.|log_activity_trace|
### automation runbook-draft replace-content

replace-content a automation runbook-draft.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--runbook-name**|string|The runbook name.|runbook_name|
|**--runbook-content**|string|The runbook draft content.|runbook_content|
### automation runbook-draft show

show a automation runbook-draft.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--runbook-name**|string|The runbook name.|runbook_name|
### automation runbook-draft undo-edit

undo-edit a automation runbook-draft.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--runbook-name**|string|The runbook name.|runbook_name|
### automation schedule create

create a automation schedule.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--schedule-name**|string|The schedule name.|schedule_name|
|**--name**|string|Gets or sets the name of the Schedule.|name|
|**--start-time**|date-time|Gets or sets the start time of the schedule.|start_time|
|**--frequency**|choice|Gets or sets the frequency of the schedule.|frequency|
|**--description**|string|Gets or sets the description of the schedule.|description|
|**--expiry-time**|date-time|Gets or sets the end time of the schedule.|expiry_time|
|**--interval**|any|Gets or sets the interval of the schedule.|interval|
|**--time-zone**|string|Gets or sets the time zone of the schedule.|time_zone|
|**--advanced-schedule-week-days**|array|Days of the week that the job should execute on.|week_days|
|**--advanced-schedule-month-days**|array|Days of the month that the job should execute on. Must be between 1 and 31.|month_days|
|**--advanced-schedule-monthly-occurrences**|array|Occurrences of days within a month.|monthly_occurrences|
### automation schedule delete

delete a automation schedule.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--schedule-name**|string|The schedule name.|schedule_name|
### automation schedule list

list a automation schedule.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
### automation schedule show

show a automation schedule.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--schedule-name**|string|The schedule name.|schedule_name|
### automation schedule update

update a automation schedule.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--schedule-name**|string|The schedule name.|schedule_name|
|**--name**|string|Gets or sets the name of the Schedule.|name|
|**--description**|string|Gets or sets the description of the schedule.|description|
|**--is-enabled**|boolean|Gets or sets a value indicating whether this schedule is enabled.|is_enabled|
### automation software-update-configuration create

create a automation software-update-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--software-update-configuration-name**|string|The name of the software update configuration to be created.|software_update_configuration_name|
|**--update-configuration-operating-system**|sealed-choice|operating system of target machines|operating_system|
|**--client-request-id**|string|Identifies this specific client request.|client_request_id|
|**--error**|object|Details of provisioning error|error|
|**--tasks-post-task-parameters**|dictionary|Gets or sets the parameters of the task.|parameters_properties_tasks_post_task_parameters|
|**--tasks-post-task-source**|string|Gets or sets the name of the runbook.|source_properties_tasks_post_task_source|
|**--tasks-pre-task-parameters**|dictionary|Gets or sets the parameters of the task.|parameters_properties_tasks_post_task_parameters|
|**--tasks-pre-task-source**|string|Gets or sets the name of the runbook.|source_properties_tasks_post_task_source|
|**--schedule-info-start-time**|date-time|Gets or sets the start time of the schedule.|start_time|
|**--schedule-info-expiry-time**|date-time|Gets or sets the end time of the schedule.|expiry_time|
|**--schedule-info-expiry-time-offset-minutes**|number|Gets or sets the expiry time's offset in minutes.|expiry_time_offset_minutes|
|**--schedule-info-is-enabled**|boolean|Gets or sets a value indicating whether this schedule is enabled.|is_enabled|
|**--schedule-info-next-run**|date-time|Gets or sets the next run time of the schedule.|next_run|
|**--schedule-info-next-run-offset-minutes**|number|Gets or sets the next run time's offset in minutes.|next_run_offset_minutes|
|**--schedule-info-interval**|integer|Gets or sets the interval of the schedule.|interval|
|**--schedule-info-frequency**|choice|Gets or sets the frequency of the schedule.|frequency|
|**--schedule-info-time-zone**|string|Gets or sets the time zone of the schedule.|time_zone|
|**--schedule-info-creation-time**|date-time|Gets or sets the creation time.|creation_time|
|**--schedule-info-last-modified-time**|date-time|Gets or sets the last modified time.|last_modified_time|
|**--schedule-info-description**|string|Gets or sets the description.|description|
|**--schedule-info-advanced-schedule-week-days**|array|Days of the week that the job should execute on.|week_days|
|**--schedule-info-advanced-schedule-month-days**|array|Days of the month that the job should execute on. Must be between 1 and 31.|month_days|
|**--schedule-info-advanced-schedule-monthly-occurrences**|array|Occurrences of days within a month.|monthly_occurrences|
|**--update-configuration-windows**|object|Windows specific update configuration.|windows|
|**--update-configuration-linux**|object|Linux specific update configuration.|linux|
|**--update-configuration-duration**|duration|Maximum time allowed for the software update configuration run. Duration needs to be specified using the format PT[n]H[n]M[n]S as per ISO8601|duration|
|**--update-configuration-azure-virtual-machines**|array|List of azure resource Ids for azure virtual machines targeted by the software update configuration.|azure_virtual_machines|
|**--update-configuration-non-azure-computer-names**|array|List of names of non-azure machines targeted by the software update configuration.|non_azure_computer_names|
|**--update-configuration-targets-azure-queries**|array|List of Azure queries in the software update configuration.|azure_queries|
|**--update-configuration-targets-non-azure-queries**|array|List of non Azure queries in the software update configuration.|non_azure_queries|
### automation software-update-configuration delete

delete a automation software-update-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--software-update-configuration-name**|string|The name of the software update configuration to be created.|software_update_configuration_name|
|**--client-request-id**|string|Identifies this specific client request.|client_request_id|
### automation software-update-configuration list

list a automation software-update-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--client-request-id**|string|Identifies this specific client request.|client_request_id|
|**--filter**|string|The filter to apply on the operation.|filter|
### automation software-update-configuration show

show a automation software-update-configuration.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--software-update-configuration-name**|string|The name of the software update configuration to be created.|software_update_configuration_name|
|**--client-request-id**|string|Identifies this specific client request.|client_request_id|
### automation software-update-configuration-machine-run list

list a automation software-update-configuration-machine-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--client-request-id**|string|Identifies this specific client request.|client_request_id|
|**--filter**|string|The filter to apply on the operation. You can use the following filters: 'properties/osType', 'properties/status', 'properties/startTime', and 'properties/softwareUpdateConfiguration/name'|filter|
|**--skip**|string|number of entries you skip before returning results|skip|
|**--top**|string|Maximum number of entries returned in the results collection|top|
### automation software-update-configuration-machine-run show

show a automation software-update-configuration-machine-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--software-update-configuration-machine-run-id**|uuid|The Id of the software update configuration machine run.|software_update_configuration_machine_run_id|
|**--client-request-id**|string|Identifies this specific client request.|client_request_id|
### automation software-update-configuration-run list

list a automation software-update-configuration-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--client-request-id**|string|Identifies this specific client request.|client_request_id|
|**--filter**|string|The filter to apply on the operation. You can use the following filters: 'properties/osType', 'properties/status', 'properties/startTime', and 'properties/softwareUpdateConfiguration/name'|filter|
|**--skip**|string|Number of entries you skip before returning results|skip|
|**--top**|string|Maximum number of entries returned in the results collection|top|
### automation software-update-configuration-run show

show a automation software-update-configuration-run.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--software-update-configuration-run-id**|uuid|The Id of the software update configuration run.|software_update_configuration_run_id|
|**--client-request-id**|string|Identifies this specific client request.|client_request_id|
### automation source-control create

create a automation source-control.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--source-control-name**|string|The source control name.|source_control_name|
|**--repo-url**|string|The repo url of the source control.|repo_url|
|**--branch**|string|The repo branch of the source control. Include branch as empty string for VsoTfvc.|branch|
|**--folder-path**|string|The folder path of the source control. Path must be relative.|folder_path|
|**--auto-sync**|boolean|The auto async of the source control. Default is false.|auto_sync|
|**--publish-runbook**|boolean|The auto publish of the source control. Default is true.|publish_runbook|
|**--source-type**|choice|The source type. Must be one of VsoGit, VsoTfvc, GitHub, case sensitive.|source_type|
|**--security-token**|object|The authorization token for the repo of the source control.|security_token|
|**--description**|string|The user description of the source control.|description|
### automation source-control delete

delete a automation source-control.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--source-control-name**|string|The name of source control.|source_control_name|
### automation source-control list

list a automation source-control.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--filter**|string|The filter to apply on the operation.|filter|
### automation source-control show

show a automation source-control.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--source-control-name**|string|The name of source control.|source_control_name|
### automation source-control update

update a automation source-control.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--source-control-name**|string|The source control name.|source_control_name|
|**--branch**|string|The repo branch of the source control.|branch|
|**--folder-path**|string|The folder path of the source control. Path must be relative.|folder_path|
|**--auto-sync**|boolean|The auto sync of the source control. Default is false.|auto_sync|
|**--publish-runbook**|boolean|The auto publish of the source control. Default is true.|publish_runbook|
|**--security-token**|object|The authorization token for the repo of the source control.|security_token|
|**--description**|string|The user description of the source control.|description|
### automation source-control-sync-job create

create a automation source-control-sync-job.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--source-control-name**|string|The source control name.|source_control_name|
|**--source-control-sync-job-id**|uuid|The source control sync job id.|source_control_sync_job_id|
|**--commit-id**|string|The commit id of the source control sync job. If not syncing to a commitId, enter an empty string.|commit_id|
### automation source-control-sync-job list

list a automation source-control-sync-job.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--source-control-name**|string|The source control name.|source_control_name|
|**--filter**|string|The filter to apply on the operation.|filter|
### automation source-control-sync-job show

show a automation source-control-sync-job.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--source-control-name**|string|The source control name.|source_control_name|
|**--source-control-sync-job-id**|uuid|The source control sync job id.|source_control_sync_job_id|
### automation source-control-sync-job-stream list

list a automation source-control-sync-job-stream.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--source-control-name**|string|The source control name.|source_control_name|
|**--source-control-sync-job-id**|uuid|The source control sync job id.|source_control_sync_job_id|
|**--filter**|string|The filter to apply on the operation.|filter|
### automation source-control-sync-job-stream show

show a automation source-control-sync-job-stream.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--source-control-name**|string|The source control name.|source_control_name|
|**--source-control-sync-job-id**|uuid|The source control sync job id.|source_control_sync_job_id|
|**--stream-id**|string|The id of the sync job stream.|stream_id|
### automation statistics list

list a automation statistics.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--filter**|string|The filter to apply on the operation.|filter|
### automation test-job create

create a automation test-job.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--runbook-name**|string|The parameters supplied to the create test job operation.|runbook_name|
|**--parameters**|dictionary|Gets or sets the parameters of the test job.|parameters|
|**--run-on**|string|Gets or sets the runOn which specifies the group name where the job is to be executed.|run_on|
### automation test-job resume

resume a automation test-job.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--runbook-name**|string|The runbook name.|runbook_name|
### automation test-job show

show a automation test-job.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--runbook-name**|string|The runbook name.|runbook_name|
### automation test-job stop

stop a automation test-job.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--runbook-name**|string|The runbook name.|runbook_name|
### automation test-job suspend

suspend a automation test-job.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--runbook-name**|string|The runbook name.|runbook_name|
### automation test-job-stream list

list a automation test-job-stream.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--runbook-name**|string|The runbook name.|runbook_name|
|**--filter**|string|The filter to apply on the operation.|filter|
### automation test-job-stream show

show a automation test-job-stream.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--runbook-name**|string|The runbook name.|runbook_name|
|**--job-stream-id**|string|The job stream id.|job_stream_id|
### automation usage list

list a automation usage.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
### automation variable create

create a automation variable.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--variable-name**|string|The variable name.|variable_name|
|**--name**|string|Gets or sets the name of the variable.|name|
|**--value**|string|Gets or sets the value of the variable.|value|
|**--description**|string|Gets or sets the description of the variable.|description|
|**--is-encrypted**|boolean|Gets or sets the encrypted flag of the variable.|is_encrypted|
### automation variable delete

delete a automation variable.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--variable-name**|string|The name of variable.|variable_name|
### automation variable list

list a automation variable.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
### automation variable show

show a automation variable.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--variable-name**|string|The name of variable.|variable_name|
### automation variable update

update a automation variable.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--variable-name**|string|The variable name.|variable_name|
|**--name**|string|Gets or sets the name of the variable.|name|
|**--value**|string|Gets or sets the value of the variable.|value|
|**--description**|string|Gets or sets the description of the variable.|description|
### automation watcher create

create a automation watcher.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--watcher-name**|string|The watcher name.|watcher_name|
|**--tags**|dictionary|Resource tags.|tags|
|**--location**|string|The Azure Region where the resource lives|location|
|**--etag**|string|Gets or sets the etag of the resource.|etag|
|**--execution-frequency-in-seconds**|integer|Gets or sets the frequency at which the watcher is invoked.|execution_frequency_in_seconds|
|**--script-name**|string|Gets or sets the name of the script the watcher is attached to, i.e. the name of an existing runbook.|script_name|
|**--script-parameters**|dictionary|Gets or sets the parameters of the script.|script_parameters|
|**--script-run-on**|string|Gets or sets the name of the hybrid worker group the watcher will run on.|script_run_on|
|**--description**|string|Gets or sets the description.|description|
### automation watcher delete

delete a automation watcher.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--watcher-name**|string|The watcher name.|watcher_name|
### automation watcher list

list a automation watcher.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--filter**|string|The filter to apply on the operation.|filter|
### automation watcher show

show a automation watcher.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--watcher-name**|string|The watcher name.|watcher_name|
### automation watcher start

start a automation watcher.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--watcher-name**|string|The watcher name.|watcher_name|
### automation watcher stop

stop a automation watcher.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--watcher-name**|string|The watcher name.|watcher_name|
### automation watcher update

update a automation watcher.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--watcher-name**|string|The watcher name.|watcher_name|
|**--name**|string|Gets or sets the name of the resource.|name|
|**--execution-frequency-in-seconds**|integer|Gets or sets the frequency at which the watcher is invoked.|execution_frequency_in_seconds|
### automation webhook create

create a automation webhook.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--webhook-name**|string|The webhook name.|webhook_name|
|**--name**|string|Gets or sets the name of the webhook.|name|
|**--is-enabled**|boolean|Gets or sets the value of the enabled flag of webhook.|is_enabled|
|**--uri**|string|Gets or sets the uri.|uri|
|**--expiry-time**|date-time|Gets or sets the expiry time.|expiry_time|
|**--parameters**|dictionary|Gets or sets the parameters of the job.|parameters|
|**--runbook**|object|Gets or sets the runbook.|runbook|
|**--run-on**|string|Gets or sets the name of the hybrid worker group the webhook job will run on.|run_on|
### automation webhook delete

delete a automation webhook.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--webhook-name**|string|The webhook name.|webhook_name|
### automation webhook generate-uri

generate-uri a automation webhook.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
### automation webhook list

list a automation webhook.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--filter**|string|The filter to apply on the operation.|filter|
### automation webhook show

show a automation webhook.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--webhook-name**|string|The webhook name.|webhook_name|
### automation webhook update

update a automation webhook.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|Name of an Azure Resource group.|resource_group_name|
|**--automation-account-name**|string|The name of the automation account.|automation_account_name|
|**--webhook-name**|string|The webhook name.|webhook_name|
|**--name**|string|Gets or sets the name of the webhook.|name|
|**--is-enabled**|boolean|Gets or sets the value of the enabled flag of webhook.|is_enabled|
|**--run-on**|string|Gets or sets the name of the hybrid worker group the webhook job will run on.|run_on|
|**--parameters**|dictionary|Gets or sets the parameters of the job.|parameters|
|**--description**|string|Gets or sets the description of the webhook.|description|
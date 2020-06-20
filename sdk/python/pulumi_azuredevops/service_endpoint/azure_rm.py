# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class AzureRM(pulumi.CustomResource):
    authorization: pulumi.Output[dict]
    azurerm_spn_tenantid: pulumi.Output[str]
    """
    The tenant id if the service principal.
    """
    azurerm_subscription_id: pulumi.Output[str]
    """
    The subscription Id of the Azure targets.
    """
    azurerm_subscription_name: pulumi.Output[str]
    """
    The subscription Name of the targets.
    """
    credentials: pulumi.Output[dict]
    """
    A `credentials` block.

      * `serviceprincipalid` (`str`) - The service principal application Id
      * `serviceprincipalkey` (`str`) - The service principal secret.
      * `serviceprincipalkeyHash` (`str`)
    """
    description: pulumi.Output[str]
    project_id: pulumi.Output[str]
    """
    The project ID or project name.
    """
    resource_group: pulumi.Output[str]
    """
    The resource group used for scope of automatic service endpoint.
    """
    service_endpoint_name: pulumi.Output[str]
    """
    The Service Endpoint name.
    """
    def __init__(__self__, resource_name, opts=None, authorization=None, azurerm_spn_tenantid=None, azurerm_subscription_id=None, azurerm_subscription_name=None, credentials=None, description=None, project_id=None, resource_group=None, service_endpoint_name=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages Manual or Automatic AzureRM service endpoint within Azure DevOps.

        ## Requirements (Manual AzureRM Service Endpoint)

        Before to create a service end point in Azure DevOps, you need to create a Service Principal in your Azure subscription.

        For detailed steps to create a service principal with Azure cli see the [documentation](https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli?view=azure-cli-latest)

        ## Example Usage

        ### Manual AzureRM Service Endpoint

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        project = azuredevops.core.Project("project",
            project_name="Sample Project",
            visibility="private",
            version_control="Git",
            work_item_template="Agile")
        endpointazure = azuredevops.service_endpoint.AzureRM("endpointazure",
            project_id=project.id,
            service_endpoint_name="TestServiceRM",
            credentials={
                "serviceprincipalid": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxx",
                "serviceprincipalkey": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            },
            azurerm_spn_tenantid="xxxxxxx-xxxx-xxx-xxxxx-xxxxxxxx",
            azurerm_subscription_id="xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxx",
            azurerm_subscription_name="Sample Subscription")
        ```

        ### Automatic AzureRM Service Endpoint

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        project = azuredevops.core.Project("project",
            project_name="Sample Project",
            visibility="private",
            version_control="Git",
            work_item_template="Agile")
        endpointazure = azuredevops.service_endpoint.AzureRM("endpointazure",
            project_id=project.id,
            service_endpoint_name="TestServiceRM",
            azurerm_spn_tenantid="xxxxxxx-xxxx-xxx-xxxxx-xxxxxxxx",
            azurerm_subscription_id="xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxx",
            azurerm_subscription_name="Microsoft Azure DEMO")
        ```

        ## Relevant Links

        * [Azure DevOps Service REST API 5.1 - Service End points](https://docs.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-5.1)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] azurerm_spn_tenantid: The tenant id if the service principal.
        :param pulumi.Input[str] azurerm_subscription_id: The subscription Id of the Azure targets.
        :param pulumi.Input[str] azurerm_subscription_name: The subscription Name of the targets.
        :param pulumi.Input[dict] credentials: A `credentials` block.
        :param pulumi.Input[str] project_id: The project ID or project name.
        :param pulumi.Input[str] resource_group: The resource group used for scope of automatic service endpoint.
        :param pulumi.Input[str] service_endpoint_name: The Service Endpoint name.

        The **credentials** object supports the following:

          * `serviceprincipalid` (`pulumi.Input[str]`) - The service principal application Id
          * `serviceprincipalkey` (`pulumi.Input[str]`) - The service principal secret.
          * `serviceprincipalkeyHash` (`pulumi.Input[str]`)
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['authorization'] = authorization
            if azurerm_spn_tenantid is None:
                raise TypeError("Missing required property 'azurerm_spn_tenantid'")
            __props__['azurerm_spn_tenantid'] = azurerm_spn_tenantid
            if azurerm_subscription_id is None:
                raise TypeError("Missing required property 'azurerm_subscription_id'")
            __props__['azurerm_subscription_id'] = azurerm_subscription_id
            if azurerm_subscription_name is None:
                raise TypeError("Missing required property 'azurerm_subscription_name'")
            __props__['azurerm_subscription_name'] = azurerm_subscription_name
            __props__['credentials'] = credentials
            __props__['description'] = description
            if project_id is None:
                raise TypeError("Missing required property 'project_id'")
            __props__['project_id'] = project_id
            __props__['resource_group'] = resource_group
            if service_endpoint_name is None:
                raise TypeError("Missing required property 'service_endpoint_name'")
            __props__['service_endpoint_name'] = service_endpoint_name
        super(AzureRM, __self__).__init__(
            'azuredevops:ServiceEndpoint/azureRM:AzureRM',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, authorization=None, azurerm_spn_tenantid=None, azurerm_subscription_id=None, azurerm_subscription_name=None, credentials=None, description=None, project_id=None, resource_group=None, service_endpoint_name=None):
        """
        Get an existing AzureRM resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] azurerm_spn_tenantid: The tenant id if the service principal.
        :param pulumi.Input[str] azurerm_subscription_id: The subscription Id of the Azure targets.
        :param pulumi.Input[str] azurerm_subscription_name: The subscription Name of the targets.
        :param pulumi.Input[dict] credentials: A `credentials` block.
        :param pulumi.Input[str] project_id: The project ID or project name.
        :param pulumi.Input[str] resource_group: The resource group used for scope of automatic service endpoint.
        :param pulumi.Input[str] service_endpoint_name: The Service Endpoint name.

        The **credentials** object supports the following:

          * `serviceprincipalid` (`pulumi.Input[str]`) - The service principal application Id
          * `serviceprincipalkey` (`pulumi.Input[str]`) - The service principal secret.
          * `serviceprincipalkeyHash` (`pulumi.Input[str]`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["authorization"] = authorization
        __props__["azurerm_spn_tenantid"] = azurerm_spn_tenantid
        __props__["azurerm_subscription_id"] = azurerm_subscription_id
        __props__["azurerm_subscription_name"] = azurerm_subscription_name
        __props__["credentials"] = credentials
        __props__["description"] = description
        __props__["project_id"] = project_id
        __props__["resource_group"] = resource_group
        __props__["service_endpoint_name"] = service_endpoint_name
        return AzureRM(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

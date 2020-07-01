# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class ResourceAuthorization(pulumi.CustomResource):
    authorized: pulumi.Output[bool]
    """
    Set to true to allow public access in the project. Type: boolean.
    """
    project_id: pulumi.Output[str]
    """
    The project ID or project name. Type: string.
    """
    resource_id: pulumi.Output[str]
    """
    The ID of the resource to authorize. Type: string.
    """
    type: pulumi.Output[str]
    """
    The type of the resource to authorize. Type: string. Valid values: `endpoint`, `queue`. Default value: `endpoint`.
    """
    def __init__(__self__, resource_name, opts=None, authorized=None, project_id=None, resource_id=None, type=None, __props__=None, __name__=None, __opts__=None):
        """
        ## # Security.ResourceAuthorization

        Manages authorization of resources, e.g. for access in build pipelines.

        Currently supported resources: service endpoint (aka service connection, endpoint).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        project = azuredevops.core.Project("project", project_name="Test Project")
        bitbucket_account = azuredevops.service_endpoint.BitBucket("bitbucketAccount",
            project_id=project.id,
            username="xxxx",
            password="xxxx",
            service_endpoint_name="test-bitbucket",
            description="test")
        auth = azuredevops.security.ResourceAuthorization("auth",
            project_id=project.id,
            resource_id=bitbucket_account.id,
            authorized=True)
        ```
        ## Relevant Links

        * [Azure DevOps Service REST API 5.1 - Authorize Definition Resource](https://docs.microsoft.com/en-us/rest/api/azure/devops/build/resources/authorize%20definition%20resources?view=azure-devops-rest-5.1)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] authorized: Set to true to allow public access in the project. Type: boolean.
        :param pulumi.Input[str] project_id: The project ID or project name. Type: string.
        :param pulumi.Input[str] resource_id: The ID of the resource to authorize. Type: string.
        :param pulumi.Input[str] type: The type of the resource to authorize. Type: string. Valid values: `endpoint`, `queue`. Default value: `endpoint`.
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

            if authorized is None:
                raise TypeError("Missing required property 'authorized'")
            __props__['authorized'] = authorized
            if project_id is None:
                raise TypeError("Missing required property 'project_id'")
            __props__['project_id'] = project_id
            __props__['resource_id'] = resource_id
            __props__['type'] = type
        super(ResourceAuthorization, __self__).__init__(
            'azuredevops:Security/resourceAuthorization:ResourceAuthorization',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, authorized=None, project_id=None, resource_id=None, type=None):
        """
        Get an existing ResourceAuthorization resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] authorized: Set to true to allow public access in the project. Type: boolean.
        :param pulumi.Input[str] project_id: The project ID or project name. Type: string.
        :param pulumi.Input[str] resource_id: The ID of the resource to authorize. Type: string.
        :param pulumi.Input[str] type: The type of the resource to authorize. Type: string. Valid values: `endpoint`, `queue`. Default value: `endpoint`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["authorized"] = authorized
        __props__["project_id"] = project_id
        __props__["resource_id"] = resource_id
        __props__["type"] = type
        return ResourceAuthorization(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class BitBucket(pulumi.CustomResource):
    authorization: pulumi.Output[dict]
    description: pulumi.Output[str]
    password: pulumi.Output[str]
    """
    Bitbucket account password.
    """
    password_hash: pulumi.Output[str]
    """
    A bcrypted hash of the attribute 'password'
    """
    project_id: pulumi.Output[str]
    """
    The project ID or project name.
    """
    service_endpoint_name: pulumi.Output[str]
    """
    The Service Endpoint name.
    """
    username: pulumi.Output[str]
    """
    Bitbucket account username.
    """
    def __init__(__self__, resource_name, opts=None, authorization=None, description=None, password=None, project_id=None, service_endpoint_name=None, username=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a Bitbucket service endpoint within Azure DevOps.

        ## Example Usage



        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        project = azuredevops.core.Project("project",
            project_name="Sample Project",
            visibility="private",
            version_control="Git",
            work_item_template="Agile")
        serviceendpoint = azuredevops.service_endpoint.BitBucket("serviceendpoint",
            project_id=project.id,
            username="xxxx",
            password="xxxx",
            service_endpoint_name="test-bitbucket",
            description="test")
        ```

        ## Relevant Links

        * [Azure DevOps Service REST API 5.1 - Agent Pools](https://docs.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-5.1)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] password: Bitbucket account password.
        :param pulumi.Input[str] project_id: The project ID or project name.
        :param pulumi.Input[str] service_endpoint_name: The Service Endpoint name.
        :param pulumi.Input[str] username: Bitbucket account username.
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
            __props__['description'] = description
            if password is None:
                raise TypeError("Missing required property 'password'")
            __props__['password'] = password
            if project_id is None:
                raise TypeError("Missing required property 'project_id'")
            __props__['project_id'] = project_id
            if service_endpoint_name is None:
                raise TypeError("Missing required property 'service_endpoint_name'")
            __props__['service_endpoint_name'] = service_endpoint_name
            if username is None:
                raise TypeError("Missing required property 'username'")
            __props__['username'] = username
            __props__['password_hash'] = None
        super(BitBucket, __self__).__init__(
            'azuredevops:ServiceEndpoint/bitBucket:BitBucket',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, authorization=None, description=None, password=None, password_hash=None, project_id=None, service_endpoint_name=None, username=None):
        """
        Get an existing BitBucket resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] password: Bitbucket account password.
        :param pulumi.Input[str] password_hash: A bcrypted hash of the attribute 'password'
        :param pulumi.Input[str] project_id: The project ID or project name.
        :param pulumi.Input[str] service_endpoint_name: The Service Endpoint name.
        :param pulumi.Input[str] username: Bitbucket account username.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["authorization"] = authorization
        __props__["description"] = description
        __props__["password"] = password
        __props__["password_hash"] = password_hash
        __props__["project_id"] = project_id
        __props__["service_endpoint_name"] = service_endpoint_name
        __props__["username"] = username
        return BitBucket(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

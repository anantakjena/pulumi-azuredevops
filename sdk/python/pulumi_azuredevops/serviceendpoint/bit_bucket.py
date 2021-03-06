# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['BitBucket']

warnings.warn("azuredevops.serviceendpoint.BitBucket has been deprecated in favor of azuredevops.ServiceEndpointBitBucket", DeprecationWarning)


class BitBucket(pulumi.CustomResource):
    warnings.warn("azuredevops.serviceendpoint.BitBucket has been deprecated in favor of azuredevops.ServiceEndpointBitBucket", DeprecationWarning)

    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 service_endpoint_name: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Bitbucket service endpoint within Azure DevOps.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        project = azuredevops.Project("project",
            visibility="private",
            version_control="Git",
            work_item_template="Agile")
        serviceendpoint = azuredevops.ServiceEndpointBitBucket("serviceendpoint",
            project_id=project.id,
            username="xxxx",
            password="xxxx",
            service_endpoint_name="test-bitbucket",
            description="test")
        ```
        ## Relevant Links

        - [Azure DevOps Service REST API 5.1 - Agent Pools](https://docs.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-5.1)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] password: Bitbucket account password.
        :param pulumi.Input[str] project_id: The project ID or project name.
        :param pulumi.Input[str] service_endpoint_name: The Service Endpoint name.
        :param pulumi.Input[str] username: Bitbucket account username.
        """
        pulumi.log.warn("BitBucket is deprecated: azuredevops.serviceendpoint.BitBucket has been deprecated in favor of azuredevops.ServiceEndpointBitBucket")
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
            opts.version = _utilities.get_version()
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
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            authorization: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            password_hash: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            service_endpoint_name: Optional[pulumi.Input[str]] = None,
            username: Optional[pulumi.Input[str]] = None) -> 'BitBucket':
        """
        Get an existing BitBucket resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
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

    @property
    @pulumi.getter
    def authorization(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "authorization")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        """
        Bitbucket account password.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="passwordHash")
    def password_hash(self) -> pulumi.Output[str]:
        """
        A bcrypted hash of the attribute 'password'
        """
        return pulumi.get(self, "password_hash")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The project ID or project name.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="serviceEndpointName")
    def service_endpoint_name(self) -> pulumi.Output[str]:
        """
        The Service Endpoint name.
        """
        return pulumi.get(self, "service_endpoint_name")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        """
        Bitbucket account username.
        """
        return pulumi.get(self, "username")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


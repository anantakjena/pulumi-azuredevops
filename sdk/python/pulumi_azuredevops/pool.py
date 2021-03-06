# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['Pool']


class Pool(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_provision: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pool_type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an agent pool within Azure DevOps.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        pool = azuredevops.Pool("pool", auto_provision=False)
        ```
        ## Relevant Links

        - [Azure DevOps Service REST API 5.1 - Agent Pools](https://docs.microsoft.com/en-us/rest/api/azure/devops/distributedtask/pools?view=azure-devops-rest-5.1)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_provision: Specifies whether or not a queue should be automatically provisioned for each project collection. Defaults to `false`.
        :param pulumi.Input[str] name: The name of the agent pool.
        :param pulumi.Input[str] pool_type: Specifies whether the agent pool type is Automation or Deployment. Defaults to `automation`.
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
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['auto_provision'] = auto_provision
            __props__['name'] = name
            __props__['pool_type'] = pool_type
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azuredevops:Agent/pool:Pool")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Pool, __self__).__init__(
            'azuredevops:index/pool:Pool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auto_provision: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            pool_type: Optional[pulumi.Input[str]] = None) -> 'Pool':
        """
        Get an existing Pool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_provision: Specifies whether or not a queue should be automatically provisioned for each project collection. Defaults to `false`.
        :param pulumi.Input[str] name: The name of the agent pool.
        :param pulumi.Input[str] pool_type: Specifies whether the agent pool type is Automation or Deployment. Defaults to `automation`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["auto_provision"] = auto_provision
        __props__["name"] = name
        __props__["pool_type"] = pool_type
        return Pool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoProvision")
    def auto_provision(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether or not a queue should be automatically provisioned for each project collection. Defaults to `false`.
        """
        return pulumi.get(self, "auto_provision")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the agent pool.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="poolType")
    def pool_type(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies whether the agent pool type is Automation or Deployment. Defaults to `automation`.
        """
        return pulumi.get(self, "pool_type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


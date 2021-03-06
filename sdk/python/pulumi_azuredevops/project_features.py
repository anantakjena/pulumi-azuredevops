# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['ProjectFeatures']


class ProjectFeatures(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 features: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages features for Azure DevOps projects

        ## Relevant Links

        No official documentation available

        ## PAT Permissions Required

        - **Project & Team**: Read, Write, & Manage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] features: Defines the status (`enabled`, `disabled`) of the project features.  
               Valid features `boards`, `repositories`, `pipelines`, `testplans`, `artifacts`
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

            if features is None:
                raise TypeError("Missing required property 'features'")
            __props__['features'] = features
            if project_id is None:
                raise TypeError("Missing required property 'project_id'")
            __props__['project_id'] = project_id
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azuredevops:Core/projectFeatures:ProjectFeatures")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ProjectFeatures, __self__).__init__(
            'azuredevops:index/projectFeatures:ProjectFeatures',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            features: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            project_id: Optional[pulumi.Input[str]] = None) -> 'ProjectFeatures':
        """
        Get an existing ProjectFeatures resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] features: Defines the status (`enabled`, `disabled`) of the project features.  
               Valid features `boards`, `repositories`, `pipelines`, `testplans`, `artifacts`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["features"] = features
        __props__["project_id"] = project_id
        return ProjectFeatures(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def features(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Defines the status (`enabled`, `disabled`) of the project features.  
        Valid features `boards`, `repositories`, `pipelines`, `testplans`, `artifacts`
        """
        return pulumi.get(self, "features")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


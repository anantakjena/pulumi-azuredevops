# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Project(pulumi.CustomResource):
    description: pulumi.Output[str]
    """
    The Description of the Project.
    """
    features: pulumi.Output[dict]
    """
    Defines the status (`enabled`, `disabled`) of the project features.  
    Valid features `boards`, `repositories`, `pipelines`, `testplans`, `artifacts`
    """
    process_template_id: pulumi.Output[str]
    """
    The Process Template ID used by the Project.
    """
    project_name: pulumi.Output[str]
    """
    The Project Name.
    """
    version_control: pulumi.Output[str]
    """
    Specifies the version control system. Valid values: `Git` or `Tfvc`. Defaults to `Git`.
    """
    visibility: pulumi.Output[str]
    """
    Specifies the visibility of the Project. Valid values: `private` or `public`. Defaults to `private`.
    """
    work_item_template: pulumi.Output[str]
    """
    Specifies the work item template. Defaults to `Agile`.
    """
    def __init__(__self__, resource_name, opts=None, description=None, features=None, project_name=None, version_control=None, visibility=None, work_item_template=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a project within Azure DevOps.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        project = azuredevops.core.Project("project",
            description="Test Project Description",
            features={
                "artifacts": "disabled",
                "testplans": "disabled",
            },
            project_name="Test Project",
            version_control="Git",
            visibility="private",
            work_item_template="Agile")
        ```
        ## Relevant Links

        * [Azure DevOps Service REST API 5.1 - Projects](https://docs.microsoft.com/en-us/rest/api/azure/devops/core/projects?view=azure-devops-rest-5.1)

        ## PAT Permissions Required

        - **Project & Team**: Read, Write, & Manage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The Description of the Project.
        :param pulumi.Input[dict] features: Defines the status (`enabled`, `disabled`) of the project features.  
               Valid features `boards`, `repositories`, `pipelines`, `testplans`, `artifacts`
        :param pulumi.Input[str] project_name: The Project Name.
        :param pulumi.Input[str] version_control: Specifies the version control system. Valid values: `Git` or `Tfvc`. Defaults to `Git`.
        :param pulumi.Input[str] visibility: Specifies the visibility of the Project. Valid values: `private` or `public`. Defaults to `private`.
        :param pulumi.Input[str] work_item_template: Specifies the work item template. Defaults to `Agile`.
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

            __props__['description'] = description
            __props__['features'] = features
            if project_name is None:
                raise TypeError("Missing required property 'project_name'")
            __props__['project_name'] = project_name
            __props__['version_control'] = version_control
            __props__['visibility'] = visibility
            __props__['work_item_template'] = work_item_template
            __props__['process_template_id'] = None
        super(Project, __self__).__init__(
            'azuredevops:Core/project:Project',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, description=None, features=None, process_template_id=None, project_name=None, version_control=None, visibility=None, work_item_template=None):
        """
        Get an existing Project resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The Description of the Project.
        :param pulumi.Input[dict] features: Defines the status (`enabled`, `disabled`) of the project features.  
               Valid features `boards`, `repositories`, `pipelines`, `testplans`, `artifacts`
        :param pulumi.Input[str] process_template_id: The Process Template ID used by the Project.
        :param pulumi.Input[str] project_name: The Project Name.
        :param pulumi.Input[str] version_control: Specifies the version control system. Valid values: `Git` or `Tfvc`. Defaults to `Git`.
        :param pulumi.Input[str] visibility: Specifies the visibility of the Project. Valid values: `private` or `public`. Defaults to `private`.
        :param pulumi.Input[str] work_item_template: Specifies the work item template. Defaults to `Agile`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["features"] = features
        __props__["process_template_id"] = process_template_id
        __props__["project_name"] = project_name
        __props__["version_control"] = version_control
        __props__["visibility"] = visibility
        __props__["work_item_template"] = work_item_template
        return Project(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

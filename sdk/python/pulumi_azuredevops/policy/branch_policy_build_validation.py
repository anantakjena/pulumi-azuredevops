# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class BranchPolicyBuildValidation(pulumi.CustomResource):
    blocking: pulumi.Output[bool]
    """
    A flag indicating if the policy should be blocking. Defaults to `true`.
    """
    enabled: pulumi.Output[bool]
    """
    A flag indicating if the policy should be enabled. Defaults to `true`.
    """
    project_id: pulumi.Output[str]
    """
    The ID of the project in which the policy will be created.
    """
    settings: pulumi.Output[dict]
    """
    Configuration for the policy. This block must be defined exactly once.

      * `buildDefinitionId` (`float`) - The ID of the build to monitor for the policy.
      * `display_name` (`str`) - The display name for the policy.
      * `manualQueueOnly` (`bool`) - If set to true, the build will need to be manually queued. Defaults to `false`
      * `queueOnSourceUpdateOnly` (`bool`) - True if the build should queue on source updates only. Defaults to `true`.
      * `scopes` (`list`) - Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.
        * `matchType` (`str`) - The match type to use when applying the policy. Supported values are `Exact` (default) or `Prefix`.
        * `repositoryId` (`str`) - The repository ID. Needed only if the scope of the policy will be limited to a single repository.
        * `repositoryRef` (`str`) - The ref pattern to use for the match. If `match_type` is `Exact`, this should be a qualified ref such as `refs/heads/master`. If `match_type` is `Prefix`, this should be a ref path such as `refs/heads/releases`.

      * `validDuration` (`float`) - The number of minutes for which the build is valid. If `0`, the build will not expire. Defaults to `720` (12 hours).
    """
    def __init__(__self__, resource_name, opts=None, blocking=None, enabled=None, project_id=None, settings=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a build validation branch policy within Azure DevOps.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        project = azuredevops.core.Project("project", project_name="Sample Project")
        git = azuredevops.repository.Git("git",
            project_id=project.id,
            initialization={
                "initType": "Clean",
            })
        build_definition = azuredevops.build.BuildDefinition("buildDefinition",
            project_id=project.id,
            repository={
                "repoType": "TfsGit",
                "repoId": git.id,
                "ymlPath": "azure-pipelines.yml",
            })
        branch_policy_build_validation = azuredevops.policy.BranchPolicyBuildValidation("branchPolicyBuildValidation",
            project_id=project.id,
            enabled=True,
            blocking=True,
            settings={
                "display_name": "Don't break the build!",
                "buildDefinitionId": build_definition.id,
                "validDuration": 720,
                "scopes": [
                    {
                        "repositoryId": git.id,
                        "repositoryRef": git.default_branch,
                        "matchType": "Exact",
                    },
                    {
                        "repositoryId": git.id,
                        "repositoryRef": "refs/heads/releases",
                        "matchType": "Prefix",
                    },
                ],
            })
        ```
        ## Relevant Links

        * [Azure DevOps Service REST API 5.1 - Policy Configurations](https://docs.microsoft.com/en-us/rest/api/azure/devops/policy/configurations/create?view=azure-devops-rest-5.1)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] blocking: A flag indicating if the policy should be blocking. Defaults to `true`.
        :param pulumi.Input[bool] enabled: A flag indicating if the policy should be enabled. Defaults to `true`.
        :param pulumi.Input[str] project_id: The ID of the project in which the policy will be created.
        :param pulumi.Input[dict] settings: Configuration for the policy. This block must be defined exactly once.

        The **settings** object supports the following:

          * `buildDefinitionId` (`pulumi.Input[float]`) - The ID of the build to monitor for the policy.
          * `display_name` (`pulumi.Input[str]`) - The display name for the policy.
          * `manualQueueOnly` (`pulumi.Input[bool]`) - If set to true, the build will need to be manually queued. Defaults to `false`
          * `queueOnSourceUpdateOnly` (`pulumi.Input[bool]`) - True if the build should queue on source updates only. Defaults to `true`.
          * `scopes` (`pulumi.Input[list]`) - Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.
            * `matchType` (`pulumi.Input[str]`) - The match type to use when applying the policy. Supported values are `Exact` (default) or `Prefix`.
            * `repositoryId` (`pulumi.Input[str]`) - The repository ID. Needed only if the scope of the policy will be limited to a single repository.
            * `repositoryRef` (`pulumi.Input[str]`) - The ref pattern to use for the match. If `match_type` is `Exact`, this should be a qualified ref such as `refs/heads/master`. If `match_type` is `Prefix`, this should be a ref path such as `refs/heads/releases`.

          * `validDuration` (`pulumi.Input[float]`) - The number of minutes for which the build is valid. If `0`, the build will not expire. Defaults to `720` (12 hours).
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

            __props__['blocking'] = blocking
            __props__['enabled'] = enabled
            if project_id is None:
                raise TypeError("Missing required property 'project_id'")
            __props__['project_id'] = project_id
            if settings is None:
                raise TypeError("Missing required property 'settings'")
            __props__['settings'] = settings
        super(BranchPolicyBuildValidation, __self__).__init__(
            'azuredevops:Policy/branchPolicyBuildValidation:BranchPolicyBuildValidation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, blocking=None, enabled=None, project_id=None, settings=None):
        """
        Get an existing BranchPolicyBuildValidation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] blocking: A flag indicating if the policy should be blocking. Defaults to `true`.
        :param pulumi.Input[bool] enabled: A flag indicating if the policy should be enabled. Defaults to `true`.
        :param pulumi.Input[str] project_id: The ID of the project in which the policy will be created.
        :param pulumi.Input[dict] settings: Configuration for the policy. This block must be defined exactly once.

        The **settings** object supports the following:

          * `buildDefinitionId` (`pulumi.Input[float]`) - The ID of the build to monitor for the policy.
          * `display_name` (`pulumi.Input[str]`) - The display name for the policy.
          * `manualQueueOnly` (`pulumi.Input[bool]`) - If set to true, the build will need to be manually queued. Defaults to `false`
          * `queueOnSourceUpdateOnly` (`pulumi.Input[bool]`) - True if the build should queue on source updates only. Defaults to `true`.
          * `scopes` (`pulumi.Input[list]`) - Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.
            * `matchType` (`pulumi.Input[str]`) - The match type to use when applying the policy. Supported values are `Exact` (default) or `Prefix`.
            * `repositoryId` (`pulumi.Input[str]`) - The repository ID. Needed only if the scope of the policy will be limited to a single repository.
            * `repositoryRef` (`pulumi.Input[str]`) - The ref pattern to use for the match. If `match_type` is `Exact`, this should be a qualified ref such as `refs/heads/master`. If `match_type` is `Prefix`, this should be a ref path such as `refs/heads/releases`.

          * `validDuration` (`pulumi.Input[float]`) - The number of minutes for which the build is valid. If `0`, the build will not expire. Defaults to `720` (12 hours).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["blocking"] = blocking
        __props__["enabled"] = enabled
        __props__["project_id"] = project_id
        __props__["settings"] = settings
        return BranchPolicyBuildValidation(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

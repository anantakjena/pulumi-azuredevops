# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class BuildDefinition(pulumi.CustomResource):
    agent_pool_name: pulumi.Output[str]
    """
    The agent pool that should execute the build. Defaults to `Hosted Ubuntu 1604`.
    """
    ci_trigger: pulumi.Output[dict]
    """
    Continuous Integration Integration trigger.

      * `override` (`dict`) - Override the azure-pipeline file and use a this configuration for all builds.
        * `batch` (`bool`) - If you set batch to true, when a pipeline is running, the system waits until the run is completed, then starts another run with all changes that have not yet been built. Defaults to `true`.
        * `branchFilters` (`list`) - The branches to include and exclude from the trigger.
          * `excludes` (`list`) - List of branch patterns to exclude.
          * `includes` (`list`) - List of branch patterns to include.

        * `maxConcurrentBuildsPerBranch` (`float`) - The number of max builds per branch. Defaults to `1`.
        * `pathFilters` (`list`) - Specify file paths to include or exclude. Note that the wildcard syntax is different between branches/tags and file paths.
          * `excludes` (`list`) - List of branch patterns to exclude.
          * `includes` (`list`) - List of branch patterns to include.

        * `pollingInterval` (`float`) - How often the external repository is polled. Defaults to `0`.
        * `pollingJobId` (`str`) - This is the ID of the polling job that polls the external repository. Once the build definition is saved/updated, this value is set.

      * `useYaml` (`bool`) - Use the azure-pipeline file for the build configuration. Defaults to `false`.
    """
    name: pulumi.Output[str]
    """
    The name of the build definition.
    """
    path: pulumi.Output[str]
    project_id: pulumi.Output[str]
    """
    The project ID or project name.
    """
    pull_request_trigger: pulumi.Output[dict]
    """
    Pull Request Integration Integration trigger.

      * `commentRequired` (`str`)
      * `forks` (`dict`) - Set permissions for Forked repositories.
        * `enabled` (`bool`) - Build pull requests form forms of this repository.
        * `shareSecrets` (`bool`) - Make secrets available to builds of forks.

      * `initialBranch` (`str`)
      * `override` (`dict`) - Override the azure-pipeline file and use a this configuration for all builds.
        * `autoCancel` (`bool`) - . Defaults to `true`.
        * `branchFilters` (`list`) - The branches to include and exclude from the trigger.
          * `excludes` (`list`) - List of branch patterns to exclude.
          * `includes` (`list`) - List of branch patterns to include.

        * `pathFilters` (`list`) - Specify file paths to include or exclude. Note that the wildcard syntax is different between branches/tags and file paths.
          * `excludes` (`list`) - List of branch patterns to exclude.
          * `includes` (`list`) - List of branch patterns to include.

      * `useYaml` (`bool`) - Use the azure-pipeline file for the build configuration. Defaults to `false`.
    """
    repository: pulumi.Output[dict]
    """
    A `repository` block as documented below.

      * `branchName` (`str`) - The branch name for which builds are triggered. Defaults to `master`.
      * `repoId` (`str`) - The id of the repository. For `TfsGit` repos, this is simply the ID of the repository. For `Github` repos, this will take the form of `<GitHub Org>/<Repo Name>`. For `Bitbucket` repos, this will take the form of `<Workspace ID>/<Repo Name>`.
      * `repoType` (`str`) - The repository type. Valid values: `GitHub` or `TfsGit` or `Bitbucket`. Defaults to `Github`.
      * `serviceConnectionId` (`str`) - The service connection ID. Used if the `repo_type` is `GitHub`.
      * `ymlPath` (`str`) - The path of the Yaml file describing the build definition.
    """
    revision: pulumi.Output[float]
    """
    The revision of the build definition
    """
    variable_groups: pulumi.Output[list]
    """
    A list of variable group IDs (integers) to link to the build definition.
    """
    variables: pulumi.Output[list]
    """
    A list of `variable` blocks, as documented below.

      * `allowOverride` (`bool`) - True if the variable can be overridden. Defaults to `true`.
      * `isSecret` (`bool`) - True if the variable is a secret. Defaults to `false`.
      * `name` (`str`) - The name of the variable.
      * `secretValue` (`str`) - The secret value of the variable. Used when `is_secret` set to `true`.
      * `value` (`str`) - The value of the variable.
    """
    def __init__(__self__, resource_name, opts=None, agent_pool_name=None, ci_trigger=None, name=None, path=None, project_id=None, pull_request_trigger=None, repository=None, variable_groups=None, variables=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a Build Definition within Azure DevOps.

        ## Example Usage



        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        project = azuredevops.core.Project("project",
            project_name="Sample Project",
            visibility="private",
            version_control="Git",
            work_item_template="Agile")
        repository = azuredevops.repository.Git("repository",
            project_id=project.id,
            initialization={
                "initType": "Clean",
            })
        vars = azuredevops.pipeline.VariableGroup("vars",
            project_id=project.id,
            description="Managed by Terraform",
            allow_access=True,
            variable=[{
                "name": "FOO",
                "value": "BAR",
            }])
        build = azuredevops.build.BuildDefinition("build",
            project_id=project.id,
            path="\\ExampleFolder",
            ci_trigger={
                "useYaml": True,
            },
            repository={
                "repoType": "TfsGit",
                "repoId": repository.id,
                "branchName": repository.default_branch,
                "ymlPath": "azure-pipelines.yml",
            },
            variable_groups=[vars.id],
            variable=[
                {
                    "name": "PipelineVariable",
                    "value": "Go Microsoft!",
                },
                {
                    "name": "PipelineSecret",
                    "secretValue": "ZGV2cw",
                    "isSecret": True,
                },
            ])
        ```

        ## Relevant Links

        * [Azure DevOps Service REST API 5.1 - Build Definitions](https://docs.microsoft.com/en-us/rest/api/azure/devops/build/definitions?view=azure-devops-rest-5.1)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] agent_pool_name: The agent pool that should execute the build. Defaults to `Hosted Ubuntu 1604`.
        :param pulumi.Input[dict] ci_trigger: Continuous Integration Integration trigger.
        :param pulumi.Input[str] name: The name of the build definition.
        :param pulumi.Input[str] project_id: The project ID or project name.
        :param pulumi.Input[dict] pull_request_trigger: Pull Request Integration Integration trigger.
        :param pulumi.Input[dict] repository: A `repository` block as documented below.
        :param pulumi.Input[list] variable_groups: A list of variable group IDs (integers) to link to the build definition.
        :param pulumi.Input[list] variables: A list of `variable` blocks, as documented below.

        The **ci_trigger** object supports the following:

          * `override` (`pulumi.Input[dict]`) - Override the azure-pipeline file and use a this configuration for all builds.
            * `batch` (`pulumi.Input[bool]`) - If you set batch to true, when a pipeline is running, the system waits until the run is completed, then starts another run with all changes that have not yet been built. Defaults to `true`.
            * `branchFilters` (`pulumi.Input[list]`) - The branches to include and exclude from the trigger.
              * `excludes` (`pulumi.Input[list]`) - List of branch patterns to exclude.
              * `includes` (`pulumi.Input[list]`) - List of branch patterns to include.

            * `maxConcurrentBuildsPerBranch` (`pulumi.Input[float]`) - The number of max builds per branch. Defaults to `1`.
            * `pathFilters` (`pulumi.Input[list]`) - Specify file paths to include or exclude. Note that the wildcard syntax is different between branches/tags and file paths.
              * `excludes` (`pulumi.Input[list]`) - List of branch patterns to exclude.
              * `includes` (`pulumi.Input[list]`) - List of branch patterns to include.

            * `pollingInterval` (`pulumi.Input[float]`) - How often the external repository is polled. Defaults to `0`.
            * `pollingJobId` (`pulumi.Input[str]`) - This is the ID of the polling job that polls the external repository. Once the build definition is saved/updated, this value is set.

          * `useYaml` (`pulumi.Input[bool]`) - Use the azure-pipeline file for the build configuration. Defaults to `false`.

        The **pull_request_trigger** object supports the following:

          * `commentRequired` (`pulumi.Input[str]`)
          * `forks` (`pulumi.Input[dict]`) - Set permissions for Forked repositories.
            * `enabled` (`pulumi.Input[bool]`) - Build pull requests form forms of this repository.
            * `shareSecrets` (`pulumi.Input[bool]`) - Make secrets available to builds of forks.

          * `initialBranch` (`pulumi.Input[str]`)
          * `override` (`pulumi.Input[dict]`) - Override the azure-pipeline file and use a this configuration for all builds.
            * `autoCancel` (`pulumi.Input[bool]`) - . Defaults to `true`.
            * `branchFilters` (`pulumi.Input[list]`) - The branches to include and exclude from the trigger.
              * `excludes` (`pulumi.Input[list]`) - List of branch patterns to exclude.
              * `includes` (`pulumi.Input[list]`) - List of branch patterns to include.

            * `pathFilters` (`pulumi.Input[list]`) - Specify file paths to include or exclude. Note that the wildcard syntax is different between branches/tags and file paths.
              * `excludes` (`pulumi.Input[list]`) - List of branch patterns to exclude.
              * `includes` (`pulumi.Input[list]`) - List of branch patterns to include.

          * `useYaml` (`pulumi.Input[bool]`) - Use the azure-pipeline file for the build configuration. Defaults to `false`.

        The **repository** object supports the following:

          * `branchName` (`pulumi.Input[str]`) - The branch name for which builds are triggered. Defaults to `master`.
          * `repoId` (`pulumi.Input[str]`) - The id of the repository. For `TfsGit` repos, this is simply the ID of the repository. For `Github` repos, this will take the form of `<GitHub Org>/<Repo Name>`. For `Bitbucket` repos, this will take the form of `<Workspace ID>/<Repo Name>`.
          * `repoType` (`pulumi.Input[str]`) - The repository type. Valid values: `GitHub` or `TfsGit` or `Bitbucket`. Defaults to `Github`.
          * `serviceConnectionId` (`pulumi.Input[str]`) - The service connection ID. Used if the `repo_type` is `GitHub`.
          * `ymlPath` (`pulumi.Input[str]`) - The path of the Yaml file describing the build definition.

        The **variables** object supports the following:

          * `allowOverride` (`pulumi.Input[bool]`) - True if the variable can be overridden. Defaults to `true`.
          * `isSecret` (`pulumi.Input[bool]`) - True if the variable is a secret. Defaults to `false`.
          * `name` (`pulumi.Input[str]`) - The name of the variable.
          * `secretValue` (`pulumi.Input[str]`) - The secret value of the variable. Used when `is_secret` set to `true`.
          * `value` (`pulumi.Input[str]`) - The value of the variable.
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

            __props__['agent_pool_name'] = agent_pool_name
            __props__['ci_trigger'] = ci_trigger
            __props__['name'] = name
            __props__['path'] = path
            if project_id is None:
                raise TypeError("Missing required property 'project_id'")
            __props__['project_id'] = project_id
            __props__['pull_request_trigger'] = pull_request_trigger
            if repository is None:
                raise TypeError("Missing required property 'repository'")
            __props__['repository'] = repository
            __props__['variable_groups'] = variable_groups
            __props__['variables'] = variables
            __props__['revision'] = None
        super(BuildDefinition, __self__).__init__(
            'azuredevops:Build/buildDefinition:BuildDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, agent_pool_name=None, ci_trigger=None, name=None, path=None, project_id=None, pull_request_trigger=None, repository=None, revision=None, variable_groups=None, variables=None):
        """
        Get an existing BuildDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] agent_pool_name: The agent pool that should execute the build. Defaults to `Hosted Ubuntu 1604`.
        :param pulumi.Input[dict] ci_trigger: Continuous Integration Integration trigger.
        :param pulumi.Input[str] name: The name of the build definition.
        :param pulumi.Input[str] project_id: The project ID or project name.
        :param pulumi.Input[dict] pull_request_trigger: Pull Request Integration Integration trigger.
        :param pulumi.Input[dict] repository: A `repository` block as documented below.
        :param pulumi.Input[float] revision: The revision of the build definition
        :param pulumi.Input[list] variable_groups: A list of variable group IDs (integers) to link to the build definition.
        :param pulumi.Input[list] variables: A list of `variable` blocks, as documented below.

        The **ci_trigger** object supports the following:

          * `override` (`pulumi.Input[dict]`) - Override the azure-pipeline file and use a this configuration for all builds.
            * `batch` (`pulumi.Input[bool]`) - If you set batch to true, when a pipeline is running, the system waits until the run is completed, then starts another run with all changes that have not yet been built. Defaults to `true`.
            * `branchFilters` (`pulumi.Input[list]`) - The branches to include and exclude from the trigger.
              * `excludes` (`pulumi.Input[list]`) - List of branch patterns to exclude.
              * `includes` (`pulumi.Input[list]`) - List of branch patterns to include.

            * `maxConcurrentBuildsPerBranch` (`pulumi.Input[float]`) - The number of max builds per branch. Defaults to `1`.
            * `pathFilters` (`pulumi.Input[list]`) - Specify file paths to include or exclude. Note that the wildcard syntax is different between branches/tags and file paths.
              * `excludes` (`pulumi.Input[list]`) - List of branch patterns to exclude.
              * `includes` (`pulumi.Input[list]`) - List of branch patterns to include.

            * `pollingInterval` (`pulumi.Input[float]`) - How often the external repository is polled. Defaults to `0`.
            * `pollingJobId` (`pulumi.Input[str]`) - This is the ID of the polling job that polls the external repository. Once the build definition is saved/updated, this value is set.

          * `useYaml` (`pulumi.Input[bool]`) - Use the azure-pipeline file for the build configuration. Defaults to `false`.

        The **pull_request_trigger** object supports the following:

          * `commentRequired` (`pulumi.Input[str]`)
          * `forks` (`pulumi.Input[dict]`) - Set permissions for Forked repositories.
            * `enabled` (`pulumi.Input[bool]`) - Build pull requests form forms of this repository.
            * `shareSecrets` (`pulumi.Input[bool]`) - Make secrets available to builds of forks.

          * `initialBranch` (`pulumi.Input[str]`)
          * `override` (`pulumi.Input[dict]`) - Override the azure-pipeline file and use a this configuration for all builds.
            * `autoCancel` (`pulumi.Input[bool]`) - . Defaults to `true`.
            * `branchFilters` (`pulumi.Input[list]`) - The branches to include and exclude from the trigger.
              * `excludes` (`pulumi.Input[list]`) - List of branch patterns to exclude.
              * `includes` (`pulumi.Input[list]`) - List of branch patterns to include.

            * `pathFilters` (`pulumi.Input[list]`) - Specify file paths to include or exclude. Note that the wildcard syntax is different between branches/tags and file paths.
              * `excludes` (`pulumi.Input[list]`) - List of branch patterns to exclude.
              * `includes` (`pulumi.Input[list]`) - List of branch patterns to include.

          * `useYaml` (`pulumi.Input[bool]`) - Use the azure-pipeline file for the build configuration. Defaults to `false`.

        The **repository** object supports the following:

          * `branchName` (`pulumi.Input[str]`) - The branch name for which builds are triggered. Defaults to `master`.
          * `repoId` (`pulumi.Input[str]`) - The id of the repository. For `TfsGit` repos, this is simply the ID of the repository. For `Github` repos, this will take the form of `<GitHub Org>/<Repo Name>`. For `Bitbucket` repos, this will take the form of `<Workspace ID>/<Repo Name>`.
          * `repoType` (`pulumi.Input[str]`) - The repository type. Valid values: `GitHub` or `TfsGit` or `Bitbucket`. Defaults to `Github`.
          * `serviceConnectionId` (`pulumi.Input[str]`) - The service connection ID. Used if the `repo_type` is `GitHub`.
          * `ymlPath` (`pulumi.Input[str]`) - The path of the Yaml file describing the build definition.

        The **variables** object supports the following:

          * `allowOverride` (`pulumi.Input[bool]`) - True if the variable can be overridden. Defaults to `true`.
          * `isSecret` (`pulumi.Input[bool]`) - True if the variable is a secret. Defaults to `false`.
          * `name` (`pulumi.Input[str]`) - The name of the variable.
          * `secretValue` (`pulumi.Input[str]`) - The secret value of the variable. Used when `is_secret` set to `true`.
          * `value` (`pulumi.Input[str]`) - The value of the variable.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["agent_pool_name"] = agent_pool_name
        __props__["ci_trigger"] = ci_trigger
        __props__["name"] = name
        __props__["path"] = path
        __props__["project_id"] = project_id
        __props__["pull_request_trigger"] = pull_request_trigger
        __props__["repository"] = repository
        __props__["revision"] = revision
        __props__["variable_groups"] = variable_groups
        __props__["variables"] = variables
        return BuildDefinition(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

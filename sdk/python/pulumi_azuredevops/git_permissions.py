# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['GitPermissions']


class GitPermissions(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 branch_name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 principal: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 replace: Optional[pulumi.Input[bool]] = None,
                 repository_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages permissions for Git repositories.

        > **Note** Permissions can be assigned to group principals and not to single user principals.

        ## Permission levels

        Permission for Git Repositories within Azure DevOps can be applied on three different levels.
        Those levels are reflected by specifying (or omitting) values for the arguments `project_id`, `repository_id` and `branch_name`.

        ### Project level

        Permissions for all Git Repositories inside a project (existing or newly created ones) are specified, if only the argument `project_id` has a value.

        #### Example usage

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        project_git_root_permissions = azuredevops.GitPermissions("project-git-root-permissions",
            project_id=azuredevops_project["project"]["id"],
            principal=data["azuredevops_group"]["project-readers"]["id"],
            permissions={
                "CreateRepository": "Deny",
                "DeleteRepository": "Deny",
                "RenameRepository": "NotSet",
            })
        ```

        ### Repository level

        Permissions for a specific Git Repository and all existing or newly created branches are specified if the arguments `project_id` and `repository_id` are set.

        #### Example usage

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        project_git_repo_permissions = azuredevops.GitPermissions("project-git-repo-permissions",
            project_id=data["azuredevops_git_repository"]["git-repo"]["project_id"],
            repository_id=data["azuredevops_git_repository"]["git-repo"]["id"],
            principal=data["azuredevops_group"]["project-administrators"]["id"],
            permissions={
                "RemoveOthersLocks": "Allow",
                "ManagePermissions": "Deny",
                "CreateTag": "Deny",
                "CreateBranch": "NotSet",
            })
        ```

        ### Branch level

        Permissions for a specific branch inside a Git Repository are specified if all above mentioned the arguments are set.

        #### Example usage

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        project_git_branch_permissions = azuredevops.GitPermissions("project-git-branch-permissions",
            project_id=data["azuredevops_git_repository"]["git-repo"]["project_id"],
            repository_id=data["azuredevops_git_repository"]["git-repo"]["id"],
            branch_name="refs/heads/master",
            principal=data["azuredevops_group"]["project-contributors"]["id"],
            permissions={
                "RemoveOthersLocks": "Allow",
                "ForcePush": "Deny",
            })
        ```

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        project = azuredevops.Project("project",
            description="Test Project Description",
            visibility="private",
            version_control="Git",
            work_item_template="Agile")
        project_readers = project.id.apply(lambda id: azuredevops.get_group(project_id=id,
            name="Readers"))
        project_contributors = project.id.apply(lambda id: azuredevops.get_group(project_id=id,
            name="Contributors"))
        project_administrators = project.id.apply(lambda id: azuredevops.get_group(project_id=id,
            name="Project administrators"))
        project_git_root_permissions = azuredevops.GitPermissions("project-git-root-permissions",
            project_id=project.id,
            principal=project_readers.id,
            permissions={
                "CreateRepository": "Deny",
                "DeleteRepository": "Deny",
                "RenameRepository": "NotSet",
            })
        git_repo = azuredevops.Git("git-repo",
            project_id=project.id,
            default_branch="refs/heads/master",
            initialization=azuredevops.GitInitializationArgs(
                init_type="Clean",
            ))
        project_git_repo_permissions = azuredevops.GitPermissions("project-git-repo-permissions",
            project_id=git_repo.project_id,
            repository_id=git_repo.id,
            principal=project_administrators.id,
            permissions={
                "RemoveOthersLocks": "Allow",
                "ManagePermissions": "Deny",
                "CreateTag": "Deny",
                "CreateBranch": "NotSet",
            })
        project_git_branch_permissions = azuredevops.GitPermissions("project-git-branch-permissions",
            project_id=git_repo.project_id,
            repository_id=git_repo.id,
            branch_name="master",
            principal=project_contributors.id,
            permissions={
                "RemoveOthersLocks": "Allow",
                "ForcePush": "Deny",
            })
        ```
        ## Relevant Links

        * [Azure DevOps Service REST API 5.1 - Security](https://docs.microsoft.com/en-us/rest/api/azure/devops/security/?view=azure-devops-rest-5.1)

        ## PAT Permissions Required

        - **Project & Team**: vso.security_manage - Grants the ability to read, write, and manage security permissions.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] branch_name: The name of the branch to assign the permissions.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] permissions: the permissions to assign. The follwing permissions are available
        :param pulumi.Input[str] principal: The **group** principal to assign the permissions.
        :param pulumi.Input[str] project_id: The ID of the project to assign the permissions.
        :param pulumi.Input[bool] replace: Replace (`true`) or merge (`false`) the permissions. Default: `true`
        :param pulumi.Input[str] repository_id: The ID of the GIT repository to assign the permissions
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

            __props__['branch_name'] = branch_name
            if permissions is None:
                raise TypeError("Missing required property 'permissions'")
            __props__['permissions'] = permissions
            if principal is None:
                raise TypeError("Missing required property 'principal'")
            __props__['principal'] = principal
            if project_id is None:
                raise TypeError("Missing required property 'project_id'")
            __props__['project_id'] = project_id
            __props__['replace'] = replace
            __props__['repository_id'] = repository_id
        super(GitPermissions, __self__).__init__(
            'azuredevops:index/gitPermissions:GitPermissions',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            branch_name: Optional[pulumi.Input[str]] = None,
            permissions: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            principal: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            replace: Optional[pulumi.Input[bool]] = None,
            repository_id: Optional[pulumi.Input[str]] = None) -> 'GitPermissions':
        """
        Get an existing GitPermissions resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] branch_name: The name of the branch to assign the permissions.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] permissions: the permissions to assign. The follwing permissions are available
        :param pulumi.Input[str] principal: The **group** principal to assign the permissions.
        :param pulumi.Input[str] project_id: The ID of the project to assign the permissions.
        :param pulumi.Input[bool] replace: Replace (`true`) or merge (`false`) the permissions. Default: `true`
        :param pulumi.Input[str] repository_id: The ID of the GIT repository to assign the permissions
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["branch_name"] = branch_name
        __props__["permissions"] = permissions
        __props__["principal"] = principal
        __props__["project_id"] = project_id
        __props__["replace"] = replace
        __props__["repository_id"] = repository_id
        return GitPermissions(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the branch to assign the permissions.
        """
        return pulumi.get(self, "branch_name")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Mapping[str, str]]:
        """
        the permissions to assign. The follwing permissions are available
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter
    def principal(self) -> pulumi.Output[str]:
        """
        The **group** principal to assign the permissions.
        """
        return pulumi.get(self, "principal")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The ID of the project to assign the permissions.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def replace(self) -> pulumi.Output[Optional[bool]]:
        """
        Replace (`true`) or merge (`false`) the permissions. Default: `true`
        """
        return pulumi.get(self, "replace")

    @property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the GIT repository to assign the permissions
        """
        return pulumi.get(self, "repository_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


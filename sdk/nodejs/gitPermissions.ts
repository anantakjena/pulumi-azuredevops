// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Manages permissions for Git repositories.
 *
 * > **Note** Permissions can be assigned to group principals and not to single user principals.
 *
 * ## Permission levels
 *
 * Permission for Git Repositories within Azure DevOps can be applied on three different levels.
 * Those levels are reflected by specifying (or omitting) values for the arguments `projectId`, `repositoryId` and `branchName`.
 *
 * ### Project level
 *
 * Permissions for all Git Repositories inside a project (existing or newly created ones) are specified, if only the argument `projectId` has a value.
 *
 * #### Example usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuredevops from "@pulumi/azuredevops";
 *
 * const project_git_root_permissions = new azuredevops.GitPermissions("project-git-root-permissions", {
 *     projectId: azuredevops_project.project.id,
 *     principal: data.azuredevops_group["project-readers"].id,
 *     permissions: {
 *         CreateRepository: "Deny",
 *         DeleteRepository: "Deny",
 *         RenameRepository: "NotSet",
 *     },
 * });
 * ```
 *
 * ### Repository level
 *
 * Permissions for a specific Git Repository and all existing or newly created branches are specified if the arguments `projectId` and `repositoryId` are set.
 *
 * #### Example usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuredevops from "@pulumi/azuredevops";
 *
 * const project_git_repo_permissions = new azuredevops.GitPermissions("project-git-repo-permissions", {
 *     projectId: data.azuredevops_git_repository["git-repo"].project_id,
 *     repositoryId: data.azuredevops_git_repository["git-repo"].id,
 *     principal: data.azuredevops_group["project-administrators"].id,
 *     permissions: {
 *         RemoveOthersLocks: "Allow",
 *         ManagePermissions: "Deny",
 *         CreateTag: "Deny",
 *         CreateBranch: "NotSet",
 *     },
 * });
 * ```
 *
 * ### Branch level
 *
 * Permissions for a specific branch inside a Git Repository are specified if all above mentioned the arguments are set.
 *
 * #### Example usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuredevops from "@pulumi/azuredevops";
 *
 * const project_git_branch_permissions = new azuredevops.GitPermissions("project-git-branch-permissions", {
 *     projectId: data.azuredevops_git_repository["git-repo"].project_id,
 *     repositoryId: data.azuredevops_git_repository["git-repo"].id,
 *     branchName: "refs/heads/master",
 *     principal: data.azuredevops_group["project-contributors"].id,
 *     permissions: {
 *         RemoveOthersLocks: "Allow",
 *         ForcePush: "Deny",
 *     },
 * });
 * ```
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuredevops from "@pulumi/azuredevops";
 *
 * const project = new azuredevops.Project("project", {
 *     description: "Test Project Description",
 *     visibility: "private",
 *     versionControl: "Git",
 *     workItemTemplate: "Agile",
 * });
 * const project-readers = project.id.apply(id => azuredevops.getGroup({
 *     projectId: id,
 *     name: "Readers",
 * }));
 * const project-contributors = project.id.apply(id => azuredevops.getGroup({
 *     projectId: id,
 *     name: "Contributors",
 * }));
 * const project-administrators = project.id.apply(id => azuredevops.getGroup({
 *     projectId: id,
 *     name: "Project administrators",
 * }));
 * const project_git_root_permissions = new azuredevops.GitPermissions("project-git-root-permissions", {
 *     projectId: project.id,
 *     principal: project_readers.id,
 *     permissions: {
 *         CreateRepository: "Deny",
 *         DeleteRepository: "Deny",
 *         RenameRepository: "NotSet",
 *     },
 * });
 * const git_repo = new azuredevops.Git("git-repo", {
 *     projectId: project.id,
 *     defaultBranch: "refs/heads/master",
 *     initialization: {
 *         initType: "Clean",
 *     },
 * });
 * const project_git_repo_permissions = new azuredevops.GitPermissions("project-git-repo-permissions", {
 *     projectId: git_repo.projectId,
 *     repositoryId: git_repo.id,
 *     principal: project_administrators.id,
 *     permissions: {
 *         RemoveOthersLocks: "Allow",
 *         ManagePermissions: "Deny",
 *         CreateTag: "Deny",
 *         CreateBranch: "NotSet",
 *     },
 * });
 * const project_git_branch_permissions = new azuredevops.GitPermissions("project-git-branch-permissions", {
 *     projectId: git_repo.projectId,
 *     repositoryId: git_repo.id,
 *     branchName: "master",
 *     principal: project_contributors.id,
 *     permissions: {
 *         RemoveOthersLocks: "Allow",
 *         ForcePush: "Deny",
 *     },
 * });
 * ```
 * ## Relevant Links
 *
 * * [Azure DevOps Service REST API 5.1 - Security](https://docs.microsoft.com/en-us/rest/api/azure/devops/security/?view=azure-devops-rest-5.1)
 *
 * ## PAT Permissions Required
 *
 * - **Project & Team**: vso.security_manage - Grants the ability to read, write, and manage security permissions.
 */
export class GitPermissions extends pulumi.CustomResource {
    /**
     * Get an existing GitPermissions resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GitPermissionsState, opts?: pulumi.CustomResourceOptions): GitPermissions {
        return new GitPermissions(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azuredevops:index/gitPermissions:GitPermissions';

    /**
     * Returns true if the given object is an instance of GitPermissions.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is GitPermissions {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === GitPermissions.__pulumiType;
    }

    /**
     * The name of the branch to assign the permissions.
     */
    public readonly branchName!: pulumi.Output<string | undefined>;
    /**
     * the permissions to assign. The follwing permissions are available
     */
    public readonly permissions!: pulumi.Output<{[key: string]: string}>;
    /**
     * The **group** principal to assign the permissions.
     */
    public readonly principal!: pulumi.Output<string>;
    /**
     * The ID of the project to assign the permissions.
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * Replace (`true`) or merge (`false`) the permissions. Default: `true`
     */
    public readonly replace!: pulumi.Output<boolean | undefined>;
    /**
     * The ID of the GIT repository to assign the permissions
     */
    public readonly repositoryId!: pulumi.Output<string | undefined>;

    /**
     * Create a GitPermissions resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GitPermissionsArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GitPermissionsArgs | GitPermissionsState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as GitPermissionsState | undefined;
            inputs["branchName"] = state ? state.branchName : undefined;
            inputs["permissions"] = state ? state.permissions : undefined;
            inputs["principal"] = state ? state.principal : undefined;
            inputs["projectId"] = state ? state.projectId : undefined;
            inputs["replace"] = state ? state.replace : undefined;
            inputs["repositoryId"] = state ? state.repositoryId : undefined;
        } else {
            const args = argsOrState as GitPermissionsArgs | undefined;
            if (!args || args.permissions === undefined) {
                throw new Error("Missing required property 'permissions'");
            }
            if (!args || args.principal === undefined) {
                throw new Error("Missing required property 'principal'");
            }
            if (!args || args.projectId === undefined) {
                throw new Error("Missing required property 'projectId'");
            }
            inputs["branchName"] = args ? args.branchName : undefined;
            inputs["permissions"] = args ? args.permissions : undefined;
            inputs["principal"] = args ? args.principal : undefined;
            inputs["projectId"] = args ? args.projectId : undefined;
            inputs["replace"] = args ? args.replace : undefined;
            inputs["repositoryId"] = args ? args.repositoryId : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(GitPermissions.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering GitPermissions resources.
 */
export interface GitPermissionsState {
    /**
     * The name of the branch to assign the permissions.
     */
    readonly branchName?: pulumi.Input<string>;
    /**
     * the permissions to assign. The follwing permissions are available
     */
    readonly permissions?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The **group** principal to assign the permissions.
     */
    readonly principal?: pulumi.Input<string>;
    /**
     * The ID of the project to assign the permissions.
     */
    readonly projectId?: pulumi.Input<string>;
    /**
     * Replace (`true`) or merge (`false`) the permissions. Default: `true`
     */
    readonly replace?: pulumi.Input<boolean>;
    /**
     * The ID of the GIT repository to assign the permissions
     */
    readonly repositoryId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a GitPermissions resource.
 */
export interface GitPermissionsArgs {
    /**
     * The name of the branch to assign the permissions.
     */
    readonly branchName?: pulumi.Input<string>;
    /**
     * the permissions to assign. The follwing permissions are available
     */
    readonly permissions: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The **group** principal to assign the permissions.
     */
    readonly principal: pulumi.Input<string>;
    /**
     * The ID of the project to assign the permissions.
     */
    readonly projectId: pulumi.Input<string>;
    /**
     * Replace (`true`) or merge (`false`) the permissions. Default: `true`
     */
    readonly replace?: pulumi.Input<boolean>;
    /**
     * The ID of the GIT repository to assign the permissions
     */
    readonly repositoryId?: pulumi.Input<string>;
}
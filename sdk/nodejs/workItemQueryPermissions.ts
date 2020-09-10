// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Manages permissions for Work Item Queries.
 *
 * > **Note** Permissions can be assigned to group principals and not to single user principals.
 *
 * ## Permission levels
 *
 * Permission for Work Item Queries within Azure DevOps can be applied on two different levels.
 * Those levels are reflected by specifying (or omitting) values for the arguments `projectId` and `path`.
 *
 * ### Project level
 *
 * Permissions for all Work Item Queries inside a project (existing or newly created ones) are specified, if only the argument `projectId` has a value.
 *
 * #### Example usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuredevops from "@pulumi/azuredevops";
 *
 * const project_wiq_root_permissions = new azuredevops.WorkItemQueryPermissions("project-wiq-root-permissions", {
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
 * ### Shared Queries folder level
 *
 * Permissions for a specific folder inside Shared Queries are specified if the arguments `projectId` and `path` are set.
 *
 * > **Note** To set permissions for the Shared Queries folder itself use `/` as path value
 *
 * #### Example usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuredevops from "@pulumi/azuredevops";
 *
 * const wiq_folder_permissions = new azuredevops.WorkItemQueryPermissions("wiq-folder-permissions", {
 *     projectId: azuredevops_project.project.id,
 *     path: "/Team",
 *     principal: data.azuredevops_group["project-readers"].id,
 *     permissions: {
 *         Contribute: "Allow",
 *         Delete: "Deny",
 *         Read: "NotSet",
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
 * const wiq_project_permissions = new azuredevops.WorkItemQueryPermissions("wiq-project-permissions", {
 *     projectId: project.id,
 *     principal: project_readers.id,
 *     permissions: {
 *         Read: "Allow",
 *         Delete: "Deny",
 *         Contribute: "Deny",
 *         ManagePermissions: "Deny",
 *     },
 * });
 * const wiq_sharedqueries_permissions = new azuredevops.WorkItemQueryPermissions("wiq-sharedqueries-permissions", {
 *     projectId: project.id,
 *     path: "/",
 *     principal: project_contributors.id,
 *     permissions: {
 *         Read: "Allow",
 *         Delete: "Deny",
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
export class WorkItemQueryPermissions extends pulumi.CustomResource {
    /**
     * Get an existing WorkItemQueryPermissions resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WorkItemQueryPermissionsState, opts?: pulumi.CustomResourceOptions): WorkItemQueryPermissions {
        return new WorkItemQueryPermissions(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azuredevops:index/workItemQueryPermissions:WorkItemQueryPermissions';

    /**
     * Returns true if the given object is an instance of WorkItemQueryPermissions.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is WorkItemQueryPermissions {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === WorkItemQueryPermissions.__pulumiType;
    }

    /**
     * Path to a query or folder beneath `Shared Queries`
     */
    public readonly path!: pulumi.Output<string | undefined>;
    /**
     * the permissions to assign. The following permissions are available
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
     * Create a WorkItemQueryPermissions resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: WorkItemQueryPermissionsArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: WorkItemQueryPermissionsArgs | WorkItemQueryPermissionsState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as WorkItemQueryPermissionsState | undefined;
            inputs["path"] = state ? state.path : undefined;
            inputs["permissions"] = state ? state.permissions : undefined;
            inputs["principal"] = state ? state.principal : undefined;
            inputs["projectId"] = state ? state.projectId : undefined;
            inputs["replace"] = state ? state.replace : undefined;
        } else {
            const args = argsOrState as WorkItemQueryPermissionsArgs | undefined;
            if (!args || args.permissions === undefined) {
                throw new Error("Missing required property 'permissions'");
            }
            if (!args || args.principal === undefined) {
                throw new Error("Missing required property 'principal'");
            }
            if (!args || args.projectId === undefined) {
                throw new Error("Missing required property 'projectId'");
            }
            inputs["path"] = args ? args.path : undefined;
            inputs["permissions"] = args ? args.permissions : undefined;
            inputs["principal"] = args ? args.principal : undefined;
            inputs["projectId"] = args ? args.projectId : undefined;
            inputs["replace"] = args ? args.replace : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(WorkItemQueryPermissions.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering WorkItemQueryPermissions resources.
 */
export interface WorkItemQueryPermissionsState {
    /**
     * Path to a query or folder beneath `Shared Queries`
     */
    readonly path?: pulumi.Input<string>;
    /**
     * the permissions to assign. The following permissions are available
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
}

/**
 * The set of arguments for constructing a WorkItemQueryPermissions resource.
 */
export interface WorkItemQueryPermissionsArgs {
    /**
     * Path to a query or folder beneath `Shared Queries`
     */
    readonly path?: pulumi.Input<string>;
    /**
     * the permissions to assign. The following permissions are available
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
}
// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Use this data source to access information about an existing Group within Azure DevOps
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuredevops from "@pulumi/azuredevops";
 *
 * const project = azuredevops.Core.getProject({
 *     projectName: "contoso-project",
 * });
 * const test = project.then(project => azuredevops.Identities.getGroup({
 *     projectId: project.id,
 *     name: "Test Group",
 * }));
 * export const groupId = test.then(test => test.id);
 * export const groupDescriptor = test.then(test => test.descriptor);
 * ```
 * ## Relevant Links
 *
 * * [Azure DevOps Service REST API 5.1 - Groups - Get](https://docs.microsoft.com/en-us/rest/api/azure/devops/graph/groups/get?view=azure-devops-rest-5.1)
 */
export function getGroup(args: GetGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetGroupResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("azuredevops:Identities/getGroup:getGroup", {
        "name": args.name,
        "projectId": args.projectId,
    }, opts);
}

/**
 * A collection of arguments for invoking getGroup.
 */
export interface GetGroupArgs {
    /**
     * The Group Name.
     */
    readonly name: string;
    /**
     * The Project Id.
     */
    readonly projectId: string;
}

/**
 * A collection of values returned by getGroup.
 */
export interface GetGroupResult {
    /**
     * The Descriptor is the primary way to reference the graph subject. This field will uniquely identify the same graph subject across both Accounts and Organizations.
     */
    readonly descriptor: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly name: string;
    readonly projectId: string;
}

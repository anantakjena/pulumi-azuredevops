// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Use this data source to access information about existing Agent Pools within Azure DevOps.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azuredevops from "@pulumi/azuredevops";
 *
 * const pools = azuredevops.getPools({});
 * export const agentPoolName = pools.then(pools => pools.agentPools.map(__item => __item.name));
 * export const autoProvision = pools.then(pools => pools.agentPools.map(__item => __item.autoProvision));
 * export const poolType = pools.then(pools => pools.agentPools.map(__item => __item.poolType));
 * ```
 * ## Relevant Links
 *
 * - [Azure DevOps Service REST API 5.1 - Agent Pools - Get](https://docs.microsoft.com/en-us/rest/api/azure/devops/distributedtask/pools/get?view=azure-devops-rest-5.1)
 */
/** @deprecated azuredevops.agent.getPools has been deprecated in favor of azuredevops.getPools */
export function getPools(opts?: pulumi.InvokeOptions): Promise<GetPoolsResult> {
    pulumi.log.warn("getPools is deprecated: azuredevops.agent.getPools has been deprecated in favor of azuredevops.getPools")
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("azuredevops:Agent/getPools:getPools", {
    }, opts);
}

/**
 * A collection of values returned by getPools.
 */
export interface GetPoolsResult {
    /**
     * A list of existing agent pools in your Azure DevOps Organization with the following details about every agent pool:
     */
    readonly agentPools: outputs.Agent.GetPoolsAgentPool[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}

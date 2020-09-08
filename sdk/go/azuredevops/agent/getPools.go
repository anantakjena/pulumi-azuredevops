// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package agent

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to access information about existing Agent Pools within Azure DevOps.
//
// ## Relevant Links
//
// - [Azure DevOps Service REST API 5.1 - Agent Pools - Get](https://docs.microsoft.com/en-us/rest/api/azure/devops/distributedtask/pools/get?view=azure-devops-rest-5.1)
func GetPools(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*GetPoolsResult, error) {
	var rv GetPoolsResult
	err := ctx.Invoke("azuredevops:Agent/getPools:getPools", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getPools.
type GetPoolsResult struct {
	// A list of existing agent pools in your Azure DevOps Organization with the following details about every agent pool:
	AgentPools []GetPoolsAgentPool `pulumi:"agentPools"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
}
// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package core

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to access information about existing Projects within Azure DevOps.
//
// ## Relevant Links
//
// - [Azure DevOps Service REST API 5.1 - Projects - Get](https://docs.microsoft.com/en-us/rest/api/azure/devops/core/projects/get?view=azure-devops-rest-5.1)
func GetProjects(ctx *pulumi.Context, args *GetProjectsArgs, opts ...pulumi.InvokeOption) (*GetProjectsResult, error) {
	var rv GetProjectsResult
	err := ctx.Invoke("azuredevops:Core/getProjects:getProjects", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getProjects.
type GetProjectsArgs struct {
	// Name of the Project, if not specified all projects will be returned.
	ProjectName *string `pulumi:"projectName"`
	// State of the Project, if not specified all projects will be returned. Valid values are `all`, `deleting`, `new`, `wellFormed`, `createPending`, `unchanged`,`deleted`.
	State *string `pulumi:"state"`
}

// A collection of values returned by getProjects.
type GetProjectsResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id          string  `pulumi:"id"`
	ProjectName *string `pulumi:"projectName"`
	// A list of existing projects in your Azure DevOps Organization with details about every project which includes:
	Projects []GetProjectsProject `pulumi:"projects"`
	// Project state.
	State *string `pulumi:"state"`
}
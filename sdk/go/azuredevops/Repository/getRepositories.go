// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package Repository

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to access information about an existing Git Repositories within Azure DevOps.
//
// ## Example Usage
//
//
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		project, err := Core.LookupProject(ctx, &Core.LookupProjectArgs{
// 			ProjectName: "contoso-project",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		allRepos, err := Repository.LookupRepositories(ctx, &Repository.LookupRepositoriesArgs{
// 			ProjectId:     project.Id,
// 			IncludeHidden: true,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		singleRepo, err := Repository.LookupRepositories(ctx, &Repository.LookupRepositoriesArgs{
// 			ProjectId: project.Id,
// 			Name:      "contoso-repo",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Relevant Links
//
// - [Azure DevOps Service REST API 5.1 - Git API](https://docs.microsoft.com/en-us/rest/api/azure/devops/git/?view=azure-devops-rest-5.1)
func GetRepositories(ctx *pulumi.Context, args *GetRepositoriesArgs, opts ...pulumi.InvokeOption) (*GetRepositoriesResult, error) {
	var rv GetRepositoriesResult
	err := ctx.Invoke("azuredevops:Repository/getRepositories:getRepositories", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getRepositories.
type GetRepositoriesArgs struct {
	IncludeHidden *bool   `pulumi:"includeHidden"`
	Name          *string `pulumi:"name"`
	ProjectId     *string `pulumi:"projectId"`
}

// A collection of values returned by getRepositories.
type GetRepositoriesResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id            string                      `pulumi:"id"`
	IncludeHidden *bool                       `pulumi:"includeHidden"`
	Name          *string                     `pulumi:"name"`
	ProjectId     *string                     `pulumi:"projectId"`
	Repositories  []GetRepositoriesRepository `pulumi:"repositories"`
}
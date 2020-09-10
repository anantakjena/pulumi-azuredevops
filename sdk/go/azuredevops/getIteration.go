// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package azuredevops

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func GetIteration(ctx *pulumi.Context, args *GetIterationArgs, opts ...pulumi.InvokeOption) (*GetIterationResult, error) {
	var rv GetIterationResult
	err := ctx.Invoke("azuredevops:index/getIteration:getIteration", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getIteration.
type GetIterationArgs struct {
	FetchChildren *bool   `pulumi:"fetchChildren"`
	Path          *string `pulumi:"path"`
	ProjectId     string  `pulumi:"projectId"`
}

// A collection of values returned by getIteration.
type GetIterationResult struct {
	Childrens     []GetIterationChildren `pulumi:"childrens"`
	FetchChildren *bool                  `pulumi:"fetchChildren"`
	HasChildren   bool                   `pulumi:"hasChildren"`
	// The provider-assigned unique ID for this managed resource.
	Id        string `pulumi:"id"`
	Name      string `pulumi:"name"`
	Path      string `pulumi:"path"`
	ProjectId string `pulumi:"projectId"`
}
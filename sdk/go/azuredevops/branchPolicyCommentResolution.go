// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package azuredevops

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Configure a comment resolution policy for your branch within Azure DevOps project.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azuredevops/sdk/go/azuredevops"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		project, err := azuredevops.NewProject(ctx, "project", nil)
// 		if err != nil {
// 			return err
// 		}
// 		git, err := azuredevops.NewGit(ctx, "git", &azuredevops.GitArgs{
// 			ProjectId: project.ID(),
// 			Initialization: &azuredevops.GitInitializationArgs{
// 				InitType: pulumi.String("Clean"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = azuredevops.NewBranchPolicyCommentResolution(ctx, "branchPolicyCommentResolution", &azuredevops.BranchPolicyCommentResolutionArgs{
// 			ProjectId: project.ID(),
// 			Enabled:   pulumi.Bool(true),
// 			Blocking:  pulumi.Bool(true),
// 			Settings: &azuredevops.BranchPolicyCommentResolutionSettingsArgs{
// 				Scopes: azuredevops.BranchPolicyCommentResolutionSettingsScopeArray{
// 					&azuredevops.BranchPolicyCommentResolutionSettingsScopeArgs{
// 						RepositoryId:  git.ID(),
// 						RepositoryRef: git.DefaultBranch,
// 						MatchType:     pulumi.String("Exact"),
// 					},
// 					&azuredevops.BranchPolicyCommentResolutionSettingsScopeArgs{
// 						RepositoryId:  git.ID(),
// 						RepositoryRef: pulumi.String("refs/heads/releases"),
// 						MatchType:     pulumi.String("Prefix"),
// 					},
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ## Relevant Links
//
// - [Azure DevOps Service REST API 5.1 - Policy Configurations](https://docs.microsoft.com/en-us/rest/api/azure/devops/policy/configurations/create?view=azure-devops-rest-5.1)
type BranchPolicyCommentResolution struct {
	pulumi.CustomResourceState

	// A flag indicating if the policy should be blocking. Defaults to `true`.
	Blocking pulumi.BoolPtrOutput `pulumi:"blocking"`
	// A flag indicating if the policy should be enabled. Defaults to `true`.
	Enabled pulumi.BoolPtrOutput `pulumi:"enabled"`
	// The ID of the project in which the policy will be created.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// Configuration for the policy. This block must be defined exactly once.
	Settings BranchPolicyCommentResolutionSettingsOutput `pulumi:"settings"`
}

// NewBranchPolicyCommentResolution registers a new resource with the given unique name, arguments, and options.
func NewBranchPolicyCommentResolution(ctx *pulumi.Context,
	name string, args *BranchPolicyCommentResolutionArgs, opts ...pulumi.ResourceOption) (*BranchPolicyCommentResolution, error) {
	if args == nil || args.ProjectId == nil {
		return nil, errors.New("missing required argument 'ProjectId'")
	}
	if args == nil || args.Settings == nil {
		return nil, errors.New("missing required argument 'Settings'")
	}
	if args == nil {
		args = &BranchPolicyCommentResolutionArgs{}
	}
	var resource BranchPolicyCommentResolution
	err := ctx.RegisterResource("azuredevops:index/branchPolicyCommentResolution:BranchPolicyCommentResolution", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetBranchPolicyCommentResolution gets an existing BranchPolicyCommentResolution resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBranchPolicyCommentResolution(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *BranchPolicyCommentResolutionState, opts ...pulumi.ResourceOption) (*BranchPolicyCommentResolution, error) {
	var resource BranchPolicyCommentResolution
	err := ctx.ReadResource("azuredevops:index/branchPolicyCommentResolution:BranchPolicyCommentResolution", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering BranchPolicyCommentResolution resources.
type branchPolicyCommentResolutionState struct {
	// A flag indicating if the policy should be blocking. Defaults to `true`.
	Blocking *bool `pulumi:"blocking"`
	// A flag indicating if the policy should be enabled. Defaults to `true`.
	Enabled *bool `pulumi:"enabled"`
	// The ID of the project in which the policy will be created.
	ProjectId *string `pulumi:"projectId"`
	// Configuration for the policy. This block must be defined exactly once.
	Settings *BranchPolicyCommentResolutionSettings `pulumi:"settings"`
}

type BranchPolicyCommentResolutionState struct {
	// A flag indicating if the policy should be blocking. Defaults to `true`.
	Blocking pulumi.BoolPtrInput
	// A flag indicating if the policy should be enabled. Defaults to `true`.
	Enabled pulumi.BoolPtrInput
	// The ID of the project in which the policy will be created.
	ProjectId pulumi.StringPtrInput
	// Configuration for the policy. This block must be defined exactly once.
	Settings BranchPolicyCommentResolutionSettingsPtrInput
}

func (BranchPolicyCommentResolutionState) ElementType() reflect.Type {
	return reflect.TypeOf((*branchPolicyCommentResolutionState)(nil)).Elem()
}

type branchPolicyCommentResolutionArgs struct {
	// A flag indicating if the policy should be blocking. Defaults to `true`.
	Blocking *bool `pulumi:"blocking"`
	// A flag indicating if the policy should be enabled. Defaults to `true`.
	Enabled *bool `pulumi:"enabled"`
	// The ID of the project in which the policy will be created.
	ProjectId string `pulumi:"projectId"`
	// Configuration for the policy. This block must be defined exactly once.
	Settings BranchPolicyCommentResolutionSettings `pulumi:"settings"`
}

// The set of arguments for constructing a BranchPolicyCommentResolution resource.
type BranchPolicyCommentResolutionArgs struct {
	// A flag indicating if the policy should be blocking. Defaults to `true`.
	Blocking pulumi.BoolPtrInput
	// A flag indicating if the policy should be enabled. Defaults to `true`.
	Enabled pulumi.BoolPtrInput
	// The ID of the project in which the policy will be created.
	ProjectId pulumi.StringInput
	// Configuration for the policy. This block must be defined exactly once.
	Settings BranchPolicyCommentResolutionSettingsInput
}

func (BranchPolicyCommentResolutionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*branchPolicyCommentResolutionArgs)(nil)).Elem()
}
// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package Policy

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a build validation branch policy within Azure DevOps.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azuredevops/sdk/go/azuredevops/Build"
// 	"github.com/pulumi/pulumi-azuredevops/sdk/go/azuredevops/Core"
// 	"github.com/pulumi/pulumi-azuredevops/sdk/go/azuredevops/Policy"
// 	"github.com/pulumi/pulumi-azuredevops/sdk/go/azuredevops/Repository"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		project, err := Core.NewProject(ctx, "project", &Core.ProjectArgs{
// 			ProjectName: pulumi.String("Sample Project"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		git, err := Repository.NewGit(ctx, "git", &Repository.GitArgs{
// 			ProjectId: project.ID(),
// 			Initialization: &Repository.GitInitializationArgs{
// 				InitType: pulumi.String("Clean"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		buildDefinition, err := Build.NewBuildDefinition(ctx, "buildDefinition", &Build.BuildDefinitionArgs{
// 			ProjectId: project.ID(),
// 			Repository: &Build.BuildDefinitionRepositoryArgs{
// 				RepoType: pulumi.String("TfsGit"),
// 				RepoId:   git.ID(),
// 				YmlPath:  pulumi.String("azure-pipelines.yml"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = Policy.NewBranchPolicyBuildValidation(ctx, "branchPolicyBuildValidation", &Policy.BranchPolicyBuildValidationArgs{
// 			ProjectId: project.ID(),
// 			Enabled:   pulumi.Bool(true),
// 			Blocking:  pulumi.Bool(true),
// 			Settings: &Policy.BranchPolicyBuildValidationSettingsArgs{
// 				DisplayName:       pulumi.String("Don't break the build!"),
// 				BuildDefinitionId: buildDefinition.ID(),
// 				ValidDuration:     pulumi.Int(720),
// 				Scopes: Policy.BranchPolicyBuildValidationSettingsScopeArray{
// 					&Policy.BranchPolicyBuildValidationSettingsScopeArgs{
// 						RepositoryId:  git.ID(),
// 						RepositoryRef: git.DefaultBranch,
// 						MatchType:     pulumi.String("Exact"),
// 					},
// 					&Policy.BranchPolicyBuildValidationSettingsScopeArgs{
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
// * [Azure DevOps Service REST API 5.1 - Policy Configurations](https://docs.microsoft.com/en-us/rest/api/azure/devops/policy/configurations/create?view=azure-devops-rest-5.1)
type BranchPolicyBuildValidation struct {
	pulumi.CustomResourceState

	// A flag indicating if the policy should be blocking. Defaults to `true`.
	Blocking pulumi.BoolPtrOutput `pulumi:"blocking"`
	// A flag indicating if the policy should be enabled. Defaults to `true`.
	Enabled pulumi.BoolPtrOutput `pulumi:"enabled"`
	// The ID of the project in which the policy will be created.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// Configuration for the policy. This block must be defined exactly once.
	Settings BranchPolicyBuildValidationSettingsOutput `pulumi:"settings"`
}

// NewBranchPolicyBuildValidation registers a new resource with the given unique name, arguments, and options.
func NewBranchPolicyBuildValidation(ctx *pulumi.Context,
	name string, args *BranchPolicyBuildValidationArgs, opts ...pulumi.ResourceOption) (*BranchPolicyBuildValidation, error) {
	if args == nil || args.ProjectId == nil {
		return nil, errors.New("missing required argument 'ProjectId'")
	}
	if args == nil || args.Settings == nil {
		return nil, errors.New("missing required argument 'Settings'")
	}
	if args == nil {
		args = &BranchPolicyBuildValidationArgs{}
	}
	var resource BranchPolicyBuildValidation
	err := ctx.RegisterResource("azuredevops:Policy/branchPolicyBuildValidation:BranchPolicyBuildValidation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetBranchPolicyBuildValidation gets an existing BranchPolicyBuildValidation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBranchPolicyBuildValidation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *BranchPolicyBuildValidationState, opts ...pulumi.ResourceOption) (*BranchPolicyBuildValidation, error) {
	var resource BranchPolicyBuildValidation
	err := ctx.ReadResource("azuredevops:Policy/branchPolicyBuildValidation:BranchPolicyBuildValidation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering BranchPolicyBuildValidation resources.
type branchPolicyBuildValidationState struct {
	// A flag indicating if the policy should be blocking. Defaults to `true`.
	Blocking *bool `pulumi:"blocking"`
	// A flag indicating if the policy should be enabled. Defaults to `true`.
	Enabled *bool `pulumi:"enabled"`
	// The ID of the project in which the policy will be created.
	ProjectId *string `pulumi:"projectId"`
	// Configuration for the policy. This block must be defined exactly once.
	Settings *BranchPolicyBuildValidationSettings `pulumi:"settings"`
}

type BranchPolicyBuildValidationState struct {
	// A flag indicating if the policy should be blocking. Defaults to `true`.
	Blocking pulumi.BoolPtrInput
	// A flag indicating if the policy should be enabled. Defaults to `true`.
	Enabled pulumi.BoolPtrInput
	// The ID of the project in which the policy will be created.
	ProjectId pulumi.StringPtrInput
	// Configuration for the policy. This block must be defined exactly once.
	Settings BranchPolicyBuildValidationSettingsPtrInput
}

func (BranchPolicyBuildValidationState) ElementType() reflect.Type {
	return reflect.TypeOf((*branchPolicyBuildValidationState)(nil)).Elem()
}

type branchPolicyBuildValidationArgs struct {
	// A flag indicating if the policy should be blocking. Defaults to `true`.
	Blocking *bool `pulumi:"blocking"`
	// A flag indicating if the policy should be enabled. Defaults to `true`.
	Enabled *bool `pulumi:"enabled"`
	// The ID of the project in which the policy will be created.
	ProjectId string `pulumi:"projectId"`
	// Configuration for the policy. This block must be defined exactly once.
	Settings BranchPolicyBuildValidationSettings `pulumi:"settings"`
}

// The set of arguments for constructing a BranchPolicyBuildValidation resource.
type BranchPolicyBuildValidationArgs struct {
	// A flag indicating if the policy should be blocking. Defaults to `true`.
	Blocking pulumi.BoolPtrInput
	// A flag indicating if the policy should be enabled. Defaults to `true`.
	Enabled pulumi.BoolPtrInput
	// The ID of the project in which the policy will be created.
	ProjectId pulumi.StringInput
	// Configuration for the policy. This block must be defined exactly once.
	Settings BranchPolicyBuildValidationSettingsInput
}

func (BranchPolicyBuildValidationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*branchPolicyBuildValidationArgs)(nil)).Elem()
}

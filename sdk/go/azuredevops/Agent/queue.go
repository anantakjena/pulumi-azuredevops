// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package Agent

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages an agent queue within Azure DevOps. In the UI, this is equivelant to adding an
// Organization defined pool to a project.
//
// The created queue is not authorized for use by all pipeliens in the project. However,
// the `Security.ResourceAuthorization` resource can be used to grant authorization.
//
// ## Example Usage
//
//
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azuredevops/sdk/go/azuredevops/Agent"
// 	"github.com/pulumi/pulumi-azuredevops/sdk/go/azuredevops/Core"
// 	"github.com/pulumi/pulumi-azuredevops/sdk/go/azuredevops/Security"
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
// 		pool, err := Agent.LookupPool(ctx, &Agent.LookupPoolArgs{
// 			Name: "contoso-pool",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		queue, err := Agent.NewQueue(ctx, "queue", &Agent.QueueArgs{
// 			ProjectId:   project.ID(),
// 			AgentPoolId: pulumi.Int(pool.Id),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		auth, err := Security.NewResourceAuthorization(ctx, "auth", &Security.ResourceAuthorizationArgs{
// 			ProjectId:  project.ID(),
// 			ResourceId: queue.ID(),
// 			Type:       pulumi.String("queue"),
// 			Authorized: pulumi.Bool(true),
// 		})
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
// * [Azure DevOps Service REST API 5.1 - Agent Queues](https://docs.microsoft.com/en-us/rest/api/azure/devops/distributedtask/queues?view=azure-devops-rest-5.1)
type Queue struct {
	pulumi.CustomResourceState

	// The ID of the organization agent pool.
	AgentPoolId pulumi.IntOutput `pulumi:"agentPoolId"`
	// The ID of the project in which to create the resource.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
}

// NewQueue registers a new resource with the given unique name, arguments, and options.
func NewQueue(ctx *pulumi.Context,
	name string, args *QueueArgs, opts ...pulumi.ResourceOption) (*Queue, error) {
	if args == nil || args.AgentPoolId == nil {
		return nil, errors.New("missing required argument 'AgentPoolId'")
	}
	if args == nil || args.ProjectId == nil {
		return nil, errors.New("missing required argument 'ProjectId'")
	}
	if args == nil {
		args = &QueueArgs{}
	}
	var resource Queue
	err := ctx.RegisterResource("azuredevops:Agent/queue:Queue", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetQueue gets an existing Queue resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetQueue(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *QueueState, opts ...pulumi.ResourceOption) (*Queue, error) {
	var resource Queue
	err := ctx.ReadResource("azuredevops:Agent/queue:Queue", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Queue resources.
type queueState struct {
	// The ID of the organization agent pool.
	AgentPoolId *int `pulumi:"agentPoolId"`
	// The ID of the project in which to create the resource.
	ProjectId *string `pulumi:"projectId"`
}

type QueueState struct {
	// The ID of the organization agent pool.
	AgentPoolId pulumi.IntPtrInput
	// The ID of the project in which to create the resource.
	ProjectId pulumi.StringPtrInput
}

func (QueueState) ElementType() reflect.Type {
	return reflect.TypeOf((*queueState)(nil)).Elem()
}

type queueArgs struct {
	// The ID of the organization agent pool.
	AgentPoolId int `pulumi:"agentPoolId"`
	// The ID of the project in which to create the resource.
	ProjectId string `pulumi:"projectId"`
}

// The set of arguments for constructing a Queue resource.
type QueueArgs struct {
	// The ID of the organization agent pool.
	AgentPoolId pulumi.IntInput
	// The ID of the project in which to create the resource.
	ProjectId pulumi.StringInput
}

func (QueueArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*queueArgs)(nil)).Elem()
}
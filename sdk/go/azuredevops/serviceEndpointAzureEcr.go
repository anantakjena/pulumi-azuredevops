// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package azuredevops

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a Azure Container Registry service endpoint within Azure DevOps.
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
// 		project, err := azuredevops.NewProject(ctx, "project", &azuredevops.ProjectArgs{
// 			Visibility:       pulumi.String("private"),
// 			VersionControl:   pulumi.String("Git"),
// 			WorkItemTemplate: pulumi.String("Agile"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = azuredevops.NewServiceEndpointAzureEcr(ctx, "azurecr", &azuredevops.ServiceEndpointAzureEcrArgs{
// 			ProjectId:               project.ID(),
// 			ServiceEndpointName:     pulumi.String("Sample AzureCR"),
// 			ResourceGroup:           pulumi.String("sample-rg"),
// 			AzurecrSpnTenantid:      pulumi.String("72f987tg-95f1-87af-91bh-2d8jd091db47"),
// 			AzurecrName:             pulumi.String("sampleAcr"),
// 			AzurecrSubscriptionId:   pulumi.String("f7ooi795-c577-6210-9886-a5e898uue3gc"),
// 			AzurecrSubscriptionName: pulumi.String("sample"),
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
// - [Azure DevOps Service REST API 5.1 - Service Endpoints](https://docs.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-5.1)
// - [Azure Container Registry REST API](https://docs.microsoft.com/en-us/rest/api/containerregistry/)
type ServiceEndpointAzureEcr struct {
	pulumi.CustomResourceState

	Authorization pulumi.StringMapOutput `pulumi:"authorization"`
	// The Azure container registry name.
	AzurecrName pulumi.StringOutput `pulumi:"azurecrName"`
	// The tenant id of the service principal.
	AzurecrSpnTenantid pulumi.StringOutput `pulumi:"azurecrSpnTenantid"`
	// The subscription id of the Azure targets.
	AzurecrSubscriptionId pulumi.StringOutput `pulumi:"azurecrSubscriptionId"`
	// The subscription name of the Azure targets.
	AzurecrSubscriptionName pulumi.StringOutput `pulumi:"azurecrSubscriptionName"`
	// The name you will use to refer to this service connection in task inputs.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The project ID or project name.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// The resource group to which the container registry belongs.
	ResourceGroup pulumi.StringOutput `pulumi:"resourceGroup"`
	// The name you will use to refer to this service connection in task inputs.
	ServiceEndpointName pulumi.StringOutput `pulumi:"serviceEndpointName"`
}

// NewServiceEndpointAzureEcr registers a new resource with the given unique name, arguments, and options.
func NewServiceEndpointAzureEcr(ctx *pulumi.Context,
	name string, args *ServiceEndpointAzureEcrArgs, opts ...pulumi.ResourceOption) (*ServiceEndpointAzureEcr, error) {
	if args == nil || args.AzurecrName == nil {
		return nil, errors.New("missing required argument 'AzurecrName'")
	}
	if args == nil || args.AzurecrSpnTenantid == nil {
		return nil, errors.New("missing required argument 'AzurecrSpnTenantid'")
	}
	if args == nil || args.AzurecrSubscriptionId == nil {
		return nil, errors.New("missing required argument 'AzurecrSubscriptionId'")
	}
	if args == nil || args.AzurecrSubscriptionName == nil {
		return nil, errors.New("missing required argument 'AzurecrSubscriptionName'")
	}
	if args == nil || args.ProjectId == nil {
		return nil, errors.New("missing required argument 'ProjectId'")
	}
	if args == nil || args.ResourceGroup == nil {
		return nil, errors.New("missing required argument 'ResourceGroup'")
	}
	if args == nil || args.ServiceEndpointName == nil {
		return nil, errors.New("missing required argument 'ServiceEndpointName'")
	}
	if args == nil {
		args = &ServiceEndpointAzureEcrArgs{}
	}
	var resource ServiceEndpointAzureEcr
	err := ctx.RegisterResource("azuredevops:index/serviceEndpointAzureEcr:ServiceEndpointAzureEcr", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetServiceEndpointAzureEcr gets an existing ServiceEndpointAzureEcr resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetServiceEndpointAzureEcr(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServiceEndpointAzureEcrState, opts ...pulumi.ResourceOption) (*ServiceEndpointAzureEcr, error) {
	var resource ServiceEndpointAzureEcr
	err := ctx.ReadResource("azuredevops:index/serviceEndpointAzureEcr:ServiceEndpointAzureEcr", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ServiceEndpointAzureEcr resources.
type serviceEndpointAzureEcrState struct {
	Authorization map[string]string `pulumi:"authorization"`
	// The Azure container registry name.
	AzurecrName *string `pulumi:"azurecrName"`
	// The tenant id of the service principal.
	AzurecrSpnTenantid *string `pulumi:"azurecrSpnTenantid"`
	// The subscription id of the Azure targets.
	AzurecrSubscriptionId *string `pulumi:"azurecrSubscriptionId"`
	// The subscription name of the Azure targets.
	AzurecrSubscriptionName *string `pulumi:"azurecrSubscriptionName"`
	// The name you will use to refer to this service connection in task inputs.
	Description *string `pulumi:"description"`
	// The project ID or project name.
	ProjectId *string `pulumi:"projectId"`
	// The resource group to which the container registry belongs.
	ResourceGroup *string `pulumi:"resourceGroup"`
	// The name you will use to refer to this service connection in task inputs.
	ServiceEndpointName *string `pulumi:"serviceEndpointName"`
}

type ServiceEndpointAzureEcrState struct {
	Authorization pulumi.StringMapInput
	// The Azure container registry name.
	AzurecrName pulumi.StringPtrInput
	// The tenant id of the service principal.
	AzurecrSpnTenantid pulumi.StringPtrInput
	// The subscription id of the Azure targets.
	AzurecrSubscriptionId pulumi.StringPtrInput
	// The subscription name of the Azure targets.
	AzurecrSubscriptionName pulumi.StringPtrInput
	// The name you will use to refer to this service connection in task inputs.
	Description pulumi.StringPtrInput
	// The project ID or project name.
	ProjectId pulumi.StringPtrInput
	// The resource group to which the container registry belongs.
	ResourceGroup pulumi.StringPtrInput
	// The name you will use to refer to this service connection in task inputs.
	ServiceEndpointName pulumi.StringPtrInput
}

func (ServiceEndpointAzureEcrState) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceEndpointAzureEcrState)(nil)).Elem()
}

type serviceEndpointAzureEcrArgs struct {
	Authorization map[string]string `pulumi:"authorization"`
	// The Azure container registry name.
	AzurecrName string `pulumi:"azurecrName"`
	// The tenant id of the service principal.
	AzurecrSpnTenantid string `pulumi:"azurecrSpnTenantid"`
	// The subscription id of the Azure targets.
	AzurecrSubscriptionId string `pulumi:"azurecrSubscriptionId"`
	// The subscription name of the Azure targets.
	AzurecrSubscriptionName string `pulumi:"azurecrSubscriptionName"`
	// The name you will use to refer to this service connection in task inputs.
	Description *string `pulumi:"description"`
	// The project ID or project name.
	ProjectId string `pulumi:"projectId"`
	// The resource group to which the container registry belongs.
	ResourceGroup string `pulumi:"resourceGroup"`
	// The name you will use to refer to this service connection in task inputs.
	ServiceEndpointName string `pulumi:"serviceEndpointName"`
}

// The set of arguments for constructing a ServiceEndpointAzureEcr resource.
type ServiceEndpointAzureEcrArgs struct {
	Authorization pulumi.StringMapInput
	// The Azure container registry name.
	AzurecrName pulumi.StringInput
	// The tenant id of the service principal.
	AzurecrSpnTenantid pulumi.StringInput
	// The subscription id of the Azure targets.
	AzurecrSubscriptionId pulumi.StringInput
	// The subscription name of the Azure targets.
	AzurecrSubscriptionName pulumi.StringInput
	// The name you will use to refer to this service connection in task inputs.
	Description pulumi.StringPtrInput
	// The project ID or project name.
	ProjectId pulumi.StringInput
	// The resource group to which the container registry belongs.
	ResourceGroup pulumi.StringInput
	// The name you will use to refer to this service connection in task inputs.
	ServiceEndpointName pulumi.StringInput
}

func (ServiceEndpointAzureEcrArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceEndpointAzureEcrArgs)(nil)).Elem()
}

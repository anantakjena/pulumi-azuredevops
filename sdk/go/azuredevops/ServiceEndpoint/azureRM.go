// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ServiceEndpoint

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages Manual or Automatic AzureRM service endpoint within Azure DevOps.
//
// ## Requirements (Manual AzureRM Service Endpoint)
//
// Before to create a service end point in Azure DevOps, you need to create a Service Principal in your Azure subscription.
//
// For detailed steps to create a service principal with Azure cli see the [documentation](https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli?view=azure-cli-latest)
//
// ## Example Usage
// ### Manual AzureRM Service Endpoint
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azuredevops/sdk/go/azuredevops/Core"
// 	"github.com/pulumi/pulumi-azuredevops/sdk/go/azuredevops/ServiceEndpoint"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		project, err := Core.NewProject(ctx, "project", &Core.ProjectArgs{
// 			ProjectName:      pulumi.String("Sample Project"),
// 			Visibility:       pulumi.String("private"),
// 			VersionControl:   pulumi.String("Git"),
// 			WorkItemTemplate: pulumi.String("Agile"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = ServiceEndpoint.NewAzureRM(ctx, "endpointazure", &ServiceEndpoint.AzureRMArgs{
// 			ProjectId:           project.ID(),
// 			ServiceEndpointName: pulumi.String("TestServiceRM"),
// 			Credentials: &ServiceEndpoint.AzureRMCredentialsArgs{
// 				Serviceprincipalid:  pulumi.String("xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxx"),
// 				Serviceprincipalkey: pulumi.String("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"),
// 			},
// 			AzurermSpnTenantid:      pulumi.String("xxxxxxx-xxxx-xxx-xxxxx-xxxxxxxx"),
// 			AzurermSubscriptionId:   pulumi.String("xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxx"),
// 			AzurermSubscriptionName: pulumi.String("Sample Subscription"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### Automatic AzureRM Service Endpoint
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azuredevops/sdk/go/azuredevops/Core"
// 	"github.com/pulumi/pulumi-azuredevops/sdk/go/azuredevops/ServiceEndpoint"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		project, err := Core.NewProject(ctx, "project", &Core.ProjectArgs{
// 			ProjectName:      pulumi.String("Sample Project"),
// 			Visibility:       pulumi.String("private"),
// 			VersionControl:   pulumi.String("Git"),
// 			WorkItemTemplate: pulumi.String("Agile"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = ServiceEndpoint.NewAzureRM(ctx, "endpointazure", &ServiceEndpoint.AzureRMArgs{
// 			ProjectId:               project.ID(),
// 			ServiceEndpointName:     pulumi.String("TestServiceRM"),
// 			AzurermSpnTenantid:      pulumi.String("xxxxxxx-xxxx-xxx-xxxxx-xxxxxxxx"),
// 			AzurermSubscriptionId:   pulumi.String("xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxx"),
// 			AzurermSubscriptionName: pulumi.String("Microsoft Azure DEMO"),
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
// * [Azure DevOps Service REST API 5.1 - Service End points](https://docs.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-5.1)
type AzureRM struct {
	pulumi.CustomResourceState

	Authorization pulumi.StringMapOutput `pulumi:"authorization"`
	// The tenant id if the service principal.
	AzurermSpnTenantid pulumi.StringOutput `pulumi:"azurermSpnTenantid"`
	// The subscription Id of the Azure targets.
	AzurermSubscriptionId pulumi.StringOutput `pulumi:"azurermSubscriptionId"`
	// The subscription Name of the targets.
	AzurermSubscriptionName pulumi.StringOutput `pulumi:"azurermSubscriptionName"`
	// A `credentials` block.
	Credentials AzureRMCredentialsPtrOutput `pulumi:"credentials"`
	Description pulumi.StringPtrOutput      `pulumi:"description"`
	// The project ID or project name.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// The resource group used for scope of automatic service endpoint.
	ResourceGroup pulumi.StringPtrOutput `pulumi:"resourceGroup"`
	// The Service Endpoint name.
	ServiceEndpointName pulumi.StringOutput `pulumi:"serviceEndpointName"`
}

// NewAzureRM registers a new resource with the given unique name, arguments, and options.
func NewAzureRM(ctx *pulumi.Context,
	name string, args *AzureRMArgs, opts ...pulumi.ResourceOption) (*AzureRM, error) {
	if args == nil || args.AzurermSpnTenantid == nil {
		return nil, errors.New("missing required argument 'AzurermSpnTenantid'")
	}
	if args == nil || args.AzurermSubscriptionId == nil {
		return nil, errors.New("missing required argument 'AzurermSubscriptionId'")
	}
	if args == nil || args.AzurermSubscriptionName == nil {
		return nil, errors.New("missing required argument 'AzurermSubscriptionName'")
	}
	if args == nil || args.ProjectId == nil {
		return nil, errors.New("missing required argument 'ProjectId'")
	}
	if args == nil || args.ServiceEndpointName == nil {
		return nil, errors.New("missing required argument 'ServiceEndpointName'")
	}
	if args == nil {
		args = &AzureRMArgs{}
	}
	var resource AzureRM
	err := ctx.RegisterResource("azuredevops:ServiceEndpoint/azureRM:AzureRM", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAzureRM gets an existing AzureRM resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAzureRM(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AzureRMState, opts ...pulumi.ResourceOption) (*AzureRM, error) {
	var resource AzureRM
	err := ctx.ReadResource("azuredevops:ServiceEndpoint/azureRM:AzureRM", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AzureRM resources.
type azureRMState struct {
	Authorization map[string]string `pulumi:"authorization"`
	// The tenant id if the service principal.
	AzurermSpnTenantid *string `pulumi:"azurermSpnTenantid"`
	// The subscription Id of the Azure targets.
	AzurermSubscriptionId *string `pulumi:"azurermSubscriptionId"`
	// The subscription Name of the targets.
	AzurermSubscriptionName *string `pulumi:"azurermSubscriptionName"`
	// A `credentials` block.
	Credentials *AzureRMCredentials `pulumi:"credentials"`
	Description *string             `pulumi:"description"`
	// The project ID or project name.
	ProjectId *string `pulumi:"projectId"`
	// The resource group used for scope of automatic service endpoint.
	ResourceGroup *string `pulumi:"resourceGroup"`
	// The Service Endpoint name.
	ServiceEndpointName *string `pulumi:"serviceEndpointName"`
}

type AzureRMState struct {
	Authorization pulumi.StringMapInput
	// The tenant id if the service principal.
	AzurermSpnTenantid pulumi.StringPtrInput
	// The subscription Id of the Azure targets.
	AzurermSubscriptionId pulumi.StringPtrInput
	// The subscription Name of the targets.
	AzurermSubscriptionName pulumi.StringPtrInput
	// A `credentials` block.
	Credentials AzureRMCredentialsPtrInput
	Description pulumi.StringPtrInput
	// The project ID or project name.
	ProjectId pulumi.StringPtrInput
	// The resource group used for scope of automatic service endpoint.
	ResourceGroup pulumi.StringPtrInput
	// The Service Endpoint name.
	ServiceEndpointName pulumi.StringPtrInput
}

func (AzureRMState) ElementType() reflect.Type {
	return reflect.TypeOf((*azureRMState)(nil)).Elem()
}

type azureRMArgs struct {
	Authorization map[string]string `pulumi:"authorization"`
	// The tenant id if the service principal.
	AzurermSpnTenantid string `pulumi:"azurermSpnTenantid"`
	// The subscription Id of the Azure targets.
	AzurermSubscriptionId string `pulumi:"azurermSubscriptionId"`
	// The subscription Name of the targets.
	AzurermSubscriptionName string `pulumi:"azurermSubscriptionName"`
	// A `credentials` block.
	Credentials *AzureRMCredentials `pulumi:"credentials"`
	Description *string             `pulumi:"description"`
	// The project ID or project name.
	ProjectId string `pulumi:"projectId"`
	// The resource group used for scope of automatic service endpoint.
	ResourceGroup *string `pulumi:"resourceGroup"`
	// The Service Endpoint name.
	ServiceEndpointName string `pulumi:"serviceEndpointName"`
}

// The set of arguments for constructing a AzureRM resource.
type AzureRMArgs struct {
	Authorization pulumi.StringMapInput
	// The tenant id if the service principal.
	AzurermSpnTenantid pulumi.StringInput
	// The subscription Id of the Azure targets.
	AzurermSubscriptionId pulumi.StringInput
	// The subscription Name of the targets.
	AzurermSubscriptionName pulumi.StringInput
	// A `credentials` block.
	Credentials AzureRMCredentialsPtrInput
	Description pulumi.StringPtrInput
	// The project ID or project name.
	ProjectId pulumi.StringInput
	// The resource group used for scope of automatic service endpoint.
	ResourceGroup pulumi.StringPtrInput
	// The Service Endpoint name.
	ServiceEndpointName pulumi.StringInput
}

func (AzureRMArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*azureRMArgs)(nil)).Elem()
}

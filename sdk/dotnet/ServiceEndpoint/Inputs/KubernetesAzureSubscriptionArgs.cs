// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureDevOps.ServiceEndpoint.Inputs
{

    public sealed class KubernetesAzureSubscriptionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Azure environment refers to whether the public cloud offering or domestic (government) clouds are being used. Currently, only the public cloud is supported. The value must be AzureCloud. This is also the default-value.
        /// </summary>
        [Input("azureEnvironment")]
        public Input<string>? AzureEnvironment { get; set; }

        /// <summary>
        /// The name of the Kubernetes cluster.
        /// </summary>
        [Input("clusterName", required: true)]
        public Input<string> ClusterName { get; set; } = null!;

        /// <summary>
        /// The Kubernetes namespace. Default value is "default".
        /// </summary>
        [Input("namespace")]
        public Input<string>? Namespace { get; set; }

        /// <summary>
        /// The resource group id, to which the Kubernetes cluster is deployed.
        /// </summary>
        [Input("resourcegroupId", required: true)]
        public Input<string> ResourcegroupId { get; set; } = null!;

        /// <summary>
        /// The id of the Azure subscription.
        /// </summary>
        [Input("subscriptionId", required: true)]
        public Input<string> SubscriptionId { get; set; } = null!;

        /// <summary>
        /// The name of the Azure subscription.
        /// </summary>
        [Input("subscriptionName", required: true)]
        public Input<string> SubscriptionName { get; set; } = null!;

        /// <summary>
        /// The id of the tenant used by the subscription.
        /// </summary>
        [Input("tenantId", required: true)]
        public Input<string> TenantId { get; set; } = null!;

        public KubernetesAzureSubscriptionArgs()
        {
        }
    }
}
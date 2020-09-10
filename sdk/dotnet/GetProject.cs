// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureDevOps
{
    public static class GetProject
    {
        /// <summary>
        /// Use this data source to access information about an existing Project within Azure DevOps.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using AzureDevOps = Pulumi.AzureDevOps;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var project = Output.Create(AzureDevOps.GetProject.InvokeAsync(new AzureDevOps.GetProjectArgs
        ///         {
        ///             ProjectIdentifier = "Sample Project",
        ///         }));
        ///         this.Id = project.Apply(project =&gt; project.Id);
        ///         this.Name = project.Apply(project =&gt; project.Name);
        ///         this.Visibility = project.Apply(project =&gt; project.Visibility);
        ///         this.VersionControl = project.Apply(project =&gt; project.VersionControl);
        ///         this.WorkItemTemplate = project.Apply(project =&gt; project.WorkItemTemplate);
        ///         this.ProcessTemplateId = project.Apply(project =&gt; project.ProcessTemplateId);
        ///     }
        /// 
        ///     [Output("id")]
        ///     public Output&lt;string&gt; Id { get; set; }
        ///     [Output("name")]
        ///     public Output&lt;string&gt; Name { get; set; }
        ///     [Output("visibility")]
        ///     public Output&lt;string&gt; Visibility { get; set; }
        ///     [Output("versionControl")]
        ///     public Output&lt;string&gt; VersionControl { get; set; }
        ///     [Output("workItemTemplate")]
        ///     public Output&lt;string&gt; WorkItemTemplate { get; set; }
        ///     [Output("processTemplateId")]
        ///     public Output&lt;string&gt; ProcessTemplateId { get; set; }
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// ## Relevant Links
        /// 
        /// - [Azure DevOps Service REST API 5.1 - Projects - Get](https://docs.microsoft.com/en-us/rest/api/azure/devops/core/projects/get?view=azure-devops-rest-5.1)
        /// </summary>
        public static Task<GetProjectResult> InvokeAsync(GetProjectArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetProjectResult>("azuredevops:index/getProject:getProject", args ?? new GetProjectArgs(), options.WithVersion());
    }


    public sealed class GetProjectArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name or ID of the Project.
        /// </summary>
        [Input("projectIdentifier", required: true)]
        public string ProjectIdentifier { get; set; } = null!;

        public GetProjectArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetProjectResult
    {
        public readonly string Description;
        public readonly ImmutableDictionary<string, object> Features;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;
        public readonly string ProcessTemplateId;
        public readonly string ProjectIdentifier;
        public readonly string VersionControl;
        public readonly string Visibility;
        public readonly string WorkItemTemplate;

        [OutputConstructor]
        private GetProjectResult(
            string description,

            ImmutableDictionary<string, object> features,

            string id,

            string name,

            string processTemplateId,

            string projectIdentifier,

            string versionControl,

            string visibility,

            string workItemTemplate)
        {
            Description = description;
            Features = features;
            Id = id;
            Name = name;
            ProcessTemplateId = processTemplateId;
            ProjectIdentifier = projectIdentifier;
            VersionControl = versionControl;
            Visibility = visibility;
            WorkItemTemplate = workItemTemplate;
        }
    }
}
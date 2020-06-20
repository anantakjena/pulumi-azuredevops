// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureDevOps.Repository
{
    public static class GetRepositories
    {
        /// <summary>
        /// Use this data source to access information about an existing Git Repositories within Azure DevOps.
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
        ///         var project = Output.Create(AzureDevOps.Core.GetProject.InvokeAsync(new AzureDevOps.Core.GetProjectArgs
        ///         {
        ///             ProjectName = "contoso-project",
        ///         }));
        ///         var allRepos = project.Apply(project =&gt; Output.Create(AzureDevOps.Repository.GetRepositories.InvokeAsync(new AzureDevOps.Repository.GetRepositoriesArgs
        ///         {
        ///             ProjectId = project.Id,
        ///             IncludeHidden = true,
        ///         })));
        ///         var singleRepo = project.Apply(project =&gt; Output.Create(AzureDevOps.Repository.GetRepositories.InvokeAsync(new AzureDevOps.Repository.GetRepositoriesArgs
        ///         {
        ///             ProjectId = project.Id,
        ///             Name = "contoso-repo",
        ///         })));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// ## Relevant Links
        /// 
        /// - [Azure DevOps Service REST API 5.1 - Git API](https://docs.microsoft.com/en-us/rest/api/azure/devops/git/?view=azure-devops-rest-5.1)
        /// </summary>
        public static Task<GetRepositoriesResult> InvokeAsync(GetRepositoriesArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetRepositoriesResult>("azuredevops:Repository/getRepositories:getRepositories", args ?? new GetRepositoriesArgs(), options.WithVersion());
    }


    public sealed class GetRepositoriesArgs : Pulumi.InvokeArgs
    {
        [Input("includeHidden")]
        public bool? IncludeHidden { get; set; }

        [Input("name")]
        public string? Name { get; set; }

        [Input("projectId")]
        public string? ProjectId { get; set; }

        public GetRepositoriesArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetRepositoriesResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly bool? IncludeHidden;
        public readonly string? Name;
        public readonly string? ProjectId;
        public readonly ImmutableArray<Outputs.GetRepositoriesRepositoryResult> Repositories;

        [OutputConstructor]
        private GetRepositoriesResult(
            string id,

            bool? includeHidden,

            string? name,

            string? projectId,

            ImmutableArray<Outputs.GetRepositoriesRepositoryResult> repositories)
        {
            Id = id;
            IncludeHidden = includeHidden;
            Name = name;
            ProjectId = projectId;
            Repositories = repositories;
        }
    }
}
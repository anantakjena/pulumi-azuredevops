// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureDevOps.Pipeline
{
    /// <summary>
    /// Manages variable groups within Azure DevOps.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using AzureDevOps = Pulumi.AzureDevOps;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var project = new AzureDevOps.Core.Project("project", new AzureDevOps.Core.ProjectArgs
    ///         {
    ///             ProjectName = "Test Project",
    ///         });
    ///         var variablegroup = new AzureDevOps.Pipeline.VariableGroup("variablegroup", new AzureDevOps.Pipeline.VariableGroupArgs
    ///         {
    ///             ProjectId = project.Id,
    ///             Description = "Test Variable Group Description",
    ///             AllowAccess = true,
    ///             Variables = 
    ///             {
    ///                 new AzureDevOps.Pipeline.Inputs.VariableGroupVariableArgs
    ///                 {
    ///                     Name = "key",
    ///                     Value = "value",
    ///                 },
    ///                 new AzureDevOps.Pipeline.Inputs.VariableGroupVariableArgs
    ///                 {
    ///                     Name = "Account Password",
    ///                     Value = "p@ssword123",
    ///                     IsSecret = true,
    ///                 },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ## Relevant Links
    /// 
    /// * [Azure DevOps Service REST API 5.1 - Variable Groups](https://docs.microsoft.com/en-us/rest/api/azure/devops/distributedtask/variablegroups?view=azure-devops-rest-5.1)
    /// * [Azure DevOps Service REST API 5.1 - Authorized Resources](https://docs.microsoft.com/en-us/rest/api/azure/devops/build/authorizedresources?view=azure-devops-rest-5.1)
    /// 
    /// ## PAT Permissions Required
    /// 
    /// - **Variable Groups**: Read, Create, &amp; Manage
    /// </summary>
    public partial class VariableGroup : Pulumi.CustomResource
    {
        /// <summary>
        /// Boolean that indicate if this variable group is shared by all pipelines of this project.
        /// </summary>
        [Output("allowAccess")]
        public Output<bool?> AllowAccess { get; private set; } = null!;

        /// <summary>
        /// The description of the Variable Group.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("keyVault")]
        public Output<Outputs.VariableGroupKeyVault?> KeyVault { get; private set; } = null!;

        /// <summary>
        /// The name of the Variable Group.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The project ID or project name.
        /// </summary>
        [Output("projectId")]
        public Output<string> ProjectId { get; private set; } = null!;

        /// <summary>
        /// One or more `variable` blocks as documented below.
        /// </summary>
        [Output("variables")]
        public Output<ImmutableArray<Outputs.VariableGroupVariable>> Variables { get; private set; } = null!;


        /// <summary>
        /// Create a VariableGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VariableGroup(string name, VariableGroupArgs args, CustomResourceOptions? options = null)
            : base("azuredevops:Pipeline/variableGroup:VariableGroup", name, args ?? new VariableGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private VariableGroup(string name, Input<string> id, VariableGroupState? state = null, CustomResourceOptions? options = null)
            : base("azuredevops:Pipeline/variableGroup:VariableGroup", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing VariableGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VariableGroup Get(string name, Input<string> id, VariableGroupState? state = null, CustomResourceOptions? options = null)
        {
            return new VariableGroup(name, id, state, options);
        }
    }

    public sealed class VariableGroupArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Boolean that indicate if this variable group is shared by all pipelines of this project.
        /// </summary>
        [Input("allowAccess")]
        public Input<bool>? AllowAccess { get; set; }

        /// <summary>
        /// The description of the Variable Group.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("keyVault")]
        public Input<Inputs.VariableGroupKeyVaultArgs>? KeyVault { get; set; }

        /// <summary>
        /// The name of the Variable Group.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The project ID or project name.
        /// </summary>
        [Input("projectId", required: true)]
        public Input<string> ProjectId { get; set; } = null!;

        [Input("variables", required: true)]
        private InputList<Inputs.VariableGroupVariableArgs>? _variables;

        /// <summary>
        /// One or more `variable` blocks as documented below.
        /// </summary>
        public InputList<Inputs.VariableGroupVariableArgs> Variables
        {
            get => _variables ?? (_variables = new InputList<Inputs.VariableGroupVariableArgs>());
            set => _variables = value;
        }

        public VariableGroupArgs()
        {
        }
    }

    public sealed class VariableGroupState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Boolean that indicate if this variable group is shared by all pipelines of this project.
        /// </summary>
        [Input("allowAccess")]
        public Input<bool>? AllowAccess { get; set; }

        /// <summary>
        /// The description of the Variable Group.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("keyVault")]
        public Input<Inputs.VariableGroupKeyVaultGetArgs>? KeyVault { get; set; }

        /// <summary>
        /// The name of the Variable Group.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The project ID or project name.
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        [Input("variables")]
        private InputList<Inputs.VariableGroupVariableGetArgs>? _variables;

        /// <summary>
        /// One or more `variable` blocks as documented below.
        /// </summary>
        public InputList<Inputs.VariableGroupVariableGetArgs> Variables
        {
            get => _variables ?? (_variables = new InputList<Inputs.VariableGroupVariableGetArgs>());
            set => _variables = value;
        }

        public VariableGroupState()
        {
        }
    }
}

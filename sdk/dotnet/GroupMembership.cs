// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureDevOps
{
    /// <summary>
    /// Manages group membership within Azure DevOps.
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
    ///         var project = new AzureDevOps.Project("project", new AzureDevOps.ProjectArgs
    ///         {
    ///         });
    ///         var user = new AzureDevOps.User("user", new AzureDevOps.UserArgs
    ///         {
    ///             PrincipalName = "foo@contoso.com",
    ///         });
    ///         var @group = project.Id.Apply(id =&gt; AzureDevOps.GetGroup.InvokeAsync(new AzureDevOps.GetGroupArgs
    ///         {
    ///             ProjectId = id,
    ///             Name = "Build Administrators",
    ///         }));
    ///         var membership = new AzureDevOps.GroupMembership("membership", new AzureDevOps.GroupMembershipArgs
    ///         {
    ///             Group = @group.Apply(@group =&gt; @group.Descriptor),
    ///             Members = 
    ///             {
    ///                 user.Descriptor,
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ## Relevant Links
    /// 
    /// - [Azure DevOps Service REST API 5.1 - Memberships](https://docs.microsoft.com/en-us/rest/api/azure/devops/graph/memberships?view=azure-devops-rest-5.0)
    /// 
    /// ## PAT Permissions Required
    /// 
    /// - **Deployment Groups**: Read &amp; Manage
    /// </summary>
    public partial class GroupMembership : Pulumi.CustomResource
    {
        /// <summary>
        /// The descriptor of the group being managed.
        /// </summary>
        [Output("group")]
        public Output<string> Group { get; private set; } = null!;

        /// <summary>
        /// A list of user or group descriptors that will become members of the group.
        /// &gt; NOTE: It's possible to define group members both within the `azuredevops.GroupMembership resource` via the members block and by using the `azuredevops.Group` resource. However it's not possible to use both methods to manage group members, since there'll be conflicts.
        /// </summary>
        [Output("members")]
        public Output<ImmutableArray<string>> Members { get; private set; } = null!;

        /// <summary>
        /// The mode how the resource manages group members.
        /// - `mode == add`: the resource will ensure that all specified members will be part of the referenced group
        /// - `mode == overwrite`: the resource will replace all existing members with the members specified within the `members` block
        /// &gt; NOTE: To clear all members from a group, specify an empty list of descriptors in the `members` attribute and set the `mode` member to `overwrite`.
        /// </summary>
        [Output("mode")]
        public Output<string?> Mode { get; private set; } = null!;


        /// <summary>
        /// Create a GroupMembership resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public GroupMembership(string name, GroupMembershipArgs args, CustomResourceOptions? options = null)
            : base("azuredevops:index/groupMembership:GroupMembership", name, args ?? new GroupMembershipArgs(), MakeResourceOptions(options, ""))
        {
        }

        private GroupMembership(string name, Input<string> id, GroupMembershipState? state = null, CustomResourceOptions? options = null)
            : base("azuredevops:index/groupMembership:GroupMembership", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                Aliases =
                {
                    new Pulumi.Alias { Type = "azuredevops:Identities/groupMembership:GroupMembership"},
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing GroupMembership resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static GroupMembership Get(string name, Input<string> id, GroupMembershipState? state = null, CustomResourceOptions? options = null)
        {
            return new GroupMembership(name, id, state, options);
        }
    }

    public sealed class GroupMembershipArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The descriptor of the group being managed.
        /// </summary>
        [Input("group", required: true)]
        public Input<string> Group { get; set; } = null!;

        [Input("members", required: true)]
        private InputList<string>? _members;

        /// <summary>
        /// A list of user or group descriptors that will become members of the group.
        /// &gt; NOTE: It's possible to define group members both within the `azuredevops.GroupMembership resource` via the members block and by using the `azuredevops.Group` resource. However it's not possible to use both methods to manage group members, since there'll be conflicts.
        /// </summary>
        public InputList<string> Members
        {
            get => _members ?? (_members = new InputList<string>());
            set => _members = value;
        }

        /// <summary>
        /// The mode how the resource manages group members.
        /// - `mode == add`: the resource will ensure that all specified members will be part of the referenced group
        /// - `mode == overwrite`: the resource will replace all existing members with the members specified within the `members` block
        /// &gt; NOTE: To clear all members from a group, specify an empty list of descriptors in the `members` attribute and set the `mode` member to `overwrite`.
        /// </summary>
        [Input("mode")]
        public Input<string>? Mode { get; set; }

        public GroupMembershipArgs()
        {
        }
    }

    public sealed class GroupMembershipState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The descriptor of the group being managed.
        /// </summary>
        [Input("group")]
        public Input<string>? Group { get; set; }

        [Input("members")]
        private InputList<string>? _members;

        /// <summary>
        /// A list of user or group descriptors that will become members of the group.
        /// &gt; NOTE: It's possible to define group members both within the `azuredevops.GroupMembership resource` via the members block and by using the `azuredevops.Group` resource. However it's not possible to use both methods to manage group members, since there'll be conflicts.
        /// </summary>
        public InputList<string> Members
        {
            get => _members ?? (_members = new InputList<string>());
            set => _members = value;
        }

        /// <summary>
        /// The mode how the resource manages group members.
        /// - `mode == add`: the resource will ensure that all specified members will be part of the referenced group
        /// - `mode == overwrite`: the resource will replace all existing members with the members specified within the `members` block
        /// &gt; NOTE: To clear all members from a group, specify an empty list of descriptors in the `members` attribute and set the `mode` member to `overwrite`.
        /// </summary>
        [Input("mode")]
        public Input<string>? Mode { get; set; }

        public GroupMembershipState()
        {
        }
    }
}

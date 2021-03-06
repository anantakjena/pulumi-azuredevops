// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureDevOps.Policy.Inputs
{

    public sealed class BranchPolicyMinReviewersSettingsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The number of reviewrs needed to approve.
        /// </summary>
        [Input("reviewerCount", required: true)]
        public Input<int> ReviewerCount { get; set; } = null!;

        [Input("scopes", required: true)]
        private InputList<Inputs.BranchPolicyMinReviewersSettingsScopeArgs>? _scopes;

        /// <summary>
        /// Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.
        /// </summary>
        public InputList<Inputs.BranchPolicyMinReviewersSettingsScopeArgs> Scopes
        {
            get => _scopes ?? (_scopes = new InputList<Inputs.BranchPolicyMinReviewersSettingsScopeArgs>());
            set => _scopes = value;
        }

        /// <summary>
        /// Controls whether or not the submitter's vote counts. Defaults to `false`.
        /// </summary>
        [Input("submitterCanVote")]
        public Input<bool>? SubmitterCanVote { get; set; }

        public BranchPolicyMinReviewersSettingsArgs()
        {
        }
    }
}

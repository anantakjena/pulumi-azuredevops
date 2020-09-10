// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureDevOps.Inputs
{

    public sealed class BranchPolicyAutoReviewersSettingsArgs : Pulumi.ResourceArgs
    {
        [Input("autoReviewerIds", required: true)]
        private InputList<string>? _autoReviewerIds;

        /// <summary>
        /// Required reviewers ids. Supports multiples user Ids.
        /// </summary>
        public InputList<string> AutoReviewerIds
        {
            get => _autoReviewerIds ?? (_autoReviewerIds = new InputList<string>());
            set => _autoReviewerIds = value;
        }

        /// <summary>
        /// Activity feed message, Message will appear in the activity feed of pull requests with automatically added reviewers.
        /// </summary>
        [Input("message")]
        public Input<string>? Message { get; set; }

        [Input("pathFilters")]
        private InputList<string>? _pathFilters;

        /// <summary>
        /// Filter path(s) on which the policy is applied. Supports absolute paths, wildcards and multiple paths. Example: /WebApp/Models/Data.cs, /WebApp/* or *.cs,/WebApp/Models/Data.cs;ClientApp/Models/Data.cs.
        /// </summary>
        public InputList<string> PathFilters
        {
            get => _pathFilters ?? (_pathFilters = new InputList<string>());
            set => _pathFilters = value;
        }

        [Input("scopes", required: true)]
        private InputList<Inputs.BranchPolicyAutoReviewersSettingsScopeArgs>? _scopes;

        /// <summary>
        /// Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.
        /// </summary>
        public InputList<Inputs.BranchPolicyAutoReviewersSettingsScopeArgs> Scopes
        {
            get => _scopes ?? (_scopes = new InputList<Inputs.BranchPolicyAutoReviewersSettingsScopeArgs>());
            set => _scopes = value;
        }

        /// <summary>
        /// Controls whether or not the submitter's vote counts. Defaults to `false`.
        /// </summary>
        [Input("submitterCanVote")]
        public Input<bool>? SubmitterCanVote { get; set; }

        public BranchPolicyAutoReviewersSettingsArgs()
        {
        }
    }
}
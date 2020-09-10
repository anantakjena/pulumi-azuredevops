// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureDevOps.Outputs
{

    [OutputType]
    public sealed class BranchPolicyAutoReviewersSettings
    {
        /// <summary>
        /// Required reviewers ids. Supports multiples user Ids.
        /// </summary>
        public readonly ImmutableArray<string> AutoReviewerIds;
        /// <summary>
        /// Activity feed message, Message will appear in the activity feed of pull requests with automatically added reviewers.
        /// </summary>
        public readonly string? Message;
        /// <summary>
        /// Filter path(s) on which the policy is applied. Supports absolute paths, wildcards and multiple paths. Example: /WebApp/Models/Data.cs, /WebApp/* or *.cs,/WebApp/Models/Data.cs;ClientApp/Models/Data.cs.
        /// </summary>
        public readonly ImmutableArray<string> PathFilters;
        /// <summary>
        /// Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.
        /// </summary>
        public readonly ImmutableArray<Outputs.BranchPolicyAutoReviewersSettingsScope> Scopes;
        /// <summary>
        /// Controls whether or not the submitter's vote counts. Defaults to `false`.
        /// </summary>
        public readonly bool? SubmitterCanVote;

        [OutputConstructor]
        private BranchPolicyAutoReviewersSettings(
            ImmutableArray<string> autoReviewerIds,

            string? message,

            ImmutableArray<string> pathFilters,

            ImmutableArray<Outputs.BranchPolicyAutoReviewersSettingsScope> scopes,

            bool? submitterCanVote)
        {
            AutoReviewerIds = autoReviewerIds;
            Message = message;
            PathFilters = pathFilters;
            Scopes = scopes;
            SubmitterCanVote = submitterCanVote;
        }
    }
}
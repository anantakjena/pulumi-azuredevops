// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureDevOps.Build.Inputs
{

    public sealed class BuildDefinitionVariableArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// True if the variable can be overridden. Defaults to `true`.
        /// </summary>
        [Input("allowOverride")]
        public Input<bool>? AllowOverride { get; set; }

        /// <summary>
        /// True if the variable is a secret. Defaults to `false`.
        /// </summary>
        [Input("isSecret")]
        public Input<bool>? IsSecret { get; set; }

        /// <summary>
        /// The name of the variable.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The secret value of the variable. Used when `is_secret` set to `true`.
        /// </summary>
        [Input("secretValue")]
        public Input<string>? SecretValue { get; set; }

        /// <summary>
        /// The value of the variable.
        /// </summary>
        [Input("value")]
        public Input<string>? Value { get; set; }

        public BuildDefinitionVariableArgs()
        {
        }
    }
}
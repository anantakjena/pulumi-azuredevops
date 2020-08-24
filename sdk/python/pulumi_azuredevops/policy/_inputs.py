# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'BranchPolicyBuildValidationSettingsArgs',
    'BranchPolicyBuildValidationSettingsScopeArgs',
    'BranchPolicyMinReviewersSettingsArgs',
    'BranchPolicyMinReviewersSettingsScopeArgs',
]

@pulumi.input_type
class BranchPolicyBuildValidationSettingsArgs:
    def __init__(__self__, *,
                 build_definition_id: pulumi.Input[float],
                 display_name: pulumi.Input[str],
                 scopes: pulumi.Input[List[pulumi.Input['BranchPolicyBuildValidationSettingsScopeArgs']]],
                 manual_queue_only: Optional[pulumi.Input[bool]] = None,
                 queue_on_source_update_only: Optional[pulumi.Input[bool]] = None,
                 valid_duration: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[float] build_definition_id: The ID of the build to monitor for the policy.
        :param pulumi.Input[str] display_name: The display name for the policy.
        :param pulumi.Input[List[pulumi.Input['BranchPolicyBuildValidationSettingsScopeArgs']]] scopes: Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.
        :param pulumi.Input[bool] manual_queue_only: If set to true, the build will need to be manually queued. Defaults to `false`
        :param pulumi.Input[bool] queue_on_source_update_only: True if the build should queue on source updates only. Defaults to `true`.
        :param pulumi.Input[float] valid_duration: The number of minutes for which the build is valid. If `0`, the build will not expire. Defaults to `720` (12 hours).
        """
        pulumi.set(__self__, "build_definition_id", build_definition_id)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "scopes", scopes)
        if manual_queue_only is not None:
            pulumi.set(__self__, "manual_queue_only", manual_queue_only)
        if queue_on_source_update_only is not None:
            pulumi.set(__self__, "queue_on_source_update_only", queue_on_source_update_only)
        if valid_duration is not None:
            pulumi.set(__self__, "valid_duration", valid_duration)

    @property
    @pulumi.getter(name="buildDefinitionId")
    def build_definition_id(self) -> pulumi.Input[float]:
        """
        The ID of the build to monitor for the policy.
        """
        return pulumi.get(self, "build_definition_id")

    @build_definition_id.setter
    def build_definition_id(self, value: pulumi.Input[float]):
        pulumi.set(self, "build_definition_id", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The display name for the policy.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Input[List[pulumi.Input['BranchPolicyBuildValidationSettingsScopeArgs']]]:
        """
        Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: pulumi.Input[List[pulumi.Input['BranchPolicyBuildValidationSettingsScopeArgs']]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter(name="manualQueueOnly")
    def manual_queue_only(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to true, the build will need to be manually queued. Defaults to `false`
        """
        return pulumi.get(self, "manual_queue_only")

    @manual_queue_only.setter
    def manual_queue_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "manual_queue_only", value)

    @property
    @pulumi.getter(name="queueOnSourceUpdateOnly")
    def queue_on_source_update_only(self) -> Optional[pulumi.Input[bool]]:
        """
        True if the build should queue on source updates only. Defaults to `true`.
        """
        return pulumi.get(self, "queue_on_source_update_only")

    @queue_on_source_update_only.setter
    def queue_on_source_update_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "queue_on_source_update_only", value)

    @property
    @pulumi.getter(name="validDuration")
    def valid_duration(self) -> Optional[pulumi.Input[float]]:
        """
        The number of minutes for which the build is valid. If `0`, the build will not expire. Defaults to `720` (12 hours).
        """
        return pulumi.get(self, "valid_duration")

    @valid_duration.setter
    def valid_duration(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "valid_duration", value)


@pulumi.input_type
class BranchPolicyBuildValidationSettingsScopeArgs:
    def __init__(__self__, *,
                 match_type: Optional[pulumi.Input[str]] = None,
                 repository_id: Optional[pulumi.Input[str]] = None,
                 repository_ref: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] match_type: The match type to use when applying the policy. Supported values are `Exact` (default) or `Prefix`.
        :param pulumi.Input[str] repository_id: The repository ID. Needed only if the scope of the policy will be limited to a single repository.
        :param pulumi.Input[str] repository_ref: The ref pattern to use for the match. If `match_type` is `Exact`, this should be a qualified ref such as `refs/heads/master`. If `match_type` is `Prefix`, this should be a ref path such as `refs/heads/releases`.
        """
        if match_type is not None:
            pulumi.set(__self__, "match_type", match_type)
        if repository_id is not None:
            pulumi.set(__self__, "repository_id", repository_id)
        if repository_ref is not None:
            pulumi.set(__self__, "repository_ref", repository_ref)

    @property
    @pulumi.getter(name="matchType")
    def match_type(self) -> Optional[pulumi.Input[str]]:
        """
        The match type to use when applying the policy. Supported values are `Exact` (default) or `Prefix`.
        """
        return pulumi.get(self, "match_type")

    @match_type.setter
    def match_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "match_type", value)

    @property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> Optional[pulumi.Input[str]]:
        """
        The repository ID. Needed only if the scope of the policy will be limited to a single repository.
        """
        return pulumi.get(self, "repository_id")

    @repository_id.setter
    def repository_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repository_id", value)

    @property
    @pulumi.getter(name="repositoryRef")
    def repository_ref(self) -> Optional[pulumi.Input[str]]:
        """
        The ref pattern to use for the match. If `match_type` is `Exact`, this should be a qualified ref such as `refs/heads/master`. If `match_type` is `Prefix`, this should be a ref path such as `refs/heads/releases`.
        """
        return pulumi.get(self, "repository_ref")

    @repository_ref.setter
    def repository_ref(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repository_ref", value)


@pulumi.input_type
class BranchPolicyMinReviewersSettingsArgs:
    def __init__(__self__, *,
                 reviewer_count: pulumi.Input[float],
                 scopes: pulumi.Input[List[pulumi.Input['BranchPolicyMinReviewersSettingsScopeArgs']]],
                 submitter_can_vote: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[float] reviewer_count: The number of reviewrs needed to approve.
        :param pulumi.Input[List[pulumi.Input['BranchPolicyMinReviewersSettingsScopeArgs']]] scopes: Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.
        :param pulumi.Input[bool] submitter_can_vote: Controls whether or not the submitter's vote counts. Defaults to `false`.
        """
        pulumi.set(__self__, "reviewer_count", reviewer_count)
        pulumi.set(__self__, "scopes", scopes)
        if submitter_can_vote is not None:
            pulumi.set(__self__, "submitter_can_vote", submitter_can_vote)

    @property
    @pulumi.getter(name="reviewerCount")
    def reviewer_count(self) -> pulumi.Input[float]:
        """
        The number of reviewrs needed to approve.
        """
        return pulumi.get(self, "reviewer_count")

    @reviewer_count.setter
    def reviewer_count(self, value: pulumi.Input[float]):
        pulumi.set(self, "reviewer_count", value)

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Input[List[pulumi.Input['BranchPolicyMinReviewersSettingsScopeArgs']]]:
        """
        Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: pulumi.Input[List[pulumi.Input['BranchPolicyMinReviewersSettingsScopeArgs']]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter(name="submitterCanVote")
    def submitter_can_vote(self) -> Optional[pulumi.Input[bool]]:
        """
        Controls whether or not the submitter's vote counts. Defaults to `false`.
        """
        return pulumi.get(self, "submitter_can_vote")

    @submitter_can_vote.setter
    def submitter_can_vote(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "submitter_can_vote", value)


@pulumi.input_type
class BranchPolicyMinReviewersSettingsScopeArgs:
    def __init__(__self__, *,
                 match_type: Optional[pulumi.Input[str]] = None,
                 repository_id: Optional[pulumi.Input[str]] = None,
                 repository_ref: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] match_type: The match type to use when applying the policy. Supported values are `Exact` (default) or `Prefix`.
        :param pulumi.Input[str] repository_id: The repository ID. Needed only if the scope of the policy will be limited to a single repository.
        :param pulumi.Input[str] repository_ref: The ref pattern to use for the match. If `match_type` is `Exact`, this should be a qualified ref such as `refs/heads/master`. If `match_type` is `Prefix`, this should be a ref path such as `refs/heads/releases`.
        """
        if match_type is not None:
            pulumi.set(__self__, "match_type", match_type)
        if repository_id is not None:
            pulumi.set(__self__, "repository_id", repository_id)
        if repository_ref is not None:
            pulumi.set(__self__, "repository_ref", repository_ref)

    @property
    @pulumi.getter(name="matchType")
    def match_type(self) -> Optional[pulumi.Input[str]]:
        """
        The match type to use when applying the policy. Supported values are `Exact` (default) or `Prefix`.
        """
        return pulumi.get(self, "match_type")

    @match_type.setter
    def match_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "match_type", value)

    @property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> Optional[pulumi.Input[str]]:
        """
        The repository ID. Needed only if the scope of the policy will be limited to a single repository.
        """
        return pulumi.get(self, "repository_id")

    @repository_id.setter
    def repository_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repository_id", value)

    @property
    @pulumi.getter(name="repositoryRef")
    def repository_ref(self) -> Optional[pulumi.Input[str]]:
        """
        The ref pattern to use for the match. If `match_type` is `Exact`, this should be a qualified ref such as `refs/heads/master`. If `match_type` is `Prefix`, this should be a ref path such as `refs/heads/releases`.
        """
        return pulumi.get(self, "repository_ref")

    @repository_ref.setter
    def repository_ref(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repository_ref", value)



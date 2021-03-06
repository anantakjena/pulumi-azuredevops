# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['GitHub']

warnings.warn("azuredevops.serviceendpoint.GitHub has been deprecated in favor of azuredevops.ServiceEndpointGitHub", DeprecationWarning)


class GitHub(pulumi.CustomResource):
    warnings.warn("azuredevops.serviceendpoint.GitHub has been deprecated in favor of azuredevops.ServiceEndpointGitHub", DeprecationWarning)

    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_oauth: Optional[pulumi.Input[pulumi.InputType['GitHubAuthOauthArgs']]] = None,
                 auth_personal: Optional[pulumi.Input[pulumi.InputType['GitHubAuthPersonalArgs']]] = None,
                 authorization: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 service_endpoint_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a GitHub service endpoint within Azure DevOps.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        project = azuredevops.Project("project",
            visibility="private",
            version_control="Git",
            work_item_template="Agile")
        serviceendpoint_gh1 = azuredevops.ServiceEndpointGitHub("serviceendpointGh1",
            project_id=project.id,
            service_endpoint_name="Sample GithHub Personal Access Token",
            auth_personal=azuredevops.ServiceEndpointGitHubAuthPersonalArgs(
                personal_access_token="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            ))
        ```

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        serviceendpoint_gh2 = azuredevops.ServiceEndpointGitHub("serviceendpointGh2",
            project_id=azuredevops_project["project"]["id"],
            service_endpoint_name="Sample GithHub Grant",
            auth_oauth=azuredevops.ServiceEndpointGitHubAuthOauthArgs(
                oauth_configuration_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            ))
        ```

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        serviceendpoint_gh3 = azuredevops.ServiceEndpointGitHub("serviceendpointGh3",
            project_id=azuredevops_project["project"]["id"],
            service_endpoint_name="Sample GithHub Apps: Azure Pipelines",
            description="")
        ```
        ## Relevant Links

        - [Azure DevOps Service REST API 5.1 - Agent Pools](https://docs.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-5.1)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GitHubAuthOauthArgs']] auth_oauth: An `auth_oauth` block as documented below. Allows connecting using an Oauth token.
        :param pulumi.Input[pulumi.InputType['GitHubAuthPersonalArgs']] auth_personal: An `auth_personal` block as documented below. Allows connecting using a personal access token.
        :param pulumi.Input[str] project_id: The project ID or project name.
        :param pulumi.Input[str] service_endpoint_name: The Service Endpoint name.
        """
        pulumi.log.warn("GitHub is deprecated: azuredevops.serviceendpoint.GitHub has been deprecated in favor of azuredevops.ServiceEndpointGitHub")
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['auth_oauth'] = auth_oauth
            __props__['auth_personal'] = auth_personal
            __props__['authorization'] = authorization
            __props__['description'] = description
            if project_id is None:
                raise TypeError("Missing required property 'project_id'")
            __props__['project_id'] = project_id
            if service_endpoint_name is None:
                raise TypeError("Missing required property 'service_endpoint_name'")
            __props__['service_endpoint_name'] = service_endpoint_name
        super(GitHub, __self__).__init__(
            'azuredevops:ServiceEndpoint/gitHub:GitHub',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auth_oauth: Optional[pulumi.Input[pulumi.InputType['GitHubAuthOauthArgs']]] = None,
            auth_personal: Optional[pulumi.Input[pulumi.InputType['GitHubAuthPersonalArgs']]] = None,
            authorization: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            service_endpoint_name: Optional[pulumi.Input[str]] = None) -> 'GitHub':
        """
        Get an existing GitHub resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GitHubAuthOauthArgs']] auth_oauth: An `auth_oauth` block as documented below. Allows connecting using an Oauth token.
        :param pulumi.Input[pulumi.InputType['GitHubAuthPersonalArgs']] auth_personal: An `auth_personal` block as documented below. Allows connecting using a personal access token.
        :param pulumi.Input[str] project_id: The project ID or project name.
        :param pulumi.Input[str] service_endpoint_name: The Service Endpoint name.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["auth_oauth"] = auth_oauth
        __props__["auth_personal"] = auth_personal
        __props__["authorization"] = authorization
        __props__["description"] = description
        __props__["project_id"] = project_id
        __props__["service_endpoint_name"] = service_endpoint_name
        return GitHub(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authOauth")
    def auth_oauth(self) -> pulumi.Output[Optional['outputs.GitHubAuthOauth']]:
        """
        An `auth_oauth` block as documented below. Allows connecting using an Oauth token.
        """
        return pulumi.get(self, "auth_oauth")

    @property
    @pulumi.getter(name="authPersonal")
    def auth_personal(self) -> pulumi.Output[Optional['outputs.GitHubAuthPersonal']]:
        """
        An `auth_personal` block as documented below. Allows connecting using a personal access token.
        """
        return pulumi.get(self, "auth_personal")

    @property
    @pulumi.getter
    def authorization(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "authorization")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The project ID or project name.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="serviceEndpointName")
    def service_endpoint_name(self) -> pulumi.Output[str]:
        """
        The Service Endpoint name.
        """
        return pulumi.get(self, "service_endpoint_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


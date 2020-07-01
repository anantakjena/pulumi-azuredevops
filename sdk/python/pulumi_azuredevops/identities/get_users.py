# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetUsersResult:
    """
    A collection of values returned by getUsers.
    """
    def __init__(__self__, id=None, origin=None, origin_id=None, principal_name=None, subject_types=None, users=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if origin and not isinstance(origin, str):
            raise TypeError("Expected argument 'origin' to be a str")
        __self__.origin = origin
        if origin_id and not isinstance(origin_id, str):
            raise TypeError("Expected argument 'origin_id' to be a str")
        __self__.origin_id = origin_id
        if principal_name and not isinstance(principal_name, str):
            raise TypeError("Expected argument 'principal_name' to be a str")
        __self__.principal_name = principal_name
        if subject_types and not isinstance(subject_types, list):
            raise TypeError("Expected argument 'subject_types' to be a list")
        __self__.subject_types = subject_types
        if users and not isinstance(users, list):
            raise TypeError("Expected argument 'users' to be a list")
        __self__.users = users
class AwaitableGetUsersResult(GetUsersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUsersResult(
            id=self.id,
            origin=self.origin,
            origin_id=self.origin_id,
            principal_name=self.principal_name,
            subject_types=self.subject_types,
            users=self.users)

def get_users(origin=None,origin_id=None,principal_name=None,subject_types=None,opts=None):
    """
    Use this data source to access information about an existing users within Azure DevOps.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azuredevops as azuredevops

    user = azuredevops.Identities.get_users(principal_name="contoso-user@contoso.onmicrosoft.com")
    all_users = azuredevops.Identities.get_users()
    all_from_origin = azuredevops.Identities.get_users(origin="aad")
    all_from_subject_types = azuredevops.Identities.get_users(subject_types=[
        "aad",
        "msa",
    ])
    all_from_origin_id = azuredevops.Identities.get_users(origin="aad",
        origin_id="a7ead982-8438-4cd2-b9e3-c3aa51a7b675")
    ```
    ## Relevant Links

    - [Azure DevOps Service REST API 5.1 - Graph Users API](https://docs.microsoft.com/en-us/rest/api/azure/devops/graph/users?view=azure-devops-rest-5.1)
    """
    __args__ = dict()


    __args__['origin'] = origin
    __args__['originId'] = origin_id
    __args__['principalName'] = principal_name
    __args__['subjectTypes'] = subject_types
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azuredevops:Identities/getUsers:getUsers', __args__, opts=opts).value

    return AwaitableGetUsersResult(
        id=__ret__.get('id'),
        origin=__ret__.get('origin'),
        origin_id=__ret__.get('originId'),
        principal_name=__ret__.get('principalName'),
        subject_types=__ret__.get('subjectTypes'),
        users=__ret__.get('users'))

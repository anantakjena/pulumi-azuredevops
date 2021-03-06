# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'AzureRMCredentials',
    'GitHubAuthOauth',
    'GitHubAuthPersonal',
    'KubernetesAzureSubscription',
    'KubernetesKubeconfig',
    'KubernetesServiceAccount',
]

@pulumi.output_type
class AzureRMCredentials(dict):
    def __init__(__self__, *,
                 serviceprincipalid: str,
                 serviceprincipalkey: str,
                 serviceprincipalkey_hash: Optional[str] = None):
        """
        :param str serviceprincipalid: The service principal application Id
        :param str serviceprincipalkey: The service principal secret.
        """
        pulumi.set(__self__, "serviceprincipalid", serviceprincipalid)
        pulumi.set(__self__, "serviceprincipalkey", serviceprincipalkey)
        if serviceprincipalkey_hash is not None:
            pulumi.set(__self__, "serviceprincipalkey_hash", serviceprincipalkey_hash)

    @property
    @pulumi.getter
    def serviceprincipalid(self) -> str:
        """
        The service principal application Id
        """
        return pulumi.get(self, "serviceprincipalid")

    @property
    @pulumi.getter
    def serviceprincipalkey(self) -> str:
        """
        The service principal secret.
        """
        return pulumi.get(self, "serviceprincipalkey")

    @property
    @pulumi.getter(name="serviceprincipalkeyHash")
    def serviceprincipalkey_hash(self) -> Optional[str]:
        return pulumi.get(self, "serviceprincipalkey_hash")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GitHubAuthOauth(dict):
    def __init__(__self__, *,
                 oauth_configuration_id: str):
        pulumi.set(__self__, "oauth_configuration_id", oauth_configuration_id)

    @property
    @pulumi.getter(name="oauthConfigurationId")
    def oauth_configuration_id(self) -> str:
        return pulumi.get(self, "oauth_configuration_id")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GitHubAuthPersonal(dict):
    def __init__(__self__, *,
                 personal_access_token: str,
                 personal_access_token_hash: Optional[str] = None):
        """
        :param str personal_access_token: The Personal Access Token for Github.
        """
        pulumi.set(__self__, "personal_access_token", personal_access_token)
        if personal_access_token_hash is not None:
            pulumi.set(__self__, "personal_access_token_hash", personal_access_token_hash)

    @property
    @pulumi.getter(name="personalAccessToken")
    def personal_access_token(self) -> str:
        """
        The Personal Access Token for Github.
        """
        return pulumi.get(self, "personal_access_token")

    @property
    @pulumi.getter(name="personalAccessTokenHash")
    def personal_access_token_hash(self) -> Optional[str]:
        return pulumi.get(self, "personal_access_token_hash")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class KubernetesAzureSubscription(dict):
    def __init__(__self__, *,
                 cluster_name: str,
                 resourcegroup_id: str,
                 subscription_id: str,
                 subscription_name: str,
                 tenant_id: str,
                 azure_environment: Optional[str] = None,
                 namespace: Optional[str] = None):
        """
        :param str cluster_name: The name of the Kubernetes cluster.
        :param str resourcegroup_id: The resource group name, to which the Kubernetes cluster is deployed.
        :param str subscription_id: The id of the Azure subscription.
        :param str subscription_name: The name of the Azure subscription.
        :param str tenant_id: The id of the tenant used by the subscription.
        :param str azure_environment: Azure environment refers to whether the public cloud offering or domestic (government) clouds are being used. Currently, only the public cloud is supported. The value must be AzureCloud. This is also the default-value.
        :param str namespace: The Kubernetes namespace. Default value is "default".
        """
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "resourcegroup_id", resourcegroup_id)
        pulumi.set(__self__, "subscription_id", subscription_id)
        pulumi.set(__self__, "subscription_name", subscription_name)
        pulumi.set(__self__, "tenant_id", tenant_id)
        if azure_environment is not None:
            pulumi.set(__self__, "azure_environment", azure_environment)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> str:
        """
        The name of the Kubernetes cluster.
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="resourcegroupId")
    def resourcegroup_id(self) -> str:
        """
        The resource group name, to which the Kubernetes cluster is deployed.
        """
        return pulumi.get(self, "resourcegroup_id")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> str:
        """
        The id of the Azure subscription.
        """
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter(name="subscriptionName")
    def subscription_name(self) -> str:
        """
        The name of the Azure subscription.
        """
        return pulumi.get(self, "subscription_name")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The id of the tenant used by the subscription.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="azureEnvironment")
    def azure_environment(self) -> Optional[str]:
        """
        Azure environment refers to whether the public cloud offering or domestic (government) clouds are being used. Currently, only the public cloud is supported. The value must be AzureCloud. This is also the default-value.
        """
        return pulumi.get(self, "azure_environment")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        """
        The Kubernetes namespace. Default value is "default".
        """
        return pulumi.get(self, "namespace")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class KubernetesKubeconfig(dict):
    def __init__(__self__, *,
                 kube_config: str,
                 accept_untrusted_certs: Optional[bool] = None,
                 cluster_context: Optional[str] = None,
                 kube_config_hash: Optional[str] = None):
        """
        :param str kube_config: The content of the kubeconfig in yaml notation to be used to communicate with the API-Server of Kubernetes.
        :param bool accept_untrusted_certs: Set this option to allow clients to accept a self-signed certificate.
        :param str cluster_context: Context within the kubeconfig file that is to be used for identifying the cluster. Default value is the current-context set in kubeconfig.
        """
        pulumi.set(__self__, "kube_config", kube_config)
        if accept_untrusted_certs is not None:
            pulumi.set(__self__, "accept_untrusted_certs", accept_untrusted_certs)
        if cluster_context is not None:
            pulumi.set(__self__, "cluster_context", cluster_context)
        if kube_config_hash is not None:
            pulumi.set(__self__, "kube_config_hash", kube_config_hash)

    @property
    @pulumi.getter(name="kubeConfig")
    def kube_config(self) -> str:
        """
        The content of the kubeconfig in yaml notation to be used to communicate with the API-Server of Kubernetes.
        """
        return pulumi.get(self, "kube_config")

    @property
    @pulumi.getter(name="acceptUntrustedCerts")
    def accept_untrusted_certs(self) -> Optional[bool]:
        """
        Set this option to allow clients to accept a self-signed certificate.
        """
        return pulumi.get(self, "accept_untrusted_certs")

    @property
    @pulumi.getter(name="clusterContext")
    def cluster_context(self) -> Optional[str]:
        """
        Context within the kubeconfig file that is to be used for identifying the cluster. Default value is the current-context set in kubeconfig.
        """
        return pulumi.get(self, "cluster_context")

    @property
    @pulumi.getter(name="kubeConfigHash")
    def kube_config_hash(self) -> Optional[str]:
        return pulumi.get(self, "kube_config_hash")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class KubernetesServiceAccount(dict):
    def __init__(__self__, *,
                 ca_cert: str,
                 token: str,
                 ca_cert_hash: Optional[str] = None,
                 token_hash: Optional[str] = None):
        """
        :param str ca_cert: The certificate from a Kubernetes secret object.
        :param str token: The token from a Kubernetes secret object.
        """
        pulumi.set(__self__, "ca_cert", ca_cert)
        pulumi.set(__self__, "token", token)
        if ca_cert_hash is not None:
            pulumi.set(__self__, "ca_cert_hash", ca_cert_hash)
        if token_hash is not None:
            pulumi.set(__self__, "token_hash", token_hash)

    @property
    @pulumi.getter(name="caCert")
    def ca_cert(self) -> str:
        """
        The certificate from a Kubernetes secret object.
        """
        return pulumi.get(self, "ca_cert")

    @property
    @pulumi.getter
    def token(self) -> str:
        """
        The token from a Kubernetes secret object.
        """
        return pulumi.get(self, "token")

    @property
    @pulumi.getter(name="caCertHash")
    def ca_cert_hash(self) -> Optional[str]:
        return pulumi.get(self, "ca_cert_hash")

    @property
    @pulumi.getter(name="tokenHash")
    def token_hash(self) -> Optional[str]:
        return pulumi.get(self, "token_hash")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop



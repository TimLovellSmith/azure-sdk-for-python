# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ResourceWriteFailureData(Model):
    """Schema of the Data property of an EventGridEvent for a
    Microsoft.Resources.ResourceWriteFailure event. This is raised when a
    resource create or update operation fails.

    :param tenant_id: The tenant ID of the resource.
    :type tenant_id: str
    :param subscription_id: The subscription ID of the resource.
    :type subscription_id: str
    :param resource_group: The resource group of the resource.
    :type resource_group: str
    :param resource_provider: The resource provider performing the operation.
    :type resource_provider: str
    :param resource_uri: The URI of the resource in the operation.
    :type resource_uri: str
    :param operation_name: The operation that was performed.
    :type operation_name: str
    :param status: The status of the operation.
    :type status: str
    :param authorization: The requested authorization for the operation.
    :type authorization: str
    :param claims: The properties of the claims.
    :type claims: str
    :param correlation_id: An operation ID used for troubleshooting.
    :type correlation_id: str
    :param http_request: The details of the operation.
    :type http_request: str
    """

    _attribute_map = {
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'resource_group': {'key': 'resourceGroup', 'type': 'str'},
        'resource_provider': {'key': 'resourceProvider', 'type': 'str'},
        'resource_uri': {'key': 'resourceUri', 'type': 'str'},
        'operation_name': {'key': 'operationName', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'authorization': {'key': 'authorization', 'type': 'str'},
        'claims': {'key': 'claims', 'type': 'str'},
        'correlation_id': {'key': 'correlationId', 'type': 'str'},
        'http_request': {'key': 'httpRequest', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ResourceWriteFailureData, self).__init__(**kwargs)
        self.tenant_id = kwargs.get('tenant_id', None)
        self.subscription_id = kwargs.get('subscription_id', None)
        self.resource_group = kwargs.get('resource_group', None)
        self.resource_provider = kwargs.get('resource_provider', None)
        self.resource_uri = kwargs.get('resource_uri', None)
        self.operation_name = kwargs.get('operation_name', None)
        self.status = kwargs.get('status', None)
        self.authorization = kwargs.get('authorization', None)
        self.claims = kwargs.get('claims', None)
        self.correlation_id = kwargs.get('correlation_id', None)
        self.http_request = kwargs.get('http_request', None)
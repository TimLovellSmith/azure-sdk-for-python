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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import BillingManagementClientConfiguration
from .operations import BillingAccountsOperations
from .operations import AddressOperations
from .operations import AvailableBalancesOperations
from .operations import InstructionsOperations
from .operations import BillingProfilesOperations
from .operations import CustomersOperations
from .operations import InvoiceSectionsOperations
from .operations import BillingPermissionsOperations
from .operations import BillingSubscriptionsOperations
from .operations import ProductsOperations
from .operations import InvoicesOperations
from .operations import TransactionsOperations
from .operations import PoliciesOperations
from .operations import BillingPropertyOperations
from .operations import Operations
from .operations import BillingRoleDefinitionsOperations
from .operations import BillingRoleAssignmentsOperations
from .operations import AgreementsOperations
from .operations import EnrollmentAccountsOperations
from .operations import BillingPeriodsOperations
from . import models


class BillingManagementClient(SDKClient):
    """Billing client provides access to billing resources for Azure subscriptions.

    :ivar config: Configuration for client.
    :vartype config: BillingManagementClientConfiguration

    :ivar billing_accounts: BillingAccounts operations
    :vartype billing_accounts: azure.mgmt.billing.operations.BillingAccountsOperations
    :ivar address: Address operations
    :vartype address: azure.mgmt.billing.operations.AddressOperations
    :ivar available_balances: AvailableBalances operations
    :vartype available_balances: azure.mgmt.billing.operations.AvailableBalancesOperations
    :ivar instructions: Instructions operations
    :vartype instructions: azure.mgmt.billing.operations.InstructionsOperations
    :ivar billing_profiles: BillingProfiles operations
    :vartype billing_profiles: azure.mgmt.billing.operations.BillingProfilesOperations
    :ivar customers: Customers operations
    :vartype customers: azure.mgmt.billing.operations.CustomersOperations
    :ivar invoice_sections: InvoiceSections operations
    :vartype invoice_sections: azure.mgmt.billing.operations.InvoiceSectionsOperations
    :ivar billing_permissions: BillingPermissions operations
    :vartype billing_permissions: azure.mgmt.billing.operations.BillingPermissionsOperations
    :ivar billing_subscriptions: BillingSubscriptions operations
    :vartype billing_subscriptions: azure.mgmt.billing.operations.BillingSubscriptionsOperations
    :ivar products: Products operations
    :vartype products: azure.mgmt.billing.operations.ProductsOperations
    :ivar invoices: Invoices operations
    :vartype invoices: azure.mgmt.billing.operations.InvoicesOperations
    :ivar transactions: Transactions operations
    :vartype transactions: azure.mgmt.billing.operations.TransactionsOperations
    :ivar policies: Policies operations
    :vartype policies: azure.mgmt.billing.operations.PoliciesOperations
    :ivar billing_property: BillingProperty operations
    :vartype billing_property: azure.mgmt.billing.operations.BillingPropertyOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.billing.operations.Operations
    :ivar billing_role_definitions: BillingRoleDefinitions operations
    :vartype billing_role_definitions: azure.mgmt.billing.operations.BillingRoleDefinitionsOperations
    :ivar billing_role_assignments: BillingRoleAssignments operations
    :vartype billing_role_assignments: azure.mgmt.billing.operations.BillingRoleAssignmentsOperations
    :ivar agreements: Agreements operations
    :vartype agreements: azure.mgmt.billing.operations.AgreementsOperations
    :ivar enrollment_accounts: EnrollmentAccounts operations
    :vartype enrollment_accounts: azure.mgmt.billing.operations.EnrollmentAccountsOperations
    :ivar billing_periods: BillingPeriods operations
    :vartype billing_periods: azure.mgmt.billing.operations.BillingPeriodsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID that uniquely identifies an Azure
     subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = BillingManagementClientConfiguration(credentials, subscription_id, base_url)
        super(BillingManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.billing_accounts = BillingAccountsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.address = AddressOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.available_balances = AvailableBalancesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.instructions = InstructionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.billing_profiles = BillingProfilesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.customers = CustomersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.invoice_sections = InvoiceSectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.billing_permissions = BillingPermissionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.billing_subscriptions = BillingSubscriptionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.products = ProductsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.invoices = InvoicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.transactions = TransactionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.policies = PoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.billing_property = BillingPropertyOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.billing_role_definitions = BillingRoleDefinitionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.billing_role_assignments = BillingRoleAssignmentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.agreements = AgreementsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.enrollment_accounts = EnrollmentAccountsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.billing_periods = BillingPeriodsOperations(
            self._client, self.config, self._serialize, self._deserialize)
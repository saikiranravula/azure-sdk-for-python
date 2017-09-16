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

from .health_evaluation import HealthEvaluation


class UpgradeDomainDeltaNodesCheckHealthEvaluation(HealthEvaluation):
    """Represents health evaluation for delta unhealthy cluster nodes in an
    upgrade domain, containing health evaluations for each unhealthy node
    that impacted current aggregated health state.
    Can be returned during cluster upgrade when cluster aggregated health
    state is Warning or Error.
    .

    :param aggregated_health_state: Possible values include: 'Invalid', 'Ok',
     'Warning', 'Error', 'Unknown'
    :type aggregated_health_state: str
    :param description: Description of the health evaluation, which
     represents a summary of the evaluation process.
    :type description: str
    :param Kind: Polymorphic Discriminator
    :type Kind: str
    :param upgrade_domain_name: Name of the upgrade domain where nodes health
     is currently evaluated.
    :type upgrade_domain_name: str
    :param baseline_error_count: Number of upgrade domain nodes with
     aggregated heath state Error in the health store at the beginning of the
     cluster upgrade.
    :type baseline_error_count: long
    :param baseline_total_count: Total number of upgrade domain nodes in the
     health store at the beginning of the cluster upgrade.
    :type baseline_total_count: long
    :param max_percent_delta_unhealthy_nodes: Maximum allowed percentage of
     upgrade domain delta unhealthy nodes from the ClusterUpgradeHealthPolicy.
    :type max_percent_delta_unhealthy_nodes: int
    :param total_count: Total number of upgrade domain nodes in the health
     store.
    :type total_count: long
    :param unhealthy_evaluations:
    :type unhealthy_evaluations: list of :class:`HealthEvaluationWrapper
     <azure.servicefabric.models.HealthEvaluationWrapper>`
    """ 

    _validation = {
        'Kind': {'required': True},
    }

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'description': {'key': 'Description', 'type': 'str'},
        'Kind': {'key': 'Kind', 'type': 'str'},
        'upgrade_domain_name': {'key': 'UpgradeDomainName', 'type': 'str'},
        'baseline_error_count': {'key': 'BaselineErrorCount', 'type': 'long'},
        'baseline_total_count': {'key': 'BaselineTotalCount', 'type': 'long'},
        'max_percent_delta_unhealthy_nodes': {'key': 'MaxPercentDeltaUnhealthyNodes', 'type': 'int'},
        'total_count': {'key': 'TotalCount', 'type': 'long'},
        'unhealthy_evaluations': {'key': 'UnhealthyEvaluations', 'type': '[HealthEvaluationWrapper]'},
    }

    def __init__(self, aggregated_health_state=None, description=None, upgrade_domain_name=None, baseline_error_count=None, baseline_total_count=None, max_percent_delta_unhealthy_nodes=None, total_count=None, unhealthy_evaluations=None):
        super(UpgradeDomainDeltaNodesCheckHealthEvaluation, self).__init__(aggregated_health_state=aggregated_health_state, description=description)
        self.upgrade_domain_name = upgrade_domain_name
        self.baseline_error_count = baseline_error_count
        self.baseline_total_count = baseline_total_count
        self.max_percent_delta_unhealthy_nodes = max_percent_delta_unhealthy_nodes
        self.total_count = total_count
        self.unhealthy_evaluations = unhealthy_evaluations
        self.Kind = 'UpgradeDomainDeltaNodesCheck'

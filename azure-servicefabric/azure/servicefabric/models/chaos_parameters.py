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


class ChaosParameters(Model):
    """Defines all the parameters to configure a Chaos run.
    .

    :param time_to_run_in_seconds: Total time (in seconds) for which Chaos
     will run before automatically stopping. The maximum allowed value is
     4,294,967,295 (System.UInt32.MaxValue).
     . Default value: "4294967295" .
    :type time_to_run_in_seconds: str
    :param max_cluster_stabilization_timeout_in_seconds: The maximum amount
     of time to wait for all cluster entities to become stable and healthy.
     Chaos executes in iterations and at the start of each iteration it
     validates the health of cluster entities.
     During validation if a cluster entity is not stable and healthy within
     MaxClusterStabilizationTimeoutInSeconds, Chaos generates a validation
     failed event.
     . Default value: 60 .
    :type max_cluster_stabilization_timeout_in_seconds: long
    :param max_concurrent_faults: MaxConcurrentFaults is the maximum number
     of concurrent faults induced per iteration.
     Chaos executes in iterations and two consecutive iterations are separated
     by a validation phase.
     The higher the concurrency, the more aggressive the injection of faults
     -- inducing more complex series of states to uncover bugs.
     The recommendation is to start with a value of 2 or 3 and to exercise
     caution while moving up.
     . Default value: 1 .
    :type max_concurrent_faults: long
    :param enable_move_replica_faults: Enables or disables the move primary
     and move secondary faults.
     . Default value: True .
    :type enable_move_replica_faults: bool
    :param wait_time_between_faults_in_seconds: Wait time (in seconds)
     between consecutive faults within a single iteration.
     The larger the value, the lower the overlapping between faults and the
     simpler the sequence of state transitions that the cluster goes through.
     The recommendation is to start with a value between 1 and 5 and exercise
     caution while moving up.
     . Default value: 20 .
    :type wait_time_between_faults_in_seconds: long
    :param wait_time_between_iterations_in_seconds: Time-separation (in
     seconds) between two consecutive iterations of Chaos.
     The larger the value, the lower the fault injection rate.
     . Default value: 30 .
    :type wait_time_between_iterations_in_seconds: long
    :param cluster_health_policy:
    :type cluster_health_policy: :class:`ClusterHealthPolicy
     <azure.servicefabric.models.ClusterHealthPolicy>`
    :param context:
    :type context: :class:`ChaosContext
     <azure.servicefabric.models.ChaosContext>`
    """ 

    _validation = {
        'max_cluster_stabilization_timeout_in_seconds': {'maximum': 4294967295, 'minimum': 0},
        'max_concurrent_faults': {'maximum': 4294967295, 'minimum': 0},
        'wait_time_between_faults_in_seconds': {'maximum': 4294967295, 'minimum': 0},
        'wait_time_between_iterations_in_seconds': {'maximum': 4294967295, 'minimum': 0},
    }

    _attribute_map = {
        'time_to_run_in_seconds': {'key': 'TimeToRunInSeconds', 'type': 'str'},
        'max_cluster_stabilization_timeout_in_seconds': {'key': 'MaxClusterStabilizationTimeoutInSeconds', 'type': 'long'},
        'max_concurrent_faults': {'key': 'MaxConcurrentFaults', 'type': 'long'},
        'enable_move_replica_faults': {'key': 'EnableMoveReplicaFaults', 'type': 'bool'},
        'wait_time_between_faults_in_seconds': {'key': 'WaitTimeBetweenFaultsInSeconds', 'type': 'long'},
        'wait_time_between_iterations_in_seconds': {'key': 'WaitTimeBetweenIterationsInSeconds', 'type': 'long'},
        'cluster_health_policy': {'key': 'ClusterHealthPolicy', 'type': 'ClusterHealthPolicy'},
        'context': {'key': 'Context', 'type': 'ChaosContext'},
    }

    def __init__(self, time_to_run_in_seconds="4294967295", max_cluster_stabilization_timeout_in_seconds=60, max_concurrent_faults=1, enable_move_replica_faults=True, wait_time_between_faults_in_seconds=20, wait_time_between_iterations_in_seconds=30, cluster_health_policy=None, context=None):
        self.time_to_run_in_seconds = time_to_run_in_seconds
        self.max_cluster_stabilization_timeout_in_seconds = max_cluster_stabilization_timeout_in_seconds
        self.max_concurrent_faults = max_concurrent_faults
        self.enable_move_replica_faults = enable_move_replica_faults
        self.wait_time_between_faults_in_seconds = wait_time_between_faults_in_seconds
        self.wait_time_between_iterations_in_seconds = wait_time_between_iterations_in_seconds
        self.cluster_health_policy = cluster_health_policy
        self.context = context

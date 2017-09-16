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

from .deployed_service_replica_detail_info import DeployedServiceReplicaDetailInfo


class DeployedStatelessServiceInstanceDetailInfo(DeployedServiceReplicaDetailInfo):
    """Information about a stateless instance running in a code package. Please
    note that DeployedServiceReplicaQueryResult will contain duplicate data
    like ServiceKind, ServiceName, PartitionId and InstanceId.

    :param service_name:
    :type service_name: str
    :param partition_id:
    :type partition_id: str
    :param current_service_operation: Possible values include: 'Unknown',
     'None', 'Open', 'ChangeRole', 'Close', 'Abort'
    :type current_service_operation: str
    :param current_service_operation_start_time_utc: The start time of the
     current service operation in UTC format.
    :type current_service_operation_start_time_utc: datetime
    :param reported_load:
    :type reported_load: list of :class:`LoadMetricReportInfo
     <azure.servicefabric.models.LoadMetricReportInfo>`
    :param ServiceKind: Polymorphic Discriminator
    :type ServiceKind: str
    :param instance_id:
    :type instance_id: str
    :param deployed_service_replica_query_result:
    :type deployed_service_replica_query_result:
     :class:`DeployedStatelessServiceInstanceInfo
     <azure.servicefabric.models.DeployedStatelessServiceInstanceInfo>`
    """ 

    _validation = {
        'ServiceKind': {'required': True},
    }

    _attribute_map = {
        'service_name': {'key': 'ServiceName', 'type': 'str'},
        'partition_id': {'key': 'PartitionId', 'type': 'str'},
        'current_service_operation': {'key': 'CurrentServiceOperation', 'type': 'str'},
        'current_service_operation_start_time_utc': {'key': 'CurrentServiceOperationStartTimeUtc', 'type': 'iso-8601'},
        'reported_load': {'key': 'ReportedLoad', 'type': '[LoadMetricReportInfo]'},
        'ServiceKind': {'key': 'ServiceKind', 'type': 'str'},
        'instance_id': {'key': 'InstanceId', 'type': 'str'},
        'deployed_service_replica_query_result': {'key': 'DeployedServiceReplicaQueryResult', 'type': 'DeployedStatelessServiceInstanceInfo'},
    }

    def __init__(self, service_name=None, partition_id=None, current_service_operation=None, current_service_operation_start_time_utc=None, reported_load=None, instance_id=None, deployed_service_replica_query_result=None):
        super(DeployedStatelessServiceInstanceDetailInfo, self).__init__(service_name=service_name, partition_id=partition_id, current_service_operation=current_service_operation, current_service_operation_start_time_utc=current_service_operation_start_time_utc, reported_load=reported_load)
        self.instance_id = instance_id
        self.deployed_service_replica_query_result = deployed_service_replica_query_result
        self.ServiceKind = 'Stateless'

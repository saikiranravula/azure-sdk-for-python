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

from .service_info import ServiceInfo


class StatelessServiceInfo(ServiceInfo):
    """Information about a stateless Service Fabric service.

    :param id:
    :type id: str
    :param name:
    :type name: str
    :param type_name:
    :type type_name: str
    :param manifest_version: The version of the service manifest.
    :type manifest_version: str
    :param health_state: Possible values include: 'Invalid', 'Ok', 'Warning',
     'Error', 'Unknown'
    :type health_state: str
    :param service_status: Possible values include: 'Unknown', 'Active',
     'Upgrading', 'Deleting', 'Creating', 'Failed'
    :type service_status: str
    :param is_service_group: Whether the service is in a service group.
    :type is_service_group: bool
    :param ServiceKind: Polymorphic Discriminator
    :type ServiceKind: str
    """ 

    _validation = {
        'ServiceKind': {'required': True},
    }

    def __init__(self, id=None, name=None, type_name=None, manifest_version=None, health_state=None, service_status=None, is_service_group=None):
        super(StatelessServiceInfo, self).__init__(id=id, name=name, type_name=type_name, manifest_version=manifest_version, health_state=health_state, service_status=service_status, is_service_group=is_service_group)
        self.ServiceKind = 'Stateless'

# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.cloud.spanner_admin_instance_v1.types import common
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.spanner.admin.instance.v1",
    manifest={
        "ReplicaInfo",
        "InstanceConfig",
        "AutoscalingConfig",
        "Instance",
        "ListInstanceConfigsRequest",
        "ListInstanceConfigsResponse",
        "GetInstanceConfigRequest",
        "CreateInstanceConfigRequest",
        "UpdateInstanceConfigRequest",
        "DeleteInstanceConfigRequest",
        "ListInstanceConfigOperationsRequest",
        "ListInstanceConfigOperationsResponse",
        "GetInstanceRequest",
        "CreateInstanceRequest",
        "ListInstancesRequest",
        "ListInstancesResponse",
        "UpdateInstanceRequest",
        "DeleteInstanceRequest",
        "CreateInstanceMetadata",
        "UpdateInstanceMetadata",
        "CreateInstanceConfigMetadata",
        "UpdateInstanceConfigMetadata",
        "InstancePartition",
        "CreateInstancePartitionMetadata",
        "CreateInstancePartitionRequest",
        "DeleteInstancePartitionRequest",
        "GetInstancePartitionRequest",
        "UpdateInstancePartitionRequest",
        "UpdateInstancePartitionMetadata",
        "ListInstancePartitionsRequest",
        "ListInstancePartitionsResponse",
        "ListInstancePartitionOperationsRequest",
        "ListInstancePartitionOperationsResponse",
    },
)


class ReplicaInfo(proto.Message):
    r"""

    Attributes:
        location (str):
            The location of the serving resources, e.g.
            "us-central1".
        type_ (google.cloud.spanner_admin_instance_v1.types.ReplicaInfo.ReplicaType):
            The type of replica.
        default_leader_location (bool):
            If true, this location is designated as the default leader
            location where leader replicas are placed. See the `region
            types
            documentation <https://cloud.google.com/spanner/docs/instances#region_types>`__
            for more details.
    """

    class ReplicaType(proto.Enum):
        r"""Indicates the type of replica. See the `replica types
        documentation <https://cloud.google.com/spanner/docs/replication#replica_types>`__
        for more details.

        Values:
            TYPE_UNSPECIFIED (0):
                Not specified.
            READ_WRITE (1):
                Read-write replicas support both reads and writes. These
                replicas:

                -  Maintain a full copy of your data.
                -  Serve reads.
                -  Can vote whether to commit a write.
                -  Participate in leadership election.
                -  Are eligible to become a leader.
            READ_ONLY (2):
                Read-only replicas only support reads (not writes).
                Read-only replicas:

                -  Maintain a full copy of your data.
                -  Serve reads.
                -  Do not participate in voting to commit writes.
                -  Are not eligible to become a leader.
            WITNESS (3):
                Witness replicas don't support reads but do participate in
                voting to commit writes. Witness replicas:

                -  Do not maintain a full copy of data.
                -  Do not serve reads.
                -  Vote whether to commit writes.
                -  Participate in leader election but are not eligible to
                   become leader.
        """
        TYPE_UNSPECIFIED = 0
        READ_WRITE = 1
        READ_ONLY = 2
        WITNESS = 3

    location: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: ReplicaType = proto.Field(
        proto.ENUM,
        number=2,
        enum=ReplicaType,
    )
    default_leader_location: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class InstanceConfig(proto.Message):
    r"""A possible configuration for a Cloud Spanner instance.
    Configurations define the geographic placement of nodes and
    their replication.

    Attributes:
        name (str):
            A unique identifier for the instance configuration. Values
            are of the form
            ``projects/<project>/instanceConfigs/[a-z][-a-z0-9]*``.
        display_name (str):
            The name of this instance configuration as it
            appears in UIs.
        config_type (google.cloud.spanner_admin_instance_v1.types.InstanceConfig.Type):
            Output only. Whether this instance config is
            a Google or User Managed Configuration.
        replicas (MutableSequence[google.cloud.spanner_admin_instance_v1.types.ReplicaInfo]):
            The geographic placement of nodes in this
            instance configuration and their replication
            properties.
        optional_replicas (MutableSequence[google.cloud.spanner_admin_instance_v1.types.ReplicaInfo]):
            Output only. The available optional replicas
            to choose from for user managed configurations.
            Populated for Google managed configurations.
        base_config (str):
            Base configuration name, e.g.
            projects/<project_name>/instanceConfigs/nam3, based on which
            this configuration is created. Only set for user managed
            configurations. ``base_config`` must refer to a
            configuration of type GOOGLE_MANAGED in the same project as
            this configuration.
        labels (MutableMapping[str, str]):
            Cloud Labels are a flexible and lightweight mechanism for
            organizing cloud resources into groups that reflect a
            customer's organizational needs and deployment strategies.
            Cloud Labels can be used to filter collections of resources.
            They can be used to control how resource metrics are
            aggregated. And they can be used as arguments to policy
            management rules (e.g. route, firewall, load balancing,
            etc.).

            -  Label keys must be between 1 and 63 characters long and
               must conform to the following regular expression:
               ``[a-z][a-z0-9_-]{0,62}``.
            -  Label values must be between 0 and 63 characters long and
               must conform to the regular expression
               ``[a-z0-9_-]{0,63}``.
            -  No more than 64 labels can be associated with a given
               resource.

            See https://goo.gl/xmQnxf for more information on and
            examples of labels.

            If you plan to use labels in your own code, please note that
            additional characters may be allowed in the future.
            Therefore, you are advised to use an internal label
            representation, such as JSON, which doesn't rely upon
            specific characters being disallowed. For example,
            representing labels as the string: name + "*" + value would
            prove problematic if we were to allow "*" in a future
            release.
        etag (str):
            etag is used for optimistic concurrency
            control as a way to help prevent simultaneous
            updates of a instance config from overwriting
            each other. It is strongly suggested that
            systems make use of the etag in the
            read-modify-write cycle to perform instance
            config updates in order to avoid race
            conditions: An etag is returned in the response
            which contains instance configs, and systems are
            expected to put that etag in the request to
            update instance config to ensure that their
            change will be applied to the same version of
            the instance config.
            If no etag is provided in the call to update
            instance config, then the existing instance
            config is overwritten blindly.
        leader_options (MutableSequence[str]):
            Allowed values of the "default_leader" schema option for
            databases in instances that use this instance configuration.
        reconciling (bool):
            Output only. If true, the instance config is
            being created or updated. If false, there are no
            ongoing operations for the instance config.
        state (google.cloud.spanner_admin_instance_v1.types.InstanceConfig.State):
            Output only. The current instance config
            state.
    """

    class Type(proto.Enum):
        r"""The type of this configuration.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified.
            GOOGLE_MANAGED (1):
                Google managed configuration.
            USER_MANAGED (2):
                User managed configuration.
        """
        TYPE_UNSPECIFIED = 0
        GOOGLE_MANAGED = 1
        USER_MANAGED = 2

    class State(proto.Enum):
        r"""Indicates the current state of the instance config.

        Values:
            STATE_UNSPECIFIED (0):
                Not specified.
            CREATING (1):
                The instance config is still being created.
            READY (2):
                The instance config is fully created and
                ready to be used to create instances.
        """
        STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    config_type: Type = proto.Field(
        proto.ENUM,
        number=5,
        enum=Type,
    )
    replicas: MutableSequence["ReplicaInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ReplicaInfo",
    )
    optional_replicas: MutableSequence["ReplicaInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="ReplicaInfo",
    )
    base_config: str = proto.Field(
        proto.STRING,
        number=7,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=9,
    )
    leader_options: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=11,
        enum=State,
    )


class AutoscalingConfig(proto.Message):
    r"""Autoscaling config for an instance.

    Attributes:
        autoscaling_limits (google.cloud.spanner_admin_instance_v1.types.AutoscalingConfig.AutoscalingLimits):
            Required. Autoscaling limits for an instance.
        autoscaling_targets (google.cloud.spanner_admin_instance_v1.types.AutoscalingConfig.AutoscalingTargets):
            Required. The autoscaling targets for an
            instance.
    """

    class AutoscalingLimits(proto.Message):
        r"""The autoscaling limits for the instance. Users can define the
        minimum and maximum compute capacity allocated to the instance, and
        the autoscaler will only scale within that range. Users can either
        use nodes or processing units to specify the limits, but should use
        the same unit to set both the min_limit and max_limit.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            min_nodes (int):
                Minimum number of nodes allocated to the
                instance. If set, this number should be greater
                than or equal to 1.

                This field is a member of `oneof`_ ``min_limit``.
            min_processing_units (int):
                Minimum number of processing units allocated
                to the instance. If set, this number should be
                multiples of 1000.

                This field is a member of `oneof`_ ``min_limit``.
            max_nodes (int):
                Maximum number of nodes allocated to the instance. If set,
                this number should be greater than or equal to min_nodes.

                This field is a member of `oneof`_ ``max_limit``.
            max_processing_units (int):
                Maximum number of processing units allocated to the
                instance. If set, this number should be multiples of 1000
                and be greater than or equal to min_processing_units.

                This field is a member of `oneof`_ ``max_limit``.
        """

        min_nodes: int = proto.Field(
            proto.INT32,
            number=1,
            oneof="min_limit",
        )
        min_processing_units: int = proto.Field(
            proto.INT32,
            number=2,
            oneof="min_limit",
        )
        max_nodes: int = proto.Field(
            proto.INT32,
            number=3,
            oneof="max_limit",
        )
        max_processing_units: int = proto.Field(
            proto.INT32,
            number=4,
            oneof="max_limit",
        )

    class AutoscalingTargets(proto.Message):
        r"""The autoscaling targets for an instance.

        Attributes:
            high_priority_cpu_utilization_percent (int):
                Required. The target high priority cpu utilization
                percentage that the autoscaler should be trying to achieve
                for the instance. This number is on a scale from 0 (no
                utilization) to 100 (full utilization). The valid range is
                [10, 90] inclusive.
            storage_utilization_percent (int):
                Required. The target storage utilization percentage that the
                autoscaler should be trying to achieve for the instance.
                This number is on a scale from 0 (no utilization) to 100
                (full utilization). The valid range is [10, 100] inclusive.
        """

        high_priority_cpu_utilization_percent: int = proto.Field(
            proto.INT32,
            number=1,
        )
        storage_utilization_percent: int = proto.Field(
            proto.INT32,
            number=2,
        )

    autoscaling_limits: AutoscalingLimits = proto.Field(
        proto.MESSAGE,
        number=1,
        message=AutoscalingLimits,
    )
    autoscaling_targets: AutoscalingTargets = proto.Field(
        proto.MESSAGE,
        number=2,
        message=AutoscalingTargets,
    )


class Instance(proto.Message):
    r"""An isolated set of Cloud Spanner resources on which databases
    can be hosted.

    Attributes:
        name (str):
            Required. A unique identifier for the instance, which cannot
            be changed after the instance is created. Values are of the
            form
            ``projects/<project>/instances/[a-z][-a-z0-9]*[a-z0-9]``.
            The final segment of the name must be between 2 and 64
            characters in length.
        config (str):
            Required. The name of the instance's configuration. Values
            are of the form
            ``projects/<project>/instanceConfigs/<configuration>``. See
            also
            [InstanceConfig][google.spanner.admin.instance.v1.InstanceConfig]
            and
            [ListInstanceConfigs][google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigs].
        display_name (str):
            Required. The descriptive name for this
            instance as it appears in UIs. Must be unique
            per project and between 4 and 30 characters in
            length.
        node_count (int):
            The number of nodes allocated to this instance. At most one
            of either node_count or processing_units should be present
            in the message.

            Users can set the node_count field to specify the target
            number of nodes allocated to the instance.

            This may be zero in API responses for instances that are not
            yet in state ``READY``.

            See `the
            documentation <https://cloud.google.com/spanner/docs/compute-capacity>`__
            for more information about nodes and processing units.
        processing_units (int):
            The number of processing units allocated to this instance.
            At most one of processing_units or node_count should be
            present in the message.

            Users can set the processing_units field to specify the
            target number of processing units allocated to the instance.

            This may be zero in API responses for instances that are not
            yet in state ``READY``.

            See `the
            documentation <https://cloud.google.com/spanner/docs/compute-capacity>`__
            for more information about nodes and processing units.
        autoscaling_config (google.cloud.spanner_admin_instance_v1.types.AutoscalingConfig):
            Optional. The autoscaling configuration. Autoscaling is
            enabled if this field is set. When autoscaling is enabled,
            node_count and processing_units are treated as OUTPUT_ONLY
            fields and reflect the current compute capacity allocated to
            the instance.
        state (google.cloud.spanner_admin_instance_v1.types.Instance.State):
            Output only. The current instance state. For
            [CreateInstance][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstance],
            the state must be either omitted or set to ``CREATING``. For
            [UpdateInstance][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstance],
            the state must be either omitted or set to ``READY``.
        labels (MutableMapping[str, str]):
            Cloud Labels are a flexible and lightweight mechanism for
            organizing cloud resources into groups that reflect a
            customer's organizational needs and deployment strategies.
            Cloud Labels can be used to filter collections of resources.
            They can be used to control how resource metrics are
            aggregated. And they can be used as arguments to policy
            management rules (e.g. route, firewall, load balancing,
            etc.).

            -  Label keys must be between 1 and 63 characters long and
               must conform to the following regular expression:
               ``[a-z][a-z0-9_-]{0,62}``.
            -  Label values must be between 0 and 63 characters long and
               must conform to the regular expression
               ``[a-z0-9_-]{0,63}``.
            -  No more than 64 labels can be associated with a given
               resource.

            See https://goo.gl/xmQnxf for more information on and
            examples of labels.

            If you plan to use labels in your own code, please note that
            additional characters may be allowed in the future. And so
            you are advised to use an internal label representation,
            such as JSON, which doesn't rely upon specific characters
            being disallowed. For example, representing labels as the
            string: name + "*" + value would prove problematic if we
            were to allow "*" in a future release.
        endpoint_uris (MutableSequence[str]):
            Deprecated. This field is not populated.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the instance
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the instance
            was most recently updated.
    """

    class State(proto.Enum):
        r"""Indicates the current state of the instance.

        Values:
            STATE_UNSPECIFIED (0):
                Not specified.
            CREATING (1):
                The instance is still being created.
                Resources may not be available yet, and
                operations such as database creation may not
                work.
            READY (2):
                The instance is fully created and ready to do
                work such as creating databases.
        """
        STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    config: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    node_count: int = proto.Field(
        proto.INT32,
        number=5,
    )
    processing_units: int = proto.Field(
        proto.INT32,
        number=9,
    )
    autoscaling_config: "AutoscalingConfig" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="AutoscalingConfig",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    endpoint_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )


class ListInstanceConfigsRequest(proto.Message):
    r"""The request for
    [ListInstanceConfigs][google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigs].

    Attributes:
        parent (str):
            Required. The name of the project for which a list of
            supported instance configurations is requested. Values are
            of the form ``projects/<project>``.
        page_size (int):
            Number of instance configurations to be
            returned in the response. If 0 or less, defaults
            to the server's maximum allowed page size.
        page_token (str):
            If non-empty, ``page_token`` should contain a
            [next_page_token][google.spanner.admin.instance.v1.ListInstanceConfigsResponse.next_page_token]
            from a previous
            [ListInstanceConfigsResponse][google.spanner.admin.instance.v1.ListInstanceConfigsResponse].
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListInstanceConfigsResponse(proto.Message):
    r"""The response for
    [ListInstanceConfigs][google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigs].

    Attributes:
        instance_configs (MutableSequence[google.cloud.spanner_admin_instance_v1.types.InstanceConfig]):
            The list of requested instance
            configurations.
        next_page_token (str):
            ``next_page_token`` can be sent in a subsequent
            [ListInstanceConfigs][google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigs]
            call to fetch more of the matching instance configurations.
    """

    @property
    def raw_page(self):
        return self

    instance_configs: MutableSequence["InstanceConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="InstanceConfig",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetInstanceConfigRequest(proto.Message):
    r"""The request for
    [GetInstanceConfigRequest][google.spanner.admin.instance.v1.InstanceAdmin.GetInstanceConfig].

    Attributes:
        name (str):
            Required. The name of the requested instance configuration.
            Values are of the form
            ``projects/<project>/instanceConfigs/<config>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateInstanceConfigRequest(proto.Message):
    r"""The request for
    [CreateInstanceConfigRequest][InstanceAdmin.CreateInstanceConfigRequest].

    Attributes:
        parent (str):
            Required. The name of the project in which to create the
            instance config. Values are of the form
            ``projects/<project>``.
        instance_config_id (str):
            Required. The ID of the instance config to create. Valid
            identifiers are of the form ``custom-[-a-z0-9]*[a-z0-9]``
            and must be between 2 and 64 characters in length. The
            ``custom-`` prefix is required to avoid name conflicts with
            Google managed configurations.
        instance_config (google.cloud.spanner_admin_instance_v1.types.InstanceConfig):
            Required. The InstanceConfig proto of the configuration to
            create. instance_config.name must be
            ``<parent>/instanceConfigs/<instance_config_id>``.
            instance_config.base_config must be a Google managed
            configuration name, e.g. /instanceConfigs/us-east1,
            /instanceConfigs/nam3.
        validate_only (bool):
            An option to validate, but not actually
            execute, a request, and provide the same
            response.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_config_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance_config: "InstanceConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="InstanceConfig",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateInstanceConfigRequest(proto.Message):
    r"""The request for
    [UpdateInstanceConfigRequest][InstanceAdmin.UpdateInstanceConfigRequest].

    Attributes:
        instance_config (google.cloud.spanner_admin_instance_v1.types.InstanceConfig):
            Required. The user instance config to update, which must
            always include the instance config name. Otherwise, only
            fields mentioned in
            [update_mask][google.spanner.admin.instance.v1.UpdateInstanceConfigRequest.update_mask]
            need be included. To prevent conflicts of concurrent
            updates,
            [etag][google.spanner.admin.instance.v1.InstanceConfig.reconciling]
            can be used.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A mask specifying which fields in
            [InstanceConfig][google.spanner.admin.instance.v1.InstanceConfig]
            should be updated. The field mask must always be specified;
            this prevents any future fields in
            [InstanceConfig][google.spanner.admin.instance.v1.InstanceConfig]
            from being erased accidentally by clients that do not know
            about them. Only display_name and labels can be updated.
        validate_only (bool):
            An option to validate, but not actually
            execute, a request, and provide the same
            response.
    """

    instance_config: "InstanceConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="InstanceConfig",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class DeleteInstanceConfigRequest(proto.Message):
    r"""The request for
    [DeleteInstanceConfigRequest][InstanceAdmin.DeleteInstanceConfigRequest].

    Attributes:
        name (str):
            Required. The name of the instance configuration to be
            deleted. Values are of the form
            ``projects/<project>/instanceConfigs/<instance_config>``
        etag (str):
            Used for optimistic concurrency control as a
            way to help prevent simultaneous deletes of an
            instance config from overwriting each other. If
            not empty, the API
            only deletes the instance config when the etag
            provided matches the current status of the
            requested instance config. Otherwise, deletes
            the instance config without checking the current
            status of the requested instance config.
        validate_only (bool):
            An option to validate, but not actually
            execute, a request, and provide the same
            response.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ListInstanceConfigOperationsRequest(proto.Message):
    r"""The request for
    [ListInstanceConfigOperations][google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigOperations].

    Attributes:
        parent (str):
            Required. The project of the instance config operations.
            Values are of the form ``projects/<project>``.
        filter (str):
            An expression that filters the list of returned operations.

            A filter expression consists of a field name, a comparison
            operator, and a value for filtering. The value must be a
            string, a number, or a boolean. The comparison operator must
            be one of: ``<``, ``>``, ``<=``, ``>=``, ``!=``, ``=``, or
            ``:``. Colon ``:`` is the contains operator. Filter rules
            are not case sensitive.

            The following fields in the
            [Operation][google.longrunning.Operation] are eligible for
            filtering:

            -  ``name`` - The name of the long-running operation
            -  ``done`` - False if the operation is in progress, else
               true.
            -  ``metadata.@type`` - the type of metadata. For example,
               the type string for
               [CreateInstanceConfigMetadata][google.spanner.admin.instance.v1.CreateInstanceConfigMetadata]
               is
               ``type.googleapis.com/google.spanner.admin.instance.v1.CreateInstanceConfigMetadata``.
            -  ``metadata.<field_name>`` - any field in metadata.value.
               ``metadata.@type`` must be specified first, if filtering
               on metadata fields.
            -  ``error`` - Error associated with the long-running
               operation.
            -  ``response.@type`` - the type of response.
            -  ``response.<field_name>`` - any field in response.value.

            You can combine multiple expressions by enclosing each
            expression in parentheses. By default, expressions are
            combined with AND logic. However, you can specify AND, OR,
            and NOT logic explicitly.

            Here are a few examples:

            -  ``done:true`` - The operation is complete.
            -  ``(metadata.@type=``
               ``type.googleapis.com/google.spanner.admin.instance.v1.CreateInstanceConfigMetadata) AND``
               ``(metadata.instance_config.name:custom-config) AND``
               ``(metadata.progress.start_time < \"2021-03-28T14:50:00Z\") AND``
               ``(error:*)`` - Return operations where:

               -  The operation's metadata type is
                  [CreateInstanceConfigMetadata][google.spanner.admin.instance.v1.CreateInstanceConfigMetadata].
               -  The instance config name contains "custom-config".
               -  The operation started before 2021-03-28T14:50:00Z.
               -  The operation resulted in an error.
        page_size (int):
            Number of operations to be returned in the
            response. If 0 or less, defaults to the server's
            maximum allowed page size.
        page_token (str):
            If non-empty, ``page_token`` should contain a
            [next_page_token][google.spanner.admin.instance.v1.ListInstanceConfigOperationsResponse.next_page_token]
            from a previous
            [ListInstanceConfigOperationsResponse][google.spanner.admin.instance.v1.ListInstanceConfigOperationsResponse]
            to the same ``parent`` and with the same ``filter``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListInstanceConfigOperationsResponse(proto.Message):
    r"""The response for
    [ListInstanceConfigOperations][google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigOperations].

    Attributes:
        operations (MutableSequence[google.longrunning.operations_pb2.Operation]):
            The list of matching instance config [long-running
            operations][google.longrunning.Operation]. Each operation's
            name will be prefixed by the instance config's name. The
            operation's
            [metadata][google.longrunning.Operation.metadata] field type
            ``metadata.type_url`` describes the type of the metadata.
        next_page_token (str):
            ``next_page_token`` can be sent in a subsequent
            [ListInstanceConfigOperations][google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigOperations]
            call to fetch more of the matching metadata.
    """

    @property
    def raw_page(self):
        return self

    operations: MutableSequence[operations_pb2.Operation] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=operations_pb2.Operation,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetInstanceRequest(proto.Message):
    r"""The request for
    [GetInstance][google.spanner.admin.instance.v1.InstanceAdmin.GetInstance].

    Attributes:
        name (str):
            Required. The name of the requested instance. Values are of
            the form ``projects/<project>/instances/<instance>``.
        field_mask (google.protobuf.field_mask_pb2.FieldMask):
            If field_mask is present, specifies the subset of
            [Instance][google.spanner.admin.instance.v1.Instance] fields
            that should be returned. If absent, all
            [Instance][google.spanner.admin.instance.v1.Instance] fields
            are returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    field_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class CreateInstanceRequest(proto.Message):
    r"""The request for
    [CreateInstance][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstance].

    Attributes:
        parent (str):
            Required. The name of the project in which to create the
            instance. Values are of the form ``projects/<project>``.
        instance_id (str):
            Required. The ID of the instance to create. Valid
            identifiers are of the form ``[a-z][-a-z0-9]*[a-z0-9]`` and
            must be between 2 and 64 characters in length.
        instance (google.cloud.spanner_admin_instance_v1.types.Instance):
            Required. The instance to create. The name may be omitted,
            but if specified must be
            ``<parent>/instances/<instance_id>``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance: "Instance" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Instance",
    )


class ListInstancesRequest(proto.Message):
    r"""The request for
    [ListInstances][google.spanner.admin.instance.v1.InstanceAdmin.ListInstances].

    Attributes:
        parent (str):
            Required. The name of the project for which a list of
            instances is requested. Values are of the form
            ``projects/<project>``.
        page_size (int):
            Number of instances to be returned in the
            response. If 0 or less, defaults to the server's
            maximum allowed page size.
        page_token (str):
            If non-empty, ``page_token`` should contain a
            [next_page_token][google.spanner.admin.instance.v1.ListInstancesResponse.next_page_token]
            from a previous
            [ListInstancesResponse][google.spanner.admin.instance.v1.ListInstancesResponse].
        filter (str):
            An expression for filtering the results of the request.
            Filter rules are case insensitive. The fields eligible for
            filtering are:

            -  ``name``
            -  ``display_name``
            -  ``labels.key`` where key is the name of a label

            Some examples of using filters are:

            -  ``name:*`` --> The instance has a name.
            -  ``name:Howl`` --> The instance's name contains the string
               "howl".
            -  ``name:HOWL`` --> Equivalent to above.
            -  ``NAME:howl`` --> Equivalent to above.
            -  ``labels.env:*`` --> The instance has the label "env".
            -  ``labels.env:dev`` --> The instance has the label "env"
               and the value of the label contains the string "dev".
            -  ``name:howl labels.env:dev`` --> The instance's name
               contains "howl" and it has the label "env" with its value
               containing "dev".
        instance_deadline (google.protobuf.timestamp_pb2.Timestamp):
            Deadline used while retrieving metadata for instances.
            Instances whose metadata cannot be retrieved within this
            deadline will be added to
            [unreachable][google.spanner.admin.instance.v1.ListInstancesResponse.unreachable]
            in
            [ListInstancesResponse][google.spanner.admin.instance.v1.ListInstancesResponse].
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    instance_deadline: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class ListInstancesResponse(proto.Message):
    r"""The response for
    [ListInstances][google.spanner.admin.instance.v1.InstanceAdmin.ListInstances].

    Attributes:
        instances (MutableSequence[google.cloud.spanner_admin_instance_v1.types.Instance]):
            The list of requested instances.
        next_page_token (str):
            ``next_page_token`` can be sent in a subsequent
            [ListInstances][google.spanner.admin.instance.v1.InstanceAdmin.ListInstances]
            call to fetch more of the matching instances.
        unreachable (MutableSequence[str]):
            The list of unreachable instances. It includes the names of
            instances whose metadata could not be retrieved within
            [instance_deadline][google.spanner.admin.instance.v1.ListInstancesRequest.instance_deadline].
    """

    @property
    def raw_page(self):
        return self

    instances: MutableSequence["Instance"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Instance",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class UpdateInstanceRequest(proto.Message):
    r"""The request for
    [UpdateInstance][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstance].

    Attributes:
        instance (google.cloud.spanner_admin_instance_v1.types.Instance):
            Required. The instance to update, which must always include
            the instance name. Otherwise, only fields mentioned in
            [field_mask][google.spanner.admin.instance.v1.UpdateInstanceRequest.field_mask]
            need be included.
        field_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A mask specifying which fields in
            [Instance][google.spanner.admin.instance.v1.Instance] should
            be updated. The field mask must always be specified; this
            prevents any future fields in
            [Instance][google.spanner.admin.instance.v1.Instance] from
            being erased accidentally by clients that do not know about
            them.
    """

    instance: "Instance" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Instance",
    )
    field_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteInstanceRequest(proto.Message):
    r"""The request for
    [DeleteInstance][google.spanner.admin.instance.v1.InstanceAdmin.DeleteInstance].

    Attributes:
        name (str):
            Required. The name of the instance to be deleted. Values are
            of the form ``projects/<project>/instances/<instance>``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateInstanceMetadata(proto.Message):
    r"""Metadata type for the operation returned by
    [CreateInstance][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstance].

    Attributes:
        instance (google.cloud.spanner_admin_instance_v1.types.Instance):
            The instance being created.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which the
            [CreateInstance][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstance]
            request was received.
        cancel_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which this operation was
            cancelled. If set, this operation is in the
            process of undoing itself (which is guaranteed
            to succeed) and cannot be cancelled again.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which this operation failed or
            was completed successfully.
        expected_fulfillment_period (google.cloud.spanner_admin_instance_v1.types.FulfillmentPeriod):
            The expected fulfillment period of this
            create operation.
    """

    instance: "Instance" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Instance",
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    cancel_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    expected_fulfillment_period: common.FulfillmentPeriod = proto.Field(
        proto.ENUM,
        number=5,
        enum=common.FulfillmentPeriod,
    )


class UpdateInstanceMetadata(proto.Message):
    r"""Metadata type for the operation returned by
    [UpdateInstance][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstance].

    Attributes:
        instance (google.cloud.spanner_admin_instance_v1.types.Instance):
            The desired end state of the update.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which
            [UpdateInstance][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstance]
            request was received.
        cancel_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which this operation was
            cancelled. If set, this operation is in the
            process of undoing itself (which is guaranteed
            to succeed) and cannot be cancelled again.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which this operation failed or
            was completed successfully.
        expected_fulfillment_period (google.cloud.spanner_admin_instance_v1.types.FulfillmentPeriod):
            The expected fulfillment period of this
            update operation.
    """

    instance: "Instance" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Instance",
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    cancel_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    expected_fulfillment_period: common.FulfillmentPeriod = proto.Field(
        proto.ENUM,
        number=5,
        enum=common.FulfillmentPeriod,
    )


class CreateInstanceConfigMetadata(proto.Message):
    r"""Metadata type for the operation returned by
    [CreateInstanceConfig][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstanceConfig].

    Attributes:
        instance_config (google.cloud.spanner_admin_instance_v1.types.InstanceConfig):
            The target instance config end state.
        progress (google.cloud.spanner_admin_instance_v1.types.OperationProgress):
            The progress of the
            [CreateInstanceConfig][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstanceConfig]
            operation.
        cancel_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which this operation was
            cancelled.
    """

    instance_config: "InstanceConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="InstanceConfig",
    )
    progress: common.OperationProgress = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.OperationProgress,
    )
    cancel_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class UpdateInstanceConfigMetadata(proto.Message):
    r"""Metadata type for the operation returned by
    [UpdateInstanceConfig][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstanceConfig].

    Attributes:
        instance_config (google.cloud.spanner_admin_instance_v1.types.InstanceConfig):
            The desired instance config after updating.
        progress (google.cloud.spanner_admin_instance_v1.types.OperationProgress):
            The progress of the
            [UpdateInstanceConfig][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstanceConfig]
            operation.
        cancel_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which this operation was
            cancelled.
    """

    instance_config: "InstanceConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="InstanceConfig",
    )
    progress: common.OperationProgress = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.OperationProgress,
    )
    cancel_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class InstancePartition(proto.Message):
    r"""An isolated set of Cloud Spanner resources that databases can
    define placements on.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. A unique identifier for the instance partition.
            Values are of the form
            ``projects/<project>/instances/<instance>/instancePartitions/[a-z][-a-z0-9]*[a-z0-9]``.
            The final segment of the name must be between 2 and 64
            characters in length. An instance partition's name cannot be
            changed after the instance partition is created.
        config (str):
            Required. The name of the instance partition's
            configuration. Values are of the form
            ``projects/<project>/instanceConfigs/<configuration>``. See
            also
            [InstanceConfig][google.spanner.admin.instance.v1.InstanceConfig]
            and
            [ListInstanceConfigs][google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigs].
        display_name (str):
            Required. The descriptive name for this
            instance partition as it appears in UIs. Must be
            unique per project and between 4 and 30
            characters in length.
        node_count (int):
            The number of nodes allocated to this instance partition.

            Users can set the node_count field to specify the target
            number of nodes allocated to the instance partition.

            This may be zero in API responses for instance partitions
            that are not yet in state ``READY``.

            This field is a member of `oneof`_ ``compute_capacity``.
        processing_units (int):
            The number of processing units allocated to this instance
            partition.

            Users can set the processing_units field to specify the
            target number of processing units allocated to the instance
            partition.

            This may be zero in API responses for instance partitions
            that are not yet in state ``READY``.

            This field is a member of `oneof`_ ``compute_capacity``.
        state (google.cloud.spanner_admin_instance_v1.types.InstancePartition.State):
            Output only. The current instance partition
            state.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the instance
            partition was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the instance
            partition was most recently updated.
        referencing_databases (MutableSequence[str]):
            Output only. The names of the databases that
            reference this instance partition. Referencing
            databases should share the parent instance. The
            existence of any referencing database prevents
            the instance partition from being deleted.
        referencing_backups (MutableSequence[str]):
            Output only. The names of the backups that
            reference this instance partition. Referencing
            backups should share the parent instance. The
            existence of any referencing backup prevents the
            instance partition from being deleted.
        etag (str):
            Used for optimistic concurrency control as a
            way to help prevent simultaneous updates of a
            instance partition from overwriting each other.
            It is strongly suggested that systems make use
            of the etag in the read-modify-write cycle to
            perform instance partition updates in order to
            avoid race conditions: An etag is returned in
            the response which contains instance partitions,
            and systems are expected to put that etag in the
            request to update instance partitions to ensure
            that their change will be applied to the same
            version of the instance partition. If no etag is
            provided in the call to update instance
            partition, then the existing instance partition
            is overwritten blindly.
    """

    class State(proto.Enum):
        r"""Indicates the current state of the instance partition.

        Values:
            STATE_UNSPECIFIED (0):
                Not specified.
            CREATING (1):
                The instance partition is still being
                created. Resources may not be available yet, and
                operations such as creating placements using
                this instance partition may not work.
            READY (2):
                The instance partition is fully created and
                ready to do work such as creating placements and
                using in databases.
        """
        STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    config: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    node_count: int = proto.Field(
        proto.INT32,
        number=5,
        oneof="compute_capacity",
    )
    processing_units: int = proto.Field(
        proto.INT32,
        number=6,
        oneof="compute_capacity",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    referencing_databases: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    referencing_backups: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=12,
    )


class CreateInstancePartitionMetadata(proto.Message):
    r"""Metadata type for the operation returned by
    [CreateInstancePartition][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstancePartition].

    Attributes:
        instance_partition (google.cloud.spanner_admin_instance_v1.types.InstancePartition):
            The instance partition being created.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which the
            [CreateInstancePartition][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstancePartition]
            request was received.
        cancel_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which this operation was
            cancelled. If set, this operation is in the
            process of undoing itself (which is guaranteed
            to succeed) and cannot be cancelled again.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which this operation failed or
            was completed successfully.
    """

    instance_partition: "InstancePartition" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="InstancePartition",
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    cancel_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class CreateInstancePartitionRequest(proto.Message):
    r"""The request for
    [CreateInstancePartition][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstancePartition].

    Attributes:
        parent (str):
            Required. The name of the instance in which to create the
            instance partition. Values are of the form
            ``projects/<project>/instances/<instance>``.
        instance_partition_id (str):
            Required. The ID of the instance partition to create. Valid
            identifiers are of the form ``[a-z][-a-z0-9]*[a-z0-9]`` and
            must be between 2 and 64 characters in length.
        instance_partition (google.cloud.spanner_admin_instance_v1.types.InstancePartition):
            Required. The instance partition to create. The
            instance_partition.name may be omitted, but if specified
            must be
            ``<parent>/instancePartitions/<instance_partition_id>``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_partition_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance_partition: "InstancePartition" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="InstancePartition",
    )


class DeleteInstancePartitionRequest(proto.Message):
    r"""The request for
    [DeleteInstancePartition][google.spanner.admin.instance.v1.InstanceAdmin.DeleteInstancePartition].

    Attributes:
        name (str):
            Required. The name of the instance partition to be deleted.
            Values are of the form
            ``projects/{project}/instances/{instance}/instancePartitions/{instance_partition}``
        etag (str):
            Optional. If not empty, the API only deletes
            the instance partition when the etag provided
            matches the current status of the requested
            instance partition. Otherwise, deletes the
            instance partition without checking the current
            status of the requested instance partition.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetInstancePartitionRequest(proto.Message):
    r"""The request for
    [GetInstancePartition][google.spanner.admin.instance.v1.InstanceAdmin.GetInstancePartition].

    Attributes:
        name (str):
            Required. The name of the requested instance partition.
            Values are of the form
            ``projects/{project}/instances/{instance}/instancePartitions/{instance_partition}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateInstancePartitionRequest(proto.Message):
    r"""The request for
    [UpdateInstancePartition][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstancePartition].

    Attributes:
        instance_partition (google.cloud.spanner_admin_instance_v1.types.InstancePartition):
            Required. The instance partition to update, which must
            always include the instance partition name. Otherwise, only
            fields mentioned in
            [field_mask][google.spanner.admin.instance.v1.UpdateInstancePartitionRequest.field_mask]
            need be included.
        field_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A mask specifying which fields in
            [InstancePartition][google.spanner.admin.instance.v1.InstancePartition]
            should be updated. The field mask must always be specified;
            this prevents any future fields in
            [InstancePartition][google.spanner.admin.instance.v1.InstancePartition]
            from being erased accidentally by clients that do not know
            about them.
    """

    instance_partition: "InstancePartition" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="InstancePartition",
    )
    field_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class UpdateInstancePartitionMetadata(proto.Message):
    r"""Metadata type for the operation returned by
    [UpdateInstancePartition][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstancePartition].

    Attributes:
        instance_partition (google.cloud.spanner_admin_instance_v1.types.InstancePartition):
            The desired end state of the update.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which
            [UpdateInstancePartition][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstancePartition]
            request was received.
        cancel_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which this operation was
            cancelled. If set, this operation is in the
            process of undoing itself (which is guaranteed
            to succeed) and cannot be cancelled again.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which this operation failed or
            was completed successfully.
    """

    instance_partition: "InstancePartition" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="InstancePartition",
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    cancel_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class ListInstancePartitionsRequest(proto.Message):
    r"""The request for
    [ListInstancePartitions][google.spanner.admin.instance.v1.InstanceAdmin.ListInstancePartitions].

    Attributes:
        parent (str):
            Required. The instance whose instance partitions should be
            listed. Values are of the form
            ``projects/<project>/instances/<instance>``.
        page_size (int):
            Number of instance partitions to be returned
            in the response. If 0 or less, defaults to the
            server's maximum allowed page size.
        page_token (str):
            If non-empty, ``page_token`` should contain a
            [next_page_token][google.spanner.admin.instance.v1.ListInstancePartitionsResponse.next_page_token]
            from a previous
            [ListInstancePartitionsResponse][google.spanner.admin.instance.v1.ListInstancePartitionsResponse].
        instance_partition_deadline (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Deadline used while retrieving metadata for
            instance partitions. Instance partitions whose metadata
            cannot be retrieved within this deadline will be added to
            [unreachable][google.spanner.admin.instance.v1.ListInstancePartitionsResponse.unreachable]
            in
            [ListInstancePartitionsResponse][google.spanner.admin.instance.v1.ListInstancePartitionsResponse].
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    instance_partition_deadline: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class ListInstancePartitionsResponse(proto.Message):
    r"""The response for
    [ListInstancePartitions][google.spanner.admin.instance.v1.InstanceAdmin.ListInstancePartitions].

    Attributes:
        instance_partitions (MutableSequence[google.cloud.spanner_admin_instance_v1.types.InstancePartition]):
            The list of requested instancePartitions.
        next_page_token (str):
            ``next_page_token`` can be sent in a subsequent
            [ListInstancePartitions][google.spanner.admin.instance.v1.InstanceAdmin.ListInstancePartitions]
            call to fetch more of the matching instance partitions.
        unreachable (MutableSequence[str]):
            The list of unreachable instance partitions. It includes the
            names of instance partitions whose metadata could not be
            retrieved within
            [instance_partition_deadline][google.spanner.admin.instance.v1.ListInstancePartitionsRequest.instance_partition_deadline].
    """

    @property
    def raw_page(self):
        return self

    instance_partitions: MutableSequence["InstancePartition"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="InstancePartition",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ListInstancePartitionOperationsRequest(proto.Message):
    r"""The request for
    [ListInstancePartitionOperations][google.spanner.admin.instance.v1.InstanceAdmin.ListInstancePartitionOperations].

    Attributes:
        parent (str):
            Required. The parent instance of the instance partition
            operations. Values are of the form
            ``projects/<project>/instances/<instance>``.
        filter (str):
            Optional. An expression that filters the list of returned
            operations.

            A filter expression consists of a field name, a comparison
            operator, and a value for filtering. The value must be a
            string, a number, or a boolean. The comparison operator must
            be one of: ``<``, ``>``, ``<=``, ``>=``, ``!=``, ``=``, or
            ``:``. Colon ``:`` is the contains operator. Filter rules
            are not case sensitive.

            The following fields in the
            [Operation][google.longrunning.Operation] are eligible for
            filtering:

            -  ``name`` - The name of the long-running operation
            -  ``done`` - False if the operation is in progress, else
               true.
            -  ``metadata.@type`` - the type of metadata. For example,
               the type string for
               [CreateInstancePartitionMetadata][google.spanner.admin.instance.v1.CreateInstancePartitionMetadata]
               is
               ``type.googleapis.com/google.spanner.admin.instance.v1.CreateInstancePartitionMetadata``.
            -  ``metadata.<field_name>`` - any field in metadata.value.
               ``metadata.@type`` must be specified first, if filtering
               on metadata fields.
            -  ``error`` - Error associated with the long-running
               operation.
            -  ``response.@type`` - the type of response.
            -  ``response.<field_name>`` - any field in response.value.

            You can combine multiple expressions by enclosing each
            expression in parentheses. By default, expressions are
            combined with AND logic. However, you can specify AND, OR,
            and NOT logic explicitly.

            Here are a few examples:

            -  ``done:true`` - The operation is complete.
            -  ``(metadata.@type=``
               ``type.googleapis.com/google.spanner.admin.instance.v1.CreateInstancePartitionMetadata) AND``
               ``(metadata.instance_partition.name:custom-instance-partition) AND``
               ``(metadata.start_time < \"2021-03-28T14:50:00Z\") AND``
               ``(error:*)`` - Return operations where:

               -  The operation's metadata type is
                  [CreateInstancePartitionMetadata][google.spanner.admin.instance.v1.CreateInstancePartitionMetadata].
               -  The instance partition name contains
                  "custom-instance-partition".
               -  The operation started before 2021-03-28T14:50:00Z.
               -  The operation resulted in an error.
        page_size (int):
            Optional. Number of operations to be returned
            in the response. If 0 or less, defaults to the
            server's maximum allowed page size.
        page_token (str):
            Optional. If non-empty, ``page_token`` should contain a
            [next_page_token][google.spanner.admin.instance.v1.ListInstancePartitionOperationsResponse.next_page_token]
            from a previous
            [ListInstancePartitionOperationsResponse][google.spanner.admin.instance.v1.ListInstancePartitionOperationsResponse]
            to the same ``parent`` and with the same ``filter``.
        instance_partition_deadline (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Deadline used while retrieving metadata for
            instance partition operations. Instance partitions whose
            operation metadata cannot be retrieved within this deadline
            will be added to
            [unreachable][ListInstancePartitionOperationsResponse.unreachable]
            in
            [ListInstancePartitionOperationsResponse][google.spanner.admin.instance.v1.ListInstancePartitionOperationsResponse].
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    instance_partition_deadline: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class ListInstancePartitionOperationsResponse(proto.Message):
    r"""The response for
    [ListInstancePartitionOperations][google.spanner.admin.instance.v1.InstanceAdmin.ListInstancePartitionOperations].

    Attributes:
        operations (MutableSequence[google.longrunning.operations_pb2.Operation]):
            The list of matching instance partition [long-running
            operations][google.longrunning.Operation]. Each operation's
            name will be prefixed by the instance partition's name. The
            operation's
            [metadata][google.longrunning.Operation.metadata] field type
            ``metadata.type_url`` describes the type of the metadata.
        next_page_token (str):
            ``next_page_token`` can be sent in a subsequent
            [ListInstancePartitionOperations][google.spanner.admin.instance.v1.InstanceAdmin.ListInstancePartitionOperations]
            call to fetch more of the matching metadata.
        unreachable_instance_partitions (MutableSequence[str]):
            The list of unreachable instance partitions. It includes the
            names of instance partitions whose operation metadata could
            not be retrieved within
            [instance_partition_deadline][google.spanner.admin.instance.v1.ListInstancePartitionOperationsRequest.instance_partition_deadline].
    """

    @property
    def raw_page(self):
        return self

    operations: MutableSequence[operations_pb2.Operation] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=operations_pb2.Operation,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable_instance_partitions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))

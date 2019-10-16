#!/usr/bin/python
# Copyright (c) 2017, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_autoscaling_auto_scaling_configuration
short_description: Manage an AutoScalingConfiguration resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an AutoScalingConfiguration resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an autoscaling configuration.
version_added: "2.5"
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the autoscaling configuration.
            - Required for create using I(state=present).
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    cool_down_in_seconds:
        description:
            - The minimum period of time to wait between scaling actions. The cooldown period gives the system time to stabilize
              before rescaling. The minimum value is 300 seconds, which is also the default.
        type: int
    is_enabled:
        description:
            - Whether the autoscaling configuration is enabled.
        type: bool
    policies:
        description:
            - ""
            - Required for create using I(state=present).
        type: list
        suboptions:
            capacity:
                description:
                    - The capacity requirements of the autoscaling policy.
                type: dict
                required: true
                suboptions:
                    max:
                        description:
                            - The maximum number of instances the instance pool is allowed to increase to (scale out).
                        type: int
                        required: true
                    min:
                        description:
                            - The minimum number of instances the instance pool is allowed to decrease to (scale in).
                        type: int
                        required: true
                    initial:
                        description:
                            - The initial number of instances to launch in the instance pool immediately after autoscaling is
                              enabled. After autoscaling retrieves performance metrics, the number of instances is automatically adjusted from this
                              initial number to a number that is based on the limits that you set.
                        type: int
                        required: true
            display_name:
                description:
                    - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
                aliases: ["name"]
            policy_type:
                description:
                    - The type of autoscaling policy.
                choices:
                    - "threshold"
                required: true
            rules:
                description:
                    - ""
                type: list
                required: true
                suboptions:
                    action:
                        description:
                            - ""
                        type: dict
                        required: true
                        suboptions:
                            type:
                                description:
                                    - The type of action to take.
                                choices:
                                    - "CHANGE_COUNT_BY"
                                required: true
                            value:
                                description:
                                    - To scale out (increase the number of instances), provide a positive value. To scale in (decrease the number of
                                      instances), provide a negative value.
                                type: int
                                required: true
                    display_name:
                        description:
                            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
                        aliases: ["name"]
                    metric:
                        description:
                            - ""
                        type: dict
                        required: true
                        suboptions:
                            metric_type:
                                description:
                                    - ""
                                choices:
                                    - "CPU_UTILIZATION"
                                    - "MEMORY_UTILIZATION"
                                required: true
                            threshold:
                                description:
                                    - ""
                                type: dict
                                required: true
                                suboptions:
                                    operator:
                                        description:
                                            - The comparison operator to use. Options are greater than (`GT`), greater than or equal to
                                              (`GTE`), less than (`LT`), and less than or equal to (`LTE`).
                                        choices:
                                            - "GT"
                                            - "GTE"
                                            - "LT"
                                            - "LTE"
                                        required: true
                                    value:
                                        description:
                                            - ""
                                        type: int
                                        required: true
    resource:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            type:
                description:
                    - The type of resource.
                choices:
                    - "instancePool"
                required: true
            id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource that is managed by the autoscaling
                      configuration.
                required: true
    auto_scaling_configuration_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the autoscaling configuration.
            - Required for update using I(state=present), I(state=absent).
        aliases: ["id"]
    state:
        description:
            - The state of the AutoScalingConfiguration.
            - Use I(state=present) to create or update an AutoScalingConfiguration.
            - Use I(state=absent) to delete an AutoScalingConfiguration.
        required: false
        default: 'present'
        choices: ["present", "absent"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle, oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create auto_scaling_configuration
  oci_autoscaling_auto_scaling_configuration:
    compartment_id: ocid1.compartment.oc1..<var>&lt;unique_ID&gt;</var>
    display_name: example_autoscaling_configuration
    cool_down_in_seconds: 300
    is_enabled: true
    policies:
    - capacity:
        max: 50
        min: 10
        initial: 15
      display_name: example_autoscaling_policy
      policy_type: threshold
      rules:
      - action:
          type: CHANGE_COUNT_BY
          value: 5
        display_name: example_scale_out_condition
        metric:
          metric_type: CPU_UTILIZATION
          threshold:
            operator: GTE
            value: 90
      - action:
          type: CHANGE_COUNT_BY
          value: -5
        display_name: example_scale_in_condition
        metric:
          metric_type: CPU_UTILIZATION
          threshold:
            operator: LTE
            value: 25
    resource:
      type: instancePool
      id: ocid1.instancepool.oc1..<var>&lt;unique_ID&gt;</var>

- name: Update auto_scaling_configuration
  oci_autoscaling_auto_scaling_configuration:
    display_name: example_autoscaling_configuration
    is_enabled: false
    cool_down_in_seconds: 600
    auto_scaling_configuration_id: ocid1.autoscalingconfiguration.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete auto_scaling_configuration
  oci_autoscaling_auto_scaling_configuration:
    auto_scaling_configuration_id: ocid1.autoscalingconfiguration.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
auto_scaling_configuration:
    description:
        - Details of the AutoScalingConfiguration resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the autoscaling
                  configuration.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the autoscaling configuration.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        cool_down_in_seconds:
            description:
                - The minimum period of time to wait between scaling actions. The cooldown period gives the system time to stabilize
                  before rescaling. The minimum value is 300 seconds, which is also the default.
            returned: on success
            type: int
            sample: 56
        is_enabled:
            description:
                - Whether the autoscaling configuration is enabled.
            returned: on success
            type: bool
            sample: true
        resource:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - The type of resource.
                    returned: on success
                    type: string
                    sample: instancePool
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource that is managed by the autoscaling
                          configuration.
                    returned: on success
                    type: string
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        policies:
            description:
                - Autoscaling policy definitions for the autoscaling configuration. An autoscaling policy defines the criteria that
                  trigger autoscaling actions and the actions to take.
                - Each autoscaling configuration can have one autoscaling policy.
            returned: on success
            type: complex
            contains:
                capacity:
                    description:
                        - The capacity requirements of the autoscaling policy.
                    returned: on success
                    type: complex
                    contains:
                        max:
                            description:
                                - The maximum number of instances the instance pool is allowed to increase to (scale out).
                            returned: on success
                            type: int
                            sample: 56
                        min:
                            description:
                                - The minimum number of instances the instance pool is allowed to decrease to (scale in).
                            returned: on success
                            type: int
                            sample: 56
                        initial:
                            description:
                                - The initial number of instances to launch in the instance pool immediately after autoscaling is
                                  enabled. After autoscaling retrieves performance metrics, the number of instances is automatically adjusted from this
                                  initial number to a number that is based on the limits that you set.
                            returned: on success
                            type: int
                            sample: 56
                id:
                    description:
                        - The ID of the autoscaling policy that is assigned after creation.
                    returned: on success
                    type: string
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                display_name:
                    description:
                        - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
                    returned: on success
                    type: string
                    sample: display_name_example
                policy_type:
                    description:
                        - The type of autoscaling policy.
                    returned: on success
                    type: string
                    sample: policy_type_example
                time_created:
                    description:
                        - The date and time the autoscaling configuration was created, in the format defined by RFC3339.
                        - "Example: `2016-08-25T21:10:29.600Z`"
                    returned: on success
                    type: string
                    sample: 2016-08-25T21:10:29.600Z
                rules:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        action:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                type:
                                    description:
                                        - The type of action to take.
                                    returned: on success
                                    type: string
                                    sample: CHANGE_COUNT_BY
                                value:
                                    description:
                                        - To scale out (increase the number of instances), provide a positive value. To scale in (decrease the number of
                                          instances), provide a negative value.
                                    returned: on success
                                    type: int
                                    sample: 56
                        display_name:
                            description:
                                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
                            returned: on success
                            type: string
                            sample: display_name_example
                        id:
                            description:
                                - ID of the condition that is assigned after creation.
                            returned: on success
                            type: string
                            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                        metric:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                metric_type:
                                    description:
                                        - ""
                                    returned: on success
                                    type: string
                                    sample: CPU_UTILIZATION
                                threshold:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        operator:
                                            description:
                                                - The comparison operator to use. Options are greater than (`GT`), greater than or equal to
                                                  (`GTE`), less than (`LT`), and less than or equal to (`LTE`).
                                            returned: on success
                                            type: string
                                            sample: GT
                                        value:
                                            description:
                                                - ""
                                            returned: on success
                                            type: int
                                            sample: 56
        time_created:
            description:
                - The date and time the AutoScalingConfiguration was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "cool_down_in_seconds": 56,
        "is_enabled": true,
        "resource": {
            "type": "instancePool",
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "policies": [{
            "capacity": {
                "max": 56,
                "min": 56,
                "initial": 56
            },
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "policy_type": "policy_type_example",
            "time_created": "2016-08-25T21:10:29.600Z",
            "rules": [{
                "action": {
                    "type": "CHANGE_COUNT_BY",
                    "value": 56
                },
                "display_name": "display_name_example",
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "metric": {
                    "metric_type": "CPU_UTILIZATION",
                    "threshold": {
                        "operator": "GT",
                        "value": 56
                    }
                }
            }]
        }],
        "time_created": "2016-08-25T21:10:29.600Z"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_common_utils
from ansible.module_utils.oracle.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.autoscaling import AutoScalingClient
    from oci.autoscaling.models import CreateAutoScalingConfigurationDetails
    from oci.autoscaling.models import UpdateAutoScalingConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutoScalingConfigurationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    @staticmethod
    def get_module_resource_id_param():
        return "auto_scaling_configuration_id"

    def get_module_resource_id(self):
        return self.module.params.get("auto_scaling_configuration_id")

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_auto_scaling_configuration,
            auto_scaling_configuration_id=self.module.params.get(
                "auto_scaling_configuration_id"
            ),
        )

    def list_resources(self):
        required_list_method_params = ["compartment_id"]

        optional_list_method_params = ["display_name"]

        required_kwargs = dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                not self.module.params.get("key_by")
                or param in self.module.params.get("key_by")
            )
        )

        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)

        return oci_common_utils.list_all_resources(
            self.client.list_auto_scaling_configurations, **kwargs
        )

    def get_create_model_class(self):
        return CreateAutoScalingConfigurationDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_common_utils.call_with_backoff(
            self.client.create_auto_scaling_configuration,
            create_auto_scaling_configuration_details=create_details,
        )

    def get_update_model_class(self):
        return UpdateAutoScalingConfigurationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_common_utils.call_with_backoff(
            self.client.update_auto_scaling_configuration,
            auto_scaling_configuration_id=self.module.params.get(
                "auto_scaling_configuration_id"
            ),
            update_auto_scaling_configuration_details=update_details,
        )

    def delete_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.delete_auto_scaling_configuration,
            auto_scaling_configuration_id=self.module.params.get(
                "auto_scaling_configuration_id"
            ),
        )


AutoScalingConfigurationHelperCustom = get_custom_class(
    "AutoScalingConfigurationHelperCustom"
)


class ResourceHelper(
    AutoScalingConfigurationHelperCustom, AutoScalingConfigurationHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            cool_down_in_seconds=dict(type="int"),
            is_enabled=dict(type="bool"),
            policies=dict(
                type="list",
                elements="dict",
                options=dict(
                    capacity=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            max=dict(type="int", required=True),
                            min=dict(type="int", required=True),
                            initial=dict(type="int", required=True),
                        ),
                    ),
                    display_name=dict(aliases=["name"], type="str"),
                    policy_type=dict(type="str", required=True, choices=["threshold"]),
                    rules=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            action=dict(
                                type="dict",
                                required=True,
                                options=dict(
                                    type=dict(
                                        type="str",
                                        required=True,
                                        choices=["CHANGE_COUNT_BY"],
                                    ),
                                    value=dict(type="int", required=True),
                                ),
                            ),
                            display_name=dict(aliases=["name"], type="str"),
                            metric=dict(
                                type="dict",
                                required=True,
                                options=dict(
                                    metric_type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "CPU_UTILIZATION",
                                            "MEMORY_UTILIZATION",
                                        ],
                                    ),
                                    threshold=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            operator=dict(
                                                type="str",
                                                required=True,
                                                choices=["GT", "GTE", "LT", "LTE"],
                                            ),
                                            value=dict(type="int", required=True),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            resource=dict(
                type="dict",
                options=dict(
                    type=dict(type="str", required=True, choices=["instancePool"]),
                    id=dict(type="str", required=True),
                ),
            ),
            auto_scaling_configuration_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="auto_scaling_configuration",
        service_client_class=AutoScalingClient,
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

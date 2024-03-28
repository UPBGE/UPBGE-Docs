.. _bpy.types.ActuatorSensor:

==============================
Actuator Sensor
==============================

.. seealso::
   See the Python reference of this logic brick in :class:`SCA_ActuatorSensor`.

The *Actuator Sensor* detects when a particular actuator receives an activation pulse. It sends a ``TRUE`` pulse when the specified actuator is activated. The sensor also sends a ``FALSE`` pulse when the specified actuator is deactivated.

.. figure:: /images/logic_bricks/sensors/logic-sensors-types-actuator-actuator.png

   Actuator sensor

Properties
++++++++++++++++++++++++++++++

See :ref:`Sensor Common Options <game-engine-logic-sensors-common-options>` for common options.

Actuator
   Name of actuator

   .. note::
      The actuator referenced must be owned by the same object.

Example
++++++++++++++++++++++++++++++

.. _bpy.types.ActuatorSensor:

***************
Actuator Sensor
***************

The *Actuator Sensor* detects when a particular actuator receives an activation pulse.
It sends a ``TRUE`` pulse when the specified actuator is activated.
The sensor also sends a ``FALSE`` pulse when the specified actuator is deactivated.

.. figure:: /images/game-engine_logic_sensors_types_actuator_node.png
   :width: 300px

   Actuator sensor.


Properties
==========

See :ref:`Sensor Common Options <game-engine-logic-sensors-common-options>` for common options.

Actuator
   Name of actuator (n.b. this must be owned by the same object).


Example
=======

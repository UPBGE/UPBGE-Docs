.. _bpy.types.PropertySensor:

***************
Property Sensor
***************

The *Property Sensor* detects changes in the properties of its owner object.

.. figure:: /images/game-engine_logic_sensors_types_property_node.png
   :width: 300px

   Property sensor.


Properties
==========

See :ref:`Sensor Common Options <game-engine-logic-sensors-common-options>` for common options.

Evaluation Type
   Specifies how the property will be evaluated against the value(s).
Greater Than
   Sends a ``TRUE`` pulse when the property value is greater than the *Value* in the sensor.
Less Than
   Sends a ``TRUE`` pulse when the property value is less than the *Value* in the sensor.
Changed
   Sends a ``TRUE`` pulse as soon as the property value changes.
Interval
   Sends a ``TRUE`` pulse when the *Value* of the property is between the *Min* and *Max* values of the sensor.
Not Equal
   Sends a ``TRUE`` pulse when the property value differs from the *Value* in the sensor.
Equal
   Sends a ``TRUE`` pulse when the property value matches the *Value* in the sensor.

.. note::

   The names of other properties can also be entered to compare properties.


Example
=======

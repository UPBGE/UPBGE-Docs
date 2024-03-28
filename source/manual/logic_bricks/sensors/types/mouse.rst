.. _bpy.types.MouseSensor:

==============================
Mouse Sensor
==============================

.. seealso::
   See the Python reference of this logic brick in :class:`SCA_MouseSensor`.

The *Mouse Sensor* detects mouse events.

.. figure:: /images/logic_bricks/sensors/logic-sensors-types-mouse-mouse.png

   Mouse sensor

Properties
++++++++++++++++++++++++++++++

See :ref:`Sensor Common Options <game-engine-logic-sensors-common-options>` for common options.

The controller consist only of a list of types of mouse events. A ``FALSE`` pulse is given when any of these conditions ends.

Mouse over any
   Gives a ``TRUE`` pulse if the mouse moves over any game object.

Mouse over
   Gives a ``TRUE`` pulse if the mouse moves over the owner object.

Movement
   Any movement with the mouse causes a stream of ``TRUE`` pulses.

Wheel Down
   Causes a stream of ``TRUE`` pulses as the scroll wheel of the mouse moves down.

Wheel Up
   Causes a stream of ``TRUE`` pulses as the scroll wheel of the mouse moves up.

Right button
   Gives a ``TRUE`` pulse when right mouse button is pressed.

Middle button
   Gives a ``TRUE`` pulse when middle mouse button is pressed.

Left button
   Gives a ``TRUE`` pulse when left mouse button is pressed.

Button 4 
   Gives a ``TRUE`` pulse when 4th mouse button is pressed.

Button 5
   Gives a ``TRUE`` pulse when 5th mouse button is pressed.

Button 6
   Gives a ``TRUE`` pulse when 6th mouse button is pressed. This button depends in mouse configuration software. It is possible that doesn't work correctly.

Button 7
   Gives a ``TRUE`` pulse when 7th mouse button is pressed. This button depends in mouse configuration software. It is possible that doesn't work correctly.

.. note::
   There is a logic brick for specific mouse movement and reactions (such as first person camera), see :ref:`Mouse Actuator <bpy.types.MouseActuator>`.

.. _bpy.types.JoystickSensor:

***************
Joystick Sensor
***************

The *Joystick Sensor* triggers whenever the joystick moves.
It also detects events on a range of ancillary controls on the joystick device (hat, buttons, etc.).
More than one joystick may be used (see "Index").
The exact layout of the joystick controls will depend on the make and model of joystick used.

.. figure:: /images/game-engine_logic_sensors_types_joystick_button.jpg
   :width: 200px

   Joystick sensor.


Properties
==========

See :ref:`Sensor Common Options <game-engine-logic-sensors-common-options>` for common options.

Event Type
   A menu to select which joystick event to use, each is described later.
Index
   Specifies which joystick to use.
All Events
   Sensor triggers for all events on this joystick's current type.


Single Axis
-----------

Detect movement in a single joystick Axis.

.. figure:: /images/game-engine_logic_sensors_types_joystick_single-axis.png
   :width: 200px

   Joystick Single Axis.

Axis Number
   Axis to detect a change.

   - 1 = Horizontal axis (left/right)
   - 2 = Vertical axis (forward/back)
   - 3 = Paddle axis up/down
   - 4 = Joystick axis twist left/right
Axis Threshold
   Threshold at which joystick fires.


Hat
---

Detects movement of a specific hat control on the joystick.

.. figure:: /images/game-engine_logic_sensors_types_joystick_hat.png
   :width: 200px

   Joystick Hat.

Hat number
   Specifies which hat to use (max. 2).
Hat Direction
   Specifies the direction to use: up, down, left, right, up/right, up/left, down/right, down/left.


Axis
----

.. figure:: /images/game-engine_logic_sensors_types_joystick_axis.jpg
   :width: 200px

   Joystick Axis.

Axis Number
   Specifies the axis (1 or 2).
Axis Threshold
   Threshold at which joystick fires.
Axis Direction
   Specifies the direction to use:

   - (Axis Number = 1) Joystick Left, Right, Up, Down
   - (Axis Number = 2) Paddle upper (Left); paddle Lower (Right);
   - Joystick twist left (Up) Joystick twist right (Down)


Button
------

.. figure:: /images/game-engine_logic_sensors_types_joystick_button.jpg
   :width: 200px

   Joystick Button.

Specifies the *button number* to use.


Example
=======

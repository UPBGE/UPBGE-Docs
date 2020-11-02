.. _bpy.types.JoystickSensor:

***************
Joystick Sensor
***************

.. seealso::
   See the Python reference of this logic brick in :class:`SCA_JoystickSensor`.

The *Joystick Sensor* triggers whenever the joystick moves.
It also detects events on a range of ancillary controls on the joystick device (hat, buttons, etc.).
More than one joystick may be used (see "Index").
The exact layout of the joystick controls will depend on the make and model of joystick used.

.. figure:: /images/Logic/logic-sensors-types-joystick-button.png

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


Stick Directions
----------------

Detect movement in a stick

.. figure:: /images/Logic/logic-sensors-types-joystick-stick-directions.png

   Joystick Stick Directions.

Stick
   Stick to detect a input: Left Stick/Right Stick.

Stick Direction
   Direction of the stick moving: Right/Left, Up/Down.


Stick Axis
----------

Detects the axis of the joystick.

.. figure:: /images/Logic/logic-sensors-types-joystick-stick-axis.png

   Joystick Stick Axis.

Stick Axis
   Which axis either of the sticks are moving on Left/Right Stick Horizontal, Left/Right Stick Vertical.


Shoulder Triggers
-----------------

.. figure:: /images/Logic/logic-sensors-types-joystick-shoulder-triggers.png

   Joystick Shoulder Triggers.

Triggers
   Triggers that are used: Left/Right Shoulder Trigger.


Buttons
-------

.. figure:: /images/Logic/logic-sensors-types-joystick-button.png

   Joystick Buttons.

Button
   Buttons that are used: A/B/X/Y, Dpad Right/Left/Up/Down, Right/Left Shoulder, Right/Left Stick, Start/Guide.


Example
=======

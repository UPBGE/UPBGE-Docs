.. _bpy.types.JoystickSensor:

==============================
Joystick Sensor
==============================

.. seealso::
   See the Python reference of this logic brick in :class:`SCA_JoystickSensor`.

The *Joystick Sensor* triggers whenever the joystick moves. It also detects events on a range of ancillary controls on the joystick device (shoulder triggers, buttons, etc.). More than one joystick may be used (see "Joystick Index").

.. note::
   UPBGE maps all the joysticks against the layout of Xbox 360 game controller. This way is easier to setup the different movements or actions because you have to do it for one type of controller only.

.. figure:: /images/logic_bricks/sensors/logic-sensors-types-joystick-button.png

   Joystick sensor

Properties
++++++++++++++++++++++++++++++

See :ref:`Sensor Common Options <game-engine-logic-sensors-common-options>` for common options.

Event Type
   A menu to select which joystick event to use, each is described later.
Joystick Index
   Specifies which joystick to use.
All Events
   Sensor triggers for all events on this joystick's current type.

Stick Directions
------------------------------

Detect movement in a stick.

.. figure:: /images/logic_bricks/sensors/logic-sensors-types-joystick-stick-directions.png

   Joystick Stick Directions

Stick
   Stick to detect a input: Left Stick/Right Stick.

Stick Direction
   Direction of the stick moving: Right/Left, Up/Down.

Stick Axis
------------------------------

Detects the axis of the joystick.

.. figure:: /images/logic_bricks/sensors/logic-sensors-types-joystick-stick-axis.png

   Joystick Stick Axis

Stick Axis
   Which axis either of the sticks are moving on Left Stick Horizontal/Vertical, Right Stick Horizontal/Vertical.

Shoulder Triggers
------------------------------

.. figure:: /images/logic_bricks/sensors/logic-sensors-types-joystick-shoulder-triggers.png

   Joystick Shoulder Triggers

Triggers
   Triggers that are used: Left/Right Shoulder Trigger.

Buttons
------------------------------

.. figure:: /images/logic_bricks/sensors/logic-sensors-types-joystick-button.png

   Joystick Buttons

Button
   Buttons that are used: ``A``, ``B``, ``X``, ``Y``, Dpad Right/Left/Up/Down, Right/Left Shoulder, Right/Left Stick, Start and Guide.

Example
++++++++++++++++++++++++++++++

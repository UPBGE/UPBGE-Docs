.. _bpy.types.VibrationActuator:

==============================
Vibration Actuator
==============================

.. seealso::
   See the Python reference of this logic brick in :class:`SCA_VibrationActuator`.

The *Vibration Actuator* allows the user to control the joystick vibration during the game.

.. figure:: /images/logic_bricks/actuators/logic-actuators-types-vibration-vibration.png

   Vibration Actuator

.. tip::
   The vibration can be updated in every logic tick. This way different vibration effects can be performed (sin, up/down, etc).

Properties
++++++++++++++++++++++++++++++

Joystick Index
   Specifies in which joystick to control the vibration.
Vibration Mode
   Play
      Play the vibration for *Duration* time.
   Stop
      Stop the vibration.
Strength Low Freq
   Vibration strength for the low frequency motor (usually at gamepad left).
Strength High Freq
   Vibration strength for the high frequency motor (usually at gamepad right).
Duration
   Duration (in milliseconds) of the vibration.

Example
++++++++++++++++++++++++++++++

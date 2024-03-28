.. _bpy.types.ObjectActuator:

.. _actuator-motion:

==============================
Motion Actuator
==============================

.. seealso::
   See the Python reference of this logic brick in :class:`SCA_ObjectActuator`.

The *Motion Actuator* sets an object into motion. There are three modes of operation, Simple, Servo and Character, in which the object can either teleport and rotate, or dynamically move.

.. figure:: /images/logic_bricks/actuators/logic-actuators-types-motion-motion.png

   Motion Actuator

Properties
++++++++++++++++++++++++++++++

Motion Type
   Determines the type of motion:

   Simple Motion
      Applies a change in location and/or rotation directly.
   Servo Control
      Sets a target speed, and also how quickly it reaches that speed.
   Character Motion
      Sets the speed and direction the character is traveling. This should be used instead of *Simple Motion* to properly move a character.

      .. note::
         This actuator will only work if the object physics type is set to Character.

Simple Motion
++++++++++++++++++++++++++++++

*Simple Motion* gives control over position and velocity, but does this as an instant displacement; the object never passes any of the coordinates between the start and end positions. This can interfere with the physical simulation of other objects, and can cause an object to go through another object. The `Servo Control`_ actuator does not suffer from this, since it produces physically correct velocities, and leaves updating the position to the physics simulation.

.. figure:: /images/logic_bricks/actuators/logic-actuators-types-motion-simple.png

   Motion actuator for Simple Motion

Loc
   The object jumps the number of Blender units entered, each time a pulse is received.
Rot
   The object rotates by the specified amount, each time a pulse is received.
L
   Coordinates specified are Global (deactivated) or Local (actived).

.. figure:: /images/logic_bricks/actuators/logic-actuators-types-motion-simple1.png

   Simple Motion for a dynamic object

Servo Control
++++++++++++++++++++++++++++++

The Servo Control actuator influences the velocity of a game object by applying forces, resulting in correct behavior when colliding with other objects controlled by the physics simulation. The amount of force necessary is determined by a `PID controller <https://en.wikipedia.org/wiki/PID_controller>`__, a type of controller that is often used in control systems. This actuator controls position or rotation only indirectly.

Controlling the position is not necessary in that respect; that is left to a player moving the object via direction-type controls (such as the WASD keys in a first person shooter). In such a scenario, each direction-key sensor should be attached to a different Servo Control actuator setting a different target velocity.

.. tip::
   To use the Servo Control actuator, it is necessary to set the object's Physics Type to "Dynamic" or "Rigid Body", and to mark the object as "Actor" in the same panel. This actuator does not work with the Character physics type.

.. figure:: /images/logic_bricks/actuators/logic-actuators-types-motion-servo.png

   Motion actuator for Servo Control

Reference Object
   Specifies the object which the actuator uses as a reference for the velocity. When set, it will use a velocity relative to that object instead of absolute (i.e. world-relative) velocity. Use this for a player object standing on a moving platform.

Servo Type
   Linear Velocity
      The target linear velocity for the object.
   Angular Velocity
      The target angular velocity for the object.
L
   Determines whether the Linear Velocity specified are in Local (button depressed) or Global (button released) coordinates.
X, Y, Z force limits
   Sets minimum and maximum limits for the force applied to the object. If disabled (i.e. X, Y or Z buttons are depressed) the force applied is unlimited.

The following three coefficients determine the response to the *velocity error*, which is the difference between the target velocity and the object's actual velocity.

Proportional Coefficient
   This controls the reaction proportional to the velocity error. Small values cause smooth (but possibly too slow) changes in velocity. Higher values cause rapid changes, but may cause overshooting.
Integral Coefficient
   This controls the reaction to the sum of errors so far. Using only the Proportional component results in a systematic velocity error if there is friction: some velocity delta is necessary to produce the force that compensates the friction. Using the Integral component suppresses this effect (the target velocity is achieved on average) but can create oscillations; the control will speed to compensate the initial velocity error. To avoid the oscillation, the Proportional component must be used with the Integral component (the Proportional component damps the control) This is why the GUI sets the Proportional Coefficient systematically when you change the Integral Coefficient.
Derivative Coefficient
   Set the Derivative Coefficient. This dampens the acceleration when the target velocity is almost reached.

Character Motion
++++++++++++++++++++++++++++++

.. figure:: /images/logic_bricks/actuators/logic-actuators-types-motion-character.png

   Motion actuator for Character Motion

Loc
   The character moves the number of Blender units entered, each time a pulse is received.
Rot
   The character rotates by the specified amount, each time a pulse is received.
L
   Coordinates specified are Global (deactivated) or Local (actived).
Add
   The movement is incorporated to the movement performed by others character motion actuators doing the movement more fluid.
Jump
   Make the character jump using the settings in the physics properties (Jump Force and Max Jumps).

.. _bpy.types.MouseActuator:

**************
Mouse Actuator
**************

.. seealso::
   See the Python reference of this logic brick in :class:`SCA_MouseActuator`.

The *Mouse Actuator* allows two modes of operation,
to show/hide the mouse cursor or to control object rotation with the mouse.
The mouse rotation is flexible enough to allow any type of mouse look
as well as banking for flight controls.

Mouse actuator for Mouse Look

.. figure:: /images/Logic/Actuators/logic-actuators-types-mouse-mouse.png

   Mouse Actuator

Properties
==========

Mode
   Determines the mouse mode.

   Visibility
      Allows to show/hide the mouse cursor.
   Look
      Controls the object rotation according to X and/or Y mouse movement.
      Moreover, the object rotation can be constrained using thresholds and capping angles.


Visibility
----------

Mouse actuator for Visibility.

.. figure:: /images/Logic/Actuators/logic-actuators-types-mouse-visibility.png

   Mouse Actuator: Visibility.

Visibility
   Toggles the visibility of the mouse cursor.


Look
----

Mouse actuator for Mouse Look

.. figure:: /images/Logic/Actuators/logic-actuators-types-mouse-look.png

   Mouse Actuator: Look.
   
.. note::

   To make Mouse Look work in a smoother way, it is necessary that the width and
   height screen resolutions, in the render window, are set with even numbers (i.e. 1920x1080).

Use ``X`` axis, ``Y`` axis
    X axis or/and Y axis mouse movement causes the rotation of the object.
Sensitivity
   The necessary amount of rotation caused by mouse movement along the X and Y axis.
Threshold
   Amount of movement from the mouse required before rotation is triggered.
Min
   The minimum angle of rotation caused by mouse movement along the X axis and Y axis in degrees.
Max
   The maximum angle of rotation caused by mouse movement along the X axis and Y axis in degrees.
Object axis ``X``, ``Y``, ``Z``
   The object's 3D axis to rotate with the mouse movement.
Local
   Rotation caused by mouse movement along the X axis and/or Y axis is local.
Reset
   Reset the cursor's X/Y position to the center of the screen space after calculating.


Example
=======

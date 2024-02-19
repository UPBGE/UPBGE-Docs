.. figure:: /images/logic_nodes/input/gamepad/ln-gamepad_vibrate.png
   :align: right
   :width: 215
   :alt: Gamepad Vibrate Node

.. _ln-gamepad_vibrate:

================
Gamepad Vibrate
================

Detects if the controller at given index has any activity.

Inputs
++++++

Condition
   Condition that need be fulfilled to activate the node.

Index
   The controller index to vibrate.

Left
   Force with which to rotate the weight in the left handle.

Right
   Force with which to rotate the weight in the right handle.

Time
   Vibrate for this many seconds.

Outputs
+++++++

Done
   *True* if the node performed successfully, else *False*.

+++++++++++++++
Gamepad Vibration
+++++++++++++++

.. figure:: /images/Logic_Nodes/gamepad_vibration_node.png
   :align: right
   :width: 215
   :alt: Gamepad Vibration.

The *Gamepad Vibration* node detects if the controller at given index has any activity.

Inputs
=======

Index
   The controller index to vibrate.

Left
   Force with which to rotate the weight in the left handle.

Right
   Force with which to rotate the weight in the right handle.

Time
   Vibrate for this many seconds.

Outputs
=======

Done
   *True* if the node performed successfully, else *False*.
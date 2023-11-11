+++++++++++++++
Gamepad Sticks
+++++++++++++++

.. figure:: /images/Logic_Nodes/gamepad_sticks_node.png
   :align: right
   :width: 215
   :alt: Gamepad Sticks.

The Gamepad *Sticks* node detects stick values of the controller at given index.

Parameters
==========

Axis
   Which stick values to read.

Inputs
=======

Invert XY
   Invert the axis values.

Index
   The controller index to monitor.

Sensitivity
   Multiplier for the axis values.

Threshold
   Dead-zone for the stick.


Outputs
=======

Vector
   Stick values as vector `(X, Y, 0)`

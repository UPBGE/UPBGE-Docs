.. figure:: /images/logic_nodes/input/gamepad/ln-gamepad_sticks.png
   :align: right
   :width: 215
   :alt: Gamepad Sticks Node

.. _ln-gamepad_sticks:

==============
Gamepad Sticks
==============

Detects stick values of the controller at given index.

Parameters
++++++++++

Axis
   Which stick values to read.

Inputs
++++++

Invert XY
   Checked axis will be inverted.

Index
   The controller index to monitor.

Sensitivity
   Multiplier for the axis values.

Threshold
   Dead-zone for the stick.

Outputs
+++++++

Vector
   Stick values as vector `(X, Y, 0)`.

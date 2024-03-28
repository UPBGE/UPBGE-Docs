.. figure:: /images/logic_nodes/input/gamepad/ln-gamepad_button.png
   :align: right
   :width: 215
   :alt: Gamepad Button Node

.. _ln-gamepad_button:

==============================
Gamepad Button
==============================

Detects if a specified button has been pressed on the controller at given index.

Parameters
++++++++++++++++++++++++++++++

Button
   Which button/trigger is monitored.

Input Type
   Input detection mode.

Inputs
++++++++++++++++++++++++++++++

Index
   The controller index to monitor.

Outputs
++++++++++++++++++++++++++++++

Pressed
   *True* if the button is active in the selected mode, else *False*.

Strength
   Value of the trigger from 0 to 1. Only visible if button is `LT/L2` or `RT/R2`.

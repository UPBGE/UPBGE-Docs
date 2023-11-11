+++++++++++++++
Gamepad Button
+++++++++++++++

.. figure:: /images/Logic_Nodes/gamepad_button_down_node.png
   :align: right
   :width: 215
   :alt: Gamepad Button.

The Gamepad *Button* node detects if a specified button has been pressed on the controller at given index.

Parameters
==========

Button
   Which button to react to.

Mode
   Input detection mode.

Inputs
=======

Index
   The controller index to monitor.

Outputs
=======

Pressed
   *True* if the button is active in the selected mode, else *False*.

Strength
   Value of the trigger from 0 to 1; Only visible if button is `LT / L2` or `RT / R2`.

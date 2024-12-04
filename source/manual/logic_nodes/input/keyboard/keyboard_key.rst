.. figure:: /images/logic_nodes/input/keyboard/ln-keyboard_key.png
   :align: right
   :width: 215
   :alt: Keyboard Key Node

.. _ln-keyboard_key:

==============================
Keyboard Key
==============================

Detects if a specified key has been pressed.

Parameters
++++++++++++++++++++++++++++++

Input Type
   Input detection mode. ``Tap`` is activated the first frame that the key is pressed, ``Down`` 
   is activated while the key is pressed (even the first frame) and ``Up`` is activated once the last frame the key is pressed.

Inputs
++++++++++++++++++++++++++++++

Key
   The key to monitor; click & press a desired key.

Outputs
++++++++++++++++++++++++++++++

If Pressed
   *True* if the key is active in the selected mode, else *False*.

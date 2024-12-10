.. figure:: /images/logic_nodes/input/keyboard/ln-instream.png
   :align: right
   :width: 215
   :alt: Key Logger Node

.. _ln-instream:

==============================
Key Logger
==============================

Records keyboard activity.

Inputs
++++++++++++++++++++++++++++++

Only Characters
   Boolean value for condition. todo

Outputs
++++++++++++++++++++++++++++++

Pressed
   *True* if the node performed successfully, else *False*.

Character
   Character represented by the key pressed (String). For example ``'a'`` will be returned for key A.

Keycode
   Integer code of the recorded key (Integer).

.. figure:: /images/logic_nodes/values/ln-value_switch.png
   :align: right
   :width: 215
   :alt: Value Switch Node

.. _ln-value_switch:

==============================
Value Switch
==============================

Will switch between two values, if condition is *True*. Used i.e. to switch movement speed of a character, if :kbd:`Shift` key is pressed.

Inputs
++++++++++++++++++++++++++++++

Switch
   If checked, A will be selected, else B value will be selected. Accepts Boolean result from connected node.

A Value
   Fixed value for A field, or a result from connected node. Value type is selected from dropdown menu.

B Value
   Fixed value for B field, or a result from connected node. Value type is selected from dropdown menu.

Outputs
++++++++++++++++++++++++++++++

Result
   Resulting value.

Example
++++++++++++++++++++++++++++++

.. figure:: /images/logic_nodes/values/ln-value_switch-example.png
   :align: center
   :figwidth: 80%
   :alt: Value Switch Node Example

   Will result in A value (0.20) if Shift key is held down

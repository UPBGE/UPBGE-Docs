.. figure:: /images/logic_nodes/events/ln-on_value_changed_to.png
   :align: right
   :width: 215
   :alt: On Value Changed To Node

.. _ln-on_value_changed_to:

===================
On Value Changed To
===================

Stores a value internally, and as soon as the value pulled through the input matches the target value, it activates. Then the new value is stored.

Inputs
++++++

Value
   The connected value is pulled each frame.

Target
   Compare the new value to this value.

Outputs
+++++++

Result
   *True* if the new value matches the target, else *False*.

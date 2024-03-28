.. figure:: /images/logic_nodes/events/ln-on_value_changed.png
   :align: right
   :width: 215
   :alt: On Value Changed Node

.. _ln-on_value_changed:

==============================
On Value Changed
==============================

Stores a value internally, and as soon as a value other than the stored one is pulled through the input, it activates. Then the new value is stored.

Parameters
++++++++++++++++++++++++++++++

Initialize
   todo

Inputs
++++++++++++++++++++++++++++++

Value
   Connected value is pulled each frame.

Outputs
++++++++++++++++++++++++++++++

If Changed
   *True* if the new value is different from the stored one, else *False*.

Old
   The stored value.

New
   The value pulled from the input socket.

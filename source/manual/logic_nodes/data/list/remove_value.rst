.. figure:: /images/logic_nodes/data/list/ln-remove_value.png
   :align: right
   :width: 215
   :alt: Remove Value Node

.. _ln-remove_value:

==============================
Remove Value
==============================

Remove the first iteration of a given value in a list.

Inputs
++++++++++++++++++++++++++++++

Condition
   Condition to be fulfilled for node to activate.

List
   List to remove the value from.

Type
   Which type and value to remove from list.

Outputs
++++++++++++++++++++++++++++++

Done
   *True* if value is removed, else *False*.

List
   Resulting list after value removal.

.. note::
   This node will only remove the first iteration in the list,
   for example if you give the list [1, 4, 104, 1] and the value integer 1,
   the output list will be [4, 104, 1] and not [4, 104] like we can think at first.
.. figure:: /images/logic_nodes/data/list/ln-remove_index.png
   :align: right
   :width: 215
   :alt: Remove Index Node

.. _ln-remove_index:

==============================
Remove Index
==============================

Remove the value at a given index on a list.

Inputs
++++++++++++++++++++++++++++++

Condition
   Condition to be fulfilled for node to be activated.

List
   List to be used.

Index
   Which index to remove from above list.

Outputs
++++++++++++++++++++++++++++++

Done
   *True* if removal of index is successful, else *False*.

List
   Resulting list after removal.

.. note::
   The list index start at 0, so for example, in the list [4, 2, 5, 8, 9], the value at index 2 will be 5.

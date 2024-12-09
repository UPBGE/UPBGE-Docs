.. figure:: /images/logic_nodes/data/list/ln-set_list_index.png
   :align: right
   :width: 215
   :alt: Set List Index Node

.. _ln-set_list_index:

==============================
Set List Index
==============================

Set a value for a given index on a list.

Inputs
++++++++++++++++++++++++++++++

Conditon
   If connected, a condition must be fulfilled for note to activate.

List
   Which list to use.

Index
   Which index to set.

Type
   Which type and value to set for above list.

Outputs
++++++++++++++++++++++++++++++

Done
   *True* if node sets an index successfully, else *False*.

List
   Resulting list after setting the index.

.. note::
   This node cannot be used to add a new value at the end of a list, it will result in
   an out of range error. Instead use the *Append* node to do this.

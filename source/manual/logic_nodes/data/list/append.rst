.. figure:: /images/logic_nodes/data/list/ln-append.png
   :align: right
   :width: 215
   :alt: Append Node

.. _ln-append:

==============================
Append
==============================

Append a value in the end of a given list.

Inputs
++++++++++++++++++++++++++++++

Condition
   Condition to be fulfilled for node to activate.

List
   Which list to append to.

Type
   Type and the value to append.

Outputs
++++++++++++++++++++++++++++++

Done
   *True* if node performs successfully, else *False*.

List
   The given list with the new value attached at the end.

.. note::
   Square socket indicates a list.

.. note::
   If you give the list [1, 2, 3, 4] and the Integer 5, the output will be the list [1, 2, 3, 4, 5]
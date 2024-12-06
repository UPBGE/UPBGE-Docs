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
   Resulting list.

.. note::
   Square socket indicates a list.

.. note::
   If you give the list [1, 2, 3, 4] and in *Type* Integer 5, the output will be the list [1, 2, 3, 4, 5]
   TODO: Add an image to show the node setup of the example 
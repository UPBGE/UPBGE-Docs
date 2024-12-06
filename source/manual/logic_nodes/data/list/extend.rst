.. figure:: /images/logic_nodes/data/list/ln-extend.png
   :align: right
   :width: 215
   :alt: Extend Node

.. _ln-extend:

==============================
Extend
==============================

Extend (concatenate) one list with another.

Inputs
++++++++++++++++++++++++++++++

List 1
   List to be extended. This list will be placed first in the output list.

List 2
   List to use for extending. This list will be placed just after *List 1* in the output list.

Outputs
++++++++++++++++++++++++++++++

List
   A new list made by concatenating *List 1* and *List 2*.

.. note::
   If you give *List 1* [1, 2, 3, 4] and *List 2* [5, 6, 7, 8, 9, 10], the output will be the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
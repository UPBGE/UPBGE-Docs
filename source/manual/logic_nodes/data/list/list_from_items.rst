.. figure:: /images/logic_nodes/data/list/ln-list_from_items.png
   :align: right
   :width: 215
   :alt: List From Items Node

.. _ln-list_from_items:

==============================
List From Items
==============================

Create a new list with the given items.

Parameters
++++++++++++++++++++++++++++++

Add Socket
   Add another socket for additional items inputs.

Inputs
++++++++++++++++++++++++++++++

Item
   Item to add to list. Each press of *Add Socket* will add another *Item* input.
   Items will be add to the list from top (index 0) to bottom (index list length-1).

Outputs
++++++++++++++++++++++++++++++

List
   New list with the added items.

.. note::
   Leaving an *Item* input blank will result in a Null item in your list.
   TODO: Add an example with mutiple blank item inputs.
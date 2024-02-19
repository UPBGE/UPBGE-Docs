.. figure:: /images/logic_nodes/events/ln-on_update.png
   :align: right
   :width: 215
   :alt: On Update Node

.. _ln-on_update:

===========
On Update
===========

Activates each frame. It is used to continuously do something. It is node equivalent to the :doc:`/manual/logic/sensors/types/always`.

Outputs
+++++++

Out
   *True* on each frame.

.. note::

   *On Update* can be expensive depending on the logic attached to it, and should only be used if necessary.

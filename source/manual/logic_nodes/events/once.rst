.. _ln-once:

.. figure:: /images/logic_nodes/events/ln-once.png
   :align: right
   :width: 215
   :alt: Once Node

==========
Once
==========

Restricts a continuous *True* condition to only the first frame.

Inputs
+++++++

Condition
   Input condition.

Repeat
   Allow another activation after the input condition is reset to *False*.

Outputs
+++++++

Out
   *True* for the first frame of a *True* input condition, else *False*.

Example
+++++++

.. figure:: /images/logic_nodes/events/ln-once-example.png
   :align: center
   :width: 500
   :alt: Once Node Example
 
   Once Node Example

:doc:`./on_update` linked to *Once* node would be equal to :doc:`./on_init`.

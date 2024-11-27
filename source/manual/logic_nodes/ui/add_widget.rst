.. figure:: /images/logic_nodes/ui/ln-add_widget.png
   :align: right
   :width: 215
   :alt: Add Widget Node

.. _ln-add_widget:

==============================
Add Widget
==============================

Add one widget to another. Child widgets will inherit positioning
and rotation from their parent and can be placed locally. They will
also only be visible if their parent is also visible.

Inputs
++++++++++++++++++++++++++++++

Condition
   If connected, condition must be fulfilled for node to activate.

Parent
   Parent to which to add the widget.

Widget
   Widget to add to the parent.

Outputs
++++++++++++++++++++++++++++++

Done
   *True* if node performed successfully, else *False*.

.. figure:: /images/logic_nodes/events/ln-receive_event.png
   :align: right
   :width: 215
   :alt: Receive Event Node

.. _ln-receive_event:

=============================
Receive Event
=============================

Reacts to events sent via the :doc:`./send_event` node or the *Uplogic* module. An event can store some data, which can be extracted using this node.

Inputs
++++++

Subject
   The ID of the event.

Outputs
+++++++

Received
   *True* if an event has been found, else *False*.

Content
   Content of this event, can be anything.

Messenger
   Messenger of this event, expected to be a ``KX_GameObject``.

.. important::

   If multiple events have the same ID (subject), older events are overwritten.

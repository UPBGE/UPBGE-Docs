.. figure:: /images/logic_nodes/events/ln-send_event.png
   :align: right
   :width: 215
   :alt: Send Event Node

.. _ln-send_event:

==============================
Send Event
==============================

Creates an event that can be reacted to, using the :doc:`./receive_event` node or the *Uplogic* module. An event can store *Content*, and a *Messenger* can be assigned.

Properties
++++++++++++++++++++++++++++++

Advanced
   Enables access to the *Content* and *Messenger* sockets.

Inputs
++++++++++++++++++++++++++++++

Condition
   If *True*, the event is created.

Subject
   The ID of the Event.

Content
   Content of this event. Can be anything. Visible only if *Advanced* is selected.

Messenger
   Messenger attached to this event, expected to be ``KX_GameObject``. Visible only if *Advanced* is selected.

Outputs
++++++++++++++++++++++++++++++

Done
   *True* if the node performed successfully, else *False*.

.. important::
   Events are only created for the next frame. After that, they are erased. If multiple events have the same ID (subject), older events are overwritten.

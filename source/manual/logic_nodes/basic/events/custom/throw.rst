+++++++++++++++
Send
+++++++++++++++

.. figure:: /images/Logic_Nodes/send_node.png
   :align: right
   :width: 215
   :alt: Send Node.

The *Send* node creates an event that can be reacted to using the :doc:`./catch` node or
the *uplogic* module. An Event can store *Content* and a *Messenger* can be assigned.

.. note::

   Events are only created for the next frame. After that, they get erased.
   
   If multiple events have the same ID (subject), older events get overwritten.


Inputs
======

Condition
   If *True*, the event is created.

Subject
   The ID of the Event.

Content
   Content of this event. Can be anything.

Messenger
   Messenger attached to this event, expected to be *KX_GameObject*


Properties
==========

Advanced
   Allows access to the *Content* and *Messenger* sockets.


Outputs
=======

Done
   *True* if the node performed successfully, else *False*

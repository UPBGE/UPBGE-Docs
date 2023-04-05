
+++++++++++++++
Receive
+++++++++++++++

.. figure:: /images/Logic_Nodes/receive_node.png
   :align: right
   :alt: Receive Node.

The *Receive* node reacts to events thrown via the *Send* node or the *uplogic* module.
An Event can store some data, which can be extracted using this node.

.. note::

   If multiple events have the same ID (subject), older events get overwritten.


Inputs
======

Subject
   The ID of the Event.

Outputs
=======

Received
   *True* if an event has been found, else *False*

Content
   Content of this event, can be anything.

Messenger
   Messenger of this event, expected to be a `KX_GameObject`

.. figure:: /images/logic_nodes/sound/fmod/ln-start_event.png
   :align: right
   :width: 215
   :alt: Start Event Node

.. _ln-start_event:

==============================
Start Event
==============================

Start an event by name.

Parameters
++++++++++++++++++++++++++++++

Speaker Mode
   If active, an object reference will be used for the position and orientation of this sound.

Inputs
++++++++++++++++++++++++++++++

Condition
   If connected, condition must be fulfilled for node to activate.

Event
   Name of the event. Event names are defined within the FMod application.

Position
   World position of this event.

Speaker
   Reference object for position and orientation.

Channel
   Channel for grouping events together.

Outputs
++++++++++++++++++++++++++++++

Done
   *True* if node performed successfully, else *False*.

Event
   The `Event` or `EventSpeaker` python object.

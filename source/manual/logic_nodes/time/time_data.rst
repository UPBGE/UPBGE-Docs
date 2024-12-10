.. figure:: /images/logic_nodes/time/ln-time_data.png
   :align: right
   :width: 215
   :alt: Time Data Node

.. _ln-time_data:

==============================
Time Data
==============================

Return useful data about the time within your game.

Outputs
++++++++++++++++++++++++++++++

Time
   The number of seconds elapsed since the game engine was launched (Float).

   .. note::
      The value returned here is independent of a scene change (time will continue to be counted without resetting the count),
      but it will be reset after loading a .blend file because it relaunches the game engine.

Delta (Frametime)
   The number of seconds elapsed between the last two frames (Float). Used for calculations requiring absolute temporal precision,
   such as progressive transitions, interpolations or mechanics requiring fine temporal management. For example,
   if you want to animate an object that has to move exactly 10 units over 5 seconds.

FPS
   *Frames Per Second* of the running game (Float).

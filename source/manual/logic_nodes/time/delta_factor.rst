.. figure:: /images/logic_nodes/time/ln-delta_factor.png
   :align: right
   :width: 215
   :alt: Delta Factor Node

.. _ln-delta_factor:

==============================
Delta Factor
==============================

Return the delta factor, a normalized multiplier based on the ratio between the actual number of FPS and 
the target number of FPS (the number of FPS the logic is runnig at).

Outputs
++++++++++++++++++++++++++++++

Factor
   *Delta Factor* between the actual number of FPS and the number of FPS used by the logic (Float). Used to dissociate logic and framerate,
   to maintain the same speed for actions managed by logic even with an unlimited number of FPS. For example, used to calculate
   the walk speed of a character.

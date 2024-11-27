.. figure:: /images/logic_nodes/time/ln-barrier.png
   :align: right
   :width: 215
   :alt: Barrier Node

.. _ln-barrier:

==============================
Barrier
==============================

Only activate if the condition is true for the given amount of time.
Example: If the condition is "Press A" and the Time socket is set to "1.0",
A has to be pressed for 1 second for the output socket to return `True`.

Inputs
++++++++++++++++++++++++++++++

Condition
   If connected, condition must be fulfilled for node to activate.

Time
   Output socket will return `True` if input condition has been true for this amount of seconds.

Outputs
++++++++++++++++++++++++++++++

Out
   `True` if input condition has been `True` for "Time" seconds, else `False`.

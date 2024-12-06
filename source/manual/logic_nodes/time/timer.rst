.. figure:: /images/logic_nodes/time/ln-timer.png
   :align: right
   :width: 215
   :alt: Timer Node

.. _ln-timer:

==============================
Timer
==============================

Wait a certain time between the reception of *True* and the output of *True*.

Inputs
++++++++++++++++++++++++++++++

Set Timer
   Condition required for timer to be set.

Seconds
   Seconds needed to pass until timer activates.

Outputs
++++++++++++++++++++++++++++++

When Elapsed
   Condition/node to execute when timer has elapsed.

.. note::
   *Timer* node is tied to the CPU clock, not to game FPS.

.. important::
   *Timer* will only handle one input at a time and will not stack them, unlike the *Delay* node.
   For example, if you connect a *Keyboard key* node to a *Timer* set to 5 seconds
   and press the key a first time and then 2 seconds later you press the key again, *Timer* will only
   output *True* 5 seconds after the first key press and not another one time *True* at 7 seconds,
   unlike *Delay*.
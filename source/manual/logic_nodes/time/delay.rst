.. figure:: /images/logic_nodes/time/ln-delay.png
   :align: right
   :width: 215
   :alt: Delay Node

.. _ln-delay:

==============================
Delay
==============================

Wait a certain time between the reception of *True* and the output of *True*.

Inputs
++++++++++++++++++++++++++++++

Condition
   If connected, condition must be fulfilled for node to activate.

Delay
   *Delay* in seconds until the node set it output to *True*.

Outputs
++++++++++++++++++++++++++++++

Out
   *True* one frame after the condition input has been fulfilled and the *Delay* has elapsed, else *False*.

.. important::
   *Delay* will handle muliple inputs at the same time and will stack them, unlike the *Timer* node.
   For example, if you connect a *Keyboard key* node to a *Delay* set to 5 seconds
   and press the key a first time and then 2 seconds later you press the key again, *Delay* will
   output *True* 5 seconds after the first key press and another one time *True* at 7 seconds,
   unlike *Timer*.
.. figure:: /images/logic_nodes/nodes/materials/ln-play_sequence.png
   :align: right
   :width: 215
   :alt: Play Sequence Node

.. _ln-mat-play_sequence:

==============================
Play Sequence
==============================

Inputs
++++++++++++++++++++++++++++++

Condition
   If connected, condition must be fulfilled for node to activate.

Material
   Which sprite/material to use.

Node Name
   todo

Outputs
++++++++++++++++++++++++++++++

On Start
   Emits *True* signal that sequence started playing.

Running
   *True* when sequence is playing.

On Finish
   Emits *True* signal when sequence stops.

Current Frame
   Integer value of current sequence frame.

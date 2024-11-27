.. figure:: /images/logic_nodes/scene/post_fx/ln-add_filter.png
   :align: right
   :width: 215
   :alt: Add Filter Node

.. _ln-add_filter:

==============================
Add Filter
==============================

This node will add a new GL filter, modifying the render output.

Available filters are:
- FXAA
- HBAO
- SSAO
- Vignette
- Brightness
- Chromatic Abberation
- Grayscale
- Levels
- Mist
- Blur

Parameters
++++++++++++++++++++++++++++++

Filter
   Filter type to add.

Inputs
++++++++++++++++++++++++++++++

Condition
   If connected, condition must be fulfilled for node to activate.

Pass Index
   Higher indices will affect the rendered image by lower indices.

Power
   Strength of the effect.

Color
   Color of the added filter (if applicable).

Brightness
   Brightness of the selected filter (if applicable).

Start
   Starting distance of the mist. For *Mist* filter only.

Density
   Density of the mist. For *Mist* filter only.

Outputs
++++++++++++++++++++++++++++++

Done 
   *True* if the node performed successfully, else *False*.

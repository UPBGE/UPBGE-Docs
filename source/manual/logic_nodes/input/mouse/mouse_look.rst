.. figure:: /images/logic_nodes/input/mouse/ln-mouse_look.png
   :align: right
   :width: 215
   :alt: Mouse Look Node

.. _ln-mouse_look:

==============================
Mouse Look
==============================

A quick way to make objects follow the mouse movement. It's possible to assign a *Body* and a *Head* object.

If no *Head* object is assigned, the body will be used for both axis, but that is generally discouraged as it can lead to unwanted side effects.

Parameters
++++++++++++++++++++++++++++++

Front
   Look direction of the *Head* Object. If set to Y, the rotational axis will be X and vice versa.

Center Mouse
   todo

Inputs
++++++++++++++++++++++++++++++

Condition
   If connected, condition must be fulfilled for node to activate.

Body
   The body object.

Head (Optional)
   The head object. If set, both objects will be rotated along their corresponding local axis.

Invert XY
   Option to invert movement for each axis (Vector2).

Sensitivity
   Multiplier for translating mouse movement to object rotation.

Cap Left/Right
   Limit the body objects rotation on its local Z axis.

X Limits
   The limits for the body objects local Z rotation (Vector2). Only shown if Cap Left/Right is selected.

Cap Up/Down
   Limit the head object's rotation on its local X/Y axis.

Y Limits
   The limits for the head object's local X/Y rotaion (Vectpr2). Only shown if Cap Up/Down is selected.

Smoothing
   Use linear interpolation to slowly adapt the object transformation to mouse movement.

Outputs
++++++++++++++++++++++++++++++

Done
   *True* if the node performed successfully, else *False*.

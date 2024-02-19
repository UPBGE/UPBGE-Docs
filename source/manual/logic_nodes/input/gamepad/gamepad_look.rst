.. figure:: /images/logic_nodes/input/gamepad/ln-gamepad_look.png
   :align: right
   :width: 215
   :alt: Gamepad Look Node

.. _ln-gamepad_look:

==============
Gamepad Look
==============

A quick way to make objects follow controller stick movement. It's possible to assign a *Body* and a *Head* object.

If no *Head* object is assigned, the *Body* will be used for both axis, but that is generally discouraged as it can lead to unwanted side effects.

Parameters
++++++++++

Axis
   Which stick of the controller to use for the transformation.

Inputs
++++++

Condition
   Input condition for node activaton.

Main Object
   The body object.

Head Object (Optional)
   Head object. If set, both objects will be rotated along their corresponding local axis.

Invert XY
   Option to invert movement for each axis (Vector2).

Index
   The index of the controller to poll.

Sensitivity
   Multiplier for translating mouse movement to object rotation.

Exponent
   Exponent for fine-tuning the stick behavior.

Cap Left/Right
   Limit the body objects rotation on its local Z axis.

X Limits
   The limits for the body object local Z rotation (Vec2). Visible if Cap Left/Right is selected.

Cap Up/Down
   Limit the head object rotation on its local X/Y axis.

Y Limits
   Limits for the head object's local X/Y rotaion (Vec2). Visible if Cap Up/Down is selected.

Threshold
   Ignore stick values under this threshold.

Outputs
+++++++

Done
   *True* if the node performed successfully, else *False*.

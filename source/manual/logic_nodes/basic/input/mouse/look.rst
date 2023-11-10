+++++++++++++++
Mouse Look
+++++++++++++++

.. figure:: /images/Logic_Nodes/mouse_look_node.png
   :align: right
   :width: 215
   :alt: Mouse Look Node.

The *Mouse Look* node is a quick way to make objects follow the mouse movement.
It's possible to assign a *Body* and a *Head* object.

If no *Head* object is assigned, the body will be used for both axis, but
that is generally discouraged as it can lead to unwanted side effects.

Inputs
=======

Condition
   Input Condition.

Main Object
   This is the body object

Head (Optional)
   This is the head object. If set, both objects will be rotated along their corresponding local axis.

Invert
   Option to invert movement for each axis (Vec2).

Sensitivity
   Multiplier for translating mouse movement to object rotation.

Cap Left/Right
   Limit the body objects rotation on its local Z axis.

X Limits
   The limits for the body objects local Z rotaion (Vec2).

Cap Up/Down
   Limit the head object's rotation on its local X/Y axis.

Y Limits
   The limits for the head object's local X/Y rotaion (Vec2).

Smoothing
   Use linear interpolation to slowly adapt the object transformation to mouse movement.

Parameters
==========

Front
   The look direction of the Head Object. If set to Y, the rotational axis will be X and vice versa.

Outputs
=======

Done
   *True* if the node performed successfully, else *False*

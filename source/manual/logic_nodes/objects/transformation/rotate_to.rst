.. figure:: /images/logic_nodes/objects/transformation/ln-rotate_to.png
   :align: right
   :width: 215
   :alt: Rotate To Node

.. _ln-rotate_to:

==============================
Rotate To
==============================

Rotates selected object to a specific angle, instantaneous or with speed. Applies rotation only on a single axis and fixed angulation in the world.

See also :ref:`Apply Rotation <ln-apply_rotation>`.

Input
++++++++++++++++++++++++++++++

Condition
   Condition for this node to start.

Object
   Object that will be rotated.

Target
   Object's rotation defined in degrees.

Factor
   Speed to complete the move. Every time the node is activated, the displacement made will be smaller.
 
Rot Axis
   The axis of the object that will be used to rotate it during node execution.

Front
   Which axis is the front of the object.

Output
++++++++++++++++++++++++++++++

Done 
   *True* if the node performed successfully, else *False*.

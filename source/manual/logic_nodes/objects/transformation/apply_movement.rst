.. figure:: /images/logic_nodes/objects/transformation/ln-apply_movement.png
   :align: right
   :width: 215
   :alt: Apply Movement Node

.. _ln-apply_movement:

==============
Apply Movement
==============

Moves the object a certain vector-defined distance. Does not apply acceleration.

The object is still subject to other forces while the motion is being applied, such as acceleration due to the force of gravity.

The node can be applied to some types of physical properties, i.e. :doc:`Game Physics </manual/editors/properties/physics>`.

Parameters
++++++++++

Mode
   Selected mode of operation.

Input
+++++

Local
   If checked, local coordinates will be used.

Condition
    The condition for this node to start.

Object
    Object that will be moved.

Vector
    The amount of displacement that will be applied to the object.

Output
++++++

Done 
    *True* if the node performed successfully else *False*.

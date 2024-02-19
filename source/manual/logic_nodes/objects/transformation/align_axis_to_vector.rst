.. figure:: /images/logic_nodes/objects/transformation/ln-align_axis_to_vector.png
   :align: right
   :width: 215
   :alt: Align Axis to Vector Node

.. _ln-align_axis_to_vector:

====================
Align Axis to Vector
====================

Input
+++++

Local
   Direction of the object will be the same direction that the vector has, in relation to the *World Origin*.
    
   If vector is in a certain position relative to *World Origin*, object will receive the same angulation in this relation: *World Origin* to *Object*.

Condition
   The condition for this node to start.

Object
   Object that will be aligned.

Vector
   Location within three-dimensional space where the object will be aligned.

Axis
   The axis that will be given as *front* of the object.

Factor
   Each time this node is activated (through *Condition*), the object will rotate to its destination by a certain amount. It can be completed in just one activation (Factor: 1.00) or up to 100 activations (Factor: 0.01). Any other value can be written between 0 and 1.

Output
++++++

Done 
    *True* if the node performed successfully, else *False*.

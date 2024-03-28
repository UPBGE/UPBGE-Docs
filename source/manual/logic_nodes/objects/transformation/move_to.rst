.. figure:: /images/logic_nodes/objects/transformation/ln-move_to.png
   :align: right
   :width: 215
   :alt: Move To Node

.. _ln-move_to:

==============================
Move To
==============================

Moves a selected object to a specific location in the scene.

Input
++++++++++++++++++++++++++++++

Condition
   The condition for this node to start.

Object
   Object that will be moved.

Target Location
   Final destination of the object.
    
Move as Dynamic
   Dynamic objects give and receive collisions, so other objects can dynamically affect the trajectory of the *Moving Object*.
  
Speed
   Amount of displacement that will be applied to the object on each *Condition* activation.

Stop At Distance
  A distance that the object needs to be close to the *Target Location*, to complete the move.

Output
++++++++++++++++++++++++++++++

Done
   *True* if the node performed successfully, else *False*.

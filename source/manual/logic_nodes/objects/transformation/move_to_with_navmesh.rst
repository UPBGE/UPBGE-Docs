.. figure:: /images/logic_nodes/objects/transformation/ln-move_to_with_navmesh.png
   :align: right
   :width: 215
   :alt: Move To with Navmesh Node

.. _ln-move_to_with_navmesh:

======================
Move To with Navmesh
======================

Moves an object in a space delimited by :ref:`Navigation Mesh <physics_navigation_mesh>`.

*Navigation Mesh* is an object that's invisible in-game - it defines where AI can walk and what's off-limit.

To define an object as a *Navigation Mesh*, go to the *Physics properties* area of the object and select in *Game Physics* the object as being *Navigation Mesh*.

Input
+++++

Condition
   The condition for this node to start.

Moving Object
   Object that will be moved.

Rotating Object
   Object that will rotate when the direction changes.
    
Navmesh Object
   Object that will limit the movement area.

Destination
   Final destination of the object. It can be a value using coordinates or location of another object.

Move as Dynamic
   Dynamic objects give and receive collisions, so other objects can dynamically affect the trajectory of the *Moving Object*.

Lin Speed
   Linear speed of the object, basically the travelling speed.

Reach Threshold
   Distance to the target it needs to count as *arrived*.

Look At
   If selected, the front of the object will observe the direction of displacement.

Rot Axis
   When the object makes a change of direction, which axis will rotate.

Front
   Which axis is the front of the object.

Rot Speed
   Speed at which the object will move sideways when making a change of direction.

Visualize
   View the displacement path with a red line during gameplay.

Output
++++++

Done
   *True* if the node performed successfully, else *False*.

When Reached
   todo

Next Point
   todo

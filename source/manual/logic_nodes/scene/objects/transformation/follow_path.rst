*************
Follow Path
*************

Description
===========

This node doesn't seem to be able to run fully in certain situations

Select an object to move through the points of a Nurbs Curve

This node only works in conjunction with "Get Curve Points"

It's very useful to use on NPCs who need to walk around


Input
=====

Condition
   The condition for this node start

Moving Object
   Object that will be moved

Rotating Object
   Object that will rotate when changing direction

Path Points
   It is necessary to use the "Get Curve Points" node
.. A series of Empty Objects parented. 
   The **Parent Object** does not define the position of the object.
   The **Child Objects** mark which positions the object will pass during displacement
   The order that the object will follow is according to the alphabetical and numerical order of the **Child Objects**.

Loop
   If selected: after arriving at the position of the last point, the object will return to the start of the displacement
    
   Unselected: The object will end the displacement at the last Curve's point.

Optional Navmesh
   If there is a boundary in the area where the object travels, select the `Navigation Mesh <https://upbge.org/manual/manual/logic_nodes/category_2/objects/transformation/move_to_with_navmesh.html>`_
    
Move as Dynamic
   Dynamic objects give and receive collisions, so other objects can dynamically affect the trajectory of the "Moving Object".
    
   See `Dynamic <https://docs.blender.org/manual/en/2.79/game_engine/physics/types/dynamic.html>`_ to more

Lin Speed
   The linear speed of the object, basically the travelling speed

Reach Threshold
   The distance to the target it needs to count as "arrived"

Look At
   If selected, the front of the object will observe the direction of displacement.

Root Speed
   The speed at which the object will move sideways when making a change of direction

Rot Axis
   When the object makes a change of direction, which axis will rotate

Front
   Which axis is the front of the object

Output
======

**Done** 
   **True** if the node performed successfully.

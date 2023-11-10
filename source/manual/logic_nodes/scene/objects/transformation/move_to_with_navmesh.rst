********************
Move To with Navmesh
********************

Description
===========

Used to move an object in a space delimited by a **Navigation Mesh** 

**Navigation Mesh** is an object that's invisible in-game that just defines where your AI can walk and what's off-limit

To define an object as a **Navigation Mesh**, you must go to the **Physics properties** area of your object and select in **Game Physics** the object as being **Navigation Mesh**


Input
=====

Condition
    The condition for this node start

Moving Object
    Object that will be moved

Rotating Object
    Object that will rotate when the direction changes
    
Navmesh Object
    Object that will delimit the movement area

Destination
    Final destination of the object. It can be a value using coordinates or location of another object.

Move as Dynamic
    Dynamic objects give and receive collisions, so other objects can dynamically affect the trajectory of the "Moving Object".
    
    See `Dynamic <https://docs.blender.org/manual/en/2.79/game_engine/physics/types/dynamic.html>`_ to more

Lin Speed
    The linear speed of the object, basically the travelling speed

Reach Threshold
     The distance to the target it needs to count as "arrived"

Look At
    If selected, the front of the object will observe the direction of displacement.

Rot Axis
    When the object makes a change of direction, which axis will rotate

Front
    Which axis is the front of the object

Rot Speed
    The speed at which the object will move sideways when making a change of direction

Visualize
    View the displacement path with a red line during gameplay

Output
======

Done
    **True** if the node performed successfully.


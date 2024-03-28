.. figure:: /images/logic_nodes/objects/transformation/ln-follow_path.png
   :align: right
   :width: 215
   :alt: Follow Path Node

.. _ln-follow_path:

==============================
Follow Path
==============================

Select an object to move through the points of a Nurbs Curve. Only works in conjunction with :ref:`Get Curve Points <ln-get_curve_points>`. Use on `NPCs <https://en.wikipedia.org/wiki/Non-player_character>`_ that need to walk around.

Input
++++++++++++++++++++++++++++++

Condition
   The condition for this node to start.

Moving Object
   Object that will be moved.

Rotating Object
   Object that will rotate when changing direction.

Path Points
   Use in combination with *Get Curve Points* node.
   
..
   A series of Empty Objects parented. 
   The **Parent Object** does not define the position of the object.
   The **Child Objects** mark which positions the object will pass during displacement
   The order that the object will follow is according to the alphabetical and numerical order of the **Child Objects**.

Loop
   Selected: after arriving at the position of the last curve point, the object will return to the start of the displacement.
    
   Unselected: The object will end the displacement at the last curve point.

Continue
   todo

Optional Navmesh
   If there is a boundary in the area where the object travels, select the :ref:`Navigation Mesh <ln-move_to_with_navmesh>`.
    
Move as Dynamic
   Dynamic objects give and receive collisions, so other objects can dynamically affect the trajectory of the *Moving Object*. See :ref:`Dynamic <game-engine-physics-dynamic>` for more info.

Lin Speed
   Linear speed of the object, basically the travelling speed.

Reach Threshold
   Distance to the target it needs to count as *arrived*.

Look At
   If selected, the front of the object will observe the direction of displacement.

Rot Speed
   Speed at which the object will move sideways when making a change of direction.

Rot Axis
   When the object makes a change of direction, on which axis will rotate.

Front
   Which axis is the front of the object.

Output
++++++++++++++++++++++++++++++

Done 
   *True* if the node performed successfully, else *False*.

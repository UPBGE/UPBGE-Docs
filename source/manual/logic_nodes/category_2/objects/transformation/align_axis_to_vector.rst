********************
Align Axis to Vector
********************

Description
===========

Aligns any of the 3 axes of an object's Cartesian plane to its positive or negative values ​​(+X, +Y, +Z, -X, -Y, -Z) to some vector.

Vector is a 3D vector is a line segment in three-dimensional space running from point A (tail) to point B (head)

.. figure:: /images/Logic_Nodes/logic-nodes-category-2-objects-transformation-align-axis-to-vector.png

   Align Axis to Vector node.

Input
=====

Global
    The **Object** will align with the **Vector** no matter where any of them are.
    
Local
    The direction of the **Object** will be the same direction that the **Vector** has in relation to the **World Origin**.
    
    If your **Vector** is in a certain position relative to **World Origin**, your object will receive the same angulation in this relation: **World Origin** to **Object**

Condition
    The condition for this node start

Object
    Object that will be aligned

Vector
    Location within three-dimensional space where the object will be aligned

Axis
    The axis that will be given as "front" of the object

Factor
    Each time this node is activated ("condition"), the "Object" will rotate to its destination by a certain amount.
    It can be completed in just one activation (Factor: 1.00) or up to 100 activations (Factor: 0.01). Any other value can be written between 0 and 1

Output
======

**Done** 
    **True** if the node performed successfully.

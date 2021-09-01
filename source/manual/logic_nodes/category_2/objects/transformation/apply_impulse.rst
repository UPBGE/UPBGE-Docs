*************
Apply Impulse
*************

Description
===========

It doesn't seem to be working properly - 01/09/2021

Applies a displacement force that has an origin(Point) and a direction(direction).

For this node to function properly, the object must have some physical property that enables displacement.

`Game Physics <https://upbge.org/manual/manual/editors/properties/physics.html>`_ > 
`Physics Type <https://upbge.org/manual/manual/editors/properties/physics.html#id1>`_: 
`Dynamic <https://upbge.org/manual/manual/editors/properties/physics_dynamic.html>`_, 
`Rigid Body <https://upbge.org/manual/manual/editors/properties/physics_rigid_body.html>`_, 
`Soft Body <https://upbge.org/manual/manual/editors/properties/physics_soft_body.html>`_.


This node applies force at a specific point. In contrast, the **Apply Force** node applies force in entire object.

Input
=====

Global
    

Local
    

Condition
    The condition for this node start

Object
    Object that will be pushed away

Point
    
    
Direction

Output
======

**Done** 
    **True** if the node performed successfully.

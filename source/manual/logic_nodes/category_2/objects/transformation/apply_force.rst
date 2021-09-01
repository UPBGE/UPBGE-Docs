***********
Apply Force
***********

Description
===========

Applies an offset force to an object on any axis of the Cartesian plane. The direction of force can be applied following the axis of the object(Local) or the axis of the world(Global).

For this node to function properly, the object must have some physical property that enables displacement.

`Game Physics <https://upbge.org/manual/manual/editors/properties/physics.html>`_ > 
`Physics Type <https://upbge.org/manual/manual/editors/properties/physics.html#id1>`_: 
`Dynamic <https://upbge.org/manual/manual/editors/properties/physics_dynamic.html>`_, 
`Rigid Body <https://upbge.org/manual/manual/editors/properties/physics_rigid_body.html>`_, 
`Soft Body <https://upbge.org/manual/manual/editors/properties/physics_soft_body.html>`_.


This node applies force to the entire object. In contrast, the **Apply Impulse** node applies force at a specific point.

Input
=====

Global
    The force will be applied in the direction of the global axes

Local
    Force will be applied in the direction of the object's axes

Condition
    The condition for this node start

Object
    Object that will be pushed away

Vector
    The value of the force that will be applied to the object by the direction of the axes in the Cartesian plane. It can be a value referring to the axes of the world (Global) or the axes of the object (Local)

Output
======

**Done** 
    **True** if the node performed successfully.

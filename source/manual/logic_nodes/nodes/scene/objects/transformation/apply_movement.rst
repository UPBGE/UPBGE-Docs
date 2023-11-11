***********
Apply Movement
***********

Description
===========

Moves the object a certain vector-defined distance. Does not apply acceleration.

The object is still subject to other forces while the motion is being applied, such as acceleration due to the force of gravity.

The node can be applied to some types of physical properties, as follows:

`Game Physics <https://upbge.org/manual/manual/editors/properties/physics.html>`_ > 
`Physics Type <https://upbge.org/manual/manual/editors/properties/physics.html#id1>`_: 
`No Collision <https://upbge.org/manual/manual/editors/properties/physics_no_collision.html>`_,
`Static <https://upbge.org/manual/manual/editors/properties/physics_static.html>`_,
`Dynamic <https://upbge.org/manual/manual/editors/properties/physics_dynamic.html>`_, 
`Rigid Body <https://upbge.org/manual/manual/editors/properties/physics_rigid_body.html>`_, 
`Character <https://upbge.org/manual/manual/editors/properties/physics_character.html>`_.

Input
=====

Condition
    The condition for this node start

Object
    Object that will be moved

Vector
    The amount of displacement that will be applied to the object.

Output
======

**Done** 
    **True** if the node performed successfully.

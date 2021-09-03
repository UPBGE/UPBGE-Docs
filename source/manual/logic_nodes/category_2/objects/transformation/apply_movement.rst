***********
Apply Movement
***********

Description
===========

Move o objeto em uma certa distância definida por vetor. Não aplica aceleração.

O objeto ainda está sujeito a outras forças enquanto o movimento está sendo aplicado, como por exemplo a aceleração da força da gravidade.

O nó pode ser aplicado em alguns tipos de propriedades físicas, sendo: 

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

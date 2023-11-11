************
Apply Torque
************

Description
===========
..
   Original text in portuguese
   Rotaciona um objeto utilizando a mecânica de torque e tenta seguir as regras físicas do mundo real. Utiliza como unidade de medida o Newton-metro (Torque = Força x Comprimento da alavanca).
   No mundo real, para aplicar torque é necessário uma **alavanca com comprimento** e um **objeto que esteja sofrendo uma força de união**. Para o movimento acontecer nesse objeto o *Torque* deve ser maior que a *força de união*. A força de união real geralmente engloba atrito e tensão.
   Diferente do mundo real que a chave de boca "prende" o parafuso que está sendo rotacionado, na UPBGE não existe essa limitação e então toda a força do Torque é aplicada de uma só vez, podendo perpetuar a continuidade da rotação.
   Se o objeto possuir algum tipo de `Collision Bounds <https://upbge.org/manual/manual/editors/properties/physics.html#collision-bounds>`_ diferente de Sphere, será necessário um valor de torque superior à força que deixa o objeto estático para ele poder "rotacionar".

Rotate an object using torque mechanics and try to follow real-world physical rules. It uses the Newton-meter as a unit of measure (Torque = Force x Length of the lever).

In the real world, applying torque requires a **lever with length** and an **object that is experiencing a binding force**. For movement to take place on this object the *Torque* must be greater than the *Bonding Force*. The *Real Bonding Force* generally encompasses friction and tension.

Unlike in the real world, the wrench "holds" the screw that is being rotated, in the UPBGE there is no such limitation and so all the Torque force is applied at once, which can perpetuate the rotation continuity.

If the object has some kind of `Collision Bounds <https://upbge.org/manual/manual/editors/properties/physics.html#collision-bounds>`_ different from Sphere, will be necessary a torque value greater than the force that makes the object static

.. note::
   In order to limit pivoting of the torquing, assign a rotation limit to a certain origin with either an `Armature Bone <https://docs.blender.org/manual/en/latest/animation/armatures/index.html>`_ or a `Rigid Body Joint Constraint <https://docs.blender.org/manual/en/2.79/rigging/constraints/relationship/rigid_body_joint.html>`_.


Input
=====
Global
    The *torque* will be applied following the global axes of the scene

Local
    The *torque* will be applied following the object's axes

Condition
    The condition for this node start

Object
    Object that will be rotated

Vector
    The value that will be applied to the rotation in newton-meters

Output
======

**Done** 
    **True** if the node performed successfully.

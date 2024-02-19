.. figure:: /images/logic_nodes/objects/transformation/ln-apply_force.png
   :align: right
   :width: 215
   :alt: Apply Force Node

.. _ln-apply_force:

==============
Apply Force
==============

Applies an offset force to an object on any axis of the Cartesian plane. To function properly, the object must have a physical property that enables displacement.

:ref:`Game Physics <game-engine-physics>` >
:ref:`Physics Type <game-engine-physics-type>`:
:ref:`Dynamic <game-engine-physics-dynamic>`,
:ref:`Rigid Body <game-engine-physics-rigid-body>`,
:ref:`Soft Body <game-engine-physics-soft-body>`.

The node applies force to the entire object. In contrast, the :ref:`Apply Impulse <ln-apply_impulse>` node applies force at a specific point.

Input
+++++

Local
   If checked, force will be applied in the direction of the object's local axes, else of the object's global axes.

Condition
   The condition for this node to start.

Object
   Object that will be pushed away.

Vector
   Value of the force that will be applied to the object, by the direction of the axes in the Cartesian plane. It can be a value referring to the axes of the world (global) or the axes of the object (local).

Output
++++++

Done
   *True* if the node performed successfully, else *False*.

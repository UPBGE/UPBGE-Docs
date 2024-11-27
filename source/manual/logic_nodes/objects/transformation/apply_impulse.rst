.. figure:: /images/logic_nodes/objects/transformation/ln-apply_impulse.png
   :align: right
   :width: 215
   :alt: Apply Impulse Node

.. _ln-apply_impulse:

==============================
Apply Impulse
==============================

Applies a displacement force that has an origin (*point*) and a *direction*. To function properly, the object must have a physical property that enables displacement.

:ref:`Game Physics <game-engine-physics>` >
:ref:`Physics Type <game-engine-physics-type>`:
:ref:`Dynamic <game-engine-physics-dynamic>`,
:ref:`Rigid Body <game-engine-physics-rigid-body>`,
:ref:`Soft Body <game-engine-physics-soft-body>`.

This node applies force at a specific point. In contrast, the :ref:`Apply Force <ln-apply_force>` node applies force in entire object.

Parameters
++++++++++++++++++++++++++++++

Mode
   Selected mode of operation to apply.

Local
   If checked, object's local axes will be used, else global axes are used.

Input
++++++++++++++++++++++++++++++

Condition
   The condition for this node to start.

Object
   Object that will be pushed away.

Vector
   The point on which to apply the impulse.

Impulse
   The impulse to be applied to the object.

Output
++++++++++++++++++++++++++++++

Done 
   *True* if the node performed successfully, else *False*.

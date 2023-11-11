*************
Apply Impulse
*************

Description
===========

It doesn't seem to be working properly - 01/09/2021

Applies a displacement force that has an origin(**Point**) and a **Direction**.

For this node to function properly, the object must have some physical property that enables displacement.

:ref:`Game Physics <game-engine-physics>` >
:ref:`Physics Type <game-engine-physics-type>`:
:ref:`Dynamic <game-engine-physics-dynamic>`,
:ref:`Rigid Body <game-engine-physics-rigid-body>`,
:ref:`Soft Body <game-engine-physics-soft-body>`.


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

.. figure:: /images/logic_nodes/physics/ln-add_constraint.png
   :align: right
   :width: 215
   :alt: Add Constraint Node

.. _ln-add_constraint:

==============================
Add Constraint
==============================

This node will create a new physics constraint on the selected object.

Parameters
++++++++++++++++++++++++++++++

Constraint Type
   Selected constraint type to add.

Inputs
++++++++++++++++++++++++++++++

Condition
   If connected, condition must be fulfilled for node to activate.

Object
   Which object to apply the constraint to.

Target
   Which object to use as target for the constraint (may not be the same as Object socket).

Name
   Unique name for this constraint for later access.

Use World Space 
   Calculate the pivot in world space instead of local.

Pivot
   Pivot for physics calculations.

Linked Collision
   If enabled, object will collide with target.

Outputs
++++++++++++++++++++++++++++++

Done
   *True* if node performed successfully, else *False*.

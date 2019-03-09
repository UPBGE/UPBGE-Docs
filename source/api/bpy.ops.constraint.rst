Constraint Operators
====================

.. module:: bpy.ops.constraint

.. function:: childof_clear_inverse(constraint="", owner='OBJECT')

   Clear inverse correction for ChildOf constraint

   :arg constraint:

      Constraint, Name of the constraint to edit

   :type constraint: string, (optional, never None)
   :arg owner:

      Owner, The owner of this constraint

      * ``OBJECT`` Object, Edit a constraint on the active object.
      * ``BONE`` Bone, Edit a constraint on the active bone.

   :type owner: enum in ['OBJECT', 'BONE'], (optional)

.. function:: childof_set_inverse(constraint="", owner='OBJECT')

   Set inverse correction for ChildOf constraint

   :arg constraint:

      Constraint, Name of the constraint to edit

   :type constraint: string, (optional, never None)
   :arg owner:

      Owner, The owner of this constraint

      * ``OBJECT`` Object, Edit a constraint on the active object.
      * ``BONE`` Bone, Edit a constraint on the active bone.

   :type owner: enum in ['OBJECT', 'BONE'], (optional)

.. function:: delete()

   Remove constraint from constraint stack

.. function:: followpath_path_animate(constraint="", owner='OBJECT', frame_start=1, length=100)

   Add default animation for path used by constraint if it isn't animated already

   :arg constraint:

      Constraint, Name of the constraint to edit

   :type constraint: string, (optional, never None)
   :arg owner:

      Owner, The owner of this constraint

      * ``OBJECT`` Object, Edit a constraint on the active object.
      * ``BONE`` Bone, Edit a constraint on the active bone.

   :type owner: enum in ['OBJECT', 'BONE'], (optional)
   :arg frame_start:

      Start Frame, First frame of path animation

   :type frame_start: int in [-1048574, 1048574], (optional)
   :arg length:

      Length, Number of frames that path animation should take

   :type length: int in [0, 1048574], (optional)

.. function:: limitdistance_reset(constraint="", owner='OBJECT')

   Reset limiting distance for Limit Distance Constraint

   :arg constraint:

      Constraint, Name of the constraint to edit

   :type constraint: string, (optional, never None)
   :arg owner:

      Owner, The owner of this constraint

      * ``OBJECT`` Object, Edit a constraint on the active object.
      * ``BONE`` Bone, Edit a constraint on the active bone.

   :type owner: enum in ['OBJECT', 'BONE'], (optional)

.. function:: move_down(constraint="", owner='OBJECT')

   Move constraint down in constraint stack

   :arg constraint:

      Constraint, Name of the constraint to edit

   :type constraint: string, (optional, never None)
   :arg owner:

      Owner, The owner of this constraint

      * ``OBJECT`` Object, Edit a constraint on the active object.
      * ``BONE`` Bone, Edit a constraint on the active bone.

   :type owner: enum in ['OBJECT', 'BONE'], (optional)

.. function:: move_up(constraint="", owner='OBJECT')

   Move constraint up in constraint stack

   :arg constraint:

      Constraint, Name of the constraint to edit

   :type constraint: string, (optional, never None)
   :arg owner:

      Owner, The owner of this constraint

      * ``OBJECT`` Object, Edit a constraint on the active object.
      * ``BONE`` Bone, Edit a constraint on the active bone.

   :type owner: enum in ['OBJECT', 'BONE'], (optional)

.. function:: objectsolver_clear_inverse(constraint="", owner='OBJECT')

   Clear inverse correction for ObjectSolver constraint

   :arg constraint:

      Constraint, Name of the constraint to edit

   :type constraint: string, (optional, never None)
   :arg owner:

      Owner, The owner of this constraint

      * ``OBJECT`` Object, Edit a constraint on the active object.
      * ``BONE`` Bone, Edit a constraint on the active bone.

   :type owner: enum in ['OBJECT', 'BONE'], (optional)

.. function:: objectsolver_set_inverse(constraint="", owner='OBJECT')

   Set inverse correction for ObjectSolver constraint

   :arg constraint:

      Constraint, Name of the constraint to edit

   :type constraint: string, (optional, never None)
   :arg owner:

      Owner, The owner of this constraint

      * ``OBJECT`` Object, Edit a constraint on the active object.
      * ``BONE`` Bone, Edit a constraint on the active bone.

   :type owner: enum in ['OBJECT', 'BONE'], (optional)

.. function:: stretchto_reset(constraint="", owner='OBJECT')

   Reset original length of bone for Stretch To Constraint

   :arg constraint:

      Constraint, Name of the constraint to edit

   :type constraint: string, (optional, never None)
   :arg owner:

      Owner, The owner of this constraint

      * ``OBJECT`` Object, Edit a constraint on the active object.
      * ``BONE`` Bone, Edit a constraint on the active bone.

   :type owner: enum in ['OBJECT', 'BONE'], (optional)


PoseBoneConstraints(bpy_struct)
===============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: PoseBoneConstraints(bpy_struct)

   Collection of pose bone constraints

   .. attribute:: active

      Active PoseChannel constraint

      :type: :class:`Constraint`

   .. method:: new(type)

      Add a constraint to this object

      :arg type:

         Constraint type to add

         * ``CAMERA_SOLVER`` Camera Solver.
         * ``FOLLOW_TRACK`` Follow Track.
         * ``OBJECT_SOLVER`` Object Solver.
         * ``COPY_LOCATION`` Copy Location, Copy the location of a target (with an optional offset), so that they move together.
         * ``COPY_ROTATION`` Copy Rotation, Copy the rotation of a target (with an optional offset), so that they rotate together.
         * ``COPY_SCALE`` Copy Scale, Copy the scale factors of a target (with an optional offset), so that they are scaled by the same amount.
         * ``COPY_TRANSFORMS`` Copy Transforms, Copy all the transformations of a target, so that they move together.
         * ``LIMIT_DISTANCE`` Limit Distance, Restrict movements to within a certain distance of a target (at the time of constraint evaluation only).
         * ``LIMIT_LOCATION`` Limit Location, Restrict movement along each axis within given ranges.
         * ``LIMIT_ROTATION`` Limit Rotation, Restrict rotation along each axis within given ranges.
         * ``LIMIT_SCALE`` Limit Scale, Restrict scaling along each axis with given ranges.
         * ``MAINTAIN_VOLUME`` Maintain Volume, Compensate for scaling one axis by applying suitable scaling to the other two axes.
         * ``TRANSFORM`` Transformation, Use one transform property from target to control another (or same) property on owner.
         * ``TRANSFORM_CACHE`` Transform Cache, Look up the transformation matrix from an external file.
         * ``CLAMP_TO`` Clamp To, Restrict movements to lie along a curve by remapping location along curve's longest axis.
         * ``DAMPED_TRACK`` Damped Track, Point towards a target by performing the smallest rotation necessary.
         * ``IK`` Inverse Kinematics, Control a chain of bones by specifying the endpoint target (Bones only).
         * ``LOCKED_TRACK`` Locked Track, Rotate around the specified ('locked') axis to point towards a target.
         * ``SPLINE_IK`` Spline IK, Align chain of bones along a curve (Bones only).
         * ``STRETCH_TO`` Stretch To, Stretch along Y-Axis to point towards a target.
         * ``TRACK_TO`` Track To, Legacy tracking constraint prone to twisting artifacts.
         * ``ACTION`` Action, Use transform property of target to look up pose for owner from an Action.
         * ``CHILD_OF`` Child Of, Make target the 'detachable' parent of owner.
         * ``FLOOR`` Floor, Use position (and optionally rotation) of target to define a 'wall' or 'floor' that the owner can not cross.
         * ``FOLLOW_PATH`` Follow Path, Use to animate an object/bone following a path.
         * ``PIVOT`` Pivot, Change pivot point for transforms (buggy).
         * ``RIGID_BODY_JOINT`` Rigid Body Joint, Use to define a Rigid Body Constraint (for Game Engine use only).
         * ``SHRINKWRAP`` Shrinkwrap, Restrict movements to surface of target mesh.

      :type type: enum in ['CAMERA_SOLVER', 'FOLLOW_TRACK', 'OBJECT_SOLVER', 'COPY_LOCATION', 'COPY_ROTATION', 'COPY_SCALE', 'COPY_TRANSFORMS', 'LIMIT_DISTANCE', 'LIMIT_LOCATION', 'LIMIT_ROTATION', 'LIMIT_SCALE', 'MAINTAIN_VOLUME', 'TRANSFORM', 'TRANSFORM_CACHE', 'CLAMP_TO', 'DAMPED_TRACK', 'IK', 'LOCKED_TRACK', 'SPLINE_IK', 'STRETCH_TO', 'TRACK_TO', 'ACTION', 'CHILD_OF', 'FLOOR', 'FOLLOW_PATH', 'PIVOT', 'RIGID_BODY_JOINT', 'SHRINKWRAP']
      :return:

         New constraint

      :rtype: :class:`Constraint`

   .. method:: remove(constraint)

      Remove a constraint from this object

      :arg constraint:

         Removed constraint

      :type constraint: :class:`Constraint`, (never None)

   .. classmethod:: bl_rna_get_subclass(id, default=None)
   
      :arg id: The RNA type identifier.
      :type id: string
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct` subclass


   .. classmethod:: bl_rna_get_subclass_py(id, default=None)
   
      :arg id: The RNA type identifier.
      :type id: string
      :return: The class or default when not found.
      :rtype: type


.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`

.. rubric:: Inherited Functions

.. hlist::
   :columns: 2

   * :class:`bpy_struct.as_pointer`
   * :class:`bpy_struct.driver_add`
   * :class:`bpy_struct.driver_remove`
   * :class:`bpy_struct.get`
   * :class:`bpy_struct.is_property_hidden`
   * :class:`bpy_struct.is_property_readonly`
   * :class:`bpy_struct.is_property_set`
   * :class:`bpy_struct.items`
   * :class:`bpy_struct.keyframe_delete`
   * :class:`bpy_struct.keyframe_insert`
   * :class:`bpy_struct.keys`
   * :class:`bpy_struct.path_from_id`
   * :class:`bpy_struct.path_resolve`
   * :class:`bpy_struct.property_unset`
   * :class:`bpy_struct.type_recast`
   * :class:`bpy_struct.values`

.. rubric:: References

.. hlist::
   :columns: 2

   * :class:`PoseBone.constraints`


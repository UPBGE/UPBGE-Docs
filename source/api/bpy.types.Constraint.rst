Constraint(bpy_struct)
======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`ActionConstraint`, :class:`CameraSolverConstraint`, :class:`ChildOfConstraint`, :class:`ClampToConstraint`, :class:`CopyLocationConstraint`, :class:`CopyRotationConstraint`, :class:`CopyScaleConstraint`, :class:`CopyTransformsConstraint`, :class:`DampedTrackConstraint`, :class:`FloorConstraint`, :class:`FollowPathConstraint`, :class:`FollowTrackConstraint`, :class:`KinematicConstraint`, :class:`LimitDistanceConstraint`, :class:`LimitLocationConstraint`, :class:`LimitRotationConstraint`, :class:`LimitScaleConstraint`, :class:`LockedTrackConstraint`, :class:`MaintainVolumeConstraint`, :class:`ObjectSolverConstraint`, :class:`PivotConstraint`, :class:`PythonConstraint`, :class:`RigidBodyJointConstraint`, :class:`ShrinkwrapConstraint`, :class:`SplineIKConstraint`, :class:`StretchToConstraint`, :class:`TrackToConstraint`, :class:`TransformCacheConstraint`, :class:`TransformConstraint`

.. class:: Constraint(bpy_struct)

   Constraint modifying the transformation of objects and bones

   .. attribute:: active

      Constraint is the one being edited

      :type: boolean, default False

   .. data:: error_location

      Amount of residual error in Blender space unit for constraints that work on position

      :type: float in [-inf, inf], default 0.0, (readonly)

   .. data:: error_rotation

      Amount of residual error in radians for constraints that work on orientation

      :type: float in [-inf, inf], default 0.0, (readonly)

   .. attribute:: influence

      Amount of influence constraint will have on the final solution

      :type: float in [0, 1], default 0.0

   .. attribute:: is_proxy_local

      Constraint was added in this proxy instance (i.e. did not belong to source Armature)

      :type: boolean, default False

   .. data:: is_valid

      Constraint has valid settings and can be evaluated

      :type: boolean, default False, (readonly)

   .. attribute:: mute

      Enable/Disable Constraint

      :type: boolean, default False

   .. attribute:: name

      Constraint name

      :type: string, default "", (never None)

   .. attribute:: owner_space

      Space that owner is evaluated in

      * ``WORLD`` World Space, The constraint is applied relative to the world coordinate system.
      * ``POSE`` Pose Space, The constraint is applied in Pose Space, the object transformation is ignored.
      * ``LOCAL_WITH_PARENT`` Local With Parent, The constraint is applied relative to the local coordinate system of the object, with the parent transformation added.
      * ``LOCAL`` Local Space, The constraint is applied relative to the local coordinate system of the object.

      :type: enum in ['WORLD', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL'], default 'WORLD'

   .. attribute:: show_expanded

      Constraint's panel is expanded in UI

      :type: boolean, default False

   .. attribute:: target_space

      Space that target is evaluated in

      * ``WORLD`` World Space, The transformation of the target is evaluated relative to the world coordinate system.
      * ``POSE`` Pose Space, The transformation of the target is only evaluated in the Pose Space, the target armature object transformation is ignored.
      * ``LOCAL_WITH_PARENT`` Local With Parent, The transformation of the target bone is evaluated relative its local coordinate system, with the parent transformation added.
      * ``LOCAL`` Local Space, The transformation of the target is evaluated relative to its local coordinate system.

      :type: enum in ['WORLD', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL'], default 'WORLD'

   .. data:: type

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

      :type: enum in ['CAMERA_SOLVER', 'FOLLOW_TRACK', 'OBJECT_SOLVER', 'COPY_LOCATION', 'COPY_ROTATION', 'COPY_SCALE', 'COPY_TRANSFORMS', 'LIMIT_DISTANCE', 'LIMIT_LOCATION', 'LIMIT_ROTATION', 'LIMIT_SCALE', 'MAINTAIN_VOLUME', 'TRANSFORM', 'TRANSFORM_CACHE', 'CLAMP_TO', 'DAMPED_TRACK', 'IK', 'LOCKED_TRACK', 'SPLINE_IK', 'STRETCH_TO', 'TRACK_TO', 'ACTION', 'CHILD_OF', 'FLOOR', 'FOLLOW_PATH', 'PIVOT', 'RIGID_BODY_JOINT', 'SHRINKWRAP'], default 'CAMERA_SOLVER', (readonly)

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

   * :class:`Object.constraints`
   * :class:`ObjectConstraints.active`
   * :class:`ObjectConstraints.new`
   * :class:`ObjectConstraints.remove`
   * :class:`PoseBone.constraints`
   * :class:`PoseBoneConstraints.active`
   * :class:`PoseBoneConstraints.new`
   * :class:`PoseBoneConstraints.remove`
   * :class:`UILayout.template_constraint`


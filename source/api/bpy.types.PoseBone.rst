PoseBone(bpy_struct)
====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: PoseBone(bpy_struct)

   Channel defining pose data for a bone in a Pose

   .. attribute:: bbone_curveinx

      X-axis handle offset for start of the B-Bone's curve, adjusts curvature

      :type: float in [-5, 5], default 0.0

   .. attribute:: bbone_curveiny

      Y-axis handle offset for start of the B-Bone's curve, adjusts curvature

      :type: float in [-5, 5], default 0.0

   .. attribute:: bbone_curveoutx

      X-axis handle offset for end of the B-Bone's curve, adjusts curvature

      :type: float in [-5, 5], default 0.0

   .. attribute:: bbone_curveouty

      Y-axis handle offset for end of the B-Bone's curve, adjusts curvature

      :type: float in [-5, 5], default 0.0

   .. attribute:: bbone_custom_handle_end

      Bone that serves as the end handle for the B-Bone curve

      :type: :class:`PoseBone`

   .. attribute:: bbone_custom_handle_start

      Bone that serves as the start handle for the B-Bone curve

      :type: :class:`PoseBone`

   .. attribute:: bbone_easein

      Length of first Bezier Handle (for B-Bones only)

      :type: float in [-5, 5], default 1.0

   .. attribute:: bbone_easeout

      Length of second Bezier Handle (for B-Bones only)

      :type: float in [-5, 5], default 1.0

   .. attribute:: bbone_rollin

      Roll offset for the start of the B-Bone, adjusts twist

      :type: float in [-6.28319, 6.28319], default 0.0

   .. attribute:: bbone_rollout

      Roll offset for the end of the B-Bone, adjusts twist

      :type: float in [-6.28319, 6.28319], default 0.0

   .. attribute:: bbone_scalein

      Scale factor for start of the B-Bone, adjusts thickness (for tapering effects)

      :type: float in [0, 5], default 1.0

   .. attribute:: bbone_scaleout

      Scale factor for end of the B-Bone, adjusts thickness (for tapering effects)

      :type: float in [0, 5], default 1.0

   .. data:: bone

      Bone associated with this PoseBone

      :type: :class:`Bone`, (readonly, never None)

   .. attribute:: bone_group

      Bone Group this pose channel belongs to

      :type: :class:`BoneGroup`

   .. attribute:: bone_group_index

      Bone Group this pose channel belongs to (0=no group)

      :type: int in [-32768, 32767], default 0

   .. data:: child

      Child of this pose bone

      :type: :class:`PoseBone`, (readonly)

   .. data:: constraints

      Constraints that act on this PoseChannel

      :type: :class:`PoseBoneConstraints` :class:`bpy_prop_collection` of :class:`Constraint`, (readonly)

   .. attribute:: custom_shape

      Object that defines custom draw type for this bone

      :type: :class:`Object`

   .. attribute:: custom_shape_scale

      Adjust the size of the custom shape

      :type: float in [0, 1000], default 0.0

   .. attribute:: custom_shape_transform

      Bone that defines the display transform of this custom shape

      :type: :class:`PoseBone`

   .. data:: head

      Location of head of the channel's bone

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. attribute:: ik_linear_weight

      Weight of scale constraint for IK

      :type: float in [0, 1], default 0.0

   .. attribute:: ik_max_x

      Maximum angles for IK Limit

      :type: float in [0, 3.14159], default 0.0

   .. attribute:: ik_max_y

      Maximum angles for IK Limit

      :type: float in [0, 3.14159], default 0.0

   .. attribute:: ik_max_z

      Maximum angles for IK Limit

      :type: float in [0, 3.14159], default 0.0

   .. attribute:: ik_min_x

      Minimum angles for IK Limit

      :type: float in [-3.14159, 0], default 0.0

   .. attribute:: ik_min_y

      Minimum angles for IK Limit

      :type: float in [-3.14159, 0], default 0.0

   .. attribute:: ik_min_z

      Minimum angles for IK Limit

      :type: float in [-3.14159, 0], default 0.0

   .. attribute:: ik_rotation_weight

      Weight of rotation constraint for IK

      :type: float in [0, 1], default 0.0

   .. attribute:: ik_stiffness_x

      IK stiffness around the X axis

      :type: float in [0, 0.99], default 0.0

   .. attribute:: ik_stiffness_y

      IK stiffness around the Y axis

      :type: float in [0, 0.99], default 0.0

   .. attribute:: ik_stiffness_z

      IK stiffness around the Z axis

      :type: float in [0, 0.99], default 0.0

   .. attribute:: ik_stretch

      Allow scaling of the bone for IK

      :type: float in [0, 1], default 0.0

   .. data:: is_in_ik_chain

      Is part of an IK chain

      :type: boolean, default False, (readonly)

   .. attribute:: location

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: lock_ik_x

      Disallow movement around the X axis

      :type: boolean, default False

   .. attribute:: lock_ik_y

      Disallow movement around the Y axis

      :type: boolean, default False

   .. attribute:: lock_ik_z

      Disallow movement around the Z axis

      :type: boolean, default False

   .. attribute:: lock_location

      Lock editing of location in the interface

      :type: boolean array of 3 items, default (False, False, False)

   .. attribute:: lock_rotation

      Lock editing of rotation in the interface

      :type: boolean array of 3 items, default (False, False, False)

   .. attribute:: lock_rotation_w

      Lock editing of 'angle' component of four-component rotations in the interface

      :type: boolean, default False

   .. attribute:: lock_rotations_4d

      Lock editing of four component rotations by components (instead of as Eulers)

      :type: boolean, default False

   .. attribute:: lock_scale

      Lock editing of scale in the interface

      :type: boolean array of 3 items, default (False, False, False)

   .. attribute:: matrix

      Final 4x4 matrix after constraints and drivers are applied (object space)

      :type: float multi-dimensional array of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. attribute:: matrix_basis

      Alternative access to location/scale/rotation relative to the parent and own rest bone

      :type: float multi-dimensional array of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. data:: matrix_channel

      4x4 matrix, before constraints

      :type: float multi-dimensional array of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), (readonly)

   .. data:: motion_path

      Motion Path for this element

      :type: :class:`MotionPath`, (readonly)

   .. attribute:: name

      :type: string, default "", (never None)

   .. data:: parent

      Parent of this pose bone

      :type: :class:`PoseBone`, (readonly)

   .. attribute:: rotation_axis_angle

      Angle of Rotation for Axis-Angle rotation representation

      :type: float array of 4 items in [-inf, inf], default (0.0, 0.0, 1.0, 0.0)

   .. attribute:: rotation_euler

      Rotation in Eulers

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: rotation_mode

      * ``QUATERNION`` Quaternion (WXYZ), No Gimbal Lock (default).
      * ``XYZ`` XYZ Euler, XYZ Rotation Order (prone to Gimbal Lock).
      * ``XZY`` XZY Euler, XZY Rotation Order (prone to Gimbal Lock).
      * ``YXZ`` YXZ Euler, YXZ Rotation Order (prone to Gimbal Lock).
      * ``YZX`` YZX Euler, YZX Rotation Order (prone to Gimbal Lock).
      * ``ZXY`` ZXY Euler, ZXY Rotation Order (prone to Gimbal Lock).
      * ``ZYX`` ZYX Euler, ZYX Rotation Order (prone to Gimbal Lock).
      * ``AXIS_ANGLE`` Axis Angle, Axis Angle (W+XYZ), defines a rotation around some axis defined by 3D-Vector.

      :type: enum in ['QUATERNION', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX', 'AXIS_ANGLE'], default 'QUATERNION'

   .. attribute:: rotation_quaternion

      Rotation in Quaternions

      :type: float array of 4 items in [-inf, inf], default (1.0, 0.0, 0.0, 0.0)

   .. attribute:: scale

      :type: float array of 3 items in [-inf, inf], default (1.0, 1.0, 1.0)

   .. data:: tail

      Location of tail of the channel's bone

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. attribute:: use_bbone_custom_handles

      Use custom reference bones as handles for B-Bones instead of next/previous bones, leave these blank to use only B-Bone offset properties to control the shape

      :type: boolean, default False

   .. attribute:: use_bbone_relative_end_handle

      Treat custom end handle position as a relative value

      :type: boolean, default False

   .. attribute:: use_bbone_relative_start_handle

      Treat custom start handle position as a relative value

      :type: boolean, default False

   .. attribute:: use_custom_shape_bone_size

      Scale the custom object by the bone length

      :type: boolean, default False

   .. attribute:: use_ik_limit_x

      Limit movement around the X axis

      :type: boolean, default False

   .. attribute:: use_ik_limit_y

      Limit movement around the Y axis

      :type: boolean, default False

   .. attribute:: use_ik_limit_z

      Limit movement around the Z axis

      :type: boolean, default False

   .. attribute:: use_ik_linear_control

      Apply channel size as IK constraint if stretching is enabled

      :type: boolean, default False

   .. attribute:: use_ik_rotation_control

      Apply channel rotation as IK constraint

      :type: boolean, default False

   .. data:: basename

      The name of this bone before any '.' character
      (readonly)

   .. data:: center

      The midpoint between the head and the tail.
      (readonly)

   .. data:: children

      (readonly)

   .. data:: children_recursive

      A list of all children from this bone.
      (readonly)

   .. data:: children_recursive_basename

      Returns a chain of children with the same base name as this bone.
      Only direct chains are supported, forks caused by multiple children
      with matching base names will terminate the function
      and not be returned.
      (readonly)

   .. attribute:: length

      The distance from head to tail,
      when set the head is moved to fit the length.

   .. data:: parent_recursive

      A list of parents, starting with the immediate parent
      (readonly)

   .. data:: vector

      The direction this bone is pointing.
      Utility function for (tail - head)
      (readonly)

   .. data:: x_axis

      Vector pointing down the x-axis of the bone.
      (readonly)

   .. data:: y_axis

      Vector pointing down the y-axis of the bone.
      (readonly)

   .. data:: z_axis

      Vector pointing down the z-axis of the bone.
      (readonly)

   .. method:: evaluate_envelope(point)

      Calculate bone envelope at given point

      :arg point:

         Point, Position in 3d space to evaluate

      :type point: float array of 3 items in [-inf, inf]
      :return:

         Factor, Envelope factor

      :rtype: float in [-inf, inf]

   .. method:: parent_index(parent_test)

      The same as 'bone in other_bone.parent_recursive'
      but saved generating a list.

   .. method:: translate(vec)

      Utility function to add *vec* to the head and tail of this bone

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

   * :mod:`bpy.context.active_pose_bone`
   * :mod:`bpy.context.pose_bone`
   * :mod:`bpy.context.selected_pose_bones`
   * :mod:`bpy.context.visible_pose_bones`
   * :class:`Object.convert_space`
   * :class:`Pose.bones`
   * :class:`PoseBone.bbone_custom_handle_end`
   * :class:`PoseBone.bbone_custom_handle_start`
   * :class:`PoseBone.child`
   * :class:`PoseBone.custom_shape_transform`
   * :class:`PoseBone.parent`


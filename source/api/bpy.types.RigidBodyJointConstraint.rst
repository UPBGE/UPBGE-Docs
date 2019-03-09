RigidBodyJointConstraint(Constraint)
====================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: RigidBodyJointConstraint(Constraint)

   For use with the Game Engine

   .. attribute:: axis_x

      Rotate pivot on X axis

      :type: float in [-6.28319, 6.28319], default 0.0

   .. attribute:: axis_y

      Rotate pivot on Y axis

      :type: float in [-6.28319, 6.28319], default 0.0

   .. attribute:: axis_z

      Rotate pivot on Z axis

      :type: float in [-6.28319, 6.28319], default 0.0

   .. attribute:: breaking_threshold

      Break on impulse greater than threshold

      :type: float in [0, inf], default 0.0

   .. attribute:: child

      Child object

      :type: :class:`Object`

   .. attribute:: limit_angle_max_x

      :type: float in [-6.28319, 6.28319], default 0.0

   .. attribute:: limit_angle_max_y

      :type: float in [-6.28319, 6.28319], default 0.0

   .. attribute:: limit_angle_max_z

      :type: float in [-6.28319, 6.28319], default 0.0

   .. attribute:: limit_angle_min_x

      :type: float in [-6.28319, 6.28319], default 0.0

   .. attribute:: limit_angle_min_y

      :type: float in [-6.28319, 6.28319], default 0.0

   .. attribute:: limit_angle_min_z

      :type: float in [-6.28319, 6.28319], default 0.0

   .. attribute:: limit_max_x

      :type: float in [-inf, inf], default 0.0

   .. attribute:: limit_max_y

      :type: float in [-inf, inf], default 0.0

   .. attribute:: limit_max_z

      :type: float in [-inf, inf], default 0.0

   .. attribute:: limit_min_x

      :type: float in [-inf, inf], default 0.0

   .. attribute:: limit_min_y

      :type: float in [-inf, inf], default 0.0

   .. attribute:: limit_min_z

      :type: float in [-inf, inf], default 0.0

   .. attribute:: pivot_type

      * ``BALL`` Ball, Allow rotations around all axes.
      * ``HINGE`` Hinge, Work in one plane, allow rotations around one axis only.
      * ``CONE_TWIST`` Cone Twist, Allow rotations around all axes with limits for the cone and twist axes.
      * ``GENERIC_6_DOF`` Generic 6 DoF, No constraints by default, limits can be set individually.

      :type: enum in ['BALL', 'HINGE', 'CONE_TWIST', 'GENERIC_6_DOF'], default 'BALL'

   .. attribute:: pivot_x

      Offset pivot on X

      :type: float in [-1000, 1000], default 0.0

   .. attribute:: pivot_y

      Offset pivot on Y

      :type: float in [-1000, 1000], default 0.0

   .. attribute:: pivot_z

      Offset pivot on Z

      :type: float in [-1000, 1000], default 0.0

   .. attribute:: show_pivot

      Display the pivot point and rotation in 3D view

      :type: boolean, default False

   .. attribute:: target

      Target Object

      :type: :class:`Object`

   .. attribute:: use_angular_limit_x

      Use minimum/maximum X angular limit

      :type: boolean, default False

   .. attribute:: use_angular_limit_y

      Use minimum/maximum Y angular limit

      :type: boolean, default False

   .. attribute:: use_angular_limit_z

      Use minimum/maximum Z angular limit

      :type: boolean, default False

   .. attribute:: use_breaking

      Allow breaking on high impulse

      :type: boolean, default False

   .. attribute:: use_limit_x

      Use minimum/maximum X limit

      :type: boolean, default False

   .. attribute:: use_limit_y

      Use minimum/maximum y limit

      :type: boolean, default False

   .. attribute:: use_limit_z

      Use minimum/maximum z limit

      :type: boolean, default False

   .. attribute:: use_linked_collision

      Disable collision between linked bodies

      :type: boolean, default False

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
   * :class:`Constraint.name`
   * :class:`Constraint.type`
   * :class:`Constraint.owner_space`
   * :class:`Constraint.target_space`
   * :class:`Constraint.mute`
   * :class:`Constraint.show_expanded`
   * :class:`Constraint.is_valid`
   * :class:`Constraint.active`
   * :class:`Constraint.is_proxy_local`
   * :class:`Constraint.influence`
   * :class:`Constraint.error_location`
   * :class:`Constraint.error_rotation`

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


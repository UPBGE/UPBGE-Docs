FollowPathConstraint(Constraint)
================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: FollowPathConstraint(Constraint)

   Lock motion to the target path

   .. attribute:: forward_axis

      Axis that points forward along the path

      :type: enum in ['FORWARD_X', 'FORWARD_Y', 'FORWARD_Z', 'TRACK_NEGATIVE_X', 'TRACK_NEGATIVE_Y', 'TRACK_NEGATIVE_Z'], default 'FORWARD_X'

   .. attribute:: offset

      Offset from the position corresponding to the time frame

      :type: float in [-1.04857e+06, 1.04857e+06], default 0.0

   .. attribute:: offset_factor

      Percentage value defining target position along length of curve

      :type: float in [0, 1], default 0.0

   .. attribute:: target

      Target Object

      :type: :class:`Object`

   .. attribute:: up_axis

      Axis that points upward

      :type: enum in ['UP_X', 'UP_Y', 'UP_Z'], default 'UP_X'

   .. attribute:: use_curve_follow

      Object will follow the heading and banking of the curve

      :type: boolean, default False

   .. attribute:: use_curve_radius

      Object is scaled by the curve radius

      :type: boolean, default False

   .. attribute:: use_fixed_location

      Object will stay locked to a single point somewhere along the length of the curve regardless of time

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


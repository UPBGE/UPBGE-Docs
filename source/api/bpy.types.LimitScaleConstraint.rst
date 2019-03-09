LimitScaleConstraint(Constraint)
================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: LimitScaleConstraint(Constraint)

   Limit the scaling of the constrained object

   .. attribute:: max_x

      Highest X value to allow

      :type: float in [-1000, 1000], default 0.0

   .. attribute:: max_y

      Highest Y value to allow

      :type: float in [-1000, 1000], default 0.0

   .. attribute:: max_z

      Highest Z value to allow

      :type: float in [-1000, 1000], default 0.0

   .. attribute:: min_x

      Lowest X value to allow

      :type: float in [-1000, 1000], default 0.0

   .. attribute:: min_y

      Lowest Y value to allow

      :type: float in [-1000, 1000], default 0.0

   .. attribute:: min_z

      Lowest Z value to allow

      :type: float in [-1000, 1000], default 0.0

   .. attribute:: use_max_x

      Use the maximum X value

      :type: boolean, default False

   .. attribute:: use_max_y

      Use the maximum Y value

      :type: boolean, default False

   .. attribute:: use_max_z

      Use the maximum Z value

      :type: boolean, default False

   .. attribute:: use_min_x

      Use the minimum X value

      :type: boolean, default False

   .. attribute:: use_min_y

      Use the minimum Y value

      :type: boolean, default False

   .. attribute:: use_min_z

      Use the minimum Z value

      :type: boolean, default False

   .. attribute:: use_transform_limit

      Transforms are affected by this constraint as well

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


SculptToolCapabilities(bpy_struct)
==================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SculptToolCapabilities(bpy_struct)

   Read-only indications of which brush operations are supported by the current sculpt tool

   .. data:: has_accumulate

      :type: boolean, default False, (readonly)

   .. data:: has_auto_smooth

      :type: boolean, default False, (readonly)

   .. data:: has_gravity

      :type: boolean, default False, (readonly)

   .. data:: has_height

      :type: boolean, default False, (readonly)

   .. data:: has_jitter

      :type: boolean, default False, (readonly)

   .. data:: has_normal_weight

      :type: boolean, default False, (readonly)

   .. data:: has_persistence

      :type: boolean, default False, (readonly)

   .. data:: has_pinch_factor

      :type: boolean, default False, (readonly)

   .. data:: has_plane_offset

      :type: boolean, default False, (readonly)

   .. data:: has_rake_factor

      :type: boolean, default False, (readonly)

   .. data:: has_random_texture_angle

      :type: boolean, default False, (readonly)

   .. data:: has_sculpt_plane

      :type: boolean, default False, (readonly)

   .. data:: has_secondary_color

      :type: boolean, default False, (readonly)

   .. data:: has_smooth_stroke

      :type: boolean, default False, (readonly)

   .. data:: has_space_attenuation

      :type: boolean, default False, (readonly)

   .. data:: has_strength_pressure

      :type: boolean, default False, (readonly)

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

   * :class:`Brush.sculpt_capabilities`


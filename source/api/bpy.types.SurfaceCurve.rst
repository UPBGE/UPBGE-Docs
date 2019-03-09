SurfaceCurve(Curve)
===================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`, :class:`Curve`

.. class:: SurfaceCurve(Curve)

   Curve data-block used for storing surfaces

   .. attribute:: use_uv_as_generated

      Uses the UV values as Generated textured coordinates

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
   * :class:`ID.name`
   * :class:`ID.users`
   * :class:`ID.use_fake_user`
   * :class:`ID.tag`
   * :class:`ID.is_updated`
   * :class:`ID.is_updated_data`
   * :class:`ID.is_library_indirect`
   * :class:`ID.library`
   * :class:`ID.preview`
   * :class:`Curve.shape_keys`
   * :class:`Curve.splines`
   * :class:`Curve.show_handles`
   * :class:`Curve.show_normal_face`
   * :class:`Curve.path_duration`
   * :class:`Curve.use_path`
   * :class:`Curve.use_path_follow`
   * :class:`Curve.use_stretch`
   * :class:`Curve.use_deform_bounds`
   * :class:`Curve.use_radius`
   * :class:`Curve.bevel_resolution`
   * :class:`Curve.offset`
   * :class:`Curve.extrude`
   * :class:`Curve.bevel_depth`
   * :class:`Curve.resolution_u`
   * :class:`Curve.resolution_v`
   * :class:`Curve.render_resolution_u`
   * :class:`Curve.render_resolution_v`
   * :class:`Curve.eval_time`
   * :class:`Curve.bevel_object`
   * :class:`Curve.taper_object`
   * :class:`Curve.dimensions`
   * :class:`Curve.fill_mode`
   * :class:`Curve.twist_mode`
   * :class:`Curve.bevel_factor_mapping_start`
   * :class:`Curve.bevel_factor_mapping_end`
   * :class:`Curve.twist_smooth`
   * :class:`Curve.use_fill_deform`
   * :class:`Curve.use_fill_caps`
   * :class:`Curve.use_map_taper`
   * :class:`Curve.use_auto_texspace`
   * :class:`Curve.texspace_location`
   * :class:`Curve.texspace_size`
   * :class:`Curve.use_uv_as_generated`
   * :class:`Curve.materials`
   * :class:`Curve.bevel_factor_start`
   * :class:`Curve.bevel_factor_end`
   * :class:`Curve.is_editmode`
   * :class:`Curve.animation_data`
   * :class:`Curve.cycles`

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
   * :class:`ID.copy`
   * :class:`ID.user_clear`
   * :class:`ID.user_remap`
   * :class:`ID.make_local`
   * :class:`ID.user_of_id`
   * :class:`ID.animation_data_create`
   * :class:`ID.animation_data_clear`
   * :class:`ID.update_tag`
   * :class:`Curve.transform`
   * :class:`Curve.validate_material_indices`


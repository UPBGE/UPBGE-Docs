AnyType(bpy_struct)
===================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: AnyType(bpy_struct)

   RNA type used for pointers to any possible data

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

   * :class:`FCurve.update_autoflags`
   * :class:`KeyingSetInfo.generate`
   * :class:`RenderEngine.bake`
   * :class:`UILayout.context_pointer_set`
   * :class:`UILayout.enum_item_description`
   * :class:`UILayout.enum_item_icon`
   * :class:`UILayout.enum_item_name`
   * :class:`UILayout.icon`
   * :class:`UILayout.prop`
   * :class:`UILayout.prop_enum`
   * :class:`UILayout.prop_menu_enum`
   * :class:`UILayout.prop_search`
   * :class:`UILayout.prop_search`
   * :class:`UILayout.props_enum`
   * :class:`UILayout.template_ID`
   * :class:`UILayout.template_ID_preview`
   * :class:`UILayout.template_any_ID`
   * :class:`UILayout.template_cache_file`
   * :class:`UILayout.template_color_picker`
   * :class:`UILayout.template_color_ramp`
   * :class:`UILayout.template_colormanaged_view_settings`
   * :class:`UILayout.template_colorspace_settings`
   * :class:`UILayout.template_component_menu`
   * :class:`UILayout.template_curve_mapping`
   * :class:`UILayout.template_histogram`
   * :class:`UILayout.template_icon_view`
   * :class:`UILayout.template_image`
   * :class:`UILayout.template_layers`
   * :class:`UILayout.template_layers`
   * :class:`UILayout.template_list`
   * :class:`UILayout.template_list`
   * :class:`UILayout.template_marker`
   * :class:`UILayout.template_movieclip`
   * :class:`UILayout.template_movieclip_information`
   * :class:`UILayout.template_palette`
   * :class:`UILayout.template_path_builder`
   * :class:`UILayout.template_track`
   * :class:`UILayout.template_vectorscope`
   * :class:`UILayout.template_waveform`
   * :class:`UIList.draw_item`
   * :class:`UIList.draw_item`
   * :class:`UIList.draw_item`
   * :class:`UIList.filter_items`


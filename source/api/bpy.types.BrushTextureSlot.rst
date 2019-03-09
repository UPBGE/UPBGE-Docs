BrushTextureSlot(TextureSlot)
=============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`TextureSlot`

.. class:: BrushTextureSlot(TextureSlot)

   Texture slot for textures in a Brush data-block

   .. attribute:: angle

      Brush texture rotation

      :type: float in [0, 6.28319], default 0.0

   .. data:: has_random_texture_angle

      :type: boolean, default False, (readonly)

   .. data:: has_texture_angle

      :type: boolean, default False, (readonly)

   .. data:: has_texture_angle_source

      :type: boolean, default False, (readonly)

   .. attribute:: map_mode

      :type: enum in ['VIEW_PLANE', 'AREA_PLANE', 'TILED', '3D', 'RANDOM', 'STENCIL'], default 'VIEW_PLANE'

   .. attribute:: mask_map_mode

      :type: enum in ['VIEW_PLANE', 'TILED', 'RANDOM', 'STENCIL'], default 'VIEW_PLANE'

   .. attribute:: random_angle

      Brush texture random angle

      :type: float in [0, 6.28319], default 0.0

   .. attribute:: tex_paint_map_mode

      :type: enum in ['VIEW_PLANE', 'TILED', '3D', 'RANDOM', 'STENCIL'], default 'VIEW_PLANE'

   .. attribute:: use_rake

      :type: boolean, default False

   .. attribute:: use_random

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
   * :class:`TextureSlot.texture`
   * :class:`TextureSlot.name`
   * :class:`TextureSlot.offset`
   * :class:`TextureSlot.scale`
   * :class:`TextureSlot.rotation`
   * :class:`TextureSlot.color`
   * :class:`TextureSlot.blend_type`
   * :class:`TextureSlot.use_stencil`
   * :class:`TextureSlot.invert`
   * :class:`TextureSlot.use_rgb_to_intensity`
   * :class:`TextureSlot.default_value`
   * :class:`TextureSlot.output_node`

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

   * :class:`Brush.mask_texture_slot`
   * :class:`Brush.texture_slot`


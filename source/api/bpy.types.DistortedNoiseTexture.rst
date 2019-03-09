DistortedNoiseTexture(Texture)
==============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`, :class:`Texture`

.. class:: DistortedNoiseTexture(Texture)

   Procedural distorted noise texture

   .. attribute:: distortion

      Amount of distortion

      :type: float in [0, 10], default 0.0

   .. attribute:: nabla

      Size of derivative offset used for calculating normal

      :type: float in [0.001, 0.1], default 0.0

   .. attribute:: noise_basis

      Noise basis used for turbulence

      * ``BLENDER_ORIGINAL`` Blender Original, Noise algorithm - Blender original: Smooth interpolated noise.
      * ``ORIGINAL_PERLIN`` Original Perlin, Noise algorithm - Original Perlin: Smooth interpolated noise.
      * ``IMPROVED_PERLIN`` Improved Perlin, Noise algorithm - Improved Perlin: Smooth interpolated noise.
      * ``VORONOI_F1`` Voronoi F1, Noise algorithm - Voronoi F1: Returns distance to the closest feature point.
      * ``VORONOI_F2`` Voronoi F2, Noise algorithm - Voronoi F2: Returns distance to the 2nd closest feature point.
      * ``VORONOI_F3`` Voronoi F3, Noise algorithm - Voronoi F3: Returns distance to the 3rd closest feature point.
      * ``VORONOI_F4`` Voronoi F4, Noise algorithm - Voronoi F4: Returns distance to the 4th closest feature point.
      * ``VORONOI_F2_F1`` Voronoi F2-F1, Noise algorithm - Voronoi F1-F2.
      * ``VORONOI_CRACKLE`` Voronoi Crackle, Noise algorithm - Voronoi Crackle: Voronoi tessellation with sharp edges.
      * ``CELL_NOISE`` Cell Noise, Noise algorithm - Cell Noise: Square cell tessellation.

      :type: enum in ['BLENDER_ORIGINAL', 'ORIGINAL_PERLIN', 'IMPROVED_PERLIN', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2_F1', 'VORONOI_CRACKLE', 'CELL_NOISE'], default 'BLENDER_ORIGINAL'

   .. attribute:: noise_distortion

      Noise basis for the distortion

      * ``BLENDER_ORIGINAL`` Blender Original, Noise algorithm - Blender original: Smooth interpolated noise.
      * ``ORIGINAL_PERLIN`` Original Perlin, Noise algorithm - Original Perlin: Smooth interpolated noise.
      * ``IMPROVED_PERLIN`` Improved Perlin, Noise algorithm - Improved Perlin: Smooth interpolated noise.
      * ``VORONOI_F1`` Voronoi F1, Noise algorithm - Voronoi F1: Returns distance to the closest feature point.
      * ``VORONOI_F2`` Voronoi F2, Noise algorithm - Voronoi F2: Returns distance to the 2nd closest feature point.
      * ``VORONOI_F3`` Voronoi F3, Noise algorithm - Voronoi F3: Returns distance to the 3rd closest feature point.
      * ``VORONOI_F4`` Voronoi F4, Noise algorithm - Voronoi F4: Returns distance to the 4th closest feature point.
      * ``VORONOI_F2_F1`` Voronoi F2-F1, Noise algorithm - Voronoi F1-F2.
      * ``VORONOI_CRACKLE`` Voronoi Crackle, Noise algorithm - Voronoi Crackle: Voronoi tessellation with sharp edges.
      * ``CELL_NOISE`` Cell Noise, Noise algorithm - Cell Noise: Square cell tessellation.

      :type: enum in ['BLENDER_ORIGINAL', 'ORIGINAL_PERLIN', 'IMPROVED_PERLIN', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2_F1', 'VORONOI_CRACKLE', 'CELL_NOISE'], default 'BLENDER_ORIGINAL'

   .. attribute:: noise_scale

      Scaling for noise input

      :type: float in [0.0001, inf], default 0.0

   .. data:: users_material

      Materials that use this texture
      (readonly)

   .. data:: users_object_modifier

      Object modifiers that use this texture
      (readonly)

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
   * :class:`Texture.type`
   * :class:`Texture.use_clamp`
   * :class:`Texture.use_color_ramp`
   * :class:`Texture.color_ramp`
   * :class:`Texture.intensity`
   * :class:`Texture.contrast`
   * :class:`Texture.saturation`
   * :class:`Texture.factor_red`
   * :class:`Texture.factor_green`
   * :class:`Texture.factor_blue`
   * :class:`Texture.use_preview_alpha`
   * :class:`Texture.use_nodes`
   * :class:`Texture.node_tree`
   * :class:`Texture.animation_data`
   * :class:`Texture.users_material`
   * :class:`Texture.users_object_modifier`
   * :class:`Texture.users_material`
   * :class:`Texture.users_object_modifier`

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
   * :class:`Texture.evaluate`


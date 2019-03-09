ImageTexture(Texture)
=====================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`, :class:`Texture`

.. class:: ImageTexture(Texture)

   

   .. attribute:: checker_distance

      Distance between checker tiles

      :type: float in [0, 0.99], default 0.0

   .. attribute:: crop_max_x

      Maximum X value to crop the image

      :type: float in [-10, 10], default 0.0

   .. attribute:: crop_max_y

      Maximum Y value to crop the image

      :type: float in [-10, 10], default 0.0

   .. attribute:: crop_min_x

      Minimum X value to crop the image

      :type: float in [-10, 10], default 0.0

   .. attribute:: crop_min_y

      Minimum Y value to crop the image

      :type: float in [-10, 10], default 0.0

   .. attribute:: extension

      How the image is extrapolated past its original bounds

      * ``EXTEND`` Extend, Extend by repeating edge pixels of the image.
      * ``CLIP`` Clip, Clip to image size and set exterior pixels as transparent.
      * ``CLIP_CUBE`` Clip Cube, Clip to cubic-shaped area around the image and set exterior pixels as transparent.
      * ``REPEAT`` Repeat, Cause the image to repeat horizontally and vertically.
      * ``CHECKER`` Checker, Cause the image to repeat in checker board pattern.

      :type: enum in ['EXTEND', 'CLIP', 'CLIP_CUBE', 'REPEAT', 'CHECKER'], default 'EXTEND'

   .. attribute:: filter_eccentricity

      Maximum eccentricity (higher gives less blur at distant/oblique angles, but is also slower)

      :type: int in [1, 256], default 0

   .. attribute:: filter_probes

      Maximum number of samples (higher gives less blur at distant/oblique angles, but is also slower)

      :type: int in [1, 256], default 0

   .. attribute:: filter_size

      Multiply the filter size used by MIP Map and Interpolation

      :type: float in [0.1, 50], default 0.0

   .. attribute:: filter_type

      Texture filter to use for sampling image

      :type: enum in ['BOX', 'EWA', 'FELINE', 'AREA'], default 'BOX'

   .. attribute:: image

      :type: :class:`Image`

   .. data:: image_user

      Parameters defining which layer, pass and frame of the image is displayed

      :type: :class:`ImageUser`, (readonly)

   .. attribute:: invert_alpha

      Invert all the alpha values in the image

      :type: boolean, default False

   .. attribute:: repeat_x

      Repetition multiplier in the X direction

      :type: int in [1, 512], default 0

   .. attribute:: repeat_y

      Repetition multiplier in the Y direction

      :type: int in [1, 512], default 0

   .. attribute:: use_alpha

      Use the alpha channel information in the image

      :type: boolean, default False

   .. attribute:: use_calculate_alpha

      Calculate an alpha channel based on RGB values in the image

      :type: boolean, default False

   .. attribute:: use_checker_even

      Even checker tiles

      :type: boolean, default False

   .. attribute:: use_checker_odd

      Odd checker tiles

      :type: boolean, default False

   .. attribute:: use_derivative_map

      Use red and green as derivative values

      :type: boolean, default False

   .. attribute:: use_filter_size_min

      Use Filter Size as a minimal filter value in pixels

      :type: boolean, default False

   .. attribute:: use_flip_axis

      Flip the texture's X and Y axis

      :type: boolean, default False

   .. attribute:: use_interpolation

      Interpolate pixels using selected filter

      :type: boolean, default False

   .. attribute:: use_mipmap

      Use auto-generated MIP maps for the image

      :type: boolean, default False

   .. attribute:: use_mipmap_gauss

      Use Gauss filter to sample down MIP maps

      :type: boolean, default False

   .. attribute:: use_mirror_x

      Mirror the image repetition on the X direction

      :type: boolean, default False

   .. attribute:: use_mirror_y

      Mirror the image repetition on the Y direction

      :type: boolean, default False

   .. attribute:: use_normal_map

      Use image RGB values for normal mapping

      :type: boolean, default False

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


VoronoiTexture(Texture)
=======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`, :class:`Texture`

.. class:: VoronoiTexture(Texture)

   Procedural voronoi texture

   .. attribute:: color_mode

      * ``INTENSITY`` Intensity, Only calculate intensity.
      * ``POSITION`` Position, Color cells by position.
      * ``POSITION_OUTLINE`` Position and Outline, Use position plus an outline based on F2-F1.
      * ``POSITION_OUTLINE_INTENSITY`` Position, Outline, and Intensity, Multiply position and outline by intensity.

      :type: enum in ['INTENSITY', 'POSITION', 'POSITION_OUTLINE', 'POSITION_OUTLINE_INTENSITY'], default 'INTENSITY'

   .. attribute:: distance_metric

      Algorithm used to calculate distance of sample points to feature points

      * ``DISTANCE`` Actual Distance, sqrt(x\*x+y\*y+z\*z).
      * ``DISTANCE_SQUARED`` Distance Squared, (x\*x+y\*y+z\*z).
      * ``MANHATTAN`` Manhattan, The length of the distance in axial directions.
      * ``CHEBYCHEV`` Chebychev, The length of the longest Axial journey.
      * ``MINKOVSKY_HALF`` Minkowski 1/2, Set Minkowski variable to 0.5.
      * ``MINKOVSKY_FOUR`` Minkowski 4, Set Minkowski variable to 4.
      * ``MINKOVSKY`` Minkowski, Use the Minkowski function to calculate distance (exponent value determines the shape of the boundaries).

      :type: enum in ['DISTANCE', 'DISTANCE_SQUARED', 'MANHATTAN', 'CHEBYCHEV', 'MINKOVSKY_HALF', 'MINKOVSKY_FOUR', 'MINKOVSKY'], default 'DISTANCE'

   .. attribute:: minkovsky_exponent

      Minkowski exponent

      :type: float in [0.01, 10], default 0.0

   .. attribute:: nabla

      Size of derivative offset used for calculating normal

      :type: float in [0.001, 0.1], default 0.0

   .. attribute:: noise_intensity

      Scales the intensity of the noise

      :type: float in [0.01, 10], default 0.0

   .. attribute:: noise_scale

      Scaling for noise input

      :type: float in [0.0001, inf], default 0.0

   .. attribute:: weight_1

      Voronoi feature weight 1

      :type: float in [-2, 2], default 0.0

   .. attribute:: weight_2

      Voronoi feature weight 2

      :type: float in [-2, 2], default 0.0

   .. attribute:: weight_3

      Voronoi feature weight 3

      :type: float in [-2, 2], default 0.0

   .. attribute:: weight_4

      Voronoi feature weight 4

      :type: float in [-2, 2], default 0.0

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


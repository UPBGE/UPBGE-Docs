ParticleSettingsTextureSlot(TextureSlot)
========================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`TextureSlot`

.. class:: ParticleSettingsTextureSlot(TextureSlot)

   Texture slot for textures in a Particle Settings data-block

   .. attribute:: clump_factor

      Amount texture affects child clump

      :type: float in [-inf, inf], default 0.0

   .. attribute:: damp_factor

      Amount texture affects particle damping

      :type: float in [-inf, inf], default 0.0

   .. attribute:: density_factor

      Amount texture affects particle density

      :type: float in [-inf, inf], default 0.0

   .. attribute:: field_factor

      Amount texture affects particle force fields

      :type: float in [-inf, inf], default 0.0

   .. attribute:: gravity_factor

      Amount texture affects particle gravity

      :type: float in [-inf, inf], default 0.0

   .. attribute:: kink_amp_factor

      Amount texture affects child kink amplitude

      :type: float in [-inf, inf], default 0.0

   .. attribute:: kink_freq_factor

      Amount texture affects child kink frequency

      :type: float in [-inf, inf], default 0.0

   .. attribute:: length_factor

      Amount texture affects child hair length

      :type: float in [-inf, inf], default 0.0

   .. attribute:: life_factor

      Amount texture affects particle life time

      :type: float in [-inf, inf], default 0.0

   .. attribute:: mapping

      * ``FLAT`` Flat, Map X and Y coordinates directly.
      * ``CUBE`` Cube, Map using the normal vector.
      * ``TUBE`` Tube, Map with Z as central axis.
      * ``SPHERE`` Sphere, Map with Z as central axis.

      :type: enum in ['FLAT', 'CUBE', 'TUBE', 'SPHERE'], default 'FLAT'

   .. attribute:: mapping_x

      :type: enum in ['NONE', 'X', 'Y', 'Z'], default 'NONE'

   .. attribute:: mapping_y

      :type: enum in ['NONE', 'X', 'Y', 'Z'], default 'NONE'

   .. attribute:: mapping_z

      :type: enum in ['NONE', 'X', 'Y', 'Z'], default 'NONE'

   .. attribute:: object

      Object to use for mapping with Object texture coordinates

      :type: :class:`Object`

   .. attribute:: rough_factor

      Amount texture affects child roughness

      :type: float in [-inf, inf], default 0.0

   .. attribute:: size_factor

      Amount texture affects physical particle size

      :type: float in [-inf, inf], default 0.0

   .. attribute:: texture_coords

      Texture coordinates used to map the texture onto the background

      * ``GLOBAL`` Global, Use global coordinates for the texture coordinates.
      * ``OBJECT`` Object, Use linked object's coordinates for texture coordinates.
      * ``UV`` UV, Use UV coordinates for texture coordinates.
      * ``ORCO`` Generated, Use the original undeformed coordinates of the object.
      * ``STRAND`` Strand / Particle, Use normalized strand texture coordinate (1D) or particle age (X) and trail position (Y).

      :type: enum in ['GLOBAL', 'OBJECT', 'UV', 'ORCO', 'STRAND'], default 'GLOBAL'

   .. attribute:: time_factor

      Amount texture affects particle emission time

      :type: float in [-inf, inf], default 0.0

   .. attribute:: use_map_clump

      Affect the child clumping

      :type: boolean, default False

   .. attribute:: use_map_damp

      Affect the particle velocity damping

      :type: boolean, default False

   .. attribute:: use_map_density

      Affect the density of the particles

      :type: boolean, default False

   .. attribute:: use_map_field

      Affect the particle force fields

      :type: boolean, default False

   .. attribute:: use_map_gravity

      Affect the particle gravity

      :type: boolean, default False

   .. attribute:: use_map_kink_amp

      Affect the child kink amplitude

      :type: boolean, default False

   .. attribute:: use_map_kink_freq

      Affect the child kink frequency

      :type: boolean, default False

   .. attribute:: use_map_length

      Affect the child hair length

      :type: boolean, default False

   .. attribute:: use_map_life

      Affect the life time of the particles

      :type: boolean, default False

   .. attribute:: use_map_rough

      Affect the child rough

      :type: boolean, default False

   .. attribute:: use_map_size

      Affect the particle size

      :type: boolean, default False

   .. attribute:: use_map_time

      Affect the emission time of the particles

      :type: boolean, default False

   .. attribute:: use_map_velocity

      Affect the particle initial velocity

      :type: boolean, default False

   .. attribute:: uv_layer

      UV map to use for mapping with UV texture coordinates

      :type: string, default "", (never None)

   .. attribute:: velocity_factor

      Amount texture affects particle initial velocity

      :type: float in [-inf, inf], default 0.0

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

   * :class:`ParticleSettings.texture_slots`
   * :class:`ParticleSettingsTextureSlots.add`
   * :class:`ParticleSettingsTextureSlots.create`


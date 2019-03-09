MaterialTextureSlot(TextureSlot)
================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`TextureSlot`

.. class:: MaterialTextureSlot(TextureSlot)

   Texture slot for textures in a Material data-block

   .. attribute:: alpha_factor

      Amount texture affects alpha

      :type: float in [-inf, inf], default 0.0

   .. attribute:: ambient_factor

      Amount texture affects ambient

      :type: float in [-inf, inf], default 0.0

   .. attribute:: bump_method

      Method to use for bump mapping

      * ``BUMP_ORIGINAL`` Original.
      * ``BUMP_COMPATIBLE`` Compatible.
      * ``BUMP_LOW_QUALITY`` Low Quality, Use 3 tap filtering.
      * ``BUMP_MEDIUM_QUALITY`` Medium Quality, Use 5 tap filtering.
      * ``BUMP_BEST_QUALITY`` Best Quality, Use bicubic filtering (requires OpenGL 3.0+, it will fall back on medium setting for other systems).

      :type: enum in ['BUMP_ORIGINAL', 'BUMP_COMPATIBLE', 'BUMP_LOW_QUALITY', 'BUMP_MEDIUM_QUALITY', 'BUMP_BEST_QUALITY'], default 'BUMP_ORIGINAL'

   .. attribute:: bump_objectspace

      Space to apply bump mapping in

      :type: enum in ['BUMP_VIEWSPACE', 'BUMP_OBJECTSPACE', 'BUMP_TEXTURESPACE'], default 'BUMP_VIEWSPACE'

   .. attribute:: density_factor

      Amount texture affects density

      :type: float in [-inf, inf], default 0.0

   .. attribute:: diffuse_color_factor

      Amount texture affects diffuse color

      :type: float in [-inf, inf], default 0.0

   .. attribute:: diffuse_factor

      Amount texture affects diffuse reflectivity

      :type: float in [-inf, inf], default 0.0

   .. attribute:: displacement_factor

      Amount texture displaces the surface

      :type: float in [-inf, inf], default 0.0

   .. attribute:: emission_color_factor

      Amount texture affects emission color

      :type: float in [-inf, inf], default 0.0

   .. attribute:: emission_factor

      Amount texture affects emission

      :type: float in [-inf, inf], default 0.0

   .. attribute:: emit_factor

      Amount texture affects emission

      :type: float in [-inf, inf], default 0.0

   .. attribute:: hardness_factor

      Amount texture affects hardness

      :type: float in [-inf, inf], default 0.0

   .. attribute:: ior

      Indice of refraction

      :type: float in [1, 50], default 0.0

   .. attribute:: lod_bias

      Amount bias on mipmapping

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

   .. attribute:: mirror_factor

      Amount texture affects mirror color

      :type: float in [-inf, inf], default 0.0

   .. attribute:: normal_factor

      Amount texture affects normal values

      :type: float in [-inf, inf], default 0.0

   .. attribute:: normal_map_space

      Set space of normal map image

      :type: enum in ['CAMERA', 'WORLD', 'OBJECT', 'TANGENT'], default 'CAMERA'

   .. attribute:: object

      Object to use for mapping with Object texture coordinates

      :type: :class:`Object`

   .. attribute:: parallax_bump_scale

      Height of SPOM

      :type: float in [-inf, inf], default 0.0

   .. attribute:: parallax_steps

      Number of steps taken to achieve result

      :type: float in [-inf, inf], default 0.0

   .. attribute:: parallax_uv_discard

      To discard parallax UV at edges

      :type: boolean, default False

   .. attribute:: raymir_factor

      Amount texture affects ray mirror

      :type: float in [-inf, inf], default 0.0

   .. attribute:: reflection_color_factor

      Amount texture affects color of out-scattered light

      :type: float in [-inf, inf], default 0.0

   .. attribute:: reflection_factor

      Amount texture affects brightness of out-scattered light

      :type: float in [-inf, inf], default 0.0

   .. attribute:: refraction_ratio

      Amount refraction mixed with reflection

      :type: float in [0, 1], default 0.0

   .. attribute:: scattering_factor

      Amount texture affects scattering

      :type: float in [-inf, inf], default 0.0

   .. attribute:: specular_color_factor

      Amount texture affects specular color

      :type: float in [-inf, inf], default 0.0

   .. attribute:: specular_factor

      Amount texture affects specular reflectivity

      :type: float in [-inf, inf], default 0.0

   .. attribute:: texture_coords

      * ``GLOBAL`` Global, Use global coordinates for the texture coordinates.
      * ``OBJECT`` Object, Use linked object's coordinates for texture coordinates.
      * ``UV`` UV, Use UV coordinates for texture coordinates.
      * ``ORCO`` Generated, Use the original undeformed coordinates of the object.
      * ``STRAND`` Strand / Particle, Use normalized strand texture coordinate (1D) or particle age (X) and trail position (Y).
      * ``WINDOW`` Window, Use screen coordinates as texture coordinates.
      * ``NORMAL`` Normal, Use normal vector as texture coordinates.
      * ``REFLECTION`` Reflection, Use reflection vector as texture coordinates.
      * ``STRESS`` Stress, Use the difference of edge lengths compared to original coordinates of the mesh.
      * ``TANGENT`` Tangent, Use the optional tangent vector as texture coordinates.

      :type: enum in ['GLOBAL', 'OBJECT', 'UV', 'ORCO', 'STRAND', 'WINDOW', 'NORMAL', 'REFLECTION', 'STRESS', 'TANGENT'], default 'GLOBAL'

   .. attribute:: translucency_factor

      Amount texture affects translucency

      :type: float in [-inf, inf], default 0.0

   .. attribute:: transmission_color_factor

      Amount texture affects result color after light has been scattered/absorbed

      :type: float in [-inf, inf], default 0.0

   .. attribute:: use

      Enable this material texture slot

      :type: boolean, default False

   .. attribute:: use_from_dupli

      Dupli's instanced from verts, faces or particles, inherit texture coordinate from their parent

      :type: boolean, default False

   .. attribute:: use_from_original

      Dupli's derive their object coordinates from the original object's transformation

      :type: boolean, default False

   .. attribute:: use_map_alpha

      The texture affects the alpha value

      :type: boolean, default False

   .. attribute:: use_map_ambient

      The texture affects the value of ambient

      :type: boolean, default False

   .. attribute:: use_map_color_diffuse

      The texture affects basic color of the material

      :type: boolean, default False

   .. attribute:: use_map_color_emission

      The texture affects the color of emission

      :type: boolean, default False

   .. attribute:: use_map_color_reflection

      The texture affects the color of scattered light

      :type: boolean, default False

   .. attribute:: use_map_color_spec

      The texture affects the specularity color

      :type: boolean, default False

   .. attribute:: use_map_color_transmission

      The texture affects the result color after other light has been scattered/absorbed

      :type: boolean, default False

   .. attribute:: use_map_density

      The texture affects the volume's density

      :type: boolean, default False

   .. attribute:: use_map_diffuse

      The texture affects the value of diffuse reflectivity

      :type: boolean, default False

   .. attribute:: use_map_displacement

      Let the texture displace the surface

      :type: boolean, default False

   .. attribute:: use_map_emission

      The texture affects the volume's emission

      :type: boolean, default False

   .. attribute:: use_map_emit

      The texture affects the emit value

      :type: boolean, default False

   .. attribute:: use_map_hardness

      The texture affects the hardness value

      :type: boolean, default False

   .. attribute:: use_map_mirror

      The texture affects the mirror color

      :type: boolean, default False

   .. attribute:: use_map_normal

      The texture affects the rendered normal

      :type: boolean, default False

   .. attribute:: use_map_parallax

      The texture affects the relief depth

      :type: boolean, default False

   .. attribute:: use_map_raymir

      The texture affects the ray-mirror value

      :type: boolean, default False

   .. attribute:: use_map_reflect

      The texture affects the reflected light's brightness

      :type: boolean, default False

   .. attribute:: use_map_scatter

      The texture affects the volume's scattering

      :type: boolean, default False

   .. attribute:: use_map_specular

      The texture affects the value of specular reflectivity

      :type: boolean, default False

   .. attribute:: use_map_to_bounds

      Map coordinates in object bounds

      :type: boolean, default False

   .. attribute:: use_map_translucency

      The texture affects the translucency value

      :type: boolean, default False

   .. attribute:: use_map_warp

      Let the texture warp texture coordinates of next channels

      :type: boolean, default False

   .. attribute:: use_parallax_uv

      This is necessary for proper use of the parallax mapping

      :type: boolean, default False

   .. attribute:: uv_layer

      UV map to use for mapping with UV texture coordinates

      :type: string, default "", (never None)

   .. attribute:: warp_factor

      Amount texture affects texture coordinates of next channels

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

   * :mod:`bpy.context.texture_slot`
   * :class:`Material.texture_slots`
   * :class:`MaterialTextureSlots.add`
   * :class:`MaterialTextureSlots.create`


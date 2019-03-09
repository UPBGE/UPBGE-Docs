Material(ID)
============

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Material(ID)

   Material data-block to define the appearance of geometric objects for rendering

   .. attribute:: active_node_material

      Active node material

      :type: :class:`Material`

   .. attribute:: active_texture

      Active texture slot being displayed

      :type: :class:`Texture`

   .. attribute:: active_texture_index

      Index of active texture slot

      :type: int in [0, 17], default 0

   .. attribute:: alpha

      Alpha transparency of the material

      :type: float in [0, 1], default 0.0

   .. attribute:: ambient

      Amount of global ambient color the material receives

      :type: float in [0, 1], default 0.0

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. data:: cycles

      Cycles material settings

      :type: :class:`CyclesMaterialSettings`, (readonly)

   .. attribute:: darkness

      Minnaert darkness

      :type: float in [0, 2], default 0.0

   .. attribute:: depth_transp_factor

      Amount of transparency depending on the depth

      :type: float in [0.001, inf], default 0.0

   .. attribute:: diffuse_color

      Diffuse color of the material

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: diffuse_fresnel

      Power of Fresnel

      :type: float in [0, 5], default 0.0

   .. attribute:: diffuse_fresnel_factor

      Blending factor of Fresnel

      :type: float in [0, 5], default 0.0

   .. attribute:: diffuse_intensity

      Amount of diffuse reflection

      :type: float in [0, 1], default 0.0

   .. data:: diffuse_ramp

      Color ramp used to affect diffuse shading

      :type: :class:`ColorRamp`, (readonly)

   .. attribute:: diffuse_ramp_blend

      Blending method of the ramp and the diffuse color

      :type: enum in ['MIX', 'ADD', 'MULTIPLY', 'SUBTRACT', 'SCREEN', 'DIVIDE', 'DIFFERENCE', 'DARKEN', 'LIGHTEN', 'OVERLAY', 'DODGE', 'BURN', 'HUE', 'SATURATION', 'VALUE', 'COLOR', 'SOFT_LIGHT', 'LINEAR_LIGHT'], default 'MIX'

   .. attribute:: diffuse_ramp_factor

      Blending factor (also uses alpha in Colorband)

      :type: float in [0, 1], default 0.0

   .. attribute:: diffuse_ramp_input

      How the ramp maps on the surface

      :type: enum in ['SHADER', 'ENERGY', 'NORMAL', 'RESULT'], default 'SHADER'

   .. attribute:: diffuse_shader

      * ``LAMBERT`` Lambert, Use a Lambertian shader.
      * ``OREN_NAYAR`` Oren-Nayar, Use an Oren-Nayar shader.
      * ``TOON`` Toon, Use a toon shader.
      * ``MINNAERT`` Minnaert, Use a Minnaert shader.
      * ``FRESNEL`` Fresnel, Use a Fresnel shader.

      :type: enum in ['LAMBERT', 'OREN_NAYAR', 'TOON', 'MINNAERT', 'FRESNEL'], default 'LAMBERT'

   .. attribute:: diffuse_toon_size

      Size of diffuse toon area

      :type: float in [0, 3.14], default 0.0

   .. attribute:: diffuse_toon_smooth

      Smoothness of diffuse toon area

      :type: float in [0, 1], default 0.0

   .. attribute:: emit

      Amount of light to emit

      :type: float in [0, inf], default 0.0

   .. data:: game_settings

      Game material settings

      :type: :class:`MaterialGameSettings`, (readonly, never None)

   .. data:: halo

      Halo settings for the material

      :type: :class:`MaterialHalo`, (readonly, never None)

   .. attribute:: invert_z

      Render material's faces with an inverted Z buffer (scanline only)

      :type: boolean, default False

   .. attribute:: light_group

      Limit lighting to lamps in this Group

      :type: :class:`Group`

   .. attribute:: line_color

      Line color used for Freestyle line rendering

      :type: float array of 4 items in [0, inf], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: line_priority

      The line color of a higher priority is used at material boundaries

      :type: int in [0, 32767], default 0

   .. attribute:: mirror_color

      Mirror color of the material

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. data:: node_tree

      Node tree for node based materials

      :type: :class:`NodeTree`, (readonly)

   .. attribute:: offset_z

      Give faces an artificial offset in the Z buffer for Z transparency

      :type: float in [-inf, inf], default 0.0

   .. attribute:: paint_active_slot

      Index of active texture paint slot

      :type: int in [0, 32767], default 0

   .. attribute:: paint_clone_slot

      Index of clone texture paint slot

      :type: int in [0, 32767], default 0

   .. attribute:: pass_index

      Index number for the "Material Index" render pass

      :type: int in [0, 32767], default 0

   .. attribute:: preview_render_type

      Type of preview render

      * ``FLAT`` Flat, Flat XY plane.
      * ``SPHERE`` Sphere, Sphere.
      * ``CUBE`` Cube, Cube.
      * ``MONKEY`` Monkey, Monkey.
      * ``HAIR`` Hair, Hair strands.
      * ``SPHERE_A`` World Sphere, Large sphere with sky.

      :type: enum in ['FLAT', 'SPHERE', 'CUBE', 'MONKEY', 'HAIR', 'SPHERE_A'], default 'FLAT'

   .. data:: raytrace_mirror

      Raytraced reflection settings for the material

      :type: :class:`MaterialRaytraceMirror`, (readonly, never None)

   .. data:: raytrace_transparency

      Raytraced transparency settings for the material

      :type: :class:`MaterialRaytraceTransparency`, (readonly, never None)

   .. attribute:: roughness

      Oren-Nayar Roughness

      :type: float in [0, 3.14], default 0.0

   .. attribute:: shadow_buffer_bias

      Factor to multiply shadow buffer bias with (0 is ignore)

      :type: float in [0, 10], default 0.0

   .. attribute:: shadow_cast_alpha

      Shadow casting alpha, in use for Irregular and Deep shadow buffer

      :type: float in [0.001, 1], default 0.0

   .. attribute:: shadow_only_type

      How to draw shadows

      * ``SHADOW_ONLY_OLD`` Shadow and Distance, Old shadow only method.
      * ``SHADOW_ONLY`` Shadow Only, Improved shadow only method.
      * ``SHADOW_ONLY_SHADED`` Shadow and Shading, Improved shadow only method which also renders lightless areas as shadows.

      :type: enum in ['SHADOW_ONLY_OLD', 'SHADOW_ONLY', 'SHADOW_ONLY_SHADED'], default 'SHADOW_ONLY_OLD'

   .. attribute:: shadow_ray_bias

      Shadow raytracing bias to prevent terminator problems on shadow boundary

      :type: float in [0, 0.25], default 0.0

   .. attribute:: specular_alpha

      Alpha transparency for specular areas

      :type: float in [0, 1], default 0.0

   .. attribute:: specular_color

      Specular color of the material

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: specular_hardness

      How hard (sharp) the specular reflection is

      :type: int in [1, 511], default 0

   .. attribute:: specular_intensity

      How intense (bright) the specular reflection is

      :type: float in [0, 1], default 0.0

   .. attribute:: specular_ior

      Specular index of refraction

      :type: float in [1, 10], default 0.0

   .. data:: specular_ramp

      Color ramp used to affect specular shading

      :type: :class:`ColorRamp`, (readonly)

   .. attribute:: specular_ramp_blend

      Blending method of the ramp and the specular color

      :type: enum in ['MIX', 'ADD', 'MULTIPLY', 'SUBTRACT', 'SCREEN', 'DIVIDE', 'DIFFERENCE', 'DARKEN', 'LIGHTEN', 'OVERLAY', 'DODGE', 'BURN', 'HUE', 'SATURATION', 'VALUE', 'COLOR', 'SOFT_LIGHT', 'LINEAR_LIGHT'], default 'MIX'

   .. attribute:: specular_ramp_factor

      Blending factor (also uses alpha in Colorband)

      :type: float in [0, 1], default 0.0

   .. attribute:: specular_ramp_input

      How the ramp maps on the surface

      :type: enum in ['SHADER', 'ENERGY', 'NORMAL', 'RESULT'], default 'SHADER'

   .. attribute:: specular_shader

      * ``COOKTORR`` CookTorr, Use a Cook-Torrance shader.
      * ``PHONG`` Phong, Use a Phong shader.
      * ``BLINN`` Blinn, Use a Blinn shader.
      * ``TOON`` Toon, Use a toon shader.
      * ``WARDISO`` WardIso, Use a Ward anisotropic shader.

      :type: enum in ['COOKTORR', 'PHONG', 'BLINN', 'TOON', 'WARDISO'], default 'COOKTORR'

   .. attribute:: specular_slope

      The standard deviation of surface slope

      :type: float in [0, 0.4], default 0.0

   .. attribute:: specular_toon_size

      Size of specular toon area

      :type: float in [0, 1.53], default 0.0

   .. attribute:: specular_toon_smooth

      Smoothness of specular toon area

      :type: float in [0, 1], default 0.0

   .. data:: strand

      Strand settings for the material

      :type: :class:`MaterialStrand`, (readonly, never None)

   .. data:: subsurface_scattering

      Subsurface scattering settings for the material

      :type: :class:`MaterialSubsurfaceScattering`, (readonly, never None)

   .. data:: texture_paint_images

      Texture images used for texture painting

      :type: :class:`bpy_prop_collection` of :class:`Image`, (readonly)

   .. data:: texture_paint_slots

      Texture slots defining the mapping and influence of textures

      :type: :class:`bpy_prop_collection` of :class:`TexPaintSlot`, (readonly)

   .. data:: texture_slots

      Texture slots defining the mapping and influence of textures

      :type: :class:`MaterialTextureSlots` :class:`bpy_prop_collection` of :class:`MaterialTextureSlot`, (readonly)

   .. attribute:: translucency

      Amount of diffuse shading on the back side

      :type: float in [0, 1], default 0.0

   .. attribute:: transparency_method

      Method to use for rendering transparency

      * ``MASK`` Mask, Mask the background.
      * ``Z_TRANSPARENCY`` Z Transparency, Use alpha buffer for transparent faces.
      * ``RAYTRACE`` Raytrace, Use raytracing for transparent refraction rendering.

      :type: enum in ['MASK', 'Z_TRANSPARENCY', 'RAYTRACE'], default 'MASK'

   .. attribute:: type

      Material type defining how the object is rendered

      * ``SURFACE`` Surface, Render object as a surface.
      * ``WIRE`` Wire, Render the edges of faces as wires (not supported in raytracing).
      * ``VOLUME`` Volume, Render object as a volume.
      * ``HALO`` Halo, Render object as halo particles.

      :type: enum in ['SURFACE', 'WIRE', 'VOLUME', 'HALO'], default 'SURFACE'

   .. attribute:: use_cast_approximate

      Allow this material to cast shadows when using approximate ambient occlusion

      :type: boolean, default False

   .. attribute:: use_cast_buffer_shadows

      Allow this material to cast shadows from shadow buffer lamps

      :type: boolean, default False

   .. attribute:: use_cast_shadows

      Allow this material to cast shadows

      :type: boolean, default False

   .. attribute:: use_cast_shadows_only

      Make objects with this material appear invisible (not rendered), only casting shadows

      :type: boolean, default False

   .. attribute:: use_constant_lamp

      Use constant values for lamps

      :type: boolean, default False

   .. attribute:: use_constant_material

      Use constant values for material

      :type: boolean, default False

   .. attribute:: use_constant_mist

      Use constant values for mist

      :type: boolean, default False

   .. attribute:: use_constant_texture

      Use constant values for textures

      :type: boolean, default False

   .. attribute:: use_constant_texture_uv

      Use constant values for textures uv transformation

      :type: boolean, default False

   .. attribute:: use_constant_world

      Use constant values for world

      :type: boolean, default False

   .. attribute:: use_cubic

      Use cubic interpolation for diffuse values, for smoother transitions

      :type: boolean, default False

   .. attribute:: use_depth_transparency

      Render material as transparent depending on the depth

      :type: boolean, default False

   .. attribute:: use_diffuse_ramp

      Toggle diffuse ramp operations

      :type: boolean, default False

   .. attribute:: use_face_texture

      Replace the object's base color with color from UV map image textures

      :type: boolean, default False

   .. attribute:: use_face_texture_alpha

      Replace the object's base alpha value with alpha from UV map image textures

      :type: boolean, default False

   .. attribute:: use_full_oversampling

      Force this material to render full shading/textures for all anti-aliasing samples

      :type: boolean, default False

   .. attribute:: use_instancing

      Use special vertex shader for instancing rendering in game engine

      :type: boolean, default False

   .. attribute:: use_light_group_exclusive

      Material uses the light group exclusively - these lamps are excluded from other scene lighting

      :type: boolean, default False

   .. attribute:: use_light_group_local

      When linked in, material uses local light group with the same name

      :type: boolean, default False

   .. attribute:: use_mist

      Use mist with this material (in world settings)

      :type: boolean, default False

   .. attribute:: use_nodes

      Use shader nodes to render the material

      :type: boolean, default False

   .. attribute:: use_object_color

      Modulate the result with a per-object color

      :type: boolean, default False

   .. attribute:: use_only_shadow

      Render shadows as the material's alpha value, making the material transparent except for shadowed areas

      :type: boolean, default False

   .. attribute:: use_ray_shadow_bias

      Prevent raytraced shadow errors on surfaces with smooth shaded normals (terminator problem)

      :type: boolean, default False

   .. attribute:: use_raytrace

      Include this material and geometry that uses it in raytracing calculations

      :type: boolean, default False

   .. attribute:: use_shadeless

      Make this material insensitive to light or shadow

      :type: boolean, default False

   .. attribute:: use_shadows

      Allow this material to receive shadows

      :type: boolean, default False

   .. attribute:: use_sky

      Render this material with zero alpha, with sky background in place (scanline only)

      :type: boolean, default False

   .. attribute:: use_specular_ramp

      Toggle specular ramp operations

      :type: boolean, default False

   .. attribute:: use_tangent_shading

      Use the material's tangent vector instead of the normal for shading - for anisotropic shading effects

      :type: boolean, default False

   .. attribute:: use_textures

      Enable/Disable each texture

      :type: boolean array of 18 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

   .. attribute:: use_transparency

      Render material as transparent

      :type: boolean, default False

   .. attribute:: use_transparent_shadows

      Allow this object to receive transparent shadows cast through other objects

      :type: boolean, default False

   .. attribute:: use_uv_project

      Use to ensure UV interpolation is correct for camera projections (use with UV project modifier)

      :type: boolean, default False

   .. attribute:: use_vertex_color_light

      Add vertex colors as additional lighting

      :type: boolean, default False

   .. attribute:: use_vertex_color_paint

      Replace object base color with vertex colors (multiply with 'texture face' face assigned textures)

      :type: boolean, default False

   .. data:: volume

      Volume settings for the material

      :type: :class:`MaterialVolume`, (readonly, never None)

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

.. rubric:: References

.. hlist::
   :columns: 2

   * :mod:`bpy.context.material`
   * :class:`BlendData.materials`
   * :class:`BlendDataMaterials.new`
   * :class:`BlendDataMaterials.remove`
   * :class:`Curve.materials`
   * :class:`DynamicPaintBrushSettings.material`
   * :class:`IDMaterials.append`
   * :class:`IDMaterials.pop`
   * :class:`Material.active_node_material`
   * :class:`MaterialSlot.material`
   * :class:`Mesh.materials`
   * :class:`MetaBall.materials`
   * :class:`Object.active_material`
   * :class:`RenderLayer.material_override`
   * :class:`SceneRenderLayer.material_override`
   * :class:`ShaderNodeExtendedMaterial.material`
   * :class:`ShaderNodeMaterial.material`


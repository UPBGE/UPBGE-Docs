SceneRenderLayer(bpy_struct)
============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SceneRenderLayer(bpy_struct)

   Render layer

   .. data:: cycles

      Cycles SceneRenderLayer Settings

      :type: :class:`CyclesRenderLayerSettings`, (readonly)

   .. attribute:: exclude_ambient_occlusion

      Exclude AO pass from combined

      :type: boolean, default False

   .. attribute:: exclude_emit

      Exclude emission pass from combined

      :type: boolean, default False

   .. attribute:: exclude_environment

      Exclude environment pass from combined

      :type: boolean, default False

   .. attribute:: exclude_indirect

      Exclude indirect pass from combined

      :type: boolean, default False

   .. attribute:: exclude_reflection

      Exclude raytraced reflection pass from combined

      :type: boolean, default False

   .. attribute:: exclude_refraction

      Exclude raytraced refraction pass from combined

      :type: boolean, default False

   .. attribute:: exclude_shadow

      Exclude shadow pass from combined

      :type: boolean, default False

   .. attribute:: exclude_specular

      Exclude specular pass from combined

      :type: boolean, default False

   .. data:: freestyle_settings

      :type: :class:`FreestyleSettings`, (readonly, never None)

   .. attribute:: invert_zmask

      For Zmask, only render what is behind solid z values instead of in front

      :type: boolean, default False

   .. attribute:: layers

      Scene layers included in this render layer

      :type: boolean array of 20 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

   .. attribute:: layers_exclude

      Exclude scene layers from having any influence

      :type: boolean array of 20 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

   .. attribute:: layers_zmask

      Zmask scene layers for solid faces

      :type: boolean array of 20 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

   .. attribute:: light_override

      Group to override all other lights in this render layer

      :type: :class:`Group`

   .. attribute:: material_override

      Material to override all other materials in this render layer

      :type: :class:`Material`

   .. attribute:: name

      Render layer name

      :type: string, default "", (never None)

   .. attribute:: pass_alpha_threshold

      Z, Index, normal, UV and vector passes are only affected by surfaces with alpha transparency equal to or higher than this threshold

      :type: float in [0, 1], default 0.0

   .. attribute:: samples

      Override number of render samples for this render layer, 0 will use the scene setting

      :type: int in [0, inf], default 0

   .. attribute:: use

      Disable or enable the render layer

      :type: boolean, default False

   .. attribute:: use_all_z

      Fill in Z values for solid faces in invisible layers, for masking

      :type: boolean, default False

   .. attribute:: use_ao

      Render AO in this Layer

      :type: boolean, default False

   .. attribute:: use_edge_enhance

      Render Edge-enhance in this Layer (only works for Solid faces)

      :type: boolean, default False

   .. attribute:: use_freestyle

      Render stylized strokes in this Layer

      :type: boolean, default False

   .. attribute:: use_halo

      Render Halos in this Layer (on top of Solid)

      :type: boolean, default False

   .. attribute:: use_pass_ambient_occlusion

      Deliver AO pass

      :type: boolean, default False

   .. attribute:: use_pass_color

      Deliver shade-less color pass

      :type: boolean, default False

   .. attribute:: use_pass_combined

      Deliver full combined RGBA buffer

      :type: boolean, default False

   .. attribute:: use_pass_diffuse

      Deliver diffuse pass

      :type: boolean, default False

   .. attribute:: use_pass_diffuse_color

      Deliver diffuse color pass

      :type: boolean, default False

   .. attribute:: use_pass_diffuse_direct

      Deliver diffuse direct pass

      :type: boolean, default False

   .. attribute:: use_pass_diffuse_indirect

      Deliver diffuse indirect pass

      :type: boolean, default False

   .. attribute:: use_pass_emit

      Deliver emission pass

      :type: boolean, default False

   .. attribute:: use_pass_environment

      Deliver environment lighting pass

      :type: boolean, default False

   .. attribute:: use_pass_glossy_color

      Deliver glossy color pass

      :type: boolean, default False

   .. attribute:: use_pass_glossy_direct

      Deliver glossy direct pass

      :type: boolean, default False

   .. attribute:: use_pass_glossy_indirect

      Deliver glossy indirect pass

      :type: boolean, default False

   .. attribute:: use_pass_indirect

      Deliver indirect lighting pass

      :type: boolean, default False

   .. attribute:: use_pass_material_index

      Deliver material index pass

      :type: boolean, default False

   .. attribute:: use_pass_mist

      Deliver mist factor pass (0.0-1.0)

      :type: boolean, default False

   .. attribute:: use_pass_normal

      Deliver normal pass

      :type: boolean, default False

   .. attribute:: use_pass_object_index

      Deliver object index pass

      :type: boolean, default False

   .. attribute:: use_pass_reflection

      Deliver raytraced reflection pass

      :type: boolean, default False

   .. attribute:: use_pass_refraction

      Deliver raytraced refraction pass

      :type: boolean, default False

   .. attribute:: use_pass_shadow

      Deliver shadow pass

      :type: boolean, default False

   .. attribute:: use_pass_specular

      Deliver specular pass

      :type: boolean, default False

   .. attribute:: use_pass_subsurface_color

      Deliver subsurface color pass

      :type: boolean, default False

   .. attribute:: use_pass_subsurface_direct

      Deliver subsurface direct pass

      :type: boolean, default False

   .. attribute:: use_pass_subsurface_indirect

      Deliver subsurface indirect pass

      :type: boolean, default False

   .. attribute:: use_pass_transmission_color

      Deliver transmission color pass

      :type: boolean, default False

   .. attribute:: use_pass_transmission_direct

      Deliver transmission direct pass

      :type: boolean, default False

   .. attribute:: use_pass_transmission_indirect

      Deliver transmission indirect pass

      :type: boolean, default False

   .. attribute:: use_pass_uv

      Deliver texture UV pass

      :type: boolean, default False

   .. attribute:: use_pass_vector

      Deliver speed vector pass

      :type: boolean, default False

   .. attribute:: use_pass_z

      Deliver Z values pass

      :type: boolean, default False

   .. attribute:: use_sky

      Render Sky in this Layer

      :type: boolean, default False

   .. attribute:: use_solid

      Render Solid faces in this Layer

      :type: boolean, default False

   .. attribute:: use_strand

      Render Strands in this Layer

      :type: boolean, default False

   .. attribute:: use_zmask

      Only render what's in front of the solid z values

      :type: boolean, default False

   .. attribute:: use_ztransp

      Render Z-Transparent faces in this Layer (on top of Solid and Halos)

      :type: boolean, default False

   .. classmethod:: update_render_passes()

      Requery the enabled render passes from the render engine


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

   * :class:`RenderEngine.register_pass`
   * :class:`RenderEngine.update_render_passes`
   * :class:`RenderLayers.active`
   * :class:`RenderLayers.new`
   * :class:`RenderLayers.remove`
   * :class:`RenderSettings.layers`


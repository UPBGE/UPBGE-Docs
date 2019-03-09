TextureSlot(bpy_struct)
=======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`BrushTextureSlot`, :class:`LampTextureSlot`, :class:`LineStyleTextureSlot`, :class:`MaterialTextureSlot`, :class:`ParticleSettingsTextureSlot`, :class:`WorldTextureSlot`

.. class:: TextureSlot(bpy_struct)

   Texture slot defining the mapping and influence of a texture

   .. attribute:: blend_type

      Mode used to apply the texture

      :type: enum in ['MIX', 'ADD', 'SUBTRACT', 'MULTIPLY', 'SCREEN', 'OVERLAY', 'DIFFERENCE', 'DIVIDE', 'DARKEN', 'LIGHTEN', 'HUE', 'SATURATION', 'VALUE', 'COLOR', 'SOFT_LIGHT', 'LINEAR_LIGHT'], default 'MIX'

   .. attribute:: color

      Default color for textures that don't return RGB or when RGB to intensity is enabled

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: default_value

      Value to use for Ref, Spec, Amb, Emit, Alpha, RayMir, TransLu and Hard

      :type: float in [-inf, inf], default 0.0

   .. attribute:: invert

      Invert the values of the texture to reverse its effect

      :type: boolean, default False

   .. data:: name

      Texture slot name

      :type: string, default "", (readonly, never None)

   .. attribute:: offset

      Fine tune of the texture mapping X, Y and Z locations

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: output_node

      Which output node to use, for node-based textures

      :type: enum in ['DUMMY'], default 'DUMMY'

   .. attribute:: rotation

      Set rotation for the texture

      :type: float in [-inf, inf], default 0.0

   .. attribute:: scale

      Set scaling for the texture's X, Y and Z sizes

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: texture

      Texture data-block used by this texture slot

      :type: :class:`Texture`

   .. attribute:: use_rgb_to_intensity

      Convert texture RGB values to intensity (gray) values

      :type: boolean, default False

   .. attribute:: use_stencil

      Use this texture as a blending value on the next texture

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

   * :class:`UILayout.template_preview`


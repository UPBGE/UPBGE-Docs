LampTextureSlot(TextureSlot)
============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`TextureSlot`

.. class:: LampTextureSlot(TextureSlot)

   Texture slot for textures in a Lamp data-block

   .. attribute:: color_factor

      Amount texture affects color values

      :type: float in [-inf, inf], default 0.0

   .. attribute:: lod_bias

      Amount bias on mipmapping

      :type: float in [-inf, inf], default 0.0

   .. attribute:: object

      Object to use for mapping with Object texture coordinates

      :type: :class:`Object`

   .. attribute:: shadow_factor

      Amount texture affects shadow

      :type: float in [-inf, inf], default 0.0

   .. attribute:: texture_coords

      * ``GLOBAL`` Global, Use global coordinates for the texture coordinates.
      * ``VIEW`` View, Use view coordinates for the texture coordinates.
      * ``OBJECT`` Object, Use linked object's coordinates for texture coordinates.

      :type: enum in ['GLOBAL', 'VIEW', 'OBJECT'], default 'GLOBAL'

   .. attribute:: use_map_color

      Let the texture affect the basic color of the lamp

      :type: boolean, default False

   .. attribute:: use_map_shadow

      Let the texture affect the shadow color of the lamp

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

   * :class:`Lamp.texture_slots`
   * :class:`LampTextureSlots.add`
   * :class:`LampTextureSlots.create`


WorldTextureSlot(TextureSlot)
=============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`TextureSlot`

.. class:: WorldTextureSlot(TextureSlot)

   Texture slot for textures in a World data-block

   .. attribute:: blend_factor

      Amount texture affects color progression of the background

      :type: float in [-inf, inf], default 0.0

   .. attribute:: horizon_factor

      Amount texture affects color of the horizon

      :type: float in [-inf, inf], default 0.0

   .. attribute:: lod_bias

      Amount bias on mipmapping

      :type: float in [-inf, inf], default 0.0

   .. attribute:: object

      Object to use for mapping with Object texture coordinates

      :type: :class:`Object`

   .. attribute:: texture_coords

      Texture coordinates used to map the texture onto the background

      * ``VIEW`` View, Use view vector for the texture coordinates.
      * ``GLOBAL`` Global, Use global coordinates for the texture coordinates (interior mist).
      * ``ANGMAP`` AngMap, Use 360 degree angular coordinates, e.g. for spherical light probes.
      * ``SPHERE`` Sphere, For 360 degree panorama sky, spherical mapped, only top half.
      * ``EQUIRECT`` Equirectangular, For 360 degree panorama sky, equirectangular mapping.
      * ``TUBE`` Tube, For 360 degree panorama sky, cylindrical mapped, only top half.
      * ``OBJECT`` Object, Use linked object's coordinates for texture coordinates.

      :type: enum in ['VIEW', 'GLOBAL', 'ANGMAP', 'SPHERE', 'EQUIRECT', 'TUBE', 'OBJECT'], default 'VIEW'

   .. attribute:: use_map_blend

      Affect the color progression of the background

      :type: boolean, default False

   .. attribute:: use_map_horizon

      Affect the color of the horizon

      :type: boolean, default False

   .. attribute:: use_map_zenith_down

      Affect the color of the zenith below

      :type: boolean, default False

   .. attribute:: use_map_zenith_up

      Affect the color of the zenith above

      :type: boolean, default False

   .. attribute:: zenith_down_factor

      Amount texture affects color of the zenith below

      :type: float in [-inf, inf], default 0.0

   .. attribute:: zenith_up_factor

      Amount texture affects color of the zenith above

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

   * :class:`World.texture_slots`
   * :class:`WorldTextureSlots.add`
   * :class:`WorldTextureSlots.create`


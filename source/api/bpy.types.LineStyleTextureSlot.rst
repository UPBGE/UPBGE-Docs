LineStyleTextureSlot(TextureSlot)
=================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`TextureSlot`

.. class:: LineStyleTextureSlot(TextureSlot)

   Texture slot for textures in a LineStyle data-block

   .. attribute:: alpha_factor

      Amount texture affects alpha

      :type: float in [-inf, inf], default 0.0

   .. attribute:: diffuse_color_factor

      Amount texture affects diffuse color

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

   .. attribute:: texture_coords

      Texture coordinates used to map the texture onto the background

      * ``WINDOW`` Window, Use screen coordinates as texture coordinates.
      * ``GLOBAL`` Global, Use global coordinates for the texture coordinates.
      * ``ALONG_STROKE`` Along stroke, Use stroke length for texture coordinates.
      * ``ORCO`` Generated, Use the original undeformed coordinates of the object.

      :type: enum in ['WINDOW', 'GLOBAL', 'ALONG_STROKE', 'ORCO'], default 'WINDOW'

   .. attribute:: use_map_alpha

      The texture affects the alpha value

      :type: boolean, default False

   .. attribute:: use_map_color_diffuse

      The texture affects basic color of the stroke

      :type: boolean, default False

   .. attribute:: use_tips

      Lower half of the texture is for tips of the stroke

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

   * :class:`FreestyleLineStyle.texture_slots`
   * :class:`LineStyleTextureSlots.add`
   * :class:`LineStyleTextureSlots.create`


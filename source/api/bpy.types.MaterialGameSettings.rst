MaterialGameSettings(bpy_struct)
================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MaterialGameSettings(bpy_struct)

   Game Engine settings for a Material data-block

   .. attribute:: alpha_blend

      Blend Mode for Transparent Faces

      * ``OPAQUE`` Opaque, Render color of textured face as color.
      * ``ADD`` Add, Render face transparent and add color of face.
      * ``CLIP`` Alpha Clip, Use the image alpha values clipped with no blending (binary alpha).
      * ``ALPHA`` Alpha Blend, Render polygon transparent, depending on alpha channel of the texture.
      * ``ALPHA_SORT`` Alpha Sort, Sort faces for correct alpha drawing (slow, use Alpha Clip instead when possible).
      * ``ALPHA_ANTIALIASING`` Alpha Anti-Aliasing, Use textures alpha as anti-aliasing mask, requires multi-sample OpenGL display.

      :type: enum in ['OPAQUE', 'ADD', 'CLIP', 'ALPHA', 'ALPHA_SORT', 'ALPHA_ANTIALIASING'], default 'OPAQUE'

   .. attribute:: face_orientation

      Especial face orientation options

      * ``NORMAL`` Normal, No transformation.
      * ``HALO`` Halo, Screen aligned billboard.
      * ``BILLBOARD`` Billboard, Billboard with Z-axis constraint.
      * ``SHADOW`` Shadow, Faces are used for shadow.

      :type: enum in ['NORMAL', 'HALO', 'BILLBOARD', 'SHADOW'], default 'NORMAL'

   .. attribute:: invisible

      Make face invisible

      :type: boolean, default False

   .. attribute:: physics

      Use physics for this materials

      :type: boolean, default False

   .. attribute:: use_backface_culling

      Hide Back of the face in Game Engine

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

   * :class:`Material.game_settings`


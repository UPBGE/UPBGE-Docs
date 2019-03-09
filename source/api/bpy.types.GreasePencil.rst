GreasePencil(ID)
================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: GreasePencil(ID)

   Freehand annotation sketchbook

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. data:: layers

      :type: :class:`GreasePencilLayers` :class:`bpy_prop_collection` of :class:`GPencilLayer`, (readonly)

   .. data:: palettes

      :type: :class:`GreasePencilPalettes` :class:`bpy_prop_collection` of :class:`GPencilPalette`, (readonly)

   .. attribute:: show_stroke_direction

      Show stroke drawing direction with a bigger green dot (start) and smaller red dot (end) points

      :type: boolean, default False

   .. attribute:: use_onion_skinning

      Show ghosts of the frames before and after the current frame, toggle to enable on active layer or disable all

      :type: boolean, default False

   .. attribute:: use_stroke_edit_mode

      Edit Grease Pencil strokes instead of viewport data

      :type: boolean, default False

   .. method:: clear()

      Remove all the grease pencil data


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

   * :class:`BlendData.grease_pencil`
   * :class:`BlendDataGreasePencils.new`
   * :class:`BlendDataGreasePencils.remove`
   * :class:`MovieClip.grease_pencil`
   * :class:`MovieTrackingTrack.grease_pencil`
   * :class:`NodeTree.grease_pencil`
   * :class:`Object.grease_pencil`
   * :class:`Scene.grease_pencil`
   * :class:`SpaceImageEditor.grease_pencil`
   * :class:`SpaceSequenceEditor.grease_pencil`


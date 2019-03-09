Screen(ID)
==========

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Screen(ID)

   Screen data-block, defining the layout of areas in a window

   .. data:: areas

      Areas the screen is subdivided into

      :type: :class:`bpy_prop_collection` of :class:`Area`, (readonly)

   .. data:: is_animation_playing

      Animation playback is active

      :type: boolean, default False, (readonly)

   .. attribute:: scene

      Active scene to be edited in the screen

      :type: :class:`Scene`, (never None)

   .. data:: show_fullscreen

      An area is maximized, filling this screen

      :type: boolean, default False, (readonly)

   .. attribute:: use_follow

      Follow current frame in editors

      :type: boolean, default False

   .. attribute:: use_play_3d_editors

      :type: boolean, default False

   .. attribute:: use_play_animation_editors

      :type: boolean, default False

   .. attribute:: use_play_clip_editors

      :type: boolean, default False

   .. attribute:: use_play_image_editors

      :type: boolean, default False

   .. attribute:: use_play_node_editors

      :type: boolean, default False

   .. attribute:: use_play_properties_editors

      :type: boolean, default False

   .. attribute:: use_play_sequence_editors

      :type: boolean, default False

   .. attribute:: use_play_top_left_3d_editor

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

   * :class:`BlendData.screens`
   * :class:`Context.screen`
   * :class:`Window.screen`


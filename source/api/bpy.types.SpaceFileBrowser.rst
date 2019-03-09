SpaceFileBrowser(Space)
=======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceFileBrowser(Space)

   File browser space data

   .. data:: active_operator

      :type: :class:`Operator`, (readonly)

   .. data:: bookmarks

      User's bookmarks

      :type: :class:`bpy_prop_collection` of :class:`FileBrowserFSMenuEntry`, (readonly)

   .. attribute:: bookmarks_active

      Index of active bookmark (-1 if none)

      :type: int in [-32768, 32767], default -1

   .. data:: operator

      :type: :class:`Operator`, (readonly)

   .. data:: params

      Parameters and Settings for the Filebrowser

      :type: :class:`FileSelectParams`, (readonly)

   .. data:: recent_folders

      :type: :class:`bpy_prop_collection` of :class:`FileBrowserFSMenuEntry`, (readonly)

   .. attribute:: recent_folders_active

      Index of active recent folder (-1 if none)

      :type: int in [-32768, 32767], default -1

   .. data:: system_bookmarks

      System's bookmarks

      :type: :class:`bpy_prop_collection` of :class:`FileBrowserFSMenuEntry`, (readonly)

   .. attribute:: system_bookmarks_active

      Index of active system bookmark (-1 if none)

      :type: int in [-32768, 32767], default -1

   .. data:: system_folders

      System's folders (usually root, available hard drives, etc)

      :type: :class:`bpy_prop_collection` of :class:`FileBrowserFSMenuEntry`, (readonly)

   .. attribute:: system_folders_active

      Index of active system folder (-1 if none)

      :type: int in [-32768, 32767], default -1

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


   .. function:: draw_handler_add()

      Undocumented
   .. function:: draw_handler_remove()

      Undocumented
.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Space.type`
   * :class:`Space.show_locked_time`

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


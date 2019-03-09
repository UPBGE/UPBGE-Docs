SpaceOutliner(Space)
====================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceOutliner(Space)

   Outliner space data

   .. attribute:: display_mode

      Type of information to display

      * ``ALL_SCENES`` All Scenes, Display data-blocks in all scenes.
      * ``CURRENT_SCENE`` Current Scene, Display data-blocks in current scene.
      * ``VISIBLE_LAYERS`` Visible Layers, Display data-blocks in visible layers.
      * ``SELECTED`` Selected, Display data-blocks of selected, visible objects.
      * ``ACTIVE`` Active, Display data-blocks of active object.
      * ``SAME_TYPES`` Same Types, Display data-blocks of all objects of same type as selected object.
      * ``GROUPS`` Groups, Display groups and their data-blocks.
      * ``SEQUENCE`` Sequence, Display sequence data-blocks.
      * ``LIBRARIES`` Blender File, Display data of current file and linked libraries.
      * ``DATABLOCKS`` Data-Blocks, Display all raw data-blocks.
      * ``USER_PREFERENCES`` User Preferences, Display user preference data.
      * ``ORPHAN_DATA`` Orphan Data, Display data-blocks which are unused and/or will be lost when the file is reloaded.

      :type: enum in ['ALL_SCENES', 'CURRENT_SCENE', 'VISIBLE_LAYERS', 'SELECTED', 'ACTIVE', 'SAME_TYPES', 'GROUPS', 'SEQUENCE', 'LIBRARIES', 'DATABLOCKS', 'USER_PREFERENCES', 'ORPHAN_DATA'], default 'ALL_SCENES'

   .. attribute:: filter_text

      Live search filtering string

      :type: string, default "", (never None)

   .. attribute:: show_restrict_columns

      Show column

      :type: boolean, default False

   .. attribute:: use_filter_case_sensitive

      Only use case sensitive matches of search string

      :type: boolean, default False

   .. attribute:: use_filter_complete

      Only use complete matches of search string

      :type: boolean, default False

   .. attribute:: use_sort_alpha

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


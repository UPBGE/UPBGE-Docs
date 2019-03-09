KeyMap(bpy_struct)
==================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: KeyMap(bpy_struct)

   Input configuration, including keymaps

   .. data:: is_modal

      Indicates that a keymap is used for translate modal events for an operator

      :type: boolean, default False, (readonly)

   .. attribute:: is_user_modified

      Keymap is defined by the user

      :type: boolean, default False

   .. data:: keymap_items

      Items in the keymap, linking an operator to an input event

      :type: :class:`KeyMapItems` :class:`bpy_prop_collection` of :class:`KeyMapItem`, (readonly)

   .. data:: name

      Name of the key map

      :type: string, default "", (readonly, never None)

   .. data:: region_type

      Optional region type keymap is associated with

      :type: enum in ['WINDOW', 'HEADER', 'CHANNELS', 'TEMPORARY', 'UI', 'TOOLS', 'TOOL_PROPS', 'PREVIEW'], default 'WINDOW', (readonly)

   .. attribute:: show_expanded_children

      Children expanded in the user interface

      :type: boolean, default False

   .. attribute:: show_expanded_items

      Expanded in the user interface

      :type: boolean, default False

   .. data:: space_type

      Optional space type keymap is associated with

      * ``EMPTY`` Empty.
      * ``VIEW_3D`` 3D View, 3D viewport.
      * ``TIMELINE`` Timeline, Timeline and playback controls.
      * ``GRAPH_EDITOR`` Graph Editor, Edit drivers and keyframe interpolation.
      * ``DOPESHEET_EDITOR`` Dope Sheet, Adjust timing of keyframes.
      * ``NLA_EDITOR`` NLA Editor, Combine and layer Actions.
      * ``IMAGE_EDITOR`` UV/Image Editor, View and edit images and UV Maps.
      * ``CLIP_EDITOR`` Movie Clip Editor, Motion tracking tools.
      * ``SEQUENCE_EDITOR`` Video Sequence Editor, Video editing tools.
      * ``NODE_EDITOR`` Node Editor, Editor for node-based shading and compositing tools.
      * ``TEXT_EDITOR`` Text Editor, Edit scripts and in-file documentation.
      * ``LOGIC_EDITOR`` Logic Editor, Game logic editing.
      * ``PROPERTIES`` Properties, Edit properties of active object and related data-blocks.
      * ``OUTLINER`` Outliner, Overview of scene graph and all available data-blocks.
      * ``USER_PREFERENCES`` User Preferences, Edit persistent configuration settings.
      * ``INFO`` Info, Main menu bar and list of error messages (drag down to expand and display).
      * ``FILE_BROWSER`` File Browser, Browse for files and assets.
      * ``CONSOLE`` Python Console, Interactive programmatic console for advanced editing and script development.

      :type: enum in ['EMPTY', 'VIEW_3D', 'TIMELINE', 'GRAPH_EDITOR', 'DOPESHEET_EDITOR', 'NLA_EDITOR', 'IMAGE_EDITOR', 'CLIP_EDITOR', 'SEQUENCE_EDITOR', 'NODE_EDITOR', 'TEXT_EDITOR', 'LOGIC_EDITOR', 'PROPERTIES', 'OUTLINER', 'USER_PREFERENCES', 'INFO', 'FILE_BROWSER', 'CONSOLE'], default 'EMPTY', (readonly)

   .. method:: active()

      active

      :return:

         Key Map, Active key map

      :rtype: :class:`KeyMap`

   .. method:: restore_to_default()

      restore_to_default


   .. method:: restore_item_to_default(item)

      restore_item_to_default

      :arg item:

         Item

      :type item: :class:`KeyMapItem`, (never None)

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

   * :class:`KeyConfig.keymaps`
   * :class:`KeyMap.active`
   * :class:`KeyMaps.find`
   * :class:`KeyMaps.find_modal`
   * :class:`KeyMaps.new`
   * :class:`KeyMaps.remove`


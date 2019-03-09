Area(bpy_struct)
================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Area(bpy_struct)

   Area in a subdivided screen, containing an editor

   .. data:: height

      Area height

      :type: int in [0, 32767], default 0, (readonly)

   .. data:: regions

      Regions this area is subdivided in

      :type: :class:`bpy_prop_collection` of :class:`Region`, (readonly)

   .. attribute:: show_menus

      Show menus in the header

      :type: boolean, default False

   .. data:: spaces

      Spaces contained in this area, the first being the active space (NOTE: Useful for example to restore a previously used 3D view space in a certain area to get the old view orientation)

      :type: :class:`AreaSpaces` :class:`bpy_prop_collection` of :class:`Space`, (readonly)

   .. attribute:: type

      Current editor type for this area

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

      :type: enum in ['EMPTY', 'VIEW_3D', 'TIMELINE', 'GRAPH_EDITOR', 'DOPESHEET_EDITOR', 'NLA_EDITOR', 'IMAGE_EDITOR', 'CLIP_EDITOR', 'SEQUENCE_EDITOR', 'NODE_EDITOR', 'TEXT_EDITOR', 'LOGIC_EDITOR', 'PROPERTIES', 'OUTLINER', 'USER_PREFERENCES', 'INFO', 'FILE_BROWSER', 'CONSOLE'], default 'VIEW_3D'

   .. data:: width

      Area width

      :type: int in [0, 32767], default 0, (readonly)

   .. data:: x

      The window relative vertical location of the area

      :type: int in [-inf, inf], default 0, (readonly)

   .. data:: y

      The window relative horizontal location of the area

      :type: int in [-inf, inf], default 0, (readonly)

   .. method:: tag_redraw()

      tag_redraw


   .. method:: header_text_set(text="")

      Set the header text

      :arg text:

         Text, New string for the header, no argument clears the text

      :type text: string, (optional, never None)

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

   * :class:`Context.area`
   * :class:`Screen.areas`


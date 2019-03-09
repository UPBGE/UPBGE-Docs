Theme(bpy_struct)
=================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Theme(bpy_struct)

   Theme settings defining draw style and colors in the user interface

   .. data:: bone_color_sets

      :type: :class:`bpy_prop_collection` of :class:`ThemeBoneColorSet`, (readonly, never None)

   .. data:: clip_editor

      :type: :class:`ThemeClipEditor`, (readonly, never None)

   .. data:: console

      :type: :class:`ThemeConsole`, (readonly, never None)

   .. data:: dopesheet_editor

      :type: :class:`ThemeDopeSheet`, (readonly, never None)

   .. data:: file_browser

      :type: :class:`ThemeFileBrowser`, (readonly, never None)

   .. data:: graph_editor

      :type: :class:`ThemeGraphEditor`, (readonly, never None)

   .. data:: image_editor

      :type: :class:`ThemeImageEditor`, (readonly, never None)

   .. data:: info

      :type: :class:`ThemeInfo`, (readonly, never None)

   .. data:: logic_editor

      :type: :class:`ThemeLogicEditor`, (readonly, never None)

   .. attribute:: name

      Name of the theme

      :type: string, default "", (never None)

   .. data:: nla_editor

      :type: :class:`ThemeNLAEditor`, (readonly, never None)

   .. data:: node_editor

      :type: :class:`ThemeNodeEditor`, (readonly, never None)

   .. data:: outliner

      :type: :class:`ThemeOutliner`, (readonly, never None)

   .. data:: properties

      :type: :class:`ThemeProperties`, (readonly, never None)

   .. data:: sequence_editor

      :type: :class:`ThemeSequenceEditor`, (readonly, never None)

   .. data:: text_editor

      :type: :class:`ThemeTextEditor`, (readonly, never None)

   .. attribute:: theme_area

      :type: enum in ['USER_INTERFACE', 'STYLE', 'BONE_COLOR_SETS', 'VIEW_3D', 'TIMELINE', 'GRAPH_EDITOR', 'DOPESHEET_EDITOR', 'NLA_EDITOR', 'IMAGE_EDITOR', 'SEQUENCE_EDITOR', 'TEXT_EDITOR', 'NODE_EDITOR', 'LOGIC_EDITOR', 'PROPERTIES', 'OUTLINER', 'USER_PREFERENCES', 'INFO', 'FILE_BROWSER', 'CONSOLE', 'CLIP_EDITOR'], default 'USER_INTERFACE'

   .. data:: timeline

      :type: :class:`ThemeTimeline`, (readonly, never None)

   .. data:: user_interface

      :type: :class:`ThemeUserInterface`, (readonly, never None)

   .. data:: user_preferences

      :type: :class:`ThemeUserPreferences`, (readonly, never None)

   .. data:: view_3d

      :type: :class:`ThemeView3D`, (readonly, never None)

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

   * :class:`UserPreferences.themes`


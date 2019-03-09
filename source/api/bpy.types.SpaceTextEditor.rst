SpaceTextEditor(Space)
======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceTextEditor(Space)

   Text editor space data

   .. attribute:: find_text

      Text to search for with the find tool

      :type: string, default "", (never None)

   .. attribute:: font_size

      Font size to use for displaying the text

      :type: int in [8, 32], default 0

   .. attribute:: margin_column

      Column number to show right margin at

      :type: int in [0, 1024], default 0

   .. attribute:: replace_text

      Text to replace selected text with using the replace tool

      :type: string, default "", (never None)

   .. attribute:: show_line_highlight

      Highlight the current line

      :type: boolean, default False

   .. attribute:: show_line_numbers

      Show line numbers next to the text

      :type: boolean, default False

   .. attribute:: show_margin

      Show right margin

      :type: boolean, default False

   .. attribute:: show_syntax_highlight

      Syntax highlight for scripting

      :type: boolean, default False

   .. attribute:: show_word_wrap

      Wrap words if there is not enough horizontal space

      :type: boolean, default False

   .. attribute:: tab_width

      Number of spaces to display tabs with

      :type: int in [2, 8], default 0

   .. attribute:: text

      Text displayed and edited in this space

      :type: :class:`Text`

   .. attribute:: top

      Top line visible

      :type: int in [0, inf], default 0

   .. attribute:: use_find_all

      Search in all text data-blocks, instead of only the active one

      :type: boolean, default False

   .. attribute:: use_find_wrap

      Search again from the start of the file when reaching the end

      :type: boolean, default False

   .. attribute:: use_live_edit

      Run python while editing

      :type: boolean, default False

   .. attribute:: use_match_case

      Search string is sensitive to uppercase and lowercase letters

      :type: boolean, default False

   .. attribute:: use_overwrite

      Overwrite characters when typing rather than inserting them

      :type: boolean, default False

   .. data:: visible_lines

      Amount of lines that can be visible in current editor

      :type: int in [-inf, inf], default 0, (readonly)

   .. method:: region_location_from_cursor(line, column)

      Retrieve the region position from the given line and character position

      :arg line:

         Line, Line index

      :type line: int in [-inf, inf]
      :arg column:

         Column, Column index

      :type column: int in [-inf, inf]
      :return:

         Region coordinates

      :rtype: int array of 2 items in [-1, inf]

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


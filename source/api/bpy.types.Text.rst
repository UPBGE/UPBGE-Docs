Text(ID)
========

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Text(ID)

   Text data-block referencing an external or packed text file

   .. data:: current_character

      Index of current character in current line, and also start index of character in selection if one exists

      :type: int in [0, inf], default 0, (readonly)

   .. data:: current_line

      Current line, and start line of selection if one exists

      :type: :class:`TextLine`, (readonly, never None)

   .. attribute:: current_line_index

      Index of current TextLine in TextLine collection

      :type: int in [-inf, inf], default 0

   .. attribute:: filepath

      Filename of the text file

      :type: string, default "", (never None)

   .. data:: is_dirty

      Text file has been edited since last save

      :type: boolean, default False, (readonly)

   .. data:: is_in_memory

      Text file is in memory, without a corresponding file on disk

      :type: boolean, default False, (readonly)

   .. data:: is_modified

      Text file on disk is different than the one in memory

      :type: boolean, default False, (readonly)

   .. data:: lines

      Lines of text

      :type: :class:`bpy_prop_collection` of :class:`TextLine`, (readonly)

   .. data:: select_end_character

      Index of character after end of selection in the selection end line

      :type: int in [0, inf], default 0, (readonly)

   .. data:: select_end_line

      End line of selection

      :type: :class:`TextLine`, (readonly, never None)

   .. attribute:: use_module

      Register this text as a module on loading, Text name must end with ".py"

      :type: boolean, default False

   .. attribute:: use_tabs_as_spaces

      Automatically converts all new tabs into spaces

      :type: boolean, default False

   .. data:: users_logic

      Logic bricks that use this text
      (readonly)

   .. method:: clear()

      clear the text block


   .. method:: write(text)

      write text at the cursor location and advance to the end of the text block

      :arg text:

         New text for this data-block

      :type text: string, (never None)

   .. method:: as_string()

      Return the text as a string.

   .. method:: from_string(string)

      Replace text with this string.

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

   * :mod:`bpy.context.edit_text`
   * :class:`BlendData.texts`
   * :class:`BlendDataTexts.load`
   * :class:`BlendDataTexts.new`
   * :class:`BlendDataTexts.remove`
   * :class:`Filter2DActuator.glsl_shader`
   * :class:`FreestyleModuleSettings.script`
   * :class:`NodeFrame.text`
   * :class:`PythonConstraint.text`
   * :class:`PythonController.text`
   * :class:`ShaderNodeScript.script`
   * :class:`SpaceTextEditor.text`


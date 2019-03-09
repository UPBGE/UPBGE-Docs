SpaceConsole(Space)
===================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceConsole(Space)

   Interactive python console

   .. attribute:: font_size

      Font size to use for displaying the text

      :type: int in [8, 32], default 0

   .. data:: history

      Command history

      :type: :class:`bpy_prop_collection` of :class:`ConsoleLine`, (readonly)

   .. attribute:: language

      Command line prompt language

      :type: string, default "", (never None)

   .. attribute:: prompt

      Command line prompt

      :type: string, default "", (never None)

   .. data:: scrollback

      Command output

      :type: :class:`bpy_prop_collection` of :class:`ConsoleLine`, (readonly)

   .. attribute:: select_end

      :type: int in [0, inf], default 0

   .. attribute:: select_start

      :type: int in [0, inf], default 0

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


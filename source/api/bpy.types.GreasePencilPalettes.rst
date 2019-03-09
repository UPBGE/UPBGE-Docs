GreasePencilPalettes(bpy_struct)
================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GreasePencilPalettes(bpy_struct)

   Collection of grease pencil palettes

   .. attribute:: active

      Current active palette

      :type: :class:`GPencilPalette`

   .. attribute:: active_index

      Index of active palette

      :type: int in [0, inf], default 0

   .. method:: new(name, set_active=True)

      Add a new grease pencil palette

      :arg name:

         Name, Name of the palette

      :type name: string, (never None)
      :arg set_active:

         Set Active, Activate the newly created palette

      :type set_active: boolean, (optional)
      :return:

         The newly created palette

      :rtype: :class:`GPencilPalette`

   .. method:: remove(palette)

      Remove a grease pencil palette

      :arg palette:

         The palette to remove

      :type palette: :class:`GPencilPalette`, (never None)

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

   * :class:`GreasePencil.palettes`


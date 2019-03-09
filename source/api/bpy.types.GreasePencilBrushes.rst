GreasePencilBrushes(bpy_struct)
===============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GreasePencilBrushes(bpy_struct)

   Collection of grease pencil brushes

   .. attribute:: active

      Current active brush

      :type: :class:`GPencilBrush`

   .. attribute:: active_index

      Index of active brush

      :type: int in [0, inf], default 0

   .. method:: new(name, set_active=False)

      Add a new grease pencil brush

      :arg name:

         Name, Name of the brush

      :type name: string, (never None)
      :arg set_active:

         Set Active, Set the newly created brush to the active brush

      :type set_active: boolean, (optional)
      :return:

         The newly created brush

      :rtype: :class:`GPencilBrush`

   .. method:: remove(brush)

      Remove a grease pencil brush

      :arg brush:

         The brush to remove

      :type brush: :class:`GPencilBrush`, (never None)

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

   * :class:`ToolSettings.gpencil_brushes`


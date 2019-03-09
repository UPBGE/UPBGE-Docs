GreasePencilLayers(bpy_struct)
==============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GreasePencilLayers(bpy_struct)

   Collection of grease pencil layers

   .. attribute:: active

      Active grease pencil layer

      :type: :class:`GPencilLayer`

   .. attribute:: active_index

      Index of active grease pencil layer

      :type: int in [0, inf], default 0

   .. method:: new(name, set_active=True)

      Add a new grease pencil layer

      :arg name:

         Name, Name of the layer

      :type name: string, (never None)
      :arg set_active:

         Set Active, Set the newly created layer to the active layer

      :type set_active: boolean, (optional)
      :return:

         The newly created layer

      :rtype: :class:`GPencilLayer`

   .. method:: remove(layer)

      Remove a grease pencil layer

      :arg layer:

         The layer to remove

      :type layer: :class:`GPencilLayer`, (never None)

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

   * :class:`GreasePencil.layers`


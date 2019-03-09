NodeLink(bpy_struct)
====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: NodeLink(bpy_struct)

   Link is valid

   .. data:: from_node

      :type: :class:`Node`, (readonly)

   .. data:: from_socket

      :type: :class:`NodeSocket`, (readonly)

   .. data:: is_hidden

      Link is hidden due to invisible sockets

      :type: boolean, default False, (readonly)

   .. attribute:: is_valid

      :type: boolean, default False

   .. data:: to_node

      :type: :class:`Node`, (readonly)

   .. data:: to_socket

      :type: :class:`NodeSocket`, (readonly)

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

   * :class:`Node.insert_link`
   * :class:`Node.internal_links`
   * :class:`NodeLinks.new`
   * :class:`NodeLinks.remove`
   * :class:`NodeTree.links`


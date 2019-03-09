Nodes(bpy_struct)
=================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Nodes(bpy_struct)

   Collection of Nodes

   .. attribute:: active

      Active node in this tree

      :type: :class:`Node`

   .. method:: new(type)

      Add a node to this node tree

      :arg type:

         Type, Type of node to add (Warning: should be same as node.bl_idname, not node.type!)

      :type type: string, (never None)
      :return:

         New node

      :rtype: :class:`Node`

   .. method:: remove(node)

      Remove a node from this node tree

      :arg node:

         The node to remove

      :type node: :class:`Node`, (never None)

   .. method:: clear()

      Remove all nodes from this node tree


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

   * :class:`NodeTree.nodes`


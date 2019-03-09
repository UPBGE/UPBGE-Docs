NodeLinks(bpy_struct)
=====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: NodeLinks(bpy_struct)

   Collection of Node Links

   .. method:: new(input, output, verify_limits=True)

      Add a node link to this node tree

      :arg input:

         The input socket

      :type input: :class:`NodeSocket`, (never None)
      :arg output:

         The output socket

      :type output: :class:`NodeSocket`, (never None)
      :arg verify_limits:

         Verify Limits, Remove existing links if connection limit is exceeded

      :type verify_limits: boolean, (optional)
      :return:

         New node link

      :rtype: :class:`NodeLink`

   .. method:: remove(link)

      remove a node link from the node tree

      :arg link:

         The node link to remove

      :type link: :class:`NodeLink`, (never None)

   .. method:: clear()

      remove all node links from the node tree


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

   * :class:`NodeTree.links`


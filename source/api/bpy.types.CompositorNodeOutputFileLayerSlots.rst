CompositorNodeOutputFileLayerSlots(bpy_struct)
==============================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: CompositorNodeOutputFileLayerSlots(bpy_struct)

   Collection of File Output node slots

   .. method:: new(name)

      Add a file slot to this node

      :arg name:

         Name

      :type name: string, (never None)
      :return:

         New socket

      :rtype: :class:`NodeSocket`

   .. method:: remove(socket)

      Remove a file slot from this node

      :arg socket:

         The socket to remove

      :type socket: :class:`NodeSocket`

   .. method:: clear()

      Remove all file slots from this node


   .. method:: move(from_index, to_index)

      Move a file slot to another position

      :arg from_index:

         From Index, Index of the socket to move

      :type from_index: int in [0, inf]
      :arg to_index:

         To Index, Target index for the socket

      :type to_index: int in [0, inf]

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

   * :class:`CompositorNodeOutputFile.layer_slots`


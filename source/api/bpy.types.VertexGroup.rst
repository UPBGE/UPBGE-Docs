VertexGroup(bpy_struct)
=======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: VertexGroup(bpy_struct)

   Group of vertices, used for armature deform and other purposes

   .. data:: index

      Index number of the vertex group

      :type: int in [0, inf], default 0, (readonly)

   .. attribute:: lock_weight

      Maintain the relative weights for the group

      :type: boolean, default False

   .. attribute:: name

      Vertex group name

      :type: string, default "", (never None)

   .. method:: add(index, weight, type)

      Add vertices to the group

      :arg index:

         Index List

      :type index: int array of 1 items in [-inf, inf]
      :arg weight:

         Vertex weight

      :type weight: float in [0, 1]
      :arg type:

         Vertex assign mode

         * ``REPLACE`` Replace, Replace.
         * ``ADD`` Add, Add.
         * ``SUBTRACT`` Subtract, Subtract.

      :type type: enum in ['REPLACE', 'ADD', 'SUBTRACT']

   .. method:: remove(index)

      Remove a vertex from the group

      :arg index:

         Index List

      :type index: int array of 1 items in [-inf, inf]

   .. method:: weight(index)

      Get a vertex weight from the group

      :arg index:

         Index, The index of the vertex

      :type index: int in [0, inf]
      :return:

         Vertex weight

      :rtype: float in [0, 1]

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

   * :class:`Object.vertex_groups`
   * :class:`VertexGroups.active`
   * :class:`VertexGroups.new`
   * :class:`VertexGroups.remove`


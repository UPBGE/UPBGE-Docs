MeshLoop(bpy_struct)
====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MeshLoop(bpy_struct)

   Loop in a Mesh data-block

   .. data:: bitangent

      Bitangent vector of this vertex for this polygon (must be computed beforehand using calc_tangents, *use it only if really needed*, slower access than bitangent_sign)

      :type: float array of 3 items in [-1, 1], default (0.0, 0.0, 0.0), (readonly)

   .. data:: bitangent_sign

      Sign of the bitangent vector of this vertex for this polygon (must be computed beforehand using calc_tangents, bitangent = bitangent_sign * cross(normal, tangent))

      :type: float in [-1, 1], default 0.0, (readonly)

   .. attribute:: edge_index

      Edge index

      :type: int in [0, inf], default 0

   .. data:: index

      Index of this loop

      :type: int in [0, inf], default 0, (readonly)

   .. attribute:: normal

      Local space unit length split normal vector of this vertex for this polygon (must be computed beforehand using calc_normals_split or calc_tangents)

      :type: float array of 3 items in [-1, 1], default (0.0, 0.0, 0.0)

   .. data:: tangent

      Local space unit length tangent vector of this vertex for this polygon (must be computed beforehand using calc_tangents)

      :type: float array of 3 items in [-1, 1], default (0.0, 0.0, 0.0), (readonly)

   .. attribute:: vertex_index

      Vertex index

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

   * :class:`Mesh.loops`


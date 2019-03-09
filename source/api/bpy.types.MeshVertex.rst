MeshVertex(bpy_struct)
======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MeshVertex(bpy_struct)

   Vertex in a Mesh data-block

   .. attribute:: bevel_weight

      Weight used by the Bevel modifier 'Only Vertices' option

      :type: float in [-inf, inf], default 0.0

   .. attribute:: co

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. data:: groups

      Weights for the vertex groups this vertex is member of

      :type: :class:`bpy_prop_collection` of :class:`VertexGroupElement`, (readonly)

   .. attribute:: hide

      :type: boolean, default False

   .. data:: index

      Index of this vertex

      :type: int in [0, inf], default 0, (readonly)

   .. attribute:: normal

      Vertex Normal

      :type: float array of 3 items in [-1, 1], default (0.0, 0.0, 0.0)

   .. attribute:: select

      :type: boolean, default False

   .. data:: undeformed_co

      For meshes with modifiers applied, the coordinate of the vertex with no deforming modifiers applied, as used for generated texture coordinates

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

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

   * :class:`Mesh.vertices`


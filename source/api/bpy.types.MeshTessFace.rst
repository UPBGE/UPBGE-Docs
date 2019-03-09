MeshTessFace(bpy_struct)
========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MeshTessFace(bpy_struct)

   TessFace in a Mesh data-block

   .. data:: area

      Read only area of this face

      :type: float in [0, inf], default 0.0, (readonly)

   .. attribute:: hide

      :type: boolean, default False

   .. data:: index

      Index of this face

      :type: int in [0, inf], default 0, (readonly)

   .. attribute:: material_index

      :type: int in [0, 32767], default 0

   .. data:: normal

      Local space unit length normal vector for this face

      :type: float array of 3 items in [-1, 1], default (0.0, 0.0, 0.0), (readonly)

   .. attribute:: select

      :type: boolean, default False

   .. data:: split_normals

      Local space unit length split normals vectors of the vertices of this face (must be computed beforehand using calc_normals_split or calc_tangents, and then calc_tessface)

      :type: float multi-dimensional array of 4 * 3 items in [-1, 1], default ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), (readonly)

   .. attribute:: use_smooth

      :type: boolean, default False

   .. attribute:: vertices

      Vertex indices

      :type: int array of 4 items in [0, inf], default (0, 0, 0, 0)

   .. attribute:: vertices_raw

      Fixed size vertex indices array

      :type: int array of 4 items in [0, inf], default (0, 0, 0, 0)

   .. data:: center

      The midpoint of the face.
      (readonly)

   .. data:: edge_keys

      (readonly)

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

   * :class:`Mesh.tessfaces`


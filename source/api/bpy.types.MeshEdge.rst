MeshEdge(bpy_struct)
====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MeshEdge(bpy_struct)

   Edge in a Mesh data-block

   .. attribute:: bevel_weight

      Weight used by the Bevel modifier

      :type: float in [-inf, inf], default 0.0

   .. attribute:: crease

      Weight used by the Subdivision Surface modifier for creasing

      :type: float in [0, 1], default 0.0

   .. attribute:: hide

      :type: boolean, default False

   .. data:: index

      Index of this edge

      :type: int in [0, inf], default 0, (readonly)

   .. attribute:: is_loose

      Loose edge

      :type: boolean, default False

   .. attribute:: select

      :type: boolean, default False

   .. attribute:: use_edge_sharp

      Sharp edge for the Edge Split modifier

      :type: boolean, default False

   .. attribute:: use_freestyle_mark

      Edge mark for Freestyle line rendering

      :type: boolean, default False

   .. attribute:: use_seam

      Seam edge for UV unwrapping

      :type: boolean, default False

   .. attribute:: vertices

      Vertex indices

      :type: int array of 2 items in [0, inf], default (0, 0)

   .. data:: key

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

   * :class:`Mesh.edges`


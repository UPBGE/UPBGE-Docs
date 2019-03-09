MeshPolygon(bpy_struct)
=======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MeshPolygon(bpy_struct)

   Polygon in a Mesh data-block

   .. data:: area

      Read only area of this polygon

      :type: float in [0, inf], default 0.0, (readonly)

   .. data:: center

      Center of this polygon

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. attribute:: hide

      :type: boolean, default False

   .. data:: index

      Index of this polygon

      :type: int in [0, inf], default 0, (readonly)

   .. attribute:: loop_start

      Index of the first loop of this polygon

      :type: int in [0, inf], default 0

   .. attribute:: loop_total

      Number of loops used by this polygon

      :type: int in [0, inf], default 0

   .. attribute:: material_index

      :type: int in [0, 32767], default 0

   .. data:: normal

      Local space unit length normal vector for this polygon

      :type: float array of 3 items in [-1, 1], default (0.0, 0.0, 0.0), (readonly)

   .. attribute:: select

      :type: boolean, default False

   .. attribute:: use_freestyle_mark

      Face mark for Freestyle line rendering

      :type: boolean, default False

   .. attribute:: use_smooth

      :type: boolean, default False

   .. attribute:: vertices

      Vertex indices

      :type: int array of 3 items in [0, inf], default (0, 0, 0)

   .. data:: edge_keys

      (readonly)

   .. data:: loop_indices

      (readonly)

   .. method:: flip()

      Invert winding of this polygon (flip its normal)


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

   * :class:`Mesh.polygons`


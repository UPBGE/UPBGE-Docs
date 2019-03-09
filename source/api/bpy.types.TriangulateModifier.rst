TriangulateModifier(Modifier)
=============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: TriangulateModifier(Modifier)

   Triangulate Mesh

   .. attribute:: ngon_method

      Method for splitting the polygons into triangles

      * ``BEAUTY`` Beauty, Arrange the new triangles evenly (slow).
      * ``CLIP`` Clip, Split the polygons with an ear clipping algorithm.

      :type: enum in ['BEAUTY', 'CLIP'], default 'BEAUTY'

   .. attribute:: quad_method

      Method for splitting the quads into triangles

      * ``BEAUTY`` Beauty , Split the quads in nice triangles, slower method.
      * ``FIXED`` Fixed, Split the quads on the first and third vertices.
      * ``FIXED_ALTERNATE`` Fixed Alternate, Split the quads on the 2nd and 4th vertices.
      * ``SHORTEST_DIAGONAL`` Shortest Diagonal, Split the quads based on the distance between the vertices.

      :type: enum in ['BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL'], default 'BEAUTY'

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
   * :class:`Modifier.name`
   * :class:`Modifier.type`
   * :class:`Modifier.show_viewport`
   * :class:`Modifier.show_render`
   * :class:`Modifier.show_in_editmode`
   * :class:`Modifier.show_on_cage`
   * :class:`Modifier.show_expanded`
   * :class:`Modifier.use_apply_on_spline`

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


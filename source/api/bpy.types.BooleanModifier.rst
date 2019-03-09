BooleanModifier(Modifier)
=========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: BooleanModifier(Modifier)

   Boolean operations modifier

   .. attribute:: debug_options

      Debugging options, only when started with '-d'

      :type: enum set in {'SEPARATE', 'NO_DISSOLVE', 'NO_CONNECT_REGIONS'}, default {'SEPARATE'}

   .. attribute:: double_threshold

      Threshold for checking overlapping geometry

      :type: float in [0, 1], default 0.0

   .. attribute:: object

      Mesh object to use for Boolean operation

      :type: :class:`Object`

   .. attribute:: operation

      * ``INTERSECT`` Intersect, Keep the part of the mesh that intersects with the other selected object.
      * ``UNION`` Union, Combine two meshes in an additive way.
      * ``DIFFERENCE`` Difference, Combine two meshes in a subtractive way.

      :type: enum in ['INTERSECT', 'UNION', 'DIFFERENCE'], default 'INTERSECT'

   .. attribute:: solver

      * ``BMESH`` BMesh, Use the BMesh boolean solver.
      * ``CARVE`` Carve, Use the Carve boolean solver.

      :type: enum in ['BMESH', 'CARVE'], default 'CARVE'

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


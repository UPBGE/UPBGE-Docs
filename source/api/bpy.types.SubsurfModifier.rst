SubsurfModifier(Modifier)
=========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: SubsurfModifier(Modifier)

   Subdivision surface modifier

   .. attribute:: levels

      Number of subdivisions to perform

      :type: int in [0, 11], default 0

   .. attribute:: render_levels

      Number of subdivisions to perform when rendering

      :type: int in [0, 11], default 0

   .. attribute:: show_only_control_edges

      Skip drawing/rendering of interior subdivided edges

      :type: boolean, default False

   .. attribute:: subdivision_type

      Select type of subdivision algorithm

      :type: enum in ['CATMULL_CLARK', 'SIMPLE'], default 'CATMULL_CLARK'

   .. attribute:: use_opensubdiv

      Use OpenSubdiv for the subdivisions (viewport only)

      :type: boolean, default False

   .. attribute:: use_subsurf_uv

      Use subsurf to subdivide UVs

      :type: boolean, default False

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


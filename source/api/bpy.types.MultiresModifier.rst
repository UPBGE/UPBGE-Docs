MultiresModifier(Modifier)
==========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: MultiresModifier(Modifier)

   Multiresolution mesh modifier

   .. attribute:: filepath

      Path to external displacements file

      :type: string, default "", (never None)

   .. data:: is_external

      Store multires displacements outside the .blend file, to save memory

      :type: boolean, default False, (readonly)

   .. attribute:: levels

      Number of subdivisions to use in the viewport

      :type: int in [0, 255], default 0

   .. attribute:: render_levels

      The subdivision level visible at render time

      :type: int in [0, 255], default 0

   .. attribute:: sculpt_levels

      Number of subdivisions to use in sculpt mode

      :type: int in [0, 255], default 0

   .. attribute:: show_only_control_edges

      Skip drawing/rendering of interior subdivided edges

      :type: boolean, default False

   .. attribute:: subdivision_type

      Select type of subdivision algorithm

      :type: enum in ['CATMULL_CLARK', 'SIMPLE'], default 'CATMULL_CLARK'

   .. data:: total_levels

      Number of subdivisions for which displacements are stored

      :type: int in [0, 255], default 0, (readonly)

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


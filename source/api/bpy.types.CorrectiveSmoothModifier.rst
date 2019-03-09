CorrectiveSmoothModifier(Modifier)
==================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: CorrectiveSmoothModifier(Modifier)

   Correct distortion caused by deformation

   .. attribute:: factor

      Smooth factor effect

      :type: float in [-inf, inf], default 0.0

   .. attribute:: invert_vertex_group

      Invert vertex group influence

      :type: boolean, default False

   .. data:: is_bind

      :type: boolean, default False, (readonly)

   .. attribute:: iterations

      :type: int in [-32768, 32767], default 0

   .. attribute:: rest_source

      Select the source of rest positions

      * ``ORCO`` Original Coords, Use base mesh vert coords as the rest position.
      * ``BIND`` Bind Coords, Use bind vert coords for rest position.

      :type: enum in ['ORCO', 'BIND'], default 'ORCO'

   .. attribute:: smooth_type

      Method used for smoothing

      * ``SIMPLE`` Simple, Use the average of adjacent edge-vertices.
      * ``LENGTH_WEIGHTED`` Length Weight, Use the average of adjacent edge-vertices weighted by their length.

      :type: enum in ['SIMPLE', 'LENGTH_WEIGHTED'], default 'SIMPLE'

   .. attribute:: use_only_smooth

      Apply smoothing without reconstructing the surface

      :type: boolean, default False

   .. attribute:: use_pin_boundary

      Excludes boundary vertices from being smoothed

      :type: boolean, default False

   .. attribute:: vertex_group

      Name of Vertex Group which determines influence of modifier per point

      :type: string, default "", (never None)

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


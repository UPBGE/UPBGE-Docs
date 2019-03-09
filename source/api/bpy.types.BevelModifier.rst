BevelModifier(Modifier)
=======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: BevelModifier(Modifier)

   Bevel modifier to make edges and vertices more rounded

   .. attribute:: angle_limit

      Angle above which to bevel edges

      :type: float in [0, 3.14159], default 0.0

   .. attribute:: edge_weight_method

      What edge weight to use for weighting a vertex

      :type: enum in ['AVERAGE', 'SHARPEST', 'LARGEST'], default 'AVERAGE'

   .. attribute:: limit_method

      * ``NONE`` None, Bevel the entire mesh by a constant amount.
      * ``ANGLE`` Angle, Only bevel edges with sharp enough angles between faces.
      * ``WEIGHT`` Weight, Use bevel weights to determine how much bevel is applied in edge mode.
      * ``VGROUP`` Vertex Group, Use vertex group weights to select whether vertex or edge is beveled.

      :type: enum in ['NONE', 'ANGLE', 'WEIGHT', 'VGROUP'], default 'NONE'

   .. attribute:: loop_slide

      Prefer sliding along edges to having even widths

      :type: boolean, default False

   .. attribute:: material

      Material index of generated faces, -1 for automatic

      :type: int in [-1, 32767], default 0

   .. attribute:: offset_type

      What distance Width measures

      * ``OFFSET`` Offset, Amount is offset of new edges from original.
      * ``WIDTH`` Width, Amount is width of new face.
      * ``DEPTH`` Depth, Amount is perpendicular distance from original edge to bevel face.
      * ``PERCENT`` Percent, Amount is percent of adjacent edge length.

      :type: enum in ['OFFSET', 'WIDTH', 'DEPTH', 'PERCENT'], default 'OFFSET'

   .. attribute:: profile

      The profile shape (0.5 = round)

      :type: float in [0, 1], default 0.0

   .. attribute:: segments

      Number of segments for round edges/verts

      :type: int in [1, 100], default 0

   .. attribute:: use_clamp_overlap

      Clamp the width to avoid overlap

      :type: boolean, default False

   .. attribute:: use_only_vertices

      Bevel verts/corners, not edges

      :type: boolean, default False

   .. attribute:: vertex_group

      Vertex group name

      :type: string, default "", (never None)

   .. attribute:: width

      Bevel value/amount

      :type: float in [0, inf], default 0.0

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


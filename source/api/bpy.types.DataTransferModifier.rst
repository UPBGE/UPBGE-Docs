DataTransferModifier(Modifier)
==============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: DataTransferModifier(Modifier)

   Modifier transferring some data from a source mesh

   .. attribute:: data_types_edges

      Which edge data layers to transfer

      * ``SHARP_EDGE`` Sharp, Transfer sharp mark.
      * ``SEAM`` UV Seam, Transfer UV seam mark.
      * ``CREASE`` Subsurf Crease, Transfer crease values.
      * ``BEVEL_WEIGHT_EDGE`` Bevel Weight, Transfer bevel weights.
      * ``FREESTYLE_EDGE`` Freestyle Mark, Transfer Freestyle edge mark.

      :type: enum set in {'SHARP_EDGE', 'SEAM', 'CREASE', 'BEVEL_WEIGHT_EDGE', 'FREESTYLE_EDGE'}, default {'SHARP_EDGE'}

   .. attribute:: data_types_loops

      Which face corner data layers to transfer

      * ``CUSTOM_NORMAL`` Custom Normals, Transfer custom normals.
      * ``VCOL`` VCol, Vertex (face corners) colors.
      * ``UV`` UVs, Transfer UV layers.

      :type: enum set in {'CUSTOM_NORMAL', 'VCOL', 'UV'}, default {'CUSTOM_NORMAL'}

   .. attribute:: data_types_polys

      Which poly data layers to transfer

      * ``SMOOTH`` Smooth, Transfer flat/smooth mark.
      * ``FREESTYLE_FACE`` Freestyle Mark, Transfer Freestyle face mark.

      :type: enum set in {'SMOOTH', 'FREESTYLE_FACE'}, default {'SMOOTH'}

   .. attribute:: data_types_verts

      Which vertex data layers to transfer

      * ``VGROUP_WEIGHTS`` Vertex Group(s), Transfer active or all vertex groups.
      * ``BEVEL_WEIGHT_VERT`` Bevel Weight, Transfer bevel weights.

      :type: enum set in {'VGROUP_WEIGHTS', 'BEVEL_WEIGHT_VERT'}, default {'VGROUP_WEIGHTS'}

   .. attribute:: edge_mapping

      Method used to map source edges to destination ones

      * ``TOPOLOGY`` Topology, Copy from identical topology meshes.
      * ``VERT_NEAREST`` Nearest Vertices, Copy from most similar edge (edge which vertices are the closest of destination edge's ones).
      * ``NEAREST`` Nearest Edge, Copy from closest edge (using midpoints).
      * ``POLY_NEAREST`` Nearest Face Edge, Copy from closest edge of closest face (using midpoints).
      * ``EDGEINTERP_VNORPROJ`` Projected Edge Interpolated, Interpolate all source edges hit by the projection of destination one along its own normal (from vertices).

      :type: enum in ['TOPOLOGY', 'VERT_NEAREST', 'NEAREST', 'POLY_NEAREST', 'EDGEINTERP_VNORPROJ'], default 'NEAREST'

   .. attribute:: invert_vertex_group

      Invert vertex group influence

      :type: boolean, default False

   .. attribute:: islands_precision

      Factor controlling precision of islands handling (typically, 0.1 should be enough, higher values can make things really slow)

      :type: float in [0, 1], default 0.0

   .. attribute:: layers_uv_select_dst

      How to match source and destination layers

      * ``ACTIVE`` Active Layer, Affect active data layer of all targets.
      * ``NAME`` By Name, Match target data layers to affect by name.
      * ``INDEX`` By Order, Match target data layers to affect by order (indices).

      :type: enum in ['ACTIVE', 'NAME', 'INDEX'], default 'NAME'

   .. attribute:: layers_uv_select_src

      Which layers to transfer, in case of multi-layers types

      * ``ACTIVE`` Active Layer, Only transfer active data layer.
      * ``ALL`` All Layers, Transfer all data layers.
      * ``BONE_SELECT`` Selected Pose Bones, Transfer all vertex groups used by selected pose bones.
      * ``BONE_DEFORM`` Deform Pose Bones, Transfer all vertex groups used by deform bones.

      :type: enum in ['ACTIVE', 'ALL', 'BONE_SELECT', 'BONE_DEFORM'], default 'ALL'

   .. attribute:: layers_vcol_select_dst

      How to match source and destination layers

      * ``ACTIVE`` Active Layer, Affect active data layer of all targets.
      * ``NAME`` By Name, Match target data layers to affect by name.
      * ``INDEX`` By Order, Match target data layers to affect by order (indices).

      :type: enum in ['ACTIVE', 'NAME', 'INDEX'], default 'NAME'

   .. attribute:: layers_vcol_select_src

      Which layers to transfer, in case of multi-layers types

      * ``ACTIVE`` Active Layer, Only transfer active data layer.
      * ``ALL`` All Layers, Transfer all data layers.
      * ``BONE_SELECT`` Selected Pose Bones, Transfer all vertex groups used by selected pose bones.
      * ``BONE_DEFORM`` Deform Pose Bones, Transfer all vertex groups used by deform bones.

      :type: enum in ['ACTIVE', 'ALL', 'BONE_SELECT', 'BONE_DEFORM'], default 'ALL'

   .. attribute:: layers_vgroup_select_dst

      How to match source and destination layers

      * ``ACTIVE`` Active Layer, Affect active data layer of all targets.
      * ``NAME`` By Name, Match target data layers to affect by name.
      * ``INDEX`` By Order, Match target data layers to affect by order (indices).

      :type: enum in ['ACTIVE', 'NAME', 'INDEX'], default 'NAME'

   .. attribute:: layers_vgroup_select_src

      Which layers to transfer, in case of multi-layers types

      * ``ACTIVE`` Active Layer, Only transfer active data layer.
      * ``ALL`` All Layers, Transfer all data layers.
      * ``BONE_SELECT`` Selected Pose Bones, Transfer all vertex groups used by selected pose bones.
      * ``BONE_DEFORM`` Deform Pose Bones, Transfer all vertex groups used by deform bones.

      :type: enum in ['ACTIVE', 'ALL', 'BONE_SELECT', 'BONE_DEFORM'], default 'ALL'

   .. attribute:: loop_mapping

      Method used to map source faces' corners to destination ones

      * ``TOPOLOGY`` Topology, Copy from identical topology meshes.
      * ``NEAREST_NORMAL`` Nearest Corner And Best Matching Normal, Copy from nearest corner which has the best matching normal.
      * ``NEAREST_POLYNOR`` Nearest Corner And Best Matching Face Normal, Copy from nearest corner which has the face with the best matching normal to destination corner's face one.
      * ``NEAREST_POLY`` Nearest Corner Of Nearest Face, Copy from nearest corner of nearest polygon.
      * ``POLYINTERP_NEAREST`` Nearest Face Interpolated, Copy from interpolated corners of the nearest source polygon.
      * ``POLYINTERP_LNORPROJ`` Projected Face Interpolated, Copy from interpolated corners of the source polygon hit by corner normal projection.

      :type: enum in ['TOPOLOGY', 'NEAREST_NORMAL', 'NEAREST_POLYNOR', 'NEAREST_POLY', 'POLYINTERP_NEAREST', 'POLYINTERP_LNORPROJ'], default 'NEAREST_POLYNOR'

   .. attribute:: max_distance

      Maximum allowed distance between source and destination element, for non-topology mappings

      :type: float in [0, inf], default 1.0

   .. attribute:: mix_factor

      Factor to use when applying data to destination (exact behavior depends on mix mode)

      :type: float in [0, 1], default 1.0

   .. attribute:: mix_mode

      How to affect destination elements with source values

      * ``REPLACE`` Replace, Overwrite all elements' data.
      * ``ABOVE_THRESHOLD`` Above Threshold, Only replace destination elements where data is above given threshold (exact behavior depends on data type).
      * ``BELOW_THRESHOLD`` Below Threshold, Only replace destination elements where data is below given threshold (exact behavior depends on data type).
      * ``MIX`` Mix, Mix source value into destination one, using given threshold as factor.
      * ``ADD`` Add, Add source value to destination one, using given threshold as factor.
      * ``SUB`` Subtract, Subtract source value to destination one, using given threshold as factor.
      * ``MUL`` Multiply, Multiply source value to destination one, using given threshold as factor.

      :type: enum in ['REPLACE', 'ABOVE_THRESHOLD', 'BELOW_THRESHOLD', 'MIX', 'ADD', 'SUB', 'MUL'], default 'REPLACE'

   .. attribute:: object

      Object to transfer data from

      :type: :class:`Object`

   .. attribute:: poly_mapping

      Method used to map source faces to destination ones

      * ``TOPOLOGY`` Topology, Copy from identical topology meshes.
      * ``NEAREST`` Nearest Face, Copy from nearest polygon (using center points).
      * ``NORMAL`` Best Normal-Matching, Copy from source polygon which normal is the closest to destination one.
      * ``POLYINTERP_PNORPROJ`` Projected Face Interpolated, Interpolate all source polygons intersected by the projection of destination one along its own normal.

      :type: enum in ['TOPOLOGY', 'NEAREST', 'NORMAL', 'POLYINTERP_PNORPROJ'], default 'NEAREST'

   .. attribute:: ray_radius

      'Width' of rays (especially useful when raycasting against vertices or edges)

      :type: float in [0, inf], default 0.0

   .. attribute:: use_edge_data

      Enable edge data transfer

      :type: boolean, default False

   .. attribute:: use_loop_data

      Enable face corner data transfer

      :type: boolean, default False

   .. attribute:: use_max_distance

      Source elements must be closer than given distance from destination one

      :type: boolean, default False

   .. attribute:: use_object_transform

      Evaluate source and destination meshes in global space

      :type: boolean, default True

   .. attribute:: use_poly_data

      Enable face data transfer

      :type: boolean, default False

   .. attribute:: use_vert_data

      Enable vertex data transfer

      :type: boolean, default False

   .. attribute:: vert_mapping

      Method used to map source vertices to destination ones

      * ``TOPOLOGY`` Topology, Copy from identical topology meshes.
      * ``NEAREST`` Nearest vertex, Copy from closest vertex.
      * ``EDGE_NEAREST`` Nearest Edge Vertex, Copy from closest vertex of closest edge.
      * ``EDGEINTERP_NEAREST`` Nearest Edge Interpolated, Copy from interpolated values of vertices from closest point on closest edge.
      * ``POLY_NEAREST`` Nearest Face Vertex, Copy from closest vertex of closest face.
      * ``POLYINTERP_NEAREST`` Nearest Face Interpolated, Copy from interpolated values of vertices from closest point on closest face.
      * ``POLYINTERP_VNORPROJ`` Projected Face Interpolated, Copy from interpolated values of vertices from point on closest face hit by normal-projection.

      :type: enum in ['TOPOLOGY', 'NEAREST', 'EDGE_NEAREST', 'EDGEINTERP_NEAREST', 'POLY_NEAREST', 'POLYINTERP_NEAREST', 'POLYINTERP_VNORPROJ'], default 'NEAREST'

   .. attribute:: vertex_group

      Vertex group name for selecting the affected areas

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


ToolSettings(bpy_struct)
========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ToolSettings(bpy_struct)

   

   .. attribute:: auto_keying_mode

      Mode of automatic keyframe insertion for Objects and Bones

      :type: enum in ['ADD_REPLACE_KEYS', 'REPLACE_KEYS'], default 'ADD_REPLACE_KEYS'

   .. data:: curve_paint_settings

      :type: :class:`CurvePaintSettings`, (readonly, never None)

   .. attribute:: double_threshold

      Limit for removing duplicates and 'Auto Merge'

      :type: float in [0, 1], default 0.0

   .. attribute:: edge_path_live_unwrap

      Changing edges seam re-calculates UV unwrap

      :type: boolean, default False

   .. attribute:: edge_path_mode

      The edge flag to tag when selecting the shortest path

      :type: enum in ['SELECT', 'SEAM', 'SHARP', 'CREASE', 'BEVEL', 'FREESTYLE'], default 'SELECT'

   .. attribute:: etch_adaptive_limit

      Correlation threshold for number of bones in the subdivided stroke

      :type: float in [1e-05, 1], default 0.0

   .. attribute:: etch_convert_mode

      Method used to convert stroke to bones

      * ``FIXED`` Fixed, Subdivide stroke in fixed number of bones.
      * ``LENGTH`` Length, Subdivide stroke in bones of specific length.
      * ``ADAPTIVE`` Adaptive, Subdivide stroke adaptively, with more subdivision in curvier parts.
      * ``RETARGET`` Retarget, Retarget template bone chain to stroke.

      :type: enum in ['FIXED', 'LENGTH', 'ADAPTIVE', 'RETARGET'], default 'FIXED'

   .. attribute:: etch_length_limit

      Maximum length of the subdivided bones

      :type: float in [1e-05, 100000], default 0.0

   .. attribute:: etch_number

      Text to replace &N with (e.g. 'Finger.&N' -> 'Finger.1' or 'Finger.One')

      :type: string, default "", (never None)

   .. attribute:: etch_roll_mode

      Method used to adjust the roll of bones when retargeting

      * ``NONE`` None, Don't adjust roll.
      * ``VIEW`` View, Roll bones to face the view.
      * ``JOINT`` Joint, Roll bone to original joint plane offset.

      :type: enum in ['NONE', 'VIEW', 'JOINT'], default 'NONE'

   .. attribute:: etch_side

      Text to replace &S with (e.g. 'Arm.&S' -> 'Arm.R' or 'Arm.Right')

      :type: string, default "", (never None)

   .. attribute:: etch_subdivision_number

      Number of bones in the subdivided stroke

      :type: int in [1, 255], default 0

   .. attribute:: etch_template

      Template armature that will be retargeted to the stroke

      :type: :class:`Object`

   .. data:: gpencil_brushes

      Grease Pencil drawing brushes

      :type: :class:`GreasePencilBrushes` :class:`bpy_prop_collection` of :class:`GPencilBrush`, (readonly)

   .. data:: gpencil_interpolate

      Settings for Grease Pencil Interpolation tools

      :type: :class:`GPencilInterpolateSettings`, (readonly)

   .. data:: gpencil_sculpt

      Settings for stroke sculpting tools and brushes

      :type: :class:`GPencilSculptSettings`, (readonly)

   .. attribute:: gpencil_stroke_placement_image_editor

      * ``CURSOR`` Cursor, Draw stroke at the 3D cursor.
      * ``VIEW`` View, Stick stroke to the view .
      * ``SURFACE`` Surface, Stick stroke to surfaces.
      * ``STROKE`` Stroke, Stick stroke to other strokes.

      :type: enum in ['CURSOR', 'VIEW', 'SURFACE', 'STROKE'], default 'VIEW'

   .. attribute:: gpencil_stroke_placement_sequencer_preview

      * ``CURSOR`` Cursor, Draw stroke at the 3D cursor.
      * ``VIEW`` View, Stick stroke to the view .
      * ``SURFACE`` Surface, Stick stroke to surfaces.
      * ``STROKE`` Stroke, Stick stroke to other strokes.

      :type: enum in ['CURSOR', 'VIEW', 'SURFACE', 'STROKE'], default 'VIEW'

   .. attribute:: gpencil_stroke_placement_view2d

      * ``CURSOR`` Cursor, Draw stroke at the 3D cursor.
      * ``VIEW`` View, Stick stroke to the view .
      * ``SURFACE`` Surface, Stick stroke to surfaces.
      * ``STROKE`` Stroke, Stick stroke to other strokes.

      :type: enum in ['CURSOR', 'VIEW', 'SURFACE', 'STROKE'], default 'VIEW'

   .. attribute:: gpencil_stroke_placement_view3d

      * ``CURSOR`` Cursor, Draw stroke at the 3D cursor.
      * ``VIEW`` View, Stick stroke to the view .
      * ``SURFACE`` Surface, Stick stroke to surfaces.
      * ``STROKE`` Stroke, Stick stroke to other strokes.

      :type: enum in ['CURSOR', 'VIEW', 'SURFACE', 'STROKE'], default 'VIEW'

   .. attribute:: grease_pencil_source

      Data-block where active Grease Pencil data is found from

      * ``SCENE`` Scene, Grease Pencil data attached to the current scene is used, unless the active object already has Grease Pencil data (i.e. for old files).
      * ``OBJECT`` Object, Grease Pencil data-blocks attached to the active object are used (required when using pre 2.73 add-ons, e.g. BSurfaces).

      :type: enum in ['SCENE', 'OBJECT'], default 'SCENE'

   .. data:: image_paint

      :type: :class:`ImagePaint`, (readonly)

   .. attribute:: keyframe_type

      Type of keyframes to create when inserting keyframes

      * ``KEYFRAME`` Keyframe, Normal keyframe - e.g. for key poses.
      * ``BREAKDOWN`` Breakdown, A breakdown pose - e.g. for transitions between key poses.
      * ``MOVING_HOLD`` Moving Hold, A keyframe that is part of a moving hold.
      * ``EXTREME`` Extreme, An 'extreme' pose, or some other purpose as needed.
      * ``JITTER`` Jitter, A filler or baked keyframe for keying on ones, or some other purpose as needed.

      :type: enum in ['KEYFRAME', 'BREAKDOWN', 'MOVING_HOLD', 'EXTREME', 'JITTER'], default 'KEYFRAME'

   .. attribute:: lock_markers

      Prevent marker editing

      :type: boolean, default False

   .. attribute:: mesh_select_mode

      Which mesh elements selection works on

      :type: boolean array of 3 items, default (False, False, False)

   .. attribute:: normal_size

      Display size for normals in the 3D view

      :type: float in [1e-05, 1000], default 0.0

   .. data:: particle_edit

      :type: :class:`ParticleEdit`, (readonly)

   .. attribute:: proportional_edit

      Proportional Editing mode, allows transforms with distance fall-off

      * ``DISABLED`` Disable, Proportional Editing disabled.
      * ``ENABLED`` Enable, Proportional Editing enabled.
      * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations.
      * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.

      :type: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], default 'DISABLED'

   .. attribute:: proportional_edit_falloff

      Falloff type for proportional editing mode

      * ``SMOOTH`` Smooth, Smooth falloff.
      * ``SPHERE`` Sphere, Spherical falloff.
      * ``ROOT`` Root, Root falloff.
      * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff.
      * ``SHARP`` Sharp, Sharp falloff.
      * ``LINEAR`` Linear, Linear falloff.
      * ``CONSTANT`` Constant, Constant falloff.
      * ``RANDOM`` Random, Random falloff.

      :type: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], default 'SMOOTH'

   .. attribute:: proportional_size

      Display size for proportional editing circle

      :type: float in [1e-05, 5000], default 0.0

   .. data:: sculpt

      :type: :class:`Sculpt`, (readonly)

   .. attribute:: show_uv_local_view

      Draw only faces with the currently displayed image assigned

      :type: boolean, default False

   .. attribute:: snap_element

      Type of element to snap to

      * ``INCREMENT`` Increment, Snap to increments of grid.
      * ``VERTEX`` Vertex, Snap to vertices.
      * ``EDGE`` Edge, Snap to edges.
      * ``FACE`` Face, Snap to faces.
      * ``VOLUME`` Volume, Snap to volume.

      :type: enum in ['INCREMENT', 'VERTEX', 'EDGE', 'FACE', 'VOLUME'], default 'INCREMENT'

   .. attribute:: snap_node_element

      Type of element to snap to

      * ``GRID`` Grid, Snap to grid.
      * ``NODE_X`` Node X, Snap to left/right node border.
      * ``NODE_Y`` Node Y, Snap to top/bottom node border.
      * ``NODE_XY`` Node X / Y, Snap to any node border.

      :type: enum in ['GRID', 'NODE_X', 'NODE_Y', 'NODE_XY'], default 'GRID'

   .. attribute:: snap_target

      Which part to snap onto the target

      * ``CLOSEST`` Closest, Snap closest point onto target.
      * ``CENTER`` Center, Snap center onto target.
      * ``MEDIAN`` Median, Snap median onto target.
      * ``ACTIVE`` Active, Snap active onto target.

      :type: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], default 'CLOSEST'

   .. attribute:: snap_uv_element

      Type of element to snap to

      * ``INCREMENT`` Increment, Snap to increments of grid.
      * ``VERTEX`` Vertex, Snap to vertices.

      :type: enum in ['INCREMENT', 'VERTEX'], default 'INCREMENT'

   .. data:: statvis

      :type: :class:`MeshStatVis`, (readonly, never None)

   .. data:: unified_paint_settings

      :type: :class:`UnifiedPaintSettings`, (readonly, never None)

   .. attribute:: use_auto_normalize

      Ensure all bone-deforming vertex groups add up to 1.0 while weight painting

      :type: boolean, default False

   .. attribute:: use_bone_sketching

      Use sketching to create and edit bones

      :type: boolean, default False

   .. attribute:: use_etch_autoname

      Automatically generate values to replace &N and &S suffix placeholders in template names

      :type: boolean, default False

   .. attribute:: use_etch_overdraw

      Adjust strokes by drawing near them

      :type: boolean, default False

   .. attribute:: use_etch_quick

      Automatically convert and delete on stroke end

      :type: boolean, default False

   .. attribute:: use_gpencil_additive_drawing

      When creating new frames, the strokes from the previous/active frame are included as the basis for the new one

      :type: boolean, default False

   .. attribute:: use_gpencil_continuous_drawing

      Allow drawing multiple strokes at a time with Grease Pencil

      :type: boolean, default False

   .. attribute:: use_gpencil_draw_onback

      When draw new strokes, the new stroke is drawn below of all strokes in the layer

      :type: boolean, default False

   .. attribute:: use_gpencil_stroke_endpoints

      Only use the first and last parts of the stroke for snapping

      :type: boolean, default False

   .. attribute:: use_keyframe_insert_auto

      Automatic keyframe insertion for Objects and Bones

      :type: boolean, default False

   .. attribute:: use_keyframe_insert_keyingset

      Automatic keyframe insertion using active Keying Set only

      :type: boolean, default False

   .. attribute:: use_mesh_automerge

      Automatically merge vertices moved to the same location

      :type: boolean, default False

   .. attribute:: use_multipaint

      Paint across the weights of all selected bones, maintaining their relative influence

      :type: boolean, default False

   .. attribute:: use_proportional_action

      Proportional editing in action editor

      :type: boolean, default False

   .. attribute:: use_proportional_edit_mask

      Proportional editing mask mode

      :type: boolean, default False

   .. attribute:: use_proportional_edit_objects

      Proportional editing object mode

      :type: boolean, default False

   .. attribute:: use_proportional_fcurve

      Proportional editing in FCurve editor

      :type: boolean, default False

   .. attribute:: use_record_with_nla

      Add a new NLA Track + Strip for every loop/pass made over the animation to allow non-destructive tweaking

      :type: boolean, default False

   .. attribute:: use_snap

      Snap during transform

      :type: boolean, default False

   .. attribute:: use_snap_align_rotation

      Align rotation with the snapping target

      :type: boolean, default False

   .. attribute:: use_snap_grid_absolute

      Absolute grid alignment while translating (based on the pivot center)

      :type: boolean, default False

   .. attribute:: use_snap_peel_object

      Consider objects as whole when finding volume center

      :type: boolean, default False

   .. attribute:: use_snap_project

      Project individual elements on the surface of other objects

      :type: boolean, default False

   .. attribute:: use_snap_self

      Snap onto itself (editmode)

      :type: boolean, default False

   .. attribute:: use_uv_sculpt

      Enable brush for UV sculpting

      :type: boolean, default False

   .. attribute:: use_uv_select_sync

      Keep UV and edit mode mesh selection in sync

      :type: boolean, default False

   .. attribute:: uv_relax_method

      Algorithm used for UV relaxation

      * ``LAPLACIAN`` Laplacian, Use Laplacian method for relaxation.
      * ``HC`` HC, Use HC method for relaxation.

      :type: enum in ['LAPLACIAN', 'HC'], default 'LAPLACIAN'

   .. data:: uv_sculpt

      :type: :class:`UvSculpt`, (readonly)

   .. attribute:: uv_sculpt_all_islands

      Brush operates on all islands

      :type: boolean, default False

   .. attribute:: uv_sculpt_lock_borders

      Disable editing of boundary edges

      :type: boolean, default False

   .. attribute:: uv_sculpt_tool

      Select Tools for the UV sculpt brushes

      * ``PINCH`` Pinch, Pinch UVs.
      * ``RELAX`` Relax, Relax UVs.
      * ``GRAB`` Grab, Grab UVs.

      :type: enum in ['PINCH', 'RELAX', 'GRAB'], default 'PINCH'

   .. attribute:: uv_select_mode

      UV selection and display mode

      * ``VERTEX`` Vertex, Vertex selection mode.
      * ``EDGE`` Edge, Edge selection mode.
      * ``FACE`` Face, Face selection mode.
      * ``ISLAND`` Island, Island selection mode.

      :type: enum in ['VERTEX', 'EDGE', 'FACE', 'ISLAND'], default 'VERTEX'

   .. attribute:: vertex_group_subset

      Filter Vertex groups for Display

      * ``ALL`` All, All Vertex Groups.
      * ``BONE_DEFORM`` Deform, Vertex Groups assigned to Deform Bones.
      * ``OTHER_DEFORM`` Other, Vertex Groups assigned to non Deform Bones.

      :type: enum in ['ALL', 'BONE_DEFORM', 'OTHER_DEFORM'], default 'ALL'

   .. attribute:: vertex_group_user

      Display unweighted vertices

      * ``NONE`` None.
      * ``ACTIVE`` Active, Show vertices with no weights in the active group.
      * ``ALL`` All, Show vertices with no weights in any group.

      :type: enum in ['NONE', 'ACTIVE', 'ALL'], default 'NONE'

   .. attribute:: vertex_group_weight

      Weight to assign in vertex groups

      :type: float in [0, 1], default 0.0

   .. data:: vertex_paint

      :type: :class:`VertexPaint`, (readonly)

   .. data:: weight_paint

      :type: :class:`VertexPaint`, (readonly)

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

   * :class:`Context.tool_settings`
   * :class:`Scene.tool_settings`


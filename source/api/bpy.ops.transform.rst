Transform Operators
===================

.. module:: bpy.ops.transform

.. function:: bend(value=(0.0), mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, center_override=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Bend selected items between the 3D cursor and the mouse

   :arg value:

      Angle

   :type value: float array of 1 items in [-inf, inf], (optional)
   :arg mirror:

      Mirror Editing

   :type mirror: boolean, (optional)
   :arg proportional:

      Proportional Editing

      * ``DISABLED`` Disable, Proportional Editing disabled.
      * ``ENABLED`` Enable, Proportional Editing enabled.
      * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations.
      * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.

   :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
   :arg proportional_edit_falloff:

      Proportional Editing Falloff, Falloff type for proportional editing mode

      * ``SMOOTH`` Smooth, Smooth falloff.
      * ``SPHERE`` Sphere, Spherical falloff.
      * ``ROOT`` Root, Root falloff.
      * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff.
      * ``SHARP`` Sharp, Sharp falloff.
      * ``LINEAR`` Linear, Linear falloff.
      * ``CONSTANT`` Constant, Constant falloff.
      * ``RANDOM`` Random, Random falloff.

   :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
   :arg proportional_size:

      Proportional Size

   :type proportional_size: float in [1e-06, inf], (optional)
   :arg snap:

      Use Snapping Options

   :type snap: boolean, (optional)
   :arg snap_target:

      Target

      * ``CLOSEST`` Closest, Snap closest point onto target.
      * ``CENTER`` Center, Snap center onto target.
      * ``MEDIAN`` Median, Snap median onto target.
      * ``ACTIVE`` Active, Snap active onto target.

   :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
   :arg snap_point:

      Point

   :type snap_point: float array of 3 items in [-inf, inf], (optional)
   :arg snap_align:

      Align with Point Normal

   :type snap_align: boolean, (optional)
   :arg snap_normal:

      Normal

   :type snap_normal: float array of 3 items in [-inf, inf], (optional)
   :arg gpencil_strokes:

      Edit Grease Pencil, Edit selected Grease Pencil strokes

   :type gpencil_strokes: boolean, (optional)
   :arg center_override:

      Center Override, Force using this center value (when set)

   :type center_override: float array of 3 items in [-inf, inf], (optional)
   :arg release_confirm:

      Confirm on Release, Always confirm operation when releasing button

   :type release_confirm: boolean, (optional)
   :arg use_accurate:

      Accurate, Use accurate transformation

   :type use_accurate: boolean, (optional)

.. function:: create_orientation(name="", use_view=False, use=False, overwrite=False)

   Create transformation orientation from selection

   :arg name:

      Name, Name of the new custom orientation

   :type name: string, (optional, never None)
   :arg use_view:

      Use View, Use the current view instead of the active object to create the new orientation

   :type use_view: boolean, (optional)
   :arg use:

      Use after creation, Select orientation after its creation

   :type use: boolean, (optional)
   :arg overwrite:

      Overwrite previous, Overwrite previously created orientation with same name

   :type overwrite: boolean, (optional)

.. function:: delete_orientation()

   Delete transformation orientation

.. function:: edge_bevelweight(value=0.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Change the bevel weight of edges

   :arg value:

      Factor

   :type value: float in [-1, 1], (optional)
   :arg snap:

      Use Snapping Options

   :type snap: boolean, (optional)
   :arg snap_target:

      Target

      * ``CLOSEST`` Closest, Snap closest point onto target.
      * ``CENTER`` Center, Snap center onto target.
      * ``MEDIAN`` Median, Snap median onto target.
      * ``ACTIVE`` Active, Snap active onto target.

   :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
   :arg snap_point:

      Point

   :type snap_point: float array of 3 items in [-inf, inf], (optional)
   :arg snap_align:

      Align with Point Normal

   :type snap_align: boolean, (optional)
   :arg snap_normal:

      Normal

   :type snap_normal: float array of 3 items in [-inf, inf], (optional)
   :arg release_confirm:

      Confirm on Release, Always confirm operation when releasing button

   :type release_confirm: boolean, (optional)
   :arg use_accurate:

      Accurate, Use accurate transformation

   :type use_accurate: boolean, (optional)

.. function:: edge_crease(value=0.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Change the crease of edges

   :arg value:

      Factor

   :type value: float in [-1, 1], (optional)
   :arg snap:

      Use Snapping Options

   :type snap: boolean, (optional)
   :arg snap_target:

      Target

      * ``CLOSEST`` Closest, Snap closest point onto target.
      * ``CENTER`` Center, Snap center onto target.
      * ``MEDIAN`` Median, Snap median onto target.
      * ``ACTIVE`` Active, Snap active onto target.

   :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
   :arg snap_point:

      Point

   :type snap_point: float array of 3 items in [-inf, inf], (optional)
   :arg snap_align:

      Align with Point Normal

   :type snap_align: boolean, (optional)
   :arg snap_normal:

      Normal

   :type snap_normal: float array of 3 items in [-inf, inf], (optional)
   :arg release_confirm:

      Confirm on Release, Always confirm operation when releasing button

   :type release_confirm: boolean, (optional)
   :arg use_accurate:

      Accurate, Use accurate transformation

   :type use_accurate: boolean, (optional)

.. function:: edge_slide(value=0.0, single_side=False, use_even=False, flipped=False, use_clamp=True, mirror=False, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), correct_uv=False, release_confirm=False, use_accurate=False)

   Slide an edge loop along a mesh

   :arg value:

      Factor

   :type value: float in [-10, 10], (optional)
   :arg single_side:

      Single Side

   :type single_side: boolean, (optional)
   :arg use_even:

      Even, Make the edge loop match the shape of the adjacent edge loop

   :type use_even: boolean, (optional)
   :arg flipped:

      Flipped, When Even mode is active, flips between the two adjacent edge loops

   :type flipped: boolean, (optional)
   :arg use_clamp:

      Clamp, Clamp within the edge extents

   :type use_clamp: boolean, (optional)
   :arg mirror:

      Mirror Editing

   :type mirror: boolean, (optional)
   :arg snap:

      Use Snapping Options

   :type snap: boolean, (optional)
   :arg snap_target:

      Target

      * ``CLOSEST`` Closest, Snap closest point onto target.
      * ``CENTER`` Center, Snap center onto target.
      * ``MEDIAN`` Median, Snap median onto target.
      * ``ACTIVE`` Active, Snap active onto target.

   :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
   :arg snap_point:

      Point

   :type snap_point: float array of 3 items in [-inf, inf], (optional)
   :arg snap_align:

      Align with Point Normal

   :type snap_align: boolean, (optional)
   :arg snap_normal:

      Normal

   :type snap_normal: float array of 3 items in [-inf, inf], (optional)
   :arg correct_uv:

      Correct UVs, Correct UV coordinates when transforming

   :type correct_uv: boolean, (optional)
   :arg release_confirm:

      Confirm on Release, Always confirm operation when releasing button

   :type release_confirm: boolean, (optional)
   :arg use_accurate:

      Accurate, Use accurate transformation

   :type use_accurate: boolean, (optional)

.. function:: mirror(constraint_axis=(False, False, False), constraint_orientation='GLOBAL', proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, gpencil_strokes=False, center_override=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Mirror selected items around one or more axes

   :arg constraint_axis:

      Constraint Axis

   :type constraint_axis: boolean array of 3 items, (optional)
   :arg constraint_orientation:

      Orientation, Transformation orientation

   :type constraint_orientation: enum in [], (optional)
   :arg proportional:

      Proportional Editing

      * ``DISABLED`` Disable, Proportional Editing disabled.
      * ``ENABLED`` Enable, Proportional Editing enabled.
      * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations.
      * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.

   :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
   :arg proportional_edit_falloff:

      Proportional Editing Falloff, Falloff type for proportional editing mode

      * ``SMOOTH`` Smooth, Smooth falloff.
      * ``SPHERE`` Sphere, Spherical falloff.
      * ``ROOT`` Root, Root falloff.
      * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff.
      * ``SHARP`` Sharp, Sharp falloff.
      * ``LINEAR`` Linear, Linear falloff.
      * ``CONSTANT`` Constant, Constant falloff.
      * ``RANDOM`` Random, Random falloff.

   :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
   :arg proportional_size:

      Proportional Size

   :type proportional_size: float in [1e-06, inf], (optional)
   :arg gpencil_strokes:

      Edit Grease Pencil, Edit selected Grease Pencil strokes

   :type gpencil_strokes: boolean, (optional)
   :arg center_override:

      Center Override, Force using this center value (when set)

   :type center_override: float array of 3 items in [-inf, inf], (optional)
   :arg release_confirm:

      Confirm on Release, Always confirm operation when releasing button

   :type release_confirm: boolean, (optional)
   :arg use_accurate:

      Accurate, Use accurate transformation

   :type use_accurate: boolean, (optional)

.. function:: push_pull(value=0.0, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), center_override=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Push/Pull selected items

   :arg value:

      Distance

   :type value: float in [-inf, inf], (optional)
   :arg mirror:

      Mirror Editing

   :type mirror: boolean, (optional)
   :arg proportional:

      Proportional Editing

      * ``DISABLED`` Disable, Proportional Editing disabled.
      * ``ENABLED`` Enable, Proportional Editing enabled.
      * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations.
      * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.

   :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
   :arg proportional_edit_falloff:

      Proportional Editing Falloff, Falloff type for proportional editing mode

      * ``SMOOTH`` Smooth, Smooth falloff.
      * ``SPHERE`` Sphere, Spherical falloff.
      * ``ROOT`` Root, Root falloff.
      * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff.
      * ``SHARP`` Sharp, Sharp falloff.
      * ``LINEAR`` Linear, Linear falloff.
      * ``CONSTANT`` Constant, Constant falloff.
      * ``RANDOM`` Random, Random falloff.

   :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
   :arg proportional_size:

      Proportional Size

   :type proportional_size: float in [1e-06, inf], (optional)
   :arg snap:

      Use Snapping Options

   :type snap: boolean, (optional)
   :arg snap_target:

      Target

      * ``CLOSEST`` Closest, Snap closest point onto target.
      * ``CENTER`` Center, Snap center onto target.
      * ``MEDIAN`` Median, Snap median onto target.
      * ``ACTIVE`` Active, Snap active onto target.

   :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
   :arg snap_point:

      Point

   :type snap_point: float array of 3 items in [-inf, inf], (optional)
   :arg snap_align:

      Align with Point Normal

   :type snap_align: boolean, (optional)
   :arg snap_normal:

      Normal

   :type snap_normal: float array of 3 items in [-inf, inf], (optional)
   :arg center_override:

      Center Override, Force using this center value (when set)

   :type center_override: float array of 3 items in [-inf, inf], (optional)
   :arg release_confirm:

      Confirm on Release, Always confirm operation when releasing button

   :type release_confirm: boolean, (optional)
   :arg use_accurate:

      Accurate, Use accurate transformation

   :type use_accurate: boolean, (optional)

.. function:: resize(value=(1.0, 1.0, 1.0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, center_override=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Scale (resize) selected items

   :arg value:

      Vector

   :type value: float array of 3 items in [-inf, inf], (optional)
   :arg constraint_axis:

      Constraint Axis

   :type constraint_axis: boolean array of 3 items, (optional)
   :arg constraint_orientation:

      Orientation, Transformation orientation

   :type constraint_orientation: enum in [], (optional)
   :arg mirror:

      Mirror Editing

   :type mirror: boolean, (optional)
   :arg proportional:

      Proportional Editing

      * ``DISABLED`` Disable, Proportional Editing disabled.
      * ``ENABLED`` Enable, Proportional Editing enabled.
      * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations.
      * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.

   :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
   :arg proportional_edit_falloff:

      Proportional Editing Falloff, Falloff type for proportional editing mode

      * ``SMOOTH`` Smooth, Smooth falloff.
      * ``SPHERE`` Sphere, Spherical falloff.
      * ``ROOT`` Root, Root falloff.
      * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff.
      * ``SHARP`` Sharp, Sharp falloff.
      * ``LINEAR`` Linear, Linear falloff.
      * ``CONSTANT`` Constant, Constant falloff.
      * ``RANDOM`` Random, Random falloff.

   :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
   :arg proportional_size:

      Proportional Size

   :type proportional_size: float in [1e-06, inf], (optional)
   :arg snap:

      Use Snapping Options

   :type snap: boolean, (optional)
   :arg snap_target:

      Target

      * ``CLOSEST`` Closest, Snap closest point onto target.
      * ``CENTER`` Center, Snap center onto target.
      * ``MEDIAN`` Median, Snap median onto target.
      * ``ACTIVE`` Active, Snap active onto target.

   :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
   :arg snap_point:

      Point

   :type snap_point: float array of 3 items in [-inf, inf], (optional)
   :arg snap_align:

      Align with Point Normal

   :type snap_align: boolean, (optional)
   :arg snap_normal:

      Normal

   :type snap_normal: float array of 3 items in [-inf, inf], (optional)
   :arg gpencil_strokes:

      Edit Grease Pencil, Edit selected Grease Pencil strokes

   :type gpencil_strokes: boolean, (optional)
   :arg texture_space:

      Edit Texture Space, Edit Object data texture space

   :type texture_space: boolean, (optional)
   :arg remove_on_cancel:

      Remove on Cancel, Remove elements on cancel

   :type remove_on_cancel: boolean, (optional)
   :arg center_override:

      Center Override, Force using this center value (when set)

   :type center_override: float array of 3 items in [-inf, inf], (optional)
   :arg release_confirm:

      Confirm on Release, Always confirm operation when releasing button

   :type release_confirm: boolean, (optional)
   :arg use_accurate:

      Accurate, Use accurate transformation

   :type use_accurate: boolean, (optional)

.. function:: rotate(value=0.0, axis=(0.0, 0.0, 0.0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, center_override=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Rotate selected items

   :arg value:

      Angle

   :type value: float in [-inf, inf], (optional)
   :arg axis:

      Axis, The axis around which the transformation occurs

   :type axis: float array of 3 items in [-inf, inf], (optional)
   :arg constraint_axis:

      Constraint Axis

   :type constraint_axis: boolean array of 3 items, (optional)
   :arg constraint_orientation:

      Orientation, Transformation orientation

   :type constraint_orientation: enum in [], (optional)
   :arg mirror:

      Mirror Editing

   :type mirror: boolean, (optional)
   :arg proportional:

      Proportional Editing

      * ``DISABLED`` Disable, Proportional Editing disabled.
      * ``ENABLED`` Enable, Proportional Editing enabled.
      * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations.
      * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.

   :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
   :arg proportional_edit_falloff:

      Proportional Editing Falloff, Falloff type for proportional editing mode

      * ``SMOOTH`` Smooth, Smooth falloff.
      * ``SPHERE`` Sphere, Spherical falloff.
      * ``ROOT`` Root, Root falloff.
      * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff.
      * ``SHARP`` Sharp, Sharp falloff.
      * ``LINEAR`` Linear, Linear falloff.
      * ``CONSTANT`` Constant, Constant falloff.
      * ``RANDOM`` Random, Random falloff.

   :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
   :arg proportional_size:

      Proportional Size

   :type proportional_size: float in [1e-06, inf], (optional)
   :arg snap:

      Use Snapping Options

   :type snap: boolean, (optional)
   :arg snap_target:

      Target

      * ``CLOSEST`` Closest, Snap closest point onto target.
      * ``CENTER`` Center, Snap center onto target.
      * ``MEDIAN`` Median, Snap median onto target.
      * ``ACTIVE`` Active, Snap active onto target.

   :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
   :arg snap_point:

      Point

   :type snap_point: float array of 3 items in [-inf, inf], (optional)
   :arg snap_align:

      Align with Point Normal

   :type snap_align: boolean, (optional)
   :arg snap_normal:

      Normal

   :type snap_normal: float array of 3 items in [-inf, inf], (optional)
   :arg gpencil_strokes:

      Edit Grease Pencil, Edit selected Grease Pencil strokes

   :type gpencil_strokes: boolean, (optional)
   :arg center_override:

      Center Override, Force using this center value (when set)

   :type center_override: float array of 3 items in [-inf, inf], (optional)
   :arg release_confirm:

      Confirm on Release, Always confirm operation when releasing button

   :type release_confirm: boolean, (optional)
   :arg use_accurate:

      Accurate, Use accurate transformation

   :type use_accurate: boolean, (optional)

.. function:: select_orientation(orientation='GLOBAL')

   Select transformation orientation

   :arg orientation:

      Orientation, Transformation orientation

   :type orientation: enum in [], (optional)

.. function:: seq_slide(value=(0.0, 0.0), snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Slide a sequence strip in time

   :arg value:

      Vector

   :type value: float array of 2 items in [-inf, inf], (optional)
   :arg snap:

      Use Snapping Options

   :type snap: boolean, (optional)
   :arg snap_target:

      Target

      * ``CLOSEST`` Closest, Snap closest point onto target.
      * ``CENTER`` Center, Snap center onto target.
      * ``MEDIAN`` Median, Snap median onto target.
      * ``ACTIVE`` Active, Snap active onto target.

   :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
   :arg snap_point:

      Point

   :type snap_point: float array of 3 items in [-inf, inf], (optional)
   :arg snap_align:

      Align with Point Normal

   :type snap_align: boolean, (optional)
   :arg snap_normal:

      Normal

   :type snap_normal: float array of 3 items in [-inf, inf], (optional)
   :arg release_confirm:

      Confirm on Release, Always confirm operation when releasing button

   :type release_confirm: boolean, (optional)
   :arg use_accurate:

      Accurate, Use accurate transformation

   :type use_accurate: boolean, (optional)

.. function:: shear(value=0.0, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, release_confirm=False, use_accurate=False)

   Shear selected items along the horizontal screen axis

   :arg value:

      Offset

   :type value: float in [-inf, inf], (optional)
   :arg mirror:

      Mirror Editing

   :type mirror: boolean, (optional)
   :arg proportional:

      Proportional Editing

      * ``DISABLED`` Disable, Proportional Editing disabled.
      * ``ENABLED`` Enable, Proportional Editing enabled.
      * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations.
      * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.

   :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
   :arg proportional_edit_falloff:

      Proportional Editing Falloff, Falloff type for proportional editing mode

      * ``SMOOTH`` Smooth, Smooth falloff.
      * ``SPHERE`` Sphere, Spherical falloff.
      * ``ROOT`` Root, Root falloff.
      * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff.
      * ``SHARP`` Sharp, Sharp falloff.
      * ``LINEAR`` Linear, Linear falloff.
      * ``CONSTANT`` Constant, Constant falloff.
      * ``RANDOM`` Random, Random falloff.

   :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
   :arg proportional_size:

      Proportional Size

   :type proportional_size: float in [1e-06, inf], (optional)
   :arg snap:

      Use Snapping Options

   :type snap: boolean, (optional)
   :arg snap_target:

      Target

      * ``CLOSEST`` Closest, Snap closest point onto target.
      * ``CENTER`` Center, Snap center onto target.
      * ``MEDIAN`` Median, Snap median onto target.
      * ``ACTIVE`` Active, Snap active onto target.

   :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
   :arg snap_point:

      Point

   :type snap_point: float array of 3 items in [-inf, inf], (optional)
   :arg snap_align:

      Align with Point Normal

   :type snap_align: boolean, (optional)
   :arg snap_normal:

      Normal

   :type snap_normal: float array of 3 items in [-inf, inf], (optional)
   :arg gpencil_strokes:

      Edit Grease Pencil, Edit selected Grease Pencil strokes

   :type gpencil_strokes: boolean, (optional)
   :arg release_confirm:

      Confirm on Release, Always confirm operation when releasing button

   :type release_confirm: boolean, (optional)
   :arg use_accurate:

      Accurate, Use accurate transformation

   :type use_accurate: boolean, (optional)

.. function:: shrink_fatten(value=0.0, use_even_offset=True, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Shrink/fatten selected vertices along normals

   :arg value:

      Offset

   :type value: float in [-inf, inf], (optional)
   :arg use_even_offset:

      Offset Even, Scale the offset to give more even thickness

   :type use_even_offset: boolean, (optional)
   :arg mirror:

      Mirror Editing

   :type mirror: boolean, (optional)
   :arg proportional:

      Proportional Editing

      * ``DISABLED`` Disable, Proportional Editing disabled.
      * ``ENABLED`` Enable, Proportional Editing enabled.
      * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations.
      * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.

   :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
   :arg proportional_edit_falloff:

      Proportional Editing Falloff, Falloff type for proportional editing mode

      * ``SMOOTH`` Smooth, Smooth falloff.
      * ``SPHERE`` Sphere, Spherical falloff.
      * ``ROOT`` Root, Root falloff.
      * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff.
      * ``SHARP`` Sharp, Sharp falloff.
      * ``LINEAR`` Linear, Linear falloff.
      * ``CONSTANT`` Constant, Constant falloff.
      * ``RANDOM`` Random, Random falloff.

   :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
   :arg proportional_size:

      Proportional Size

   :type proportional_size: float in [1e-06, inf], (optional)
   :arg snap:

      Use Snapping Options

   :type snap: boolean, (optional)
   :arg snap_target:

      Target

      * ``CLOSEST`` Closest, Snap closest point onto target.
      * ``CENTER`` Center, Snap center onto target.
      * ``MEDIAN`` Median, Snap median onto target.
      * ``ACTIVE`` Active, Snap active onto target.

   :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
   :arg snap_point:

      Point

   :type snap_point: float array of 3 items in [-inf, inf], (optional)
   :arg snap_align:

      Align with Point Normal

   :type snap_align: boolean, (optional)
   :arg snap_normal:

      Normal

   :type snap_normal: float array of 3 items in [-inf, inf], (optional)
   :arg release_confirm:

      Confirm on Release, Always confirm operation when releasing button

   :type release_confirm: boolean, (optional)
   :arg use_accurate:

      Accurate, Use accurate transformation

   :type use_accurate: boolean, (optional)

.. function:: skin_resize(value=(1.0, 1.0, 1.0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Scale selected vertices' skin radii

   :arg value:

      Vector

   :type value: float array of 3 items in [-inf, inf], (optional)
   :arg constraint_axis:

      Constraint Axis

   :type constraint_axis: boolean array of 3 items, (optional)
   :arg constraint_orientation:

      Orientation, Transformation orientation

   :type constraint_orientation: enum in [], (optional)
   :arg mirror:

      Mirror Editing

   :type mirror: boolean, (optional)
   :arg proportional:

      Proportional Editing

      * ``DISABLED`` Disable, Proportional Editing disabled.
      * ``ENABLED`` Enable, Proportional Editing enabled.
      * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations.
      * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.

   :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
   :arg proportional_edit_falloff:

      Proportional Editing Falloff, Falloff type for proportional editing mode

      * ``SMOOTH`` Smooth, Smooth falloff.
      * ``SPHERE`` Sphere, Spherical falloff.
      * ``ROOT`` Root, Root falloff.
      * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff.
      * ``SHARP`` Sharp, Sharp falloff.
      * ``LINEAR`` Linear, Linear falloff.
      * ``CONSTANT`` Constant, Constant falloff.
      * ``RANDOM`` Random, Random falloff.

   :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
   :arg proportional_size:

      Proportional Size

   :type proportional_size: float in [1e-06, inf], (optional)
   :arg snap:

      Use Snapping Options

   :type snap: boolean, (optional)
   :arg snap_target:

      Target

      * ``CLOSEST`` Closest, Snap closest point onto target.
      * ``CENTER`` Center, Snap center onto target.
      * ``MEDIAN`` Median, Snap median onto target.
      * ``ACTIVE`` Active, Snap active onto target.

   :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
   :arg snap_point:

      Point

   :type snap_point: float array of 3 items in [-inf, inf], (optional)
   :arg snap_align:

      Align with Point Normal

   :type snap_align: boolean, (optional)
   :arg snap_normal:

      Normal

   :type snap_normal: float array of 3 items in [-inf, inf], (optional)
   :arg release_confirm:

      Confirm on Release, Always confirm operation when releasing button

   :type release_confirm: boolean, (optional)
   :arg use_accurate:

      Accurate, Use accurate transformation

   :type use_accurate: boolean, (optional)

.. function:: tilt(value=0.0, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Tilt selected control vertices of 3D curve

   :arg value:

      Angle

   :type value: float in [-inf, inf], (optional)
   :arg mirror:

      Mirror Editing

   :type mirror: boolean, (optional)
   :arg proportional:

      Proportional Editing

      * ``DISABLED`` Disable, Proportional Editing disabled.
      * ``ENABLED`` Enable, Proportional Editing enabled.
      * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations.
      * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.

   :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
   :arg proportional_edit_falloff:

      Proportional Editing Falloff, Falloff type for proportional editing mode

      * ``SMOOTH`` Smooth, Smooth falloff.
      * ``SPHERE`` Sphere, Spherical falloff.
      * ``ROOT`` Root, Root falloff.
      * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff.
      * ``SHARP`` Sharp, Sharp falloff.
      * ``LINEAR`` Linear, Linear falloff.
      * ``CONSTANT`` Constant, Constant falloff.
      * ``RANDOM`` Random, Random falloff.

   :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
   :arg proportional_size:

      Proportional Size

   :type proportional_size: float in [1e-06, inf], (optional)
   :arg snap:

      Use Snapping Options

   :type snap: boolean, (optional)
   :arg snap_target:

      Target

      * ``CLOSEST`` Closest, Snap closest point onto target.
      * ``CENTER`` Center, Snap center onto target.
      * ``MEDIAN`` Median, Snap median onto target.
      * ``ACTIVE`` Active, Snap active onto target.

   :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
   :arg snap_point:

      Point

   :type snap_point: float array of 3 items in [-inf, inf], (optional)
   :arg snap_align:

      Align with Point Normal

   :type snap_align: boolean, (optional)
   :arg snap_normal:

      Normal

   :type snap_normal: float array of 3 items in [-inf, inf], (optional)
   :arg release_confirm:

      Confirm on Release, Always confirm operation when releasing button

   :type release_confirm: boolean, (optional)
   :arg use_accurate:

      Accurate, Use accurate transformation

   :type use_accurate: boolean, (optional)

.. function:: tosphere(value=0.0, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, center_override=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Move selected vertices outward in a spherical shape around mesh center

   :arg value:

      Factor

   :type value: float in [0, 1], (optional)
   :arg mirror:

      Mirror Editing

   :type mirror: boolean, (optional)
   :arg proportional:

      Proportional Editing

      * ``DISABLED`` Disable, Proportional Editing disabled.
      * ``ENABLED`` Enable, Proportional Editing enabled.
      * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations.
      * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.

   :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
   :arg proportional_edit_falloff:

      Proportional Editing Falloff, Falloff type for proportional editing mode

      * ``SMOOTH`` Smooth, Smooth falloff.
      * ``SPHERE`` Sphere, Spherical falloff.
      * ``ROOT`` Root, Root falloff.
      * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff.
      * ``SHARP`` Sharp, Sharp falloff.
      * ``LINEAR`` Linear, Linear falloff.
      * ``CONSTANT`` Constant, Constant falloff.
      * ``RANDOM`` Random, Random falloff.

   :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
   :arg proportional_size:

      Proportional Size

   :type proportional_size: float in [1e-06, inf], (optional)
   :arg snap:

      Use Snapping Options

   :type snap: boolean, (optional)
   :arg snap_target:

      Target

      * ``CLOSEST`` Closest, Snap closest point onto target.
      * ``CENTER`` Center, Snap center onto target.
      * ``MEDIAN`` Median, Snap median onto target.
      * ``ACTIVE`` Active, Snap active onto target.

   :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
   :arg snap_point:

      Point

   :type snap_point: float array of 3 items in [-inf, inf], (optional)
   :arg snap_align:

      Align with Point Normal

   :type snap_align: boolean, (optional)
   :arg snap_normal:

      Normal

   :type snap_normal: float array of 3 items in [-inf, inf], (optional)
   :arg gpencil_strokes:

      Edit Grease Pencil, Edit selected Grease Pencil strokes

   :type gpencil_strokes: boolean, (optional)
   :arg center_override:

      Center Override, Force using this center value (when set)

   :type center_override: float array of 3 items in [-inf, inf], (optional)
   :arg release_confirm:

      Confirm on Release, Always confirm operation when releasing button

   :type release_confirm: boolean, (optional)
   :arg use_accurate:

      Accurate, Use accurate transformation

   :type use_accurate: boolean, (optional)

.. function:: trackball(value=(0.0, 0.0), mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, center_override=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Trackball style rotation of selected items

   :arg value:

      Angle

   :type value: float array of 2 items in [-inf, inf], (optional)
   :arg mirror:

      Mirror Editing

   :type mirror: boolean, (optional)
   :arg proportional:

      Proportional Editing

      * ``DISABLED`` Disable, Proportional Editing disabled.
      * ``ENABLED`` Enable, Proportional Editing enabled.
      * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations.
      * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.

   :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
   :arg proportional_edit_falloff:

      Proportional Editing Falloff, Falloff type for proportional editing mode

      * ``SMOOTH`` Smooth, Smooth falloff.
      * ``SPHERE`` Sphere, Spherical falloff.
      * ``ROOT`` Root, Root falloff.
      * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff.
      * ``SHARP`` Sharp, Sharp falloff.
      * ``LINEAR`` Linear, Linear falloff.
      * ``CONSTANT`` Constant, Constant falloff.
      * ``RANDOM`` Random, Random falloff.

   :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
   :arg proportional_size:

      Proportional Size

   :type proportional_size: float in [1e-06, inf], (optional)
   :arg snap:

      Use Snapping Options

   :type snap: boolean, (optional)
   :arg snap_target:

      Target

      * ``CLOSEST`` Closest, Snap closest point onto target.
      * ``CENTER`` Center, Snap center onto target.
      * ``MEDIAN`` Median, Snap median onto target.
      * ``ACTIVE`` Active, Snap active onto target.

   :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
   :arg snap_point:

      Point

   :type snap_point: float array of 3 items in [-inf, inf], (optional)
   :arg snap_align:

      Align with Point Normal

   :type snap_align: boolean, (optional)
   :arg snap_normal:

      Normal

   :type snap_normal: float array of 3 items in [-inf, inf], (optional)
   :arg gpencil_strokes:

      Edit Grease Pencil, Edit selected Grease Pencil strokes

   :type gpencil_strokes: boolean, (optional)
   :arg center_override:

      Center Override, Force using this center value (when set)

   :type center_override: float array of 3 items in [-inf, inf], (optional)
   :arg release_confirm:

      Confirm on Release, Always confirm operation when releasing button

   :type release_confirm: boolean, (optional)
   :arg use_accurate:

      Accurate, Use accurate transformation

   :type use_accurate: boolean, (optional)

.. function:: transform(mode='TRANSLATION', value=(0.0, 0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, center_override=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Transform selected items by mode type

   :arg mode:

      Mode

   :type mode: enum in ['INIT', 'DUMMY', 'TRANSLATION', 'ROTATION', 'RESIZE', 'SKIN_RESIZE', 'TOSPHERE', 'SHEAR', 'BEND', 'SHRINKFATTEN', 'TILT', 'TRACKBALL', 'PUSHPULL', 'CREASE', 'MIRROR', 'BONE_SIZE', 'BONE_ENVELOPE', 'BONE_ENVELOPE_DIST', 'CURVE_SHRINKFATTEN', 'MASK_SHRINKFATTEN', 'GPENCIL_SHRINKFATTEN', 'BONE_ROLL', 'TIME_TRANSLATE', 'TIME_SLIDE', 'TIME_SCALE', 'TIME_EXTEND', 'BAKE_TIME', 'BWEIGHT', 'ALIGN', 'EDGESLIDE', 'SEQSLIDE'], (optional)
   :arg value:

      Values

   :type value: float array of 4 items in [-inf, inf], (optional)
   :arg axis:

      Axis, The axis around which the transformation occurs

   :type axis: float array of 3 items in [-inf, inf], (optional)
   :arg constraint_axis:

      Constraint Axis

   :type constraint_axis: boolean array of 3 items, (optional)
   :arg constraint_orientation:

      Orientation, Transformation orientation

   :type constraint_orientation: enum in [], (optional)
   :arg mirror:

      Mirror Editing

   :type mirror: boolean, (optional)
   :arg proportional:

      Proportional Editing

      * ``DISABLED`` Disable, Proportional Editing disabled.
      * ``ENABLED`` Enable, Proportional Editing enabled.
      * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations.
      * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.

   :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
   :arg proportional_edit_falloff:

      Proportional Editing Falloff, Falloff type for proportional editing mode

      * ``SMOOTH`` Smooth, Smooth falloff.
      * ``SPHERE`` Sphere, Spherical falloff.
      * ``ROOT`` Root, Root falloff.
      * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff.
      * ``SHARP`` Sharp, Sharp falloff.
      * ``LINEAR`` Linear, Linear falloff.
      * ``CONSTANT`` Constant, Constant falloff.
      * ``RANDOM`` Random, Random falloff.

   :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
   :arg proportional_size:

      Proportional Size

   :type proportional_size: float in [1e-06, inf], (optional)
   :arg snap:

      Use Snapping Options

   :type snap: boolean, (optional)
   :arg snap_target:

      Target

      * ``CLOSEST`` Closest, Snap closest point onto target.
      * ``CENTER`` Center, Snap center onto target.
      * ``MEDIAN`` Median, Snap median onto target.
      * ``ACTIVE`` Active, Snap active onto target.

   :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
   :arg snap_point:

      Point

   :type snap_point: float array of 3 items in [-inf, inf], (optional)
   :arg snap_align:

      Align with Point Normal

   :type snap_align: boolean, (optional)
   :arg snap_normal:

      Normal

   :type snap_normal: float array of 3 items in [-inf, inf], (optional)
   :arg gpencil_strokes:

      Edit Grease Pencil, Edit selected Grease Pencil strokes

   :type gpencil_strokes: boolean, (optional)
   :arg center_override:

      Center Override, Force using this center value (when set)

   :type center_override: float array of 3 items in [-inf, inf], (optional)
   :arg release_confirm:

      Confirm on Release, Always confirm operation when releasing button

   :type release_confirm: boolean, (optional)
   :arg use_accurate:

      Accurate, Use accurate transformation

   :type use_accurate: boolean, (optional)

.. function:: translate(value=(0.0, 0.0, 0.0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False, use_accurate=False)

   Translate (move) selected items

   :arg value:

      Vector

   :type value: float array of 3 items in [-inf, inf], (optional)
   :arg constraint_axis:

      Constraint Axis

   :type constraint_axis: boolean array of 3 items, (optional)
   :arg constraint_orientation:

      Orientation, Transformation orientation

   :type constraint_orientation: enum in [], (optional)
   :arg mirror:

      Mirror Editing

   :type mirror: boolean, (optional)
   :arg proportional:

      Proportional Editing

      * ``DISABLED`` Disable, Proportional Editing disabled.
      * ``ENABLED`` Enable, Proportional Editing enabled.
      * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations.
      * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.

   :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
   :arg proportional_edit_falloff:

      Proportional Editing Falloff, Falloff type for proportional editing mode

      * ``SMOOTH`` Smooth, Smooth falloff.
      * ``SPHERE`` Sphere, Spherical falloff.
      * ``ROOT`` Root, Root falloff.
      * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff.
      * ``SHARP`` Sharp, Sharp falloff.
      * ``LINEAR`` Linear, Linear falloff.
      * ``CONSTANT`` Constant, Constant falloff.
      * ``RANDOM`` Random, Random falloff.

   :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
   :arg proportional_size:

      Proportional Size

   :type proportional_size: float in [1e-06, inf], (optional)
   :arg snap:

      Use Snapping Options

   :type snap: boolean, (optional)
   :arg snap_target:

      Target

      * ``CLOSEST`` Closest, Snap closest point onto target.
      * ``CENTER`` Center, Snap center onto target.
      * ``MEDIAN`` Median, Snap median onto target.
      * ``ACTIVE`` Active, Snap active onto target.

   :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
   :arg snap_point:

      Point

   :type snap_point: float array of 3 items in [-inf, inf], (optional)
   :arg snap_align:

      Align with Point Normal

   :type snap_align: boolean, (optional)
   :arg snap_normal:

      Normal

   :type snap_normal: float array of 3 items in [-inf, inf], (optional)
   :arg gpencil_strokes:

      Edit Grease Pencil, Edit selected Grease Pencil strokes

   :type gpencil_strokes: boolean, (optional)
   :arg texture_space:

      Edit Texture Space, Edit Object data texture space

   :type texture_space: boolean, (optional)
   :arg remove_on_cancel:

      Remove on Cancel, Remove elements on cancel

   :type remove_on_cancel: boolean, (optional)
   :arg release_confirm:

      Confirm on Release, Always confirm operation when releasing button

   :type release_confirm: boolean, (optional)
   :arg use_accurate:

      Accurate, Use accurate transformation

   :type use_accurate: boolean, (optional)

.. function:: vert_slide(value=0.0, use_even=False, flipped=False, use_clamp=True, mirror=False, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), correct_uv=False, release_confirm=False, use_accurate=False)

   Slide a vertex along a mesh

   :arg value:

      Factor

   :type value: float in [-10, 10], (optional)
   :arg use_even:

      Even, Make the edge loop match the shape of the adjacent edge loop

   :type use_even: boolean, (optional)
   :arg flipped:

      Flipped, When Even mode is active, flips between the two adjacent edge loops

   :type flipped: boolean, (optional)
   :arg use_clamp:

      Clamp, Clamp within the edge extents

   :type use_clamp: boolean, (optional)
   :arg mirror:

      Mirror Editing

   :type mirror: boolean, (optional)
   :arg snap:

      Use Snapping Options

   :type snap: boolean, (optional)
   :arg snap_target:

      Target

      * ``CLOSEST`` Closest, Snap closest point onto target.
      * ``CENTER`` Center, Snap center onto target.
      * ``MEDIAN`` Median, Snap median onto target.
      * ``ACTIVE`` Active, Snap active onto target.

   :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
   :arg snap_point:

      Point

   :type snap_point: float array of 3 items in [-inf, inf], (optional)
   :arg snap_align:

      Align with Point Normal

   :type snap_align: boolean, (optional)
   :arg snap_normal:

      Normal

   :type snap_normal: float array of 3 items in [-inf, inf], (optional)
   :arg correct_uv:

      Correct UVs, Correct UV coordinates when transforming

   :type correct_uv: boolean, (optional)
   :arg release_confirm:

      Confirm on Release, Always confirm operation when releasing button

   :type release_confirm: boolean, (optional)
   :arg use_accurate:

      Accurate, Use accurate transformation

   :type use_accurate: boolean, (optional)

.. function:: vertex_random(offset=0.1, uniform=0.0, normal=0.0, seed=0)

   Randomize vertices

   :arg offset:

      Amount, Distance to offset

   :type offset: float in [-inf, inf], (optional)
   :arg uniform:

      Uniform, Increase for uniform offset distance

   :type uniform: float in [0, 1], (optional)
   :arg normal:

      normal, Align offset direction to normals

   :type normal: float in [0, 1], (optional)
   :arg seed:

      Random Seed, Seed for the random number generator

   :type seed: int in [0, 10000], (optional)

.. function:: vertex_warp(warp_angle=6.28319, offset_angle=0.0, min=-1, max=1.0, viewmat=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), center=(0.0, 0.0, 0.0))

   Warp vertices around the cursor

   :arg warp_angle:

      Warp Angle, Amount to warp about the cursor

   :type warp_angle: float in [-inf, inf], (optional)
   :arg offset_angle:

      Offset Angle, Angle to use as the basis for warping

   :type offset_angle: float in [-inf, inf], (optional)
   :arg min:

      Min

   :type min: float in [-inf, inf], (optional)
   :arg max:

      Max

   :type max: float in [-inf, inf], (optional)
   :arg viewmat:

      Matrix

   :type viewmat: float multi-dimensional array of 4 * 4 items in [-inf, inf], (optional)
   :arg center:

      Center

   :type center: float array of 3 items in [-inf, inf], (optional)


Gpencil Operators
=================

.. module:: bpy.ops.gpencil

.. function:: active_frame_delete()

   Delete the active frame for the active Grease Pencil Layer

.. function:: active_frames_delete_all()

   Delete the active frame(s) of all editable Grease Pencil layers

.. function:: blank_frame_add(all_layers=False)

   Insert a blank frame on the current frame (all subsequently existing frames, if any, are shifted right by one frame)

   :arg all_layers:

      All Layers, Create blank frame in all layers, not only active

   :type all_layers: boolean, (optional)

.. function:: brush_add()

   Add new Grease Pencil drawing brush for the active Grease Pencil data-block

.. function:: brush_change(brush='DEFAULT')

   Change active Grease Pencil drawing brush

   :arg brush:

      Grease Pencil Brush

   :type brush: enum in ['DEFAULT'], (optional)

.. function:: brush_copy()

   Copy current Grease Pencil drawing brush

.. function:: brush_move(type='UP')

   Move the active Grease Pencil drawing brush up/down in the list

   :arg type:

      Type

   :type type: enum in ['UP', 'DOWN'], (optional)

.. function:: brush_paint(stroke=None, wait_for_input=True)

   Apply tweaks to strokes by painting over the strokes

   :arg stroke:

      Stroke

   :type stroke: :class:`bpy_prop_collection` of :class:`OperatorStrokeElement`, (optional)
   :arg wait_for_input:

      Wait for Input, Enter a mini 'sculpt-mode' if enabled, otherwise, exit after drawing a single stroke

   :type wait_for_input: boolean, (optional)

.. function:: brush_presets_create()

   Create a set of predefined Grease Pencil drawing brushes

.. function:: brush_remove()

   Remove active Grease Pencil drawing brush

.. function:: brush_select(index=0)

   Select a Grease Pencil drawing brush

   :arg index:

      Index, Index of Drawing Brush

   :type index: int in [0, inf], (optional)

.. function:: convert(type='PATH', use_normalize_weights=True, radius_multiplier=1.0, use_link_strokes=True, timing_mode='FULL', frame_range=100, start_frame=1, use_realtime=False, end_frame=250, gap_duration=0.0, gap_randomness=0.0, seed=0, use_timing_data=False)

   Convert the active Grease Pencil layer to a new Curve Object

   :arg type:

      Type, Which type of curve to convert to

      * ``PATH`` Path, Animation path.
      * ``CURVE`` Bezier Curve, Smooth Bezier curve.
      * ``POLY`` Polygon Curve, Bezier curve with straight-line segments (vector handles).

   :type type: enum in ['PATH', 'CURVE', 'POLY'], (optional)
   :arg use_normalize_weights:

      Normalize Weight, Normalize weight (set from stroke width)

   :type use_normalize_weights: boolean, (optional)
   :arg radius_multiplier:

      Radius Fac, Multiplier for the points' radii (set from stroke width)

   :type radius_multiplier: float in [0, 1000], (optional)
   :arg use_link_strokes:

      Link Strokes, Whether to link strokes with zero-radius sections of curves

   :type use_link_strokes: boolean, (optional)
   :arg timing_mode:

      Timing Mode, How to use timing data stored in strokes

      * ``NONE`` No Timing, Ignore timing.
      * ``LINEAR`` Linear, Simple linear timing.
      * ``FULL`` Original, Use the original timing, gaps included.
      * ``CUSTOMGAP`` Custom Gaps, Use the original timing, but with custom gap lengths (in frames).

   :type timing_mode: enum in ['NONE', 'LINEAR', 'FULL', 'CUSTOMGAP'], (optional)
   :arg frame_range:

      Frame Range, The duration of evaluation of the path control curve

   :type frame_range: int in [1, 10000], (optional)
   :arg start_frame:

      Start Frame, The start frame of the path control curve

   :type start_frame: int in [1, 100000], (optional)
   :arg use_realtime:

      Realtime, Whether the path control curve reproduces the drawing in realtime, starting from Start Frame

   :type use_realtime: boolean, (optional)
   :arg end_frame:

      End Frame, The end frame of the path control curve (if Realtime is not set)

   :type end_frame: int in [1, 100000], (optional)
   :arg gap_duration:

      Gap Duration, Custom Gap mode: (Average) length of gaps, in frames (Note: Realtime value, will be scaled if Realtime is not set)

   :type gap_duration: float in [0, 10000], (optional)
   :arg gap_randomness:

      Gap Randomness, Custom Gap mode: Number of frames that gap lengths can vary

   :type gap_randomness: float in [0, 10000], (optional)
   :arg seed:

      Random Seed, Custom Gap mode: Random generator seed

   :type seed: int in [0, 1000], (optional)
   :arg use_timing_data:

      Has Valid Timing, Whether the converted Grease Pencil layer has valid timing data (internal use)

   :type use_timing_data: boolean, (optional)

.. function:: copy()

   Copy selected Grease Pencil points and strokes

.. function:: data_add()

   Add new Grease Pencil data-block

.. function:: data_unlink()

   Unlink active Grease Pencil data-block

.. function:: delete(type='POINTS')

   Delete selected Grease Pencil strokes, vertices, or frames

   :arg type:

      Type, Method used for deleting Grease Pencil data

      * ``POINTS`` Points, Delete selected points and split strokes into segments.
      * ``STROKES`` Strokes, Delete selected strokes.
      * ``FRAME`` Frame, Delete active frame.

   :type type: enum in ['POINTS', 'STROKES', 'FRAME'], (optional)

.. function:: dissolve()

   Delete selected points without splitting strokes

.. function:: draw(mode='DRAW', stroke=None, wait_for_input=True)

   Make annotations on the active data

   :arg mode:

      Mode, Way to interpret mouse movements

      * ``DRAW`` Draw Freehand, Draw freehand stroke(s).
      * ``DRAW_STRAIGHT`` Draw Straight Lines, Draw straight line segment(s).
      * ``DRAW_POLY`` Draw Poly Line, Click to place endpoints of straight line segments (connected).
      * ``ERASER`` Eraser, Erase Grease Pencil strokes.

   :type mode: enum in ['DRAW', 'DRAW_STRAIGHT', 'DRAW_POLY', 'ERASER'], (optional)
   :arg stroke:

      Stroke

   :type stroke: :class:`bpy_prop_collection` of :class:`OperatorStrokeElement`, (optional)
   :arg wait_for_input:

      Wait for Input, Wait for first click instead of painting immediately

   :type wait_for_input: boolean, (optional)

.. function:: duplicate()

   Duplicate the selected Grease Pencil strokes

.. function:: duplicate_move(GPENCIL_OT_duplicate=None, TRANSFORM_OT_translate=None)

   Make copies of the selected Grease Pencil strokes and move them

   :arg GPENCIL_OT_duplicate:

      Duplicate Strokes, Duplicate the selected Grease Pencil strokes

   :type GPENCIL_OT_duplicate: :class:`GPENCIL_OT_duplicate`, (optional)
   :arg TRANSFORM_OT_translate:

      Translate, Translate (move) selected items

   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: editmode_toggle()

   Enter/Exit edit mode for Grease Pencil strokes

.. function:: hide(unselected=False)

   Hide selected/unselected Grease Pencil layers

   :arg unselected:

      Unselected, Hide unselected rather than selected layers

   :type unselected: boolean, (optional)

.. function:: interpolate(shift=0.0)

   Interpolate grease pencil strokes between frames

   :arg shift:

      Shift, Bias factor for which frame has more influence on the interpolated strokes

   :type shift: float in [-1, 1], (optional)

.. function:: interpolate_reverse()

   Remove breakdown frames generated by interpolating between two Grease Pencil frames

.. function:: interpolate_sequence()

   Generate 'in-betweens' to smoothly interpolate between Grease Pencil frames

.. function:: layer_add()

   Add new Grease Pencil layer for the active Grease Pencil data-block

.. function:: layer_change(layer='DEFAULT')

   Change active Grease Pencil layer

   :arg layer:

      Grease Pencil Layer

   :type layer: enum in ['DEFAULT'], (optional)

.. function:: layer_duplicate()

   Make a copy of the active Grease Pencil layer

.. function:: layer_isolate(affect_visibility=False)

   Toggle whether the active layer is the only one that can be edited and/or visible

   :arg affect_visibility:

      Affect Visibility, In addition to toggling the editability, also affect the visibility

   :type affect_visibility: boolean, (optional)

.. function:: layer_merge()

   Merge the current layer with the layer below

.. function:: layer_move(type='UP')

   Move the active Grease Pencil layer up/down in the list

   :arg type:

      Type

   :type type: enum in ['UP', 'DOWN'], (optional)

.. function:: layer_remove()

   Remove active Grease Pencil layer

.. function:: lock_all()

   Lock all Grease Pencil layers to prevent them from being accidentally modified

.. function:: move_to_layer(layer='DEFAULT')

   Move selected strokes to another layer

   :arg layer:

      Grease Pencil Layer

   :type layer: enum in ['DEFAULT'], (optional)

.. function:: palette_add()

   Add new Grease Pencil palette for the active Grease Pencil data-block

.. function:: palette_change(palette='DEFAULT')

   Change active Grease Pencil palette

   :arg palette:

      Grease Pencil Palette

   :type palette: enum in ['DEFAULT'], (optional)

.. function:: palette_lock_layer()

   Lock and hide any color not used in any layer

.. function:: palette_remove()

   Remove active Grease Pencil palette

.. function:: palettecolor_add()

   Add new Grease Pencil palette color for the active Grease Pencil data-block

.. function:: palettecolor_copy()

   Copy current Grease Pencil palette color

.. function:: palettecolor_hide(unselected=False)

   Hide selected/unselected Grease Pencil colors

   :arg unselected:

      Unselected, Hide unselected rather than selected colors

   :type unselected: boolean, (optional)

.. function:: palettecolor_isolate(affect_visibility=False)

   Toggle whether the active color is the only one that is editable and/or visible

   :arg affect_visibility:

      Affect Visibility, In addition to toggling the editability, also affect the visibility

   :type affect_visibility: boolean, (optional)

.. function:: palettecolor_lock_all()

   Lock all Grease Pencil colors to prevent them from being accidentally modified

.. function:: palettecolor_move(direction='UP')

   Move the active Grease Pencil palette color up/down in the list

   :arg direction:

      Direction

   :type direction: enum in ['UP', 'DOWN'], (optional)

.. function:: palettecolor_remove()

   Remove active Grease Pencil palette color

.. function:: palettecolor_reveal()

   Unhide all hidden Grease Pencil palette colors

.. function:: palettecolor_select()

   Select all Grease Pencil strokes using current color

.. function:: palettecolor_unlock_all()

   Unlock all Grease Pencil colors so that they can be edited

.. function:: paste(type='COPY')

   Paste previously copied strokes or copy and merge in active layer

   :arg type:

      Type

   :type type: enum in ['COPY', 'MERGE'], (optional)

.. function:: reproject(type='PLANAR')

   Reproject the selected strokes from the current viewpoint as if they had been newly drawn (e.g. to fix problems from accidental 3D cursor movement or accidental viewport changes, or for matching deforming geometry)

   :arg type:

      Projection Type

      * ``PLANAR`` Planar, Reproject the strokes to end up on the same plane, as if drawn from the current viewpoint using 'Cursor' Stroke Placement.
      * ``SURFACE`` Surface, Reproject the strokes on to the scene geometry, as if drawn using 'Surface' placement.

   :type type: enum in ['PLANAR', 'SURFACE'], (optional)

.. function:: reveal(select=True)

   Show all Grease Pencil layers

   :arg select:

      Select

   :type select: boolean, (optional)

.. function:: select(extend=False, deselect=False, toggle=False, entire_strokes=False, location=(0, 0))

   Select Grease Pencil strokes and/or stroke points

   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)
   :arg deselect:

      Deselect, Remove from selection

   :type deselect: boolean, (optional)
   :arg toggle:

      Toggle Selection, Toggle the selection

   :type toggle: boolean, (optional)
   :arg entire_strokes:

      Entire Strokes, Select entire strokes instead of just the nearest stroke vertex

   :type entire_strokes: boolean, (optional)
   :arg location:

      Location, Mouse location

   :type location: int array of 2 items in [-inf, inf], (optional)

.. function:: select_all(action='TOGGLE')

   Change selection of all Grease Pencil strokes currently visible

   :arg action:

      Action, Selection action to execute

      * ``TOGGLE`` Toggle, Toggle selection for all elements.
      * ``SELECT`` Select, Select all elements.
      * ``DESELECT`` Deselect, Deselect all elements.
      * ``INVERT`` Invert, Invert selection of all elements.

   :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

.. function:: select_border(xmin=0, xmax=0, ymin=0, ymax=0, deselect=False, extend=True)

   Select Grease Pencil strokes within a rectangular region

   :arg xmin:

      X Min

   :type xmin: int in [-inf, inf], (optional)
   :arg xmax:

      X Max

   :type xmax: int in [-inf, inf], (optional)
   :arg ymin:

      Y Min

   :type ymin: int in [-inf, inf], (optional)
   :arg ymax:

      Y Max

   :type ymax: int in [-inf, inf], (optional)
   :arg deselect:

      Deselect, Deselect rather than select items

   :type deselect: boolean, (optional)
   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)

.. function:: select_circle(x=0, y=0, radius=25, deselect=False)

   Select Grease Pencil strokes using brush selection

   :arg x:

      X

   :type x: int in [-inf, inf], (optional)
   :arg y:

      Y

   :type y: int in [-inf, inf], (optional)
   :arg radius:

      Radius

   :type radius: int in [1, inf], (optional)
   :arg deselect:

      Deselect, Deselect rather than select items

   :type deselect: boolean, (optional)

.. function:: select_first(only_selected_strokes=False, extend=False)

   Select first point in Grease Pencil strokes

   :arg only_selected_strokes:

      Selected Strokes Only, Only select the first point of strokes that already have points selected

   :type only_selected_strokes: boolean, (optional)
   :arg extend:

      Extend, Extend selection instead of deselecting all other selected points

   :type extend: boolean, (optional)

.. function:: select_grouped(type='LAYER')

   Select all strokes with similar characteristics

   :arg type:

      Type

      * ``LAYER`` Layer, Shared layers.
      * ``COLOR`` Color, Shared colors.

   :type type: enum in ['LAYER', 'COLOR'], (optional)

.. function:: select_lasso(path=None, deselect=False, extend=True)

   Select Grease Pencil strokes using lasso selection

   :arg path:

      Path

   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg deselect:

      Deselect, Deselect rather than select items

   :type deselect: boolean, (optional)
   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)

.. function:: select_last(only_selected_strokes=False, extend=False)

   Select last point in Grease Pencil strokes

   :arg only_selected_strokes:

      Selected Strokes Only, Only select the last point of strokes that already have points selected

   :type only_selected_strokes: boolean, (optional)
   :arg extend:

      Extend, Extend selection instead of deselecting all other selected points

   :type extend: boolean, (optional)

.. function:: select_less()

   Shrink sets of selected Grease Pencil points

.. function:: select_linked()

   Select all points in same strokes as already selected points

.. function:: select_more()

   Grow sets of selected Grease Pencil points

.. function:: selection_opacity_toggle()

   Hide/Unhide selected points for Grease Pencil strokes setting alpha factor

.. function:: snap_cursor_to_selected()

   Snap cursor to center of selected points

.. function:: snap_to_cursor(use_offset=True)

   Snap selected points/strokes to the cursor

   :arg use_offset:

      With Offset, Offset the entire stroke instead of selected points only

   :type use_offset: boolean, (optional)

.. function:: snap_to_grid()

   Snap selected points to the nearest grid points

.. function:: stroke_apply_thickness()

   Apply the thickness change of the layer to its strokes

.. function:: stroke_arrange(direction='UP')

   Arrange selected strokes up/down in the drawing order of the active layer

   :arg direction:

      Direction

   :type direction: enum in ['UP', 'DOWN', 'TOP', 'BOTTOM'], (optional)

.. function:: stroke_change_color()

   Move selected strokes to active color

.. function:: stroke_cyclical_set(type='TOGGLE')

   Close or open the selected stroke adding an edge from last to first point

   :arg type:

      Type

   :type type: enum in ['CLOSE', 'OPEN', 'TOGGLE'], (optional)

.. function:: stroke_flip()

   Change direction of the points of the selected strokes

.. function:: stroke_join(type='JOIN', leave_gaps=False)

   Join selected strokes (optionally as new stroke)

   :arg type:

      Type

   :type type: enum in ['JOIN', 'JOINCOPY'], (optional)
   :arg leave_gaps:

      Leave Gaps, Leave gaps between joined strokes instead of linking them

   :type leave_gaps: boolean, (optional)

.. function:: stroke_lock_color()

   Lock any color not used in any selected stroke

.. function:: stroke_subdivide(number_cuts=1)

   Subdivide between continuous selected points of the stroke adding a point half way between them

   :arg number_cuts:

      Number of Cuts

   :type number_cuts: int in [1, 10], (optional)

.. function:: unlock_all()

   Unlock all Grease Pencil layers so that they can be edited


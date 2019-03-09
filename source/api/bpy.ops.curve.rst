Curve Operators
===============

.. module:: bpy.ops.curve

.. function:: cyclic_toggle(direction='CYCLIC_U')

   Make active spline closed/opened loop

   :arg direction:

      Direction, Direction to make surface cyclic in

   :type direction: enum in ['CYCLIC_U', 'CYCLIC_V'], (optional)

.. function:: de_select_first()

   (De)select first of visible part of each NURBS

.. function:: de_select_last()

   (De)select last of visible part of each NURBS

.. function:: decimate(ratio=1.0)

   Simplify selected curves

   :arg ratio:

      Ratio

   :type ratio: float in [0, 1], (optional)

.. function:: delete(type='VERT')

   Delete selected control points or segments

   :arg type:

      Type, Which elements to delete

   :type type: enum in ['VERT', 'SEGMENT'], (optional)

.. function:: dissolve_verts()

   Delete selected control points, correcting surrounding handles

.. function:: draw(error_threshold=0.0, fit_method='REFIT', corner_angle=1.22173, use_cyclic=True, stroke=None, wait_for_input=True)

   Draw a freehand spline

   :arg error_threshold:

      Error, Error distance threshold (in object units)

   :type error_threshold: float in [0, 10], (optional)
   :arg fit_method:

      Fit Method

      * ``REFIT`` Refit, Incrementally re-fit the curve (high quality).
      * ``SPLIT`` Split, Split the curve until the tolerance is met (fast).

   :type fit_method: enum in ['REFIT', 'SPLIT'], (optional)
   :arg corner_angle:

      Corner Angle

   :type corner_angle: float in [0, 3.14159], (optional)
   :arg use_cyclic:

      Cyclic

   :type use_cyclic: boolean, (optional)
   :arg stroke:

      Stroke

   :type stroke: :class:`bpy_prop_collection` of :class:`OperatorStrokeElement`, (optional)
   :arg wait_for_input:

      Wait for Input

   :type wait_for_input: boolean, (optional)

.. function:: duplicate()

   Duplicate selected control points

.. function:: duplicate_move(CURVE_OT_duplicate=None, TRANSFORM_OT_translate=None)

   Duplicate curve and move

   :arg CURVE_OT_duplicate:

      Duplicate Curve, Duplicate selected control points

   :type CURVE_OT_duplicate: :class:`CURVE_OT_duplicate`, (optional)
   :arg TRANSFORM_OT_translate:

      Translate, Translate (move) selected items

   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: extrude(mode='TRANSLATION')

   Extrude selected control point(s)

   :arg mode:

      Mode

   :type mode: enum in ['INIT', 'DUMMY', 'TRANSLATION', 'ROTATION', 'RESIZE', 'SKIN_RESIZE', 'TOSPHERE', 'SHEAR', 'BEND', 'SHRINKFATTEN', 'TILT', 'TRACKBALL', 'PUSHPULL', 'CREASE', 'MIRROR', 'BONE_SIZE', 'BONE_ENVELOPE', 'BONE_ENVELOPE_DIST', 'CURVE_SHRINKFATTEN', 'MASK_SHRINKFATTEN', 'GPENCIL_SHRINKFATTEN', 'BONE_ROLL', 'TIME_TRANSLATE', 'TIME_SLIDE', 'TIME_SCALE', 'TIME_EXTEND', 'BAKE_TIME', 'BWEIGHT', 'ALIGN', 'EDGESLIDE', 'SEQSLIDE'], (optional)

.. function:: extrude_move(CURVE_OT_extrude=None, TRANSFORM_OT_translate=None)

   Extrude curve and move result

   :arg CURVE_OT_extrude:

      Extrude, Extrude selected control point(s)

   :type CURVE_OT_extrude: :class:`CURVE_OT_extrude`, (optional)
   :arg TRANSFORM_OT_translate:

      Translate, Translate (move) selected items

   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: handle_type_set(type='AUTOMATIC')

   Set type of handles for selected control points

   :arg type:

      Type, Spline type

   :type type: enum in ['AUTOMATIC', 'VECTOR', 'ALIGNED', 'FREE_ALIGN', 'TOGGLE_FREE_ALIGN'], (optional)

.. function:: hide(unselected=False)

   Hide (un)selected control points

   :arg unselected:

      Unselected, Hide unselected rather than selected

   :type unselected: boolean, (optional)

.. function:: make_segment()

   Join two curves by their selected ends

.. function:: match_texture_space()

   Match texture space to object's bounding box

.. function:: normals_make_consistent(calc_length=False)

   Recalculate the direction of selected handles

   :arg calc_length:

      Length, Recalculate handle length

   :type calc_length: boolean, (optional)

.. function:: primitive_bezier_circle_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

   Construct a Bezier Circle

   :arg radius:

      Radius

   :type radius: float in [0, inf], (optional)
   :arg view_align:

      Align to View, Align the new object to the view

   :type view_align: boolean, (optional)
   :arg enter_editmode:

      Enter Editmode, Enter editmode when adding this object

   :type enter_editmode: boolean, (optional)
   :arg location:

      Location, Location for the newly added object

   :type location: float array of 3 items in [-inf, inf], (optional)
   :arg rotation:

      Rotation, Rotation for the newly added object

   :type rotation: float array of 3 items in [-inf, inf], (optional)
   :arg layers:

      Layer

   :type layers: boolean array of 20 items, (optional)

.. function:: primitive_bezier_curve_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

   Construct a Bezier Curve

   :arg radius:

      Radius

   :type radius: float in [0, inf], (optional)
   :arg view_align:

      Align to View, Align the new object to the view

   :type view_align: boolean, (optional)
   :arg enter_editmode:

      Enter Editmode, Enter editmode when adding this object

   :type enter_editmode: boolean, (optional)
   :arg location:

      Location, Location for the newly added object

   :type location: float array of 3 items in [-inf, inf], (optional)
   :arg rotation:

      Rotation, Rotation for the newly added object

   :type rotation: float array of 3 items in [-inf, inf], (optional)
   :arg layers:

      Layer

   :type layers: boolean array of 20 items, (optional)

.. function:: primitive_nurbs_circle_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

   Construct a Nurbs Circle

   :arg radius:

      Radius

   :type radius: float in [0, inf], (optional)
   :arg view_align:

      Align to View, Align the new object to the view

   :type view_align: boolean, (optional)
   :arg enter_editmode:

      Enter Editmode, Enter editmode when adding this object

   :type enter_editmode: boolean, (optional)
   :arg location:

      Location, Location for the newly added object

   :type location: float array of 3 items in [-inf, inf], (optional)
   :arg rotation:

      Rotation, Rotation for the newly added object

   :type rotation: float array of 3 items in [-inf, inf], (optional)
   :arg layers:

      Layer

   :type layers: boolean array of 20 items, (optional)

.. function:: primitive_nurbs_curve_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

   Construct a Nurbs Curve

   :arg radius:

      Radius

   :type radius: float in [0, inf], (optional)
   :arg view_align:

      Align to View, Align the new object to the view

   :type view_align: boolean, (optional)
   :arg enter_editmode:

      Enter Editmode, Enter editmode when adding this object

   :type enter_editmode: boolean, (optional)
   :arg location:

      Location, Location for the newly added object

   :type location: float array of 3 items in [-inf, inf], (optional)
   :arg rotation:

      Rotation, Rotation for the newly added object

   :type rotation: float array of 3 items in [-inf, inf], (optional)
   :arg layers:

      Layer

   :type layers: boolean array of 20 items, (optional)

.. function:: primitive_nurbs_path_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

   Construct a Path

   :arg radius:

      Radius

   :type radius: float in [0, inf], (optional)
   :arg view_align:

      Align to View, Align the new object to the view

   :type view_align: boolean, (optional)
   :arg enter_editmode:

      Enter Editmode, Enter editmode when adding this object

   :type enter_editmode: boolean, (optional)
   :arg location:

      Location, Location for the newly added object

   :type location: float array of 3 items in [-inf, inf], (optional)
   :arg rotation:

      Rotation, Rotation for the newly added object

   :type rotation: float array of 3 items in [-inf, inf], (optional)
   :arg layers:

      Layer

   :type layers: boolean array of 20 items, (optional)

.. function:: radius_set(radius=1.0)

   Set per-point radius which is used for bevel tapering

   :arg radius:

      Radius

   :type radius: float in [0, inf], (optional)

.. function:: reveal(select=True)

   Reveal hidden control points

   :arg select:

      Select

   :type select: boolean, (optional)

.. function:: select_all(action='TOGGLE')

   (De)select all control points

   :arg action:

      Action, Selection action to execute

      * ``TOGGLE`` Toggle, Toggle selection for all elements.
      * ``SELECT`` Select, Select all elements.
      * ``DESELECT`` Deselect, Deselect all elements.
      * ``INVERT`` Invert, Invert selection of all elements.

   :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

.. function:: select_less()

   Reduce current selection by deselecting boundary elements

.. function:: select_linked()

   Select all control points linked to active one

.. function:: select_linked_pick(deselect=False)

   Select all control points linked to already selected ones

   :arg deselect:

      Deselect, Deselect linked control points rather than selecting them

   :type deselect: boolean, (optional)

.. function:: select_more()

   Select control points directly linked to already selected ones

.. function:: select_next()

   Select control points following already selected ones along the curves

.. function:: select_nth(nth=2, skip=1, offset=0)

   Deselect every other vertex

   :arg nth:

      Nth Selection

   :type nth: int in [2, inf], (optional)
   :arg skip:

      Skip

   :type skip: int in [1, inf], (optional)
   :arg offset:

      Offset

   :type offset: int in [-inf, inf], (optional)

.. function:: select_previous()

   Select control points preceding already selected ones along the curves

.. function:: select_random(percent=50.0, seed=0, action='SELECT')

   Randomly select some control points

   :arg percent:

      Percent, Percentage of objects to select randomly

   :type percent: float in [0, 100], (optional)
   :arg seed:

      Random Seed, Seed for the random number generator

   :type seed: int in [0, inf], (optional)
   :arg action:

      Action, Selection action to execute

      * ``SELECT`` Select, Select all elements.
      * ``DESELECT`` Deselect, Deselect all elements.

   :type action: enum in ['SELECT', 'DESELECT'], (optional)

.. function:: select_row()

   Select a row of control points including active one

.. function:: select_similar(type='WEIGHT', compare='EQUAL', threshold=0.1)

   Select similar curve points by property type

   :arg type:

      Type

   :type type: enum in ['TYPE', 'RADIUS', 'WEIGHT', 'DIRECTION'], (optional)
   :arg compare:

      Compare

   :type compare: enum in ['EQUAL', 'GREATER', 'LESS'], (optional)
   :arg threshold:

      Threshold

   :type threshold: float in [0, inf], (optional)

.. function:: separate()

   Separate selected points from connected unselected points into a new object

.. function:: shade_flat()

   Set shading to flat

.. function:: shade_smooth()

   Set shading to smooth

.. function:: shortest_path_pick()

   Select shortest path between two selections

.. function:: smooth()

   Flatten angles of selected points

.. function:: smooth_radius()

   Interpolate radii of selected points

.. function:: smooth_tilt()

   Interpolate tilt of selected points

.. function:: smooth_weight()

   Interpolate weight of selected points

.. function:: spin(center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0))

   Extrude selected boundary row around pivot point and current view axis

   :arg center:

      Center, Center in global view space

   :type center: float array of 3 items in [-inf, inf], (optional)
   :arg axis:

      Axis, Axis in global view space

   :type axis: float array of 3 items in [-1, 1], (optional)

.. function:: spline_type_set(type='POLY', use_handles=False)

   Set type of active spline

   :arg type:

      Type, Spline type

   :type type: enum in ['POLY', 'BEZIER', 'NURBS'], (optional)
   :arg use_handles:

      Handles, Use handles when converting bezier curves into polygons

   :type use_handles: boolean, (optional)

.. function:: spline_weight_set(weight=1.0)

   Set softbody goal weight for selected points

   :arg weight:

      Weight

   :type weight: float in [0, 1], (optional)

.. function:: split()

   Split off selected points from connected unselected points

.. function:: subdivide(number_cuts=1)

   Subdivide selected segments

   :arg number_cuts:

      Number of cuts

   :type number_cuts: int in [1, 1000], (optional)

.. function:: switch_direction()

   Switch direction of selected splines

.. function:: tilt_clear()

   Clear the tilt of selected control points

.. function:: vertex_add(location=(0.0, 0.0, 0.0))

   Add a new control point (linked to only selected end-curve one, if any)

   :arg location:

      Location, Location to add new vertex at

   :type location: float array of 3 items in [-inf, inf], (optional)


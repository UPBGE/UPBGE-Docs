Action Operators
================

.. module:: bpy.ops.action

.. function:: clean(threshold=0.001, channels=False)

   Simplify F-Curves by removing closely spaced keyframes

   :arg threshold:

      Threshold

   :type threshold: float in [0, inf], (optional)
   :arg channels:

      Channels

   :type channels: boolean, (optional)

.. function:: clickselect(extend=False, column=False, channel=False)

   Select keyframes by clicking on them

   :arg extend:

      Extend Select, Toggle keyframe selection instead of leaving newly selected keyframes only

   :type extend: boolean, (optional)
   :arg column:

      Column Select, Select all keyframes that occur on the same frame as the one under the mouse

   :type column: boolean, (optional)
   :arg channel:

      Only Channel, Select all the keyframes in the channel under the mouse

   :type channel: boolean, (optional)

.. function:: copy()

   Copy selected keyframes to the copy/paste buffer

.. function:: delete()

   Remove all selected keyframes

.. function:: duplicate()

   Make a copy of all selected keyframes

.. function:: duplicate_move(ACTION_OT_duplicate=None, TRANSFORM_OT_transform=None)

   Make a copy of all selected keyframes and move them

   :arg ACTION_OT_duplicate:

      Duplicate Keyframes, Make a copy of all selected keyframes

   :type ACTION_OT_duplicate: :class:`ACTION_OT_duplicate`, (optional)
   :arg TRANSFORM_OT_transform:

      Transform, Transform selected items by mode type

   :type TRANSFORM_OT_transform: :class:`TRANSFORM_OT_transform`, (optional)

.. function:: extrapolation_type(type='CONSTANT')

   Set extrapolation mode for selected F-Curves

   :arg type:

      Type

      * ``CONSTANT`` Constant Extrapolation, Values on endpoint keyframes are held.
      * ``LINEAR`` Linear Extrapolation, Straight-line slope of end segments are extended past the endpoint keyframes.
      * ``MAKE_CYCLIC`` Make Cyclic (F-Modifier), Add Cycles F-Modifier if one doesn't exist already.
      * ``CLEAR_CYCLIC`` Clear Cyclic (F-Modifier), Remove Cycles F-Modifier if not needed anymore.

   :type type: enum in ['CONSTANT', 'LINEAR', 'MAKE_CYCLIC', 'CLEAR_CYCLIC'], (optional)

.. function:: frame_jump()

   Set the current frame to the average frame value of selected keyframes

.. function:: handle_type(type='FREE')

   Set type of handle for selected keyframes

   :arg type:

      Type

      * ``FREE`` Free.
      * ``VECTOR`` Vector.
      * ``ALIGNED`` Aligned.
      * ``AUTO`` Automatic.
      * ``AUTO_CLAMPED`` Auto Clamped, Auto handles clamped to not overshoot.

   :type type: enum in ['FREE', 'VECTOR', 'ALIGNED', 'AUTO', 'AUTO_CLAMPED'], (optional)

.. function:: interpolation_type(type='CONSTANT')

   Set interpolation mode for the F-Curve segments starting from the selected keyframes

   :arg type:

      Type

      * ``CONSTANT`` Constant, No interpolation, value of A gets held until B is encountered.
      * ``LINEAR`` Linear, Straight-line interpolation between A and B (i.e. no ease in/out).
      * ``BEZIER`` Bezier, Smooth interpolation between A and B, with some control over curve shape.
      * ``SINE`` Sinusoidal, Sinusoidal easing (weakest, almost linear but with a slight curvature).
      * ``QUAD`` Quadratic, Quadratic easing.
      * ``CUBIC`` Cubic, Cubic easing.
      * ``QUART`` Quartic, Quartic easing.
      * ``QUINT`` Quintic, Quintic easing.
      * ``EXPO`` Exponential, Exponential easing (dramatic).
      * ``CIRC`` Circular, Circular easing (strongest and most dynamic).
      * ``BACK`` Back, Cubic easing with overshoot and settle.
      * ``BOUNCE`` Bounce, Exponentially decaying parabolic bounce, like when objects collide.
      * ``ELASTIC`` Elastic, Exponentially decaying sine wave, like an elastic band.

   :type type: enum in ['CONSTANT', 'LINEAR', 'BEZIER', 'SINE', 'QUAD', 'CUBIC', 'QUART', 'QUINT', 'EXPO', 'CIRC', 'BACK', 'BOUNCE', 'ELASTIC'], (optional)

.. function:: keyframe_insert(type='ALL')

   Insert keyframes for the specified channels

   :arg type:

      Type

   :type type: enum in ['ALL', 'SEL', 'GROUP'], (optional)

.. function:: keyframe_type(type='KEYFRAME')

   Set type of keyframe for the selected keyframes

   :arg type:

      Type

      * ``KEYFRAME`` Keyframe, Normal keyframe - e.g. for key poses.
      * ``BREAKDOWN`` Breakdown, A breakdown pose - e.g. for transitions between key poses.
      * ``MOVING_HOLD`` Moving Hold, A keyframe that is part of a moving hold.
      * ``EXTREME`` Extreme, An 'extreme' pose, or some other purpose as needed.
      * ``JITTER`` Jitter, A filler or baked keyframe for keying on ones, or some other purpose as needed.

   :type type: enum in ['KEYFRAME', 'BREAKDOWN', 'MOVING_HOLD', 'EXTREME', 'JITTER'], (optional)

.. function:: layer_next()

   Switch to editing action in animation layer above the current action in the NLA Stack

.. function:: layer_prev()

   Switch to editing action in animation layer below the current action in the NLA Stack

.. function:: markers_make_local()

   Move selected scene markers to the active Action as local 'pose' markers

.. function:: mirror(type='CFRA')

   Flip selected keyframes over the selected mirror line

   :arg type:

      Type

      * ``CFRA`` By Times over Current frame, Flip times of selected keyframes using the current frame as the mirror line.
      * ``XAXIS`` By Values over Value=0, Flip values of selected keyframes (i.e. negative values become positive, and vice versa).
      * ``MARKER`` By Times over First Selected Marker, Flip times of selected keyframes using the first selected marker as the reference point.

   :type type: enum in ['CFRA', 'XAXIS', 'MARKER'], (optional)

.. function:: new()

   Create new action

.. function:: paste(offset='START', merge='MIX', flipped=False)

   Paste keyframes from copy/paste buffer for the selected channels, starting on the current frame

   :arg offset:

      Offset, Paste time offset of keys

      * ``START`` Frame Start, Paste keys starting at current frame.
      * ``END`` Frame End, Paste keys ending at current frame.
      * ``RELATIVE`` Frame Relative, Paste keys relative to the current frame when copying.
      * ``NONE`` No Offset, Paste keys from original time.

   :type offset: enum in ['START', 'END', 'RELATIVE', 'NONE'], (optional)
   :arg merge:

      Type, Method of merging pasted keys and existing

      * ``MIX`` Mix, Overlay existing with new keys.
      * ``OVER_ALL`` Overwrite All, Replace all keys.
      * ``OVER_RANGE`` Overwrite Range, Overwrite keys in pasted range.
      * ``OVER_RANGE_ALL`` Overwrite Entire Range, Overwrite keys in pasted range, using the range of all copied keys.

   :type merge: enum in ['MIX', 'OVER_ALL', 'OVER_RANGE', 'OVER_RANGE_ALL'], (optional)
   :arg flipped:

      Flipped, Paste keyframes from mirrored bones if they exist

   :type flipped: boolean, (optional)

.. function:: previewrange_set()

   Set Preview Range based on extents of selected Keyframes

.. function:: properties()

   Toggle the properties region visibility

.. function:: push_down()

   Push action down on to the NLA stack as a new strip

.. function:: sample()

   Add keyframes on every frame between the selected keyframes

.. function:: select_all_toggle(invert=False)

   Toggle selection of all keyframes

   :arg invert:

      Invert

   :type invert: boolean, (optional)

.. function:: select_border(xmin=0, xmax=0, ymin=0, ymax=0, deselect=False, extend=True, axis_range=False)

   Select all keyframes within the specified region

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
   :arg axis_range:

      Axis Range

   :type axis_range: boolean, (optional)

.. function:: select_circle(x=0, y=0, radius=25, deselect=False)

   Select keyframe points using circle selection

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

.. function:: select_column(mode='KEYS')

   Select all keyframes on the specified frame(s)

   :arg mode:

      Mode

   :type mode: enum in ['KEYS', 'CFRA', 'MARKERS_COLUMN', 'MARKERS_BETWEEN'], (optional)

.. function:: select_lasso(path=None, deselect=False, extend=True)

   Select keyframe points using lasso selection

   :arg path:

      Path

   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg deselect:

      Deselect, Deselect rather than select items

   :type deselect: boolean, (optional)
   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)

.. function:: select_leftright(mode='CHECK', extend=False)

   Select keyframes to the left or the right of the current frame

   :arg mode:

      Mode

   :type mode: enum in ['CHECK', 'LEFT', 'RIGHT'], (optional)
   :arg extend:

      Extend Select

   :type extend: boolean, (optional)

.. function:: select_less()

   Deselect keyframes on ends of selection islands

.. function:: select_linked()

   Select keyframes occurring in the same F-Curves as selected ones

.. function:: select_more()

   Select keyframes beside already selected ones

.. function:: snap(type='CFRA')

   Snap selected keyframes to the times specified

   :arg type:

      Type

      * ``CFRA`` Current frame, Snap selected keyframes to the current frame.
      * ``NEAREST_FRAME`` Nearest Frame, Snap selected keyframes to the nearest (whole) frame (use to fix accidental sub-frame offsets).
      * ``NEAREST_SECOND`` Nearest Second, Snap selected keyframes to the nearest second.
      * ``NEAREST_MARKER`` Nearest Marker, Snap selected keyframes to the nearest marker.

   :type type: enum in ['CFRA', 'NEAREST_FRAME', 'NEAREST_SECOND', 'NEAREST_MARKER'], (optional)

.. function:: stash(create_new=True)

   Store this action in the NLA stack as a non-contributing strip for later use

   :arg create_new:

      Create New Action, Create a new action once the existing one has been safely stored

   :type create_new: boolean, (optional)

.. function:: stash_and_create()

   Store this action in the NLA stack as a non-contributing strip for later use, and create a new action

.. function:: unlink(force_delete=False)

   Unlink this action from the active action slot (and/or exit Tweak Mode)

   :arg force_delete:

      Force Delete, Clear Fake User and remove copy stashed in this data-block's NLA stack

   :type force_delete: boolean, (optional)

.. function:: view_all()

   Reset viewable area to show full keyframe range

.. function:: view_frame()

   Reset viewable area to show range around current frame

.. function:: view_selected()

   Reset viewable area to show selected keyframes range


Nla Operators
=============

.. module:: bpy.ops.nla

.. function:: action_pushdown(channel_index=-1)

   Push action down onto the top of the NLA stack as a new strip

   :arg channel_index:

      Channel Index, Index of NLA action channel to perform pushdown operation on

   :type channel_index: int in [-1, inf], (optional)

.. function:: action_sync_length(active=True)

   Synchronize the length of the referenced Action with the length used in the strip

   :arg active:

      Active Strip Only, Only sync the active length for the active strip

   :type active: boolean, (optional)

.. function:: action_unlink(force_delete=False)

   Unlink this action from the active action slot (and/or exit Tweak Mode)

   :arg force_delete:

      Force Delete, Clear Fake User and remove copy stashed in this datablock's NLA stack

   :type force_delete: boolean, (optional)

.. function:: actionclip_add(action='')

   Add an Action-Clip strip (i.e. an NLA Strip referencing an Action) to the active track

   :arg action:

      Action

   :type action: enum in [], (optional)

.. function:: apply_scale()

   Apply scaling of selected strips to their referenced Actions

.. function:: bake(frame_start=1, frame_end=250, step=1, only_selected=True, visual_keying=False, clear_constraints=False, clear_parents=False, use_current_action=False, bake_types={'POSE'})

   Bake all selected objects loc/scale/rotation animation to an action

   :arg frame_start:

      Start Frame, Start frame for baking

   :type frame_start: int in [0, 300000], (optional)
   :arg frame_end:

      End Frame, End frame for baking

   :type frame_end: int in [1, 300000], (optional)
   :arg step:

      Frame Step, Frame Step

   :type step: int in [1, 120], (optional)
   :arg only_selected:

      Only Selected Bones, Only key selected bones (Pose baking only)

   :type only_selected: boolean, (optional)
   :arg visual_keying:

      Visual Keying, Keyframe from the final transformations (with constraints applied)

   :type visual_keying: boolean, (optional)
   :arg clear_constraints:

      Clear Constraints, Remove all constraints from keyed object/bones, and do 'visual' keying

   :type clear_constraints: boolean, (optional)
   :arg clear_parents:

      Clear Parents, Bake animation onto the object then clear parents (objects only)

   :type clear_parents: boolean, (optional)
   :arg use_current_action:

      Overwrite Current Action, Bake animation into current action, instead of creating a new one (useful for baking only part of bones in an armature)

   :type use_current_action: boolean, (optional)
   :arg bake_types:

      Bake Data, Which data's transformations to bake

      * ``POSE`` Pose, Bake bones transformations.
      * ``OBJECT`` Object, Bake object transformations.

   :type bake_types: enum set in {'POSE', 'OBJECT'}, (optional)

   :file: `startup\bl_operators\anim.py\:260 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\anim.py$260>`_

.. function:: channels_click(extend=False)

   Handle clicks to select NLA channels

   :arg extend:

      Extend Select

   :type extend: boolean, (optional)

.. function:: clear_scale()

   Reset scaling of selected strips

.. function:: click_select(extend=False)

   Handle clicks to select NLA Strips

   :arg extend:

      Extend Select

   :type extend: boolean, (optional)

.. function:: delete()

   Delete selected strips

.. function:: duplicate(linked=False, mode='TRANSLATION')

   Duplicate selected NLA-Strips, adding the new strips in new tracks above the originals

   :arg linked:

      Linked, When duplicating strips, assign new copies of the actions they use

   :type linked: boolean, (optional)
   :arg mode:

      Mode

   :type mode: enum in ['INIT', 'DUMMY', 'TRANSLATION', 'ROTATION', 'RESIZE', 'SKIN_RESIZE', 'TOSPHERE', 'SHEAR', 'BEND', 'SHRINKFATTEN', 'TILT', 'TRACKBALL', 'PUSHPULL', 'CREASE', 'MIRROR', 'BONE_SIZE', 'BONE_ENVELOPE', 'BONE_ENVELOPE_DIST', 'CURVE_SHRINKFATTEN', 'MASK_SHRINKFATTEN', 'GPENCIL_SHRINKFATTEN', 'BONE_ROLL', 'TIME_TRANSLATE', 'TIME_SLIDE', 'TIME_SCALE', 'TIME_EXTEND', 'BAKE_TIME', 'BWEIGHT', 'ALIGN', 'EDGESLIDE', 'SEQSLIDE'], (optional)

.. function:: fmodifier_add(type='NULL', only_active=True)

   Add F-Modifier to the active/selected NLA-Strips

   :arg type:

      Type

      * ``NULL`` Invalid.
      * ``GENERATOR`` Generator, Generate a curve using a factorized or expanded polynomial.
      * ``FNGENERATOR`` Built-In Function, Generate a curve using standard math functions such as sin and cos.
      * ``ENVELOPE`` Envelope, Reshape F-Curve values - e.g. change amplitude of movements.
      * ``CYCLES`` Cycles, Cyclic extend/repeat keyframe sequence.
      * ``NOISE`` Noise, Add pseudo-random noise on top of F-Curves.
      * ``LIMITS`` Limits, Restrict maximum and minimum values of F-Curve.
      * ``STEPPED`` Stepped Interpolation, Snap values to nearest grid-step - e.g. for a stop-motion look.

   :type type: enum in ['NULL', 'GENERATOR', 'FNGENERATOR', 'ENVELOPE', 'CYCLES', 'NOISE', 'LIMITS', 'STEPPED'], (optional)
   :arg only_active:

      Only Active, Only add a F-Modifier of the specified type to the active strip

   :type only_active: boolean, (optional)

.. function:: fmodifier_copy()

   Copy the F-Modifier(s) of the active NLA-Strip

.. function:: fmodifier_paste(only_active=True, replace=False)

   Add copied F-Modifiers to the selected NLA-Strips

   :arg only_active:

      Only Active, Only paste F-Modifiers on active strip

   :type only_active: boolean, (optional)
   :arg replace:

      Replace Existing, Replace existing F-Modifiers, instead of just appending to the end of the existing list

   :type replace: boolean, (optional)

.. function:: make_single_user()

   Ensure that each action is only used once in the set of strips selected

.. function:: meta_add()

   Add new meta-strips incorporating the selected strips

.. function:: meta_remove()

   Separate out the strips held by the selected meta-strips

.. function:: move_down()

   Move selected strips down a track if there's room

.. function:: move_up()

   Move selected strips up a track if there's room

.. function:: mute_toggle()

   Mute or un-mute selected strips

.. function:: previewrange_set()

   Automatically set Preview Range based on range of keyframes

.. function:: properties()

   Toggle the properties region visibility

.. function:: select_all_toggle(invert=False)

   Select or deselect all NLA-Strips

   :arg invert:

      Invert

   :type invert: boolean, (optional)

.. function:: select_border(xmin=0, xmax=0, ymin=0, ymax=0, deselect=False, extend=True, axis_range=False)

   Use box selection to grab NLA-Strips

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

.. function:: select_leftright(mode='CHECK', extend=False)

   Select strips to the left or the right of the current frame

   :arg mode:

      Mode

   :type mode: enum in ['CHECK', 'LEFT', 'RIGHT'], (optional)
   :arg extend:

      Extend Select

   :type extend: boolean, (optional)

.. function:: selected_objects_add()

   Make selected objects appear in NLA Editor by adding Animation Data

.. function:: snap(type='CFRA')

   Move start of strips to specified time

   :arg type:

      Type

   :type type: enum in ['CFRA', 'NEAREST_FRAME', 'NEAREST_SECOND', 'NEAREST_MARKER'], (optional)

.. function:: soundclip_add()

   Add a strip for controlling when speaker plays its sound clip

.. function:: split()

   Split selected strips at their midpoints

.. function:: swap()

   Swap order of selected strips within tracks

.. function:: tracks_add(above_selected=False)

   Add NLA-Tracks above/after the selected tracks

   :arg above_selected:

      Above Selected, Add a new NLA Track above every existing selected one

   :type above_selected: boolean, (optional)

.. function:: tracks_delete()

   Delete selected NLA-Tracks and the strips they contain

.. function:: transition_add()

   Add a transition strip between two adjacent selected strips

.. function:: tweakmode_enter(isolate_action=False)

   Enter tweaking mode for the action referenced by the active strip to edit its keyframes

   :arg isolate_action:

      Isolate Action, Enable 'solo' on the NLA Track containing the active strip, to edit it without seeing the effects of the NLA stack

   :type isolate_action: boolean, (optional)

.. function:: tweakmode_exit(isolate_action=False)

   Exit tweaking mode for the action referenced by the active strip

   :arg isolate_action:

      Isolate Action, Disable 'solo' on any of the NLA Tracks after exiting tweak mode to get things back to normal

   :type isolate_action: boolean, (optional)

.. function:: view_all()

   Reset viewable area to show full strips range

.. function:: view_frame()

   Reset viewable area to show range around current frame

.. function:: view_selected()

   Reset viewable area to show selected strips range


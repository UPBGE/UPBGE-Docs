NlaStrip(bpy_struct)
====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: NlaStrip(bpy_struct)

   A container referencing an existing Action

   .. attribute:: action

      Action referenced by this strip

      :type: :class:`Action`

   .. attribute:: action_frame_end

      Last frame from action to use

      :type: float in [-inf, inf], default 0.0

   .. attribute:: action_frame_start

      First frame from action to use

      :type: float in [-inf, inf], default 0.0

   .. data:: active

      NLA Strip is active

      :type: boolean, default False, (readonly)

   .. attribute:: blend_in

      Number of frames at start of strip to fade in influence

      :type: float in [-inf, inf], default 0.0

   .. attribute:: blend_out

      :type: float in [-inf, inf], default 0.0

   .. attribute:: blend_type

      Method used for combining strip's result with accumulated result

      * ``REPLACE`` Replace, Result strip replaces the accumulated results by amount specified by influence.
      * ``ADD`` Add, Weighted result of strip is added to the accumulated results.
      * ``SUBTRACT`` Subtract, Weighted result of strip is removed from the accumulated results.
      * ``MULTIPLY`` Multiply, Weighted result of strip is multiplied with the accumulated results.

      :type: enum in ['REPLACE', 'ADD', 'SUBTRACT', 'MULTIPLY'], default 'REPLACE'

   .. attribute:: extrapolation

      Action to take for gaps past the strip extents

      * ``NOTHING`` Nothing, Strip has no influence past its extents.
      * ``HOLD`` Hold, Hold the first frame if no previous strips in track, and always hold last frame.
      * ``HOLD_FORWARD`` Hold Forward, Only hold last frame.

      :type: enum in ['NOTHING', 'HOLD', 'HOLD_FORWARD'], default 'HOLD'

   .. data:: fcurves

      F-Curves for controlling the strip's influence and timing

      :type: :class:`NlaStripFCurves` :class:`bpy_prop_collection` of :class:`FCurve`, (readonly)

   .. attribute:: frame_end

      :type: float in [-inf, inf], default 0.0

   .. attribute:: frame_start

      :type: float in [-inf, inf], default 0.0

   .. attribute:: influence

      Amount the strip contributes to the current result

      :type: float in [0, 1], default 0.0

   .. data:: modifiers

      Modifiers affecting all the F-Curves in the referenced Action

      :type: :class:`bpy_prop_collection` of :class:`FModifier`, (readonly)

   .. attribute:: mute

      NLA Strip is not evaluated

      :type: boolean, default False

   .. attribute:: name

      :type: string, default "", (never None)

   .. attribute:: repeat

      Number of times to repeat the action range

      :type: float in [0.1, 1000], default 0.0

   .. attribute:: scale

      Scaling factor for action

      :type: float in [0.0001, 1000], default 0.0

   .. attribute:: select

      NLA Strip is selected

      :type: boolean, default False

   .. attribute:: strip_time

      Frame of referenced Action to evaluate

      :type: float in [-inf, inf], default 0.0

   .. data:: strips

      NLA Strips that this strip acts as a container for (if it is of type Meta)

      :type: :class:`bpy_prop_collection` of :class:`NlaStrip`, (readonly)

   .. data:: type

      Type of NLA Strip

      * ``CLIP`` Action Clip, NLA Strip references some Action.
      * ``TRANSITION`` Transition, NLA Strip 'transitions' between adjacent strips.
      * ``META`` Meta, NLA Strip acts as a container for adjacent strips.
      * ``SOUND`` Sound Clip, NLA Strip representing a sound event for speakers.

      :type: enum in ['CLIP', 'TRANSITION', 'META', 'SOUND'], default 'CLIP', (readonly)

   .. attribute:: use_animated_influence

      Influence setting is controlled by an F-Curve rather than automatically determined

      :type: boolean, default False

   .. attribute:: use_animated_time

      Strip time is controlled by an F-Curve rather than automatically determined

      :type: boolean, default False

   .. attribute:: use_animated_time_cyclic

      Cycle the animated time within the action start & end

      :type: boolean, default False

   .. attribute:: use_auto_blend

      Number of frames for Blending In/Out is automatically determined from overlapping strips

      :type: boolean, default False

   .. attribute:: use_reverse

      NLA Strip is played back in reverse order (only when timing is automatically determined)

      :type: boolean, default False

   .. attribute:: use_sync_length

      Update range of frames referenced from action after tweaking strip and its keyframes

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

   * :class:`NlaStrip.strips`
   * :class:`NlaStrips.new`
   * :class:`NlaStrips.remove`
   * :class:`NlaTrack.strips`


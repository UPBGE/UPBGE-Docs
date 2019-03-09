MovieTrackingTrack(bpy_struct)
==============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MovieTrackingTrack(bpy_struct)

   Match-moving track data for tracking

   .. data:: average_error

      Average error of re-projection

      :type: float in [-inf, inf], default 0.0, (readonly)

   .. data:: bundle

      Position of bundle reconstructed from this track

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. attribute:: color

      Color of the track in the Movie Clip Editor and the 3D viewport after a solve

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: correlation_min

      Minimal value of correlation between matched pattern and reference that is still treated as successful tracking

      :type: float in [0, 1], default 0.0

   .. attribute:: frames_limit

      Every tracking cycle, this number of frames are tracked

      :type: int in [0, 32767], default 0

   .. attribute:: grease_pencil

      Grease pencil data for this track

      :type: :class:`GreasePencil`

   .. data:: has_bundle

      True if track has a valid bundle

      :type: boolean, default False, (readonly)

   .. attribute:: hide

      Track is hidden

      :type: boolean, default False

   .. attribute:: lock

      Track is locked and all changes to it are disabled

      :type: boolean, default False

   .. attribute:: margin

      Distance from image boundary at which marker stops tracking

      :type: int in [0, 300], default 0

   .. data:: markers

      Collection of markers in track

      :type: :class:`MovieTrackingMarkers` :class:`bpy_prop_collection` of :class:`MovieTrackingMarker`, (readonly)

   .. attribute:: motion_model

      Default motion model to use for tracking

      * ``Perspective`` Perspective, Search for markers that are perspectively deformed (homography) between frames.
      * ``Affine`` Affine, Search for markers that are affine-deformed (t, r, k, and skew) between frames.
      * ``LocRotScale`` LocRotScale, Search for markers that are translated, rotated, and scaled between frames.
      * ``LocScale`` LocScale, Search for markers that are translated and scaled between frames.
      * ``LocRot`` LocRot, Search for markers that are translated and rotated between frames.
      * ``Loc`` Loc, Search for markers that are translated between frames.

      :type: enum in ['Perspective', 'Affine', 'LocRotScale', 'LocScale', 'LocRot', 'Loc'], default 'Loc'

   .. attribute:: name

      Unique name of track

      :type: string, default "", (never None)

   .. attribute:: offset

      Offset of track from the parenting point

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: pattern_match

      Track pattern from given frame when tracking marker to next frame

      * ``KEYFRAME`` Keyframe, Track pattern from keyframe to next frame.
      * ``PREV_FRAME`` Previous frame, Track pattern from current frame to next frame.

      :type: enum in ['KEYFRAME', 'PREV_FRAME'], default 'KEYFRAME'

   .. attribute:: select

      Track is selected

      :type: boolean, default False

   .. attribute:: select_anchor

      Track's anchor point is selected

      :type: boolean, default False

   .. attribute:: select_pattern

      Track's pattern area is selected

      :type: boolean, default False

   .. attribute:: select_search

      Track's search area is selected

      :type: boolean, default False

   .. attribute:: use_alpha_preview

      Apply track's mask on displaying preview

      :type: boolean, default False

   .. attribute:: use_blue_channel

      Use blue channel from footage for tracking

      :type: boolean, default False

   .. attribute:: use_brute

      Use a brute-force translation only pre-track before refinement

      :type: boolean, default False

   .. attribute:: use_custom_color

      Use custom color instead of theme-defined

      :type: boolean, default False

   .. attribute:: use_grayscale_preview

      Display what the tracking algorithm sees in the preview

      :type: boolean, default False

   .. attribute:: use_green_channel

      Use green channel from footage for tracking

      :type: boolean, default False

   .. attribute:: use_mask

      Use a grease pencil data-block as a mask to use only specified areas of pattern when tracking

      :type: boolean, default False

   .. attribute:: use_normalization

      Normalize light intensities while tracking. Slower

      :type: boolean, default False

   .. attribute:: use_red_channel

      Use red channel from footage for tracking

      :type: boolean, default False

   .. attribute:: weight

      Influence of this track on a final solution

      :type: float in [0, 1], default 0.0

   .. attribute:: weight_stab

      Influence of this track on 2D stabilization

      :type: float in [0, 1], default 0.0

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

   * :class:`MovieTracking.tracks`
   * :class:`MovieTrackingObject.tracks`
   * :class:`MovieTrackingObjectPlaneTracks.active`
   * :class:`MovieTrackingObjectTracks.active`
   * :class:`MovieTrackingObjectTracks.new`
   * :class:`MovieTrackingStabilization.rotation_tracks`
   * :class:`MovieTrackingStabilization.tracks`
   * :class:`MovieTrackingTracks.active`
   * :class:`MovieTrackingTracks.new`
   * :class:`UILayout.template_marker`


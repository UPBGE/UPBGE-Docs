MovieTrackingSettings(bpy_struct)
=================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MovieTrackingSettings(bpy_struct)

   Match moving settings

   .. attribute:: clean_action

      Cleanup action to execute

      * ``SELECT`` Select, Select unclean tracks.
      * ``DELETE_TRACK`` Delete Track, Delete unclean tracks.
      * ``DELETE_SEGMENTS`` Delete Segments, Delete unclean segments of tracks.

      :type: enum in ['SELECT', 'DELETE_TRACK', 'DELETE_SEGMENTS'], default 'SELECT'

   .. attribute:: clean_error

      Effect on tracks which have a larger re-projection error

      :type: float in [0, inf], default 0.0

   .. attribute:: clean_frames

      Effect on tracks which are tracked less than the specified amount of frames

      :type: int in [0, inf], default 0

   .. attribute:: default_correlation_min

      Default minimum value of correlation between matched pattern and reference that is still treated as successful tracking

      :type: float in [0, 1], default 0.0

   .. attribute:: default_frames_limit

      Every tracking cycle, this number of frames are tracked

      :type: int in [0, 32767], default 0

   .. attribute:: default_margin

      Default distance from image boundary at which marker stops tracking

      :type: int in [0, 300], default 0

   .. attribute:: default_motion_model

      Default motion model to use for tracking

      * ``Perspective`` Perspective, Search for markers that are perspectively deformed (homography) between frames.
      * ``Affine`` Affine, Search for markers that are affine-deformed (t, r, k, and skew) between frames.
      * ``LocRotScale`` LocRotScale, Search for markers that are translated, rotated, and scaled between frames.
      * ``LocScale`` LocScale, Search for markers that are translated and scaled between frames.
      * ``LocRot`` LocRot, Search for markers that are translated and rotated between frames.
      * ``Loc`` Loc, Search for markers that are translated between frames.

      :type: enum in ['Perspective', 'Affine', 'LocRotScale', 'LocScale', 'LocRot', 'Loc'], default 'Loc'

   .. attribute:: default_pattern_match

      Track pattern from given frame when tracking marker to next frame

      * ``KEYFRAME`` Keyframe, Track pattern from keyframe to next frame.
      * ``PREV_FRAME`` Previous frame, Track pattern from current frame to next frame.

      :type: enum in ['KEYFRAME', 'PREV_FRAME'], default 'KEYFRAME'

   .. attribute:: default_pattern_size

      Size of pattern area for newly created tracks

      :type: int in [5, 1000], default 0

   .. attribute:: default_search_size

      Size of search area for newly created tracks

      :type: int in [5, 1000], default 0

   .. attribute:: default_weight

      Influence of newly created track on a final solution

      :type: float in [0, 1], default 0.0

   .. attribute:: distance

      Distance between two bundles used for scene scaling

      :type: float in [-inf, inf], default 1.0

   .. attribute:: object_distance

      Distance between two bundles used for object scaling

      :type: float in [0.001, 10000], default 1.0

   .. attribute:: refine_intrinsics

      Refine intrinsics during camera solving

      * ``NONE`` Nothing, Do not refine camera intrinsics.
      * ``FOCAL_LENGTH`` Focal Length, Refine focal length.
      * ``FOCAL_LENGTH_RADIAL_K1`` Focal length, K1, Refine focal length and radial distortion K1.
      * ``FOCAL_LENGTH_RADIAL_K1_K2`` Focal length, K1, K2, Refine focal length and radial distortion K1 and K2.
      * ``FOCAL_LENGTH_PRINCIPAL_POINT_RADIAL_K1_K2`` Focal Length, Optical Center, K1, K2, Refine focal length, optical center and radial distortion K1 and K2.
      * ``FOCAL_LENGTH_PRINCIPAL_POINT`` Focal Length, Optical Center, Refine focal length and optical center.
      * ``RADIAL_K1_K2`` K1, K2, Refine radial distortion K1 and K2.

      :type: enum in ['NONE', 'FOCAL_LENGTH', 'FOCAL_LENGTH_RADIAL_K1', 'FOCAL_LENGTH_RADIAL_K1_K2', 'FOCAL_LENGTH_PRINCIPAL_POINT_RADIAL_K1_K2', 'FOCAL_LENGTH_PRINCIPAL_POINT', 'RADIAL_K1_K2'], default 'NONE'

   .. attribute:: show_default_expanded

      Show default options expanded in the user interface

      :type: boolean, default False

   .. attribute:: show_extra_expanded

      Show extra options expanded in the user interface

      :type: boolean, default False

   .. attribute:: speed

      Limit speed of tracking to make visual feedback easier (this does not affect the tracking quality)

      * ``FASTEST`` Fastest, Track as fast as it's possible.
      * ``DOUBLE`` Double, Track with double speed.
      * ``REALTIME`` Realtime, Track with realtime speed.
      * ``HALF`` Half, Track with half of realtime speed.
      * ``QUARTER`` Quarter, Track with quarter of realtime speed.

      :type: enum in ['FASTEST', 'DOUBLE', 'REALTIME', 'HALF', 'QUARTER'], default 'FASTEST'

   .. attribute:: use_default_blue_channel

      Use blue channel from footage for tracking

      :type: boolean, default False

   .. attribute:: use_default_brute

      Use a brute-force translation-only initialization when tracking

      :type: boolean, default False

   .. attribute:: use_default_green_channel

      Use green channel from footage for tracking

      :type: boolean, default False

   .. attribute:: use_default_mask

      Use a grease pencil data-block as a mask to use only specified areas of pattern when tracking

      :type: boolean, default False

   .. attribute:: use_default_normalization

      Normalize light intensities while tracking (slower)

      :type: boolean, default False

   .. attribute:: use_default_red_channel

      Use red channel from footage for tracking

      :type: boolean, default False

   .. attribute:: use_keyframe_selection

      Automatically select keyframes when solving camera/object motion

      :type: boolean, default False

   .. attribute:: use_tripod_solver

      Use special solver to track a stable camera position, such as a tripod

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

   * :class:`MovieTracking.settings`


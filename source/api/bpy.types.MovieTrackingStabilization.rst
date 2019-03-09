MovieTrackingStabilization(bpy_struct)
======================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MovieTrackingStabilization(bpy_struct)

   2D stabilization based on tracking markers

   .. attribute:: active_rotation_track_index

      Index of active track in rotation stabilization tracks list

      :type: int in [-inf, inf], default 0

   .. attribute:: active_track_index

      Index of active track in translation stabilization tracks list

      :type: int in [-inf, inf], default 0

   .. attribute:: anchor_frame

      Reference point to anchor stabilization (other frames will be adjusted relative to this frame's position)

      :type: int in [0, 1048574], default 0

   .. attribute:: filter_type

      Interpolation to use for sub-pixel shifts and rotations due to stabilization

      * ``NEAREST`` Nearest, No interpolation, use nearest neighbor pixel.
      * ``BILINEAR`` Bilinear, Simple interpolation between adjacent pixels.
      * ``BICUBIC`` Bicubic, High quality pixel interpolation.

      :type: enum in ['NEAREST', 'BILINEAR', 'BICUBIC'], default 'NEAREST'

   .. attribute:: influence_location

      Influence of stabilization algorithm on footage location

      :type: float in [0, 1], default 0.0

   .. attribute:: influence_rotation

      Influence of stabilization algorithm on footage rotation

      :type: float in [0, 1], default 0.0

   .. attribute:: influence_scale

      Influence of stabilization algorithm on footage scale

      :type: float in [0, 1], default 0.0

   .. data:: rotation_tracks

      Collection of tracks used for 2D stabilization (translation)

      :type: :class:`bpy_prop_collection` of :class:`MovieTrackingTrack`, (readonly)

   .. attribute:: scale_max

      Limit the amount of automatic scaling

      :type: float in [0, 10], default 0.0

   .. attribute:: show_tracks_expanded

      Show UI list of tracks participating in stabilization

      :type: boolean, default False

   .. attribute:: target_position

      Known relative offset of original shot, will be subtracted (e.g. for panning shot, can be animated)

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: target_rotation

      Rotation present on original shot, will be compensated (e.g. for deliberate tilting)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: target_scale

      Explicitly scale resulting frame to compensate zoom of original shot

      :type: float in [1.192e-07, inf], default 0.0

   .. data:: tracks

      Collection of tracks used for 2D stabilization (translation)

      :type: :class:`bpy_prop_collection` of :class:`MovieTrackingTrack`, (readonly)

   .. attribute:: use_2d_stabilization

      Use 2D stabilization for footage

      :type: boolean, default False

   .. attribute:: use_autoscale

      Automatically scale footage to cover unfilled areas when stabilizing

      :type: boolean, default False

   .. attribute:: use_stabilize_rotation

      Stabilize detected rotation around center of frame

      :type: boolean, default False

   .. attribute:: use_stabilize_scale

      Compensate any scale changes relative to center of rotation

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

   * :class:`MovieTracking.stabilization`


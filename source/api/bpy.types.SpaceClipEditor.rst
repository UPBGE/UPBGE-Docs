SpaceClipEditor(Space)
======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceClipEditor(Space)

   Clip editor space data

   .. attribute:: clip

      Movie clip displayed and edited in this space

      :type: :class:`MovieClip`

   .. data:: clip_user

      Parameters defining which frame of the movie clip is displayed

      :type: :class:`MovieClipUser`, (readonly, never None)

   .. attribute:: grease_pencil_source

      Where the grease pencil comes from

      * ``CLIP`` Clip, Show grease pencil data-block which belongs to movie clip.
      * ``TRACK`` Track, Show grease pencil data-block which belongs to active track.

      :type: enum in ['CLIP', 'TRACK'], default 'CLIP'

   .. attribute:: lock_selection

      Lock viewport to selected markers during playback

      :type: boolean, default False

   .. attribute:: lock_time_cursor

      Lock curves view to time cursor during playback and tracking

      :type: boolean, default False

   .. attribute:: mask

      Mask displayed and edited in this space

      :type: :class:`Mask`

   .. attribute:: mask_draw_type

      Draw type for mask splines

      * ``OUTLINE`` Outline, Draw white edges with black outline.
      * ``DASH`` Dash, Draw dashed black-white edges.
      * ``BLACK`` Black, Draw black edges.
      * ``WHITE`` White, Draw white edges.

      :type: enum in ['OUTLINE', 'DASH', 'BLACK', 'WHITE'], default 'OUTLINE'

   .. attribute:: mask_overlay_mode

      Overlay mode of rasterized mask

      * ``ALPHACHANNEL`` Alpha Channel, Show alpha channel of the mask.
      * ``COMBINED`` Combined, Combine space background image with the mask.

      :type: enum in ['ALPHACHANNEL', 'COMBINED'], default 'ALPHACHANNEL'

   .. attribute:: mode

      Editing context being displayed

      * ``TRACKING`` Tracking, Show tracking and solving tools.
      * ``MASK`` Mask, Show mask editing tools.

      :type: enum in ['TRACKING', 'MASK'], default 'TRACKING'

   .. attribute:: path_length

      Length of displaying path, in frames

      :type: int in [0, inf], default 0

   .. attribute:: pivot_point

      Pivot center for rotation/scaling

      * ``BOUNDING_BOX_CENTER`` Bounding Box Center, Pivot around bounding box center of selected object(s).
      * ``CURSOR`` 2D Cursor, Pivot around the 2D cursor.
      * ``INDIVIDUAL_ORIGINS`` Individual Origins, Pivot around each object's own origin.
      * ``MEDIAN_POINT`` Median Point, Pivot around the median point of selected objects.

      :type: enum in ['BOUNDING_BOX_CENTER', 'CURSOR', 'INDIVIDUAL_ORIGINS', 'MEDIAN_POINT'], default 'BOUNDING_BOX_CENTER'

   .. data:: scopes

      Scopes to visualize movie clip statistics

      :type: :class:`MovieClipScopes`, (readonly)

   .. attribute:: show_blue_channel

      Show blue channel in the frame

      :type: boolean, default False

   .. attribute:: show_bundles

      Show projection of 3D markers into footage

      :type: boolean, default False

   .. attribute:: show_disabled

      Show disabled tracks from the footage

      :type: boolean, default False

   .. attribute:: show_filters

      Show filters for graph editor

      :type: boolean, default False

   .. attribute:: show_graph_frames

      Show curve for per-frame average error (camera motion should be solved first)

      :type: boolean, default False

   .. attribute:: show_graph_hidden

      Include channels from objects/bone that aren't visible

      :type: boolean, default False

   .. attribute:: show_graph_only_selected

      Only include channels relating to selected objects and data

      :type: boolean, default False

   .. attribute:: show_graph_tracks_error

      Display the reprojection error curve for selected tracks

      :type: boolean, default False

   .. attribute:: show_graph_tracks_motion

      Display the speed curves (in "x" direction red, in "y" direction green) for the selected tracks

      :type: boolean, default False

   .. attribute:: show_grease_pencil

      Show grease pencil for this view

      :type: boolean, default False

   .. attribute:: show_green_channel

      Show green channel in the frame

      :type: boolean, default False

   .. attribute:: show_grid

      Show grid showing lens distortion

      :type: boolean, default False

   .. attribute:: show_marker_pattern

      Show pattern boundbox for markers

      :type: boolean, default False

   .. attribute:: show_marker_search

      Show search boundbox for markers

      :type: boolean, default False

   .. attribute:: show_mask_overlay

      :type: boolean, default False

   .. attribute:: show_mask_smooth

      :type: boolean, default False

   .. attribute:: show_metadata

      Show metadata of clip

      :type: boolean, default False

   .. attribute:: show_names

      Show track names and status

      :type: boolean, default False

   .. attribute:: show_red_channel

      Show red channel in the frame

      :type: boolean, default False

   .. attribute:: show_seconds

      Show timing in seconds not frames

      :type: boolean, default False

   .. attribute:: show_stable

      Show stable footage in editor (if stabilization is enabled)

      :type: boolean, default False

   .. attribute:: show_tiny_markers

      Show markers in a more compact manner

      :type: boolean, default False

   .. attribute:: show_track_path

      Show path of how track moves

      :type: boolean, default False

   .. attribute:: use_grayscale_preview

      Display frame in grayscale mode

      :type: boolean, default False

   .. attribute:: use_manual_calibration

      Use manual calibration helpers

      :type: boolean, default False

   .. attribute:: use_mute_footage

      Mute footage and show black background instead

      :type: boolean, default False

   .. attribute:: view

      Type of the clip editor view

      * ``CLIP`` Clip, Show editing clip preview.
      * ``GRAPH`` Graph, Show graph view for active element.
      * ``DOPESHEET`` Dopesheet, Dopesheet view for tracking data.

      :type: enum in ['CLIP', 'GRAPH', 'DOPESHEET'], default 'CLIP'

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


   .. function:: draw_handler_add()

      Undocumented
   .. function:: draw_handler_remove()

      Undocumented
.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Space.type`
   * :class:`Space.show_locked_time`

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


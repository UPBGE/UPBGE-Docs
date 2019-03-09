Clip Operators
==============

.. module:: bpy.ops.clip

.. function:: add_marker(location=(0.0, 0.0))

   Place new marker at specified location

   :arg location:

      Location, Location of marker on frame

   :type location: float array of 2 items in [-inf, inf], (optional)

.. function:: add_marker_at_click()

   Place new marker at the desired (clicked) position

.. function:: add_marker_move(CLIP_OT_add_marker=None, TRANSFORM_OT_translate=None)

   Add new marker and move it on movie

   :arg CLIP_OT_add_marker:

      Add Marker, Place new marker at specified location

   :type CLIP_OT_add_marker: :class:`CLIP_OT_add_marker`, (optional)
   :arg TRANSFORM_OT_translate:

      Translate, Translate (move) selected items

   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: add_marker_slide(CLIP_OT_add_marker=None, TRANSFORM_OT_translate=None)

   Add new marker and slide it with mouse until mouse button release

   :arg CLIP_OT_add_marker:

      Add Marker, Place new marker at specified location

   :type CLIP_OT_add_marker: :class:`CLIP_OT_add_marker`, (optional)
   :arg TRANSFORM_OT_translate:

      Translate, Translate (move) selected items

   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: apply_solution_scale(distance=0.0)

   Apply scale on solution itself to make distance between selected tracks equals to desired

   :arg distance:

      Distance, Distance between selected tracks

   :type distance: float in [-inf, inf], (optional)

.. function:: bundles_to_mesh()

   Create vertex cloud using coordinates of reconstructed tracks

   :file: `startup\bl_operators\clip.py\:286 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\clip.py$286>`_

.. function:: camera_preset_add(name="", remove_active=False, use_focal_length=True)

   Add or remove a Tracking Camera Intrinsics Preset

   :arg name:

      Name, Name of the preset, used to make the path name

   :type name: string, (optional, never None)
   :arg remove_active:

      remove_active

   :type remove_active: boolean, (optional)
   :arg use_focal_length:

      Include Focal Length, Include focal length into the preset

   :type use_focal_length: boolean, (optional)

   :file: `startup\bl_operators\presets.py\:71 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\presets.py$71>`_

.. function:: change_frame(frame=0)

   Interactively change the current frame number

   :arg frame:

      Frame

   :type frame: int in [-1048574, 1048574], (optional)

.. function:: clean_tracks(frames=0, error=0.0, action='SELECT')

   Clean tracks with high error values or few frames

   :arg frames:

      Tracked Frames, Effect on tracks which are tracked less than specified amount of frames

   :type frames: int in [0, inf], (optional)
   :arg error:

      Reprojection Error, Effect on tracks which have got larger re-projection error

   :type error: float in [0, inf], (optional)
   :arg action:

      Action, Cleanup action to execute

      * ``SELECT`` Select, Select unclean tracks.
      * ``DELETE_TRACK`` Delete Track, Delete unclean tracks.
      * ``DELETE_SEGMENTS`` Delete Segments, Delete unclean segments of tracks.

   :type action: enum in ['SELECT', 'DELETE_TRACK', 'DELETE_SEGMENTS'], (optional)

.. function:: clear_solution()

   Clear all calculated data

.. function:: clear_track_path(action='REMAINED', clear_active=False)

   Clear tracks after/before current position or clear the whole track

   :arg action:

      Action, Clear action to execute

      * ``UPTO`` Clear up-to, Clear path up to current frame.
      * ``REMAINED`` Clear remained, Clear path at remaining frames (after current).
      * ``ALL`` Clear all, Clear the whole path.

   :type action: enum in ['UPTO', 'REMAINED', 'ALL'], (optional)
   :arg clear_active:

      Clear Active, Clear active track only instead of all selected tracks

   :type clear_active: boolean, (optional)

.. function:: constraint_to_fcurve()

   Create F-Curves for object which will copy object's movement caused by this constraint

   :file: `startup\bl_operators\clip.py\:512 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\clip.py$512>`_

.. function:: copy_tracks()

   Copy selected tracks to clipboard

.. function:: create_plane_track()

   Create new plane track out of selected point tracks

.. function:: cursor_set(location=(0.0, 0.0))

   Set 2D cursor location

   :arg location:

      Location, Cursor location in normalized clip coordinates

   :type location: float array of 2 items in [-inf, inf], (optional)

.. function:: delete_marker()

   Delete marker for current frame from selected tracks

.. function:: delete_proxy()

   Delete movie clip proxy files from the hard drive

   :file: `startup\bl_operators\clip.py\:355 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\clip.py$355>`_

.. function:: delete_track()

   Delete selected tracks

.. function:: detect_features(placement='FRAME', margin=16, threshold=0.5, min_distance=120)

   Automatically detect features and place markers to track

   :arg placement:

      Placement, Placement for detected features

      * ``FRAME`` Whole Frame, Place markers across the whole frame.
      * ``INSIDE_GPENCIL`` Inside grease pencil, Place markers only inside areas outlined with grease pencil.
      * ``OUTSIDE_GPENCIL`` Outside grease pencil, Place markers only outside areas outlined with grease pencil.

   :type placement: enum in ['FRAME', 'INSIDE_GPENCIL', 'OUTSIDE_GPENCIL'], (optional)
   :arg margin:

      Margin, Only features further than margin pixels from the image edges are considered

   :type margin: int in [0, inf], (optional)
   :arg threshold:

      Threshold, Threshold level to consider feature good enough for tracking

   :type threshold: float in [0.0001, inf], (optional)
   :arg min_distance:

      Distance, Minimal distance accepted between two features

   :type min_distance: int in [0, inf], (optional)

.. function:: disable_markers(action='DISABLE')

   Disable/enable selected markers

   :arg action:

      Action, Disable action to execute

      * ``DISABLE`` Disable, Disable selected markers.
      * ``ENABLE`` Enable, Enable selected markers.
      * ``TOGGLE`` Toggle, Toggle disabled flag for selected markers.

   :type action: enum in ['DISABLE', 'ENABLE', 'TOGGLE'], (optional)

.. function:: dopesheet_select_channel(location=(0.0, 0.0), extend=False)

   Select movie tracking channel

   :arg location:

      Location, Mouse location to select channel

   :type location: float array of 2 items in [-inf, inf], (optional)
   :arg extend:

      Extend, Extend selection rather than clearing the existing selection

   :type extend: boolean, (optional)

.. function:: dopesheet_view_all()

   Reset viewable area to show full keyframe range

.. function:: filter_tracks(track_threshold=5.0)

   Filter tracks which has weirdly looking spikes in motion curves

   :arg track_threshold:

      Track Threshold, Filter Threshold to select problematic tracks

   :type track_threshold: float in [-inf, inf], (optional)

   :file: `startup\bl_operators\clip.py\:200 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\clip.py$200>`_

.. function:: frame_jump(position='PATHSTART')

   Jump to special frame

   :arg position:

      Position, Position to jump to

      * ``PATHSTART`` Path Start, Jump to start of current path.
      * ``PATHEND`` Path End, Jump to end of current path.
      * ``FAILEDPREV`` Previous Failed, Jump to previous failed frame.
      * ``FAILNEXT`` Next Failed, Jump to next failed frame.

   :type position: enum in ['PATHSTART', 'PATHEND', 'FAILEDPREV', 'FAILNEXT'], (optional)

.. function:: graph_center_current_frame()

   Scroll view so current frame would be centered

.. function:: graph_delete_curve()

   Delete track corresponding to the selected curve

.. function:: graph_delete_knot()

   Delete curve knots

.. function:: graph_disable_markers(action='DISABLE')

   Disable/enable selected markers

   :arg action:

      Action, Disable action to execute

      * ``DISABLE`` Disable, Disable selected markers.
      * ``ENABLE`` Enable, Enable selected markers.
      * ``TOGGLE`` Toggle, Toggle disabled flag for selected markers.

   :type action: enum in ['DISABLE', 'ENABLE', 'TOGGLE'], (optional)

.. function:: graph_select(location=(0.0, 0.0), extend=False)

   Select graph curves

   :arg location:

      Location, Mouse location to select nearest entity

   :type location: float array of 2 items in [-inf, inf], (optional)
   :arg extend:

      Extend, Extend selection rather than clearing the existing selection

   :type extend: boolean, (optional)

.. function:: graph_select_all_markers(action='TOGGLE')

   Change selection of all markers of active track

   :arg action:

      Action, Selection action to execute

      * ``TOGGLE`` Toggle, Toggle selection for all elements.
      * ``SELECT`` Select, Select all elements.
      * ``DESELECT`` Deselect, Deselect all elements.
      * ``INVERT`` Invert, Invert selection of all elements.

   :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

.. function:: graph_select_border(xmin=0, xmax=0, ymin=0, ymax=0, deselect=False, extend=True)

   Select curve points using border selection

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

.. function:: graph_view_all()

   View all curves in editor

.. function:: hide_tracks(unselected=False)

   Hide selected tracks

   :arg unselected:

      Unselected, Hide unselected tracks

   :type unselected: boolean, (optional)

.. function:: hide_tracks_clear()

   Clear hide selected tracks

.. function:: join_tracks()

   Join selected tracks

.. function:: keyframe_delete()

   Delete a keyframe from selected tracks at current frame

.. function:: keyframe_insert()

   Insert a keyframe to selected tracks at current frame

.. function:: lock_tracks(action='LOCK')

   Lock/unlock selected tracks

   :arg action:

      Action, Lock action to execute

      * ``LOCK`` Lock, Lock selected tracks.
      * ``UNLOCK`` Unlock, Unlock selected tracks.
      * ``TOGGLE`` Toggle, Toggle locked flag for selected tracks.

   :type action: enum in ['LOCK', 'UNLOCK', 'TOGGLE'], (optional)

.. function:: mode_set(mode='TRACKING')

   Set the clip interaction mode

   :arg mode:

      Mode

      * ``TRACKING`` Tracking, Show tracking and solving tools.
      * ``MASK`` Mask, Show mask editing tools.

   :type mode: enum in ['TRACKING', 'MASK'], (optional)

.. function:: open(directory="", files=None, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA')

   Load a sequence of frames or a movie file

   :arg directory:

      Directory, Directory of the file

   :type directory: string, (optional, never None)
   :arg files:

      Files

   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg filter_blender:

      Filter .blend files

   :type filter_blender: boolean, (optional)
   :arg filter_backup:

      Filter .blend files

   :type filter_backup: boolean, (optional)
   :arg filter_image:

      Filter image files

   :type filter_image: boolean, (optional)
   :arg filter_movie:

      Filter movie files

   :type filter_movie: boolean, (optional)
   :arg filter_python:

      Filter python files

   :type filter_python: boolean, (optional)
   :arg filter_font:

      Filter font files

   :type filter_font: boolean, (optional)
   :arg filter_sound:

      Filter sound files

   :type filter_sound: boolean, (optional)
   :arg filter_text:

      Filter text files

   :type filter_text: boolean, (optional)
   :arg filter_btx:

      Filter btx files

   :type filter_btx: boolean, (optional)
   :arg filter_collada:

      Filter COLLADA files

   :type filter_collada: boolean, (optional)
   :arg filter_alembic:

      Filter Alembic files

   :type filter_alembic: boolean, (optional)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_blenlib:

      Filter Blender IDs

   :type filter_blenlib: boolean, (optional)
   :arg filemode:

      File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

   :type filemode: int in [1, 9], (optional)
   :arg relative_path:

      Relative Path, Select the file relative to the blend file

   :type relative_path: boolean, (optional)
   :arg show_multiview:

      Enable Multi-View

   :type show_multiview: boolean, (optional)
   :arg use_multiview:

      Use Multi-View

   :type use_multiview: boolean, (optional)
   :arg display_type:

      Display Type

      * ``DEFAULT`` Default, Automatically determine display type for files.
      * ``LIST_SHORT`` Short List, Display files as short list.
      * ``LIST_LONG`` Long List, Display files as a detailed list.
      * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.

   :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
   :arg sort_method:

      File sorting mode

      * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type.
      * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time.
      * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.

   :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

.. function:: paste_tracks()

   Paste tracks from clipboard

.. function:: prefetch()

   Prefetch frames from disk for faster playback/tracking

.. function:: properties()

   Toggle the properties region visibility

.. function:: rebuild_proxy()

   Rebuild all selected proxies and timecode indices in the background

.. function:: refine_markers(backwards=False)

   Refine selected markers positions by running the tracker from track's reference to current frame

   :arg backwards:

      Backwards, Do backwards tracking

   :type backwards: boolean, (optional)

.. function:: reload()

   Reload clip

.. function:: select(extend=False, location=(0.0, 0.0))

   Select tracking markers

   :arg extend:

      Extend, Extend selection rather than clearing the existing selection

   :type extend: boolean, (optional)
   :arg location:

      Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds

   :type location: float array of 2 items in [-inf, inf], (optional)

.. function:: select_all(action='TOGGLE')

   Change selection of all tracking markers

   :arg action:

      Action, Selection action to execute

      * ``TOGGLE`` Toggle, Toggle selection for all elements.
      * ``SELECT`` Select, Select all elements.
      * ``DESELECT`` Deselect, Deselect all elements.
      * ``INVERT`` Invert, Invert selection of all elements.

   :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

.. function:: select_border(xmin=0, xmax=0, ymin=0, ymax=0, deselect=False, extend=True)

   Select markers using border selection

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

   Select markers using circle selection

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

.. function:: select_grouped(group='ESTIMATED')

   Select all tracks from specified group

   :arg group:

      Action, Clear action to execute

      * ``KEYFRAMED`` Keyframed tracks, Select all keyframed tracks.
      * ``ESTIMATED`` Estimated tracks, Select all estimated tracks.
      * ``TRACKED`` Tracked tracks, Select all tracked tracks.
      * ``LOCKED`` Locked tracks, Select all locked tracks.
      * ``DISABLED`` Disabled tracks, Select all disabled tracks.
      * ``COLOR`` Tracks with same color, Select all tracks with same color as active track.
      * ``FAILED`` Failed Tracks, Select all tracks which failed to be reconstructed.

   :type group: enum in ['KEYFRAMED', 'ESTIMATED', 'TRACKED', 'LOCKED', 'DISABLED', 'COLOR', 'FAILED'], (optional)

.. function:: select_lasso(path=None, deselect=False, extend=True)

   Select markers using lasso selection

   :arg path:

      Path

   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg deselect:

      Deselect, Deselect rather than select items

   :type deselect: boolean, (optional)
   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)

.. function:: set_active_clip()

   Undocumented

   :file: `startup\bl_operators\clip.py\:215 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\clip.py$215>`_

.. function:: set_axis(axis='X')

   Set direction of scene axis rotating camera (or its parent if present) and assume selected track lies on real axis, joining it with the origin

   :arg axis:

      Axis, Axis to use to align bundle along

      * ``X`` X, Align bundle align X axis.
      * ``Y`` Y, Align bundle align Y axis.

   :type axis: enum in ['X', 'Y'], (optional)

.. function:: set_center_principal()

   Set optical center to center of footage

.. function:: set_origin(use_median=False)

   Set active marker as origin by moving camera (or its parent if present) in 3D space

   :arg use_median:

      Use Median, Set origin to median point of selected bundles

   :type use_median: boolean, (optional)

.. function:: set_plane(plane='FLOOR')

   Set plane based on 3 selected bundles by moving camera (or its parent if present) in 3D space

   :arg plane:

      Plane, Plane to be used for orientation

      * ``FLOOR`` Floor, Set floor plane.
      * ``WALL`` Wall, Set wall plane.

   :type plane: enum in ['FLOOR', 'WALL'], (optional)

.. function:: set_scale(distance=0.0)

   Set scale of scene by scaling camera (or its parent if present)

   :arg distance:

      Distance, Distance between selected tracks

   :type distance: float in [-inf, inf], (optional)

.. function:: set_scene_frames()

   Set scene's start and end frame to match clip's start frame and length

.. function:: set_solution_scale(distance=0.0)

   Set object solution scale using distance between two selected tracks

   :arg distance:

      Distance, Distance between selected tracks

   :type distance: float in [-inf, inf], (optional)

.. function:: set_solver_keyframe(keyframe='KEYFRAME_A')

   Set keyframe used by solver

   :arg keyframe:

      Keyframe, Keyframe to set

   :type keyframe: enum in ['KEYFRAME_A', 'KEYFRAME_B'], (optional)

.. function:: set_viewport_background()

   Set current movie clip as a camera background in 3D view-port (works only when a 3D view-port is visible)

   :file: `startup\bl_operators\clip.py\:416 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\clip.py$416>`_

.. function:: setup_tracking_scene()

   Prepare scene for compositing 3D objects into this footage

   :file: `startup\bl_operators\clip.py\:980 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\clip.py$980>`_

.. function:: slide_marker(offset=(0.0, 0.0))

   Slide marker areas

   :arg offset:

      Offset, Offset in floating point units, 1.0 is the width and height of the image

   :type offset: float array of 2 items in [-inf, inf], (optional)

.. function:: slide_plane_marker()

   Slide plane marker areas

.. function:: solve_camera()

   Solve camera motion from tracks

.. function:: stabilize_2d_add()

   Add selected tracks to 2D translation stabilization

.. function:: stabilize_2d_remove()

   Remove selected track from translation stabilization

.. function:: stabilize_2d_rotation_add()

   Add selected tracks to 2D rotation stabilization

.. function:: stabilize_2d_rotation_remove()

   Remove selected track from rotation stabilization

.. function:: stabilize_2d_rotation_select()

   Select tracks which are used for rotation stabilization

.. function:: stabilize_2d_select()

   Select tracks which are used for translation stabilization

.. function:: tools()

   Toggle clip tools panel

.. function:: track_color_preset_add(name="", remove_active=False)

   Add or remove a Clip Track Color Preset

   :arg name:

      Name, Name of the preset, used to make the path name

   :type name: string, (optional, never None)
   :arg remove_active:

      remove_active

   :type remove_active: boolean, (optional)

   :file: `startup\bl_operators\presets.py\:71 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\presets.py$71>`_

.. function:: track_copy_color()

   Copy color to all selected tracks

.. function:: track_markers(backwards=False, sequence=False)

   Track selected markers

   :arg backwards:

      Backwards, Do backwards tracking

   :type backwards: boolean, (optional)
   :arg sequence:

      Track Sequence, Track marker during image sequence rather than single image

   :type sequence: boolean, (optional)

.. function:: track_settings_as_default()

   Copy tracking settings from active track to default settings

   :file: `startup\bl_operators\clip.py\:1017 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\clip.py$1017>`_

.. function:: track_settings_to_track()

   Copy tracking settings from active track to selected tracks

   :file: `startup\bl_operators\clip.py\:1065 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\clip.py$1065>`_

.. function:: track_to_empty()

   Create an Empty object which will be copying movement of active track

   :file: `startup\bl_operators\clip.py\:262 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\clip.py$262>`_

.. function:: tracking_object_new()

   Add new object for tracking

.. function:: tracking_object_remove()

   Remove object for tracking

.. function:: tracking_settings_preset_add(name="", remove_active=False)

   Add or remove a motion tracking settings preset

   :arg name:

      Name, Name of the preset, used to make the path name

   :type name: string, (optional, never None)
   :arg remove_active:

      remove_active

   :type remove_active: boolean, (optional)

   :file: `startup\bl_operators\presets.py\:71 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\presets.py$71>`_

.. function:: view_all(fit_view=False)

   View whole image with markers

   :arg fit_view:

      Fit View, Fit frame to the viewport

   :type fit_view: boolean, (optional)

.. function:: view_ndof()

   Use a 3D mouse device to pan/zoom the view

.. function:: view_pan(offset=(0.0, 0.0))

   Pan the view

   :arg offset:

      Offset, Offset in floating point units, 1.0 is the width and height of the image

   :type offset: float array of 2 items in [-inf, inf], (optional)

.. function:: view_selected()

   View all selected elements

.. function:: view_zoom(factor=0.0)

   Zoom in/out the view

   :arg factor:

      Factor, Zoom factor, values higher than 1.0 zoom in, lower values zoom out

   :type factor: float in [-inf, inf], (optional)

.. function:: view_zoom_in(location=(0.0, 0.0))

   Zoom in the view

   :arg location:

      Location, Cursor location in screen coordinates

   :type location: float array of 2 items in [-inf, inf], (optional)

.. function:: view_zoom_out(location=(0.0, 0.0))

   Zoom out the view

   :arg location:

      Location, Cursor location in normalized (0.0-1.0) coordinates

   :type location: float array of 2 items in [-inf, inf], (optional)

.. function:: view_zoom_ratio(ratio=0.0)

   Set the zoom ratio (based on clip size)

   :arg ratio:

      Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out

   :type ratio: float in [-inf, inf], (optional)


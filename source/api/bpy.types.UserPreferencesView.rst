UserPreferencesView(bpy_struct)
===============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: UserPreferencesView(bpy_struct)

   Preferences related to viewing data

   .. attribute:: manipulator_handle_size

      Size of manipulator handles as percentage of the radius

      :type: int in [2, 40], default 25

   .. attribute:: manipulator_hotspot

      Distance around the handles to accept mouse clicks

      :type: int in [4, 40], default 14

   .. attribute:: manipulator_size

      Diameter of the manipulator

      :type: int in [10, 200], default 75

   .. attribute:: mini_axis_brightness

      Brightness of the icon

      :type: int in [0, 10], default 0

   .. attribute:: mini_axis_size

      The axes icon's size

      :type: int in [10, 64], default 0

   .. attribute:: object_origin_size

      Diameter in Pixels for Object/Lamp origin display

      :type: int in [4, 10], default 0

   .. attribute:: open_left_mouse_delay

      Time in 1/10 seconds to hold the Left Mouse Button before opening the toolbox

      :type: int in [1, 40], default 0

   .. attribute:: open_right_mouse_delay

      Time in 1/10 seconds to hold the Right Mouse Button before opening the toolbox

      :type: int in [1, 40], default 0

   .. attribute:: open_sublevel_delay

      Time delay in 1/10 seconds before automatically opening sub level menus

      :type: int in [1, 40], default 0

   .. attribute:: open_toplevel_delay

      Time delay in 1/10 seconds before automatically opening top level menus

      :type: int in [1, 40], default 0

   .. attribute:: pie_animation_timeout

      Time needed to fully animate the pie to unfolded state (in 1/100ths of sec)

      :type: int in [0, 1000], default 0

   .. attribute:: pie_initial_timeout

      Pie menus will use the initial mouse position as center for this amount of time (in 1/100ths of sec)

      :type: int in [0, 1000], default 0

   .. attribute:: pie_menu_confirm

      Distance threshold after which selection is made (zero to disable)

      :type: int in [0, 1000], default 0

   .. attribute:: pie_menu_radius

      Pie menu size in pixels

      :type: int in [0, 1000], default 0

   .. attribute:: pie_menu_threshold

      Distance from center needed before a selection can be made

      :type: int in [0, 1000], default 0

   .. attribute:: rotation_angle

      Rotation step for numerical pad keys (2 4 6 8)

      :type: float in [0, 90], default 0.0

   .. attribute:: show_column_layout

      Use a column layout for toolbox

      :type: boolean, default False

   .. attribute:: show_large_cursors

      Use large mouse cursors when available

      :type: boolean, default False

   .. attribute:: show_manipulator

      Use 3D transform manipulator

      :type: boolean, default False

   .. attribute:: show_mini_axis

      Show a small rotating 3D axes in the bottom left corner of the 3D View

      :type: boolean, default False

   .. attribute:: show_object_info

      Display objects name and frame number in 3D view

      :type: boolean, default False

   .. attribute:: show_playback_fps

      Show the frames per second screen refresh rate, while animation is played back

      :type: boolean, default False

   .. attribute:: show_splash

      Display splash screen on startup

      :type: boolean, default False

   .. attribute:: show_tooltips

      Display tooltips (when off hold Alt to force display)

      :type: boolean, default False

   .. attribute:: show_tooltips_python

      Show Python references in tooltips

      :type: boolean, default False

   .. attribute:: show_view_name

      Show the name of the view's direction in each 3D View

      :type: boolean, default False

   .. attribute:: smooth_view

      Time to animate the view in milliseconds, zero to disable

      :type: int in [0, 1000], default 0

   .. attribute:: timecode_style

      Format of Time Codes displayed when not displaying timing in terms of frames

      * ``MINIMAL`` Minimal Info, Most compact representation, uses '+' as separator for sub-second frame numbers, with left and right truncation of the timecode as necessary.
      * ``SMPTE`` SMPTE (Full), Full SMPTE timecode (format is HH:MM:SS:FF).
      * ``SMPTE_COMPACT`` SMPTE (Compact), SMPTE timecode showing minutes, seconds, and frames only - hours are also shown if necessary, but not by default.
      * ``MILLISECONDS`` Compact with Milliseconds, Similar to SMPTE (Compact), except that instead of frames, milliseconds are shown instead.
      * ``SECONDS_ONLY`` Only Seconds, Direct conversion of frame numbers to seconds.

      :type: enum in ['MINIMAL', 'SMPTE', 'SMPTE_COMPACT', 'MILLISECONDS', 'SECONDS_ONLY'], default 'MINIMAL'

   .. attribute:: ui_line_width

      Changes the thickness of lines and points in the interface

      * ``THIN`` Thin, Thinner lines than the default.
      * ``AUTO`` Auto, Automatic line width based on UI scale.
      * ``THICK`` Thick, Thicker lines than the default.

      :type: enum in ['THIN', 'AUTO', 'THICK'], default 'AUTO'

   .. attribute:: ui_scale

      Changes the size of the fonts and buttons in the interface

      :type: float in [0.25, 4], default 1.0

   .. attribute:: use_auto_perspective

      Automatically switch between orthographic and perspective when changing from top/front/side views

      :type: boolean, default False

   .. attribute:: use_camera_lock_parent

      When the camera is locked to the view and in fly mode, transform the parent rather than the camera

      :type: boolean, default False

   .. attribute:: use_cursor_lock_adjust

      Place the cursor without 'jumping' to the new location (when lock-to-cursor is used)

      :type: boolean, default False

   .. attribute:: use_directional_menus

      Otherwise menus, etc will always be top to bottom, left to right, no matter opening direction

      :type: boolean, default False

   .. attribute:: use_global_pivot

      Lock the same rotation/scaling pivot in all 3D Views

      :type: boolean, default False

   .. attribute:: use_global_scene

      Force the current Scene to be displayed in all Screens

      :type: boolean, default False

   .. attribute:: use_mouse_depth_cursor

      Use the depth under the mouse when placing the cursor

      :type: boolean, default False

   .. attribute:: use_mouse_depth_navigate

      Use the depth under the mouse to improve view pan/rotate/zoom functionality

      :type: boolean, default False

   .. attribute:: use_mouse_over_open

      Open menu buttons and pulldowns automatically when the mouse is hovering

      :type: boolean, default False

   .. attribute:: use_quit_dialog

      Ask for confirmation when quitting through the window close button

      :type: boolean, default False

   .. attribute:: use_rotate_around_active

      Use selection as the pivot point

      :type: boolean, default False

   .. attribute:: use_zoom_to_mouse

      Zoom in towards the mouse pointer's position in the 3D view, rather than the 2D window center

      :type: boolean, default False

   .. attribute:: view2d_grid_spacing_min

      Minimum number of pixels between each gridline in 2D Viewports

      :type: int in [1, 500], default 0

   .. attribute:: view_frame_keyframes

      Keyframes around cursor that we zoom around

      :type: int in [1, 500], default 0

   .. attribute:: view_frame_seconds

      Seconds around cursor that we zoom around

      :type: float in [0, 10000], default 0.0

   .. attribute:: view_frame_type

      How zooming to frame focuses around current frame

      :type: enum in ['KEEP_RANGE', 'SECONDS', 'KEYFRAMES'], default 'KEEP_RANGE'

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

   * :class:`UserPreferences.view`


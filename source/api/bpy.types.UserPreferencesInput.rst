UserPreferencesInput(bpy_struct)
================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: UserPreferencesInput(bpy_struct)

   Settings for input devices

   .. attribute:: active_keyconfig

      The name of the active key configuration

      :type: string, default "", (never None)

   .. attribute:: drag_threshold

      Amount of pixels you have to drag before dragging UI items happens

      :type: int in [3, 40], default 0

   .. attribute:: invert_mouse_zoom

      Invert the axis of mouse movement for zooming

      :type: boolean, default False

   .. attribute:: invert_zoom_wheel

      Swap the Mouse Wheel zoom direction

      :type: boolean, default False

   .. attribute:: mouse_double_click_time

      Time/delay (in ms) for a double click

      :type: int in [1, 1000], default 0

   .. attribute:: navigation_mode

      Which method to use for viewport navigation

      * ``WALK`` Walk, Interactively walk or free navigate around the scene.
      * ``FLY`` Fly, Use fly dynamics to navigate the scene.

      :type: enum in ['WALK', 'FLY'], default 'WALK'

   .. attribute:: ndof_deadzone

      Threshold of initial movement needed from the device's rest position

      :type: float in [0, 1], default 0.0

   .. attribute:: ndof_fly_helicopter

      Device up/down directly controls your Z position

      :type: boolean, default False

   .. attribute:: ndof_lock_horizon

      Keep horizon level while flying with 3D Mouse

      :type: boolean, default False

   .. attribute:: ndof_orbit_sensitivity

      Overall sensitivity of the 3D Mouse for orbiting

      :type: float in [0.01, 40], default 0.0

   .. attribute:: ndof_pan_yz_swap_axis

      Pan using up/down on the device (otherwise forward/backward)

      :type: boolean, default False

   .. attribute:: ndof_panx_invert_axis

      :type: boolean, default False

   .. attribute:: ndof_pany_invert_axis

      :type: boolean, default False

   .. attribute:: ndof_panz_invert_axis

      :type: boolean, default False

   .. attribute:: ndof_rotx_invert_axis

      :type: boolean, default False

   .. attribute:: ndof_roty_invert_axis

      :type: boolean, default False

   .. attribute:: ndof_rotz_invert_axis

      :type: boolean, default False

   .. attribute:: ndof_sensitivity

      Overall sensitivity of the 3D Mouse for panning

      :type: float in [0.01, 40], default 0.0

   .. attribute:: ndof_show_guide

      Display the center and axis during rotation

      :type: boolean, default False

   .. attribute:: ndof_view_navigate_method

      Navigation style in the viewport

      * ``FREE`` Free, Use full 6 degrees of freedom by default.
      * ``ORBIT`` Orbit, Orbit about the view center by default.

      :type: enum in ['FREE', 'ORBIT'], default 'FREE'

   .. attribute:: ndof_view_rotate_method

      Rotation style in the viewport

      * ``TURNTABLE`` Turntable, Use turntable style rotation in the viewport.
      * ``TRACKBALL`` Trackball, Use trackball style rotation in the viewport.

      :type: enum in ['TURNTABLE', 'TRACKBALL'], default 'TRACKBALL'

   .. attribute:: ndof_zoom_invert

      Zoom using opposite direction

      :type: boolean, default False

   .. attribute:: select_mouse

      Mouse button used for selection

      * ``LEFT`` Left, Use left Mouse Button for selection.
      * ``RIGHT`` Right, Use Right Mouse Button for selection.

      :type: enum in ['LEFT', 'RIGHT'], default 'RIGHT'

   .. attribute:: tweak_threshold

      Number of pixels you have to drag before tweak event is triggered

      :type: int in [3, 1024], default 0

   .. attribute:: use_emulate_numpad

      Main 1 to 0 keys act as the numpad ones (useful for laptops)

      :type: boolean, default False

   .. attribute:: use_mouse_continuous

      Allow moving the mouse outside the view on some manipulations (transform, ui control drag)

      :type: boolean, default False

   .. attribute:: use_mouse_emulate_3_button

      Emulate Middle Mouse with Alt+Left Mouse (doesn't work with Left Mouse Select option)

      :type: boolean, default False

   .. attribute:: use_mouse_mmb_paste

      In text window, paste with middle mouse button instead of panning

      :type: boolean, default False

   .. data:: use_ndof

      :type: boolean, default True, (readonly)

   .. attribute:: use_trackpad_natural

      If your system uses 'natural' scrolling, this option keeps consistent trackpad usage throughout the UI

      :type: boolean, default False

   .. attribute:: view_rotate_method

      Rotation style in the viewport

      * ``TURNTABLE`` Turntable, Use turntable style rotation in the viewport.
      * ``TRACKBALL`` Trackball, Use trackball style rotation in the viewport.

      :type: enum in ['TURNTABLE', 'TRACKBALL'], default 'TURNTABLE'

   .. attribute:: view_zoom_axis

      Axis of mouse movement to zoom in or out on

      * ``VERTICAL`` Vertical, Zoom in and out based on vertical mouse movement.
      * ``HORIZONTAL`` Horizontal, Zoom in and out based on horizontal mouse movement.

      :type: enum in ['VERTICAL', 'HORIZONTAL'], default 'VERTICAL'

   .. attribute:: view_zoom_method

      Which style to use for viewport scaling

      * ``CONTINUE`` Continue, Old style zoom, continues while moving mouse up or down.
      * ``DOLLY`` Dolly, Zoom in and out based on vertical mouse movement.
      * ``SCALE`` Scale, Zoom in and out like scaling the view, mouse movements relative to center.

      :type: enum in ['CONTINUE', 'DOLLY', 'SCALE'], default 'CONTINUE'

   .. data:: walk_navigation

      Settings for walk navigation mode

      :type: :class:`WalkNavigation`, (readonly, never None)

   .. attribute:: wheel_scroll_lines

      Number of lines scrolled at a time with the mouse wheel

      :type: int in [0, 32], default 0

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

   * :class:`UserPreferences.inputs`


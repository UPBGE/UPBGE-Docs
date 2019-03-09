SpaceGraphEditor(Space)
=======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceGraphEditor(Space)

   Graph Editor space data

   .. attribute:: auto_snap

      Automatic time snapping settings for transformations

      * ``NONE`` No Auto-Snap.
      * ``STEP`` Frame Step, Snap to 1.0 frame intervals.
      * ``TIME_STEP`` Second Step, Snap to 1.0 second intervals.
      * ``FRAME`` Nearest Frame, Snap to actual frames (nla-action time).
      * ``SECOND`` Nearest Second, Snap to actual seconds (nla-action time).
      * ``MARKER`` Nearest Marker, Snap to nearest marker.

      :type: enum in ['NONE', 'STEP', 'TIME_STEP', 'FRAME', 'SECOND', 'MARKER'], default 'NONE'

   .. attribute:: cursor_position_x

      Graph Editor 2D-Value cursor - X-Value component

      :type: float in [-inf, inf], default 0.0

   .. attribute:: cursor_position_y

      Graph Editor 2D-Value cursor - Y-Value component

      :type: float in [-inf, inf], default 0.0

   .. data:: dopesheet

      Settings for filtering animation data

      :type: :class:`DopeSheet`, (readonly)

   .. data:: has_ghost_curves

      Graph Editor instance has some ghost curves stored

      :type: boolean, default False, (readonly)

   .. attribute:: mode

      Editing context being displayed

      * ``FCURVES`` F-Curve, Edit animation/keyframes displayed as 2D curves.
      * ``DRIVERS`` Drivers, Edit drivers.

      :type: enum in ['FCURVES', 'DRIVERS'], default 'FCURVES'

   .. attribute:: pivot_point

      Pivot center for rotation/scaling

      :type: enum in ['BOUNDING_BOX_CENTER', 'CURSOR', 'INDIVIDUAL_ORIGINS'], default 'BOUNDING_BOX_CENTER'

   .. attribute:: show_cursor

      Show 2D cursor

      :type: boolean, default False

   .. attribute:: show_frame_indicator

      Show frame number beside the current frame indicator line

      :type: boolean, default False

   .. attribute:: show_group_colors

      Draw groups and channels with colors matching their corresponding groups

      :type: boolean, default False

   .. attribute:: show_handles

      Show handles of Bezier control points

      :type: boolean, default False

   .. attribute:: show_seconds

      Show timing in seconds not frames

      :type: boolean, default False

   .. attribute:: show_sliders

      Show sliders beside F-Curve channels

      :type: boolean, default False

   .. attribute:: use_auto_merge_keyframes

      Automatically merge nearby keyframes

      :type: boolean, default False

   .. attribute:: use_auto_normalization

      Automatically recalculate curve normalization on every curve edit

      :type: boolean, default False

   .. attribute:: use_beauty_drawing

      Draw F-Curves using Anti-Aliasing and other fancy effects (disable for better performance)

      :type: boolean, default False

   .. attribute:: use_normalization

      Display curves in normalized to -1..1 range, for easier editing of multiple curves with different ranges

      :type: boolean, default False

   .. attribute:: use_only_selected_curves_handles

      Only keyframes of selected F-Curves are visible and editable

      :type: boolean, default False

   .. attribute:: use_only_selected_keyframe_handles

      Only show and edit handles of selected keyframes

      :type: boolean, default False

   .. attribute:: use_realtime_update

      When transforming keyframes, changes to the animation data are flushed to other views

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


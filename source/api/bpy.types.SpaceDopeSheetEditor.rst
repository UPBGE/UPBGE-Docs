SpaceDopeSheetEditor(Space)
===========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceDopeSheetEditor(Space)

   Dope Sheet space data

   .. attribute:: action

      Action displayed and edited in this space

      :type: :class:`Action`

   .. attribute:: auto_snap

      Automatic time snapping settings for transformations

      * ``NONE`` No Auto-Snap.
      * ``STEP`` Frame Step, Snap to 1.0 frame intervals.
      * ``TIME_STEP`` Second Step, Snap to 1.0 second intervals.
      * ``FRAME`` Nearest Frame, Snap to actual frames (nla-action time).
      * ``SECOND`` Nearest Second, Snap to actual seconds (nla-action time).
      * ``MARKER`` Nearest Marker, Snap to nearest marker.

      :type: enum in ['NONE', 'STEP', 'TIME_STEP', 'FRAME', 'SECOND', 'MARKER'], default 'NONE'

   .. data:: dopesheet

      Settings for filtering animation data

      :type: :class:`DopeSheet`, (readonly)

   .. attribute:: mode

      Editing context being displayed

      * ``DOPESHEET`` Dope Sheet, Edit all keyframes in scene.
      * ``ACTION`` Action Editor, Edit keyframes in active object's Object-level action.
      * ``SHAPEKEY`` Shape Key Editor, Edit keyframes in active object's Shape Keys action.
      * ``GPENCIL`` Grease Pencil, Edit timings for all Grease Pencil sketches in file.
      * ``MASK`` Mask, Edit timings for Mask Editor splines.
      * ``CACHEFILE`` Cache File, Edit timings for Cache File data-blocks.

      :type: enum in ['DOPESHEET', 'ACTION', 'SHAPEKEY', 'GPENCIL', 'MASK', 'CACHEFILE'], default 'ACTION'

   .. attribute:: show_frame_indicator

      Show frame number beside the current frame indicator line

      :type: boolean, default False

   .. attribute:: show_group_colors

      Draw groups and channels with colors matching their corresponding groups (pose bones only currently)

      :type: boolean, default False

   .. attribute:: show_pose_markers

      Show markers belonging to the active action instead of Scene markers (Action and Shape Key Editors only)

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

   .. attribute:: use_marker_sync

      Sync Markers with keyframe edits

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


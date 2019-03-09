SpaceNLA(Space)
===============

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceNLA(Space)

   NLA editor space data

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

   .. attribute:: show_frame_indicator

      Show frame number beside the current frame indicator line

      :type: boolean, default False

   .. attribute:: show_local_markers

      Show action-local markers on the strips, useful when synchronizing timing across strips

      :type: boolean, default False

   .. attribute:: show_seconds

      Show timing in seconds not frames

      :type: boolean, default False

   .. attribute:: show_strip_curves

      Show influence F-Curves on strips

      :type: boolean, default False

   .. attribute:: use_realtime_update

      When transforming strips, changes to the animation data are flushed to other views

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


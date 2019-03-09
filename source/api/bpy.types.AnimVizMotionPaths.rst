AnimVizMotionPaths(bpy_struct)
==============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: AnimVizMotionPaths(bpy_struct)

   Motion Path settings for animation visualization

   .. attribute:: bake_location

      When calculating Bone Paths, use Head or Tips

      * ``HEADS`` Heads, Calculate bone paths from heads.
      * ``TAILS`` Tails, Calculate bone paths from tails.

      :type: enum in ['HEADS', 'TAILS'], default 'TAILS'

   .. attribute:: frame_after

      Number of frames to show after the current frame (only for 'Around Current Frame' Onion-skinning method)

      :type: int in [1, 524287], default 0

   .. attribute:: frame_before

      Number of frames to show before the current frame (only for 'Around Current Frame' Onion-skinning method)

      :type: int in [1, 524287], default 0

   .. attribute:: frame_end

      End frame of range of paths to display/calculate (not for 'Around Current Frame' Onion-skinning method)

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_start

      Starting frame of range of paths to display/calculate (not for 'Around Current Frame' Onion-skinning method)

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_step

      Number of frames between paths shown (not for 'On Keyframes' Onion-skinning method)

      :type: int in [1, 100], default 0

   .. data:: has_motion_paths

      Are there any bone paths that will need updating (read-only)

      :type: boolean, default False, (readonly)

   .. attribute:: show_frame_numbers

      Show frame numbers on Motion Paths

      :type: boolean, default False

   .. attribute:: show_keyframe_action_all

      For bone motion paths, search whole Action for keyframes instead of in group with matching name only (is slower)

      :type: boolean, default False

   .. attribute:: show_keyframe_highlight

      Emphasize position of keyframes on Motion Paths

      :type: boolean, default False

   .. attribute:: show_keyframe_numbers

      Show frame numbers of Keyframes on Motion Paths

      :type: boolean, default False

   .. attribute:: type

      Type of range to show for Motion Paths

      * ``CURRENT_FRAME`` Around Frame, Display Paths of poses within a fixed number of frames around the current frame.
      * ``RANGE`` In Range, Display Paths of poses within specified range.

      :type: enum in ['CURRENT_FRAME', 'RANGE'], default 'RANGE'

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

   * :class:`AnimViz.motion_path`


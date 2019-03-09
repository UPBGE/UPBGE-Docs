AnimVizOnionSkinning(bpy_struct)
================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: AnimVizOnionSkinning(bpy_struct)

   Onion Skinning settings for animation visualization

   .. attribute:: frame_after

      Number of frames to show after the current frame (only for 'Around Current Frame' Onion-skinning method)

      :type: int in [0, 30], default 0

   .. attribute:: frame_before

      Number of frames to show before the current frame (only for 'Around Current Frame' Onion-skinning method)

      :type: int in [0, 30], default 0

   .. attribute:: frame_end

      End frame of range of Ghosts to display (not for 'Around Current Frame' Onion-skinning method)

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_start

      Starting frame of range of Ghosts to display (not for 'Around Current Frame' Onion-skinning method)

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_step

      Number of frames between ghosts shown (not for 'On Keyframes' Onion-skinning method)

      :type: int in [1, 20], default 0

   .. attribute:: show_only_selected

      For Pose-Mode drawing, only draw ghosts for selected bones

      :type: boolean, default False

   .. attribute:: type

      Method used for determining what ghosts get drawn

      * ``NONE`` No Ghosts, Do not show any ghosts.
      * ``CURRENT_FRAME`` Around Current Frame, Show ghosts from around the current frame.
      * ``RANGE`` In Range, Show ghosts for the specified frame range.
      * ``KEYS`` On Keyframes, Show ghosts on keyframes.

      :type: enum in ['NONE', 'CURRENT_FRAME', 'RANGE', 'KEYS'], default 'NONE'

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

   * :class:`AnimViz.onion_skin_frames`


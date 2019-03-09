FModifierCycles(FModifier)
==========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`FModifier`

.. class:: FModifierCycles(FModifier)

   Repeat the values of the modified F-Curve

   .. attribute:: cycles_after

      Maximum number of cycles to allow after last keyframe (0 = infinite)

      :type: int in [-32768, 32767], default 0

   .. attribute:: cycles_before

      Maximum number of cycles to allow before first keyframe (0 = infinite)

      :type: int in [-32768, 32767], default 0

   .. attribute:: mode_after

      Cycling mode to use after last keyframe

      * ``NONE`` No Cycles, Don't do anything.
      * ``REPEAT`` Repeat Motion, Repeat keyframe range as-is.
      * ``REPEAT_OFFSET`` Repeat with Offset, Repeat keyframe range, but with offset based on gradient between start and end values.
      * ``MIRROR`` Repeat Mirrored, Alternate between forward and reverse playback of keyframe range.

      :type: enum in ['NONE', 'REPEAT', 'REPEAT_OFFSET', 'MIRROR'], default 'NONE'

   .. attribute:: mode_before

      Cycling mode to use before first keyframe

      * ``NONE`` No Cycles, Don't do anything.
      * ``REPEAT`` Repeat Motion, Repeat keyframe range as-is.
      * ``REPEAT_OFFSET`` Repeat with Offset, Repeat keyframe range, but with offset based on gradient between start and end values.
      * ``MIRROR`` Repeat Mirrored, Alternate between forward and reverse playback of keyframe range.

      :type: enum in ['NONE', 'REPEAT', 'REPEAT_OFFSET', 'MIRROR'], default 'NONE'

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
   * :class:`FModifier.type`
   * :class:`FModifier.show_expanded`
   * :class:`FModifier.mute`
   * :class:`FModifier.is_valid`
   * :class:`FModifier.active`
   * :class:`FModifier.use_restricted_range`
   * :class:`FModifier.frame_start`
   * :class:`FModifier.frame_end`
   * :class:`FModifier.blend_in`
   * :class:`FModifier.blend_out`
   * :class:`FModifier.use_influence`
   * :class:`FModifier.influence`

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


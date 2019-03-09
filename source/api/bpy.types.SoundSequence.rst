SoundSequence(Sequence)
=======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Sequence`

.. class:: SoundSequence(Sequence)

   Sequence strip defining a sound to be played over a period of time

   .. attribute:: animation_offset_end

      Animation end offset (trim end)

      :type: int in [0, inf], default 0

   .. attribute:: animation_offset_start

      Animation start offset (trim start)

      :type: int in [0, inf], default 0

   .. attribute:: pan

      Playback panning of the sound (only for Mono sources)

      :type: float in [-2, 2], default 0.0

   .. attribute:: pitch

      Playback pitch of the sound

      :type: float in [0.1, 10], default 0.0

   .. attribute:: show_waveform

      Whether to draw the sound's waveform

      :type: boolean, default False

   .. attribute:: sound

      Sound data-block used by this sequence

      :type: :class:`Sound`

   .. attribute:: volume

      Playback volume of the sound

      :type: float in [0, 100], default 0.0

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
   * :class:`Sequence.name`
   * :class:`Sequence.type`
   * :class:`Sequence.select`
   * :class:`Sequence.select_left_handle`
   * :class:`Sequence.select_right_handle`
   * :class:`Sequence.mute`
   * :class:`Sequence.lock`
   * :class:`Sequence.frame_final_duration`
   * :class:`Sequence.frame_duration`
   * :class:`Sequence.frame_start`
   * :class:`Sequence.frame_final_start`
   * :class:`Sequence.frame_final_end`
   * :class:`Sequence.frame_offset_start`
   * :class:`Sequence.frame_offset_end`
   * :class:`Sequence.frame_still_start`
   * :class:`Sequence.frame_still_end`
   * :class:`Sequence.channel`
   * :class:`Sequence.use_linear_modifiers`
   * :class:`Sequence.blend_type`
   * :class:`Sequence.blend_alpha`
   * :class:`Sequence.effect_fader`
   * :class:`Sequence.use_default_fade`
   * :class:`Sequence.speed_factor`
   * :class:`Sequence.modifiers`

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
   * :class:`Sequence.update`
   * :class:`Sequence.strip_elem_from_frame`
   * :class:`Sequence.swap`


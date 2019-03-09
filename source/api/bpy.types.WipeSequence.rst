WipeSequence(EffectSequence)
============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Sequence`, :class:`EffectSequence`

.. class:: WipeSequence(EffectSequence)

   Sequence strip creating a wipe transition

   .. attribute:: angle

      Edge angle

      :type: float in [-1.5708, 1.5708], default 0.0

   .. attribute:: blur_width

      Width of the blur edge, in percentage relative to the image size

      :type: float in [0, 1], default 0.0

   .. attribute:: direction

      Wipe direction

      :type: enum in ['OUT', 'IN'], default 'OUT'

   .. attribute:: input_1

      First input for the effect strip

      :type: :class:`Sequence`, (never None)

   .. attribute:: input_2

      Second input for the effect strip

      :type: :class:`Sequence`, (never None)

   .. data:: input_count

      :type: int in [0, inf], default 0, (readonly)

   .. attribute:: transition_type

      :type: enum in ['SINGLE', 'DOUBLE', 'IRIS', 'CLOCK'], default 'SINGLE'

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
   * :class:`EffectSequence.use_deinterlace`
   * :class:`EffectSequence.alpha_mode`
   * :class:`EffectSequence.use_flip_x`
   * :class:`EffectSequence.use_flip_y`
   * :class:`EffectSequence.use_float`
   * :class:`EffectSequence.use_reverse_frames`
   * :class:`EffectSequence.color_multiply`
   * :class:`EffectSequence.color_saturation`
   * :class:`EffectSequence.strobe`
   * :class:`EffectSequence.use_translation`
   * :class:`EffectSequence.transform`
   * :class:`EffectSequence.use_crop`
   * :class:`EffectSequence.crop`
   * :class:`EffectSequence.use_proxy`
   * :class:`EffectSequence.proxy`

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


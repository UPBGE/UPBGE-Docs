Sequence(bpy_struct)
====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`EffectSequence`, :class:`ImageSequence`, :class:`MaskSequence`, :class:`MetaSequence`, :class:`MovieClipSequence`, :class:`MovieSequence`, :class:`SceneSequence`, :class:`SoundSequence`

.. class:: Sequence(bpy_struct)

   Sequence strip in the sequence editor

   .. attribute:: blend_alpha

      Percentage of how much the strip's colors affect other strips

      :type: float in [0, 1], default 0.0

   .. attribute:: blend_type

      Method for controlling how the strip combines with other strips

      :type: enum in ['REPLACE', 'CROSS', 'ADD', 'SUBTRACT', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS', 'MULTIPLY', 'OVER_DROP', 'LIGHTEN', 'DARKEN', 'SCREEN', 'OVERLAY', 'DODGE', 'BURN', 'LINEAR_BURN', 'SOFT_LIGHT', 'HARD_LIGHT', 'PIN_LIGHT', 'LINEAR_LIGHT', 'VIVID_LIGHT', 'COLOR', 'HUE', 'SATURATION', 'VALUE', 'DIFFERENCE', 'EXCLUSION'], default 'REPLACE'

   .. attribute:: channel

      Y position of the sequence strip

      :type: int in [1, 32], default 0

   .. attribute:: effect_fader

      Custom fade value

      :type: float in [0, 1], default 0.0

   .. data:: frame_duration

      The length of the contents of this strip before the handles are applied

      :type: int in [1, 1048574], default 0, (readonly)

   .. attribute:: frame_final_duration

      The length of the contents of this strip after the handles are applied

      :type: int in [1, 1048574], default 0

   .. attribute:: frame_final_end

      End frame displayed in the sequence editor after offsets are applied

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_final_start

      Start frame displayed in the sequence editor after offsets are applied, setting this is equivalent to moving the handle, not the actual start frame

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_offset_end

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_offset_start

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_start

      X position where the strip begins

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_still_end

      :type: int in [0, 1048574], default 0

   .. attribute:: frame_still_start

      :type: int in [0, 1048574], default 0

   .. attribute:: lock

      Lock strip so that it cannot be transformed

      :type: boolean, default False

   .. data:: modifiers

      Modifiers affecting this strip

      :type: :class:`SequenceModifiers` :class:`bpy_prop_collection` of :class:`SequenceModifier`, (readonly)

   .. attribute:: mute

      Disable strip so that it cannot be viewed in the output

      :type: boolean, default False

   .. attribute:: name

      :type: string, default "", (never None)

   .. attribute:: select

      :type: boolean, default False

   .. attribute:: select_left_handle

      :type: boolean, default False

   .. attribute:: select_right_handle

      :type: boolean, default False

   .. attribute:: speed_factor

      Multiply the current speed of the sequence with this number or remap current frame to this frame

      :type: float in [-inf, inf], default 0.0

   .. data:: type

      :type: enum in ['IMAGE', 'META', 'SCENE', 'MOVIE', 'MOVIECLIP', 'MASK', 'SOUND', 'CROSS', 'ADD', 'SUBTRACT', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS', 'MULTIPLY', 'OVER_DROP', 'WIPE', 'GLOW', 'TRANSFORM', 'COLOR', 'SPEED', 'MULTICAM', 'ADJUSTMENT', 'GAUSSIAN_BLUR', 'TEXT', 'COLORMIX'], default 'IMAGE', (readonly)

   .. attribute:: use_default_fade

      Fade effect using the built-in default (usually make transition as long as effect strip)

      :type: boolean, default False

   .. attribute:: use_linear_modifiers

      Calculate modifiers in linear space instead of sequencer's space

      :type: boolean, default False

   .. method:: update(data=False)

      Update the strip dimensions

      :arg data:

         Data, Update strip data

      :type data: boolean, (optional)

   .. method:: strip_elem_from_frame(frame)

      Return the strip element from a given frame or None

      :arg frame:

         Frame, The frame to get the strip element from

      :type frame: int in [-1048574, 1048574]
      :return:

         strip element of the current frame

      :rtype: :class:`SequenceElement`

   .. method:: swap(other)

      swap

      :arg other:

         Other

      :type other: :class:`Sequence`, (never None)

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

   * :mod:`bpy.context.selected_editable_sequences`
   * :mod:`bpy.context.selected_sequences`
   * :mod:`bpy.context.sequences`
   * :class:`AddSequence.input_1`
   * :class:`AddSequence.input_2`
   * :class:`AlphaOverSequence.input_1`
   * :class:`AlphaOverSequence.input_2`
   * :class:`AlphaUnderSequence.input_1`
   * :class:`AlphaUnderSequence.input_2`
   * :class:`ColorMixSequence.input_1`
   * :class:`ColorMixSequence.input_2`
   * :class:`CrossSequence.input_1`
   * :class:`CrossSequence.input_2`
   * :class:`GammaCrossSequence.input_1`
   * :class:`GammaCrossSequence.input_2`
   * :class:`GaussianBlurSequence.input_1`
   * :class:`GlowSequence.input_1`
   * :class:`MetaSequence.sequences`
   * :class:`MultiplySequence.input_1`
   * :class:`MultiplySequence.input_2`
   * :class:`OverDropSequence.input_1`
   * :class:`OverDropSequence.input_2`
   * :class:`Sequence.swap`
   * :class:`SequenceEditor.active_strip`
   * :class:`SequenceEditor.meta_stack`
   * :class:`SequenceEditor.sequences`
   * :class:`SequenceEditor.sequences_all`
   * :class:`SequenceModifier.input_mask_strip`
   * :class:`Sequences.new_clip`
   * :class:`Sequences.new_effect`
   * :class:`Sequences.new_effect`
   * :class:`Sequences.new_effect`
   * :class:`Sequences.new_effect`
   * :class:`Sequences.new_image`
   * :class:`Sequences.new_mask`
   * :class:`Sequences.new_movie`
   * :class:`Sequences.new_scene`
   * :class:`Sequences.new_sound`
   * :class:`Sequences.remove`
   * :class:`SpeedControlSequence.input_1`
   * :class:`SubtractSequence.input_1`
   * :class:`SubtractSequence.input_2`
   * :class:`TransformSequence.input_1`
   * :class:`WipeSequence.input_1`
   * :class:`WipeSequence.input_2`


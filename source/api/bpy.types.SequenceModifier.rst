SequenceModifier(bpy_struct)
============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`BrightContrastModifier`, :class:`ColorBalanceModifier`, :class:`CurvesModifier`, :class:`HueCorrectModifier`, :class:`SequencerTonemapModifierData`, :class:`WhiteBalanceModifier`

.. class:: SequenceModifier(bpy_struct)

   Modifier for sequence strip

   .. attribute:: input_mask_id

      Mask ID used as mask input for the modifier

      :type: :class:`Mask`

   .. attribute:: input_mask_strip

      Strip used as mask input for the modifier

      :type: :class:`Sequence`

   .. attribute:: input_mask_type

      Type of input data used for mask

      * ``STRIP`` Strip, Use sequencer strip as mask input.
      * ``ID`` Mask, Use mask ID as mask input.

      :type: enum in ['STRIP', 'ID'], default 'STRIP'

   .. attribute:: mask_time

      Time to use for the Mask animation

      * ``RELATIVE`` Relative, Mask animation is offset to start of strip.
      * ``ABSOLUTE`` Absolute, Mask animation is in sync with scene frame.

      :type: enum in ['RELATIVE', 'ABSOLUTE'], default 'RELATIVE'

   .. attribute:: mute

      Mute this modifier

      :type: boolean, default False

   .. attribute:: name

      :type: string, default "", (never None)

   .. attribute:: show_expanded

      Mute expanded settings for the modifier

      :type: boolean, default False

   .. data:: type

      :type: enum in ['COLOR_BALANCE', 'CURVES', 'HUE_CORRECT', 'BRIGHT_CONTRAST', 'MASK', 'WHITE_BALANCE', 'TONEMAP'], default 'COLOR_BALANCE', (readonly)

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

   * :class:`Sequence.modifiers`
   * :class:`SequenceModifiers.new`
   * :class:`SequenceModifiers.remove`


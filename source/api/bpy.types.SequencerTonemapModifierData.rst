SequencerTonemapModifierData(SequenceModifier)
==============================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`SequenceModifier`

.. class:: SequencerTonemapModifierData(SequenceModifier)

   Tone mapping modifier

   .. attribute:: adaptation

      If 0, global; if 1, based on pixel intensity

      :type: float in [0, 1], default 0.0

   .. attribute:: contrast

      Set to 0 to use estimate from input image

      :type: float in [0, 1], default 0.0

   .. attribute:: correction

      If 0, same for all channels; if 1, each independent

      :type: float in [0, 1], default 0.0

   .. attribute:: gamma

      If not used, set to 1

      :type: float in [0.001, 3], default 0.0

   .. attribute:: intensity

      If less than zero, darkens image; otherwise, makes it brighter

      :type: float in [-8, 8], default 0.0

   .. attribute:: key

      The value the average luminance is mapped to

      :type: float in [0, 1], default 0.0

   .. attribute:: offset

      Normally always 1, but can be used as an extra control to alter the brightness curve

      :type: float in [0.001, 10], default 0.0

   .. attribute:: tonemap_type

      Tone mapping algorithm

      :type: enum in ['RD_PHOTORECEPTOR', 'RH_SIMPLE'], default 'RH_SIMPLE'

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
   * :class:`SequenceModifier.name`
   * :class:`SequenceModifier.type`
   * :class:`SequenceModifier.mute`
   * :class:`SequenceModifier.show_expanded`
   * :class:`SequenceModifier.input_mask_type`
   * :class:`SequenceModifier.mask_time`
   * :class:`SequenceModifier.input_mask_strip`
   * :class:`SequenceModifier.input_mask_id`

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


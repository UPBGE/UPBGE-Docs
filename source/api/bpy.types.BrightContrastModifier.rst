BrightContrastModifier(SequenceModifier)
========================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`SequenceModifier`

.. class:: BrightContrastModifier(SequenceModifier)

   Bright/contrast modifier data for sequence strip

   .. attribute:: bright

      Adjust the luminosity of the colors

      :type: float in [-inf, inf], default 0.0

   .. attribute:: contrast

      Adjust the difference in luminosity between pixels

      :type: float in [-inf, inf], default 0.0

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


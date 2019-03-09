FModifierNoise(FModifier)
=========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`FModifier`

.. class:: FModifierNoise(FModifier)

   Give randomness to the modified F-Curve

   .. attribute:: blend_type

      Method of modifying the existing F-Curve

      :type: enum in ['REPLACE', 'ADD', 'SUBTRACT', 'MULTIPLY'], default 'REPLACE'

   .. attribute:: depth

      Amount of fine level detail present in the noise

      :type: int in [0, 32767], default 0

   .. attribute:: offset

      Time offset for the noise effect

      :type: float in [-inf, inf], default 0.0

   .. attribute:: phase

      A random seed for the noise effect

      :type: float in [-inf, inf], default 0.0

   .. attribute:: scale

      Scaling (in time) of the noise

      :type: float in [-inf, inf], default 0.0

   .. attribute:: strength

      Amplitude of the noise - the amount that it modifies the underlying curve

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


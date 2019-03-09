SoundActuator(Actuator)
=======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Actuator`

.. class:: SoundActuator(Actuator)

   Sound file

   .. attribute:: cone_inner_angle_3d

      The angle of the inner cone

      :type: float in [-inf, inf], default 0.0

   .. attribute:: cone_outer_angle_3d

      The angle of the outer cone

      :type: float in [-inf, inf], default 0.0

   .. attribute:: cone_outer_gain_3d

      The gain outside the outer cone (the gain in the outer cone will be interpolated between this value and the normal gain in the inner cone)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: distance_3d_max

      The maximum distance at which you can hear the sound

      :type: float in [-inf, inf], default 0.0

   .. attribute:: distance_3d_reference

      The distance where the sound has a gain of 1.0

      :type: float in [-inf, inf], default 0.0

   .. attribute:: gain_3d_max

      The maximum gain of the sound, no matter how near it is

      :type: float in [-inf, inf], default 0.0

   .. attribute:: gain_3d_min

      The minimum gain of the sound, no matter how far it is away

      :type: float in [-inf, inf], default 0.0

   .. attribute:: mode

      :type: enum in ['PLAYSTOP', 'PLAYEND', 'LOOPSTOP', 'LOOPEND', 'LOOPBIDIRECTIONAL', 'LOOPBIDIRECTIONALSTOP'], default 'PLAYSTOP'

   .. attribute:: pitch

      Pitch of the sound

      :type: float in [-inf, inf], default 0.0

   .. attribute:: rolloff_factor_3d

      The influence factor on volume depending on distance

      :type: float in [-inf, inf], default 0.0

   .. attribute:: sound

      :type: :class:`Sound`

   .. attribute:: use_sound_3d

      Enable/Disable 3D Sound

      :type: boolean, default False

   .. attribute:: volume

      Initial volume of the sound

      :type: float in [0, 2], default 0.0

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
   * :class:`Actuator.name`
   * :class:`Actuator.type`
   * :class:`Actuator.pin`
   * :class:`Actuator.show_expanded`
   * :class:`Actuator.active`

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
   * :class:`Actuator.link`
   * :class:`Actuator.unlink`


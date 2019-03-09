ActionActuator(Actuator)
========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Actuator`

.. class:: ActionActuator(Actuator)

   Actuator to control the object movement

   .. attribute:: action

      :type: :class:`Action`

   .. attribute:: apply_to_children

      Update Action on all children Objects as well

      :type: boolean, default False

   .. attribute:: blend_mode

      How this layer is blended with previous layers

      :type: enum in ['BLEND', 'ADD'], default 'BLEND'

   .. attribute:: frame_blend_in

      Number of frames of motion blending

      :type: int in [0, 32767], default 0

   .. attribute:: frame_end

      :type: float in [-inf, inf], default 0.0

   .. attribute:: frame_property

      Assign the action's current frame number to this property

      :type: string, default "", (never None)

   .. attribute:: frame_start

      :type: float in [-inf, inf], default 0.0

   .. attribute:: layer

      The animation layer to play the action on

      :type: int in [0, 32766], default 0

   .. attribute:: layer_weight

      How much of the previous layer to blend into this one

      :type: float in [0, 1], default 0.0

   .. attribute:: play_mode

      Action playback type

      :type: enum in ['PLAY', 'PINGPONG', 'FLIPPER', 'LOOPSTOP', 'LOOPEND', 'PROPERTY'], default 'PLAY'

   .. attribute:: priority

      Execution priority - lower numbers will override actions with higher numbers (with 2 or more actions at once, the overriding channels must be lower in the stack)

      :type: int in [0, 100], default 0

   .. attribute:: property

      Use this property to define the Action position

      :type: string, default "", (never None)

   .. attribute:: use_additive

      Action is added to the current loc/rot/scale in global or local coordinate according to Local flag

      :type: boolean, default False

   .. attribute:: use_continue_last_frame

      Restore last frame when switching on/off, otherwise play from the start each time

      :type: boolean, default False

   .. attribute:: use_force

      Apply Action as a global or local force depending on the local option (dynamic objects only)

      :type: boolean, default False

   .. attribute:: use_local

      Let the Action act in local coordinates, used in Force and Add mode

      :type: boolean, default False

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


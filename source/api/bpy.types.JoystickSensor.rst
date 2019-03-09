JoystickSensor(Sensor)
======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Sensor`

.. class:: JoystickSensor(Sensor)

   Sensor to detect joystick events

   .. attribute:: axis_direction

      The direction of the stick

      :type: enum in ['RIGHTAXIS', 'UPAXIS', 'LEFTAXIS', 'DOWNAXIS'], default 'RIGHTAXIS'

   .. attribute:: axis_number

      Which Stick to use

      :type: enum in ['LEFT_STICK', 'RIGHT_STICK'], default 'LEFT_STICK'

   .. attribute:: axis_threshold

      Threshold minimum to detect the stick/trigger

      :type: int in [0, 32768], default 0

   .. attribute:: axis_trigger_number

      Which trigger to detect

      :type: enum in ['LEFT_SHOULDER_TRIGGER', 'RIGHT_SHOULDER_TRIGGER'], default 'LEFT_SHOULDER_TRIGGER'

   .. attribute:: button_number

      Which button to use

      :type: enum in ['BUTTON_A', 'BUTTON_B', 'BUTTON_X', 'BUTTON_Y', 'BUTTON_BACK', 'BUTTON_GUIDE', 'BUTTON_START', 'BUTTON_STICK_LEFT', 'BUTTON_STICK_RIGHT', 'BUTTON_SHOULDER_LEFT', 'BUTTON_SHOULDER_RIGHT', 'BUTTON_DPAD_UP', 'BUTTON_DPAD_DOWN', 'BUTTON_DPAD_LEFT', 'BUTTON_DPAD_RIGHT'], default 'BUTTON_A'

   .. attribute:: event_type

      The type of event this joystick sensor is triggered on

      :type: enum in ['STICK_DIRECTIONS', 'STICK_AXIS', 'SHOULDER_TRIGGERS', 'BUTTONS'], default 'BUTTONS'

   .. attribute:: joystick_index

      Which joystick to use

      :type: int in [0, 7], default 0

   .. attribute:: single_axis_number

      Which stick single axis (vertical/horizontal/other) to detect

      :type: enum in ['LEFT_STICK_HORIZONTAL', 'LEFT_STICK_VERTICAL', 'RIGHT_STICK_HORIZONTAL', 'RIGHT_STICK_VERTICAL'], default 'LEFT_STICK_HORIZONTAL'

   .. attribute:: use_all_events

      Triggered by all events on this joystick's current type (axis/button)

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
   * :class:`Sensor.name`
   * :class:`Sensor.type`
   * :class:`Sensor.pin`
   * :class:`Sensor.active`
   * :class:`Sensor.show_expanded`
   * :class:`Sensor.invert`
   * :class:`Sensor.use_level`
   * :class:`Sensor.use_pulse_true_level`
   * :class:`Sensor.use_pulse_false_level`
   * :class:`Sensor.tick_skip`
   * :class:`Sensor.use_tap`
   * :class:`Sensor.controllers`

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
   * :class:`Sensor.link`
   * :class:`Sensor.unlink`


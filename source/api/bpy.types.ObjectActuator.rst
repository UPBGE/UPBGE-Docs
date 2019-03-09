ObjectActuator(Actuator)
========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Actuator`

.. class:: ObjectActuator(Actuator)

   Actuator to control the object movement

   .. attribute:: angular_velocity

      Angular velocity

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: damping

      Number of frames to reach the target velocity

      :type: int in [-32768, 32767], default 0

   .. attribute:: derivate_coefficient

      Not required, high values can cause instability

      :type: float in [-inf, inf], default 0.0

   .. attribute:: force

      Force

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: force_max_x

      Upper limit for X force

      :type: float in [-inf, inf], default 0.0

   .. attribute:: force_max_y

      Upper limit for Y force

      :type: float in [-inf, inf], default 0.0

   .. attribute:: force_max_z

      Upper limit for Z force

      :type: float in [-inf, inf], default 0.0

   .. attribute:: force_min_x

      Lower limit for X force

      :type: float in [-inf, inf], default 0.0

   .. attribute:: force_min_y

      Lower limit for Y force

      :type: float in [-inf, inf], default 0.0

   .. attribute:: force_min_z

      Lower limit for Z force

      :type: float in [-inf, inf], default 0.0

   .. attribute:: integral_coefficient

      Low value (0.01) for slow response, high value (0.5) for fast response

      :type: float in [-inf, inf], default 0.0

   .. attribute:: linear_velocity

      Linear velocity (in Servo mode it sets the target relative linear velocity, it will be achieved by automatic application of force - Null velocity is a valid target)

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: mode

      Specify the motion system

      :type: enum in ['OBJECT_NORMAL', 'OBJECT_SERVO', 'OBJECT_CHARACTER'], default 'OBJECT_NORMAL'

   .. attribute:: offset_location

      Location

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: offset_rotation

      Rotation

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: proportional_coefficient

      Typical value is 60x integral coefficient

      :type: float in [-inf, inf], default 0.0

   .. attribute:: reference_object

      Reference object for velocity calculation, leave empty for world reference

      :type: :class:`Object`

   .. attribute:: servo_mode

      Specify the servo control system

      :type: enum in ['SERVO_LINEAR', 'SERVO_ANGULAR'], default 'SERVO_LINEAR'

   .. attribute:: torque

      Torque

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: use_add_character_location

      Toggle between ADD and SET character location

      :type: boolean, default False

   .. attribute:: use_add_linear_velocity

      Toggles between ADD and SET linV

      :type: boolean, default False

   .. attribute:: use_character_jump

      Make the character jump using the settings in the physics properties

      :type: boolean, default False

   .. attribute:: use_local_angular_velocity

      Angular velocity is defined in local coordinates

      :type: boolean, default False

   .. attribute:: use_local_force

      Force is defined in local coordinates

      :type: boolean, default False

   .. attribute:: use_local_linear_velocity

      Velocity is defined in local coordinates

      :type: boolean, default False

   .. attribute:: use_local_location

      Location is defined in local coordinates

      :type: boolean, default False

   .. attribute:: use_local_rotation

      Rotation is defined in local coordinates

      :type: boolean, default False

   .. attribute:: use_local_torque

      Torque is defined in local coordinates

      :type: boolean, default False

   .. attribute:: use_servo_limit_x

      Set limit to force/torque along the X axis

      :type: boolean, default False

   .. attribute:: use_servo_limit_y

      Set limit to force/torque along the Y axis

      :type: boolean, default False

   .. attribute:: use_servo_limit_z

      Set limit to force/torque along the Z axis

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


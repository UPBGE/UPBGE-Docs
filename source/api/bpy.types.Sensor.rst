Sensor(bpy_struct)
==================

.. module:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`ActuatorSensor`, :class:`AlwaysSensor`, :class:`ArmatureSensor`, :class:`CollisionSensor`, :class:`DelaySensor`, :class:`JoystickSensor`, :class:`KeyboardSensor`, :class:`MessageSensor`, :class:`MouseSensor`, :class:`MovementSensor`, :class:`NearSensor`, :class:`PropertySensor`, :class:`RadarSensor`, :class:`RandomSensor`, :class:`RaySensor`

.. class:: Sensor(bpy_struct)

   Game engine logic brick to detect events

   .. attribute:: active

      Set active state of the sensor

      :type: boolean, default False

   .. data:: controllers

      The list containing the controllers connected to the sensor

      :type: :class:`bpy_prop_collection` of :class:`Controller`, (readonly)

   .. attribute:: invert

      Invert the level(output) of this sensor

      :type: boolean, default False

   .. attribute:: name

      Sensor name

      :type: string, default "", (never None)

   .. attribute:: pin

      Display when not linked to a visible states controller

      :type: boolean, default False

   .. attribute:: show_expanded

      Set sensor expanded in the user interface

      :type: boolean, default False

   .. attribute:: tick_skip

      Number of logic ticks skipped between 2 active pulses (0 = pulse every logic tick, 1 = skip 1 logic tick between pulses, etc.)

      :type: int in [0, 10000], default 0

   .. attribute:: type

      :type: enum in ['ACTUATOR', 'ALWAYS', 'ARMATURE', 'COLLISION', 'DELAY', 'JOYSTICK', 'KEYBOARD', 'MESSAGE', 'MOUSE', 'NEAR', 'PROPERTY', 'RADAR', 'MOVEMENT', 'RANDOM', 'RAY'], default 'ALWAYS'

   .. attribute:: use_level

      Level detector, trigger controllers of new states (only applicable upon logic state transition)

      :type: boolean, default False

   .. attribute:: use_pulse_false_level

      Activate FALSE level triggering (pulse mode)

      :type: boolean, default False

   .. attribute:: use_pulse_true_level

      Activate TRUE level triggering (pulse mode)

      :type: boolean, default False

   .. attribute:: use_tap

      Trigger controllers only for an instant, even while the sensor remains true

      :type: boolean, default False

   .. method:: link(controller)

      Link the sensor to a controller

      :arg controller:

         Controller to link to

      :type controller: :class:`Controller`

   .. method:: unlink(controller)

      Unlink the sensor from a controller

      :arg controller:

         Controller to unlink from

      :type controller: :class:`Controller`

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

   * :class:`Controller.link`
   * :class:`Controller.unlink`
   * :class:`GameObjectSettings.sensors`


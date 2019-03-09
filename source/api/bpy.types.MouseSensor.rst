MouseSensor(Sensor)
===================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Sensor`

.. class:: MouseSensor(Sensor)

   Sensor to detect mouse events

   .. attribute:: mask

      Mask filter compared with object's collision group

      :type: boolean array of 16 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

   .. attribute:: material

      Only look for objects with this material (blank = all objects)

      :type: string, default "", (never None)

   .. attribute:: mouse_event

      Type of event this mouse sensor should trigger on

      :type: enum in ['LEFTCLICK', 'MIDDLECLICK', 'RIGHTCLICK', 'WHEELUP', 'WHEELDOWN', 'MOVEMENT', 'MOUSEOVER', 'MOUSEOVERANY'], default 'LEFTCLICK'

   .. attribute:: property

      Only look for objects with this property (blank = all objects)

      :type: string, default "", (never None)

   .. attribute:: use_material

      Toggle collision on material or property

      * ``PROPERTY`` Property, Use a property for ray intersections.
      * ``MATERIAL`` Material, Use a material for ray intersections.

      :type: enum in ['PROPERTY', 'MATERIAL'], default 'PROPERTY'

   .. attribute:: use_pulse

      Moving the mouse over a different object generates a pulse

      :type: boolean, default False

   .. attribute:: use_x_ray

      Toggle X-Ray option (see through objects that don't have the property)

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


PropertySensor(Sensor)
======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Sensor`

.. class:: PropertySensor(Sensor)

   Sensor to detect values and changes in values of properties

   .. attribute:: evaluation_type

      Type of property evaluation

      :type: enum in ['PROPEQUAL', 'PROPNEQUAL', 'PROPINTERVAL', 'PROPCHANGED', 'PROPLESSTHAN', 'PROPGREATERTHAN'], default 'PROPEQUAL'

   .. attribute:: property

      :type: string, default "", (never None)

   .. attribute:: value

      Check for this value in types in Equal, Not Equal, Less Than and Greater Than types

      :type: string, default "", (never None)

   .. attribute:: value_max

      Maximum value in Interval type

      :type: string, default "", (never None)

   .. attribute:: value_min

      Minimum value in Interval type

      :type: string, default "", (never None)

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


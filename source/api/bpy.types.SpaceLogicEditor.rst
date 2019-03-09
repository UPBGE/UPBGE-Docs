SpaceLogicEditor(Space)
=======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceLogicEditor(Space)

   Logic editor space data

   .. attribute:: import_string

      Import string used to find the component when adding a new component

      :type: string, default "", (never None)

   .. attribute:: show_actuators_active_object

      Show actuators of active object

      :type: boolean, default False

   .. attribute:: show_actuators_active_states

      Show only actuators connected to active states

      :type: boolean, default False

   .. attribute:: show_actuators_linked_controller

      Show linked objects to the actuator

      :type: boolean, default False

   .. attribute:: show_actuators_selected_objects

      Show actuators of all selected objects

      :type: boolean, default False

   .. attribute:: show_controllers_active_object

      Show controllers of active object

      :type: boolean, default False

   .. attribute:: show_controllers_linked_controller

      Show linked objects to sensor/actuator

      :type: boolean, default False

   .. attribute:: show_controllers_selected_objects

      Show controllers of all selected objects

      :type: boolean, default False

   .. attribute:: show_sensors_active_object

      Show sensors of active object

      :type: boolean, default False

   .. attribute:: show_sensors_active_states

      Show only sensors connected to active states

      :type: boolean, default False

   .. attribute:: show_sensors_linked_controller

      Show linked objects to the controller

      :type: boolean, default False

   .. attribute:: show_sensors_selected_objects

      Show sensors of all selected objects

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


   .. function:: draw_handler_add()

      Undocumented
   .. function:: draw_handler_remove()

      Undocumented
.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Space.type`
   * :class:`Space.show_locked_time`

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


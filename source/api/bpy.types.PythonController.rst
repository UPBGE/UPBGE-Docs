PythonController(Controller)
============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Controller`

.. class:: PythonController(Controller)

   Controller executing a python script

   .. attribute:: mode

      Python script type (textblock or module - faster)

      :type: enum in ['SCRIPT', 'MODULE'], default 'SCRIPT'

   .. attribute:: module

      Module name and function to run, e.g. "someModule.main" (internal texts and external python files can be used)

      :type: string, default "", (never None)

   .. attribute:: text

      Text data-block with the python script

      :type: :class:`Text`

   .. attribute:: use_debug

      Continuously reload the module from disk for editing external modules without restarting

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
   * :class:`Controller.name`
   * :class:`Controller.type`
   * :class:`Controller.show_expanded`
   * :class:`Controller.active`
   * :class:`Controller.use_priority`
   * :class:`Controller.actuators`
   * :class:`Controller.states`

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
   * :class:`Controller.link`
   * :class:`Controller.unlink`


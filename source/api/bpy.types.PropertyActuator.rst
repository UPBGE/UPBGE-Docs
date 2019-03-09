PropertyActuator(Actuator)
==========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Actuator`

.. class:: PropertyActuator(Actuator)

   Actuator to handle properties

   .. attribute:: mode

      * ``ASSIGN`` Assign.
      * ``ADD`` Add.
      * ``COPY`` Copy.
      * ``TOGGLE`` Toggle, For bool/int/float/timer properties only.
      * ``LEVEL`` Level, For bool/int/float/timer properties only.

      :type: enum in ['ASSIGN', 'ADD', 'COPY', 'TOGGLE', 'LEVEL'], default 'ASSIGN'

   .. attribute:: object

      Copy from this Object

      :type: :class:`Object`

   .. attribute:: object_property

      Copy this property

      :type: string, default "", (never None)

   .. attribute:: property

      The name of the property

      :type: string, default "", (never None)

   .. attribute:: value

      The name of the property or the value to use (use "" around strings)

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


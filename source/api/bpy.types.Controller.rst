Controller(bpy_struct)
======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`AndController`, :class:`ExpressionController`, :class:`NandController`, :class:`NorController`, :class:`OrController`, :class:`PythonController`, :class:`XnorController`, :class:`XorController`

.. class:: Controller(bpy_struct)

   Game engine logic brick to process events, connecting sensors to actuators

   .. attribute:: active

      Set the active state of the controller

      :type: boolean, default False

   .. data:: actuators

      The list containing the actuators connected to the controller

      :type: :class:`bpy_prop_collection` of :class:`Actuator`, (readonly)

   .. attribute:: name

      :type: string, default "", (never None)

   .. attribute:: show_expanded

      Set controller expanded in the user interface

      :type: boolean, default False

   .. attribute:: states

      Set Controller state index (1 to 30)

      :type: int in [1, 30], default 0

   .. attribute:: type

      * ``LOGIC_AND`` And, Logic And.
      * ``LOGIC_OR`` Or, Logic Or.
      * ``LOGIC_NAND`` Nand, Logic Nand.
      * ``LOGIC_NOR`` Nor, Logic Nor.
      * ``LOGIC_XOR`` Xor, Logic Xor.
      * ``LOGIC_XNOR`` Xnor, Logic Xnor.
      * ``EXPRESSION`` Expression.
      * ``PYTHON`` Python.

      :type: enum in ['LOGIC_AND', 'LOGIC_OR', 'LOGIC_NAND', 'LOGIC_NOR', 'LOGIC_XOR', 'LOGIC_XNOR', 'EXPRESSION', 'PYTHON'], default 'LOGIC_AND'

   .. attribute:: use_priority

      Mark controller for execution before all non-marked controllers (good for startup scripts)

      :type: boolean, default False

   .. method:: link(sensor=None, actuator=None)

      Link the controller with a sensor/actuator

      :arg sensor:

         Sensor to link the controller to

      :type sensor: :class:`Sensor`, (optional)
      :arg actuator:

         Actuator to link the controller to

      :type actuator: :class:`Actuator`, (optional)

   .. method:: unlink(sensor=None, actuator=None)

      Unlink the controller from a sensor/actuator

      :arg sensor:

         Sensor to unlink the controller from

      :type sensor: :class:`Sensor`, (optional)
      :arg actuator:

         Actuator to unlink the controller from

      :type actuator: :class:`Actuator`, (optional)

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

   * :class:`Actuator.link`
   * :class:`Actuator.unlink`
   * :class:`GameObjectSettings.controllers`
   * :class:`Sensor.controllers`
   * :class:`Sensor.link`
   * :class:`Sensor.unlink`


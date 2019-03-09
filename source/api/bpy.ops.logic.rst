Logic Operators
===============

.. module:: bpy.ops.logic

.. function:: actuator_add(type='', name="", object="")

   Add an actuator to the active object

   :arg type:

      Type, Type of actuator to add

   :type type: enum in [], (optional)
   :arg name:

      Name, Name of the Actuator to add

   :type name: string, (optional, never None)
   :arg object:

      Object, Name of the Object to add the Actuator to

   :type object: string, (optional, never None)

.. function:: actuator_move(actuator="", object="", direction='UP')

   Move Actuator

   :arg actuator:

      Actuator, Name of the actuator to edit

   :type actuator: string, (optional, never None)
   :arg object:

      Object, Name of the object the actuator belongs to

   :type object: string, (optional, never None)
   :arg direction:

      Direction, Move Up or Down

   :type direction: enum in ['UP', 'DOWN'], (optional)

.. function:: actuator_remove(actuator="", object="")

   Remove an actuator from the active object

   :arg actuator:

      Actuator, Name of the actuator to edit

   :type actuator: string, (optional, never None)
   :arg object:

      Object, Name of the object the actuator belongs to

   :type object: string, (optional, never None)

.. function:: add_python_component(component_name="module.Component")

   Add a python component to the selected object

   :arg component_name:

      Component, The component class name with module (module.ComponentName)

   :type component_name: string, (never None)

.. function:: component_reload(index=0)

   Reload Component

   :arg index:

      Index, Component index to reload

   :type index: int in [0, inf], (optional)

.. function:: component_remove(index=0)

   Remove Component

   :arg index:

      Index, Component index to remove

   :type index: int in [0, inf], (optional)

.. function:: controller_add(type='LOGIC_AND', name="", object="")

   Add a controller to the active object

   :arg type:

      Type, Type of controller to add

      * ``LOGIC_AND`` And, Logic And.
      * ``LOGIC_OR`` Or, Logic Or.
      * ``LOGIC_NAND`` Nand, Logic Nand.
      * ``LOGIC_NOR`` Nor, Logic Nor.
      * ``LOGIC_XOR`` Xor, Logic Xor.
      * ``LOGIC_XNOR`` Xnor, Logic Xnor.
      * ``EXPRESSION`` Expression.
      * ``PYTHON`` Python.

   :type type: enum in ['LOGIC_AND', 'LOGIC_OR', 'LOGIC_NAND', 'LOGIC_NOR', 'LOGIC_XOR', 'LOGIC_XNOR', 'EXPRESSION', 'PYTHON'], (optional)
   :arg name:

      Name, Name of the Controller to add

   :type name: string, (optional, never None)
   :arg object:

      Object, Name of the Object to add the Controller to

   :type object: string, (optional, never None)

.. function:: controller_move(controller="", object="", direction='UP')

   Move Controller

   :arg controller:

      Controller, Name of the controller to edit

   :type controller: string, (optional, never None)
   :arg object:

      Object, Name of the object the controller belongs to

   :type object: string, (optional, never None)
   :arg direction:

      Direction, Move Up or Down

   :type direction: enum in ['UP', 'DOWN'], (optional)

.. function:: controller_remove(controller="", object="")

   Remove a controller from the active object

   :arg controller:

      Controller, Name of the controller to edit

   :type controller: string, (optional, never None)
   :arg object:

      Object, Name of the object the controller belongs to

   :type object: string, (optional, never None)

.. function:: links_cut(path=None, cursor=9)

   Remove logic brick connections

   :arg path:

      Path

   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg cursor:

      Cursor

   :type cursor: int in [0, inf], (optional)

.. function:: properties()

   Toggle the properties region visibility

.. function:: sensor_add(type='', name="", object="")

   Add a sensor to the active object

   :arg type:

      Type, Type of sensor to add

   :type type: enum in [], (optional)
   :arg name:

      Name, Name of the Sensor to add

   :type name: string, (optional, never None)
   :arg object:

      Object, Name of the Object to add the Sensor to

   :type object: string, (optional, never None)

.. function:: sensor_move(sensor="", object="", direction='UP')

   Move Sensor

   :arg sensor:

      Sensor, Name of the sensor to edit

   :type sensor: string, (optional, never None)
   :arg object:

      Object, Name of the object the sensor belongs to

   :type object: string, (optional, never None)
   :arg direction:

      Direction, Move Up or Down

   :type direction: enum in ['UP', 'DOWN'], (optional)

.. function:: sensor_remove(sensor="", object="")

   Remove a sensor from the active object

   :arg sensor:

      Sensor, Name of the sensor to edit

   :type sensor: string, (optional, never None)
   :arg object:

      Object, Name of the object the sensor belongs to

   :type object: string, (optional, never None)

.. function:: view_all()

   Resize view so you can see all logic bricks


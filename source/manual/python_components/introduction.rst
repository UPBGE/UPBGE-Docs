.. _python_components-introduction:

============
Introduction
============

What Is A Python Component?
---------------------------

.. figure:: /images/Python_Components/Fig-01.png

   Python Component

The idea of a component is a simple one. They are modules that can be attached to game objects. You can attach as many as you want, 
and each one serves a specific purpose such as third person character movement with WASD. After a component has been attached to an object, 
it can have various exposed settings that you can edit. In the case of a third person movement component, this could be things such as 
movement speed and turn speed.

Python component can be compared to python logic bricks with parameters. The python component is a script loaded in the UI, this script defined 
a component class by inheriting from KX_PythonComponent. 
This class must contain a dictionary of properties: **args** and two default functions: **start()** and **update()**.
Additionally, the component can include an optional function: **dispose()**

The script used to create the component must have .py extension. The component properties are loaded from the args attribute from the UI at loading time. 
When the game start the function start() is called with as arguments a dictionary of the properties’ name and value. 
The update() function is called each frame during the logic stage before running logics bricks. The goal of this function is to handle and process everything.

The following component example moves and rotates the object when pressing the keys W, A, S and D.

.. code-block:: python

   import bge
   from collections import OrderedDict

   class ThirdPerson(bge.types.KX_PythonComponent):
      """Basic third person controls

      W: move forward
      A: turn left
      S: move backward
      D: turn right

      """

      args = OrderedDict([
            ("Move Speed", 0.1),
            ("Turn Speed", 0.04)
      ])

      def start(self, args):
         self.move_speed = args['Move Speed']
         self.turn_speed = args['Turn Speed']

      def update(self):
         keyboard = bge.logic.keyboard.events

         move = 0
         rotate = 0

         if keyboard[bge.events.WKEY]:
            move += self.move_speed
         if keyboard[bge.events.SKEY]:
            move -= self.move_speed

         if keyboard[bge.events.AKEY]:
            rotate += self.turn_speed
         if keyboard[bge.events.DKEY]:
            rotate -= self.turn_speed

         self.object.applyMovement((0, move, 0), True)
         self.object.applyRotation((0, 0, rotate), True)


The property types supported are float, integer, boolean, string, set (for enumeration) and Vector 2D, 3D and 4D. 
The following example show all of these property types:

.. code-block:: python
   
   from bge import *
   from mathutils import *
   from collections import OrderedDict

   class Component(types.KX_PythonComponent):
   args = OrderedDict([
         ("Float", 58.6),
         ("Integer", 150),
         ("Boolean", True),
         ("String", "Cube"),
         ("Enum", {"Enum 1", "Enum 2", "Enum 3"}),
         ("Vector 2D", Vector((0.8, 0.7))),
         ("Vector 3D", Vector((0.4, 0.3, 0.1))),
         ("Vector 4D", Vector((0.5, 0.2, 0.9, 0.6)))
   ])

   def start(self, args):
      print(args)

   def update(self):
      pass

The optional **dispose()** function is called when the component is destroyed. It is only necessary in very specific cases.

Inside of UPBGE there are several python component templates that can help us with common tasks. We will analyze them in the next subchapters.

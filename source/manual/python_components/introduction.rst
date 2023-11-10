.. _python_components-introduction:

============
Introduction
============

What Is A Python Component?
---------------------------

The idea of a component is a simple one. They are modules that can be attached to game objects. You can attach as many as you want, 
and each one serves a specific purpose such as third person character movement with :kbd:`WASD` keys. After a component has been attached to an object,
it can have various exposed settings that you can edit. In the case of a third person movement component, this could be things such as 
movement speed and turn speed.

.. figure:: /images/Python_Components/Fig-01.png

   Python Component (Vehicle Wheeled template)
   
Python component can be compared to python logic bricks with parameters. The python component is a script loaded in the UI, this script defined 
a component class by inheriting from KX_PythonComponent. 
This class must contain a dictionary of properties: **args** and two default functions: **start()** and **update()**.
Additionally, the component can include an optional function: **dispose()**

The script used to create the component must have .py extension. The component properties are loaded from the args attribute from the UI at loading time. 
When the game start the function start() is called with as arguments a dictionary of the properties’ name and value. 
The update() function is called each frame during the logic stage before running logics bricks. The goal of this function is to handle and process everything.

The following component example moves and rotates the object when pressing the keys :kbd:`W`, :kbd:`A`, :kbd:`S` and :kbd:`D`.

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


The standard property types supported are float, integer, boolean, string, set (for enumeration) and Vector 2D, 3D and 4D. 
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

Additionally, the following data (ID) property types are supported too:


.. figure:: /images/Python_Components/Fig-20.png
   :align: left
   :width: 90%

   Data (ID) Property Types supported

.. code-block:: python

   import bge, bpy
   from collections import OrderedDict

   class Bootstrap(bge.types.KX_PythonComponent):
      args = OrderedDict((
         ("myAction", bpy.types.Action),
         ("myArmature", bpy.types.Armature),
         ("myCamera", bpy.types.Camera),
         ("myCollection", bpy.types.Collection),
         ("myCurve", bpy.types.Curve),
         ("myImage", bpy.types.Image),
         ("myKey", bpy.types.Key),
         ("myLibrary", bpy.types.Library),
         ("myLight", bpy.types.Light),
         ("myMaterial", bpy.types.Material),
         ("myMesh", bpy.types.Mesh),
         ("myMovieClip", bpy.types.MovieClip),
         ("myNodeTree", bpy.types.NodeTree),
         ("myObject", bpy.types.Object),
         ("myParticle", bpy.types.ParticleSettings),
         ("mySound", bpy.types.Sound),
         ("mySpeaker", bpy.types.Speaker),
         ("myText", bpy.types.Text),
         ("myTexture", bpy.types.Texture),
         ("myVectorFont", bpy.types.VectorFont),
         ("myVolume", bpy.types.Volume),
         ("myWorld", bpy.types.World),
      ))

      def start(self, args: dict):
         self.myObject = None
         if "myObject" in args:
            print("myObject = ", args["myObject"])
            self.myObject = args["myObject"]
         else:
            print("myObject not found!")

      def update(self) -> None:
         if self.myObject:
            print(self.myObject.name)


The optional **dispose()** function is called when the component is destroyed. It is only necessary in very specific cases.

Inside of UPBGE there are several python component templates that can help us with common tasks. We will analyze them in the next subchapters.


Python Component Creation
-------------------------

The Python Component panel, or also called Game Component panel, is placed in the Properties editor under the Game Object Properties tab.

.. figure:: /images/Python_Components/Fig-02.png

   Game Component panel
   
You will find there the 2 ways to make a Python Component in UPBGE, **Add** and **Create**.

.. figure:: /images/Python_Components/Fig-03.png

   The 2 ways to make a Python Component
   
Create Component
++++++++++++++++

When you push over the **Create** button a detachable panel will appear. In that panel you can introduce the component module name and the class name, both separate by a dot.
After entering the name and clicking on the **Create** button, a new python script with the name of the component's module will be created in the script editor.
That python script will contain an empty class which name will be the one entered previously. 

.. figure:: /images/Python_Components/Fig-04.png

   Create Component process

As the component script is developed you can click on the component reload option to see the updated component.

.. figure:: /images/Python_Components/Fig-05.png

   Python Component reload process

Add Component
+++++++++++++

This process is the opposite of the previous one. First of all, we already have a python script previously formatted as a component that can be placed either in the script editor or at the same level as the .blend file.

When we click on the **Add** button we will have to enter the name of the python script (without the .py) followed by a dot and the class name. After accept the Python Component will be created.

.. figure:: /images/Python_Components/Fig-06.png

   Add Component process

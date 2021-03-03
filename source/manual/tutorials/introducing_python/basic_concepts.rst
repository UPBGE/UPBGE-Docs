==============
Basic Concepts
==============

This tutorial will give you a quick introduction about how to use Python within the
Game Engine. Basically, it will enable you to start with Python scripting avoiding
typical errors and wrong paths.

When writing Python code for the UPBGE we recommend to keep the UPBGE Python API
open as reference. You can find it here: `UPBGE Python API <https://upbge.org/api/>`__

-------------------------------------------
If you don't know enough Python to begin...
-------------------------------------------
This tutorial is not a tutorial to teach you Python. If you don't know enough Python
to begin with maybe worth trying to play with Python on the side, at least to cover the basics.

This one essentially looks amazing (make sure to go through the different chapters!)
`https://jakevdp.github.io/WhirlwindTourOfPython/02-basic-python-syntax.html <https://jakevdp.github.io/WhirlwindTourOfPython/02-basic-python-syntax.html>`__

Maybe a lot to read, but at least they explain a bunch of things, you don’t have
to rush... `https://www.techbeamers.com/python-tutorial-step-by-step <https://www.techbeamers.com/python-tutorial-step-by-step/>`__

And we mean, maybe Google explains better than us:
`https://developers.google.com/edu/python/set-up <https://developers.google.com/edu/python/set-up/>`__

Just pick your poison. Take your time to read, really :-).
If you go through with it, you’ll be ready to try your new spells on the UPBGE!

------------------------------
Logic Brick: Python Controller
------------------------------

.. figure:: /images/Tutorials/Introducing_Python/tutorials-introducing-python-01.png

   Controller brick at Logic Brick editor.

A Python controller is basically a logic brick that you can program using Python scripts.

If you look at how a controller usually behaves, they do pretty simple things:

- ``AND`` Controller: When all connected sensors are positive, activate all connected actuators.
- ``OR`` Controller: When one of the connected sensors is positive, activate all connected actuators.
- ``NAND`` Controller: When no connected sensor is positive, activate all connected actuators.
- ``XOR`` Controller: When only one of the connected sensors is positive, activate all, etc.
These are all basic logic gates, but what if you want more control? What if you want to test
if a sensor is positive, and actually check some values from it?

That is when you use a Python controller:

.. figure:: /images/Tutorials/Introducing_Python/tutorials-introducing-python-02.png

   Python controller at Logic Brick editor.

.. note::

   You need at least one sensor connected to the controller in order to trigger it!.
   It can be anything, but the trigger comes from a sensor…

Now to write a script you just open Blender’s text editor, and you can start writing your first script.

So, little bit of disclaimer: When people see programs they usually go “that’s so hacker, it is too complex”.
But fear not: Programs are meant to be written using English words, a bit like a recipe! It is a simple
list of instructions to get from a state A to a state B.

.. code-block:: python

   import bge # the module to interact with the Blender Game Engine

   # When this script gets executed by a controller (when it will be its turn)
   # the following variable will point to the current running controller.
   # The BGE executes each controller one after the other, but boy is it fast.
   controller = bge.logic.getCurrentController()

   # Controller "objects" (in Python) have a property named ".owner" that
   # refers to the object owning the currently running controller.
   # This is because this script can be shared by different Python controllers
   # attached to other objects. Since we will run multiple times in a different context,
   # this line allows us to figure out what object is currently running the controller!
   owner = controller.owner

   # In this example, let's do something silly, and move the cube up
   owner.worldPosition.z += 0.1

   # Let's make it turn too
   owner.applyRotation([0, 0, 0.1]) # [x, y, z]

Lot of comments in this code, but if you read the code word by word, usually it is pretty easy
to understand what is going to happen once the Python controller will execute it!

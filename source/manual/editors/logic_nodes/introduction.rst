.. _lne-introduction:

==============================
Introduction
==============================

Logic Node Add-On
++++++++++++++++++++++++++++++

Logic Node add-on adds a large variety of logic nodes to the UPBGE game engine, enabling easy visual game development, just like in the Unreal Engine or Armory3D.

Why use logic nodes when there's logic bricks
---------------------------------------------

Basically, there's two ways to get logic into your game.

-  Logic bricks, and
-  Python scripts.

Using nodes is effectively scripting in python, only visually. They have the advantage of being a lot more versatile than logic bricks. Nodes can be placed freely, trees can be nested and eventually, the code contained by each node will be accessible.

Things to consider
------------------------------

Logic bricks are fastest

   This is because they are using Blenders native C++ API, which makes them simply creepy fast. Second fastest is custom :py:`python code`, and logic nodes are the slowest.

Only execute code when needed

   You always want to avoid the :ln:`On Update` node, which basically executes every frame. Only use this when necessary, otherwise try to get some kind of ``condition``. Logic trees can also be linked to every ``sensor`` the logic bricks can offer, make good use of that.

The main loop
------------------------------

Main loop is most basic calculation the engine has to go through effectively 60 times a second, keep that in mind. In that loop, every sensor logic brick on every object is checked for its status (whether it is active or not), which is incredibly fast.

If any sensor is active, the linked controller will be executed. A controller can be either a logic gate, in which case it fires up the linked actuators, or it can be python controller, in which case the referenced python code is evaluated.

This is where you need to be *careful* what you do. You don't want to run *a lot of unnecessary code* each frame, so put in breaking conditions as often as you can to avoid overhead in the main loop.

How does it work
------------------------------

Under the hood, each logic node includes some lines of python code. That code is executed when the condition for the node is met. If a node has no condition, it is executed each time the sensor logic brick connected to it is active.

When pressing :menuselection:``Apply To Selected`` (or :menuselection:``Force Compile``) in the logic node tree editor, a .py file is generated. The file defines a reference class for each node in a particular order so that every node is executed only when all values needed for it are computed.

Then, whenever the connected sensor is active, the :py:``evaluate()`` function for each node is called. This is where the magic happens. This function collects all the input values from its sockets before waltzing though the lines of code that make something happen in-game.

.. seealso::
   For general *nodes* overview see Blender's `nodes chapter <https://docs.blender.org/manual/en/latest/interface/controls/nodes/index.html>`__. 

Basic Node Types
++++++++++++++++++++++++++++++

There are 3 basic logic node types:

Condition Nodes
------------------------------

These nodes are either conditions themselves (like ``sensors``) or they can act as logic gates.

Parameter Nodes
------------------------------

Most parameter nodes do not need a condition to perform. They are pre-defined calculations or data fetchers.

Action Nodes
------------------------------

These are the nodes that manipulate, generate or remove something in the game. From moving objects to writing save files, these nodes perform a certain action.

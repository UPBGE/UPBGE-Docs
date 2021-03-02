.. _bpy.types.SpaceLogicEditor:

*******************
Logic Bricks Editor
*******************

The Logic Bricks Editor provides the main method of setting up and
editing the game logic for the various actors (i.e. objects) that make up the game.
The logic for the objects which are currently selected in the associated 3D View are displayed as logic bricks,
which are shown as a table with three columns, showing sensors, controllers, and actuators, respectively.
The links joining the logic bricks conduct the pulses between sensor-controller and controller-actuator.

To give you a better understanding of the Logic Bricks Editor, the image below shows a typical
editor content in which the major components have been labeled.
We will look at each one individually.

.. figure:: /images/Editors/editors-logic_editor-logic_editor.png

   The different parts of the Logic Editor.

   1) Property Region, 2) Object Name, 3a) Links, 3b) Link socket,
   4) Sensor column, 5) Controller Column, 6) Actuator Column, 7) Python Components Region.

=========
Main View
=========

Object Name
   This toggle shows the name of the object which owns the logic bricks below.
Links
   Links (3A) indicate the direction of logical flow between objects.
   Link lines are drawn by :kbd:`LMB` dragging from one Link socket (3B) to another.
   Links can be drawn from Sensors to Controllers, or from Controllers to Actuators.
   If you try to link directly a Sensor with an Actuator a new Controller will appear
   between both. Actuators cannot be linked back to Sensors
   (however, special actuator and sensor types are available to provide these connections).

   Sending nodes (the chain link found on the right-hand side of Sensors and Controllers)
   can send to multiple Reception nodes
   (the chain link found on the left-hand side of Controllers and Actuators).
   Reception nodes can likewise receive multiple links.

   Links can be created between logic bricks belonging to different objects.
   To delete a link between two nodes, :kbd:`CTRL-RMB` drag between the two nodes.

-------------
Sensor Column
-------------

This column contains a list of all sensors owned by the active object (and any other selected objects).
New sensors for the active object are created using the "Add Sensor" button.
For a more in-depth look at the content, layout and available operations in this area,
see :doc:`Sensors <manual/logic/sensors/introduction>`.

-----------------
Controller Column
-----------------

This column contains a list of all controllers owned by the active object (and any other selected objects).
New controllers for the active object are created using the "Add Controller" button,
together with the creation of states for the active object.
For a more in-depth look at the content, layout, and available operations in this area,
see :doc:`Controllers <manual/logic/controllers/introduction>`.

---------------
Actuator Column
---------------

This column contains a list of all actuators owned by the active object (and any other selected objects).
New actuators for the active object are created using the "Add Actuator" button.
For a more in-depth look at the content, layout, and available operations in this area,
see :doc:`Actuators <manual/logic/actuators/introduction>`.

===============
Property Region
===============

Game properties are like variables in other programming languages.
They are used to save and access data associated with an object.
Several types of properties are available.
Properties are declared by clicking the *Add Game Property* button in this region.
For a more in-depth look at the content,
layout and available operations in this region, see :doc:`Properties <manual/logic/properties>`.


========================
Python Components Region
========================

This region is where the *Python Components* are placed. *Python Components* are an independently
logic system from Logic Bricks system. They are modules that can be attached to game objects.
For a more in-depth look at the content,
layout and available operations in this region, see :doc:`Python Components <manual/python_components/introduction>`.

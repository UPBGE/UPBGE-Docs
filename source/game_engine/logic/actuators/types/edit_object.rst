.. _bpy.types.EditObjectActuator:

********************
Edit Object Actuator
********************

The *Edit Object Actuator* allows the user to edit settings of objects in-game.
In example edits the object's mesh, adds objects, or destroys them.
It can also change the mesh of an object (and soon also recreate the collision mesh).


Properties
==========

Edit Object
   How the object is modified, each is described below.


Dynamics
--------

Provides a menu of *Dynamic Operations* to set up dynamics options for object.

.. figure:: /images/game-engine_logic_actuators_types_edit-object_dynamics.png
   :width: 271px

   Edit Object: Dynamics.

Set Mass
   Enables the user to set the mass of the current object for Physics.
Disable Rigid Body
   Disables the Rigid Body state of the object -- disables collision.
Enable Rigid Body
   Disables the Rigid Body state of the object -- enables collision.
Suspend Dynamics
   Suspends the object dynamics (object velocity).
Restore Dynamics
   Resumes the object dynamics (object velocity).


Track To
--------

Makes the object "look at" another object, in 2D or 3D.
The Y axis is considered the front of the object.

.. figure:: /images/game-engine_logic_actuators_types_edit-object_track-to.jpg
   :width: 271px

   Edit Object: Track To.

Object
   Object to follow.
Time
   Number of frames it will take to turn towards the target object.
3D Button (toggle).
   Enable 2D (X, Y) or 3D (X, Y, Z) tracking.


Replace Mesh
------------

Replace mesh with another. Both the mesh and/or its physics can be replaced,
together or independently.

.. figure:: /images/game-engine_logic_actuators_types_edit-object_replace-mesh.jpg
   :width: 271px

   Edit Object: Replace Mesh.

Mesh
   Name of mesh to replace the current mesh.
Gfx Button
   Replace visible mesh.
Phys Button
   Replace physics mesh (not compound shapes).


End Object
----------

Destroy the current object (note, debug properties will display error Zombie Object in console).

.. figure:: /images/game-engine_logic_actuators_types_edit-object_end-object.png
   :width: 271px

   Edit Object: End Object.


Add Object
----------

Adds an object at the center of the current object.
The object that is added needs to be on another, hidden, layer.

.. figure:: /images/game-engine_logic_actuators_types_edit-object_add-object.png
   :width: 271px

   Edit Object: Add Object.

Object
   The name of the object that is going to be added.
Time
   The time (in frames) the object stays alive before it disappears.
   Zero makes it stay forever.
Linear Velocity
   Linear Velocity, works like in the motion actuator but on the created object instead of the object itself.
   Useful for shooting objects, create them with an initial speed.
Angular Velocity
   Angular velocity, works like in the motion actuator but on the created object instead of the object itself.

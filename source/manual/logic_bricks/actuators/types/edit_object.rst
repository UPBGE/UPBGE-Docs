.. _bpy.types.EditObjectActuator:

==============================
Edit Object Actuator
==============================

.. seealso::
   See the Python reference of this logic brick in :class:`SCA_AddObjectActuator`, :class:`SCA_DynamicActuator`, :class:`SCA_EndObjectActuator` and :class:`SCA_ReplaceMeshActuator`.

The *Edit Object Actuator* allows the user to edit settings of objects in-game. In example edits the object's mesh, adds objects, or destroys them. It can also change the mesh of an object.

.. figure:: /images/logic_bricks/actuators/logic-actuators-types-edit_object-edit_object.png

   Edit Object Actuator

Properties
++++++++++++++++++++++++++++++

Edit Object
   How the object is modified, each is described below.

Dynamics
------------------------------

Provides a menu of *Dynamic Operations* to set up dynamics options for object.

.. figure:: /images/logic_bricks/actuators/logic-actuators-types-edit_object-dynamics.png

   Edit Object: Dynamics

Set Mass
   Enables the user to set the mass of the current object for Physics.
Disable Rigid Body
   Disables the Rigid Body state of the object, it then behaves like a Dynamic object (no rotation).
Enable Rigid Body
   Enables the Rigid Body state of the object (enables rotation).
Suspend Dynamics
   Suspends the object dynamics (object velocity).
Restore Dynamics
   Resumes the object dynamics (object velocity).
Suspend Physics
   Suspends the object physics (disables object velocity and collision).
Restore Physics
   Resumes the object physics (enables object velocity and collision).

Track To
------------------------------

Makes the object "look at" another object, in 2D or 3D. The Y axis is considered the front of the object.

.. figure:: /images/logic_bricks/actuators/logic-actuators-types-edit_object-track_to.png

   Edit Object: Track To

Object
   Object to follow.
Time
   Number of frames it will take to turn towards the target object.
3D Button (toggle).
   Enable 2D (X, Y) or 3D (X, Y, Z) tracking.
Up Axis
   Selects the axis that should point up.
Track Axis
   Selects the axis that should point to the target object.

Replace Mesh
------------------------------

Replace mesh with another. Both the mesh and/or its physics can be replaced, together or independently.

.. figure:: /images/logic_bricks/actuators/logic-actuators-types-edit_object-replace_mesh.png

   Edit Object: Replace Mesh

Mesh
   Name of mesh to replace the current mesh.
Gfx Button
   Replace visible mesh.
Phys Button
   Replace physics mesh (not compound shapes).

End Object
------------------------------

Destroy the current object (note, debug properties will display error Zombie Object in console).

.. figure:: /images/logic_bricks/actuators/logic-actuators-types-edit_object-end_object.png

   Edit Object: End Object

Add Object
------------------------------

Adds an object at the center of the current object. The object that is added needs to be on another, hidden, layer.

.. figure:: /images/logic_bricks/actuators/logic-actuators-types-edit_object-add_object.png

   Edit Object: Add Object

Object
   The name of the object that is going to be added.
Time
   The time (in frames) the object stays alive before it disappears. Zero makes it stay forever.
Linear Velocity
   Linear Velocity, works like in the motion actuator but on the created object instead of the object itself. Useful for shooting objects, create them with an initial speed.
Angular Velocity
   Angular velocity, works like in the motion actuator but on the created object instead of the object itself.

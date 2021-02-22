.. _bpy.types.CollectionActuator:

*******************
Collection Actuator
*******************

.. seealso::
   See the Python reference of this logic brick in :class:`SCA_CollectionActuator`.

The *Collection Actuator* manages the what the user can see through their view. This can be a inventory, ammunition and other UI.

.. figure:: /images/Logic/Actuators/logic-actuators-types-collection-collection.png

    Collection Actuator.

Properties
==========

Collection
   Select which collection you want to manipulate.

Logic
   Resume/suspend sensors in the selected collection. 

Physics
   Resume/suspend physics in the selected collections objects. 

Visibility 
   Resume/suspend visibility of the selected collections objects.

Suspend Collection
------------------

Suspends the view of the collection.

.. figure:: /images/Logic/Actuators/logic-actuators-types-collection-suspend_collection.png

   Suspend Collection.

Resume Collection
-----------------

Resumes the view of the collection.

.. figure:: /images/Logic/Actuators/logic-actuators-types-collection-resume_collection.png

   Resume Collection.

Add Overlay Collection
----------------------

Adds a new overlay collection.

.. figure:: /images/Logic/Actuators/logic-actuators-types-collection-add_overlay_collection.png

   Add Overlay Collection.

Remove Overlay Collection
-------------------------

Removes the overlay collection.

.. figure:: /images/Logic/Actuators/logic-actuators-types-collection-remove_overlay_collection.png

   Remove Overlay Collection.

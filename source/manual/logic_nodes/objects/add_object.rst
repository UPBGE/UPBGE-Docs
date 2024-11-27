.. figure:: /images/logic_nodes/objects/ln-add_object.png
   :align: right
   :width: 215
   :alt: Add Object Node

.. _ln-add_object:

==============================
Add Object
==============================

Add a copy of an object into the current scene.

Inputs
++++++++++++++++++++++++++++++

Condition
   Which condition will be used for node to activate.

Object to Add
   Object Data Block to add into the scene.

Copy Data From
   Copy the transform data from this object (optional).

Life
   Total amount of frames after which the object is removed.

Full Copy
   Duplicate the data used by the spawned object. This will duplicate any material, action etc. used by this Data Block.
   
Outputs
++++++++++++++++++++++++++++++

Done 
    *True* if the node performed successfully, else *False*.

Added Object
   Spawned instance of the object.

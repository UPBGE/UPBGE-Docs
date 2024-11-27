.. figure:: /images/logic_nodes/physics/ln-collision.png
   :align: right
   :width: 215
   :alt: Collision Node

.. _ln-collision:

==============================
Collision
==============================

Detect and react to collisions involving a given object.

Parameters
++++++++++++++++++++++++++++++

Continuous
   Monitor for continuous collision, not just initial one.

Inputs
++++++++++++++++++++++++++++++

Object
   The monitored object.

Use Material
   If enabled, changes the "Property" socket to a "Material" one.

Property
   If set, only detect collisions with objects that have this property.

Material
   If set, only detect collisions with objects that have this material applied.

Outputs
++++++++++++++++++++++++++++++

On Collision
   `True` if a collision has occured according to the "Continuous" property, else `False`.
   
Colliding Object
   The object with which the monitored object is colliding with.

Colliding Objects
   A list of objects with which the monitored object is colliding with.

Point
   The point in world space where the collision has occured.

Normal
   The normal of the face on which the collision has occured.

.. figure:: /images/logic_nodes/raycasts/ln-camera_ray.png
   :align: right
   :width: 215
   :alt: Camera Ray Node

.. _ln-camera_ray:

==============================
Camera Ray
==============================

Cast a ray from the camera in the direction of coordinates on the screen.

Inputs
++++++++++++++++++++++++++++++

Condition
   Which condition will be used for node to activate.

Aim
   Screen coordinates at which to cast the ray.

Property
   Which property to use.

X-Ray
   Ignore objects that don't have the given property.

Distance
   Maximum reach of the ray.
   
Mask
   Bitmask to use.

Outputs
++++++++++++++++++++++++++++++

Has Result
   `True` if the ray has hit a target, else `False`

Picked Object
   The object the ray has hit, or `None`

Picked Point
   The world point the ray has hit, or `None`

Picked Normal
   The normal of the face the ray has hit, or `None`


*************************
Bullet physics Python API
*************************

Bullet Physics provides collision detection and rigid body dynamics for the Blender Game Engine.
It takes some settings from Blender that previously were designed for the former
collision detection system (called Sumo).

However, new features do not have a user interface yet,
so Python can be used to fill the gap for now.

Features:

- Vehicle simulation.
- Rigid body constraints: hinge and point to point (ball socket).
- Access to internal physics settings, like deactivation time, debugging features.

Easiest is to look at the Bullet physics demos, how to use them. More information can be found
`here <http://www.continuousphysics.com/Bullet/phpBB2/viewforum.php?f=17>`__.

Python script example::

   import PhysicsConstraints
   print dir(PhysicsConstraints)

.. note:: Parameter Settings

   Since this API is not well documented, it can be unclear what kind of values to use for setting parameters.
   In general, damping settings should be in the range of 0 to 1 and
   stiffness settings should not be much higher than about 10.

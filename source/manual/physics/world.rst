
==============================
World Physics
==============================

.. figure:: /images/game_engine-physics-world_panel.png
   :align: right
   :width: 290px

   World Physics panel

Physics Panel
++++++++++++++++++++++++++++++

The *Game Physics* located in the *World* panel determine the type of physical rules that govern the Game Engine scene, and the gravity value to be used. Based on the physics engine selected, in physics simulations in the Game Engine, Blender will automatically move *Actors* in the downward (-Z) direction. After you arrange the actors and they move as you wish, you can then bake this computed motion into keyframes (see :ref:`game-engine-physics-bake-keyframes` for more info).

Physics Engine
   Set the type of physics engine to use.

   Bullet
      The default physics engine, in active development. It handles movement and collision detection. The things that collide transfer momentum to the collided object.
   None
      No physics in use. Things are not affected by gravity and can fly about in a virtual space. Objects in motion stay in that motion.
Gravity
   The gravitational acceleration, m.s\ :sup:`-2` (in units of meters per squared second), of this world. Each object that is an actor has a mass and size slider. In conjunction with the frame rate, Blender uses this info to calculate how fast the object should accelerate downward.
Culling Resolution
   The size of the occlusion culling buffer in pixel, use higher value for better precision (slower). The optimized Bullet DBVT for view frustum and occlusion culling is activated internally by default.
Physics Steps
   Max
      Sets the maximum number of physics steps per game frame if graphics slow down the game. higher value allows physics to keep up with real-time.
   Substeps
      Sets the number of simulation sub-steps per physics time step. Higher value give better physics precision.
   FPS
      Set the nominal number of game frames per second. Physics fixed timestep = 1/fps, independently of actual frame rate.
Logic Steps
   Sets the maximum number of logic frame per game frame if graphics slows down the game, higher value allows better synchronization with physics.
Physics Deactivation
   These settings control the threshold at which physics is deactivated. These settings help reducing the processing spent on Physics simulation during the game.

   Linear Threshold
      The speed limit under which a rigid body will go to sleep (stop moving) if it stays below the limits for a time equal or longer than the deactivation time (sleeping is disabled when deactivation time is set to 0).
   Angular Threshold
      Same as linear threshold, but for rotation limit (in rad/s)
   Time
      The amount of time in which the object must have motion below the thresholds for physics to be disabled (0.0 disables physics deactivation).

Navigation Mesh
++++++++++++++++++++++++++++++

Rasterization
   Cell size
      Rasterized cell size.
   Cell height
      Rasterized cell height.
Agent
   Height
      Minimum height where the agent can still walk.
   Radius
      Radius of the agent.
   Max climb
      Maximum height between grid cells the agent can climb.
   Max slope
      Maximum walkable slope angle in degrees.
Region
   Min Region Size
      Minimum regions size. Smaller regions will be deleted.
   Merged Region Size
      Minimum regions size. Smaller regions will be merged.
Partitioning
   Watershed
      Classic Recast partitioning method generating the nicest tessellation.
   Monotone
      The fastest navmesh generation method, but may cause long thin polygons.
   Layers
      A reasonably fast method that produces better triangles than monotone partitioning.
Polygonization
   Max Edge Length
      Maximum contour edge length.
   Max Edge Error
      Maximum distance error from contour to cells.
   Vertices Per Poly
      Max number of vertices per polygon.
Detail Mesh
   Sample Distance
      Detail mesh sample spacing.
   Max Sample Error
      Detail mesh simplification max sample error.

Obstacle Simulation
++++++++++++++++++++++++++++++

Simulation used for obstacle avoidance in the Game Engine, based on the RVO (Reciprocal Velocity Obstacles) principle. The aim is to prevent one or more actors colliding with obstacles.

See `Pathfinding and steering behaviors <https://wiki.blender.org/index.php/User:Nicks/Gsoc2010/Docs>`__ for more details.

Type
   None
      Obstacle simulation is disabled, actors are not able to avoid obstacles.
   RVO (cells)
      Obstacle simulation is based on the `RVO method <http://gamma.cs.unc.edu/RVO/>`__ with cell sampling.
   RVO (rays)
      Obstacle simulation is based on the `RVO method <http://gamma.cs.unc.edu/RVO>`__ with ray sampling.

Level height
   Max difference in heights of obstacles to enable their interaction. Used to define minimum margin between obstacles by height, when they are treated as those which are situated one above the other i.e. they does not influence to each other.
Visualization
   Enable debug visualization for obstacle simulation.

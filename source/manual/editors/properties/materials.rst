
**************
Materials
**************

Game Settings
=============

.. figure:: /images/game-engine_materials_panel.png

   Game Settings panel.

This panel contains properties that control how the object surfaces
that use the material are rendered in real-time by the Blender Game Engine.

Backface Cull
   Hide the back-faces of objects rendered with this material.
   If "Off", both sides of the surface are visible (at the expense of lower rendering speed).
   Note that this setting is applied per material and not per face; e.g.
   if the material is applied to a cube, only the back and front faces of the cube are visible,
   and not both sides of each face.

Invisible
   Hide all faces of objects rendered with this material.

Text
   Use material as Text object in the Game Engine.

Alpha Blend
   Controls how the alpha channel is used to create a transparent texture in the rendered image.

   Alpha Sort
      Orders the sequence in which transparent objects are drawn on top of each other,
      so that ones in front receive more light than ones behind.
   Alpha Blend
      Uses the alpha values present in the bitmap image sourced in the Image slot.
   Alpha Clip
      Uses the alpha channel as a simple mask.
   Add
      Render face transparent and add color of face.
   Opaque (default)
      All alpha values are ignored; the scene is completely non-transparent.


Face Orientation
================

Provides options regarding the orientation (i.e. rotation transformation)
of faces to which the material is applied.

   Shadow
      Faces are used for shadow.
   Billboard
      Billboard with Z-axis constraint.
   Halo
      Screen-aligned billboard.
   Normal (default)
      No transformation.


Material Physics
================

.. figure:: /images/game-engine_materials_physics-panel.png

   Panel Physics in Material context.

This panel contains physical properties that control how the object surfaces
that use the material are rendered in real-time by the Blender Game Engine.

Physics settings are visible when using the Game Engine for rendering,
and handled by the :doc:`Game Engine's physics engine </manual/editors/properties/physics>`.

Friction
   Coulomb friction coefficient when inside the physics distance area.

Elasticity
   The elasticity of collisions determines how much of the kinetic
   energy is retained after the collision.
   A value of 1 will result in a collision where objects bounce off each other,
   and the kinetic energy after the collision is the same as before.
   A value of 0 will result in a collision where the objects stick together after the collision,
   as all energy will have been converted to heat
   (or other energy forms that Blender also does not model).

   In macroscopic nature (so bigger than atomic particles)
   an elasticity of 1 is never seen, as at least some energy is converted
   to heat, sound, etc. An elastic (elasticity=high) collision occurs
   when two metal balls collide. An inelastic (elasticity=low)
   collision is seen when two half-inflated beach balls collide.

Force Field
   Controls force field settings.

   Force
      Upward spring force when inside the physics distance area.
   Distance
      Distance of physics area.
   Damping
      Damping of the spring force when inside the physics distance area.
   Align to Normal
      Align dynamic game objects along the surface normal when inside the physics distance area.

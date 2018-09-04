
*******************
Compatibility Notes
*******************

UPBGE VS Blender
================

UPBGE is fully integrated into Blender environment, but it doesn't mean it supports 
all the features that Blender provides. Here's some compatibility info about various 
features present in Blender relative to UPBGE.

.. _compatibility-supported-objects:

.. rubric:: Object types supported

- Mesh
- Text
- Armature
- Empty
- Camera
- Lamp

.. note:: Any other object type (like Curve, Speaker, Force Field, etc) will not be rendered into game. Curves may be converted to Meshes though.

.. _compatibility-supported-datablocks:

.. rubric:: Data-blocks supported

- Cameras
- Scenes
- Objects
- Materials
- Meshes
- Lamps
- Libraries
- Images
- Textures (only Images, procedural Textures not supported)
- Worlds
- Groups
- Shape Keys (along with Actions, otherwise unused)
- Texts (partially)
- Sounds
- Armatures
- Actions

.. note:: Any other data-block type (like Line Styles, Particles, Brushes, etc) have no use or will not be rendered into game.

.. note:: Text objects only work partially, with advanced formatting features currently not being supported.

UPBGE VS BGE
================

BGE also have some incompatibilities with UPBGE. UPBGE can load and execute games made 
in BGE, but a game made in UPBGE can't be executed in BGE, resulting in several 
issues like:

- Logic can't run most of the times.
- Materials get messed up.
- Sometimes physics properties get messed up.

Along with this compatibility with BGE, UPBGE comes with features not supported by 
BGE, like Modifiers applied automatically at game start (instead of discarded, as in BGE).
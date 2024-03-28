.. _intro-compatibility_notes:
   
==============================
Compatibility Notes
==============================

UPBGE VS Blender
++++++++++++++++++++++++++++++

UPBGE is fully integrated into Blender environment, but it doesn't mean it supports all the features that Blender provides. Here's some compatibility info about various features present in Blender relative to UPBGE.

.. _object_types_supported:

.. rubric:: Object types supported

-  Armature
-  Camera
-  Collection
-  Empty
-  Light
-  Mesh
-  Object
-  Text

.. important::
   Any other object type (like Curve, Speaker, Force Field, etc) will not be rendered into game. A Curve Object can be converted to Mesh though.

.. _data_blocks_supported:

.. rubric:: Data-blocks supported

-  Action
-  Armature
-  Camera
-  Collection
-  Image
-  Light
-  Library
-  Material
-  Mesh
-  Object
-  Scene
-  Shapekey (with Action, otherwise unused)
-  Sound
-  Text
-  Texture
-  World
-  Particle (partially supported)

.. important::
   Any other data-block type (like Line Styles, Brushes, etc) have no use or will not be rendered into game.

UPBGE VS BGE
==============================

BGE also have some incompatibilities with UPBGE. UPBGE can partially load and execute games made in BGE, but a game made in UPBGE can't be executed in BGE, resulting in several issues like:

-  Logic can't run most of the times.

-  Materials get messed up.

-  UPBGE do not support Multitexture material mode anymore. Set to GLSL when in vanilla BGE.

-  Sometimes physics simulation get messed up.

Along with this compatibility with BGE, UPBGE comes with features not supported by BGE, like Modifiers applied automatically at game start (instead of discarded, as in BGE).

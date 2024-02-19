.. _intro-compatibility_notes:
   
==============================
Compatibility Notes
==============================

UPBGE VS Blender
++++++++++++++++++++++++++++++

UPBGE is fully integrated into Blender environment, but it doesn't mean it supports all the features that Blender provides. Here's some compatibility info about various features present in Blender relative to UPBGE.

.. _object_types_supported:

.. rubric:: Object types supported

- :ref:`datablock-armature`
- :ref:`datablock-camera`
- :ref:`datablock-collection`
- :ref:`datablock-empty`
- :ref:`datablock-light`
- :ref:`datablock-mesh`
- :ref:`datablock-object`
- :ref:`datablock-text`

.. important:: Any other object type (like Curve, Speaker, Force Field, etc) will not be rendered into game. A Curve Object can be converted to :ref:`datablock-mesh` though.

.. _data_blocks_supported:

.. rubric:: Data-blocks supported

- :ref:`datablock-action`
- :ref:`datablock-armature`
- :ref:`datablock-camera`
- :ref:`datablock-collection`
- :ref:`datablock-image`
- :ref:`datablock-light`
- :ref:`datablock-library`
- :ref:`datablock-material`
- :ref:`datablock-mesh`
- :ref:`datablock-object`
- :ref:`datablock-scene`
- Shapekey (along with :ref:`datablock-action`, otherwise unused)
- :ref:`datablock-sound`
- :ref:`datablock-text`
- :ref:`datablock-texture`
- :ref:`datablock-world`
- Particle (partially supported)

.. important:: Any other data-block type (like Line Styles, Brushes, etc) have no use or will not be rendered into game.

UPBGE VS BGE
==============================

BGE also have some incompatibilities with UPBGE. UPBGE can partially load and execute games made in BGE, but a game made in UPBGE can't be executed in BGE, resulting in several issues like:

- Logic can't run most of the times.
- Materials get messed up.
- UPBGE do not support Multitexture material mode anymore. Set to GLSL when in vanilla BGE.
- Sometimes physics simulation get messed up.

Along with this compatibility with BGE, UPBGE comes with features not supported by BGE, like Modifiers applied automatically at game start (instead of discarded, as in BGE).

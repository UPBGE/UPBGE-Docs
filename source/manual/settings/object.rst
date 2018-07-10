
***************
Object Settings
***************

.. _bpy.types.LodLevel:

Level of Detail
===============

When creating visual assets it is often desirable to have a high amount of detail in the asset
for up close viewing. However,
this high amount of detail is wasted if the object is viewed from a distance,
and brings down the scene's performance. To solve this,
the asset can be swapped out at certain viewing distances.
This is commonly referred to as a level of detail system.
Each visual step of the asset is known as a level of detail. Levels of detail are most
appropriate to use when you have a large scene where certain objects can be viewed both up
close and from a distance.


Settings
--------

.. note:: Modifiers on Level of Detail Objects

   Any level of detail objects that have a modifier do not display correctly in the Game Engine.
   You will need to apply any modifiers for level of detail objects to appear correctly.
   A fix for this is being looked into.

.. figure:: /images/game-engine_settings_object_level-of-detail-panel.png

Level of detail settings can be found in the Object settings when the renderer is set to
Blender Game.
In the Levels of Detail panel is a button to add a new level of detail to the current object.
The settings for each level of detail are displayed in its own box.
The exception to this is the base level of detail.
This is automatically setup as the current object with a distance setting of 0.
To remove a level of detail,
click on the X button in the top right corner of the box of the level to be removed.

Object
   The object to use for this level of detail.
Distance
   The distance at which this level of detail becomes visible.
Use Mesh
   When this option is enabled,
   the mesh from the level of detail object is used until a lower level of detail overrides it.
Use Material
   When this option is enabled,
   the material from the level of detail object is used until a lower level of detail overrides it.


Tools
-----

Some tools for making levels of detail easier to manage and create can be found from
the select menu next to the add button in the Levels of Detail panel.


Set By Name
^^^^^^^^^^^

Searches the scene for specifically named objects and attempts to set them up as levels of
detail on the currently selected object. The selected object must be the base level of detail
(e.g. LOD0). This can be useful to quickly setup levels of detail on imported assets.
In order to make use of this tool, your naming must be consistent, and each level must be
prefixed or suffixed with "lodx" where x is the level that object is intended for.
The case on "lod" must be consistent across all objects.
Below are some example names that the tool will recognize.

- LOD0_Box, LOD1_Box, LOD2_Box
- Box.lod0, Box.lod1, Box.lod2
- LoD0box, LoD1box, LoD2box


Generate
^^^^^^^^

.. figure:: /images/game-engine_settings_object_level-of-detail-generation.png

This tool generates and sets up levels of details based on the selected object.
Generation is done using the Decimate Modifier.
Generation does not apply the modifier to allow further changing the settings.
Generated objects are automatically named based on the level they are generated for.
Below are some settings for the operator.

Count
   The number of levels desired after generation. This operator creates Count-1 new objects.
Target Size
   The ratio setting for the Decimate Modifier on the last level of detail.
   The ratio settings for the other levels are determined by linear interpolation.
Package into Group
   With this setting enabled the operator performs some extra tasks
   to make the asset ready for easy linking into a new file.
   The base object and all of its levels of detail are placed into a group based on the base object's name.
   Levels other than the base are hidden for both the viewport and rendering.
   This simplifies the appearance of the system and does not affect the appearance of the base object.
   Finally, all levels are parented to the base object to remove clutter from the Outliner.


Clear All
^^^^^^^^^

Clears the level of detail settings from the current object.

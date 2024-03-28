.. _dbl-data_blocks-index:

==============================
Data-Blocks
==============================

This page is based on Blender Manual `Data-blocks <https://docs.blender.org/manual/en/latest/files/data_blocks.html>`__. Please see the link for additional details.

----

The base unit for any Blender project is the data-block. Examples of data-blocks include *mesh*, *object*, *material*, *texture*, *node tree*, *scene*, *text*, *brush*, and even *workspaces*.

.. figure:: /images/datablocks/dbl-outliner-blender_file_mode.png
   :figwidth: 35%
   :align: right

   Blender File mode in Outliner

A data-block is a generic abstraction of very different kinds of data, which features a common set of basic features, properties and behaviors.

Some common characteristics:

- They are the primary contents of the blend-file.
- They can reference each other, for reuse and instancing (child/parent, object/object-data, materials/images, in modifiers or constraints too ...).
- Their names are unique within a blend-file, for a given type.
- They can be added/removed/edited/duplicated.
- They can be linked between files (only enabled for a limited set of data-blocks).
- They can have their own animation data.
- They can have custom properties.

User will typically interact with the higher level data types (objects, meshes etc.). When doing more complex projects, managing data-blocks becomes more important, especially when inter-linking blend-files. The main editor for that is the :ref:`gs-outliner_editor`.

.. figure:: /images/datablocks/dbl-types-icons.png
   :figwidth: 35%
   :align: right

   Data-block types with their icons

Not all data in Blender is a data-block; i.e. bones, sequence strips or vertex groups are not - they belong to armature, scene and mesh types respectively.

.. _dbl-data_block_types:

Data-Block Types
++++++++++++++++++++++++++++++

For reference, here is a table of data-block types stored in blend-files.

Link
   Library Linking, supports being linked into other blend-files.
Pack
   File Packing, supports file contents being packed into the blend-file (**not** applicable for most data-blocks which have no file reference).

.. container:: lead

   .. clear

.. |tick|  unicode:: U+2713
.. |cross| unicode:: U+2717
.. |none|  unicode:: U+2014

A table-representation of data-blocks supported in UPBGE.

.. tip::
   :kbd:`Shift-scroll` over the table if text is cut/hidden.

Object-related Datablocks
------------------------------

.. list-table::
   :header-rows: 1
   :class: valign
   :widths: 18 4 4 40

   * - Type
     - Link
     - Pack
     - Description
   * - Armature
     - |tick|
     - |none|
     - Skeleton used to deform meshes; used as data of armature objects, and by the Armature Modifier
   * - Camera
     - |tick|
     - |none|
     - Used as data by camera objects
   * - Collection
     - |tick|
     - |none|
     - Group and organize objects in scenes; used to instance objects, and in library linking
   * - Empty
     - |none| 
     - |none| 
     - 
   * - Light
     - |tick|
     - |none|
     - Used as object data by light objects
   * - Mesh
     - |tick|
     - |none|
     - Geometry made of vertices/edges/faces; used as data of mesh objects
   * - Object
     - |tick|
     - |none|
     - An entity in the scene with location, scale, rotation; used by scenes & collections
   * - Text
     - |tick|
     - |cross|
     - Text data; used by Python scripts and OSL shaders

File-related Datablocks
------------------------------

.. list-table::
   :header-rows: 1
   :class: valign
   :widths: 18 4 4 40

   * - Type
     - Link
     - Pack
     - Description
   * - Image
     - |tick|
     - |tick|
     - Image files; used by shader nodes and textures
   * - Library
     - |cross|
     - |tick|
     - References to an external blend-file; access from the Outliner's *Blender File* view
   * - Sounds
     - |tick|
     - |tick|
     - Reference to sound files; used as data of speaker objects

Other Datablocks
------------------------------

.. list-table::
   :header-rows: 1
   :class: valign
   :widths: 18 4 4 40

   * - Type
     - Link
     - Pack
     - Description
   * - Action
     - |tick|
     - |none|
     - Stores animation F-Curves; used as data-block animation data, and the Nonlinear Animation editor
   * - Material
     - |tick|
     - |none|
     - Set shading and texturing render properties; used by objects, meshes & curves
   * - Scene
     - |tick|
     - |none|
     - Primary store of all data displayed and animated; used as top-level storage for objects & animation
   * - Texture
     - |tick|
     - |none|
     - 2D/3D textures; used by brushes and modifiers
   * - World
     - |tick|
     - |none|
     - Define global render environment settings

.. _dbl-life_time:

Life Time
++++++++++++++++++++++++++++++

Every data-block has its usage counted (reference count) - when there is more than one, you can see the number of current users of a data-block to the right of its name in the interface. Blender follows the general rule that unused data is eventually removed.

Since it is common to add and remove a lot of data while working, this has the advantage of not having to manually manage every single data-block. This works by skipping zero user data-blocks when writing blend-files.

.. figure:: /images/datablocks/dbl-zero_fake_user.png
   :figwidth: 50%
   :align: right

   Protected (blue shield) data-block

.. _dbl-protected:

Protected
------------------------------

Since zero user data-blocks are not saved, there are times when you want to force the data to be kept irrespective of its users.

If you are building a blend-file to serve as a library of assets that you intend to link to and from other files, you will need to make sure that they do not accidentally get deleted from the library file.

To protect a data-block, use the button with the shield icon next to its name. The data-block will then never be silently deleted by Blender, but you can still manually remove it if needed.

Sharing
++++++++++++++++++++++++++++++

Data-blocks can be shared among other data-blocks.

Examples where sharing data is common:

- Sharing textures among materials.
- Sharing meshes between objects (instances).
- Sharing animated actions between objects, for example to make all the lights dim together.

You can also share data-blocks between files.

.. _dbl-making_single_user:

Making Single User
++++++++++++++++++++++++++++++

When a data-block is shared between several users, you can make a copy of it for a given user. To do so, click on the user count button to the right of its name (number ``43`` in above image). This will duplicate that data-block and assign the newly created copy to that usage only.

.. note::
   Objects have a set of more advanced actions to become single-user.

Removing Data-Blocks
++++++++++++++++++++++++++++++

As covered in `Life Time`_, data-blocks are typically removed when they are no longer used. They can also be manually *unlinked* or *deleted*.

Unlinking a data-block means that its user won't use it anymore. This can be achieved by clicking on the :menuselection:`X` icon next to a data-block's name (see above image). If you unlink a data-block from all of its users, it will eventually be deleted by Blender as described above (unless it is a protected one).

Deleting a data-block directly erases it from the blend-file, automatically unlinking it from all of its users. This can be achieved by :kbd:`Shift-LMB` on the :menuselection:`X` icon next to its name.

.. warning::
   Deleting some data-blocks can lead to deletion of some of its users, which would become invalid without them. The main example is that object-data deletion (like mesh, curve, camera ...) will also delete all objects using it.

Those two operations are also available in the context menu when :kbd:`RMB`-clicking on a data-block in the *Outliner*.

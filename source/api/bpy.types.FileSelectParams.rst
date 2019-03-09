FileSelectParams(bpy_struct)
============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FileSelectParams(bpy_struct)

   File Select Parameters

   .. attribute:: directory

      Directory displayed in the file browser

      :type: string, default "", (never None)

   .. attribute:: display_size

      Change the size of the display (width of columns or thumbnails size)

      :type: enum in ['TINY', 'SMALL', 'NORMAL', 'LARGE'], default 'TINY'

   .. attribute:: display_type

      Display mode for the file list

      * ``LIST_SHORT`` Short List, Display files as short list.
      * ``LIST_LONG`` Long List, Display files as a detailed list.
      * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.

      :type: enum in ['LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], default 'LIST_SHORT'

   .. attribute:: filename

      Active file in the file browser

      :type: string, default "", (never None)

   .. attribute:: filter_glob

      :type: string, default "", (never None)

   .. attribute:: filter_id

      Which ID types to show/hide, when browsing a library

      * ``ACTION`` Actions, Show/hide Action data-blocks.
      * ``ARMATURE`` Armatures, Show/hide Armature data-blocks.
      * ``BRUSH`` Brushes, Show/hide Brushes data-blocks.
      * ``CAMERA`` Cameras, Show/hide Camera data-blocks.
      * ``CACHEFILE`` Cache Files, Show/hide Cache File data-blocks.
      * ``CURVE`` Curves, Show/hide Curve data-blocks.
      * ``GREASE_PENCIL`` Grease Pencil, Show/hide Grease pencil data-blocks.
      * ``GROUP`` Groups, Show/hide Group data-blocks.
      * ``IMAGE`` Images, Show/hide Image data-blocks.
      * ``LAMP`` Lamps, Show/hide Lamp data-blocks.
      * ``LINESTYLE`` Freestyle Linestyles, Show/hide Freestyle's Line Style data-blocks.
      * ``LATTICE`` Lattices, Show/hide Lattice data-blocks.
      * ``MATERIAL`` Materials, Show/hide Material data-blocks.
      * ``METABALL`` Metaballs, Show/hide Metaball data-blocks.
      * ``MOVIE_CLIP`` Movie Clips, Show/hide Movie Clip data-blocks.
      * ``MESH`` Meshes, Show/hide Mesh data-blocks.
      * ``MASK`` Masks, Show/hide Mask data-blocks.
      * ``NODE_TREE`` Node Trees, Show/hide Node Tree data-blocks.
      * ``OBJECT`` Objects, Show/hide Object data-blocks.
      * ``PARTICLE_SETTINGS`` Particles Settings, Show/hide Particle Settings data-blocks.
      * ``PALETTE`` Palettes, Show/hide Palette data-blocks.
      * ``PAINT_CURVE`` Paint Curves, Show/hide Paint Curve data-blocks.
      * ``SCENE`` Scenes, Show/hide Scene data-blocks.
      * ``SPEAKER`` Speakers, Show/hide Speaker data-blocks.
      * ``SOUND`` Sounds, Show/hide Sound data-blocks.
      * ``TEXTURE`` Textures, Show/hide Texture data-blocks.
      * ``TEXT`` Texts, Show/hide Text data-blocks.
      * ``FONT`` Fonts, Show/hide Font data-blocks.
      * ``WORLD`` Worlds, Show/hide World data-blocks.

      :type: enum set in {'ACTION', 'ARMATURE', 'BRUSH', 'CAMERA', 'CACHEFILE', 'CURVE', 'GREASE_PENCIL', 'GROUP', 'IMAGE', 'LAMP', 'LINESTYLE', 'LATTICE', 'MATERIAL', 'METABALL', 'MOVIE_CLIP', 'MESH', 'MASK', 'NODE_TREE', 'OBJECT', 'PARTICLE_SETTINGS', 'PALETTE', 'PAINT_CURVE', 'SCENE', 'SPEAKER', 'SOUND', 'TEXTURE', 'TEXT', 'FONT', 'WORLD'}, default {'ACTION'}

   .. attribute:: filter_id_category

      Which ID categories to show/hide, when browsing a library

      * ``SCENE`` Scenes, Show/hide scenes.
      * ``ANIMATION`` Animations, Show/hide animation data.
      * ``OBJECT`` Objects & Groups, Show/hide objects and groups.
      * ``GEOMETRY`` Geometry, Show/hide meshes, curves, lattice, armatures and metaballs data.
      * ``SHADING`` Shading, Show/hide materials, nodetrees, textures and Freestyle's linestyles.
      * ``IMAGE`` Images & Sounds, Show/hide images, movie clips, sounds and masks.
      * ``ENVIRONMENT`` Environment, Show/hide worlds, lamps, cameras and speakers.
      * ``MISC`` Miscellaneous, Show/hide other data types.

      :type: enum set in {'SCENE', 'ANIMATION', 'OBJECT', 'GEOMETRY', 'SHADING', 'IMAGE', 'ENVIRONMENT', 'MISC'}, default {'SCENE'}

   .. attribute:: filter_search

      Filter by name, supports '*' wildcard

      :type: string, default "", (never None)

   .. attribute:: recursion_level

      Numbers of dirtree levels to show simultaneously

      * ``NONE`` None, Only list current directory's content, with no recursion.
      * ``BLEND`` Blend File, List .blend files' content.
      * ``ALL_1`` One Level, List all sub-directories' content, one level of recursion.
      * ``ALL_2`` Two Levels, List all sub-directories' content, two levels of recursion.
      * ``ALL_3`` Three Levels, List all sub-directories' content, three levels of recursion.

      :type: enum in ['NONE', 'BLEND', 'ALL_1', 'ALL_2', 'ALL_3'], default 'NONE'

   .. attribute:: show_hidden

      Show hidden dot files

      :type: boolean, default False

   .. attribute:: sort_method

      * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type.
      * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time.
      * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.

      :type: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], default 'FILE_SORT_ALPHA'

   .. data:: title

      Title for the file browser

      :type: string, default "", (readonly, never None)

   .. attribute:: use_filter

      Enable filtering of files

      :type: boolean, default False

   .. attribute:: use_filter_backup

      Show .blend1, .blend2, etc. files

      :type: boolean, default False

   .. attribute:: use_filter_blender

      Show .blend files

      :type: boolean, default False

   .. attribute:: use_filter_blendid

      Show .blend files items (objects, materials, etc.)

      :type: boolean, default False

   .. attribute:: use_filter_folder

      Show folders

      :type: boolean, default False

   .. attribute:: use_filter_font

      Show font files

      :type: boolean, default False

   .. attribute:: use_filter_image

      Show image files

      :type: boolean, default False

   .. attribute:: use_filter_movie

      Show movie files

      :type: boolean, default False

   .. attribute:: use_filter_script

      Show script files

      :type: boolean, default False

   .. attribute:: use_filter_sound

      Show sound files

      :type: boolean, default False

   .. attribute:: use_filter_text

      Show text files

      :type: boolean, default False

   .. data:: use_library_browsing

      Whether we may browse blender files' content or not

      :type: boolean, default False, (readonly)

   .. classmethod:: bl_rna_get_subclass(id, default=None)
   
      :arg id: The RNA type identifier.
      :type id: string
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct` subclass


   .. classmethod:: bl_rna_get_subclass_py(id, default=None)
   
      :arg id: The RNA type identifier.
      :type id: string
      :return: The class or default when not found.
      :rtype: type


.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`

.. rubric:: Inherited Functions

.. hlist::
   :columns: 2

   * :class:`bpy_struct.as_pointer`
   * :class:`bpy_struct.driver_add`
   * :class:`bpy_struct.driver_remove`
   * :class:`bpy_struct.get`
   * :class:`bpy_struct.is_property_hidden`
   * :class:`bpy_struct.is_property_readonly`
   * :class:`bpy_struct.is_property_set`
   * :class:`bpy_struct.items`
   * :class:`bpy_struct.keyframe_delete`
   * :class:`bpy_struct.keyframe_insert`
   * :class:`bpy_struct.keys`
   * :class:`bpy_struct.path_from_id`
   * :class:`bpy_struct.path_resolve`
   * :class:`bpy_struct.property_unset`
   * :class:`bpy_struct.type_recast`
   * :class:`bpy_struct.values`

.. rubric:: References

.. hlist::
   :columns: 2

   * :class:`SpaceFileBrowser.params`


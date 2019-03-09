Texture Operators
=================

.. module:: bpy.ops.texture

.. function:: envmap_clear()

   Discard the environment map and free it from memory

.. function:: envmap_clear_all()

   Discard all environment maps in the .blend file and free them from memory

.. function:: envmap_save(layout=(0.0, 0.0, 1.0, 0.0, 2.0, 0.0, 0.0, 1.0, 1.0, 1.0, 2.0, 1.0), filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA')

   Save the current generated Environment map to an image file

   :arg layout:

      File layout, Flat array describing the X,Y position of each cube face in the output image, where 1 is the size of a face - order is [+Z -Z +Y -X -Y +X] (use -1 to skip a face)

   :type layout: float array of 12 items in [-inf, inf], (optional)
   :arg filepath:

      File Path, Path to file

   :type filepath: string, (optional, never None)
   :arg check_existing:

      Check Existing, Check and warn on overwriting existing files

   :type check_existing: boolean, (optional)
   :arg filter_blender:

      Filter .blend files

   :type filter_blender: boolean, (optional)
   :arg filter_backup:

      Filter .blend files

   :type filter_backup: boolean, (optional)
   :arg filter_image:

      Filter image files

   :type filter_image: boolean, (optional)
   :arg filter_movie:

      Filter movie files

   :type filter_movie: boolean, (optional)
   :arg filter_python:

      Filter python files

   :type filter_python: boolean, (optional)
   :arg filter_font:

      Filter font files

   :type filter_font: boolean, (optional)
   :arg filter_sound:

      Filter sound files

   :type filter_sound: boolean, (optional)
   :arg filter_text:

      Filter text files

   :type filter_text: boolean, (optional)
   :arg filter_btx:

      Filter btx files

   :type filter_btx: boolean, (optional)
   :arg filter_collada:

      Filter COLLADA files

   :type filter_collada: boolean, (optional)
   :arg filter_alembic:

      Filter Alembic files

   :type filter_alembic: boolean, (optional)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_blenlib:

      Filter Blender IDs

   :type filter_blenlib: boolean, (optional)
   :arg filemode:

      File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

   :type filemode: int in [1, 9], (optional)
   :arg show_multiview:

      Enable Multi-View

   :type show_multiview: boolean, (optional)
   :arg use_multiview:

      Use Multi-View

   :type use_multiview: boolean, (optional)
   :arg display_type:

      Display Type

      * ``DEFAULT`` Default, Automatically determine display type for files.
      * ``LIST_SHORT`` Short List, Display files as short list.
      * ``LIST_LONG`` Long List, Display files as a detailed list.
      * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.

   :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
   :arg sort_method:

      File sorting mode

      * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type.
      * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time.
      * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.

   :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

.. function:: new()

   Add a new texture

.. function:: slot_copy()

   Copy the material texture settings and nodes

.. function:: slot_move(type='UP')

   Move texture slots up and down

   :arg type:

      Type

   :type type: enum in ['UP', 'DOWN'], (optional)

.. function:: slot_paste()

   Copy the texture settings and nodes


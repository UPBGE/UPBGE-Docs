File Operators
==============

.. module:: bpy.ops.file

.. function:: autopack_toggle()

   Automatically pack all external files into the .blend file

.. function:: bookmark_add()

   Add a bookmark for the selected/active directory

.. function:: bookmark_cleanup()

   Delete all invalid bookmarks

.. function:: bookmark_delete(index=-1)

   Delete selected bookmark

   :arg index:

      Index

   :type index: int in [-1, 20000], (optional)

.. function:: bookmark_move(direction='TOP')

   Move the active bookmark up/down in the list

   :arg direction:

      Direction, Direction to move the active bookmark towards

      * ``TOP`` Top, Top of the list.
      * ``UP`` Up.
      * ``DOWN`` Down.
      * ``BOTTOM`` Bottom, Bottom of the list.

   :type direction: enum in ['TOP', 'UP', 'DOWN', 'BOTTOM'], (optional)

.. function:: bookmark_toggle()

   Toggle bookmarks display

.. function:: cancel()

   Cancel loading of selected file

.. function:: delete()

   Delete selected files

.. function:: directory_new(directory="", open=False)

   Create a new directory

   :arg directory:

      Directory, Name of new directory

   :type directory: string, (optional, never None)
   :arg open:

      Open, Open new directory

   :type open: boolean, (optional)

.. function:: execute(need_active=False)

   Execute selected file

   :arg need_active:

      Need Active, Only execute if there's an active selected file in the file list

   :type need_active: boolean, (optional)

.. function:: filenum(increment=1)

   Increment number in filename

   :arg increment:

      Increment

   :type increment: int in [-100, 100], (optional)

.. function:: filepath_drop(filepath="Path")

   Undocumented

   :type filepath: string, (optional, never None)

.. function:: find_missing_files(find_all=False, directory="", filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=False, filter_blenlib=False, filemode=9, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA')

   Try to find missing external files

   :arg find_all:

      Find All, Find all files in the search path (not just missing)

   :type find_all: boolean, (optional)
   :arg directory:

      Directory, Directory of the file

   :type directory: string, (optional, never None)
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

.. function:: hidedot()

   Toggle hide hidden dot files

.. function:: highlight()

   Highlight selected file(s)

.. function:: make_paths_absolute()

   Make all paths to external files absolute

.. function:: make_paths_relative()

   Make all paths to external files relative to current .blend

.. function:: next()

   Move to next folder

.. function:: pack_all()

   Pack all used external files into the .blend

.. function:: pack_libraries()

   Pack all used Blender library files into the current .blend

.. function:: parent()

   Move to parent directory

.. function:: previous()

   Move to previous folder

.. function:: refresh()

   Refresh the file list

.. function:: rename()

   Rename file or file directory

.. function:: report_missing_files()

   Report all missing external files

.. function:: reset_recent()

   Reset Recent files

.. function:: select(extend=False, fill=False, open=True)

   Activate/select file

   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)
   :arg fill:

      Fill, Select everything beginning with the last selection

   :type fill: boolean, (optional)
   :arg open:

      Open, Open a directory when selecting it

   :type open: boolean, (optional)

.. function:: select_all_toggle()

   Select or deselect all files

.. function:: select_bookmark(dir="")

   Select a bookmarked directory

   :arg dir:

      Dir

   :type dir: string, (optional, never None)

.. function:: select_border(xmin=0, xmax=0, ymin=0, ymax=0, deselect=False, extend=True)

   Activate/select the file(s) contained in the border

   :arg xmin:

      X Min

   :type xmin: int in [-inf, inf], (optional)
   :arg xmax:

      X Max

   :type xmax: int in [-inf, inf], (optional)
   :arg ymin:

      Y Min

   :type ymin: int in [-inf, inf], (optional)
   :arg ymax:

      Y Max

   :type ymax: int in [-inf, inf], (optional)
   :arg deselect:

      Deselect, Deselect rather than select items

   :type deselect: boolean, (optional)
   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)

.. function:: select_walk(direction='UP', extend=False, fill=False)

   Select/Deselect files by walking through them

   :arg direction:

      Walk Direction, Select/Deselect file in this direction

   :type direction: enum in ['UP', 'DOWN', 'LEFT', 'RIGHT'], (optional)
   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)
   :arg fill:

      Fill, Select everything beginning with the last selection

   :type fill: boolean, (optional)

.. function:: smoothscroll()

   Smooth scroll to make editable file visible

.. function:: unpack_all(method='USE_LOCAL')

   Unpack all files packed into this .blend to external ones

   :arg method:

      Method, How to unpack

   :type method: enum in ['USE_LOCAL', 'WRITE_LOCAL', 'USE_ORIGINAL', 'WRITE_ORIGINAL', 'KEEP'], (optional)

.. function:: unpack_item(method='USE_LOCAL', id_name="", id_type=19785)

   Unpack this file to an external file

   :arg method:

      Method, How to unpack

   :type method: enum in ['USE_LOCAL', 'WRITE_LOCAL', 'USE_ORIGINAL', 'WRITE_ORIGINAL'], (optional)
   :arg id_name:

      ID name, Name of ID block to unpack

   :type id_name: string, (optional, never None)
   :arg id_type:

      ID Type, Identifier type of ID block

   :type id_type: int in [0, inf], (optional)

.. function:: unpack_libraries()

   Unpack all used Blender library files from this .blend file


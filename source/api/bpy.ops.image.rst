Image Operators
===============

.. module:: bpy.ops.image

.. function:: change_frame(frame=0)

   Interactively change the current frame number

   :arg frame:

      Frame

   :type frame: int in [-1048574, 1048574], (optional)

.. function:: clear_render_border()

   Clear the boundaries of the border render and disable border render

.. function:: curves_point_set(point='BLACK_POINT')

   Set black point or white point for curves

   :arg point:

      Point, Set black point or white point for curves

   :type point: enum in ['BLACK_POINT', 'WHITE_POINT'], (optional)

.. function:: cycle_render_slot(reverse=False)

   Cycle through all non-void render slots

   :arg reverse:

      Cycle in Reverse

   :type reverse: boolean, (optional)

.. function:: external_edit(filepath="")

   Edit image in an external application

   :arg filepath:

      filepath

   :type filepath: string, (optional, never None)

   :file: `startup\bl_operators\image.py\:61 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\image.py$61>`_

.. function:: invert(invert_r=False, invert_g=False, invert_b=False, invert_a=False)

   Invert image's channels

   :arg invert_r:

      Red, Invert Red Channel

   :type invert_r: boolean, (optional)
   :arg invert_g:

      Green, Invert Green Channel

   :type invert_g: boolean, (optional)
   :arg invert_b:

      Blue, Invert Blue Channel

   :type invert_b: boolean, (optional)
   :arg invert_a:

      Alpha, Invert Alpha Channel

   :type invert_a: boolean, (optional)

.. function:: match_movie_length()

   Set image's user's length to the one of this video

.. function:: new(name="Untitled", width=1024, height=1024, color=(0.0, 0.0, 0.0, 1.0), alpha=True, generated_type='BLANK', float=False, gen_context='NONE', use_stereo_3d=False)

   Create a new image

   :arg name:

      Name, Image data-block name

   :type name: string, (optional, never None)
   :arg width:

      Width, Image width

   :type width: int in [1, inf], (optional)
   :arg height:

      Height, Image height

   :type height: int in [1, inf], (optional)
   :arg color:

      Color, Default fill color

   :type color: float array of 4 items in [0, inf], (optional)
   :arg alpha:

      Alpha, Create an image with an alpha channel

   :type alpha: boolean, (optional)
   :arg generated_type:

      Generated Type, Fill the image with a grid for UV map testing

      * ``BLANK`` Blank, Generate a blank image.
      * ``UV_GRID`` UV Grid, Generated grid to test UV mappings.
      * ``COLOR_GRID`` Color Grid, Generated improved UV grid to test UV mappings.

   :type generated_type: enum in ['BLANK', 'UV_GRID', 'COLOR_GRID'], (optional)
   :arg float:

      32 bit Float, Create image with 32 bit floating point bit depth

   :type float: boolean, (optional)
   :arg gen_context:

      Gen Context, Generation context

   :type gen_context: enum in ['NONE', 'PAINT_CANVAS', 'PAINT_STENCIL'], (optional)
   :arg use_stereo_3d:

      Stereo 3D, Create an image with left and right views

   :type use_stereo_3d: boolean, (optional)

.. function:: open(filepath="", directory="", files=None, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', use_sequence_detection=True)

   Open image

   :arg filepath:

      File Path, Path to file

   :type filepath: string, (optional, never None)
   :arg directory:

      Directory, Directory of the file

   :type directory: string, (optional, never None)
   :arg files:

      Files

   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
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
   :arg relative_path:

      Relative Path, Select the file relative to the blend file

   :type relative_path: boolean, (optional)
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
   :arg use_sequence_detection:

      Detect Sequences, Automatically detect animated sequences in selected images (based on file names)

   :type use_sequence_detection: boolean, (optional)

.. function:: pack(as_png=False)

   Pack an image as embedded data into the .blend file

   :arg as_png:

      Pack As PNG, Pack image as lossless PNG

   :type as_png: boolean, (optional)

.. function:: project_apply()

   Project edited image back onto the object

   :file: `startup\bl_operators\image.py\:230 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\image.py$230>`_

.. function:: project_edit()

   Edit a snapshot of the view-port in an external image editor

   :file: `startup\bl_operators\image.py\:159 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\image.py$159>`_

.. function:: properties()

   Toggle the properties region visibility

.. function:: read_renderlayers()

   Read all the current scene's render layers from cache, as needed

.. function:: reload()

   Reload current image from disk

.. function:: render_border(xmin=0, xmax=0, ymin=0, ymax=0)

   Set the boundaries of the border render and enable border render

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

.. function:: replace(filepath="", filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA')

   Replace current image by another one from disk

   :arg filepath:

      File Path, Path to file

   :type filepath: string, (optional, never None)
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
   :arg relative_path:

      Relative Path, Select the file relative to the blend file

   :type relative_path: boolean, (optional)
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

.. function:: resize_cube_map()

   Resize CubeMap texture to a compatible format

.. function:: sample()

   Use mouse to sample a color in current image

.. function:: sample_line(xstart=0, xend=0, ystart=0, yend=0, cursor=1002)

   Sample a line and show it in Scope panels

   :arg xstart:

      X Start

   :type xstart: int in [-inf, inf], (optional)
   :arg xend:

      X End

   :type xend: int in [-inf, inf], (optional)
   :arg ystart:

      Y Start

   :type ystart: int in [-inf, inf], (optional)
   :arg yend:

      Y End

   :type yend: int in [-inf, inf], (optional)
   :arg cursor:

      Cursor, Mouse cursor style to use during the modal operator

   :type cursor: int in [0, inf], (optional)

.. function:: save()

   Save the image with current name and settings

.. function:: save_as(save_as_render=False, copy=False, filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA')

   Save the image with another name and/or settings

   :arg save_as_render:

      Save As Render, Apply render part of display transform when saving byte image

   :type save_as_render: boolean, (optional)
   :arg copy:

      Copy, Create a new image file without modifying the current image in blender

   :type copy: boolean, (optional)
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
   :arg relative_path:

      Relative Path, Select the file relative to the blend file

   :type relative_path: boolean, (optional)
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

.. function:: save_dirty()

   Save all modified textures

   :file: `startup\bl_operators\image.py\:124 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\image.py$124>`_

.. function:: save_sequence()

   Save a sequence of images

.. function:: toolshelf()

   Toggles tool shelf display

.. function:: unpack(method='USE_LOCAL', id="")

   Save an image packed in the .blend file to disk

   :arg method:

      Method, How to unpack

   :type method: enum in ['USE_LOCAL', 'WRITE_LOCAL', 'USE_ORIGINAL', 'WRITE_ORIGINAL'], (optional)
   :arg id:

      Image Name, Image data-block name to unpack

   :type id: string, (optional, never None)

.. function:: view_all(fit_view=False)

   View the entire image

   :arg fit_view:

      Fit View, Fit frame to the viewport

   :type fit_view: boolean, (optional)

.. function:: view_ndof()

   Use a 3D mouse device to pan/zoom the view

.. function:: view_pan(offset=(0.0, 0.0))

   Pan the view

   :arg offset:

      Offset, Offset in floating point units, 1.0 is the width and height of the image

   :type offset: float array of 2 items in [-inf, inf], (optional)

.. function:: view_selected()

   View all selected UVs

.. function:: view_zoom(factor=0.0)

   Zoom in/out the image

   :arg factor:

      Factor, Zoom factor, values higher than 1.0 zoom in, lower values zoom out

   :type factor: float in [-inf, inf], (optional)

.. function:: view_zoom_border(xmin=0, xmax=0, ymin=0, ymax=0, zoom_out=False)

   Zoom in the view to the nearest item contained in the border

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
   :arg zoom_out:

      Zoom Out

   :type zoom_out: boolean, (optional)

.. function:: view_zoom_in(location=(0.0, 0.0))

   Zoom in the image (centered around 2D cursor)

   :arg location:

      Location, Cursor location in screen coordinates

   :type location: float array of 2 items in [-inf, inf], (optional)

.. function:: view_zoom_out(location=(0.0, 0.0))

   Zoom out the image (centered around 2D cursor)

   :arg location:

      Location, Cursor location in screen coordinates

   :type location: float array of 2 items in [-inf, inf], (optional)

.. function:: view_zoom_ratio(ratio=0.0)

   Set zoom ratio of the view

   :arg ratio:

      Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out

   :type ratio: float in [-inf, inf], (optional)


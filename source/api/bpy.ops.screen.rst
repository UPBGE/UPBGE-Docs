Screen Operators
================

.. module:: bpy.ops.screen

.. function:: actionzone(modifier=0)

   Handle area action zones for mouse actions/gestures

   :arg modifier:

      Modifier, Modifier state

   :type modifier: int in [0, 2], (optional)

.. function:: animation_cancel(restore_frame=True)

   Cancel animation, returning to the original frame

   :arg restore_frame:

      Restore Frame, Restore the frame when animation was initialized

   :type restore_frame: boolean, (optional)

.. function:: animation_play(reverse=False, sync=False)

   Play animation

   :arg reverse:

      Play in Reverse, Animation is played backwards

   :type reverse: boolean, (optional)
   :arg sync:

      Sync, Drop frames to maintain framerate

   :type sync: boolean, (optional)

.. function:: animation_step()

   Step through animation by position

.. function:: area_dupli()

   Duplicate selected area into new window

.. function:: area_join(min_x=-100, min_y=-100, max_x=-100, max_y=-100)

   Join selected areas into new window

   :arg min_x:

      X 1

   :type min_x: int in [-inf, inf], (optional)
   :arg min_y:

      Y 1

   :type min_y: int in [-inf, inf], (optional)
   :arg max_x:

      X 2

   :type max_x: int in [-inf, inf], (optional)
   :arg max_y:

      Y 2

   :type max_y: int in [-inf, inf], (optional)

.. function:: area_move(x=0, y=0, delta=0)

   Move selected area edges

   :arg x:

      X

   :type x: int in [-inf, inf], (optional)
   :arg y:

      Y

   :type y: int in [-inf, inf], (optional)
   :arg delta:

      Delta

   :type delta: int in [-inf, inf], (optional)

.. function:: area_options()

   Operations for splitting and merging

.. function:: area_split(direction='HORIZONTAL', factor=0.5, mouse_x=-100, mouse_y=-100)

   Split selected area into new windows

   :arg direction:

      Direction

   :type direction: enum in ['HORIZONTAL', 'VERTICAL'], (optional)
   :arg factor:

      Factor

   :type factor: float in [0, 1], (optional)
   :arg mouse_x:

      Mouse X

   :type mouse_x: int in [-inf, inf], (optional)
   :arg mouse_y:

      Mouse Y

   :type mouse_y: int in [-inf, inf], (optional)

.. function:: area_swap()

   Swap selected areas screen positions

.. function:: back_to_previous()

   Revert back to the original screen layout, before fullscreen area overlay

.. function:: delete()

   Delete active screen

.. function:: frame_jump(end=False)

   Jump to first/last frame in frame range

   :arg end:

      Last Frame, Jump to the last frame of the frame range

   :type end: boolean, (optional)

.. function:: frame_offset(delta=0)

   Move current frame forward/backward by a given number

   :arg delta:

      Delta

   :type delta: int in [-inf, inf], (optional)

.. function:: header()

   Toggle header display

.. function:: header_toggle_menus()

   Expand or collapse the header pulldown menus

.. function:: header_toolbox()

   Display header region toolbox

.. function:: keyframe_jump(next=True)

   Jump to previous/next keyframe

   :arg next:

      Next Keyframe

   :type next: boolean, (optional)

.. function:: marker_jump(next=True)

   Jump to previous/next marker

   :arg next:

      Next Marker

   :type next: boolean, (optional)

.. function:: new()

   Add a new screen

.. function:: redo_last()

   Display menu for last action performed

.. function:: region_blend()

   Blend in and out overlapping region

.. function:: region_flip()

   Toggle the region's alignment (left/right or top/bottom)

.. function:: region_quadview()

   Split selected area into camera, front, right & top views

.. function:: region_scale()

   Scale selected area

.. function:: repeat_history(index=0)

   Display menu for previous actions performed

   :arg index:

      Index

   :type index: int in [0, inf], (optional)

.. function:: repeat_last()

   Repeat last action

.. function:: screen_full_area(use_hide_panels=False)

   Toggle display selected area as fullscreen/maximized

   :arg use_hide_panels:

      Hide Panels, Hide all the panels

   :type use_hide_panels: boolean, (optional)

.. function:: screen_set(delta=0)

   Cycle through available screens

   :arg delta:

      Delta

   :type delta: int in [-inf, inf], (optional)

.. function:: screencast(filepath="", full=True)

   Capture a video of the active area or whole Blender window

   :arg filepath:

      filepath

   :type filepath: string, (optional, never None)
   :arg full:

      Full Screen, Capture the whole window (otherwise only capture the active area)

   :type full: boolean, (optional)

.. function:: screenshot(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', full=True)

   Capture a picture of the active area or whole Blender window

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
   :arg full:

      Full Screen, Capture the whole window (otherwise only capture the active area)

   :type full: boolean, (optional)

.. function:: space_context_cycle(direction='NEXT')

   Cycle through the editor context by activating the next/previous one

   :arg direction:

      Direction, Direction to cycle through

   :type direction: enum in ['PREV', 'NEXT'], (optional)

.. function:: spacedata_cleanup()

   Remove unused settings for invisible editors

.. function:: userpref_show()

   Show user preferences


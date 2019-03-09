Sequencer Operators
===================

.. module:: bpy.ops.sequencer

.. function:: change_effect_input(swap='A_B')

   Undocumented

   :arg swap:

      Swap, The effect inputs to swap

   :type swap: enum in ['A_B', 'B_C', 'A_C'], (optional)

.. function:: change_effect_type(type='CROSS')

   Undocumented

   :arg type:

      Type, Sequencer effect type

      * ``CROSS`` Crossfade, Crossfade effect strip type.
      * ``ADD`` Add, Add effect strip type.
      * ``SUBTRACT`` Subtract, Subtract effect strip type.
      * ``ALPHA_OVER`` Alpha Over, Alpha Over effect strip type.
      * ``ALPHA_UNDER`` Alpha Under, Alpha Under effect strip type.
      * ``GAMMA_CROSS`` Gamma Cross, Gamma Cross effect strip type.
      * ``MULTIPLY`` Multiply, Multiply effect strip type.
      * ``OVER_DROP`` Alpha Over Drop, Alpha Over Drop effect strip type.
      * ``WIPE`` Wipe, Wipe effect strip type.
      * ``GLOW`` Glow, Glow effect strip type.
      * ``TRANSFORM`` Transform, Transform effect strip type.
      * ``COLOR`` Color, Color effect strip type.
      * ``SPEED`` Speed, Color effect strip type.
      * ``MULTICAM`` Multicam Selector.
      * ``ADJUSTMENT`` Adjustment Layer.
      * ``GAUSSIAN_BLUR`` Gaussian Blur.
      * ``TEXT`` Text.
      * ``COLORMIX`` Color Mix.

   :type type: enum in ['CROSS', 'ADD', 'SUBTRACT', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS', 'MULTIPLY', 'OVER_DROP', 'WIPE', 'GLOW', 'TRANSFORM', 'COLOR', 'SPEED', 'MULTICAM', 'ADJUSTMENT', 'GAUSSIAN_BLUR', 'TEXT', 'COLORMIX'], (optional)

.. function:: change_path(filepath="", directory="", files=None, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', use_placeholders=False)

   Undocumented

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
   :arg use_placeholders:

      Use Placeholders, Use placeholders for missing frames of the strip

   :type use_placeholders: boolean, (optional)

.. function:: copy()

   Undocumented

.. function:: crossfade_sounds()

   Do cross-fading volume animation of two selected sound strips

   :file: `startup\bl_operators\sequencer.py\:41 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\sequencer.py$41>`_

.. function:: cut(frame=0, type='SOFT', side='BOTH')

   Cut the selected strips

   :arg frame:

      Frame, Frame where selected strips will be cut

   :type frame: int in [-inf, inf], (optional)
   :arg type:

      Type, The type of cut operation to perform on strips

   :type type: enum in ['SOFT', 'HARD'], (optional)
   :arg side:

      Side, The side that remains selected after cutting

   :type side: enum in ['LEFT', 'RIGHT', 'BOTH'], (optional)

.. function:: cut_multicam(camera=1)

   Cut multi-cam strip and select camera

   :arg camera:

      Camera

   :type camera: int in [1, 32], (optional)

   :file: `startup\bl_operators\sequencer.py\:99 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\sequencer.py$99>`_

.. function:: deinterlace_selected_movies()

   Deinterlace all selected movie sources

   :file: `startup\bl_operators\sequencer.py\:131 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\sequencer.py$131>`_

.. function:: delete()

   Erase selected strips from the sequencer

.. function:: duplicate(mode='TRANSLATION')

   Duplicate the selected strips

   :arg mode:

      Mode

   :type mode: enum in ['INIT', 'DUMMY', 'TRANSLATION', 'ROTATION', 'RESIZE', 'SKIN_RESIZE', 'TOSPHERE', 'SHEAR', 'BEND', 'SHRINKFATTEN', 'TILT', 'TRACKBALL', 'PUSHPULL', 'CREASE', 'MIRROR', 'BONE_SIZE', 'BONE_ENVELOPE', 'BONE_ENVELOPE_DIST', 'CURVE_SHRINKFATTEN', 'MASK_SHRINKFATTEN', 'GPENCIL_SHRINKFATTEN', 'BONE_ROLL', 'TIME_TRANSLATE', 'TIME_SLIDE', 'TIME_SCALE', 'TIME_EXTEND', 'BAKE_TIME', 'BWEIGHT', 'ALIGN', 'EDGESLIDE', 'SEQSLIDE'], (optional)

.. function:: duplicate_move(SEQUENCER_OT_duplicate=None, TRANSFORM_OT_seq_slide=None)

   Duplicate selected strips and move them

   :arg SEQUENCER_OT_duplicate:

      Duplicate Strips, Duplicate the selected strips

   :type SEQUENCER_OT_duplicate: :class:`SEQUENCER_OT_duplicate`, (optional)
   :arg TRANSFORM_OT_seq_slide:

      Sequence Slide, Slide a sequence strip in time

   :type TRANSFORM_OT_seq_slide: :class:`TRANSFORM_OT_seq_slide`, (optional)

.. function:: effect_strip_add(frame_start=0, frame_end=0, channel=1, replace_sel=True, overlap=False, type='CROSS', color=(0.0, 0.0, 0.0))

   Add an effect to the sequencer, most are applied on top of existing strips

   :arg frame_start:

      Start Frame, Start frame of the sequence strip

   :type frame_start: int in [-inf, inf], (optional)
   :arg frame_end:

      End Frame, End frame for the color strip

   :type frame_end: int in [-inf, inf], (optional)
   :arg channel:

      Channel, Channel to place this strip into

   :type channel: int in [1, 32], (optional)
   :arg replace_sel:

      Replace Selection, Replace the current selection

   :type replace_sel: boolean, (optional)
   :arg overlap:

      Allow Overlap, Don't correct overlap on new sequence strips

   :type overlap: boolean, (optional)
   :arg type:

      Type, Sequencer effect type

      * ``CROSS`` Crossfade, Crossfade effect strip type.
      * ``ADD`` Add, Add effect strip type.
      * ``SUBTRACT`` Subtract, Subtract effect strip type.
      * ``ALPHA_OVER`` Alpha Over, Alpha Over effect strip type.
      * ``ALPHA_UNDER`` Alpha Under, Alpha Under effect strip type.
      * ``GAMMA_CROSS`` Gamma Cross, Gamma Cross effect strip type.
      * ``MULTIPLY`` Multiply, Multiply effect strip type.
      * ``OVER_DROP`` Alpha Over Drop, Alpha Over Drop effect strip type.
      * ``WIPE`` Wipe, Wipe effect strip type.
      * ``GLOW`` Glow, Glow effect strip type.
      * ``TRANSFORM`` Transform, Transform effect strip type.
      * ``COLOR`` Color, Color effect strip type.
      * ``SPEED`` Speed, Color effect strip type.
      * ``MULTICAM`` Multicam Selector.
      * ``ADJUSTMENT`` Adjustment Layer.
      * ``GAUSSIAN_BLUR`` Gaussian Blur.
      * ``TEXT`` Text.
      * ``COLORMIX`` Color Mix.

   :type type: enum in ['CROSS', 'ADD', 'SUBTRACT', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS', 'MULTIPLY', 'OVER_DROP', 'WIPE', 'GLOW', 'TRANSFORM', 'COLOR', 'SPEED', 'MULTICAM', 'ADJUSTMENT', 'GAUSSIAN_BLUR', 'TEXT', 'COLORMIX'], (optional)
   :arg color:

      Color, Initialize the strip with this color (only used when type='COLOR')

   :type color: float array of 3 items in [0, 1], (optional)

.. function:: enable_proxies(proxy_25=False, proxy_50=False, proxy_75=False, proxy_100=False, overwrite=False)

   Enable selected proxies on all selected Movie strips

   :arg proxy_25:

      25%

   :type proxy_25: boolean, (optional)
   :arg proxy_50:

      50%

   :type proxy_50: boolean, (optional)
   :arg proxy_75:

      75%

   :type proxy_75: boolean, (optional)
   :arg proxy_100:

      100%

   :type proxy_100: boolean, (optional)
   :arg overwrite:

      Overwrite

   :type overwrite: boolean, (optional)

.. function:: export_subtitles(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA')

   Export .srt file containing text strips

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

.. function:: gap_insert(frames=10)

   Insert gap at current frame to first strips at the right, independent of selection or locked state of strips

   :arg frames:

      Frames, Frames to insert after current strip

   :type frames: int in [0, inf], (optional)

.. function:: gap_remove(all=False)

   Remove gap at current frame to first strip at the right, independent of selection or locked state of strips

   :arg all:

      All Gaps, Do all gaps to right of current frame

   :type all: boolean, (optional)

.. function:: image_strip_add(directory="", files=None, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', frame_start=0, frame_end=0, channel=1, replace_sel=True, overlap=False, use_placeholders=False)

   Add an image or image sequence to the sequencer

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
   :arg frame_start:

      Start Frame, Start frame of the sequence strip

   :type frame_start: int in [-inf, inf], (optional)
   :arg frame_end:

      End Frame, End frame for the color strip

   :type frame_end: int in [-inf, inf], (optional)
   :arg channel:

      Channel, Channel to place this strip into

   :type channel: int in [1, 32], (optional)
   :arg replace_sel:

      Replace Selection, Replace the current selection

   :type replace_sel: boolean, (optional)
   :arg overlap:

      Allow Overlap, Don't correct overlap on new sequence strips

   :type overlap: boolean, (optional)
   :arg use_placeholders:

      Use Placeholders, Use placeholders for missing frames of the strip

   :type use_placeholders: boolean, (optional)

.. function:: images_separate(length=1)

   On image sequence strips, it returns a strip for each image

   :arg length:

      Length, Length of each frame

   :type length: int in [1, inf], (optional)

.. function:: lock()

   Lock the active strip so that it can't be transformed

.. function:: mask_strip_add(frame_start=0, channel=1, replace_sel=True, overlap=False, mask='')

   Add a mask strip to the sequencer

   :arg frame_start:

      Start Frame, Start frame of the sequence strip

   :type frame_start: int in [-inf, inf], (optional)
   :arg channel:

      Channel, Channel to place this strip into

   :type channel: int in [1, 32], (optional)
   :arg replace_sel:

      Replace Selection, Replace the current selection

   :type replace_sel: boolean, (optional)
   :arg overlap:

      Allow Overlap, Don't correct overlap on new sequence strips

   :type overlap: boolean, (optional)
   :arg mask:

      Mask

   :type mask: enum in [], (optional)

.. function:: meta_make()

   Group selected strips into a metastrip

.. function:: meta_separate()

   Put the contents of a metastrip back in the sequencer

.. function:: meta_toggle()

   Toggle a metastrip (to edit enclosed strips)

.. function:: movie_strip_add(filepath="", files=None, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', frame_start=0, channel=1, replace_sel=True, overlap=False, sound=True, use_framerate=True)

   Add a movie strip to the sequencer

   :arg filepath:

      File Path, Path to file

   :type filepath: string, (optional, never None)
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
   :arg frame_start:

      Start Frame, Start frame of the sequence strip

   :type frame_start: int in [-inf, inf], (optional)
   :arg channel:

      Channel, Channel to place this strip into

   :type channel: int in [1, 32], (optional)
   :arg replace_sel:

      Replace Selection, Replace the current selection

   :type replace_sel: boolean, (optional)
   :arg overlap:

      Allow Overlap, Don't correct overlap on new sequence strips

   :type overlap: boolean, (optional)
   :arg sound:

      Sound, Load sound with the movie

   :type sound: boolean, (optional)
   :arg use_framerate:

      Use Movie Framerate, Use framerate from the movie to keep sound and video in sync

   :type use_framerate: boolean, (optional)

.. function:: movieclip_strip_add(frame_start=0, channel=1, replace_sel=True, overlap=False, clip='')

   Add a movieclip strip to the sequencer

   :arg frame_start:

      Start Frame, Start frame of the sequence strip

   :type frame_start: int in [-inf, inf], (optional)
   :arg channel:

      Channel, Channel to place this strip into

   :type channel: int in [1, 32], (optional)
   :arg replace_sel:

      Replace Selection, Replace the current selection

   :type replace_sel: boolean, (optional)
   :arg overlap:

      Allow Overlap, Don't correct overlap on new sequence strips

   :type overlap: boolean, (optional)
   :arg clip:

      Clip

   :type clip: enum in [], (optional)

.. function:: mute(unselected=False)

   Mute (un)selected strips

   :arg unselected:

      Unselected, Mute unselected rather than selected strips

   :type unselected: boolean, (optional)

.. function:: offset_clear()

   Clear strip offsets from the start and end frames

.. function:: paste()

   Undocumented

.. function:: properties()

   Toggle the properties region visibility

.. function:: reassign_inputs()

   Reassign the inputs for the effect strip

.. function:: rebuild_proxy()

   Rebuild all selected proxies and timecode indices using the job system

.. function:: refresh_all()

   Refresh the sequencer editor

.. function:: reload(adjust_length=False)

   Reload strips in the sequencer

   :arg adjust_length:

      Adjust Length, Adjust length of strips to their data length

   :type adjust_length: boolean, (optional)

.. function:: rendersize()

   Set render size and aspect from active sequence

.. function:: sample()

   Use mouse to sample color in current frame

.. function:: scene_strip_add(frame_start=0, channel=1, replace_sel=True, overlap=False, scene='')

   Add a strip to the sequencer using a blender scene as a source

   :arg frame_start:

      Start Frame, Start frame of the sequence strip

   :type frame_start: int in [-inf, inf], (optional)
   :arg channel:

      Channel, Channel to place this strip into

   :type channel: int in [1, 32], (optional)
   :arg replace_sel:

      Replace Selection, Replace the current selection

   :type replace_sel: boolean, (optional)
   :arg overlap:

      Allow Overlap, Don't correct overlap on new sequence strips

   :type overlap: boolean, (optional)
   :arg scene:

      Scene

   :type scene: enum in [], (optional)

.. function:: select(extend=False, linked_handle=False, left_right='NONE', linked_time=False)

   Select a strip (last selected becomes the "active strip")

   :arg extend:

      Extend, Extend the selection

   :type extend: boolean, (optional)
   :arg linked_handle:

      Linked Handle, Select handles next to the active strip

   :type linked_handle: boolean, (optional)
   :arg left_right:

      Left/Right, Select based on the current frame side the cursor is on

      * ``NONE`` None, Don't do left-right selection.
      * ``MOUSE`` Mouse, Use mouse position for selection.
      * ``LEFT`` Left, Select left.
      * ``RIGHT`` Right, Select right.

   :type left_right: enum in ['NONE', 'MOUSE', 'LEFT', 'RIGHT'], (optional)
   :arg linked_time:

      Linked Time, Select other strips at the same time

   :type linked_time: boolean, (optional)

.. function:: select_active_side(side='BOTH')

   Select strips on the nominated side of the active strip

   :arg side:

      Side, The side of the handle that is selected

   :type side: enum in ['LEFT', 'RIGHT', 'BOTH'], (optional)

.. function:: select_all(action='TOGGLE')

   Select or deselect all strips

   :arg action:

      Action, Selection action to execute

      * ``TOGGLE`` Toggle, Toggle selection for all elements.
      * ``SELECT`` Select, Select all elements.
      * ``DESELECT`` Deselect, Deselect all elements.
      * ``INVERT`` Invert, Invert selection of all elements.

   :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

.. function:: select_border(xmin=0, xmax=0, ymin=0, ymax=0, deselect=False, extend=True)

   Select strips using border selection

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

.. function:: select_grouped(type='TYPE', extend=False, use_active_channel=False)

   Select all strips grouped by various properties

   :arg type:

      Type

      * ``TYPE`` Type, Shared strip type.
      * ``TYPE_BASIC`` Global Type, All strips of same basic type (Graphical or Sound).
      * ``TYPE_EFFECT`` Effect Type, Shared strip effect type (if active strip is not an effect one, select all non-effect strips).
      * ``DATA`` Data, Shared data (scene, image, sound, etc.).
      * ``EFFECT`` Effect, Shared effects.
      * ``EFFECT_LINK`` Effect/Linked, Other strips affected by the active one (sharing some time, and below or effect-assigned).
      * ``OVERLAP`` Overlap, Overlapping time.

   :type type: enum in ['TYPE', 'TYPE_BASIC', 'TYPE_EFFECT', 'DATA', 'EFFECT', 'EFFECT_LINK', 'OVERLAP'], (optional)
   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)
   :arg use_active_channel:

      Same Channel, Only consider strips on the same channel as the active one

   :type use_active_channel: boolean, (optional)

.. function:: select_handles(side='BOTH')

   Select manipulator handles on the sides of the selected strip

   :arg side:

      Side, The side of the handle that is selected

   :type side: enum in ['LEFT', 'RIGHT', 'BOTH'], (optional)

.. function:: select_less()

   Shrink the current selection of adjacent selected strips

.. function:: select_linked()

   Select all strips adjacent to the current selection

.. function:: select_linked_pick(extend=False)

   Select a chain of linked strips nearest to the mouse pointer

   :arg extend:

      Extend, Extend the selection

   :type extend: boolean, (optional)

.. function:: select_more()

   Select more strips adjacent to the current selection

.. function:: slip(offset=0)

   Trim the contents of the active strip

   :arg offset:

      Offset, Offset to the data of the strip

   :type offset: int in [-inf, inf], (optional)

.. function:: snap(frame=0)

   Frame where selected strips will be snapped

   :arg frame:

      Frame, Frame where selected strips will be snapped

   :type frame: int in [-inf, inf], (optional)

.. function:: sound_strip_add(filepath="", files=None, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=True, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', frame_start=0, channel=1, replace_sel=True, overlap=False, cache=False, mono=False)

   Add a sound strip to the sequencer

   :arg filepath:

      File Path, Path to file

   :type filepath: string, (optional, never None)
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
   :arg frame_start:

      Start Frame, Start frame of the sequence strip

   :type frame_start: int in [-inf, inf], (optional)
   :arg channel:

      Channel, Channel to place this strip into

   :type channel: int in [1, 32], (optional)
   :arg replace_sel:

      Replace Selection, Replace the current selection

   :type replace_sel: boolean, (optional)
   :arg overlap:

      Allow Overlap, Don't correct overlap on new sequence strips

   :type overlap: boolean, (optional)
   :arg cache:

      Cache, Cache the sound in memory

   :type cache: boolean, (optional)
   :arg mono:

      Mono, Merge all the sound's channels into one

   :type mono: boolean, (optional)

.. function:: strip_jump(next=True, center=True)

   Move frame to previous edit point

   :arg next:

      Next Strip

   :type next: boolean, (optional)
   :arg center:

      Use strip center

   :type center: boolean, (optional)

.. function:: strip_modifier_add(type='COLOR_BALANCE')

   Add a modifier to the strip

   :arg type:

      Type

   :type type: enum in ['COLOR_BALANCE', 'CURVES', 'HUE_CORRECT', 'BRIGHT_CONTRAST', 'MASK', 'WHITE_BALANCE', 'TONEMAP'], (optional)

.. function:: strip_modifier_copy(type='REPLACE')

   Copy modifiers of the active strip to all selected strips

   :arg type:

      Type

      * ``REPLACE`` Replace, Replace modifiers in destination.
      * ``APPEND`` Append, Append active modifiers to selected strips.

   :type type: enum in ['REPLACE', 'APPEND'], (optional)

.. function:: strip_modifier_move(name="Name", direction='UP')

   Move modifier up and down in the stack

   :arg name:

      Name, Name of modifier to remove

   :type name: string, (optional, never None)
   :arg direction:

      Type

      * ``UP`` Up, Move modifier up in the stack.
      * ``DOWN`` Down, Move modifier down in the stack.

   :type direction: enum in ['UP', 'DOWN'], (optional)

.. function:: strip_modifier_remove(name="Name")

   Remove a modifier from the strip

   :arg name:

      Name, Name of modifier to remove

   :type name: string, (optional, never None)

.. function:: swap(side='RIGHT')

   Swap active strip with strip to the right or left

   :arg side:

      Side, Side of the strip to swap

   :type side: enum in ['LEFT', 'RIGHT'], (optional)

.. function:: swap_data()

   Swap 2 sequencer strips

.. function:: swap_inputs()

   Swap the first two inputs for the effect strip

.. function:: unlock()

   Unlock the active strip so that it can't be transformed

.. function:: unmute(unselected=False)

   Unmute (un)selected strips

   :arg unselected:

      Unselected, Unmute unselected rather than selected strips

   :type unselected: boolean, (optional)

.. function:: view_all()

   View all the strips in the sequencer

.. function:: view_all_preview()

   Zoom preview to fit in the area

.. function:: view_frame()

   Reset viewable area to show range around current frame

.. function:: view_ghost_border(xmin=0, xmax=0, ymin=0, ymax=0)

   Set the boundaries of the border used for offset-view

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

.. function:: view_selected()

   Zoom the sequencer on the selected strips

.. function:: view_toggle()

   Toggle between sequencer views (sequence, preview, both)

.. function:: view_zoom_ratio(ratio=1.0)

   Change zoom ratio of sequencer preview

   :arg ratio:

      Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out

   :type ratio: float in [-inf, inf], (optional)


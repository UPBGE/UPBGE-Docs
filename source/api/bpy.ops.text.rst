Text Operators
==============

.. module:: bpy.ops.text

.. function:: autocomplete()

   Show a list of used text in the open document

.. function:: comment()

   Convert selected text to comment

.. function:: convert_whitespace(type='SPACES')

   Convert whitespaces by type

   :arg type:

      Type, Type of whitespace to convert to

   :type type: enum in ['SPACES', 'TABS'], (optional)

.. function:: copy()

   Copy selected text to clipboard

.. function:: cursor_set(x=0, y=0)

   Set cursor position

   :arg x:

      X

   :type x: int in [-inf, inf], (optional)
   :arg y:

      Y

   :type y: int in [-inf, inf], (optional)

.. function:: cut()

   Cut selected text to clipboard

.. function:: delete(type='NEXT_CHARACTER')

   Delete text by cursor position

   :arg type:

      Type, Which part of the text to delete

   :type type: enum in ['NEXT_CHARACTER', 'PREVIOUS_CHARACTER', 'NEXT_WORD', 'PREVIOUS_WORD'], (optional)

.. function:: duplicate_line()

   Duplicate the current line

.. function:: find()

   Find specified text

.. function:: find_set_selected()

   Find specified text and set as selected

.. function:: indent()

   Indent selected text

.. function:: insert(text="")

   Insert text at cursor position

   :arg text:

      Text, Text to insert at the cursor position

   :type text: string, (optional, never None)

.. function:: jump(line=1)

   Jump cursor to line

   :arg line:

      Line, Line number to jump to

   :type line: int in [1, inf], (optional)

.. function:: line_break()

   Insert line break at cursor position

.. function:: line_number()

   The current line number

.. function:: make_internal()

   Make active text file internal

.. function:: move(type='LINE_BEGIN')

   Move cursor to position type

   :arg type:

      Type, Where to move cursor to

   :type type: enum in ['LINE_BEGIN', 'LINE_END', 'FILE_TOP', 'FILE_BOTTOM', 'PREVIOUS_CHARACTER', 'NEXT_CHARACTER', 'PREVIOUS_WORD', 'NEXT_WORD', 'PREVIOUS_LINE', 'NEXT_LINE', 'PREVIOUS_PAGE', 'NEXT_PAGE'], (optional)

.. function:: move_lines(direction='DOWN')

   Move the currently selected line(s) up/down

   :arg direction:

      Direction

   :type direction: enum in ['UP', 'DOWN'], (optional)

.. function:: move_select(type='LINE_BEGIN')

   Move the cursor while selecting

   :arg type:

      Type, Where to move cursor to, to make a selection

   :type type: enum in ['LINE_BEGIN', 'LINE_END', 'FILE_TOP', 'FILE_BOTTOM', 'PREVIOUS_CHARACTER', 'NEXT_CHARACTER', 'PREVIOUS_WORD', 'NEXT_WORD', 'PREVIOUS_LINE', 'NEXT_LINE', 'PREVIOUS_PAGE', 'NEXT_PAGE'], (optional)

.. function:: new()

   Create a new text data-block

.. function:: open(filepath="", filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=True, filter_font=False, filter_sound=False, filter_text=True, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', internal=False)

   Open a new text data-block

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
   :arg internal:

      Make internal, Make text file internal after loading

   :type internal: boolean, (optional)

.. function:: overwrite_toggle()

   Toggle overwrite while typing

.. function:: paste(selection=False)

   Paste text from clipboard

   :arg selection:

      Selection, Paste text selected elsewhere rather than copied (X11 only)

   :type selection: boolean, (optional)

.. function:: properties()

   Toggle the properties region visibility

.. function:: refresh_pyconstraints()

   Refresh all pyconstraints

.. function:: reload()

   Reload active text data-block from its file

.. function:: replace()

   Replace text with the specified text

.. function:: replace_set_selected()

   Replace text with specified text and set as selected

.. function:: resolve_conflict(resolution='IGNORE')

   When external text is out of sync, resolve the conflict

   :arg resolution:

      Resolution, How to solve conflict due to differences in internal and external text

   :type resolution: enum in ['IGNORE', 'RELOAD', 'SAVE', 'MAKE_INTERNAL'], (optional)

.. function:: run_script()

   Run active script

.. function:: save()

   Save active text data-block

.. function:: save_as(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=True, filter_font=False, filter_sound=False, filter_text=True, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA')

   Save active text file with options

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

.. function:: scroll(lines=1)

   Undocumented

   :arg lines:

      Lines, Number of lines to scroll

   :type lines: int in [-inf, inf], (optional)

.. function:: scroll_bar(lines=1)

   Undocumented

   :arg lines:

      Lines, Number of lines to scroll

   :type lines: int in [-inf, inf], (optional)

.. function:: select_all()

   Select all text

.. function:: select_line()

   Select text by line

.. function:: select_word()

   Select word under cursor

.. function:: selection_set(select=False)

   Set cursor selection

   :arg select:

      Select, Set selection end rather than cursor

   :type select: boolean, (optional)

.. function:: start_find()

   Start searching text

.. function:: to_3d_object(split_lines=False)

   Create 3D text object from active text data-block

   :arg split_lines:

      Split Lines, Create one object per line in the text

   :type split_lines: boolean, (optional)

.. function:: uncomment()

   Convert selected comment to text

.. function:: unindent()

   Unindent selected text

.. function:: unlink()

   Unlink active text data-block


Console Operators
=================

.. module:: bpy.ops.console

.. function:: autocomplete()

   Evaluate the namespace up until the cursor and give a list of options or complete the name if there is only one

   :file: `startup\bl_operators\console.py\:72 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\console.py$72>`_

.. function:: banner()

   Print a message when the terminal initializes

   :file: `startup\bl_operators\console.py\:117 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\console.py$117>`_

.. function:: clear(scrollback=True, history=False)

   Clear text by type

   :arg scrollback:

      Scrollback, Clear the scrollback history

   :type scrollback: boolean, (optional)
   :arg history:

      History, Clear the command history

   :type history: boolean, (optional)

.. function:: clear_line()

   Clear the line and store in history

.. function:: copy()

   Copy selected text to clipboard

.. function:: copy_as_script()

   Copy the console contents for use in a script

   :file: `startup\bl_operators\console.py\:94 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\console.py$94>`_

.. function:: delete(type='NEXT_CHARACTER')

   Delete text by cursor position

   :arg type:

      Type, Which part of the text to delete

   :type type: enum in ['NEXT_CHARACTER', 'PREVIOUS_CHARACTER', 'NEXT_WORD', 'PREVIOUS_WORD'], (optional)

.. function:: execute(interactive=False)

   Execute the current console line as a python expression

   :arg interactive:

      interactive

   :type interactive: boolean, (optional)

   :file: `startup\bl_operators\console.py\:48 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\console.py$48>`_

.. function:: history_append(text="", current_character=0, remove_duplicates=False)

   Append history at cursor position

   :arg text:

      Text, Text to insert at the cursor position

   :type text: string, (optional, never None)
   :arg current_character:

      Cursor, The index of the cursor

   :type current_character: int in [0, inf], (optional)
   :arg remove_duplicates:

      Remove Duplicates, Remove duplicate items in the history

   :type remove_duplicates: boolean, (optional)

.. function:: history_cycle(reverse=False)

   Cycle through history

   :arg reverse:

      Reverse, Reverse cycle history

   :type reverse: boolean, (optional)

.. function:: indent()

   Add 4 spaces at line beginning

.. function:: insert(text="")

   Insert text at cursor position

   :arg text:

      Text, Text to insert at the cursor position

   :type text: string, (optional, never None)

.. function:: language(language="")

   Set the current language for this console

   :arg language:

      Language

   :type language: string, (optional, never None)

   :file: `startup\bl_operators\console.py\:149 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\console.py$149>`_

.. function:: move(type='LINE_BEGIN')

   Move cursor position

   :arg type:

      Type, Where to move cursor to

   :type type: enum in ['LINE_BEGIN', 'LINE_END', 'PREVIOUS_CHARACTER', 'NEXT_CHARACTER', 'PREVIOUS_WORD', 'NEXT_WORD'], (optional)

.. function:: paste()

   Paste text from clipboard

.. function:: scrollback_append(text="", type='OUTPUT')

   Append scrollback text by type

   :arg text:

      Text, Text to insert at the cursor position

   :type text: string, (optional, never None)
   :arg type:

      Type, Console output type

   :type type: enum in ['OUTPUT', 'INPUT', 'INFO', 'ERROR'], (optional)

.. function:: select_set()

   Set the console selection

.. function:: select_word()

   Select word at cursor position

.. function:: unindent()

   Delete 4 spaces from line beginning


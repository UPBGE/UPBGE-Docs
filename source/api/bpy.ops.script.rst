Script Operators
================

.. module:: bpy.ops.script

.. function:: autoexec_warn_clear()

   Ignore autoexec warning

.. function:: execute_preset(filepath="", menu_idname="")

   Execute a preset

   :arg filepath:

      filepath

   :type filepath: string, (optional, never None)
   :arg menu_idname:

      Menu ID Name, ID name of the menu this was called from

   :type menu_idname: string, (optional, never None)

   :file: `startup\bl_operators\presets.py\:217 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\presets.py$217>`_

.. function:: python_file_run(filepath="")

   Run Python file

   :arg filepath:

      Path

   :type filepath: string, (optional, never None)

.. function:: reload()

   Reload Scripts


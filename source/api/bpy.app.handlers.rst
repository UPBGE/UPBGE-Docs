Application Handlers (bpy.app.handlers)
=======================================

.. module:: bpy.app.handlers

This module contains callback lists

Basic Handler Example
+++++++++++++++++++++

This script shows the most simple example of adding a handler.

.. literalinclude:: ..\examples\bpy.app.handlers.py
   :lines: 7-

Persistent Handler Example
++++++++++++++++++++++++++

By default handlers are freed when loading new files, in some cases you may
wan't the handler stay running across multiple files (when the handler is
part of an add-on for example).

For this the :data:`bpy.app.handlers.persistent` decorator needs to be used.

.. literalinclude:: ..\examples\bpy.app.handlers.1.py
   :lines: 11-

.. data:: frame_change_post

   on frame change for playback and rendering (after)


.. data:: frame_change_pre

   on frame change for playback and rendering (before)


.. data:: game_post

   on ending the game engine


.. data:: game_pre

   on starting the game engine


.. data:: load_post

   on loading a new blend file (after)


.. data:: load_pre

   on loading a new blend file (before)


.. data:: render_cancel

   on canceling a render job


.. data:: render_complete

   on completion of render job


.. data:: render_init

   on initialization of a render job


.. data:: render_post

   on render (after)


.. data:: render_pre

   on render (before)


.. data:: render_stats

   on printing render statistics


.. data:: render_write

   on writing a render frame (directly after the frame is written)


.. data:: save_post

   on saving a blend file (after)


.. data:: save_pre

   on saving a blend file (before)


.. data:: scene_update_post

   on every scene data update. Does not imply that anything changed in the scene, just that the dependency graph was reevaluated, and the scene was possibly updated by Blender's animation system.


.. data:: scene_update_pre

   on every scene data update. Does not imply that anything changed in the scene, just that the dependency graph is about to be reevaluated, and the scene is about to be updated by Blender's animation system.


.. data:: version_update

   on ending the versioning code


.. data:: persistent

   Function decorator for callback functions not to be removed when loading new files



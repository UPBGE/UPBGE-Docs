UserPreferencesFilePaths(bpy_struct)
====================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: UserPreferencesFilePaths(bpy_struct)

   Default paths for external files

   .. attribute:: animation_player

      Path to a custom animation/frame sequence player

      :type: string, default "", (never None)

   .. attribute:: animation_player_preset

      Preset configs for external animation players

      * ``INTERNAL`` Internal, Built-in animation player.
      * ``DJV`` Djv, Open source frame player: http://djv.sourceforge.net.
      * ``FRAMECYCLER`` FrameCycler, Frame player from IRIDAS.
      * ``RV`` rv, Frame player from Tweak Software.
      * ``MPLAYER`` MPlayer, Media player for video & png/jpeg/sgi image sequences.
      * ``CUSTOM`` Custom, Custom animation player executable path.

      :type: enum in ['INTERNAL', 'DJV', 'FRAMECYCLER', 'RV', 'MPLAYER', 'CUSTOM'], default 'INTERNAL'

   .. attribute:: auto_save_time

      The time (in minutes) to wait between automatic temporary saves

      :type: int in [1, 60], default 0

   .. attribute:: font_directory

      The default directory to search for loading fonts

      :type: string, default "", (never None)

   .. attribute:: hide_recent_locations

      Hide recent locations in the file selector

      :type: boolean, default False

   .. attribute:: hide_system_bookmarks

      Hide system bookmarks in the file selector

      :type: boolean, default False

   .. attribute:: i18n_branches_directory

      The path to the '/branches' directory of your local svn-translation copy, to allow translating from the UI

      :type: string, default "", (never None)

   .. attribute:: image_editor

      Path to an image editor

      :type: string, default "", (never None)

   .. attribute:: recent_files

      Maximum number of recently opened files to remember

      :type: int in [0, 30], default 0

   .. attribute:: render_cache_directory

      Where to cache raw render results

      :type: string, default "", (never None)

   .. attribute:: render_output_directory

      The default directory for rendering output, for new scenes

      :type: string, default "", (never None)

   .. attribute:: save_version

      The number of old versions to maintain in the current directory, when manually saving

      :type: int in [0, 32], default 0

   .. attribute:: script_directory

      Alternate script path, matching the default layout with subdirs: startup, add-ons & modules (requires restart)

      :type: string, default "", (never None)

   .. attribute:: show_hidden_files_datablocks

      Hide files/data-blocks that start with a dot (.*)

      :type: boolean, default False

   .. attribute:: show_thumbnails

      Open in thumbnail view for images and movies

      :type: boolean, default False

   .. attribute:: sound_directory

      The default directory to search for sounds

      :type: string, default "", (never None)

   .. attribute:: temporary_directory

      The directory for storing temporary save files

      :type: string, default "", (never None)

   .. attribute:: texture_directory

      The default directory to search for textures

      :type: string, default "", (never None)

   .. attribute:: use_auto_save_temporary_files

      Automatic saving of temporary files in temp directory, uses process ID (Sculpt or edit mode data won't be saved!')

      :type: boolean, default False

   .. attribute:: use_file_compression

      Enable file compression when saving .blend files

      :type: boolean, default False

   .. attribute:: use_filter_files

      Display only files with extensions in the image select window

      :type: boolean, default False

   .. attribute:: use_keep_session

      Always load session recovery and save it after quitting Blender

      :type: boolean, default False

   .. attribute:: use_load_ui

      Load user interface setup when loading .blend files

      :type: boolean, default False

   .. attribute:: use_relative_paths

      Default relative path option for the file selector

      :type: boolean, default False

   .. attribute:: use_save_preview_images

      Enables automatic saving of preview images in the .blend file

      :type: boolean, default False

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

   * :class:`UserPreferences.filepaths`


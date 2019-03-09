Application Data (bpy.app)
==========================

.. module:: bpy.app

This module contains application values that remain unchanged during runtime.

Submodules:

.. toctree::
   :maxdepth: 1

   bpy.app.handlers.rst
   bpy.app.translations.rst

.. attribute:: autoexec_fail

   Undocumented


.. attribute:: autoexec_fail_message

   Undocumented


.. attribute:: autoexec_fail_quiet

   Undocumented


.. attribute:: binary_path_python

   String, the path to the python executable (read-only)


.. attribute:: debug

   Boolean, for debug info (started with --debug / --debug_* matching this attribute name)


.. attribute:: debug_depsgraph

   Boolean, for debug info (started with --debug / --debug_* matching this attribute name)


.. attribute:: debug_events

   Boolean, for debug info (started with --debug / --debug_* matching this attribute name)


.. attribute:: debug_ffmpeg

   Boolean, for debug info (started with --debug / --debug_* matching this attribute name)


.. attribute:: debug_freestyle

   Boolean, for debug info (started with --debug / --debug_* matching this attribute name)


.. attribute:: debug_gpumem

   Boolean, for debug info (started with --debug / --debug_* matching this attribute name)


.. attribute:: debug_handlers

   Boolean, for debug info (started with --debug / --debug_* matching this attribute name)


.. attribute:: debug_python

   Boolean, for debug info (started with --debug / --debug_* matching this attribute name)


.. attribute:: debug_simdata

   Boolean, for debug info (started with --debug / --debug_* matching this attribute name)


.. attribute:: debug_value

   Int, number which can be set to non-zero values for testing purposes


.. attribute:: debug_wm

   Boolean, for debug info (started with --debug / --debug_* matching this attribute name)


.. attribute:: driver_namespace

   Dictionary for drivers namespace, editable in-place, reset on file load (read-only)


.. attribute:: render_icon_size

   Reference size for icon/preview renders (read-only)


.. attribute:: render_preview_size

   Reference size for icon/preview renders (read-only)


.. attribute:: tempdir

   String, the temp directory used by blender (read-only)


.. data:: background

   Boolean, True when blender is running without a user interface (started with -b)


.. data:: factory_startup

   Boolean, True when blender is running with --factory-startup)


.. data:: translations

   Application and addons internationalization API


.. data:: build_branch

   The branch this blender instance was built from


.. data:: build_cflags

   C compiler flags


.. data:: build_commit_date

   The date of commit this blender instance was built


.. data:: build_commit_time

   The time of commit this blender instance was built


.. data:: build_cxxflags

   C++ compiler flags


.. data:: build_date

   The date this blender instance was built


.. data:: build_hash

   The commit hash this blender instance was built with


.. data:: build_linkflags

   Binary linking flags


.. data:: build_platform

   The platform this blender instance was built for


.. data:: build_system

   Build system used


.. data:: build_time

   The time this blender instance was built


.. data:: build_type

   The type of build (Release, Debug)


.. data:: build_commit_timestamp

   The unix timestamp of commit this blender instance was built


.. data:: binary_path

   The location of blenders executable, useful for utilities that spawn new instances


.. data:: version_char

   The Blender version character (for minor releases)


.. data:: version_cycle

   The release status of this build alpha/beta/rc/release


.. data:: version_string

   The Blender version formatted as a string


.. data:: version

   The Blender version as a tuple of 3 numbers. eg. (2, 50, 11)


.. data:: alembic

   constant value bpy.app.alembic(supported=True, version=(1, 7, 1), version_string=' 1,  7,  1')

.. data:: build_options

   constant value bpy.app.build_options(bullet=True, codec_avi=True, codec_ffmpeg=True, codec_sndfile=True, compositor=True, cycles=True, cycles_osl=True, freestyle=True, gameengine=True, image_cineon=True, image_dds=True, image_frameserver=True, image_hdr=True, image_openexr=True, image_openjpeg=True, image_tiff=True, input_ndof=True, audaspace=True, international=True, openal=True, sdl=True, sdl_dynload=False, jack=False, libmv=True, mod_boolean=True, mod_fluid=True, mod_oceansim=True, mod_remesh=True, ...)

.. data:: ffmpeg

   constant value bpy.app.ffmpeg(supported=True, avcodec_version=(57, 64, 101), avcodec_version_string='57, 64, 101', avdevice_version=(57, 1, 100), avdevice_version_string='57,  1, 100', avformat_version=(57, 56, 100), avformat_version_string='57, 56, 100', avutil_version=(55, 34, 100), avutil_version_string='55, 34, 100', swscale_version=(4, 2, 100), swscale_version_string=' 4,  2, 100')

.. data:: handlers

   constant value bpy.app.handlers(frame_change_pre=[], frame_change_post=[], render_pre=[], render_post=[], render_write=[], render_stats=[], render_init=[], render_complete=[], render_cancel=[], load_pre=[], load_post=[], save_pre=[], save_post=[], scene_update_pre=[], scene_update_post=[], game_pre=[], game_post=[], version_update=[<function do_versions at 0x0877B198>], persistent=<class 'persistent'>)

.. data:: ocio

   constant value bpy.app.ocio(supported=True, version=(1, 0, 9), version_string=' 1,  0,  9')

.. data:: oiio

   constant value bpy.app.oiio(supported=True, version=(1, 7, 15), version_string=' 1,  7, 15')

.. data:: opensubdiv

   constant value bpy.app.opensubdiv(supported=True, version=(3, 1, 1), version_string=' 3,  1,  1')

.. data:: openvdb

   constant value bpy.app.openvdb(supported=True, version=(3, 1, 0), version_string=' 3,  1,  0')

.. data:: sdl

   constant value bpy.app.sdl(supported=True, version=(2, 0, 4), version_string='2.0.4', available=True)


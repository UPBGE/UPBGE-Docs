Utilities (bpy.utils)
=====================

.. module:: bpy.utils

This module contains utility functions specific to blender but
not associated with blenders internal data.

.. toctree::
   :maxdepth: 1
   :glob:

   bpy.utils.previews.rst
   bpy.utils.units.rst

.. function:: blend_paths(absolute=False, packed=False, local=False)

   Returns a list of paths to external files referenced by the loaded .blend file.

   :arg absolute: When true the paths returned are made absolute.
   :type absolute: boolean
   :arg packed: When true skip file paths for packed data.
   :type packed: boolean
   :arg local: When true skip linked library paths.
   :type local: boolean
   :return: path list.
   :rtype: list of strings


.. function:: escape_identifier(string)

   Simple string escaping function used for animation paths.

   :arg string: text
   :type string: string
   :return: The escaped string.
   :rtype: string


.. method:: register_class(cls)

   Register a subclass of a blender type in (:class:`bpy.types.Panel`,
   :class:`bpy.types.UIList`, :class:`bpy.types.Menu`, :class:`bpy.types.Header`,
   :class:`bpy.types.Operator`, :class:`bpy.types.KeyingSetInfo`,
   :class:`bpy.types.RenderEngine`).

   If the class has a *register* class method it will be called
   before registration.

   .. note::

      :exc:`ValueError` exception is raised if the class is not a
      subclass of a registerable blender class.


.. function:: resource_path(type, major=bpy.app.version[0], minor=bpy.app.version[1])

   Return the base path for storing system files.

   :arg type: string in ['USER', 'LOCAL', 'SYSTEM'].
   :type type: string
   :arg major: major version, defaults to current.
   :type major: int
   :arg minor: minor version, defaults to current.
   :type minor: string
   :return: the resource path (not necessarily existing).
   :rtype: string


.. method:: unregister_class(cls)

   Unload the python class from blender.

   If the class has an *unregister* class method it will be called
   before unregistering.


.. function:: keyconfig_set(filepath, report=None)

.. function:: load_scripts(reload_scripts=False, refresh_scripts=False)

   Load scripts and run each modules register function.
   
   :arg reload_scripts: Causes all scripts to have their unregister method
      called before loading.
   :type reload_scripts: bool
   :arg refresh_scripts: only load scripts which are not already loaded
      as modules.
   :type refresh_scripts: bool

.. function:: modules_from_path(path, loaded_modules)

   Load all modules in a path and return them as a list.
   
   :arg path: this path is scanned for scripts and packages.
   :type path: string
   :arg loaded_modules: already loaded module names, files matching these
      names will be ignored.
   :type loaded_modules: set
   :return: all loaded modules.
   :rtype: list

.. function:: preset_find(name, preset_path, display_name=False, ext='.py')

.. function:: preset_paths(subdir)

   Returns a list of paths for a specific preset.
   
   :arg subdir: preset subdirectory (must not be an absolute path).
   :type subdir: string
   :return: script paths.
   :rtype: list

.. function:: refresh_script_paths()

   Run this after creating new script paths to update sys.path

.. function:: app_template_paths(subdir=None)

   Returns valid application template paths.
   
   :arg subdir: Optional subdir.
   :type subdir: string
   :return: app template paths.
   :rtype: generator

.. function:: register_module(module, verbose=False)

.. function:: register_manual_map(manual_hook)

.. function:: unregister_manual_map(manual_hook)

.. function:: register_classes_factory(classes)

   Utility function to create register and unregister functions
   which simply registers and unregisters a sequence of classes.

.. function:: register_submodule_factory(module_name, submodule_names)

   Utility function to create register and unregister functions
   which simply load submodules,
   calling their register & unregister functions.
   
   .. note::
   
      Modules are registered in the order given,
      unregistered in reverse order.
   
   :arg module_name: The module name, typically ``__name__``.
   :type module_name: string
   :arg submodule_names: List of submodule names to load and unload.
   :type submodule_names: list of strings
   :return: register and unregister functions.
   :rtype: tuple pair of functions

.. function:: make_rna_paths(struct_name, prop_name, enum_name)

   Create RNA "paths" from given names.
   
   :arg struct_name: Name of a RNA struct (like e.g. "Scene").
   :type struct_name: string
   :arg prop_name: Name of a RNA struct's property.
   :type prop_name: string
   :arg enum_name: Name of a RNA enum identifier.
   :type enum_name: string
   :return: A triple of three "RNA paths"
      (most_complete_path, "struct.prop", "struct.prop:'enum'").
      If no enum_name is given, the third element will always be void.
   :rtype: tuple of strings

.. function:: manual_map()

.. function:: script_path_user()

   returns the env var and falls back to home dir or None

.. function:: script_path_pref()

   returns the user preference or None

.. function:: script_paths(subdir=None, user_pref=True, check_all=False, use_user=True)

   Returns a list of valid script paths.
   
   :arg subdir: Optional subdir.
   :type subdir: string
   :arg user_pref: Include the user preference script path.
   :type user_pref: bool
   :arg check_all: Include local, user and system paths rather just the paths
      blender uses.
   :type check_all: bool
   :return: script paths.
   :rtype: list

.. function:: smpte_from_frame(frame, fps=None, fps_base=None)

   Returns an SMPTE formatted string from the *frame*:
   ``HH:MM:SS:FF``.
   
   If *fps* and *fps_base* are not given the current scene is used.
   
   :arg frame: frame number.
   :type frame: int or float.
   :return: the frame string.
   :rtype: string

.. function:: smpte_from_seconds(time, fps=None)

   Returns an SMPTE formatted string from the *time*:
   ``HH:MM:SS:FF``.
   
   If the *fps* is not given the current scene is used.
   
   :arg time: time in seconds.
   :type time: int, float or ``datetime.timedelta``.
   :return: the frame string.
   :rtype: string

.. function:: unregister_module(module, verbose=False)

.. function:: user_resource(resource_type, path='', create=False)

   Return a user resource path (normally from the users home directory).
   
   :arg type: Resource type in ['DATAFILES', 'CONFIG', 'SCRIPTS', 'AUTOSAVE'].
   :type type: string
   :arg subdir: Optional subdirectory.
   :type subdir: string
   :arg create: Treat the path as a directory and create
      it if its not existing.
   :type create: boolean
   :return: a path.
   :rtype: string


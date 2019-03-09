UserPreferences(bpy_struct)
===========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: UserPreferences(bpy_struct)

   Global user preferences

   .. attribute:: active_section

      Active section of the user preferences shown in the user interface

      :type: enum in ['INTERFACE', 'EDITING', 'INPUT', 'ADDONS', 'THEMES', 'FILES', 'SYSTEM'], default 'INTERFACE'

   .. data:: addons

      :type: :class:`Addons` :class:`bpy_prop_collection` of :class:`Addon`, (readonly)

   .. attribute:: app_template

      :type: string, default "", (never None)

   .. data:: autoexec_paths

      :type: :class:`PathCompareCollection` :class:`bpy_prop_collection` of :class:`PathCompare`, (readonly)

   .. data:: edit

      Settings for interacting with Blender data

      :type: :class:`UserPreferencesEdit`, (readonly, never None)

   .. data:: filepaths

      Default paths for external files

      :type: :class:`UserPreferencesFilePaths`, (readonly, never None)

   .. data:: inputs

      Settings for input devices

      :type: :class:`UserPreferencesInput`, (readonly, never None)

   .. data:: system

      Graphics driver and operating system settings

      :type: :class:`UserPreferencesSystem`, (readonly, never None)

   .. data:: themes

      :type: :class:`bpy_prop_collection` of :class:`Theme`, (readonly)

   .. data:: ui_styles

      :type: :class:`bpy_prop_collection` of :class:`ThemeStyle`, (readonly)

   .. data:: version

      Version of Blender the userpref.blend was saved with

      :type: int array of 3 items in [0, inf], default (0, 0, 0), (readonly)

   .. data:: view

      Preferences related to viewing data

      :type: :class:`UserPreferencesView`, (readonly, never None)

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

   * :class:`Context.user_preferences`


KeyingSet(bpy_struct)
=====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: KeyingSet(bpy_struct)

   Settings that should be keyframed together

   .. attribute:: bl_description

      A short description of the keying set

      :type: string, default "", (never None)

   .. attribute:: bl_idname

      If this is set, the Keying Set gets a custom ID, otherwise it takes the name of the class used to define the Keying Set (for example, if the class name is "BUILTIN_KSI_location", and bl_idname is not set by the script, then bl_idname = "BUILTIN_KSI_location")

      :type: string, default "", (never None)

   .. attribute:: bl_label

      :type: string, default "", (never None)

   .. data:: is_path_absolute

      Keying Set defines specific paths/settings to be keyframed (i.e. is not reliant on context info)

      :type: boolean, default False, (readonly)

   .. data:: paths

      Keying Set Paths to define settings that get keyframed together

      :type: :class:`KeyingSetPaths` :class:`bpy_prop_collection` of :class:`KeyingSetPath`, (readonly)

   .. data:: type_info

      Callback function defines for built-in Keying Sets

      :type: :class:`KeyingSetInfo`, (readonly)

   .. attribute:: use_insertkey_needed

      Only insert keyframes where they're needed in the relevant F-Curves

      :type: boolean, default False

   .. attribute:: use_insertkey_override_needed

      Override default setting to only insert keyframes where they're needed in the relevant F-Curves

      :type: boolean, default False

   .. attribute:: use_insertkey_override_visual

      Override default setting to insert keyframes based on 'visual transforms'

      :type: boolean, default False

   .. attribute:: use_insertkey_override_xyz_to_rgb

      Override default setting to set color for newly added transformation F-Curves (Location, Rotation, Scale) to be based on the transform axis

      :type: boolean, default False

   .. attribute:: use_insertkey_visual

      Insert keyframes based on 'visual transforms'

      :type: boolean, default False

   .. attribute:: use_insertkey_xyz_to_rgb

      Color for newly added transformation F-Curves (Location, Rotation, Scale) is based on the transform axis

      :type: boolean, default False

   .. method:: refresh()

      Refresh Keying Set to ensure that it is valid for the current context (call before each use of one)


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

   * :class:`KeyingSetInfo.generate`
   * :class:`KeyingSetInfo.iterator`
   * :class:`KeyingSets.active`
   * :class:`KeyingSets.new`
   * :class:`KeyingSetsAll.active`
   * :class:`Scene.keying_sets`
   * :class:`Scene.keying_sets_all`


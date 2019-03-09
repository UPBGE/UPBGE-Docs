KeyingSetPaths(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: KeyingSetPaths(bpy_struct)

   Collection of keying set paths

   .. attribute:: active

      Active Keying Set used to insert/delete keyframes

      :type: :class:`KeyingSetPath`

   .. attribute:: active_index

      Current Keying Set index

      :type: int in [-inf, inf], default 0

   .. method:: add(target_id, data_path, index=-1, group_method='KEYINGSET', group_name="")

      Add a new path for the Keying Set

      :arg target_id:

         Target ID, ID data-block for the destination

      :type target_id: :class:`ID`
      :arg data_path:

         Data-Path, RNA-Path to destination property

      :type data_path: string, (never None)
      :arg index:

         Index, The index of the destination property (i.e. axis of Location/Rotation/etc.), or -1 for the entire array

      :type index: int in [-1, inf], (optional)
      :arg group_method:

         Grouping Method, Method used to define which Group-name to use

      :type group_method: enum in ['NAMED', 'NONE', 'KEYINGSET'], (optional)
      :arg group_name:

         Group Name, Name of Action Group to assign destination to (only if grouping mode is to use this name)

      :type group_name: string, (optional, never None)
      :return:

         New Path, Path created and added to the Keying Set

      :rtype: :class:`KeyingSetPath`

   .. method:: remove(path)

      Remove the given path from the Keying Set

      :arg path:

         Path

      :type path: :class:`KeyingSetPath`, (never None)

   .. method:: clear()

      Remove all the paths from the Keying Set


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

   * :class:`KeyingSet.paths`


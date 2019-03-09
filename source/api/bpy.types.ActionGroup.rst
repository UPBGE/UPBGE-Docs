ActionGroup(bpy_struct)
=======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ActionGroup(bpy_struct)

   Groups of F-Curves

   .. data:: channels

      F-Curves in this group

      :type: :class:`bpy_prop_collection` of :class:`FCurve`, (readonly)

   .. attribute:: color_set

      Custom color set to use

      :type: enum in ['DEFAULT', 'THEME01', 'THEME02', 'THEME03', 'THEME04', 'THEME05', 'THEME06', 'THEME07', 'THEME08', 'THEME09', 'THEME10', 'THEME11', 'THEME12', 'THEME13', 'THEME14', 'THEME15', 'THEME16', 'THEME17', 'THEME18', 'THEME19', 'THEME20', 'CUSTOM'], default 'DEFAULT'

   .. data:: colors

      Copy of the colors associated with the group's color set

      :type: :class:`ThemeBoneColorSet`, (readonly, never None)

   .. data:: is_custom_color_set

      Color set is user-defined instead of a fixed theme color set

      :type: boolean, default False, (readonly)

   .. attribute:: lock

      Action group is locked

      :type: boolean, default False

   .. attribute:: name

      :type: string, default "", (never None)

   .. attribute:: select

      Action group is selected

      :type: boolean, default False

   .. attribute:: show_expanded

      Action group is expanded

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

   * :class:`Action.groups`
   * :class:`ActionGroups.new`
   * :class:`ActionGroups.remove`
   * :class:`FCurve.group`


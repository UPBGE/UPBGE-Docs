SpaceUserPreferences(Space)
===========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceUserPreferences(Space)

   User preferences space data

   .. attribute:: filter_text

      Search term for filtering in the UI

      :type: string, default "", (never None)

   .. attribute:: filter_type

      Filter method

      * ``NAME`` Name, Filter based on the operator name.
      * ``KEY`` Key-Binding, Filter based on key bindings.

      :type: enum in ['NAME', 'KEY'], default 'NAME'

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


   .. function:: draw_handler_add()

      Undocumented
   .. function:: draw_handler_remove()

      Undocumented
.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Space.type`
   * :class:`Space.show_locked_time`

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


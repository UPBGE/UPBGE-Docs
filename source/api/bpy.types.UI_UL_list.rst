UI_UL_list(UIList)
==================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`UIList`

.. class:: UI_UL_list(UIList)

   

   .. staticmethod:: filter_items_by_name(pattern, bitflag, items, propname='name', flags=None, reverse=False)

      Set FILTER_ITEM for items which name matches filter_name one (case-insensitive).
      pattern is the filtering pattern.
      propname is the name of the string property to use for filtering.
      flags must be a list of integers the same length as items, or None!
      return a list of flags (based on given flags if not None),
      or an empty list if no flags were given and no filtering has been done.

   .. staticmethod:: sort_items_helper(sort_data, key, reverse=False)

      Common sorting utility. Returns a neworder list mapping org_idx -> new_idx.
      sort_data must be an (unordered) list of tuples [(org_idx, ...), (org_idx, ...), ...].
      key must be the same kind of callable you would use for sorted() builtin function.
      reverse will reverse the sorting!

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
   * :class:`UIList.bl_idname`
   * :class:`UIList.layout_type`
   * :class:`UIList.use_filter_show`
   * :class:`UIList.filter_name`
   * :class:`UIList.use_filter_invert`
   * :class:`UIList.use_filter_sort_alpha`
   * :class:`UIList.use_filter_sort_reverse`
   * :class:`UIList.bitflag_filter_item`

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
   * :class:`UIList.draw_item`
   * :class:`UIList.draw_filter`
   * :class:`UIList.filter_items`
   * :class:`UIList.append`
   * :class:`UIList.is_extended`
   * :class:`UIList.prepend`
   * :class:`UIList.remove`


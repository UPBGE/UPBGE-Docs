NODE_UL_interface_sockets(UIList)
=================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`UIList`

.. class:: NODE_UL_interface_sockets(UIList)

   

   .. method:: draw_item(context, layout, data, item, icon, active_data, active_propname, index)

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


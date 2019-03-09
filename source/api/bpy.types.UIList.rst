UIList(bpy_struct)
==================

.. module:: bpy.types

Basic UIList Example
++++++++++++++++++++

This script is the UIList subclass used to show material slots, with a bunch of additional commentaries.

Notice the name of the class, this naming convention is similar as the one for panels or menus.

.. note::

   UIList subclasses must be registered for blender to use them.

.. literalinclude:: ..\examples\bpy.types.UIList.1.py
   :lines: 13-

Advanced UIList Example - Filtering and Reordering
++++++++++++++++++++++++++++++++++++++++++++++++++

This script is an extended version of the ``UIList`` subclass used to show vertex groups. It is not used 'as is',
because iterating over all vertices in a 'draw' function is a very bad idea for UI performances! However, it's a good
example of how to create/use filtering/reordering callbacks.

.. literalinclude:: ..\examples\bpy.types.UIList.2.py
   :lines: 9-

base class --- :class:`bpy_struct`

subclasses --- 
:class:`CLIP_UL_tracking_objects`, :class:`FILEBROWSER_UL_dir`, :class:`GPENCIL_UL_brush`, :class:`GPENCIL_UL_layer`, :class:`GPENCIL_UL_palettecolor`, :class:`MASK_UL_layers`, :class:`MATERIAL_UL_matslots`, :class:`MESH_UL_shape_keys`, :class:`MESH_UL_uvmaps_vcols`, :class:`MESH_UL_vgroups`, :class:`NODE_UL_interface_sockets`, :class:`PARTICLE_UL_particle_systems`, :class:`PHYSICS_UL_dynapaint_surfaces`, :class:`RENDERLAYER_UL_linesets`, :class:`RENDERLAYER_UL_renderlayers`, :class:`RENDERLAYER_UL_renderviews`, :class:`SCENE_UL_keying_set_paths`, :class:`TEXTURE_UL_texpaintslots`, :class:`TEXTURE_UL_texslots`, :class:`UI_UL_list`

.. class:: UIList(bpy_struct)

   UI list containing the elements of a collection

   .. data:: bitflag_filter_item

      The value of the reserved bitflag 'FILTER_ITEM' (in filter_flags values)

      :type: int in [0, inf], default 0, (readonly)

   .. attribute:: bl_idname

      If this is set, the uilist gets a custom ID, otherwise it takes the name of the class used to define the uilist (for example, if the class name is "OBJECT_UL_vgroups", and bl_idname is not set by the script, then bl_idname = "OBJECT_UL_vgroups")

      :type: string, default "", (never None)

   .. attribute:: filter_name

      Only show items matching this name (use '*' as wildcard)

      :type: string, default "", (never None)

   .. data:: layout_type

      * ``DEFAULT`` Default Layout, Use the default, multi-rows layout.
      * ``COMPACT`` Compact Layout, Use the compact, single-row layout.
      * ``GRID`` Grid Layout, Use the grid-based layout.

      :type: enum in ['DEFAULT', 'COMPACT', 'GRID'], default 'DEFAULT', (readonly)

   .. attribute:: use_filter_invert

      Invert filtering (show hidden items, and vice-versa)

      :type: boolean, default False

   .. attribute:: use_filter_show

      Show filtering options

      :type: boolean, default False

   .. attribute:: use_filter_sort_alpha

      Sort items by their name

      :type: boolean, default False

   .. attribute:: use_filter_sort_reverse

      Invert the order of shown items

      :type: boolean, default False

   .. method:: draw_item(context, layout, data, item, icon, active_data, active_property, index=0, flt_flag=0)

      Draw an item in the list (NOTE: when you define your own draw_item function, you may want to check given 'item' is of the right type...)

      :type context: :class:`Context`
      :arg layout:

         Layout to draw the item

      :type layout: :class:`UILayout`, (never None)
      :arg data:

         Data from which to take Collection property

      :type data: :class:`AnyType`
      :arg item:

         Item of the collection property

      :type item: :class:`AnyType`
      :arg icon:

         Icon of the item in the collection

      :type icon: int in [0, inf]
      :arg active_data:

         Data from which to take property for the active element

      :type active_data: :class:`AnyType`, (never None)
      :arg active_property:

         Identifier of property in active_data, for the active element

      :type active_property: string, (optional argument, never None)
      :arg index:

         Index of the item in the collection

      :type index: int in [0, inf], (optional)
      :arg flt_flag:

         The filter-flag result for this item

      :type flt_flag: int in [0, inf], (optional)

   .. method:: draw_filter(context, layout)

      Draw filtering options

      :type context: :class:`Context`
      :arg layout:

         Layout to draw the item

      :type layout: :class:`UILayout`, (never None)

   .. method:: filter_items(context, data, property)

      Filter and/or re-order items of the collection (output filter results in filter_flags, and reorder results in filter_neworder arrays)

      :type context: :class:`Context`
      :arg data:

         Data from which to take Collection property

      :type data: :class:`AnyType`
      :arg property:

         Identifier of property in data, for the collection

      :type property: string, (never None)
      :return (filter_flags, filter_neworder):
         `filter_flags`, An array of filter flags, one for each item in the collection (NOTE: FILTER_ITEM bit is reserved, it defines whether the item is shown or not), int array of 1 items in [0, inf]

         `filter_neworder`, An array of indices, one for each item in the collection, mapping the org index to the new one, int array of 1 items in [0, inf]


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


ThemeWidgetColors(bpy_struct)
=============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ThemeWidgetColors(bpy_struct)

   Theme settings for widget color sets

   .. attribute:: inner

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: inner_sel

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: item

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: outline

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: shadedown

      :type: int in [-100, 100], default 0

   .. attribute:: shadetop

      :type: int in [-100, 100], default 0

   .. attribute:: show_shaded

      :type: boolean, default False

   .. attribute:: text

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: text_sel

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

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

   * :class:`ThemeUserInterface.wcol_box`
   * :class:`ThemeUserInterface.wcol_list_item`
   * :class:`ThemeUserInterface.wcol_menu`
   * :class:`ThemeUserInterface.wcol_menu_back`
   * :class:`ThemeUserInterface.wcol_menu_item`
   * :class:`ThemeUserInterface.wcol_num`
   * :class:`ThemeUserInterface.wcol_numslider`
   * :class:`ThemeUserInterface.wcol_option`
   * :class:`ThemeUserInterface.wcol_pie_menu`
   * :class:`ThemeUserInterface.wcol_progress`
   * :class:`ThemeUserInterface.wcol_pulldown`
   * :class:`ThemeUserInterface.wcol_radio`
   * :class:`ThemeUserInterface.wcol_regular`
   * :class:`ThemeUserInterface.wcol_scroll`
   * :class:`ThemeUserInterface.wcol_text`
   * :class:`ThemeUserInterface.wcol_toggle`
   * :class:`ThemeUserInterface.wcol_tool`
   * :class:`ThemeUserInterface.wcol_tooltip`


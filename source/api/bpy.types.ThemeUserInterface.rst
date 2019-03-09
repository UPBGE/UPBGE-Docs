ThemeUserInterface(bpy_struct)
==============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ThemeUserInterface(bpy_struct)

   Theme settings for user interface elements

   .. attribute:: axis_x

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: axis_y

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: axis_z

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: icon_alpha

      Transparency of icons in the interface, to reduce contrast

      :type: float in [0, 1], default 0.0

   .. attribute:: icon_file

      :type: string, default "", (never None)

   .. attribute:: menu_shadow_fac

      Blending factor for menu shadows

      :type: float in [0.01, 1], default 0.0

   .. attribute:: menu_shadow_width

      Width of menu shadows, set to zero to disable

      :type: int in [0, 24], default 0

   .. data:: wcol_box

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_list_item

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_menu

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_menu_back

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_menu_item

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_num

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_numslider

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_option

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_pie_menu

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_progress

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_pulldown

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_radio

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_regular

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_scroll

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_state

      :type: :class:`ThemeWidgetStateColors`, (readonly, never None)

   .. data:: wcol_text

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_toggle

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_tool

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_tooltip

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. attribute:: widget_emboss

      Color of the 1px shadow line underlying widgets

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

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

   * :class:`Theme.user_interface`


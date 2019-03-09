ThemeFontStyle(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ThemeFontStyle(bpy_struct)

   Theme settings for Font

   .. attribute:: font_kerning_style

      Which style to use for font kerning

      * ``UNFITTED`` Unfitted, Use scaled but un-grid-fitted kerning distances.
      * ``FITTED`` Fitted, Use scaled and grid-fitted kerning distances.

      :type: enum in ['UNFITTED', 'FITTED'], default 'UNFITTED'

   .. attribute:: points

      :type: int in [6, 48], default 0

   .. attribute:: shadow

      Shadow size (0, 3 and 5 supported)

      :type: int in [0, 5], default 0

   .. attribute:: shadow_alpha

      :type: float in [0, 1], default 0.0

   .. attribute:: shadow_offset_x

      Shadow offset in pixels

      :type: int in [-10, 10], default 0

   .. attribute:: shadow_offset_y

      Shadow offset in pixels

      :type: int in [-10, 10], default 0

   .. attribute:: shadow_value

      Shadow color in gray value

      :type: float in [0, 1], default 0.0

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

   * :class:`ThemeStyle.panel_title`
   * :class:`ThemeStyle.widget`
   * :class:`ThemeStyle.widget_label`


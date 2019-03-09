GPencilPaletteColor(bpy_struct)
===============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GPencilPaletteColor(bpy_struct)

   Collection of related colors

   .. attribute:: alpha

      Color Opacity

      :type: float in [0, 1], default 0.0

   .. attribute:: color

      Color for strokes

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: fill_alpha

      Opacity for filling region bounded by each stroke

      :type: float in [0, 1], default 0.0

   .. attribute:: fill_color

      Color for filling region bounded by each stroke

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: ghost

      Display strokes using this color when showing onion skins

      :type: boolean, default False

   .. attribute:: hide

      Set color Visibility

      :type: boolean, default False

   .. data:: is_fill_visible

      True when opacity of fill is set high enough to be visible

      :type: boolean, default False, (readonly)

   .. data:: is_stroke_visible

      True when opacity of stroke is set high enough to be visible

      :type: boolean, default False, (readonly)

   .. attribute:: lock

      Protect color from further editing and/or frame changes

      :type: boolean, default False

   .. attribute:: name

      Color name

      :type: string, default "", (never None)

   .. attribute:: use_hq_fill

      Fill strokes using high quality to avoid glitches (slower fps during animation play)

      :type: boolean, default False

   .. attribute:: use_volumetric_strokes

      Draw strokes as a series of circular blobs, resulting in a volumetric effect

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

   * :mod:`bpy.context.active_gpencil_palettecolor`
   * :class:`GPencilPalette.colors`
   * :class:`GPencilPaletteColors.active`
   * :class:`GPencilPaletteColors.new`
   * :class:`GPencilPaletteColors.remove`
   * :class:`GPencilStroke.color`


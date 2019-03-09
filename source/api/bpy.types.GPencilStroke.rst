GPencilStroke(bpy_struct)
=========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GPencilStroke(bpy_struct)

   Freehand curve defining part of a sketch

   .. data:: color

      Color from palette used in Stroke

      :type: :class:`GPencilPaletteColor`, (readonly)

   .. attribute:: colorname

      Palette color name

      :type: string, default "", (never None)

   .. attribute:: draw_cyclic

      Enable cyclic drawing, closing the stroke

      :type: boolean, default False

   .. attribute:: draw_mode

      * ``SCREEN`` Screen, Stroke is in screen-space.
      * ``3DSPACE`` 3D Space, Stroke is in 3D-space.
      * ``2DSPACE`` 2D Space, Stroke is in 2D-space.
      * ``2DIMAGE`` 2D Image, Stroke is in 2D-space (but with special 'image' scaling).

      :type: enum in ['SCREEN', '3DSPACE', '2DSPACE', '2DIMAGE'], default 'SCREEN'

   .. attribute:: line_width

      Thickness of stroke (in pixels)

      :type: int in [1, 300], default 0

   .. data:: points

      Stroke data points

      :type: :class:`GPencilStrokePoints` :class:`bpy_prop_collection` of :class:`GPencilStrokePoint`, (readonly)

   .. attribute:: select

      Stroke is selected for viewport editing

      :type: boolean, default False

   .. data:: triangles

      Triangulation data for HQ fill

      :type: :class:`bpy_prop_collection` of :class:`GPencilTriangle`, (readonly)

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

   * :mod:`bpy.context.editable_gpencil_strokes`
   * :class:`GPencilFrame.strokes`
   * :class:`GPencilStrokes.new`
   * :class:`GPencilStrokes.remove`


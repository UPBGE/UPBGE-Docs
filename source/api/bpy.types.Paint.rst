Paint(bpy_struct)
=================

.. module:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`ImagePaint`, :class:`Sculpt`, :class:`UvSculpt`, :class:`VertexPaint`

.. class:: Paint(bpy_struct)

   

   .. attribute:: brush

      Active Brush

      :type: :class:`Brush`

   .. data:: cavity_curve

      Editable cavity curve

      :type: :class:`CurveMapping`, (readonly, never None)

   .. attribute:: input_samples

      Average multiple input samples together to smooth the brush stroke

      :type: int in [0, inf], default 0

   .. attribute:: palette

      Active Palette

      :type: :class:`Palette`

   .. attribute:: show_brush

      :type: boolean, default False

   .. attribute:: show_brush_on_surface

      :type: boolean, default False

   .. attribute:: show_low_resolution

      For multires, show low resolution while navigating the view

      :type: boolean, default False

   .. attribute:: tile_offset

      Stride at which tiled strokes are copied

      :type: float array of 3 items in [0.01, inf], default (0.0, 0.0, 0.0)

   .. attribute:: tile_x

      Tile along X axis

      :type: boolean, default False

   .. attribute:: tile_y

      Tile along Y axis

      :type: boolean, default False

   .. attribute:: tile_z

      Tile along Z axis

      :type: boolean, default False

   .. attribute:: use_cavity

      Mask painting according to mesh geometry cavity

      :type: boolean, default False

   .. attribute:: use_symmetry_feather

      Reduce the strength of the brush where it overlaps symmetrical daubs

      :type: boolean, default False

   .. attribute:: use_symmetry_x

      Mirror brush across the X axis

      :type: boolean, default False

   .. attribute:: use_symmetry_y

      Mirror brush across the Y axis

      :type: boolean, default False

   .. attribute:: use_symmetry_z

      Mirror brush across the Z axis

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


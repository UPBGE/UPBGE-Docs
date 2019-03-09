Sculpt(Paint)
=============

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Paint`

.. class:: Sculpt(Paint)

   

   .. attribute:: constant_detail_resolution

      Maximum edge length for dynamic topology sculpting (as divisor of blender unit - higher value means smaller edge length)

      :type: float in [0.0001, inf], default 0.0

   .. attribute:: detail_percent

      Maximum edge length for dynamic topology sculpting (in brush percenage)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: detail_refine_method

      In dynamic-topology mode, how to add or remove mesh detail

      * ``SUBDIVIDE`` Subdivide Edges, Subdivide long edges to add mesh detail where needed.
      * ``COLLAPSE`` Collapse Edges, Collapse short edges to remove mesh detail where possible.
      * ``SUBDIVIDE_COLLAPSE`` Subdivide Collapse, Both subdivide long edges and collapse short edges to refine mesh detail.

      :type: enum in ['SUBDIVIDE', 'COLLAPSE', 'SUBDIVIDE_COLLAPSE'], default 'SUBDIVIDE'

   .. attribute:: detail_size

      Maximum edge length for dynamic topology sculpting (in pixels)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: detail_type_method

      In dynamic-topology mode, how mesh detail size is calculated

      * ``RELATIVE`` Relative Detail, Mesh detail is relative to the brush size and detail size.
      * ``CONSTANT`` Constant Detail, Mesh detail is constant in object space according to detail size.
      * ``BRUSH`` Brush Detail, Mesh detail is relative to brush radius.

      :type: enum in ['RELATIVE', 'CONSTANT', 'BRUSH'], default 'RELATIVE'

   .. attribute:: gravity

      Amount of gravity after each dab

      :type: float in [0, 1], default 0.0

   .. attribute:: gravity_object

      Object whose Z axis defines orientation of gravity

      :type: :class:`Object`

   .. attribute:: lock_x

      Disallow changes to the X axis of vertices

      :type: boolean, default False

   .. attribute:: lock_y

      Disallow changes to the Y axis of vertices

      :type: boolean, default False

   .. attribute:: lock_z

      Disallow changes to the Z axis of vertices

      :type: boolean, default False

   .. attribute:: radial_symmetry

      Number of times to copy strokes across the surface

      :type: int array of 3 items in [1, 64], default (1, 1, 1)

   .. attribute:: show_diffuse_color

      Show diffuse color of object and overlay sculpt mask on top of it

      :type: boolean, default False

   .. attribute:: symmetrize_direction

      Source and destination for symmetrize operator

      :type: enum in ['NEGATIVE_X', 'POSITIVE_X', 'NEGATIVE_Y', 'POSITIVE_Y', 'NEGATIVE_Z', 'POSITIVE_Z'], default 'NEGATIVE_X'

   .. attribute:: use_deform_only

      Use only deformation modifiers (temporary disable all constructive modifiers except multi-resolution)

      :type: boolean, default False

   .. attribute:: use_smooth_shading

      Show faces in dynamic-topology mode with smooth shading rather than flat shaded

      :type: boolean, default False

   .. attribute:: use_threaded

      Take advantage of multiple CPU cores to improve sculpting performance

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
   * :class:`Paint.brush`
   * :class:`Paint.palette`
   * :class:`Paint.show_brush`
   * :class:`Paint.show_brush_on_surface`
   * :class:`Paint.show_low_resolution`
   * :class:`Paint.input_samples`
   * :class:`Paint.use_symmetry_x`
   * :class:`Paint.use_symmetry_y`
   * :class:`Paint.use_symmetry_z`
   * :class:`Paint.use_symmetry_feather`
   * :class:`Paint.cavity_curve`
   * :class:`Paint.use_cavity`
   * :class:`Paint.tile_offset`
   * :class:`Paint.tile_x`
   * :class:`Paint.tile_y`
   * :class:`Paint.tile_z`

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

   * :class:`ToolSettings.sculpt`


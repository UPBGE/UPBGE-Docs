RemeshModifier(Modifier)
========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: RemeshModifier(Modifier)

   Generate a new surface with regular topology that follows the shape of the input mesh

   .. attribute:: mode

      * ``BLOCKS`` Blocks, Output a blocky surface with no smoothing.
      * ``SMOOTH`` Smooth, Output a smooth surface with no sharp-features detection.
      * ``SHARP`` Sharp, Output a surface that reproduces sharp edges and corners from the input mesh.

      :type: enum in ['BLOCKS', 'SMOOTH', 'SHARP'], default 'BLOCKS'

   .. attribute:: octree_depth

      Resolution of the octree; higher values give finer details

      :type: int in [1, 12], default 0

   .. attribute:: scale

      The ratio of the largest dimension of the model over the size of the grid

      :type: float in [0, 0.99], default 0.0

   .. attribute:: sharpness

      Tolerance for outliers; lower values filter noise while higher values will reproduce edges closer to the input

      :type: float in [-inf, inf], default 0.0

   .. attribute:: threshold

      If removing disconnected pieces, minimum size of components to preserve as a ratio of the number of polygons in the largest component

      :type: float in [0, 1], default 0.0

   .. attribute:: use_remove_disconnected

      :type: boolean, default False

   .. attribute:: use_smooth_shade

      Output faces with smooth shading rather than flat shaded

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
   * :class:`Modifier.name`
   * :class:`Modifier.type`
   * :class:`Modifier.show_viewport`
   * :class:`Modifier.show_render`
   * :class:`Modifier.show_in_editmode`
   * :class:`Modifier.show_on_cage`
   * :class:`Modifier.show_expanded`
   * :class:`Modifier.use_apply_on_spline`

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


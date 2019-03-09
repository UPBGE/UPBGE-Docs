CyclesCurveRenderSettings(bpy_struct)
=====================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: CyclesCurveRenderSettings(bpy_struct)

   

   .. attribute:: cull_backfacing

      Do not test the back-face of each strand

      :type: boolean, default True

   .. attribute:: maximum_width

      Maximum extension that strand radius can be increased by

      :type: float in [0, 100], default 0.1

   .. attribute:: minimum_width

      Minimal pixel width for strands (0 - deactivated)

      :type: float in [0, 100], default 0.0

   .. attribute:: primitive

      Type of primitive used for hair rendering

      * ``TRIANGLES`` Triangles, Create triangle geometry around strands.
      * ``LINE_SEGMENTS`` Line Segments, Use line segment primitives.
      * ``CURVE_SEGMENTS`` Curve Segments, Use segmented cardinal curve primitives.

      :type: enum in ['TRIANGLES', 'LINE_SEGMENTS', 'CURVE_SEGMENTS'], default 'LINE_SEGMENTS'

   .. attribute:: resolution

      Resolution of generated mesh

      :type: int in [3, 64], default 3

   .. attribute:: shape

      Form of hair

      * ``RIBBONS`` Ribbons, Ignore thickness of each strand.
      * ``THICK`` Thick, Use thickness of strand when rendering.

      :type: enum in ['RIBBONS', 'THICK'], default 'THICK'

   .. attribute:: subdivisions

      Number of subdivisions used in Cardinal curve intersection (power of 2)

      :type: int in [0, 24], default 4

   .. attribute:: use_curves

      Activate Cycles hair rendering for particle system

      :type: boolean, default True

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


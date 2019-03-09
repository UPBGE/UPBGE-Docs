LineStyleGeometryModifier_Blueprint(LineStyleGeometryModifier)
==============================================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`LineStyleModifier`, :class:`LineStyleGeometryModifier`

.. class:: LineStyleGeometryModifier_Blueprint(LineStyleGeometryModifier)

   Produce a blueprint using circular, elliptic, and square contour strokes

   .. attribute:: backbone_length

      Amount of backbone stretching

      :type: float in [-inf, inf], default 0.0

   .. attribute:: expanded

      True if the modifier tab is expanded

      :type: boolean, default False

   .. attribute:: name

      Name of the modifier

      :type: string, default "", (never None)

   .. attribute:: random_backbone

      Randomness of the backbone stretching

      :type: int in [0, inf], default 0

   .. attribute:: random_center

      Randomness of the center

      :type: int in [0, inf], default 0

   .. attribute:: random_radius

      Randomness of the radius

      :type: int in [0, inf], default 0

   .. attribute:: rounds

      Number of rounds in contour strokes

      :type: int in [1, 1000], default 0

   .. attribute:: shape

      Select the shape of blueprint contour strokes

      * ``CIRCLES`` Circles, Draw a blueprint using circular contour strokes.
      * ``ELLIPSES`` Ellipses, Draw a blueprint using elliptic contour strokes.
      * ``SQUARES`` Squares, Draw a blueprint using square contour strokes.

      :type: enum in ['CIRCLES', 'ELLIPSES', 'SQUARES'], default 'CIRCLES'

   .. data:: type

      Type of the modifier

      :type: enum in ['2D_OFFSET', '2D_TRANSFORM', 'BACKBONE_STRETCHER', 'BEZIER_CURVE', 'BLUEPRINT', 'GUIDING_LINES', 'PERLIN_NOISE_1D', 'PERLIN_NOISE_2D', 'POLYGONIZATION', 'SAMPLING', 'SIMPLIFICATION', 'SINUS_DISPLACEMENT', 'SPATIAL_NOISE', 'TIP_REMOVER'], default '2D_OFFSET', (readonly)

   .. attribute:: use

      Enable or disable this modifier during stroke rendering

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


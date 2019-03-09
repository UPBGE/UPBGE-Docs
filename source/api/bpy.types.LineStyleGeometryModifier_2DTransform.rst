LineStyleGeometryModifier_2DTransform(LineStyleGeometryModifier)
================================================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`LineStyleModifier`, :class:`LineStyleGeometryModifier`

.. class:: LineStyleGeometryModifier_2DTransform(LineStyleGeometryModifier)

   Apply two-dimensional scaling and rotation to stroke backbone geometry

   .. attribute:: angle

      Rotation angle

      :type: float in [-inf, inf], default 0.0

   .. attribute:: expanded

      True if the modifier tab is expanded

      :type: boolean, default False

   .. attribute:: name

      Name of the modifier

      :type: string, default "", (never None)

   .. attribute:: pivot

      Pivot of scaling and rotation operations

      :type: enum in ['CENTER', 'START', 'END', 'PARAM', 'ABSOLUTE'], default 'CENTER'

   .. attribute:: pivot_u

      Pivot in terms of the stroke point parameter u (0 <= u <= 1)

      :type: float in [0, 1], default 0.0

   .. attribute:: pivot_x

      2D X coordinate of the absolute pivot

      :type: float in [-inf, inf], default 0.0

   .. attribute:: pivot_y

      2D Y coordinate of the absolute pivot

      :type: float in [-inf, inf], default 0.0

   .. attribute:: scale_x

      Scaling factor that is applied along the X axis

      :type: float in [-inf, inf], default 0.0

   .. attribute:: scale_y

      Scaling factor that is applied along the Y axis

      :type: float in [-inf, inf], default 0.0

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


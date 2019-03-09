GPencilBrush(bpy_struct)
========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GPencilBrush(bpy_struct)

   Collection of brushes being used to control the line style of new strokes

   .. attribute:: angle

      Direction of the stroke at which brush gives maximal thickness (0° for horizontal)

      :type: float in [-1.5708, 1.5708], default 0.0

   .. attribute:: angle_factor

      Reduce brush thickness by this factor when stroke is perpendicular to 'Angle' direction

      :type: float in [0, 1], default 0.0

   .. data:: curve_jitter

      Curve used for the jitter effect

      :type: :class:`CurveMapping`, (readonly)

   .. data:: curve_sensitivity

      Curve used for the sensitivity

      :type: :class:`CurveMapping`, (readonly)

   .. data:: curve_strength

      Curve used for the strength

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: jitter

      Jitter factor for new strokes

      :type: float in [0, 1], default 0.0

   .. attribute:: line_width

      Thickness of strokes (in pixels)

      :type: int in [1, 300], default 0

   .. attribute:: name

      Brush name

      :type: string, default "", (never None)

   .. attribute:: pen_sensitivity_factor

      Pressure sensitivity factor for new strokes

      :type: float in [0.1, 3], default 0.0

   .. attribute:: pen_smooth_factor

      Amount of smoothing to apply to newly created strokes, to reduce jitter/noise

      :type: float in [0, 2], default 0.0

   .. attribute:: pen_smooth_steps

      Number of times to smooth newly created strokes

      :type: int in [1, 3], default 0

   .. attribute:: pen_subdivision_steps

      Number of times to subdivide newly created strokes, for less jagged strokes

      :type: int in [0, 3], default 0

   .. attribute:: random_press

      Randomness factor for pressure and strength in new strokes

      :type: float in [0, 1], default 0.0

   .. attribute:: random_subdiv

      Randomness factor for new strokes after subdivision

      :type: float in [0, 1], default 0.0

   .. attribute:: strength

      Color strength for new strokes (affect alpha factor of color)

      :type: float in [0, 1], default 0.0

   .. attribute:: use_jitter_pressure

      Use tablet pressure for jitter

      :type: boolean, default False

   .. attribute:: use_pressure

      Use tablet pressure

      :type: boolean, default False

   .. attribute:: use_random_pressure

      Use random value for pressure

      :type: boolean, default False

   .. attribute:: use_random_strength

      Use random value for strength

      :type: boolean, default False

   .. attribute:: use_strength_pressure

      Use tablet pressure for color strength

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

   * :class:`GreasePencilBrushes.active`
   * :class:`GreasePencilBrushes.new`
   * :class:`GreasePencilBrushes.remove`
   * :class:`ToolSettings.gpencil_brushes`


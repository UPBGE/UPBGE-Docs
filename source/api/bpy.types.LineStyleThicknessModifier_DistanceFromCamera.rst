LineStyleThicknessModifier_DistanceFromCamera(LineStyleThicknessModifier)
=========================================================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`LineStyleModifier`, :class:`LineStyleThicknessModifier`

.. class:: LineStyleThicknessModifier_DistanceFromCamera(LineStyleThicknessModifier)

   Change line thickness based on the distance from the camera

   .. attribute:: blend

      Specify how the modifier value is blended into the base value

      :type: enum in ['MIX', 'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'DIFFERENCE', 'MININUM', 'MAXIMUM'], default 'MIX'

   .. data:: curve

      Curve used for the curve mapping

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: expanded

      True if the modifier tab is expanded

      :type: boolean, default False

   .. attribute:: influence

      Influence factor by which the modifier changes the property

      :type: float in [0, 1], default 0.0

   .. attribute:: invert

      Invert the fade-out direction of the linear mapping

      :type: boolean, default False

   .. attribute:: mapping

      Select the mapping type

      * ``LINEAR`` Linear, Use linear mapping.
      * ``CURVE`` Curve, Use curve mapping.

      :type: enum in ['LINEAR', 'CURVE'], default 'LINEAR'

   .. attribute:: name

      Name of the modifier

      :type: string, default "", (never None)

   .. attribute:: range_max

      Upper bound of the input range the mapping is applied

      :type: float in [-inf, inf], default 0.0

   .. attribute:: range_min

      Lower bound of the input range the mapping is applied

      :type: float in [-inf, inf], default 0.0

   .. data:: type

      Type of the modifier

      :type: enum in ['ALONG_STROKE', 'CALLIGRAPHY', 'CREASE_ANGLE', 'CURVATURE_3D', 'DISTANCE_FROM_CAMERA', 'DISTANCE_FROM_OBJECT', 'MATERIAL', 'NOISE', 'TANGENT'], default 'ALONG_STROKE', (readonly)

   .. attribute:: use

      Enable or disable this modifier during stroke rendering

      :type: boolean, default False

   .. attribute:: value_max

      Maximum output value of the mapping

      :type: float in [-inf, inf], default 0.0

   .. attribute:: value_min

      Minimum output value of the mapping

      :type: float in [-inf, inf], default 0.0

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


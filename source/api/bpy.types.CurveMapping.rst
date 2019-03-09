CurveMapping(bpy_struct)
========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: CurveMapping(bpy_struct)

   Curve mapping to map color, vector and scalar values to other values using a user defined curve

   .. attribute:: black_level

      For RGB curves, the color that black is mapped to

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: clip_max_x

      :type: float in [-100, 100], default 0.0

   .. attribute:: clip_max_y

      :type: float in [-100, 100], default 0.0

   .. attribute:: clip_min_x

      :type: float in [-100, 100], default 0.0

   .. attribute:: clip_min_y

      :type: float in [-100, 100], default 0.0

   .. data:: curves

      :type: :class:`bpy_prop_collection` of :class:`CurveMap`, (readonly)

   .. attribute:: use_clip

      Force the curve view to fit a defined boundary

      :type: boolean, default False

   .. attribute:: white_level

      For RGB curves, the color that white is mapped to

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. method:: update()

      Update curve mapping after making changes


   .. method:: initialize()

      Initialize curve


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

   * :class:`Brush.curve`
   * :class:`ColorManagedViewSettings.curve_mapping`
   * :class:`CompositorNodeCurveRGB.mapping`
   * :class:`CompositorNodeCurveVec.mapping`
   * :class:`CompositorNodeHueCorrect.mapping`
   * :class:`CompositorNodeTime.curve`
   * :class:`CurvesModifier.curve_mapping`
   * :class:`GPencilBrush.curve_jitter`
   * :class:`GPencilBrush.curve_sensitivity`
   * :class:`GPencilBrush.curve_strength`
   * :class:`GPencilInterpolateSettings.interpolation_curve`
   * :class:`HookModifier.falloff_curve`
   * :class:`HueCorrectModifier.curve_mapping`
   * :class:`LineStyleAlphaModifier_AlongStroke.curve`
   * :class:`LineStyleAlphaModifier_CreaseAngle.curve`
   * :class:`LineStyleAlphaModifier_Curvature_3D.curve`
   * :class:`LineStyleAlphaModifier_DistanceFromCamera.curve`
   * :class:`LineStyleAlphaModifier_DistanceFromObject.curve`
   * :class:`LineStyleAlphaModifier_Material.curve`
   * :class:`LineStyleAlphaModifier_Noise.curve`
   * :class:`LineStyleAlphaModifier_Tangent.curve`
   * :class:`LineStyleThicknessModifier_AlongStroke.curve`
   * :class:`LineStyleThicknessModifier_CreaseAngle.curve`
   * :class:`LineStyleThicknessModifier_Curvature_3D.curve`
   * :class:`LineStyleThicknessModifier_DistanceFromCamera.curve`
   * :class:`LineStyleThicknessModifier_DistanceFromObject.curve`
   * :class:`LineStyleThicknessModifier_Material.curve`
   * :class:`LineStyleThicknessModifier_Tangent.curve`
   * :class:`Paint.cavity_curve`
   * :class:`ParticleBrush.curve`
   * :class:`ParticleSettings.clump_curve`
   * :class:`ParticleSettings.roughness_curve`
   * :class:`PointDensity.falloff_curve`
   * :class:`PointLamp.falloff_curve`
   * :class:`RenderSettings.motion_blur_shutter_curve`
   * :class:`ShaderNodeRGBCurve.mapping`
   * :class:`ShaderNodeVectorCurve.mapping`
   * :class:`SpotLamp.falloff_curve`
   * :class:`TextureNodeCurveRGB.mapping`
   * :class:`TextureNodeCurveTime.curve`
   * :class:`VertexWeightEditModifier.map_curve`
   * :class:`WarpModifier.falloff_curve`


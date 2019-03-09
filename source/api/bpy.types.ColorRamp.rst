ColorRamp(bpy_struct)
=====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ColorRamp(bpy_struct)

   Color ramp mapping a scalar value to a color

   .. attribute:: color_mode

      Set color mode to use for interpolation

      :type: enum in ['RGB', 'HSV', 'HSL'], default 'RGB'

   .. data:: elements

      :type: :class:`ColorRampElements` :class:`bpy_prop_collection` of :class:`ColorRampElement`, (readonly)

   .. attribute:: hue_interpolation

      Set color interpolation

      :type: enum in ['NEAR', 'FAR', 'CW', 'CCW'], default 'NEAR'

   .. attribute:: interpolation

      Set interpolation between color stops

      :type: enum in ['EASE', 'CARDINAL', 'LINEAR', 'B_SPLINE', 'CONSTANT'], default 'LINEAR'

   .. method:: evaluate(position)

      Evaluate ColorRamp

      :arg position:

         Position, Evaluate ColorRamp at position

      :type position: float in [0, 1]
      :return:

         Color, Color at given position

      :rtype: float array of 4 items in [-inf, inf]

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

   * :class:`Brush.gradient`
   * :class:`ColorMapping.color_ramp`
   * :class:`CompositorNodeValToRGB.color_ramp`
   * :class:`DynamicPaintBrushSettings.paint_ramp`
   * :class:`DynamicPaintBrushSettings.velocity_ramp`
   * :class:`LineStyleColorModifier_AlongStroke.color_ramp`
   * :class:`LineStyleColorModifier_CreaseAngle.color_ramp`
   * :class:`LineStyleColorModifier_Curvature_3D.color_ramp`
   * :class:`LineStyleColorModifier_DistanceFromCamera.color_ramp`
   * :class:`LineStyleColorModifier_DistanceFromObject.color_ramp`
   * :class:`LineStyleColorModifier_Material.color_ramp`
   * :class:`LineStyleColorModifier_Noise.color_ramp`
   * :class:`LineStyleColorModifier_Tangent.color_ramp`
   * :class:`Material.diffuse_ramp`
   * :class:`Material.specular_ramp`
   * :class:`PointDensity.color_ramp`
   * :class:`ShaderNodeValToRGB.color_ramp`
   * :class:`SmokeDomainSettings.color_ramp`
   * :class:`Texture.color_ramp`
   * :class:`TextureNodeValToRGB.color_ramp`
   * :class:`UserPreferencesSystem.weight_color_range`


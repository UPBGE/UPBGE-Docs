WorldLighting(bpy_struct)
=========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: WorldLighting(bpy_struct)

   Lighting for a World data-block

   .. attribute:: adapt_to_speed

      Use the speed vector pass to reduce AO samples in fast moving pixels - higher values result in more aggressive sample reduction (requires Vec pass enabled, for Raytrace Adaptive QMC)

      :type: float in [0, 1], default 0.0

   .. attribute:: ao_blend_type

      Defines how AO mixes with material shading

      * ``MULTIPLY`` Multiply, Multiply direct lighting with ambient occlusion, darkening the result.
      * ``ADD`` Add, Add light and shadow.

      :type: enum in ['MULTIPLY', 'ADD'], default 'ADD'

   .. attribute:: ao_factor

      Factor for ambient occlusion blending

      :type: float in [0, inf], default 0.0

   .. attribute:: bias

      Bias (in radians) to prevent smoothed faces from showing banding (for Raytrace Constant Jittered)

      :type: float in [0, 0.5], default 0.0

   .. attribute:: correction

      Ad-hoc correction for over-occlusion due to the approximation

      :type: float in [0, 1], default 0.0

   .. attribute:: distance

      Length of rays, defines how far away other faces give occlusion effect

      :type: float in [-inf, inf], default 0.0

   .. attribute:: environment_color

      Defines where the color of the environment light comes from

      * ``PLAIN`` White, Plain diffuse energy (white.).
      * ``SKY_COLOR`` Sky Color, Use horizon and zenith color for diffuse energy.
      * ``SKY_TEXTURE`` Sky Texture, Does full Sky texture render for diffuse energy.

      :type: enum in ['PLAIN', 'SKY_COLOR', 'SKY_TEXTURE'], default 'PLAIN'

   .. attribute:: environment_energy

      Defines the strength of environment light

      :type: float in [-inf, inf], default 0.0

   .. attribute:: error_threshold

      Low values are slower and higher quality

      :type: float in [0.0001, 10], default 0.0

   .. attribute:: falloff_strength

      Attenuation falloff strength, the higher, the less influence distant objects have

      :type: float in [-inf, inf], default 0.0

   .. attribute:: gather_method

      * ``RAYTRACE`` Raytrace, Accurate, but slow when noise-free results are required.
      * ``APPROXIMATE`` Approximate, Inaccurate, but faster and without noise.

      :type: enum in ['RAYTRACE', 'APPROXIMATE'], default 'RAYTRACE'

   .. attribute:: indirect_bounces

      Number of indirect diffuse light bounces

      :type: int in [1, 32767], default 0

   .. attribute:: indirect_factor

      Factor for how much surrounding objects contribute to light

      :type: float in [0, inf], default 0.0

   .. attribute:: passes

      Number of preprocessing passes to reduce over-occlusion

      :type: int in [0, 10], default 0

   .. attribute:: sample_method

      Method for generating shadow samples (for Raytrace)

      * ``CONSTANT_JITTERED`` Constant Jittered, Fastest and gives the most noise.
      * ``ADAPTIVE_QMC`` Adaptive QMC, Fast in high-contrast areas.
      * ``CONSTANT_QMC`` Constant QMC, Best quality.

      :type: enum in ['CONSTANT_JITTERED', 'ADAPTIVE_QMC', 'CONSTANT_QMC'], default 'CONSTANT_JITTERED'

   .. attribute:: samples

      Amount of ray samples. Higher values give smoother results and longer rendering times

      :type: int in [1, 128], default 0

   .. attribute:: threshold

      Samples below this threshold will be considered fully shadowed/unshadowed and skipped (for Raytrace Adaptive QMC)

      :type: float in [0, 1], default 0.0

   .. attribute:: use_ambient_occlusion

      Use Ambient Occlusion to add shadowing based on distance between objects

      :type: boolean, default False

   .. attribute:: use_cache

      Cache AO results in pixels and interpolate over neighboring pixels for speedup

      :type: boolean, default False

   .. attribute:: use_environment_light

      Add light coming from the environment

      :type: boolean, default False

   .. attribute:: use_falloff

      Distance will be used to attenuate shadows

      :type: boolean, default False

   .. attribute:: use_indirect_light

      Add indirect light bouncing of surrounding objects

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

   * :class:`World.light_settings`


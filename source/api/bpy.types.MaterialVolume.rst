MaterialVolume(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MaterialVolume(bpy_struct)

   Volume rendering settings for a Material data-block

   .. attribute:: asymmetry

      Back scattering (-1.0) to Forward scattering (1.0) and the range in between

      :type: float in [-1, 1], default 0.0

   .. attribute:: cache_resolution

      Resolution of the voxel grid, low resolutions are faster, high resolutions use more memory

      :type: int in [1, 1024], default 0

   .. attribute:: density

      The base density of the volume

      :type: float in [0, 1], default 0.0

   .. attribute:: density_scale

      Multiplier for the material's density

      :type: float in [0, inf], default 0.0

   .. attribute:: depth_threshold

      Stop ray marching early if transmission drops below this luminance - higher values give speedups in dense volumes at the expense of accuracy

      :type: float in [0, 1], default 0.0

   .. attribute:: emission

      Amount of light that gets emitted by the volume

      :type: float in [0, inf], default 0.0

   .. attribute:: emission_color

      Color of emitted light

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: light_method

      Method of shading, attenuating, and scattering light through the volume

      * ``SHADELESS`` Shadeless, Do not calculate lighting and shadows.
      * ``SHADOWED`` Shadowed.
      * ``SHADED`` Shaded.
      * ``MULTIPLE_SCATTERING`` Multiple Scattering.
      * ``SHADED_PLUS_MULTIPLE_SCATTERING`` Shaded + Multiple Scattering.

      :type: enum in ['SHADELESS', 'SHADOWED', 'SHADED', 'MULTIPLE_SCATTERING', 'SHADED_PLUS_MULTIPLE_SCATTERING'], default 'SHADELESS'

   .. attribute:: ms_diffusion

      Diffusion factor, the strength of the blurring effect

      :type: float in [0, inf], default 0.0

   .. attribute:: ms_intensity

      Multiplier for multiple scattered light energy

      :type: float in [0, inf], default 0.0

   .. attribute:: ms_spread

      Proportional distance over which the light is diffused

      :type: float in [0, inf], default 0.0

   .. attribute:: reflection

      Multiplier to make out-scattered light brighter or darker (non-physically correct)

      :type: float in [0, inf], default 0.0

   .. attribute:: reflection_color

      Color of light scattered out of the volume (does not affect transmission)

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: scattering

      Amount of light that gets scattered out by the volume - the more out-scattering, the shallower the light will penetrate

      :type: float in [0, inf], default 0.0

   .. attribute:: step_method

      Method of calculating the steps through the volume

      :type: enum in ['RANDOMIZED', 'CONSTANT'], default 'RANDOMIZED'

   .. attribute:: step_size

      Distance between subsequent volume depth samples

      :type: float in [0, inf], default 0.0

   .. attribute:: transmission_color

      Result color of the volume, after other light has been scattered/absorbed

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: use_external_shadows

      Receive shadows from sources outside the volume (temporary)

      :type: boolean, default False

   .. attribute:: use_light_cache

      Pre-calculate the shading information into a voxel grid, speeds up shading at slightly less accuracy

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

   * :class:`Material.volume`


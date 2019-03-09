LampSkySettings(bpy_struct)
===========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: LampSkySettings(bpy_struct)

   Sky related settings for a sun lamp

   .. attribute:: atmosphere_distance_factor

      Multiplier to convert blender units to physical distance

      :type: float in [0, 500], default 0.0

   .. attribute:: atmosphere_extinction

      Extinction scattering contribution factor

      :type: float in [0, 1], default 0.0

   .. attribute:: atmosphere_inscattering

      Scatter contribution factor

      :type: float in [0, 1], default 0.0

   .. attribute:: atmosphere_turbidity

      Sky turbidity

      :type: float in [1, 30], default 0.0

   .. attribute:: backscattered_light

      Backscattered light

      :type: float in [-1, 1], default 0.0

   .. attribute:: horizon_brightness

      Horizon brightness

      :type: float in [0, 20], default 0.0

   .. attribute:: sky_blend

      Blend factor with sky

      :type: float in [0, 2], default 0.0

   .. attribute:: sky_blend_type

      Blend mode for combining sun sky with world sky

      :type: enum in ['MIX', 'ADD', 'MULTIPLY', 'SUBTRACT', 'SCREEN', 'DIVIDE', 'DIFFERENCE', 'DARKEN', 'LIGHTEN', 'OVERLAY', 'DODGE', 'BURN', 'HUE', 'SATURATION', 'VALUE', 'COLOR', 'SOFT_LIGHT', 'LINEAR_LIGHT'], default 'MIX'

   .. attribute:: sky_color_space

      Color space to use for internal XYZ->RGB color conversion

      :type: enum in ['SMPTE', 'REC709', 'CIE'], default 'SMPTE'

   .. attribute:: sky_exposure

      Strength of sky shading exponential exposure correction

      :type: float in [0, 20], default 0.0

   .. attribute:: spread

      Horizon Spread

      :type: float in [0, 10], default 0.0

   .. attribute:: sun_brightness

      Sun brightness

      :type: float in [0, 10], default 0.0

   .. attribute:: sun_intensity

      Sun intensity

      :type: float in [0, 10], default 0.0

   .. attribute:: sun_size

      Sun size

      :type: float in [0, 10], default 0.0

   .. attribute:: use_atmosphere

      Apply sun effect on atmosphere

      :type: boolean, default False

   .. attribute:: use_sky

      Apply sun effect on sky

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

   * :class:`SunLamp.sky`


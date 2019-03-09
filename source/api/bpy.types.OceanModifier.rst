OceanModifier(Modifier)
=======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: OceanModifier(Modifier)

   Simulate an ocean surface

   .. attribute:: bake_foam_fade

      How much foam accumulates over time (baked ocean only)

      :type: float in [0, inf], default 0.0

   .. attribute:: choppiness

      Choppiness of the wave's crest (adds some horizontal component to the displacement)

      :type: float in [0, inf], default 0.0

   .. attribute:: damping

      Damp reflected waves going in opposite direction to the wind

      :type: float in [0, 1], default 0.0

   .. attribute:: depth

      Depth of the solid ground below the water surface

      :type: float in [-inf, inf], default 0.0

   .. attribute:: filepath

      Path to a folder to store external baked images

      :type: string, default "", (never None)

   .. attribute:: foam_coverage

      Amount of generated foam

      :type: float in [-inf, inf], default 0.0

   .. attribute:: foam_layer_name

      Name of the vertex color layer used for foam

      :type: string, default "", (never None)

   .. attribute:: frame_end

      End frame of the ocean baking

      :type: int in [0, inf], default 0

   .. attribute:: frame_start

      Start frame of the ocean baking

      :type: int in [0, inf], default 0

   .. attribute:: geometry_mode

      Method of modifying geometry

      * ``GENERATE`` Generate, Generate ocean surface geometry at the specified resolution.
      * ``DISPLACE`` Displace, Displace existing geometry according to simulation.

      :type: enum in ['GENERATE', 'DISPLACE'], default 'GENERATE'

   .. data:: is_cached

      Whether the ocean is using cached data or simulating

      :type: boolean, default False, (readonly)

   .. attribute:: random_seed

      Seed of the random generator

      :type: int in [0, inf], default 0

   .. attribute:: repeat_x

      Repetitions of the generated surface in X

      :type: int in [1, 1024], default 0

   .. attribute:: repeat_y

      Repetitions of the generated surface in Y

      :type: int in [1, 1024], default 0

   .. attribute:: resolution

      Resolution of the generated surface

      :type: int in [1, 1024], default 0

   .. attribute:: size

      Surface scale factor (does not affect the height of the waves)

      :type: float in [0, inf], default 0.0

   .. attribute:: spatial_size

      Size of the simulation domain (in meters), and of the generated geometry (in BU)

      :type: int in [-inf, inf], default 0

   .. attribute:: time

      Current time of the simulation

      :type: float in [0, inf], default 0.0

   .. attribute:: use_foam

      Generate foam mask as a vertex color channel

      :type: boolean, default False

   .. attribute:: use_normals

      Output normals for bump mapping - disabling can speed up performance if its not needed

      :type: boolean, default False

   .. attribute:: wave_alignment

      How much the waves are aligned to each other

      :type: float in [0, 10], default 0.0

   .. attribute:: wave_direction

      Main direction of the waves when they are (partially) aligned

      :type: float in [-inf, inf], default 0.0

   .. attribute:: wave_scale

      Scale of the displacement effect

      :type: float in [0, inf], default 0.0

   .. attribute:: wave_scale_min

      Shortest allowed wavelength

      :type: float in [0, inf], default 0.0

   .. attribute:: wind_velocity

      Wind speed

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
   * :class:`Modifier.name`
   * :class:`Modifier.type`
   * :class:`Modifier.show_viewport`
   * :class:`Modifier.show_render`
   * :class:`Modifier.show_in_editmode`
   * :class:`Modifier.show_on_cage`
   * :class:`Modifier.show_expanded`
   * :class:`Modifier.use_apply_on_spline`

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


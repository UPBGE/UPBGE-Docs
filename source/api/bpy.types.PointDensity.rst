PointDensity(bpy_struct)
========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: PointDensity(bpy_struct)

   Point density settings

   .. data:: color_ramp

      :type: :class:`ColorRamp`, (readonly)

   .. attribute:: falloff

      Method of attenuating density by distance from the point

      * ``STANDARD`` Standard.
      * ``SMOOTH`` Smooth.
      * ``SOFT`` Soft.
      * ``CONSTANT`` Constant, Density is constant within lookup radius.
      * ``ROOT`` Root.
      * ``PARTICLE_AGE`` Particle Age.
      * ``PARTICLE_VELOCITY`` Particle Velocity.

      :type: enum in ['STANDARD', 'SMOOTH', 'SOFT', 'CONSTANT', 'ROOT', 'PARTICLE_AGE', 'PARTICLE_VELOCITY'], default 'STANDARD'

   .. data:: falloff_curve

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: falloff_soft

      Softness of the 'soft' falloff option

      :type: float in [0.01, inf], default 0.0

   .. attribute:: falloff_speed_scale

      Multiplier to bring particle speed within an acceptable range

      :type: float in [0.001, 100], default 0.0

   .. attribute:: noise_basis

      Noise formula used for turbulence

      * ``BLENDER_ORIGINAL`` Blender Original, Noise algorithm - Blender original: Smooth interpolated noise.
      * ``ORIGINAL_PERLIN`` Original Perlin, Noise algorithm - Original Perlin: Smooth interpolated noise.
      * ``IMPROVED_PERLIN`` Improved Perlin, Noise algorithm - Improved Perlin: Smooth interpolated noise.
      * ``VORONOI_F1`` Voronoi F1, Noise algorithm - Voronoi F1: Returns distance to the closest feature point.
      * ``VORONOI_F2`` Voronoi F2, Noise algorithm - Voronoi F2: Returns distance to the 2nd closest feature point.
      * ``VORONOI_F3`` Voronoi F3, Noise algorithm - Voronoi F3: Returns distance to the 3rd closest feature point.
      * ``VORONOI_F4`` Voronoi F4, Noise algorithm - Voronoi F4: Returns distance to the 4th closest feature point.
      * ``VORONOI_F2_F1`` Voronoi F2-F1, Noise algorithm - Voronoi F1-F2.
      * ``VORONOI_CRACKLE`` Voronoi Crackle, Noise algorithm - Voronoi Crackle: Voronoi tessellation with sharp edges.
      * ``CELL_NOISE`` Cell Noise, Noise algorithm - Cell Noise: Square cell tessellation.

      :type: enum in ['BLENDER_ORIGINAL', 'ORIGINAL_PERLIN', 'IMPROVED_PERLIN', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2_F1', 'VORONOI_CRACKLE', 'CELL_NOISE'], default 'BLENDER_ORIGINAL'

   .. attribute:: object

      Object to take point data from

      :type: :class:`Object`

   .. attribute:: particle_cache_space

      Coordinate system to cache particles in

      :type: enum in ['OBJECT_LOCATION', 'OBJECT_SPACE', 'WORLD_SPACE'], default 'OBJECT_LOCATION'

   .. attribute:: particle_color_source

      Data to derive color results from

      * ``CONSTANT`` Constant.
      * ``PARTICLE_AGE`` Particle Age, Lifetime mapped as 0.0 - 1.0 intensity.
      * ``PARTICLE_SPEED`` Particle Speed, Particle speed (absolute magnitude of velocity) mapped as 0.0-1.0 intensity.
      * ``PARTICLE_VELOCITY`` Particle Velocity, XYZ velocity mapped to RGB colors.

      :type: enum in ['CONSTANT', 'PARTICLE_AGE', 'PARTICLE_SPEED', 'PARTICLE_VELOCITY'], default 'CONSTANT'

   .. attribute:: particle_system

      Particle System to render as points

      :type: :class:`ParticleSystem`

   .. attribute:: point_source

      Point data to use as renderable point density

      * ``PARTICLE_SYSTEM`` Particle System, Generate point density from a particle system.
      * ``OBJECT`` Object Vertices, Generate point density from an object's vertices.

      :type: enum in ['PARTICLE_SYSTEM', 'OBJECT'], default 'PARTICLE_SYSTEM'

   .. attribute:: radius

      Radius from the shaded sample to look for points within

      :type: float in [0.001, inf], default 0.0

   .. attribute:: speed_scale

      Multiplier to bring particle speed within an acceptable range

      :type: float in [0.001, 100], default 0.0

   .. attribute:: turbulence_depth

      Level of detail in the added turbulent noise

      :type: int in [0, 30], default 0

   .. attribute:: turbulence_influence

      Method for driving added turbulent noise

      * ``STATIC`` Static, Noise patterns will remain unchanged, faster and suitable for stills.
      * ``PARTICLE_VELOCITY`` Particle Velocity, Turbulent noise driven by particle velocity.
      * ``PARTICLE_AGE`` Particle Age, Turbulent noise driven by the particle's age between birth and death.
      * ``GLOBAL_TIME`` Global Time, Turbulent noise driven by the global current frame.

      :type: enum in ['STATIC', 'PARTICLE_VELOCITY', 'PARTICLE_AGE', 'GLOBAL_TIME'], default 'STATIC'

   .. attribute:: turbulence_scale

      Scale of the added turbulent noise

      :type: float in [0.01, inf], default 0.0

   .. attribute:: turbulence_strength

      Strength of the added turbulent noise

      :type: float in [0.01, inf], default 0.0

   .. attribute:: use_falloff_curve

      Use a custom falloff curve

      :type: boolean, default False

   .. attribute:: use_turbulence

      Add directed noise to the density at render-time

      :type: boolean, default False

   .. attribute:: vertex_attribute_name

      Vertex attribute to use for color

      :type: string, default "", (never None)

   .. attribute:: vertex_cache_space

      Coordinate system to cache vertices in

      :type: enum in ['OBJECT_LOCATION', 'OBJECT_SPACE', 'WORLD_SPACE'], default 'OBJECT_LOCATION'

   .. attribute:: vertex_color_source

      Data to derive color results from

      * ``CONSTANT`` Constant.
      * ``VERTEX_COLOR`` Vertex Color, Vertex color layer.
      * ``VERTEX_WEIGHT`` Vertex Weight, Vertex group weight.
      * ``VERTEX_NORMAL`` Vertex Normal, XYZ normal vector mapped to RGB colors.

      :type: enum in ['CONSTANT', 'VERTEX_COLOR', 'VERTEX_WEIGHT', 'VERTEX_NORMAL'], default 'CONSTANT'

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

   * :class:`PointDensityTexture.point_density`


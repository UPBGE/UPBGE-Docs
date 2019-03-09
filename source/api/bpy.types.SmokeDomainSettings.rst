SmokeDomainSettings(bpy_struct)
===============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SmokeDomainSettings(bpy_struct)

   Smoke domain settings

   .. attribute:: adapt_margin

      Margin added around fluid to minimize boundary interference

      :type: int in [2, 24], default 0

   .. attribute:: adapt_threshold

      Maximum amount of fluid cell can contain before it is considered empty

      :type: float in [0.01, 0.5], default 0.0

   .. attribute:: additional_res

      Maximum number of additional cells

      :type: int in [0, 512], default 0

   .. attribute:: alpha

      How much density affects smoke motion (higher value results in faster rising smoke)

      :type: float in [-5, 5], default 0.0

   .. attribute:: amplify

      Enhance the resolution of smoke by this factor using noise

      :type: int in [1, 10], default 0

   .. attribute:: axis_slice_method

      * ``FULL`` Full, Slice the whole domain object.
      * ``SINGLE`` Single, Perform a single slice of the domain object.

      :type: enum in ['FULL', 'SINGLE'], default 'FULL'

   .. attribute:: beta

      How much heat affects smoke motion (higher value results in faster rising smoke)

      :type: float in [-5, 5], default 0.0

   .. attribute:: burning_rate

      Speed of the burning reaction (use larger values for smaller flame)

      :type: float in [0.01, 4], default 0.0

   .. attribute:: cache_file_format

      Select the file format to be used for caching

      * ``POINTCACHE`` Point Cache, Blender specific point cache file format.
      * ``OPENVDB`` OpenVDB, OpenVDB file format.

      :type: enum in ['POINTCACHE', 'OPENVDB'], default 'POINTCACHE'

   .. data:: cell_size

      Cell Size

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. attribute:: coba_field

      Simulation field to color map

      * ``COLOR_R`` Red, Red component of the color field.
      * ``COLOR_G`` Green, Green component of the color field.
      * ``COLOR_B`` Blue, Blue component of the color field.
      * ``DENSITY`` Density, Quantity of soot in the fluid.
      * ``FLAME`` Flame, Flame field.
      * ``FUEL`` Fuel, Fuel field.
      * ``HEAT`` Heat, Temperature of the fluid.
      * ``VELOCITY_X`` X Velocity, X component of the velocity field.
      * ``VELOCITY_Y`` Y Velocity, Y component of the velocity field.
      * ``VELOCITY_Z`` Z Velocity, Z component of the velocity field.

      :type: enum in ['COLOR_R', 'COLOR_G', 'COLOR_B', 'DENSITY', 'FLAME', 'FUEL', 'HEAT', 'VELOCITY_X', 'VELOCITY_Y', 'VELOCITY_Z'], default 'DENSITY'

   .. attribute:: collision_extents

      Select which domain border will be treated as collision object

      * ``BORDEROPEN`` Open, Smoke doesn't collide with any border.
      * ``BORDERVERTICAL`` Vertically Open, Smoke doesn't collide with top and bottom sides.
      * ``BORDERCLOSED`` Collide All, Smoke collides with every side.

      :type: enum in ['BORDEROPEN', 'BORDERVERTICAL', 'BORDERCLOSED'], default 'BORDEROPEN'

   .. attribute:: collision_group

      Limit collisions to this group

      :type: :class:`Group`

   .. data:: color_grid

      Smoke color grid

      :type: float array of 32 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), (readonly)

   .. data:: color_ramp

      :type: :class:`ColorRamp`, (readonly)

   .. attribute:: data_depth

      Bit depth for writing all scalar (including vector) lower values reduce file size

      * ``16`` Float (Half), Half float (16 bit data).
      * ``32`` Float (Full), Full float (32 bit data).

      :type: enum in ['16', '32'], default '32'

   .. data:: density_grid

      Smoke density grid

      :type: float array of 32 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), (readonly)

   .. attribute:: display_thickness

      Thickness of smoke drawing in the viewport

      :type: float in [0.001, 1000], default 0.0

   .. attribute:: dissolve_speed

      Dissolve Speed

      :type: int in [1, 10000], default 0

   .. data:: domain_resolution

      Smoke Grid Resolution

      :type: int array of 3 items in [-inf, inf], default (0, 0, 0), (readonly)

   .. attribute:: draw_velocity

      Toggle visualization of the velocity field as needles

      :type: boolean, default False

   .. attribute:: effector_group

      Limit effectors to this group

      :type: :class:`Group`

   .. data:: effector_weights

      :type: :class:`EffectorWeights`, (readonly)

   .. data:: flame_grid

      Smoke flame grid

      :type: float array of 32 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), (readonly)

   .. attribute:: flame_ignition

      Minimum temperature of flames

      :type: float in [0.5, 5], default 0.0

   .. attribute:: flame_max_temp

      Maximum temperature of flames

      :type: float in [1, 10], default 0.0

   .. attribute:: flame_smoke

      Amount of smoke created by burning fuel

      :type: float in [0, 8], default 0.0

   .. attribute:: flame_smoke_color

      Color of smoke emitted from burning fuel

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: flame_vorticity

      Additional vorticity for the flames

      :type: float in [0, 2], default 0.0

   .. attribute:: fluid_group

      Limit fluid objects to this group

      :type: :class:`Group`

   .. data:: heat_grid

      Smoke heat grid

      :type: float array of 32 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), (readonly)

   .. attribute:: highres_sampling

      Method for sampling the high resolution flow

      :type: enum in ['FULLSAMPLE', 'LINEAR', 'NEAREST'], default 'NEAREST'

   .. attribute:: noise_type

      Noise method which is used for creating the high resolution

      :type: enum in ['NOISEWAVE', 'NOISEFFT'], default 'NOISEWAVE'

   .. attribute:: openvdb_cache_compress_type

      Compression method to be used

      * ``ZIP`` Zip, Effective but slow compression.
      * ``BLOSC`` Blosc, Multithreaded compression, similar in size and quality as 'Zip'.
      * ``NONE`` None, Do not use any compression.

      :type: enum in ['ZIP', 'BLOSC', 'NONE'], default 'BLOSC'

   .. data:: point_cache

      :type: :class:`PointCache`, (readonly, never None)

   .. attribute:: point_cache_compress_type

      Compression method to be used

      * ``CACHELIGHT`` Light, Fast but not so effective compression.
      * ``CACHEHEAVY`` Heavy, Effective but slow compression.

      :type: enum in ['CACHELIGHT', 'CACHEHEAVY'], default 'CACHELIGHT'

   .. attribute:: resolution_max

      Maximal resolution used in the fluid domain

      :type: int in [6, 512], default 0

   .. attribute:: show_high_resolution

      Show high resolution (using amplification)

      :type: boolean, default False

   .. attribute:: slice_axis

      * ``AUTO`` Auto, Adjust slice direction according to the view direction.
      * ``X`` X, Slice along the X axis.
      * ``Y`` Y, Slice along the Y axis.
      * ``Z`` Z, Slice along the Z axis.

      :type: enum in ['AUTO', 'X', 'Y', 'Z'], default 'AUTO'

   .. attribute:: slice_depth

      Position of the slice

      :type: float in [0, 1], default 0.0

   .. attribute:: slice_method

      How to slice the volume for viewport rendering

      * ``VIEW_ALIGNED`` View, Slice volume parallel to the view plane.
      * ``AXIS_ALIGNED`` Axis, Slice volume parallel to the major axis.

      :type: enum in ['VIEW_ALIGNED', 'AXIS_ALIGNED'], default 'VIEW_ALIGNED'

   .. attribute:: slice_per_voxel

      How many slices per voxel should be generated

      :type: float in [0, 100], default 0.0

   .. data:: start_point

      Start point

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. attribute:: strength

      Strength of noise

      :type: float in [0, 10], default 0.0

   .. attribute:: time_scale

      Adjust simulation speed

      :type: float in [0.2, 1.5], default 0.0

   .. attribute:: use_adaptive_domain

      Adapt simulation resolution and size to fluid

      :type: boolean, default False

   .. attribute:: use_color_ramp

      Render a simulation field while mapping its voxels values to the colors of a ramp

      :type: boolean, default False

   .. attribute:: use_dissolve_smoke

      Enable smoke to disappear over time

      :type: boolean, default False

   .. attribute:: use_dissolve_smoke_log

      Using 1/x

      :type: boolean, default False

   .. attribute:: use_high_resolution

      Enable high resolution (using amplification)

      :type: boolean, default False

   .. attribute:: vector_draw_type

      * ``NEEDLE`` Needle, Draw vectors as needles.
      * ``STREAMLINE`` Streamlines, Draw vectors as streamlines.

      :type: enum in ['NEEDLE', 'STREAMLINE'], default 'NEEDLE'

   .. attribute:: vector_scale

      Multiplier for scaling the vectors

      :type: float in [0, 1000], default 0.0

   .. data:: velocity_grid

      Smoke velocity grid

      :type: float array of 32 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), (readonly)

   .. attribute:: vorticity

      Amount of turbulence/rotation in fluid

      :type: float in [0.01, 4], default 0.0

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

   * :class:`SmokeModifier.domain_settings`


CyclesRenderSettings(bpy_struct)
================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: CyclesRenderSettings(bpy_struct)

   

   .. attribute:: aa_samples

      Number of antialiasing samples to render for each pixel

      :type: int in [1, 2097151], default 128

   .. attribute:: ao_bounces

      Approximate indirect light with background tinted ambient occlusion at the specified bounce, 0 disables this feature

      :type: int in [0, 1024], default 0

   .. attribute:: ao_bounces_render

      Approximate indirect light with background tinted ambient occlusion at the specified bounce, 0 disables this feature

      :type: int in [0, 1024], default 0

   .. attribute:: ao_samples

      Number of ambient occlusion samples to render for each AA sample

      :type: int in [1, 1024], default 1

   .. attribute:: bake_type

      Type of pass to bake

      :type: enum in ['COMBINED', 'AO', 'SHADOW', 'NORMAL', 'UV', 'EMIT', 'ENVIRONMENT', 'DIFFUSE', 'GLOSSY', 'TRANSMISSION', 'SUBSURFACE'], default 'COMBINED'

   .. attribute:: blur_glossy

      Adaptively blur glossy shaders after blurry bounces, to reduce noise at the cost of accuracy

      :type: float in [0, 10], default 1.0

   .. attribute:: camera_cull_margin

      Margin for the camera space culling

      :type: float in [0, 5], default 0.1

   .. attribute:: caustics_reflective

      Use reflective caustics, resulting in a brighter image (more noise but added realism)

      :type: boolean, default True

   .. attribute:: caustics_refractive

      Use refractive caustics, resulting in a brighter image (more noise but added realism)

      :type: boolean, default True

   .. attribute:: debug_bvh_time_steps

      Split BVH primitives by this number of time steps to speed up render time in cost of memory

      :type: int in [0, 16], default 0

   .. attribute:: debug_bvh_type

      Choose between faster updates, or faster render

      * ``DYNAMIC_BVH`` Dynamic BVH, Objects can be individually updated, at the cost of slower render time.
      * ``STATIC_BVH`` Static BVH, Any object modification requires a complete BVH rebuild, but renders faster.

      :type: enum in ['DYNAMIC_BVH', 'STATIC_BVH'], default 'DYNAMIC_BVH'

   .. attribute:: debug_cancel_timeout

      :type: float in [0.01, 10], default 0.1

   .. attribute:: debug_opencl_device_type

      :type: enum in ['NONE', 'ALL', 'DEFAULT', 'CPU', 'GPU', 'ACCELERATOR'], default 'ALL'

   .. attribute:: debug_opencl_kernel_single_program

      :type: boolean, default True

   .. attribute:: debug_opencl_kernel_type

      :type: enum in ['DEFAULT', 'MEGA', 'SPLIT'], default 'DEFAULT'

   .. attribute:: debug_opencl_mem_limit

      Artificial limit on OpenCL memory usage in MB (0 to disable limit)

      :type: int in [-inf, inf], default 0

   .. attribute:: debug_reset_timeout

      :type: float in [0.01, 10], default 0.1

   .. attribute:: debug_text_timeout

      :type: float in [0.01, 10], default 1.0

   .. attribute:: debug_tile_size

      :type: int in [1, 4096], default 1024

   .. attribute:: debug_use_cpu_avx

      :type: boolean, default True

   .. attribute:: debug_use_cpu_avx2

      :type: boolean, default True

   .. attribute:: debug_use_cpu_split_kernel

      :type: boolean, default False

   .. attribute:: debug_use_cpu_sse2

      :type: boolean, default True

   .. attribute:: debug_use_cpu_sse3

      :type: boolean, default True

   .. attribute:: debug_use_cpu_sse41

      :type: boolean, default True

   .. attribute:: debug_use_cuda_adaptive_compile

      :type: boolean, default False

   .. attribute:: debug_use_cuda_split_kernel

      :type: boolean, default False

   .. attribute:: debug_use_hair_bvh

      Use special type BVH optimized for hair (uses more ram but renders faster)

      :type: boolean, default True

   .. attribute:: debug_use_opencl_debug

      :type: boolean, default False

   .. attribute:: debug_use_qbvh

      :type: boolean, default True

   .. attribute:: debug_use_spatial_splits

      Use BVH spatial splits: longer builder time, faster render

      :type: boolean, default False

   .. attribute:: device

      Device to use for rendering

      * ``CPU`` CPU, Use CPU for rendering.
      * ``GPU`` GPU Compute, Use GPU compute device for rendering, configured in the system tab in the user preferences.

      :type: enum in ['CPU', 'GPU'], default 'CPU'

   .. attribute:: dicing_rate

      Size of a micropolygon in pixels

      :type: float in [0.1, 1000], default 1.0

   .. attribute:: diffuse_bounces

      Maximum number of diffuse reflection bounces, bounded by total maximum

      :type: int in [0, 1024], default 4

   .. attribute:: diffuse_samples

      Number of diffuse bounce samples to render for each AA sample

      :type: int in [1, 1024], default 1

   .. attribute:: distance_cull_margin

      Cull objects which are further away from camera than this distance

      :type: float in [0, inf], default 50.0

   .. attribute:: feature_set

      Feature set to use for rendering

      * ``SUPPORTED`` Supported, Only use finished and supported features.
      * ``EXPERIMENTAL`` Experimental, Use experimental and incomplete features that might be broken or change in the future.

      :type: enum in ['SUPPORTED', 'EXPERIMENTAL'], default 'SUPPORTED'

   .. attribute:: film_exposure

      Image brightness scale

      :type: float in [0, 10], default 1.0

   .. attribute:: film_transparent

      World background is transparent with premultiplied alpha

      :type: boolean, default False

   .. attribute:: filter_type

      Pixel filter type

      * ``BOX`` Box, Box filter.
      * ``GAUSSIAN`` Gaussian, Gaussian filter.
      * ``BLACKMAN_HARRIS`` Blackman-Harris, Blackman-Harris filter.

      :type: enum in ['BOX', 'GAUSSIAN', 'BLACKMAN_HARRIS'], default 'BLACKMAN_HARRIS'

   .. attribute:: filter_width

      Pixel filter width

      :type: float in [0.01, 10], default 1.5

   .. attribute:: glossy_bounces

      Maximum number of glossy reflection bounces, bounded by total maximum

      :type: int in [0, 1024], default 4

   .. attribute:: glossy_samples

      Number of glossy bounce samples to render for each AA sample

      :type: int in [1, 1024], default 1

   .. attribute:: light_sampling_threshold

      Probabilistically terminate light samples when the light contribution is below this threshold (more noise but faster rendering). Zero disables the test and never ignores lights

      :type: float in [0, 1], default 0.01

   .. attribute:: max_bounces

      Total maximum number of bounces

      :type: int in [0, 1024], default 12

   .. attribute:: max_subdivisions

      Stop subdividing when this level is reached even if the dice rate would produce finer tessellation

      :type: int in [0, 16], default 12

   .. attribute:: mesh_light_samples

      Number of mesh emission light samples to render for each AA sample

      :type: int in [1, 1024], default 1

   .. attribute:: motion_blur_position

      Offset for the shutter's time interval, allows to change the motion blur trails

      * ``START`` Start on Frame, The shutter opens at the current frame.
      * ``CENTER`` Center on Frame, The shutter is open during the current frame.
      * ``END`` End on Frame, The shutter closes at the current frame.

      :type: enum in ['START', 'CENTER', 'END'], default 'CENTER'

   .. attribute:: pixel_filter_type

      Pixel filter type

      * ``BOX`` Box, Box filter.
      * ``GAUSSIAN`` Gaussian, Gaussian filter.
      * ``BLACKMAN_HARRIS`` Blackman-Harris, Blackman-Harris filter.

      :type: enum in ['BOX', 'GAUSSIAN', 'BLACKMAN_HARRIS'], default 'BLACKMAN_HARRIS'

   .. attribute:: preview_aa_samples

      Number of antialiasing samples to render in the viewport, unlimited if 0

      :type: int in [0, 2097151], default 32

   .. attribute:: preview_active_layer

      Preview active render layer in viewport

      :type: boolean, default False

   .. attribute:: preview_dicing_rate

      Size of a micropolygon in pixels during preview render

      :type: float in [0.1, 1000], default 8.0

   .. attribute:: preview_pause

      Pause all viewport preview renders

      :type: boolean, default False

   .. attribute:: preview_samples

      Number of samples to render in the viewport, unlimited if 0

      :type: int in [0, inf], default 32

   .. attribute:: preview_start_resolution

      Resolution to start rendering preview at, progressively increasing it to the full viewport size

      :type: int in [8, 16384], default 64

   .. attribute:: progressive

      Method to sample lights and materials

      * ``BRANCHED_PATH`` Branched Path Tracing, Path tracing integrator that branches on the first bounce, giving more control over the number of light and material samples.
      * ``PATH`` Path Tracing, Pure path tracing integrator.

      :type: enum in ['BRANCHED_PATH', 'PATH'], default 'PATH'

   .. attribute:: rolling_shutter_duration

      Scanline "exposure" time for the rolling shutter effect

      :type: float in [0, 1], default 0.1

   .. attribute:: rolling_shutter_type

      Type of rolling shutter effect matching CMOS-based cameras

      * ``NONE`` None, No rolling shutter effect used.
      * ``TOP`` Top-Bottom, Sensor is being scanned from top to bottom.

      :type: enum in ['NONE', 'TOP'], default 'NONE'

   .. attribute:: sample_all_lights_direct

      Sample all lights (for direct samples), rather than randomly picking one

      :type: boolean, default True

   .. attribute:: sample_all_lights_indirect

      Sample all lights (for indirect samples), rather than randomly picking one

      :type: boolean, default True

   .. attribute:: sample_clamp_direct

      If non-zero, the maximum value for a direct sample, higher values will be scaled down to avoid too much noise and slow convergence at the cost of accuracy

      :type: float in [0, inf], default 0.0

   .. attribute:: sample_clamp_indirect

      If non-zero, the maximum value for an indirect sample, higher values will be scaled down to avoid too much noise and slow convergence at the cost of accuracy

      :type: float in [0, inf], default 10.0

   .. attribute:: samples

      Number of samples to render for each pixel

      :type: int in [1, inf], default 128

   .. attribute:: sampling_pattern

      Random sampling pattern used by the integrator

      * ``SOBOL`` Sobol, Use Sobol random sampling pattern.
      * ``CORRELATED_MUTI_JITTER`` Correlated Multi-Jitter, Use Correlated Multi-Jitter random sampling pattern.

      :type: enum in ['SOBOL', 'CORRELATED_MUTI_JITTER'], default 'SOBOL'

   .. attribute:: seed

      Seed value for integrator to get different noise patterns

      :type: int in [0, inf], default 0

   .. attribute:: shading_system

      Use Open Shading Language (CPU rendering only)

      :type: boolean, default False

   .. attribute:: subsurface_samples

      Number of subsurface scattering samples to render for each AA sample

      :type: int in [1, 1024], default 1

   .. attribute:: texture_limit

      Limit texture size used by viewport rendering

      * ``OFF`` No Limit, No texture size limit.
      * ``128`` 128, Limit texture size to 128 pixels.
      * ``256`` 256, Limit texture size to 256 pixels.
      * ``512`` 512, Limit texture size to 512 pixels.
      * ``1024`` 1024, Limit texture size to 1024 pixels.
      * ``2048`` 2048, Limit texture size to 2048 pixels.
      * ``4096`` 4096, Limit texture size to 4096 pixels.
      * ``8192`` 8192, Limit texture size to 8192 pixels.

      :type: enum in ['OFF', '128', '256', '512', '1024', '2048', '4096', '8192'], default 'OFF'

   .. attribute:: texture_limit_render

      Limit texture size used by final rendering

      * ``OFF`` No Limit, No texture size limit.
      * ``128`` 128, Limit texture size to 128 pixels.
      * ``256`` 256, Limit texture size to 256 pixels.
      * ``512`` 512, Limit texture size to 512 pixels.
      * ``1024`` 1024, Limit texture size to 1024 pixels.
      * ``2048`` 2048, Limit texture size to 2048 pixels.
      * ``4096`` 4096, Limit texture size to 4096 pixels.
      * ``8192`` 8192, Limit texture size to 8192 pixels.

      :type: enum in ['OFF', '128', '256', '512', '1024', '2048', '4096', '8192'], default 'OFF'

   .. attribute:: tile_order

      Tile order for rendering

      * ``CENTER`` Center, Render from center to the edges.
      * ``RIGHT_TO_LEFT`` Right to Left, Render from right to left.
      * ``LEFT_TO_RIGHT`` Left to Right, Render from left to right.
      * ``TOP_TO_BOTTOM`` Top to Bottom, Render from top to bottom.
      * ``BOTTOM_TO_TOP`` Bottom to Top, Render from bottom to top.
      * ``HILBERT_SPIRAL`` Hilbert Spiral, Render in a Hilbert Spiral.

      :type: enum in ['CENTER', 'RIGHT_TO_LEFT', 'LEFT_TO_RIGHT', 'TOP_TO_BOTTOM', 'BOTTOM_TO_TOP', 'HILBERT_SPIRAL'], default 'HILBERT_SPIRAL'

   .. attribute:: transmission_bounces

      Maximum number of transmission bounces, bounded by total maximum

      :type: int in [0, 1024], default 12

   .. attribute:: transmission_samples

      Number of transmission bounce samples to render for each AA sample

      :type: int in [1, 1024], default 1

   .. attribute:: transparent_max_bounces

      Maximum number of transparent bounces

      :type: int in [0, 1024], default 8

   .. attribute:: use_animated_seed

      Use different seed values (and hence noise patterns) at different frames

      :type: boolean, default False

   .. attribute:: use_camera_cull

      Allow objects to be culled based on the camera frustum

      :type: boolean, default False

   .. attribute:: use_distance_cull

      Allow objects to be culled based on the distance from camera

      :type: boolean, default False

   .. attribute:: use_layer_samples

      How to use per render layer sample settings

      * ``USE`` Use, Per render layer number of samples override scene samples.
      * ``BOUNDED`` Bounded, Bound per render layer number of samples by global samples.
      * ``IGNORE`` Ignore, Ignore per render layer number of samples.

      :type: enum in ['USE', 'BOUNDED', 'IGNORE'], default 'USE'

   .. attribute:: use_progressive_refine

      Instead of rendering each tile until it is finished, refine the whole image progressively (this renders somewhat slower, but time can be saved by manually stopping the render when the noise is low enough)

      :type: boolean, default False

   .. attribute:: use_square_samples

      Square sampling values for easier artist control

      :type: boolean, default False

   .. attribute:: volume_bounces

      Maximum number of volumetric scattering events

      :type: int in [0, 1024], default 0

   .. attribute:: volume_max_steps

      Maximum number of steps through the volume before giving up, to avoid extremely long render times with big objects or small step sizes

      :type: int in [2, 65536], default 1024

   .. attribute:: volume_samples

      Number of volume scattering samples to render for each AA sample

      :type: int in [1, 1024], default 1

   .. attribute:: volume_step_size

      Distance between volume shader samples when rendering the volume (lower values give more accurate and detailed results, but also increased render time)

      :type: float in [1e-07, 100000], default 0.1

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


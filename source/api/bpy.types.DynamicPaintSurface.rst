DynamicPaintSurface(bpy_struct)
===============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: DynamicPaintSurface(bpy_struct)

   A canvas surface layer

   .. attribute:: brush_group

      Only use brush objects from this group

      :type: :class:`Group`

   .. attribute:: brush_influence_scale

      Adjust influence brush objects have on this surface

      :type: float in [0, 1], default 0.0

   .. attribute:: brush_radius_scale

      Adjust radius of proximity brushes or particles for this surface

      :type: float in [0, 10], default 0.0

   .. attribute:: color_dry_threshold

      The wetness level when colors start to shift to the background

      :type: float in [0, 1], default 0.0

   .. attribute:: color_spread_speed

      How fast colors get mixed within wet paint

      :type: float in [0, 2], default 0.0

   .. attribute:: depth_clamp

      Maximum level of depth intersection in object space (use 0.0 to disable)

      :type: float in [0, 50], default 0.0

   .. attribute:: displace_factor

      Strength of displace when applied to the mesh

      :type: float in [-50, 50], default 0.0

   .. attribute:: displace_type

      :type: enum in ['DISPLACE', 'DEPTH'], default 'DISPLACE'

   .. attribute:: dissolve_speed

      Approximately in how many frames should dissolve happen

      :type: int in [1, 10000], default 0

   .. attribute:: drip_acceleration

      How much surface acceleration affects dripping

      :type: float in [-200, 200], default 0.0

   .. attribute:: drip_velocity

      How much surface velocity affects dripping

      :type: float in [-200, 200], default 0.0

   .. attribute:: dry_speed

      Approximately in how many frames should drying happen

      :type: int in [1, 10000], default 0

   .. attribute:: effect_ui

      :type: enum in ['SPREAD', 'DRIP', 'SHRINK'], default 'SPREAD'

   .. data:: effector_weights

      :type: :class:`EffectorWeights`, (readonly)

   .. attribute:: frame_end

      Simulation end frame

      :type: int in [1, 1048574], default 0

   .. attribute:: frame_start

      Simulation start frame

      :type: int in [1, 1048574], default 0

   .. attribute:: frame_substeps

      Do extra frames between scene frames to ensure smooth motion

      :type: int in [0, 20], default 0

   .. attribute:: image_fileformat

      :type: enum in ['PNG', 'OPENEXR'], default 'PNG'

   .. attribute:: image_output_path

      Directory to save the textures

      :type: string, default "", (never None)

   .. attribute:: image_resolution

      Output image resolution

      :type: int in [16, 4096], default 0

   .. attribute:: init_color

      Initial color of the surface

      :type: float array of 4 items in [0, inf], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: init_color_type

      :type: enum in ['NONE', 'COLOR', 'TEXTURE', 'VERTEX_COLOR'], default 'NONE'

   .. attribute:: init_layername

      :type: string, default "", (never None)

   .. attribute:: init_texture

      :type: :class:`Texture`

   .. attribute:: is_active

      Toggle whether surface is processed or ignored

      :type: boolean, default False

   .. data:: is_cache_user

      :type: boolean, default False, (readonly)

   .. attribute:: name

      Surface name

      :type: string, default "", (never None)

   .. attribute:: output_name_a

      Name used to save output from this surface

      :type: string, default "", (never None)

   .. attribute:: output_name_b

      Name used to save output from this surface

      :type: string, default "", (never None)

   .. data:: point_cache

      :type: :class:`PointCache`, (readonly, never None)

   .. attribute:: preview_id

      :type: enum in ['PAINT', 'WETMAP'], default 'PAINT'

   .. attribute:: show_preview

      Display surface preview in 3D-views

      :type: boolean, default False

   .. attribute:: shrink_speed

      How fast shrink effect moves on the canvas surface

      :type: float in [0.001, 10], default 0.0

   .. attribute:: spread_speed

      How fast spread effect moves on the canvas surface

      :type: float in [0.001, 10], default 0.0

   .. attribute:: surface_format

      Surface Format

      :type: enum in ['VERTEX', 'IMAGE'], default 'VERTEX'

   .. attribute:: surface_type

      Surface Type

      :type: enum in ['PAINT'], default 'PAINT'

   .. attribute:: use_antialiasing

      Use 5x multisampling to smooth paint edges

      :type: boolean, default False

   .. data:: use_color_preview

      Whether this surface has some color preview for 3D view

      :type: boolean, default False, (readonly)

   .. attribute:: use_dissolve

      Enable to make surface changes disappear over time

      :type: boolean, default False

   .. attribute:: use_dissolve_log

      Use logarithmic dissolve (makes high values to fade faster than low values)

      :type: boolean, default False

   .. attribute:: use_drip

      Process drip effect (drip wet paint to gravity direction)

      :type: boolean, default False

   .. attribute:: use_dry_log

      Use logarithmic drying (makes high values to dry faster than low values)

      :type: boolean, default False

   .. attribute:: use_drying

      Enable to make surface wetness dry over time

      :type: boolean, default False

   .. attribute:: use_incremental_displace

      New displace is added cumulatively on top of existing

      :type: boolean, default False

   .. attribute:: use_output_a

      Save this output layer

      :type: boolean, default False

   .. attribute:: use_output_b

      Save this output layer

      :type: boolean, default False

   .. attribute:: use_premultiply

      Multiply color by alpha (recommended for Blender input)

      :type: boolean, default False

   .. attribute:: use_shrink

      Process shrink effect (shrink paint areas)

      :type: boolean, default False

   .. attribute:: use_spread

      Process spread effect (spread wet paint around surface)

      :type: boolean, default False

   .. attribute:: use_wave_open_border

      Pass waves through mesh edges

      :type: boolean, default False

   .. attribute:: uv_layer

      UV map name

      :type: string, default "", (never None)

   .. attribute:: wave_damping

      Wave damping factor

      :type: float in [0, 1], default 0.0

   .. attribute:: wave_smoothness

      Limit maximum steepness of wave slope between simulation points (use higher values for smoother waves at expense of reduced detail)

      :type: float in [0, 10], default 0.0

   .. attribute:: wave_speed

      Wave propagation speed

      :type: float in [0.01, 5], default 0.0

   .. attribute:: wave_spring

      Spring force that pulls water level back to zero

      :type: float in [0, 1], default 0.0

   .. attribute:: wave_timescale

      Wave time scaling factor

      :type: float in [0.01, 3], default 0.0

   .. method:: output_exists(object, index)

      Checks if surface output layer of given name exists

      :type object: :class:`Object`, (never None)
      :arg index:

         Index

      :type index: int in [0, 1]
      :rtype: boolean

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

   * :class:`DynamicPaintCanvasSettings.canvas_surfaces`
   * :class:`DynamicPaintSurfaces.active`


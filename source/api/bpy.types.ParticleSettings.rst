ParticleSettings(ID)
====================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: ParticleSettings(ID)

   Particle settings, reusable by multiple particle systems

   .. data:: active_dupliweight

      :type: :class:`ParticleDupliWeight`, (readonly)

   .. attribute:: active_dupliweight_index

      :type: int in [0, inf], default 0

   .. attribute:: active_texture

      Active texture slot being displayed

      :type: :class:`Texture`

   .. attribute:: active_texture_index

      Index of active texture slot

      :type: int in [0, 17], default 0

   .. attribute:: adaptive_angle

      How many degrees path has to curve to make another render segment

      :type: int in [0, 45], default 0

   .. attribute:: adaptive_pixel

      How many pixels path has to cover to make another render segment

      :type: int in [0, 50], default 0

   .. attribute:: angular_velocity_factor

      Angular velocity amount (in radians per second)

      :type: float in [-200, 200], default 0.0

   .. attribute:: angular_velocity_mode

      What axis is used to change particle rotation with time

      :type: enum in ['NONE', 'VELOCITY', 'HORIZONTAL', 'VERTICAL', 'GLOBAL_X', 'GLOBAL_Y', 'GLOBAL_Z', 'RAND'], default 'NONE'

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. attribute:: apply_effector_to_children

      Apply effectors to children

      :type: boolean, default False

   .. attribute:: apply_guide_to_children

      :type: boolean, default False

   .. attribute:: bending_random

      Random stiffness of hairs

      :type: float in [0, 1], default 0.0

   .. attribute:: billboard_align

      In respect to what the billboards are aligned

      :type: enum in ['X', 'Y', 'Z', 'VIEW', 'VEL'], default 'X'

   .. attribute:: billboard_animation

      How to animate billboard textures

      :type: enum in ['NONE', 'AGE', 'FRAME', 'ANGLE'], default 'NONE'

   .. attribute:: billboard_object

      Billboards face this object (default is active camera)

      :type: :class:`Object`

   .. attribute:: billboard_offset

      :type: float array of 2 items in [-100, 100], default (0.0, 0.0)

   .. attribute:: billboard_offset_split

      How to offset billboard textures

      :type: enum in ['NONE', 'LINEAR', 'RANDOM'], default 'NONE'

   .. attribute:: billboard_size

      Scale billboards relative to particle size

      :type: float array of 2 items in [0.001, 10], default (0.0, 0.0)

   .. attribute:: billboard_tilt

      Tilt of the billboards

      :type: float in [-1, 1], default 0.0

   .. attribute:: billboard_tilt_random

      Random tilt of the billboards

      :type: float in [0, 1], default 0.0

   .. attribute:: billboard_uv_split

      Number of rows/columns to split UV coordinates for billboards

      :type: int in [1, 100], default 0

   .. attribute:: billboard_velocity_head

      Scale billboards by velocity

      :type: float in [0, 10], default 0.0

   .. attribute:: billboard_velocity_tail

      Scale billboards by velocity

      :type: float in [0, 10], default 0.0

   .. data:: boids

      :type: :class:`BoidSettings`, (readonly)

   .. attribute:: branch_threshold

      Threshold of branching

      :type: float in [0, 1], default 0.0

   .. attribute:: brownian_factor

      Amount of random, erratic particle movement

      :type: float in [0, 200], default 0.0

   .. attribute:: child_length

      Length of child paths

      :type: float in [0, 1], default 0.0

   .. attribute:: child_length_threshold

      Amount of particles left untouched by child path length

      :type: float in [0, 1], default 0.0

   .. attribute:: child_nbr

      Number of children/parent

      :type: int in [0, 100000], default 0

   .. attribute:: child_parting_factor

      Create parting in the children based on parent strands

      :type: float in [0, 1], default 0.0

   .. attribute:: child_parting_max

      Maximum root to tip angle (tip distance/root distance for long hair)

      :type: float in [0, 180], default 0.0

   .. attribute:: child_parting_min

      Minimum root to tip angle (tip distance/root distance for long hair)

      :type: float in [0, 180], default 0.0

   .. attribute:: child_radius

      Radius of children around parent

      :type: float in [0, 10], default 0.0

   .. attribute:: child_roundness

      Roundness of children around parent

      :type: float in [0, 1], default 0.0

   .. attribute:: child_size

      A multiplier for the child particle size

      :type: float in [0.001, 100000], default 0.0

   .. attribute:: child_size_random

      Random variation to the size of the child particles

      :type: float in [0, 1], default 0.0

   .. attribute:: child_type

      Create child particles

      :type: enum in ['NONE', 'SIMPLE', 'INTERPOLATED'], default 'NONE'

   .. data:: clump_curve

      Curve defining clump tapering

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: clump_factor

      Amount of clumping

      :type: float in [-1, 1], default 0.0

   .. attribute:: clump_noise_size

      Size of clump noise

      :type: float in [1e-05, 100000], default 0.0

   .. attribute:: clump_shape

      Shape of clumping

      :type: float in [-0.999, 0.999], default 0.0

   .. attribute:: collision_group

      Limit colliders to this Group

      :type: :class:`Group`

   .. attribute:: color_maximum

      Maximum length of the particle color vector

      :type: float in [0.01, 100], default 0.0

   .. attribute:: count

      Total number of particles

      :type: int in [0, 10000000], default 0

   .. attribute:: courant_target

      The relative distance a particle can move before requiring more subframes (target Courant number); 0.01-0.3 is the recommended range

      :type: float in [0.0001, 10], default 0.1

   .. attribute:: create_long_hair_children

      Calculate children that suit long hair well

      :type: boolean, default False

   .. data:: cycles

      Cycles hair settings

      :type: :class:`CyclesCurveSettings`, (readonly)

   .. attribute:: damping

      Amount of damping

      :type: float in [0, 1], default 0.0

   .. attribute:: distribution

      How to distribute particles on selected element

      :type: enum in ['JIT', 'RAND', 'GRID'], default 'JIT'

   .. attribute:: drag_factor

      Amount of air-drag

      :type: float in [0, 1], default 0.0

   .. attribute:: draw_color

      Draw additional particle data as a color

      :type: enum in ['NONE', 'MATERIAL', 'VELOCITY', 'ACCELERATION'], default 'NONE'

   .. attribute:: draw_method

      How particles are drawn in viewport

      :type: enum in ['NONE', 'RENDER', 'DOT', 'CIRC', 'CROSS', 'AXIS'], default 'NONE'

   .. attribute:: draw_percentage

      Percentage of particles to display in 3D view

      :type: int in [0, 100], default 0

   .. attribute:: draw_size

      Size of particles on viewport in pixels (0=default)

      :type: int in [0, 1000], default 0

   .. attribute:: draw_step

      How many steps paths are drawn with (power of 2)

      :type: int in [0, 10], default 0

   .. attribute:: dupli_group

      Show Objects in this Group in place of particles

      :type: :class:`Group`

   .. attribute:: dupli_object

      Show this Object in place of particles

      :type: :class:`Object`

   .. data:: dupli_weights

      Weights for all of the objects in the dupli group

      :type: :class:`bpy_prop_collection` of :class:`ParticleDupliWeight`, (readonly)

   .. attribute:: effect_hair

      Hair stiffness for effectors

      :type: float in [0, 1], default 0.0

   .. attribute:: effector_amount

      How many particles are effectors (0 is all particles)

      :type: int in [0, 10000], default 0

   .. data:: effector_weights

      :type: :class:`EffectorWeights`, (readonly)

   .. attribute:: emit_from

      Where to emit particles from

      :type: enum in ['VERT', 'FACE', 'VOLUME'], default 'VERT'

   .. attribute:: factor_random

      Give the starting velocity a random variation

      :type: float in [0, 200], default 0.0

   .. data:: fluid

      :type: :class:`SPHFluidSettings`, (readonly)

   .. data:: force_field_1

      :type: :class:`FieldSettings`, (readonly)

   .. data:: force_field_2

      :type: :class:`FieldSettings`, (readonly)

   .. attribute:: frame_end

      Frame number to stop emitting particles

      :type: float in [-1.04857e+06, 1.04857e+06], default 0.0

   .. attribute:: frame_start

      Frame number to start emitting particles

      :type: float in [-1.04857e+06, 1.04857e+06], default 0.0

   .. attribute:: grid_random

      Add random offset to the grid locations

      :type: float in [0, 1], default 0.0

   .. attribute:: grid_resolution

      The resolution of the particle grid

      :type: int in [1, 250], default 0

   .. attribute:: hair_length

      Length of the hair

      :type: float in [0, 1000], default 0.0

   .. attribute:: hair_step

      Number of hair segments

      :type: int in [2, 32767], default 0

   .. attribute:: hexagonal_grid

      Create the grid in a hexagonal pattern

      :type: boolean, default False

   .. attribute:: integrator

      Algorithm used to calculate physics, from the fastest to the most stable/accurate: Midpoint, Euler, Verlet, RK4 (Old)

      :type: enum in ['EULER', 'VERLET', 'MIDPOINT', 'RK4'], default 'EULER'

   .. attribute:: invert_grid

      Invert what is considered object and what is not

      :type: boolean, default False

   .. data:: is_fluid

      Particles were created by a fluid simulation

      :type: boolean, default False, (readonly)

   .. attribute:: jitter_factor

      Amount of jitter applied to the sampling

      :type: float in [0, 2], default 0.0

   .. attribute:: keyed_loops

      Number of times the keys are looped

      :type: int in [1, 10000], default 0

   .. attribute:: keys_step

      :type: int in [0, 32767], default 0

   .. attribute:: kink

      Type of periodic offset on the path

      :type: enum in ['NO', 'CURL', 'RADIAL', 'WAVE', 'BRAID', 'SPIRAL'], default 'NO'

   .. attribute:: kink_amplitude

      The amplitude of the offset

      :type: float in [-100000, 100000], default 0.0

   .. attribute:: kink_amplitude_clump

      How much clump affects kink amplitude

      :type: float in [0, 1], default 0.0

   .. attribute:: kink_amplitude_random

      Random variation of the amplitude

      :type: float in [0, 1], default 0.0

   .. attribute:: kink_axis

      Which axis to use for offset

      :type: enum in ['X', 'Y', 'Z'], default 'X'

   .. attribute:: kink_axis_random

      Random variation of the orientation

      :type: float in [0, 1], default 0.0

   .. attribute:: kink_extra_steps

      Extra steps for resolution of special kink features

      :type: int in [1, inf], default 0

   .. attribute:: kink_flat

      How flat the hairs are

      :type: float in [0, 1], default 0.0

   .. attribute:: kink_frequency

      The frequency of the offset (1/total length)

      :type: float in [-100000, 100000], default 0.0

   .. attribute:: kink_shape

      Adjust the offset to the beginning/end

      :type: float in [-0.999, 0.999], default 0.0

   .. attribute:: length_random

      Give path length a random variation

      :type: float in [0, 1], default 0.0

   .. attribute:: lifetime

      Life span of the particles

      :type: float in [1, 1.04857e+06], default 0.0

   .. attribute:: lifetime_random

      Give the particle life a random variation

      :type: float in [0, 1], default 0.0

   .. attribute:: line_length_head

      Length of the line's head

      :type: float in [0, 100000], default 0.0

   .. attribute:: line_length_tail

      Length of the line's tail

      :type: float in [0, 100000], default 0.0

   .. attribute:: lock_billboard

      Lock the billboards align axis

      :type: boolean, default False

   .. attribute:: lock_boids_to_surface

      Constrain boids to a surface

      :type: boolean, default False

   .. attribute:: mass

      Mass of the particles

      :type: float in [1e-08, 100000], default 0.0

   .. attribute:: material

      Index of material slot used for rendering particles

      :type: int in [1, 32767], default 0

   .. attribute:: material_slot

      Material slot used for rendering particles

      :type: enum in ['DUMMY'], default 'DUMMY'

   .. attribute:: normal_factor

      Let the surface normal give the particle a starting velocity

      :type: float in [-1000, 1000], default 0.0

   .. attribute:: object_align_factor

      Let the emitter object orientation give the particle a starting velocity

      :type: float array of 3 items in [-200, 200], default (0.0, 0.0, 0.0)

   .. attribute:: object_factor

      Let the object give the particle a starting velocity

      :type: float in [-200, 200], default 0.0

   .. attribute:: particle_factor

      Let the target particle give the particle a starting velocity

      :type: float in [-200, 200], default 0.0

   .. attribute:: particle_size

      The size of the particles

      :type: float in [0.001, 100000], default 0.0

   .. attribute:: path_end

      End time of drawn path

      :type: float in [-inf, inf], default 0.0

   .. attribute:: path_start

      Starting time of drawn path

      :type: float in [-inf, inf], default 0.0

   .. attribute:: phase_factor

      Rotation around the chosen orientation axis

      :type: float in [-1, 1], default 0.0

   .. attribute:: phase_factor_random

      Randomize rotation around the chosen orientation axis

      :type: float in [0, 2], default 0.0

   .. attribute:: physics_type

      Particle physics type

      :type: enum in ['NO', 'NEWTON', 'KEYED', 'BOIDS', 'FLUID'], default 'NO'

   .. attribute:: react_event

      The event of target particles to react on

      :type: enum in ['DEATH', 'COLLIDE', 'NEAR'], default 'DEATH'

   .. attribute:: reactor_factor

      Let the vector away from the target particle's location give the particle a starting velocity

      :type: float in [-10, 10], default 0.0

   .. attribute:: regrow_hair

      Regrow hair for each frame

      :type: boolean, default False

   .. attribute:: render_step

      How many steps paths are rendered with (power of 2)

      :type: int in [0, 20], default 0

   .. attribute:: render_type

      How particles are rendered

      :type: enum in ['NONE', 'HALO', 'LINE', 'PATH', 'OBJECT', 'GROUP', 'BILLBOARD'], default 'NONE'

   .. attribute:: rendered_child_count

      Number of children/parent for rendering

      :type: int in [0, 100000], default 0

   .. attribute:: rotation_factor_random

      Randomize particle orientation

      :type: float in [0, 1], default 0.0

   .. attribute:: rotation_mode

      Particle orientation axis (does not affect Explode modifier's results)

      :type: enum in ['NONE', 'NOR', 'NOR_TAN', 'VEL', 'GLOB_X', 'GLOB_Y', 'GLOB_Z', 'OB_X', 'OB_Y', 'OB_Z'], default 'NONE'

   .. attribute:: roughness_1

      Amount of location dependent rough

      :type: float in [0, 100000], default 0.0

   .. attribute:: roughness_1_size

      Size of location dependent rough

      :type: float in [0.01, 100000], default 0.0

   .. attribute:: roughness_2

      Amount of random rough

      :type: float in [0, 100000], default 0.0

   .. attribute:: roughness_2_size

      Size of random rough

      :type: float in [0.01, 100000], default 0.0

   .. attribute:: roughness_2_threshold

      Amount of particles left untouched by random rough

      :type: float in [0, 1], default 0.0

   .. data:: roughness_curve

      Curve defining roughness

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: roughness_end_shape

      Shape of end point rough

      :type: float in [0, 10], default 0.0

   .. attribute:: roughness_endpoint

      Amount of end point rough

      :type: float in [0, 100000], default 0.0

   .. attribute:: show_guide_hairs

      Show guide hairs

      :type: boolean, default False

   .. attribute:: show_hair_grid

      Show hair simulation grid

      :type: boolean, default False

   .. attribute:: show_health

      Draw boid health

      :type: boolean, default False

   .. attribute:: show_number

      Show particle number

      :type: boolean, default False

   .. attribute:: show_size

      Show particle size

      :type: boolean, default False

   .. attribute:: show_unborn

      Show particles before they are emitted

      :type: boolean, default False

   .. attribute:: show_velocity

      Show particle velocity

      :type: boolean, default False

   .. attribute:: simplify_rate

      Speed of simplification

      :type: float in [0, 1], default 0.0

   .. attribute:: simplify_refsize

      Reference size in pixels, after which simplification begins

      :type: int in [1, 32767], default 0

   .. attribute:: simplify_transition

      Transition period for fading out strands

      :type: float in [0, 1], default 0.0

   .. attribute:: simplify_viewport

      Speed of Simplification

      :type: float in [0, 0.999], default 0.0

   .. attribute:: size_random

      Give the particle size a random variation

      :type: float in [0, 1], default 0.0

   .. attribute:: subframes

      Subframes to simulate for improved stability and finer granularity simulations (dt = timestep / (subframes + 1))

      :type: int in [0, 1000], default 0

   .. attribute:: tangent_factor

      Let the surface tangent give the particle a starting velocity

      :type: float in [-1000, 1000], default 0.0

   .. attribute:: tangent_phase

      Rotate the surface tangent

      :type: float in [-1, 1], default 0.0

   .. data:: texture_slots

      Texture slots defining the mapping and influence of textures

      :type: :class:`ParticleSettingsTextureSlots` :class:`bpy_prop_collection` of :class:`ParticleSettingsTextureSlot`, (readonly)

   .. attribute:: time_tweak

      A multiplier for physics timestep (1.0 means one frame = 1/25 seconds)

      :type: float in [0, 100], default 0.0

   .. attribute:: timestep

      The simulation timestep per frame (seconds per frame)

      :type: float in [0.0001, 100], default 0.0

   .. attribute:: trail_count

      Number of trail particles

      :type: int in [1, 100000], default 0

   .. attribute:: type

      Particle Type

      :type: enum in ['EMITTER', 'HAIR'], default 'EMITTER'

   .. attribute:: use_absolute_path_time

      Path timing is in absolute frames

      :type: boolean, default False

   .. attribute:: use_adaptive_subframes

      Automatically set the number of subframes

      :type: boolean, default False

   .. attribute:: use_advanced_hair

      Use full physics calculations for growing hair

      :type: boolean, default False

   .. attribute:: use_clump_curve

      Use a curve to define clump tapering

      :type: boolean, default False

   .. attribute:: use_clump_noise

      Create random clumps around the parent

      :type: boolean, default False

   .. attribute:: use_dead

      Show particles after they have died

      :type: boolean, default False

   .. attribute:: use_die_on_collision

      Particles die when they collide with a deflector object

      :type: boolean, default False

   .. attribute:: use_dynamic_rotation

      Particle rotations are affected by collisions and effectors

      :type: boolean, default False

   .. attribute:: use_emit_random

      Emit in random order of elements

      :type: boolean, default False

   .. attribute:: use_even_distribution

      Use even distribution from faces based on face areas or edge lengths

      :type: boolean, default False

   .. attribute:: use_global_dupli

      Use object's global coordinates for duplication

      :type: boolean, default False

   .. attribute:: use_group_count

      Use object multiple times in the same group

      :type: boolean, default False

   .. attribute:: use_group_pick_random

      Pick objects from group randomly

      :type: boolean, default False

   .. attribute:: use_hair_bspline

      Interpolate hair using B-Splines

      :type: boolean, default False

   .. attribute:: use_modifier_stack

      Emit particles from mesh with modifiers applied (must use same subsurf level for viewport and render for correct results)

      :type: boolean, default False

   .. attribute:: use_multiply_size_mass

      Multiply mass by particle size

      :type: boolean, default False

   .. attribute:: use_parent_particles

      Render parent particles

      :type: boolean, default False

   .. attribute:: use_react_multiple

      React multiple times

      :type: boolean, default False

   .. attribute:: use_react_start_end

      Give birth to unreacted particles eventually

      :type: boolean, default False

   .. attribute:: use_render_adaptive

      Draw steps of the particle path

      :type: boolean, default False

   .. attribute:: use_render_emitter

      Render emitter Object also

      :type: boolean, default False

   .. attribute:: use_rotation_dupli

      Use object's rotation for duplication (global x-axis is aligned particle rotation axis)

      :type: boolean, default False

   .. attribute:: use_rotations

      Calculate particle rotations

      :type: boolean, default False

   .. attribute:: use_roughness_curve

      Use a curve to define roughness

      :type: boolean, default False

   .. attribute:: use_scale_dupli

      Use object's scale for duplication

      :type: boolean, default False

   .. attribute:: use_self_effect

      Particle effectors affect themselves

      :type: boolean, default False

   .. attribute:: use_simplify

      Remove child strands as the object becomes smaller on the screen

      :type: boolean, default False

   .. attribute:: use_simplify_viewport

      :type: boolean, default False

   .. attribute:: use_size_deflect

      Use particle's size in deflection

      :type: boolean, default False

   .. attribute:: use_strand_primitive

      Use the strand primitive for rendering

      :type: boolean, default False

   .. attribute:: use_velocity_length

      Multiply line length by particle speed

      :type: boolean, default False

   .. attribute:: use_whole_group

      Use whole group at once

      :type: boolean, default False

   .. attribute:: userjit

      Emission locations / face (0 = automatic)

      :type: int in [0, 1000], default 0

   .. attribute:: virtual_parents

      Relative amount of virtual parents

      :type: float in [0, 1], default 0.0

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
   * :class:`ID.name`
   * :class:`ID.users`
   * :class:`ID.use_fake_user`
   * :class:`ID.tag`
   * :class:`ID.is_updated`
   * :class:`ID.is_updated_data`
   * :class:`ID.is_library_indirect`
   * :class:`ID.library`
   * :class:`ID.preview`

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
   * :class:`ID.copy`
   * :class:`ID.user_clear`
   * :class:`ID.user_remap`
   * :class:`ID.make_local`
   * :class:`ID.user_of_id`
   * :class:`ID.animation_data_create`
   * :class:`ID.animation_data_clear`
   * :class:`ID.update_tag`

.. rubric:: References

.. hlist::
   :columns: 2

   * :mod:`bpy.context.particle_settings`
   * :class:`BlendData.particles`
   * :class:`BlendDataParticles.new`
   * :class:`BlendDataParticles.remove`
   * :class:`ParticleSystem.settings`


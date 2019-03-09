SmokeFlowSettings(bpy_struct)
=============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SmokeFlowSettings(bpy_struct)

   Smoke flow settings

   .. attribute:: density

      :type: float in [0, 1], default 0.0

   .. attribute:: density_vertex_group

      Name of vertex group which determines surface emission rate

      :type: string, default "", (never None)

   .. attribute:: fuel_amount

      :type: float in [0, 10], default 0.0

   .. attribute:: noise_texture

      Texture that controls emission strength

      :type: :class:`Texture`

   .. attribute:: particle_size

      Particle size in simulation cells

      :type: float in [0.1, 20], default 0.0

   .. attribute:: particle_system

      Particle systems emitted from the object

      :type: :class:`ParticleSystem`

   .. attribute:: smoke_color

      Color of smoke

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: smoke_flow_source

      Change how smoke is emitted

      * ``PARTICLES`` Particle System, Emit smoke from particles.
      * ``MESH`` Mesh, Emit smoke from mesh surface or volume.

      :type: enum in ['PARTICLES', 'MESH'], default 'PARTICLES'

   .. attribute:: smoke_flow_type

      Change how flow affects the simulation

      * ``OUTFLOW`` Outflow, Delete smoke from simulation.
      * ``SMOKE`` Smoke, Add smoke.
      * ``BOTH`` Fire + Smoke, Add fire and smoke.
      * ``FIRE`` Fire, Add fire.

      :type: enum in ['OUTFLOW', 'SMOKE', 'BOTH', 'FIRE'], default 'SMOKE'

   .. attribute:: subframes

      Number of additional samples to take between frames to improve quality of fast moving flows

      :type: int in [0, 50], default 0

   .. attribute:: surface_distance

      Maximum distance from mesh surface to emit smoke

      :type: float in [0, 10], default 0.0

   .. attribute:: temperature

      Temperature difference to ambient temperature

      :type: float in [-10, 10], default 0.0

   .. attribute:: texture_map_type

      Texture mapping type

      * ``AUTO`` Generated, Generated coordinates centered to flow object.
      * ``UV`` UV, Use UV layer for texture coordinates.

      :type: enum in ['AUTO', 'UV'], default 'AUTO'

   .. attribute:: texture_offset

      Z-offset of texture mapping

      :type: float in [0, 200], default 0.0

   .. attribute:: texture_size

      Size of texture mapping

      :type: float in [0.01, 10], default 0.0

   .. attribute:: use_absolute

      Only allow given density value in emitter area

      :type: boolean, default False

   .. attribute:: use_initial_velocity

      Smoke has some initial velocity when it is emitted

      :type: boolean, default False

   .. attribute:: use_particle_size

      Set particle size in simulation cells or use nearest cell

      :type: boolean, default False

   .. attribute:: use_texture

      Use a texture to control emission strength

      :type: boolean, default False

   .. attribute:: uv_layer

      UV map name

      :type: string, default "", (never None)

   .. attribute:: velocity_factor

      Multiplier of source velocity passed to smoke

      :type: float in [-100, 100], default 0.0

   .. attribute:: velocity_normal

      Amount of normal directional velocity

      :type: float in [-100, 100], default 0.0

   .. attribute:: velocity_random

      Amount of random velocity

      :type: float in [0, 10], default 0.0

   .. attribute:: volume_density

      Factor for smoke emitted from inside the mesh volume

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

   * :class:`SmokeModifier.flow_settings`


BoidSettings(bpy_struct)
========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BoidSettings(bpy_struct)

   Settings for boid physics

   .. attribute:: accuracy

      Accuracy of attack

      :type: float in [0, 1], default 0.0

   .. data:: active_boid_state

      :type: :class:`BoidRule`, (readonly)

   .. attribute:: active_boid_state_index

      :type: int in [0, inf], default 0

   .. attribute:: aggression

      Boid will fight this times stronger enemy

      :type: float in [0, 100], default 0.0

   .. attribute:: air_acc_max

      Maximum acceleration in air (relative to maximum speed)

      :type: float in [0, 1], default 0.0

   .. attribute:: air_ave_max

      Maximum angular velocity in air (relative to 180 degrees)

      :type: float in [0, 1], default 0.0

   .. attribute:: air_personal_space

      Radius of boids personal space in air (% of particle size)

      :type: float in [0, 10], default 0.0

   .. attribute:: air_speed_max

      Maximum speed in air

      :type: float in [0, 100], default 0.0

   .. attribute:: air_speed_min

      Minimum speed in air (relative to maximum speed)

      :type: float in [0, 1], default 0.0

   .. attribute:: bank

      Amount of rotation around velocity vector on turns

      :type: float in [0, 2], default 0.0

   .. attribute:: health

      Initial boid health when born

      :type: float in [0, 100], default 0.0

   .. attribute:: height

      Boid height relative to particle size

      :type: float in [0, 2], default 0.0

   .. attribute:: land_acc_max

      Maximum acceleration on land (relative to maximum speed)

      :type: float in [0, 1], default 0.0

   .. attribute:: land_ave_max

      Maximum angular velocity on land (relative to 180 degrees)

      :type: float in [0, 1], default 0.0

   .. attribute:: land_jump_speed

      Maximum speed for jumping

      :type: float in [0, 100], default 0.0

   .. attribute:: land_personal_space

      Radius of boids personal space on land (% of particle size)

      :type: float in [0, 10], default 0.0

   .. attribute:: land_smooth

      How smoothly the boids land

      :type: float in [0, 10], default 0.0

   .. attribute:: land_speed_max

      Maximum speed on land

      :type: float in [0, 100], default 0.0

   .. attribute:: land_stick_force

      How strong a force must be to start effecting a boid on land

      :type: float in [0, 1000], default 0.0

   .. attribute:: pitch

      Amount of rotation around side vector

      :type: float in [0, 2], default 0.0

   .. attribute:: range

      Maximum distance from which a boid can attack

      :type: float in [0, 100], default 0.0

   .. data:: states

      :type: :class:`bpy_prop_collection` of :class:`BoidState`, (readonly)

   .. attribute:: strength

      Maximum caused damage on attack per second

      :type: float in [0, 100], default 0.0

   .. attribute:: use_climb

      Allow boids to climb goal objects

      :type: boolean, default False

   .. attribute:: use_flight

      Allow boids to move in air

      :type: boolean, default False

   .. attribute:: use_land

      Allow boids to move on land

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

   * :class:`ParticleSettings.boids`


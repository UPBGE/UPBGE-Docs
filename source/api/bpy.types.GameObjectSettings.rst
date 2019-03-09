GameObjectSettings(bpy_struct)
==============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GameObjectSettings(bpy_struct)

   Game engine related settings for the object

   .. data:: activity_culling

      :type: :class:`ObjectActivityCulling`, (readonly, never None)

   .. data:: actuators

      Game engine actuators to act on events

      :type: :class:`bpy_prop_collection` of :class:`Actuator`, (readonly)

   .. attribute:: angular_velocity_max

      Clamp angular velocity to this maximum speed, in angle per second

      :type: float in [0, 1000], default 0.0

   .. attribute:: angular_velocity_min

      Clamp angular velocity to this minimum speed (except when totally still), in angle per second

      :type: float in [0, 1000], default 0.0

   .. attribute:: collision_bounds_type

      Select the collision shape that better fits the object

      :type: enum in ['BOX', 'SPHERE', 'CYLINDER', 'CONE', 'CONVEX_HULL', 'TRIANGLE_MESH', 'CAPSULE', 'Empty'], default 'BOX'

   .. attribute:: collision_group

      The collision group of the object

      :type: boolean array of 16 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

   .. attribute:: collision_margin

      Extra margin around object for collision detection, small amount required for stability. In most cases margin can be set to 0.0 for static/not moving objects.If you have jittering, decrease the margin

      :type: float in [0, 1], default 0.04

   .. attribute:: collision_mask

      The groups this object can collide with

      :type: boolean array of 16 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

   .. data:: components

      Game engine components

      :type: :class:`bpy_prop_collection` of :class:`PythonComponent`, (readonly)

   .. data:: controllers

      Game engine controllers to process events, connecting sensors to actuators

      :type: :class:`bpy_prop_collection` of :class:`Controller`, (readonly)

   .. attribute:: damping

      General movement damping

      :type: float in [0, 1], default 0.04

   .. attribute:: elasticity

      Elasticity of collisions

      :type: float in [0, 1], default 0.0

   .. attribute:: fall_speed

      Maximum speed at which the character will fall

      :type: float in [0, 1000], default 55.0

   .. attribute:: fh_damping

      Damping of the spring force, when inside the physics distance area

      :type: float in [0, 1], default 0.0

   .. attribute:: fh_distance

      Distance of the physics area

      :type: float in [0, 20], default 0.0

   .. attribute:: fh_force

      Upward spring force, when inside the physics distance area

      :type: float in [0, 1], default 0.0

   .. attribute:: form_factor

      Form factor scales the inertia tensor

      :type: float in [0, 1000], default 0.4

   .. attribute:: friction

      Coulomb friction coefficient, when inside the physics distance area

      :type: float in [0, 100], default 0.0

   .. attribute:: friction_coefficients

      Relative friction coefficients in the in the X, Y and Z directions, when anisotropic friction is enabled

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: jump_max

      The maximum number of jumps the character can make before it hits the ground

      :type: int in [1, 255], default 1

   .. attribute:: jump_speed

      Upward velocity applied to the character when jumping

      :type: float in [0, 1000], default 10.0

   .. attribute:: lock_location_x

      Disable simulation of linear motion along the X axis

      :type: boolean, default False

   .. attribute:: lock_location_y

      Disable simulation of linear motion along the Y axis

      :type: boolean, default False

   .. attribute:: lock_location_z

      Disable simulation of linear motion along the Z axis

      :type: boolean, default False

   .. attribute:: lock_rotation_x

      Disable simulation of angular motion along the X axis

      :type: boolean, default False

   .. attribute:: lock_rotation_y

      Disable simulation of angular motion along the Y axis

      :type: boolean, default False

   .. attribute:: lock_rotation_z

      Disable simulation of angular motion along the Z axis

      :type: boolean, default False

   .. attribute:: mass

      Mass of the object

      :type: float in [0.01, 1e+06], default 1.0

   .. attribute:: max_slope

      Maximum slope angle which the character will climb

      :type: float in [0, 1.5708], default 1.5708

   .. attribute:: obstacle_radius

      Radius of object representation in obstacle simulation

      :type: float in [0, 1000], default 1.0

   .. attribute:: physics_type

      Select the type of physical representation

      * ``NO_COLLISION`` No Collision, Disable collision for this object.
      * ``STATIC`` Static, Stationary object.
      * ``DYNAMIC`` Dynamic, Linear physics.
      * ``RIGID_BODY`` Rigid Body, Linear and angular physics.
      * ``SOFT_BODY`` Soft Body, Soft body.
      * ``OCCLUDER`` Occluder, Occluder for optimizing scene rendering.
      * ``SENSOR`` Sensor, Collision Sensor, detects static and dynamic objects but not the other collision sensor objects.
      * ``NAVMESH`` Navigation Mesh, Navigation mesh.
      * ``CHARACTER`` Character, Simple kinematic physics appropriate for game characters.

      :type: enum in ['NO_COLLISION', 'STATIC', 'DYNAMIC', 'RIGID_BODY', 'SOFT_BODY', 'OCCLUDER', 'SENSOR', 'NAVMESH', 'CHARACTER'], default 'STATIC'

   .. attribute:: predefined_bound

      Predefined mesh bounding volume used when Auto Update Bound is disable

      :type: :class:`Mesh`

   .. data:: properties

      Game engine properties

      :type: :class:`bpy_prop_collection` of :class:`GameProperty`, (readonly)

   .. attribute:: radius

      Radius of bounding sphere and material physics

      :type: float in [0.01, inf], default 1.0

   .. attribute:: rolling_friction

      Coulomb friction coefficient of rounded shapes

      :type: float in [0, 100], default 0.0

   .. attribute:: rotation_damping

      General rotation damping

      :type: float in [0, 1], default 0.1

   .. data:: sensors

      Game engine sensor to detect events

      :type: :class:`bpy_prop_collection` of :class:`Sensor`, (readonly)

   .. attribute:: show_actuators

      Shows actuators for this object in the user interface

      :type: boolean, default False

   .. attribute:: show_controllers

      Shows controllers for this object in the user interface

      :type: boolean, default False

   .. attribute:: show_debug_state

      Print state debug info in the game engine

      :type: boolean, default False

   .. attribute:: show_sensors

      Shows sensors for this object in the user interface

      :type: boolean, default False

   .. attribute:: show_state_panel

      Show state panel

      :type: boolean, default False

   .. data:: soft_body

      Settings for Bullet soft body simulation

      :type: :class:`GameSoftBodySettings`, (readonly)

   .. attribute:: states_initial

      Initial state when the game starts

      :type: boolean array of 30 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

   .. attribute:: states_visible

      State determining which controllers are displayed

      :type: boolean array of 30 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

   .. attribute:: step_height

      Maximum height of steps the character can run over

      :type: float in [0.01, 1], default 0.15

   .. attribute:: use_actor

      Object is detected by the Near and Radar sensor

      :type: boolean, default False

   .. attribute:: use_all_states

      Set all state bits

      :type: boolean, default False

   .. attribute:: use_anisotropic_friction

      Enable anisotropic friction

      :type: boolean, default False

   .. attribute:: use_collision_bounds

      Specify a collision bounds type other than the default

      :type: boolean, default False

   .. attribute:: use_collision_compound

      Add children to form a compound collision object

      :type: boolean, default False

   .. attribute:: use_fh_normal

      Align dynamic game objects along the surface normal, when inside the physics distance area

      :type: boolean, default False

   .. attribute:: use_ghost

      Object does not react to collisions, like a ghost

      :type: boolean, default False

   .. attribute:: use_obstacle_create

      Create representation for obstacle simulation

      :type: boolean, default False

   .. attribute:: use_physics_fh

      React to force field physics settings

      :type: boolean, default False

   .. attribute:: use_rotate_from_normal

      Use face normal to rotate object, so that it points away from the surface

      :type: boolean, default False

   .. attribute:: use_sleep

      Disable auto (de)activation in physics simulation

      :type: boolean, default False

   .. data:: used_states

      States which are being used by controllers

      :type: boolean array of 30 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False), (readonly)

   .. attribute:: velocity_max

      Clamp velocity to this maximum speed, in distance per second

      :type: float in [0, 1000], default 0.0

   .. attribute:: velocity_min

      Clamp velocity to this minimum speed (except when totally still), in distance per second

      :type: float in [0, 1000], default 0.0

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

   * :class:`Object.game`


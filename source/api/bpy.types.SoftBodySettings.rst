SoftBodySettings(bpy_struct)
============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SoftBodySettings(bpy_struct)

   Soft body simulation settings for an object

   .. attribute:: aero

      Make edges 'sail'

      :type: int in [0, 30000], default 0

   .. attribute:: aerodynamics_type

      Method of calculating aerodynamic interaction

      * ``SIMPLE`` Simple, Edges receive a drag force from surrounding media.
      * ``LIFT_FORCE`` Lift Force, Edges receive a lift force when passing through surrounding media.

      :type: enum in ['SIMPLE', 'LIFT_FORCE'], default 'SIMPLE'

   .. attribute:: ball_damp

      Blending to inelastic collision

      :type: float in [0.001, 1], default 0.0

   .. attribute:: ball_size

      Absolute ball size or factor if not manually adjusted

      :type: float in [-10, 10], default 0.0

   .. attribute:: ball_stiff

      Ball inflating pressure

      :type: float in [0.001, 100], default 0.0

   .. attribute:: bend

      Bending Stiffness

      :type: float in [0, 10], default 0.0

   .. attribute:: choke

      'Viscosity' inside collision target

      :type: int in [0, 100], default 0

   .. attribute:: collision_group

      Limit colliders to this Group

      :type: :class:`Group`

   .. attribute:: collision_type

      Choose Collision Type

      * ``MANUAL`` Manual, Manual adjust.
      * ``AVERAGE`` Average, Average Spring length \* Ball Size.
      * ``MINIMAL`` Minimal, Minimal Spring length \* Ball Size.
      * ``MAXIMAL`` Maximal, Maximal Spring length \* Ball Size.
      * ``MINMAX`` AvMinMax, (Min+Max)/2 \* Ball Size.

      :type: enum in ['MANUAL', 'AVERAGE', 'MINIMAL', 'MAXIMAL', 'MINMAX'], default 'MANUAL'

   .. attribute:: damping

      Edge spring friction

      :type: float in [0, 50], default 0.0

   .. data:: effector_weights

      :type: :class:`EffectorWeights`, (readonly)

   .. attribute:: error_threshold

      The Runge-Kutta ODE solver error limit, low value gives more precision, high values speed

      :type: float in [0.001, 10], default 0.0

   .. attribute:: friction

      General media friction for point movements

      :type: float in [0, 50], default 0.0

   .. attribute:: fuzzy

      Fuzziness while on collision, high values make collision handling faster but less stable

      :type: int in [1, 100], default 0

   .. attribute:: goal_default

      Default Goal (vertex target position) value

      :type: float in [0, 1], default 0.0

   .. attribute:: goal_friction

      Goal (vertex target position) friction

      :type: float in [0, 50], default 0.0

   .. attribute:: goal_max

      Goal maximum, vertex weights are scaled to match this range

      :type: float in [0, 1], default 0.0

   .. attribute:: goal_min

      Goal minimum, vertex weights are scaled to match this range

      :type: float in [0, 1], default 0.0

   .. attribute:: goal_spring

      Goal (vertex target position) spring stiffness

      :type: float in [0, 0.999], default 0.0

   .. attribute:: gravity

      Apply gravitation to point movement

      :type: float in [-10, 10], default 0.0

   .. attribute:: location_mass_center

      Location of Center of mass

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: mass

      General Mass value

      :type: float in [0, 50000], default 0.0

   .. attribute:: plastic

      Permanent deform

      :type: int in [0, 100], default 0

   .. attribute:: pull

      Edge spring stiffness when longer than rest length

      :type: float in [0, 0.999], default 0.0

   .. attribute:: push

      Edge spring stiffness when shorter than rest length

      :type: float in [0, 0.999], default 0.0

   .. attribute:: rotation_estimate

      Estimated rotation matrix

      :type: float multi-dimensional array of 3 * 3 items in [-inf, inf], default ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))

   .. attribute:: scale_estimate

      Estimated scale matrix

      :type: float multi-dimensional array of 3 * 3 items in [-inf, inf], default ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))

   .. attribute:: shear

      Shear Stiffness

      :type: float in [0, 1], default 0.0

   .. attribute:: speed

      Tweak timing for physics to control frequency and speed

      :type: float in [0.01, 100], default 0.0

   .. attribute:: spring_length

      Alter spring length to shrink/blow up (unit %) 0 to disable

      :type: int in [0, 200], default 0

   .. attribute:: step_max

      Maximal # solver steps/frame

      :type: int in [0, 30000], default 0

   .. attribute:: step_min

      Minimal # solver steps/frame

      :type: int in [0, 30000], default 0

   .. attribute:: use_auto_step

      Use velocities for automagic step sizes

      :type: boolean, default False

   .. attribute:: use_diagnose

      Turn on SB diagnose console prints

      :type: boolean, default False

   .. attribute:: use_edge_collision

      Edges collide too

      :type: boolean, default False

   .. attribute:: use_edges

      Use Edges as springs

      :type: boolean, default False

   .. attribute:: use_estimate_matrix

      Estimate matrix... split to COM, ROT, SCALE

      :type: boolean, default False

   .. attribute:: use_face_collision

      Faces collide too, can be very slow

      :type: boolean, default False

   .. attribute:: use_goal

      Define forces for vertices to stick to animated position

      :type: boolean, default False

   .. attribute:: use_self_collision

      Enable naive vertex ball self collision

      :type: boolean, default False

   .. attribute:: use_stiff_quads

      Add diagonal springs on 4-gons

      :type: boolean, default False

   .. attribute:: vertex_group_goal

      Control point weight values

      :type: string, default "", (never None)

   .. attribute:: vertex_group_mass

      Control point mass values

      :type: string, default "", (never None)

   .. attribute:: vertex_group_spring

      Control point spring strength values

      :type: string, default "", (never None)

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

   * :class:`Object.soft_body`
   * :class:`SoftBodyModifier.settings`


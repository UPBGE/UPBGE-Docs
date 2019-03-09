RigidBodyWorld(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: RigidBodyWorld(bpy_struct)

   Self-contained rigid body simulation environment and settings

   .. attribute:: constraints

      Group containing rigid body constraint objects

      :type: :class:`Group`

   .. data:: effector_weights

      :type: :class:`EffectorWeights`, (readonly)

   .. attribute:: enabled

      Simulation will be evaluated

      :type: boolean, default False

   .. attribute:: group

      Group containing objects participating in this simulation

      :type: :class:`Group`

   .. data:: point_cache

      :type: :class:`PointCache`, (readonly, never None)

   .. attribute:: solver_iterations

      Number of constraint solver iterations made per simulation step (higher values are more accurate but slower)

      :type: int in [1, 1000], default 10

   .. attribute:: steps_per_second

      Number of simulation steps taken per second (higher values are more accurate but slower)

      :type: int in [1, 32767], default 60

   .. attribute:: time_scale

      Change the speed of the simulation

      :type: float in [0, 100], default 1.0

   .. attribute:: use_split_impulse

      Reduce extra velocity that can build up when objects collide (lowers simulation stability a little so use only when necessary)

      :type: boolean, default False

   .. method:: convex_sweep_test(object, start, end)

      Sweep test convex rigidbody against the current rigidbody world

      :arg object:

         Rigidbody object with a convex collision shape

      :type object: :class:`Object`, (never None)
      :type start: float array of 3 items in [-inf, inf]
      :type end: float array of 3 items in [-inf, inf]
      :return (object_location, hitpoint, normal, has_hit):
         `object_location`, The hit location of this sweep test, float array of 3 items in [-inf, inf]

         `hitpoint`, The hit location of this sweep test, float array of 3 items in [-inf, inf]

         `normal`, The face normal at the sweep test hit location, float array of 3 items in [-inf, inf]

         `has_hit`, If the function has found collision point, value is 1, otherwise 0, int in [-inf, inf]


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

   * :class:`Scene.rigidbody_world`


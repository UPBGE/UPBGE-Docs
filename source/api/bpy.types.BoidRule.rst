BoidRule(bpy_struct)
====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`BoidRuleAverageSpeed`, :class:`BoidRuleAvoid`, :class:`BoidRuleAvoidCollision`, :class:`BoidRuleFight`, :class:`BoidRuleFollowLeader`, :class:`BoidRuleGoal`

.. class:: BoidRule(bpy_struct)

   

   .. attribute:: name

      Boid rule name

      :type: string, default "", (never None)

   .. data:: type

      * ``GOAL`` Goal, Go to assigned object or loudest assigned signal source.
      * ``AVOID`` Avoid, Get away from assigned object or loudest assigned signal source.
      * ``AVOID_COLLISION`` Avoid Collision, Maneuver to avoid collisions with other boids and deflector objects in near future.
      * ``SEPARATE`` Separate, Keep from going through other boids.
      * ``FLOCK`` Flock, Move to center of neighbors and match their velocity.
      * ``FOLLOW_LEADER`` Follow Leader, Follow a boid or assigned object.
      * ``AVERAGE_SPEED`` Average Speed, Maintain speed, flight level or wander.
      * ``FIGHT`` Fight, Go to closest enemy and attack when in range.

      :type: enum in ['GOAL', 'AVOID', 'AVOID_COLLISION', 'SEPARATE', 'FLOCK', 'FOLLOW_LEADER', 'AVERAGE_SPEED', 'FIGHT'], default 'GOAL', (readonly)

   .. attribute:: use_in_air

      Use rule when boid is flying

      :type: boolean, default False

   .. attribute:: use_on_land

      Use rule when boid is on land

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

   * :class:`BoidSettings.active_boid_state`
   * :class:`BoidState.active_boid_rule`
   * :class:`BoidState.rules`


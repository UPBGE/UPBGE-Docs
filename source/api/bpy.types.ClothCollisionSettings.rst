ClothCollisionSettings(bpy_struct)
==================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ClothCollisionSettings(bpy_struct)

   Cloth simulation settings for self collision and collision with other objects

   .. attribute:: collision_quality

      How many collision iterations should be done. (higher is better quality but slower)

      :type: int in [1, 32767], default 0

   .. attribute:: damping

      Amount of velocity lost on collision

      :type: float in [0, 1], default 1.0

   .. attribute:: distance_min

      Minimum distance between collision objects before collision response takes in

      :type: float in [0.001, 1], default 0.0

   .. attribute:: distance_repel

      Maximum distance to apply repulsion force, must be greater than minimum distance

      :type: float in [0.001, 10], default 0.005

   .. attribute:: friction

      Friction force if a collision happened (higher = less movement)

      :type: float in [0, 80], default 0.0

   .. attribute:: group

      Limit colliders to this Group

      :type: :class:`Group`

   .. attribute:: repel_force

      Repulsion force to apply on cloth when close to colliding

      :type: float in [0, 20], default 1.0

   .. attribute:: self_collision_quality

      How many self collision iterations should be done (higher is better quality but slower)

      :type: int in [1, 32767], default 0

   .. attribute:: self_distance_min

      0.5 means no distance at all, 1.0 is maximum distance

      :type: float in [0.5, 1], default 0.0

   .. attribute:: self_friction

      Friction/damping with self contact

      :type: float in [0, 80], default 0.0

   .. attribute:: use_collision

      Enable collisions with other objects

      :type: boolean, default False

   .. attribute:: use_self_collision

      Enable self collisions

      :type: boolean, default False

   .. attribute:: vertex_group_self_collisions

      Vertex group to define vertices which are not used during self collisions

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

   * :class:`ClothModifier.collision_settings`


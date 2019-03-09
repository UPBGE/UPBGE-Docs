CollisionSettings(bpy_struct)
=============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: CollisionSettings(bpy_struct)

   Collision settings for object in physics simulation

   .. attribute:: absorption

      How much of effector force gets lost during collision with this object (in percent)

      :type: float in [0, 1], default 0.0

   .. attribute:: damping

      Amount of damping during collision

      :type: float in [0, 1], default 0.0

   .. attribute:: damping_factor

      Amount of damping during particle collision

      :type: float in [0, 1], default 0.0

   .. attribute:: damping_random

      Random variation of damping

      :type: float in [0, 1], default 0.0

   .. attribute:: friction_factor

      Amount of friction during particle collision

      :type: float in [0, 1], default 0.0

   .. attribute:: friction_random

      Random variation of friction

      :type: float in [0, 1], default 0.0

   .. attribute:: permeability

      Chance that the particle will pass through the mesh

      :type: float in [0, 1], default 0.0

   .. attribute:: stickiness

      Amount of stickiness to surface collision

      :type: float in [0, 10], default 0.0

   .. attribute:: thickness_inner

      Inner face thickness (only used by softbodies)

      :type: float in [0.001, 1], default 0.0

   .. attribute:: thickness_outer

      Outer face thickness

      :type: float in [0.001, 1], default 0.0

   .. attribute:: use

      Enable this objects as a collider for physics systems

      :type: boolean, default False

   .. attribute:: use_particle_kill

      Kill collided particles

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

   * :class:`CollisionModifier.settings`
   * :class:`Object.collision`


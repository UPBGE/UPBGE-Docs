GameSoftBodySettings(bpy_struct)
================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GameSoftBodySettings(bpy_struct)

   Soft body simulation settings for an object in the game engine

   .. attribute:: bending_distance

      Bending Constraint Distance

      :type: int in [1, 1000], default 0

   .. attribute:: cluster_iterations

      Number of cluster iterations

      :type: int in [1, 1000], default 0

   .. attribute:: cluster_solver_iterations

      Cluster solver iterations

      :type: int in [1, 1000], default 0

   .. attribute:: collision_margin

      Collision margin for soft body. Small value makes the algorithm unstable

      :type: float in [0.01, 1], default 0.0

   .. attribute:: drift_solver_iterations

      Drift solver iterations

      :type: int in [0, 1000], default 0

   .. attribute:: dynamic_friction

      Dynamic Friction

      :type: float in [0, 1], default 0.0

   .. attribute:: kahr

      Anchors hardness

      :type: float in [0, 1], default 0.0

   .. attribute:: kchr

      Rigid contacts hardness

      :type: float in [0, 1], default 0.0

   .. attribute:: kdg

      Drag coeffient

      :type: float in [0, 1000], default 0.0

   .. attribute:: kdp

      Damping coefficient

      :type: float in [0, 1], default 0.0

   .. attribute:: kkhr

      Kinetic contacts hardness

      :type: float in [0, 1], default 0.0

   .. attribute:: klf

      Lift coefficient

      :type: float in [0, 1000], default 0.0

   .. attribute:: kpr

      Pressure coefficient

      :type: float in [-1000, 1000], default 0.0

   .. attribute:: kshr

      Soft contacts hardness

      :type: float in [0, 1], default 0.0

   .. attribute:: ksk_split_cl

      Kinetic impulse split

      :type: float in [0, 1], default 0.0

   .. attribute:: kskhr_cl

      Soft vs kinetic hardness

      :type: float in [0, 1], default 0.0

   .. attribute:: ksr_split_cl

      Rigid impulse split

      :type: float in [0, 1], default 0.0

   .. attribute:: ksrhr_cl

      Soft vs rigid hardness

      :type: float in [0, 1], default 0.0

   .. attribute:: kss_split_cl

      Soft impulse split

      :type: float in [0, 1], default 0.0

   .. attribute:: ksshr_cl

      Soft vs soft hardness

      :type: float in [0, 1], default 0.0

   .. attribute:: kvc

      Volume conservation coefficient

      :type: float in [0, 1000], default 0.0

   .. attribute:: kvcf

      Velocity correction factor

      :type: float in [0, 1], default 0.0

   .. attribute:: linear_stiffness

      Linear stiffness of the soft body links

      :type: float in [0, 1], default 0.0

   .. attribute:: position_solver_iterations

      Position solver iterations

      :type: int in [1, 1000], default 0

   .. attribute:: shape_threshold

      Shape matching threshold

      :type: float in [0, 1], default 0.0

   .. attribute:: use_bending_constraints

      Enable bending constraints

      :type: boolean, default False

   .. attribute:: use_cluster_rigid_to_softbody

      Enable cluster collision between soft and rigid body

      :type: boolean, default False

   .. attribute:: use_cluster_soft_to_softbody

      Enable cluster collision between soft and soft body

      :type: boolean, default False

   .. attribute:: use_shape_match

      Enable soft body shape matching goal

      :type: boolean, default False

   .. attribute:: velocity_solver_iterations

      Position solver iterations

      :type: int in [0, 1000], default 0

   .. attribute:: weld_threshold

      Welding threshold: distance between nearby vertices to be considered equal => set to 0.0 to disable welding test and speed up scene loading (ok if the mesh has no duplicates)

      :type: float in [0, 0.01], default 0.0

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

   * :class:`GameObjectSettings.soft_body`


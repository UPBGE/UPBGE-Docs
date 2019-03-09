ClothSettings(bpy_struct)
=========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ClothSettings(bpy_struct)

   Cloth simulation settings for an object

   .. attribute:: air_damping

      Air has normally some thickness which slows falling things down

      :type: float in [0, 10], default 0.0

   .. attribute:: bending_damping

      Damping of bending motion

      :type: float in [0, 1000], default 0.0

   .. attribute:: bending_stiffness

      Wrinkle coefficient (higher = less smaller but more big wrinkles)

      :type: float in [0, 10000], default 0.0

   .. attribute:: bending_stiffness_max

      Maximum bending stiffness value

      :type: float in [0, 10000], default 0.0

   .. attribute:: collider_friction

      :type: float in [0, 1], default 0.0

   .. attribute:: density_strength

      Influence of target density on the simulation

      :type: float in [0, 1], default 0.0

   .. attribute:: density_target

      Maximum density of hair

      :type: float in [0, 10000], default 0.0

   .. data:: effector_weights

      :type: :class:`EffectorWeights`, (readonly)

   .. attribute:: goal_default

      Default Goal (vertex target position) value, when no Vertex Group used

      :type: float in [0, 1], default 0.0

   .. attribute:: goal_friction

      Goal (vertex target position) friction

      :type: float in [0, 50], default 0.0

   .. attribute:: goal_max

      Goal maximum, vertex group weights are scaled to match this range

      :type: float in [0, 1], default 0.0

   .. attribute:: goal_min

      Goal minimum, vertex group weights are scaled to match this range

      :type: float in [0, 1], default 0.0

   .. attribute:: goal_spring

      Goal (vertex target position) spring stiffness

      :type: float in [0, 0.999], default 0.0

   .. attribute:: gravity

      Gravity or external force vector

      :type: float array of 3 items in [-100, 100], default (0.0, 0.0, 0.0)

   .. attribute:: internal_friction

      :type: float in [0, 1], default 0.0

   .. attribute:: mass

      Mass of cloth material

      :type: float in [0, 10], default 0.0

   .. attribute:: pin_stiffness

      Pin (vertex target position) spring stiffness

      :type: float in [0, 50], default 0.0

   .. attribute:: quality

      Quality of the simulation in steps per frame (higher is better quality but slower)

      :type: int in [1, inf], default 0

   .. attribute:: rest_shape_key

      Shape key to use the rest spring lengths from

      :type: :class:`ShapeKey`

   .. attribute:: sewing_force_max

      Maximum sewing force

      :type: float in [0, 10000], default 0.0

   .. attribute:: shrink_max

      Max amount to shrink cloth by

      :type: float in [0, 1], default 0.0

   .. attribute:: shrink_min

      Min amount to shrink cloth by

      :type: float in [0, 1], default 0.0

   .. attribute:: spring_damping

      Damping of cloth velocity (higher = more smooth, less jiggling)

      :type: float in [0, 50], default 0.0

   .. attribute:: structural_stiffness

      Overall stiffness of structure

      :type: float in [0, 10000], default 0.0

   .. attribute:: structural_stiffness_max

      Maximum structural stiffness value

      :type: float in [0, 10000], default 0.0

   .. attribute:: time_scale

      Cloth speed is multiplied by this value

      :type: float in [0, inf], default 0.0

   .. attribute:: use_dynamic_mesh

      Make simulation respect deformations in the base mesh

      :type: boolean, default False

   .. attribute:: use_pin_cloth

      Enable pinning of cloth vertices to other objects/positions

      :type: boolean, default False

   .. attribute:: use_sewing_springs

      Pulls loose edges together

      :type: boolean, default False

   .. attribute:: use_stiffness_scale

      If enabled, stiffness can be scaled along a weight painted vertex group

      :type: boolean, default False

   .. attribute:: vel_damping

      Damp velocity to help cloth reach the resting position faster (1.0 = no damping, 0.0 = fully dampened)

      :type: float in [0, 1], default 0.0

   .. attribute:: vertex_group_bending

      Vertex group for fine control over bending stiffness

      :type: string, default "", (never None)

   .. attribute:: vertex_group_mass

      Vertex Group for pinning of vertices

      :type: string, default "", (never None)

   .. attribute:: vertex_group_shrink

      Vertex Group for shrinking cloth

      :type: string, default "", (never None)

   .. attribute:: vertex_group_structural_stiffness

      Vertex group for fine control over structural stiffness

      :type: string, default "", (never None)

   .. attribute:: voxel_cell_size

      Size of the voxel grid cells for interaction effects

      :type: float in [0.0001, 10000], default 0.1

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

   * :class:`ClothModifier.settings`


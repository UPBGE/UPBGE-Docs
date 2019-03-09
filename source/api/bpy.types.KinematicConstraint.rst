KinematicConstraint(Constraint)
===============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: KinematicConstraint(Constraint)

   Inverse Kinematics

   .. attribute:: chain_count

      How many bones are included in the IK effect - 0 uses all bones

      :type: int in [0, 255], default 0

   .. attribute:: distance

      Radius of limiting sphere

      :type: float in [0, 100], default 0.0

   .. attribute:: ik_type

      :type: enum in ['COPY_POSE', 'DISTANCE'], default 'COPY_POSE'

   .. attribute:: iterations

      Maximum number of solving iterations

      :type: int in [0, 10000], default 0

   .. attribute:: limit_mode

      Distances in relation to sphere of influence to allow

      * ``LIMITDIST_INSIDE`` Inside, The object is constrained inside a virtual sphere around the target object, with a radius defined by the limit distance.
      * ``LIMITDIST_OUTSIDE`` Outside, The object is constrained outside a virtual sphere around the target object, with a radius defined by the limit distance.
      * ``LIMITDIST_ONSURFACE`` On Surface, The object is constrained on the surface of a virtual sphere around the target object, with a radius defined by the limit distance.

      :type: enum in ['LIMITDIST_INSIDE', 'LIMITDIST_OUTSIDE', 'LIMITDIST_ONSURFACE'], default 'LIMITDIST_INSIDE'

   .. attribute:: lock_location_x

      Constraint position along X axis

      :type: boolean, default False

   .. attribute:: lock_location_y

      Constraint position along Y axis

      :type: boolean, default False

   .. attribute:: lock_location_z

      Constraint position along Z axis

      :type: boolean, default False

   .. attribute:: lock_rotation_x

      Constraint rotation along X axis

      :type: boolean, default False

   .. attribute:: lock_rotation_y

      Constraint rotation along Y axis

      :type: boolean, default False

   .. attribute:: lock_rotation_z

      Constraint rotation along Z axis

      :type: boolean, default False

   .. attribute:: orient_weight

      For Tree-IK: Weight of orientation control for this target

      :type: float in [0.01, 1], default 0.0

   .. attribute:: pole_angle

      Pole rotation offset

      :type: float in [-3.14159, 3.14159], default 0.0

   .. attribute:: pole_subtarget

      :type: string, default "", (never None)

   .. attribute:: pole_target

      Object for pole rotation

      :type: :class:`Object`

   .. attribute:: reference_axis

      Constraint axis Lock options relative to Bone or Target reference

      :type: enum in ['BONE', 'TARGET'], default 'BONE'

   .. attribute:: subtarget

      :type: string, default "", (never None)

   .. attribute:: target

      Target Object

      :type: :class:`Object`

   .. attribute:: use_location

      Chain follows position of target

      :type: boolean, default False

   .. attribute:: use_rotation

      Chain follows rotation of target

      :type: boolean, default False

   .. attribute:: use_stretch

      Enable IK Stretching

      :type: boolean, default False

   .. attribute:: use_tail

      Include bone's tail as last element in chain

      :type: boolean, default False

   .. attribute:: weight

      For Tree-IK: Weight of position control for this target

      :type: float in [0.01, 1], default 0.0

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
   * :class:`Constraint.name`
   * :class:`Constraint.type`
   * :class:`Constraint.owner_space`
   * :class:`Constraint.target_space`
   * :class:`Constraint.mute`
   * :class:`Constraint.show_expanded`
   * :class:`Constraint.is_valid`
   * :class:`Constraint.active`
   * :class:`Constraint.is_proxy_local`
   * :class:`Constraint.influence`
   * :class:`Constraint.error_location`
   * :class:`Constraint.error_rotation`

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


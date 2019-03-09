StretchToConstraint(Constraint)
===============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: StretchToConstraint(Constraint)

   Stretch to meet the target object

   .. attribute:: bulge

      Factor between volume variation and stretching

      :type: float in [0, 100], default 0.0

   .. attribute:: bulge_max

      Maximum volume stretching factor

      :type: float in [1, 100], default 0.0

   .. attribute:: bulge_min

      Minimum volume stretching factor

      :type: float in [0, 1], default 0.0

   .. attribute:: bulge_smooth

      Strength of volume stretching clamping

      :type: float in [0, 1], default 0.0

   .. attribute:: head_tail

      Target along length of bone: Head=0, Tail=1

      :type: float in [0, 1], default 0.0

   .. attribute:: keep_axis

      Axis to maintain during stretch

      * ``PLANE_X`` X, Keep X Axis.
      * ``PLANE_Z`` Z, Keep Z Axis.

      :type: enum in ['PLANE_X', 'PLANE_Z'], default 'PLANE_X'

   .. attribute:: rest_length

      Length at rest position

      :type: float in [0, 1000], default 0.0

   .. attribute:: subtarget

      :type: string, default "", (never None)

   .. attribute:: target

      Target Object

      :type: :class:`Object`

   .. attribute:: use_bbone_shape

      Follow shape of B-Bone segments when calculating Head/Tail position

      :type: boolean, default False

   .. attribute:: use_bulge_max

      Use upper limit for volume variation

      :type: boolean, default False

   .. attribute:: use_bulge_min

      Use lower limit for volume variation

      :type: boolean, default False

   .. attribute:: volume

      Maintain the object's volume as it stretches

      :type: enum in ['VOLUME_XZX', 'VOLUME_X', 'VOLUME_Z', 'NO_VOLUME'], default 'VOLUME_XZX'

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


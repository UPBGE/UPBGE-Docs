SplineIKConstraint(Constraint)
==============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: SplineIKConstraint(Constraint)

   Align 'n' bones along a curve

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

   .. attribute:: chain_count

      How many bones are included in the chain

      :type: int in [1, 255], default 0

   .. attribute:: joint_bindings

      (EXPERIENCED USERS ONLY) The relative positions of the joints along the chain, as percentages

      :type: float array of 32 items in [0, 1], default (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

   .. attribute:: target

      Curve that controls this relationship

      :type: :class:`Object`

   .. attribute:: use_bulge_max

      Use upper limit for volume variation

      :type: boolean, default False

   .. attribute:: use_bulge_min

      Use lower limit for volume variation

      :type: boolean, default False

   .. attribute:: use_chain_offset

      Offset the entire chain relative to the root joint

      :type: boolean, default False

   .. attribute:: use_curve_radius

      Average radius of the endpoints is used to tweak the X and Z Scaling of the bones, on top of XZ Scale mode

      :type: boolean, default False

   .. attribute:: use_even_divisions

      Ignore the relative lengths of the bones when fitting to the curve

      :type: boolean, default False

   .. attribute:: use_y_stretch

      Stretch the Y axis of the bones to fit the curve

      :type: boolean, default False

   .. attribute:: xz_scale_mode

      Method used for determining the scaling of the X and Z axes of the bones

      * ``NONE`` None, Don't scale the X and Z axes (Default).
      * ``BONE_ORIGINAL`` Bone Original, Use the original scaling of the bones.
      * ``INVERSE_PRESERVE`` Inverse Scale, Scale of the X and Z axes is the inverse of the Y-Scale.
      * ``VOLUME_PRESERVE`` Volume Preservation, Scale of the X and Z axes are adjusted to preserve the volume of the bones.

      :type: enum in ['NONE', 'BONE_ORIGINAL', 'INVERSE_PRESERVE', 'VOLUME_PRESERVE'], default 'NONE'

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


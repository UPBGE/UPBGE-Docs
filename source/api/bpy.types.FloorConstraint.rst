FloorConstraint(Constraint)
===========================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: FloorConstraint(Constraint)

   Use the target object for location limitation

   .. attribute:: floor_location

      Location of target that object will not pass through

      :type: enum in ['FLOOR_X', 'FLOOR_Y', 'FLOOR_Z', 'FLOOR_NEGATIVE_X', 'FLOOR_NEGATIVE_Y', 'FLOOR_NEGATIVE_Z'], default 'FLOOR_X'

   .. attribute:: offset

      Offset of floor from object origin

      :type: float in [-inf, inf], default 0.0

   .. attribute:: subtarget

      :type: string, default "", (never None)

   .. attribute:: target

      Target Object

      :type: :class:`Object`

   .. attribute:: use_rotation

      Use the target's rotation to determine floor

      :type: boolean, default False

   .. attribute:: use_sticky

      Immobilize object while constrained

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


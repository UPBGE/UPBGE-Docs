Pose(bpy_struct)
================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Pose(bpy_struct)

   A collection of pose channels, including settings for animating bones

   .. data:: animation_visualization

      Animation data for this data-block

      :type: :class:`AnimViz`, (readonly, never None)

   .. data:: bone_groups

      Groups of the bones

      :type: :class:`BoneGroups` :class:`bpy_prop_collection` of :class:`BoneGroup`, (readonly)

   .. data:: bones

      Individual pose bones for the armature

      :type: :class:`bpy_prop_collection` of :class:`PoseBone`, (readonly)

   .. data:: ik_param

      Parameters for IK solver

      :type: :class:`IKParam`, (readonly)

   .. attribute:: ik_solver

      Selection of IK solver for IK chain

      * ``LEGACY`` Standard, Original IK solver.
      * ``ITASC`` iTaSC, Multi constraint, stateful IK solver.

      :type: enum in ['LEGACY', 'ITASC'], default 'LEGACY'

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

   * :class:`Object.pose`


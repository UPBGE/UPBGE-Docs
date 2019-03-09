ShrinkwrapConstraint(Constraint)
================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: ShrinkwrapConstraint(Constraint)

   Create constraint-based shrinkwrap relationship

   .. attribute:: distance

      Distance to Target

      :type: float in [0, inf], default 0.0

   .. attribute:: project_axis

      Axis constrain to

      :type: enum in ['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], default 'POS_X'

   .. attribute:: project_axis_space

      Space for the projection axis

      * ``WORLD`` World Space, The constraint is applied relative to the world coordinate system.
      * ``POSE`` Pose Space, The constraint is applied in Pose Space, the object transformation is ignored.
      * ``LOCAL_WITH_PARENT`` Local With Parent, The constraint is applied relative to the local coordinate system of the object, with the parent transformation added.
      * ``LOCAL`` Local Space, The constraint is applied relative to the local coordinate system of the object.

      :type: enum in ['WORLD', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL'], default 'WORLD'

   .. attribute:: project_limit

      Limit the distance used for projection (zero disables)

      :type: float in [0, inf], default 0.0

   .. attribute:: shrinkwrap_type

      Select type of shrinkwrap algorithm for target position

      * ``NEAREST_SURFACE`` Nearest Surface Point, Shrink the location to the nearest target surface.
      * ``PROJECT`` Project, Shrink the location to the nearest target surface along a given axis.
      * ``NEAREST_VERTEX`` Nearest Vertex, Shrink the location to the nearest target vertex.

      :type: enum in ['NEAREST_SURFACE', 'PROJECT', 'NEAREST_VERTEX'], default 'NEAREST_SURFACE'

   .. attribute:: target

      Target Object

      :type: :class:`Object`

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


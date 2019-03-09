TransformConstraint(Constraint)
===============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: TransformConstraint(Constraint)

   Map transformations of the target to the object

   .. attribute:: from_max_x

      Top range of X axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_max_x_rot

      Top range of X axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_max_x_scale

      Top range of X axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_max_y

      Top range of Y axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_max_y_rot

      Top range of Y axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_max_y_scale

      Top range of Y axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_max_z

      Top range of Z axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_max_z_rot

      Top range of Z axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_max_z_scale

      Top range of Z axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_min_x

      Bottom range of X axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_min_x_rot

      Bottom range of X axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_min_x_scale

      Bottom range of X axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_min_y

      Bottom range of Y axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_min_y_rot

      Bottom range of Y axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_min_y_scale

      Bottom range of Y axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_min_z

      Bottom range of Z axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_min_z_rot

      Bottom range of Z axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_min_z_scale

      Bottom range of Z axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: map_from

      The transformation type to use from the target

      :type: enum in ['LOCATION', 'ROTATION', 'SCALE'], default 'LOCATION'

   .. attribute:: map_to

      The transformation type to affect of the constrained object

      :type: enum in ['LOCATION', 'ROTATION', 'SCALE'], default 'LOCATION'

   .. attribute:: map_to_x_from

      The source axis constrained object's X axis uses

      :type: enum in ['X', 'Y', 'Z'], default 'X'

   .. attribute:: map_to_y_from

      The source axis constrained object's Y axis uses

      :type: enum in ['X', 'Y', 'Z'], default 'X'

   .. attribute:: map_to_z_from

      The source axis constrained object's Z axis uses

      :type: enum in ['X', 'Y', 'Z'], default 'X'

   .. attribute:: subtarget

      :type: string, default "", (never None)

   .. attribute:: target

      Target Object

      :type: :class:`Object`

   .. attribute:: to_max_x

      Top range of X axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_max_x_rot

      Top range of X axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_max_x_scale

      Top range of X axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_max_y

      Top range of Y axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_max_y_rot

      Top range of Y axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_max_y_scale

      Top range of Y axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_max_z

      Top range of Z axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_max_z_rot

      Top range of Z axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_max_z_scale

      Top range of Z axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_min_x

      Bottom range of X axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_min_x_rot

      Bottom range of X axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_min_x_scale

      Bottom range of X axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_min_y

      Bottom range of Y axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_min_y_rot

      Bottom range of Y axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_min_y_scale

      Bottom range of Y axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_min_z

      Bottom range of Z axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_min_z_rot

      Bottom range of Z axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_min_z_scale

      Bottom range of Z axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: use_motion_extrapolate

      Extrapolate ranges

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


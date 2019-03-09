ClothModifier(Modifier)
=======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: ClothModifier(Modifier)

   Cloth simulation modifier

   .. data:: collision_settings

      :type: :class:`ClothCollisionSettings`, (readonly, never None)

   .. data:: hair_grid_max

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. data:: hair_grid_min

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. data:: hair_grid_resolution

      :type: int array of 3 items in [-inf, inf], default (0, 0, 0), (readonly)

   .. data:: point_cache

      :type: :class:`PointCache`, (readonly, never None)

   .. data:: settings

      :type: :class:`ClothSettings`, (readonly, never None)

   .. data:: solver_result

      :type: :class:`ClothSolverResult`, (readonly)

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
   * :class:`Modifier.name`
   * :class:`Modifier.type`
   * :class:`Modifier.show_viewport`
   * :class:`Modifier.show_render`
   * :class:`Modifier.show_in_editmode`
   * :class:`Modifier.show_on_cage`
   * :class:`Modifier.show_expanded`
   * :class:`Modifier.use_apply_on_spline`

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

   * :mod:`bpy.context.cloth`
   * :class:`ParticleSystem.cloth`


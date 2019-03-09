ClothSolverResult(bpy_struct)
=============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ClothSolverResult(bpy_struct)

   Result of cloth solver iteration

   .. data:: avg_error

      Average error during substeps

      :type: float in [-inf, inf], default 0.0, (readonly)

   .. data:: avg_iterations

      Average iterations during substeps

      :type: float in [-inf, inf], default 0.0, (readonly)

   .. data:: max_error

      Maximum error during substeps

      :type: float in [-inf, inf], default 0.0, (readonly)

   .. data:: max_iterations

      Maximum iterations during substeps

      :type: int in [-inf, inf], default 0, (readonly)

   .. data:: min_error

      Minimum error during substeps

      :type: float in [-inf, inf], default 0.0, (readonly)

   .. data:: min_iterations

      Minimum iterations during substeps

      :type: int in [-inf, inf], default 0, (readonly)

   .. data:: status

      Status of the solver iteration

      * ``SUCCESS`` Success, Computation was successful.
      * ``NUMERICAL_ISSUE`` Numerical Issue, The provided data did not satisfy the prerequisites.
      * ``NO_CONVERGENCE`` No Convergence, Iterative procedure did not converge.
      * ``INVALID_INPUT`` Invalid Input, The inputs are invalid, or the algorithm has been improperly called.

      :type: enum set in {'SUCCESS', 'NUMERICAL_ISSUE', 'NO_CONVERGENCE', 'INVALID_INPUT'}, default {'SUCCESS'}, (readonly)

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

   * :class:`ClothModifier.solver_result`


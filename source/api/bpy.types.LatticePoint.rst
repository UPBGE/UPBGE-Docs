LatticePoint(bpy_struct)
========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: LatticePoint(bpy_struct)

   Point in the lattice grid

   .. data:: co

      Original undeformed location used to calculate the strength of the deform effect (edit/animate the Deformed Location instead)

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. attribute:: co_deform

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. data:: groups

      Weights for the vertex groups this point is member of

      :type: :class:`bpy_prop_collection` of :class:`VertexGroupElement`, (readonly)

   .. attribute:: select

      Selection status

      :type: boolean, default False

   .. attribute:: weight_softbody

      Softbody goal weight

      :type: float in [0.01, 100], default 0.0

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

   * :class:`Lattice.points`


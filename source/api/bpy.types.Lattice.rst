Lattice(ID)
===========

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Lattice(ID)

   Lattice data-block defining a grid for deforming other objects

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. attribute:: interpolation_type_u

      :type: enum in ['KEY_LINEAR', 'KEY_CARDINAL', 'KEY_CATMULL_ROM', 'KEY_BSPLINE'], default 'KEY_LINEAR'

   .. attribute:: interpolation_type_v

      :type: enum in ['KEY_LINEAR', 'KEY_CARDINAL', 'KEY_CATMULL_ROM', 'KEY_BSPLINE'], default 'KEY_LINEAR'

   .. attribute:: interpolation_type_w

      :type: enum in ['KEY_LINEAR', 'KEY_CARDINAL', 'KEY_CATMULL_ROM', 'KEY_BSPLINE'], default 'KEY_LINEAR'

   .. data:: is_editmode

      True when used in editmode

      :type: boolean, default False, (readonly)

   .. data:: points

      Points of the lattice

      :type: :class:`bpy_prop_collection` of :class:`LatticePoint`, (readonly)

   .. attribute:: points_u

      Point in U direction (can't be changed when there are shape keys)

      :type: int in [1, 64], default 0

   .. attribute:: points_v

      Point in V direction (can't be changed when there are shape keys)

      :type: int in [1, 64], default 0

   .. attribute:: points_w

      Point in W direction (can't be changed when there are shape keys)

      :type: int in [1, 64], default 0

   .. data:: shape_keys

      :type: :class:`Key`, (readonly)

   .. attribute:: use_outside

      Only draw, and take into account, the outer vertices

      :type: boolean, default False

   .. attribute:: vertex_group

      Vertex group to apply the influence of the lattice

      :type: string, default "", (never None)

   .. method:: transform(matrix, shape_keys=False)

      Transform lattice by a matrix

      :arg matrix:

         Matrix

      :type matrix: float multi-dimensional array of 4 * 4 items in [-inf, inf]
      :arg shape_keys:

         Transform Shape Keys

      :type shape_keys: boolean, (optional)

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
   * :class:`ID.name`
   * :class:`ID.users`
   * :class:`ID.use_fake_user`
   * :class:`ID.tag`
   * :class:`ID.is_updated`
   * :class:`ID.is_updated_data`
   * :class:`ID.is_library_indirect`
   * :class:`ID.library`
   * :class:`ID.preview`

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
   * :class:`ID.copy`
   * :class:`ID.user_clear`
   * :class:`ID.user_remap`
   * :class:`ID.make_local`
   * :class:`ID.user_of_id`
   * :class:`ID.animation_data_create`
   * :class:`ID.animation_data_clear`
   * :class:`ID.update_tag`

.. rubric:: References

.. hlist::
   :columns: 2

   * :mod:`bpy.context.lattice`
   * :class:`BlendData.lattices`
   * :class:`BlendDataLattices.new`
   * :class:`BlendDataLattices.remove`


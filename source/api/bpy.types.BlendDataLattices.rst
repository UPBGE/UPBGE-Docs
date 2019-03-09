BlendDataLattices(bpy_struct)
=============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BlendDataLattices(bpy_struct)

   Collection of lattices

   .. data:: is_updated

      :type: boolean, default False, (readonly)

   .. method:: new(name)

      Add a new lattice to the main database

      :arg name:

         New name for the data-block

      :type name: string, (never None)
      :return:

         New lattices data-block

      :rtype: :class:`Lattice`

   .. method:: remove(lattice, do_unlink=True, do_id_user=True, do_ui_user=True)

      Remove a lattice from the current blendfile

      :arg lattice:

         Lattice to remove

      :type lattice: :class:`Lattice`, (never None)
      :arg do_unlink:

         Unlink all usages of this lattice before deleting it (WARNING: will also delete objects instancing that lattice data)

      :type do_unlink: boolean, (optional)
      :arg do_id_user:

         Decrement user counter of all datablocks used by this lattice data

      :type do_id_user: boolean, (optional)
      :arg do_ui_user:

         Make sure interface does not reference this lattice data

      :type do_ui_user: boolean, (optional)

   .. method:: tag(value)

      tag

      :arg value:

         Value

      :type value: boolean

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

   * :class:`BlendData.lattices`


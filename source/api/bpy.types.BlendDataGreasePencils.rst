BlendDataGreasePencils(bpy_struct)
==================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BlendDataGreasePencils(bpy_struct)

   Collection of grease pencils

   .. data:: is_updated

      :type: boolean, default False, (readonly)

   .. method:: tag(value)

      tag

      :arg value:

         Value

      :type value: boolean

   .. classmethod:: new(name)

      new

      :arg name:

         New name for the data-block

      :type name: string, (never None)
      :return:

         New grease pencil data-block

      :rtype: :class:`GreasePencil`

   .. method:: remove(grease_pencil, do_unlink=True, do_id_user=True, do_ui_user=True)

      Remove a grease pencil instance from the current blendfile

      :arg grease_pencil:

         Grease Pencil to remove

      :type grease_pencil: :class:`GreasePencil`, (never None)
      :arg do_unlink:

         Unlink all usages of this grease pencil before deleting it

      :type do_unlink: boolean, (optional)
      :arg do_id_user:

         Decrement user counter of all datablocks used by this grease pencil

      :type do_id_user: boolean, (optional)
      :arg do_ui_user:

         Make sure interface does not reference this grease pencil

      :type do_ui_user: boolean, (optional)

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

   * :class:`BlendData.grease_pencil`


BlendDataMasks(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BlendDataMasks(bpy_struct)

   Collection of masks

   .. data:: is_updated

      :type: boolean, default False, (readonly)

   .. method:: tag(value)

      tag

      :arg value:

         Value

      :type value: boolean

   .. method:: new(name="")

      Add a new mask with a given name to the main database

      :arg name:

         Mask, Name of new mask data-block

      :type name: string, (optional, never None)
      :return:

         New mask data-block

      :rtype: :class:`Mask`

   .. method:: remove(mask, do_unlink=True, do_id_user=True, do_ui_user=True)

      Remove a masks from the current blendfile.

      :arg mask:

         Mask to remove

      :type mask: :class:`Mask`, (never None)
      :arg do_unlink:

         Unlink all usages of this mask before deleting it

      :type do_unlink: boolean, (optional)
      :arg do_id_user:

         Decrement user counter of all datablocks used by this mask

      :type do_id_user: boolean, (optional)
      :arg do_ui_user:

         Make sure interface does not reference this mask

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

   * :class:`BlendData.masks`


BlendDataMetaBalls(bpy_struct)
==============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BlendDataMetaBalls(bpy_struct)

   Collection of metaballs

   .. data:: is_updated

      :type: boolean, default False, (readonly)

   .. method:: new(name)

      Add a new metaball to the main database

      :arg name:

         New name for the data-block

      :type name: string, (never None)
      :return:

         New metaball data-block

      :rtype: :class:`MetaBall`

   .. method:: remove(metaball, do_unlink=True, do_id_user=True, do_ui_user=True)

      Remove a metaball from the current blendfile

      :arg metaball:

         Metaball to remove

      :type metaball: :class:`MetaBall`, (never None)
      :arg do_unlink:

         Unlink all usages of this metaball before deleting it (WARNING: will also delete objects instancing that metaball data)

      :type do_unlink: boolean, (optional)
      :arg do_id_user:

         Decrement user counter of all datablocks used by this metaball data

      :type do_id_user: boolean, (optional)
      :arg do_ui_user:

         Make sure interface does not reference this metaball data

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

   * :class:`BlendData.metaballs`


KeyConfig(bpy_struct)
=====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: KeyConfig(bpy_struct)

   Input configuration, including keymaps

   .. data:: is_user_defined

      Indicates that a keyconfig was defined by the user

      :type: boolean, default False, (readonly)

   .. data:: keymaps

      Key maps configured as part of this configuration

      :type: :class:`KeyMaps` :class:`bpy_prop_collection` of :class:`KeyMap`, (readonly)

   .. attribute:: name

      Name of the key configuration

      :type: string, default "", (never None)

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

   * :class:`KeyConfigurations.active`
   * :class:`KeyConfigurations.addon`
   * :class:`KeyConfigurations.default`
   * :class:`KeyConfigurations.new`
   * :class:`KeyConfigurations.remove`
   * :class:`KeyConfigurations.user`
   * :class:`WindowManager.keyconfigs`


KeyConfigurations(bpy_struct)
=============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: KeyConfigurations(bpy_struct)

   Collection of KeyConfigs

   .. attribute:: active

      Active key configuration (preset)

      :type: :class:`KeyConfig`

   .. data:: addon

      Key configuration that can be extended by add-ons, and is added to the active configuration when handling events

      :type: :class:`KeyConfig`, (readonly)

   .. data:: default

      Default builtin key configuration

      :type: :class:`KeyConfig`, (readonly)

   .. data:: user

      Final key configuration that combines keymaps from the active and add-on configurations, and can be edited by the user

      :type: :class:`KeyConfig`, (readonly)

   .. method:: new(name)

      new

      :arg name:

         Name

      :type name: string, (never None)
      :return:

         Key Configuration, Added key configuration

      :rtype: :class:`KeyConfig`

   .. method:: remove(keyconfig)

      remove

      :arg keyconfig:

         Key Configuration, Removed key configuration

      :type keyconfig: :class:`KeyConfig`, (never None)

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

   * :class:`WindowManager.keyconfigs`


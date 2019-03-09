ObjectBase(bpy_struct)
======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ObjectBase(bpy_struct)

   An object instance in a scene

   .. attribute:: layers

      Layers the object base is on

      :type: boolean array of 20 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

   .. data:: layers_local_view

      3D local view layers the object base is on

      :type: boolean array of 8 items, default (False, False, False, False, False, False, False, False), (readonly)

   .. data:: object

      Object this base links to

      :type: :class:`Object`, (readonly)

   .. attribute:: select

      Object base selection state

      :type: boolean, default False

   .. method:: layers_from_view(view)

      Sets the object layers from a 3D View (use when adding an object in local view)

      :type view: :class:`SpaceView3D`, (never None)

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

   * :mod:`bpy.context.active_base`
   * :mod:`bpy.context.editable_bases`
   * :mod:`bpy.context.selectable_bases`
   * :mod:`bpy.context.selected_bases`
   * :mod:`bpy.context.selected_editable_bases`
   * :mod:`bpy.context.visible_bases`
   * :class:`Scene.object_bases`
   * :class:`SceneBases.active`
   * :class:`SceneObjects.link`


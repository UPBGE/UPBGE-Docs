RenderViews(bpy_struct)
=======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: RenderViews(bpy_struct)

   Collection of render views

   .. attribute:: active

      Active Render View

      :type: :class:`SceneRenderView`, (never None)

   .. attribute:: active_index

      Active index in render view array

      :type: int in [0, 32767], default 0

   .. method:: new(name)

      Add a render view to scene

      :arg name:

         New name for the marker (not unique)

      :type name: string, (never None)
      :return:

         Newly created render view

      :rtype: :class:`SceneRenderView`

   .. method:: remove(view)

      Remove a render view

      :arg view:

         Render view to remove

      :type view: :class:`SceneRenderView`, (never None)

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

   * :class:`RenderSettings.views`


RenderPasses(bpy_struct)
========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: RenderPasses(bpy_struct)

   Collection of render passes

   .. method:: find_by_type(pass_type, view)

      Get the render pass for a given type and view

      :arg pass_type:

         Pass

      :type pass_type: enum in ['COMBINED', 'Z', 'COLOR', 'DIFFUSE', 'SPECULAR', 'SHADOW', 'AO', 'REFLECTION', 'NORMAL', 'VECTOR', 'REFRACTION', 'OBJECT_INDEX', 'UV', 'MIST', 'EMIT', 'ENVIRONMENT', 'MATERIAL_INDEX', 'DIFFUSE_DIRECT', 'DIFFUSE_INDIRECT', 'DIFFUSE_COLOR', 'GLOSSY_DIRECT', 'GLOSSY_INDIRECT', 'GLOSSY_COLOR', 'TRANSMISSION_DIRECT', 'TRANSMISSION_INDIRECT', 'TRANSMISSION_COLOR', 'SUBSURFACE_DIRECT', 'SUBSURFACE_INDIRECT', 'SUBSURFACE_COLOR']
      :arg view:

         View, Render view to get pass from

      :type view: string, (never None)
      :return:

         The matching render pass

      :rtype: :class:`RenderPass`

   .. method:: find_by_name(name, view)

      Get the render pass for a given name and view

      :arg name:

         Pass

      :type name: string, (never None)
      :arg view:

         View, Render view to get pass from

      :type view: string, (never None)
      :return:

         The matching render pass

      :rtype: :class:`RenderPass`

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

   * :class:`RenderLayer.passes`


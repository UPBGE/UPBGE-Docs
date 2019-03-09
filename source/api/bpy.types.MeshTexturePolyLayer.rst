MeshTexturePolyLayer(bpy_struct)
================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MeshTexturePolyLayer(bpy_struct)

   UV map with assigned image textures in a Mesh data-block

   .. attribute:: active

      Set the map as active for display and editing

      :type: boolean, default False

   .. attribute:: active_clone

      Set the map as active for cloning

      :type: boolean, default False

   .. attribute:: active_render

      Set the map as active for rendering

      :type: boolean, default False

   .. data:: data

      :type: :class:`bpy_prop_collection` of :class:`MeshTexturePoly`, (readonly)

   .. attribute:: name

      Name of UV map

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

   * :class:`Mesh.uv_texture_clone`
   * :class:`Mesh.uv_texture_stencil`
   * :class:`Mesh.uv_textures`
   * :class:`UVTextures.active`
   * :class:`UVTextures.new`
   * :class:`UVTextures.remove`


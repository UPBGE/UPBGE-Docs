BlendDataMeshes(bpy_struct)
===========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BlendDataMeshes(bpy_struct)

   Collection of meshes

   .. data:: is_updated

      :type: boolean, default False, (readonly)

   .. method:: new(name)

      Add a new mesh to the main database

      :arg name:

         New name for the data-block

      :type name: string, (never None)
      :return:

         New mesh data-block

      :rtype: :class:`Mesh`

   .. method:: new_from_object(scene, object, apply_modifiers, settings, calc_tessface=True, calc_undeformed=False)

      Add a new mesh created from object with modifiers applied

      :arg scene:

         Scene within which to evaluate modifiers

      :type scene: :class:`Scene`, (never None)
      :arg object:

         Object to create mesh from

      :type object: :class:`Object`, (never None)
      :arg apply_modifiers:

         Apply modifiers

      :type apply_modifiers: boolean
      :arg settings:

         Modifier settings to apply

         * ``PREVIEW`` Preview, Apply modifier preview settings.
         * ``RENDER`` Render, Apply modifier render settings.

      :type settings: enum in ['PREVIEW', 'RENDER']
      :arg calc_tessface:

         Calculate Tessellation, Calculate tessellation faces

      :type calc_tessface: boolean, (optional)
      :arg calc_undeformed:

         Calculate Undeformed, Calculate undeformed vertex coordinates

      :type calc_undeformed: boolean, (optional)
      :return:

         Mesh created from object, remove it if it is only used for export

      :rtype: :class:`Mesh`

   .. method:: remove(mesh, do_unlink=True, do_id_user=True, do_ui_user=True)

      Remove a mesh from the current blendfile

      :arg mesh:

         Mesh to remove

      :type mesh: :class:`Mesh`, (never None)
      :arg do_unlink:

         Unlink all usages of this mesh before deleting it (WARNING: will also delete objects instancing that mesh data)

      :type do_unlink: boolean, (optional)
      :arg do_id_user:

         Decrement user counter of all datablocks used by this mesh data

      :type do_id_user: boolean, (optional)
      :arg do_ui_user:

         Make sure interface does not reference this mesh data

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

   * :class:`BlendData.meshes`


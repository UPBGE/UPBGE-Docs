Struct(bpy_struct)
==================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Struct(bpy_struct)

   RNA structure definition

   .. data:: base

      Struct definition this is derived from

      :type: :class:`Struct`, (readonly)

   .. data:: description

      Description of the Struct's purpose

      :type: string, default "", (readonly, never None)

   .. data:: functions

      :type: :class:`bpy_prop_collection` of :class:`Function`, (readonly)

   .. data:: identifier

      Unique name used in the code and scripting

      :type: string, default "", (readonly, never None)

   .. data:: name

      Human readable name

      :type: string, default "", (readonly, never None)

   .. data:: name_property

      Property that gives the name of the struct

      :type: :class:`StringProperty`, (readonly)

   .. data:: nested

      Struct in which this struct is always nested, and to which it logically belongs

      :type: :class:`Struct`, (readonly)

   .. data:: properties

      Properties in the struct

      :type: :class:`bpy_prop_collection` of :class:`Property`, (readonly)

   .. data:: property_tags

      Tags that properties can use to influence behavior

      :type: :class:`bpy_prop_collection` of :class:`EnumPropertyItem`, (readonly)

   .. data:: translation_context

      Translation context of the struct's name

      :type: string, default "", (readonly, never None)

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

   * :class:`BlenderRNA.structs`
   * :class:`CollectionProperty.fixed_type`
   * :class:`NodeSocketInterface.register_properties`
   * :class:`PointerProperty.fixed_type`
   * :class:`Property.srna`
   * :class:`Struct.base`
   * :class:`Struct.nested`


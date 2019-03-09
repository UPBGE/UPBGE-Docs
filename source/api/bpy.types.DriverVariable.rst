DriverVariable(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: DriverVariable(bpy_struct)

   Variable from some source/target for driver relationship

   .. data:: is_name_valid

      Is this a valid name for a driver variable

      :type: boolean, default False, (readonly)

   .. attribute:: name

      Name to use in scripted expressions/functions (no spaces or dots are allowed, and must start with a letter)

      :type: string, default "", (never None)

   .. data:: targets

      Sources of input data for evaluating this variable

      :type: :class:`bpy_prop_collection` of :class:`DriverTarget`, (readonly)

   .. attribute:: type

      Driver variable type

      * ``SINGLE_PROP`` Single Property, Use the value from some RNA property (Default).
      * ``TRANSFORMS`` Transform Channel, Final transformation value of object or bone.
      * ``ROTATION_DIFF`` Rotational Difference, Use the angle between two bones.
      * ``LOC_DIFF`` Distance, Distance between two bones or objects.

      :type: enum in ['SINGLE_PROP', 'TRANSFORMS', 'ROTATION_DIFF', 'LOC_DIFF'], default 'SINGLE_PROP'

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

   * :class:`ChannelDriverVariables.new`
   * :class:`ChannelDriverVariables.remove`
   * :class:`Driver.variables`


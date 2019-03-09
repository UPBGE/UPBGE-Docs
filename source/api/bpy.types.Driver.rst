Driver(bpy_struct)
==================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Driver(bpy_struct)

   Driver for the value of a setting based on an external value

   .. attribute:: expression

      Expression to use for Scripted Expression

      :type: string, default "", (never None)

   .. attribute:: is_valid

      Driver could not be evaluated in past, so should be skipped

      :type: boolean, default False

   .. attribute:: show_debug_info

      Show intermediate values for the driver calculations to allow debugging of drivers

      :type: boolean, default False

   .. attribute:: type

      Driver type

      :type: enum in ['AVERAGE', 'SUM', 'SCRIPTED', 'MIN', 'MAX'], default 'AVERAGE'

   .. attribute:: use_self

      Include a 'self' variable in the name-space, so drivers can easily reference the data being modified (object, bone, etc...)

      :type: boolean, default False

   .. data:: variables

      Properties acting as inputs for this driver

      :type: :class:`ChannelDriverVariables` :class:`bpy_prop_collection` of :class:`DriverVariable`, (readonly)

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

   * :class:`FCurve.driver`


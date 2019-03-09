AnimDataDrivers(bpy_struct)
===========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: AnimDataDrivers(bpy_struct)

   Collection of Driver F-Curves

   .. method:: from_existing(src_driver=None)

      Add a new driver given an existing one

      :arg src_driver:

         Existing Driver F-Curve to use as template for a new one

      :type src_driver: :class:`FCurve`, (optional)
      :return:

         New Driver F-Curve

      :rtype: :class:`FCurve`

   .. method:: find(data_path, index=0)

      Find a driver F-Curve. Note that this function performs a linear scan of all driver F-Curves.

      :arg data_path:

         Data Path, F-Curve data path

      :type data_path: string, (never None)
      :arg index:

         Index, Array index

      :type index: int in [0, inf], (optional)
      :return:

         The found F-Curve, or None if it doesn't exist

      :rtype: :class:`FCurve`

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

   * :class:`AnimData.drivers`


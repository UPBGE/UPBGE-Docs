ActionFCurves(bpy_struct)
=========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ActionFCurves(bpy_struct)

   Collection of action F-Curves

   .. method:: new(data_path, index=0, action_group="")

      Add an F-Curve to the action

      :arg data_path:

         Data Path, F-Curve data path to use

      :type data_path: string, (never None)
      :arg index:

         Index, Array index

      :type index: int in [0, inf], (optional)
      :arg action_group:

         Action Group, Acton group to add this F-Curve into

      :type action_group: string, (optional, never None)
      :return:

         Newly created F-Curve

      :rtype: :class:`FCurve`

   .. method:: find(data_path, index=0)

      Find an F-Curve. Note that this function performs a linear scan of all F-Curves in the action.

      :arg data_path:

         Data Path, F-Curve data path

      :type data_path: string, (never None)
      :arg index:

         Index, Array index

      :type index: int in [0, inf], (optional)
      :return:

         The found F-Curve, or None if it doesn't exist

      :rtype: :class:`FCurve`

   .. method:: remove(fcurve)

      Remove action group

      :arg fcurve:

         F-Curve to remove

      :type fcurve: :class:`FCurve`, (never None)

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

   * :class:`Action.fcurves`


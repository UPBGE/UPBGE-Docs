DisplaySafeAreas(bpy_struct)
============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: DisplaySafeAreas(bpy_struct)

   Safe Areas used in 3D view and the VSE

   .. attribute:: action

      Safe area for general elements

      :type: float array of 2 items in [0, 1], default (0.1, 0.05)

   .. attribute:: action_center

      Safe area for general elements in a different aspect ratio

      :type: float array of 2 items in [0, 1], default (0.15, 0.05)

   .. attribute:: title

      Safe area for text and graphics

      :type: float array of 2 items in [0, 1], default (0.035, 0.035)

   .. attribute:: title_center

      Safe area for text and graphics in a different aspect ratio

      :type: float array of 2 items in [0, 1], default (0.175, 0.05)

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

   * :class:`Scene.safe_areas`


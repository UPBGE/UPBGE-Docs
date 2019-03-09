GPencilStrokePoints(bpy_struct)
===============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GPencilStrokePoints(bpy_struct)

   Collection of grease pencil stroke points

   .. method:: add(count=1, pressure=1.0, strength=1.0)

      Add a new grease pencil stroke point

      :arg count:

         Number, Number of points to add to the stroke

      :type count: int in [0, inf], (optional)
      :arg pressure:

         Pressure, Pressure for newly created points

      :type pressure: float in [0, 1], (optional)
      :arg strength:

         Strength, Color intensity (alpha factor) for newly created points

      :type strength: float in [0, 1], (optional)

   .. method:: pop(index=-1)

      Remove a grease pencil stroke point

      :arg index:

         Index, point index

      :type index: int in [-inf, inf], (optional)

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

   * :class:`GPencilStroke.points`


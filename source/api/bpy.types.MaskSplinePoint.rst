MaskSplinePoint(bpy_struct)
===========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MaskSplinePoint(bpy_struct)

   Single point in spline used for defining mask

   .. attribute:: co

      Coordinates of the control point

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. data:: feather_points

      Points defining feather

      :type: :class:`bpy_prop_collection` of :class:`MaskSplinePointUW`, (readonly)

   .. attribute:: handle_left

      Coordinates of the first handle

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: handle_left_type

      Handle type

      :type: enum in ['AUTO', 'VECTOR', 'ALIGNED', 'ALIGNED_DOUBLESIDE', 'FREE'], default 'FREE'

   .. attribute:: handle_right

      Coordinates of the second handle

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: handle_right_type

      Handle type

      :type: enum in ['AUTO', 'VECTOR', 'ALIGNED', 'ALIGNED_DOUBLESIDE', 'FREE'], default 'FREE'

   .. attribute:: handle_type

      Handle type

      :type: enum in ['AUTO', 'VECTOR', 'ALIGNED', 'ALIGNED_DOUBLESIDE', 'FREE'], default 'FREE'

   .. data:: parent

      :type: :class:`MaskParent`, (readonly)

   .. attribute:: select

      Selection status

      :type: boolean, default False

   .. attribute:: weight

      Weight of the point

      :type: float in [0, 1], default 0.0

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

   * :class:`MaskSpline.points`
   * :class:`MaskSplinePoints.remove`
   * :class:`MaskSplines.active_point`


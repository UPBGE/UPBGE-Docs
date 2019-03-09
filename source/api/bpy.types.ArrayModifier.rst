ArrayModifier(Modifier)
=======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: ArrayModifier(Modifier)

   Array duplication modifier

   .. attribute:: constant_offset_displace

      Value for the distance between arrayed items

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: count

      Number of duplicates to make

      :type: int in [1, inf], default 0

   .. attribute:: curve

      Curve object to fit array length to

      :type: :class:`Object`

   .. attribute:: end_cap

      Mesh object to use as an end cap

      :type: :class:`Object`

   .. attribute:: fit_length

      Length to fit array within

      :type: float in [0, inf], default 0.0

   .. attribute:: fit_type

      Array length calculation method

      * ``FIXED_COUNT`` Fixed Count, Duplicate the object a certain number of times.
      * ``FIT_LENGTH`` Fit Length, Duplicate the object as many times as fits in a certain length.
      * ``FIT_CURVE`` Fit Curve, Fit the duplicated objects to a curve.

      :type: enum in ['FIXED_COUNT', 'FIT_LENGTH', 'FIT_CURVE'], default 'FIXED_COUNT'

   .. attribute:: merge_threshold

      Limit below which to merge vertices

      :type: float in [0, inf], default 0.0

   .. attribute:: offset_object

      Use the location and rotation of another object to determine the distance and rotational change between arrayed items

      :type: :class:`Object`

   .. attribute:: offset_u

      Amount to offset array UVs on the U axis

      :type: float in [-1, 1], default 0.0

   .. attribute:: offset_v

      Amount to offset array UVs on the V axis

      :type: float in [-1, 1], default 0.0

   .. attribute:: relative_offset_displace

      The size of the geometry will determine the distance between arrayed items

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: start_cap

      Mesh object to use as a start cap

      :type: :class:`Object`

   .. attribute:: use_constant_offset

      Add a constant offset

      :type: boolean, default False

   .. attribute:: use_merge_vertices

      Merge vertices in adjacent duplicates

      :type: boolean, default False

   .. attribute:: use_merge_vertices_cap

      Merge vertices in first and last duplicates

      :type: boolean, default False

   .. attribute:: use_object_offset

      Add another object's transformation to the total offset

      :type: boolean, default False

   .. attribute:: use_relative_offset

      Add an offset relative to the object's bounding box

      :type: boolean, default False

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
   * :class:`Modifier.name`
   * :class:`Modifier.type`
   * :class:`Modifier.show_viewport`
   * :class:`Modifier.show_render`
   * :class:`Modifier.show_in_editmode`
   * :class:`Modifier.show_on_cage`
   * :class:`Modifier.show_expanded`
   * :class:`Modifier.use_apply_on_spline`

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


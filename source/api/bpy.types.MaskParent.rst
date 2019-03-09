MaskParent(bpy_struct)
======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MaskParent(bpy_struct)

   Parenting settings for masking element

   .. attribute:: id

      ID-block to which masking element would be parented to or to it's property

      :type: :class:`ID`

   .. attribute:: id_type

      Type of ID-block that can be used

      :type: enum in ['MOVIECLIP'], default 'MOVIECLIP'

   .. attribute:: parent

      Name of parent object in specified data-block to which parenting happens

      :type: string, default "", (never None)

   .. attribute:: sub_parent

      Name of parent sub-object in specified data-block to which parenting happens

      :type: string, default "", (never None)

   .. attribute:: type

      Parent Type

      :type: enum in ['POINT_TRACK', 'PLANE_TRACK'], default 'POINT_TRACK'

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

   * :class:`MaskSplinePoint.parent`


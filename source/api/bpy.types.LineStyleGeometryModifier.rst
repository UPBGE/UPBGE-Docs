LineStyleGeometryModifier(LineStyleModifier)
============================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`LineStyleModifier`

subclasses --- 
:class:`LineStyleGeometryModifier_2DOffset`, :class:`LineStyleGeometryModifier_2DTransform`, :class:`LineStyleGeometryModifier_BackboneStretcher`, :class:`LineStyleGeometryModifier_BezierCurve`, :class:`LineStyleGeometryModifier_Blueprint`, :class:`LineStyleGeometryModifier_GuidingLines`, :class:`LineStyleGeometryModifier_PerlinNoise1D`, :class:`LineStyleGeometryModifier_PerlinNoise2D`, :class:`LineStyleGeometryModifier_Polygonalization`, :class:`LineStyleGeometryModifier_Sampling`, :class:`LineStyleGeometryModifier_Simplification`, :class:`LineStyleGeometryModifier_SinusDisplacement`, :class:`LineStyleGeometryModifier_SpatialNoise`, :class:`LineStyleGeometryModifier_TipRemover`

.. class:: LineStyleGeometryModifier(LineStyleModifier)

   Base type to define stroke geometry modifiers

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

   * :class:`FreestyleLineStyle.geometry_modifiers`
   * :class:`LineStyleGeometryModifiers.new`
   * :class:`LineStyleGeometryModifiers.remove`


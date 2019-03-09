LineStyleColorModifier(LineStyleModifier)
=========================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`LineStyleModifier`

subclasses --- 
:class:`LineStyleColorModifier_AlongStroke`, :class:`LineStyleColorModifier_CreaseAngle`, :class:`LineStyleColorModifier_Curvature_3D`, :class:`LineStyleColorModifier_DistanceFromCamera`, :class:`LineStyleColorModifier_DistanceFromObject`, :class:`LineStyleColorModifier_Material`, :class:`LineStyleColorModifier_Noise`, :class:`LineStyleColorModifier_Tangent`

.. class:: LineStyleColorModifier(LineStyleModifier)

   Base type to define line color modifiers

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

   * :class:`FreestyleLineStyle.color_modifiers`
   * :class:`LineStyleColorModifiers.new`
   * :class:`LineStyleColorModifiers.remove`


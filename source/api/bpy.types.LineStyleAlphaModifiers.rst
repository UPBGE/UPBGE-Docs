LineStyleAlphaModifiers(bpy_struct)
===================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: LineStyleAlphaModifiers(bpy_struct)

   Alpha modifiers for changing line alphas

   .. method:: new(name, type)

      Add a alpha modifier to line style

      :arg name:

         New name for the alpha modifier (not unique)

      :type name: string, (never None)
      :arg type:

         Alpha modifier type to add

      :type type: enum in ['ALONG_STROKE', 'CREASE_ANGLE', 'CURVATURE_3D', 'DISTANCE_FROM_CAMERA', 'DISTANCE_FROM_OBJECT', 'MATERIAL', 'NOISE', 'TANGENT']
      :return:

         Newly added alpha modifier

      :rtype: :class:`LineStyleAlphaModifier`

   .. method:: remove(modifier)

      Remove a alpha modifier from line style

      :arg modifier:

         Alpha modifier to remove

      :type modifier: :class:`LineStyleAlphaModifier`, (never None)

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

   * :class:`FreestyleLineStyle.alpha_modifiers`


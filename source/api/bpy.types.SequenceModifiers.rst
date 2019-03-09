SequenceModifiers(bpy_struct)
=============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SequenceModifiers(bpy_struct)

   Collection of strip modifiers

   .. method:: new(name, type)

      Add a new modifier

      :arg name:

         New name for the modifier

      :type name: string, (never None)
      :arg type:

         Modifier type to add

      :type type: enum in ['COLOR_BALANCE', 'CURVES', 'HUE_CORRECT', 'BRIGHT_CONTRAST', 'MASK', 'WHITE_BALANCE', 'TONEMAP']
      :return:

         Newly created modifier

      :rtype: :class:`SequenceModifier`

   .. method:: remove(modifier)

      Remove an existing modifier from the sequence

      :arg modifier:

         Modifier to remove

      :type modifier: :class:`SequenceModifier`, (never None)

   .. method:: clear()

      Remove all modifiers from the sequence


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

   * :class:`Sequence.modifiers`


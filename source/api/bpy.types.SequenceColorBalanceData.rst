SequenceColorBalanceData(bpy_struct)
====================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`SequenceColorBalance`

.. class:: SequenceColorBalanceData(bpy_struct)

   Color balance parameters for a sequence strip and it's modifiers

   .. attribute:: gain

      Color balance gain (highlights)

      :type: float array of 3 items in [0, inf], default (1.0, 1.0, 1.0)

   .. attribute:: gamma

      Color balance gamma (midtones)

      :type: float array of 3 items in [0, inf], default (1.0, 1.0, 1.0)

   .. attribute:: invert_gain

      Invert the gain color`

      :type: boolean, default False

   .. attribute:: invert_gamma

      Invert the gamma color

      :type: boolean, default False

   .. attribute:: invert_lift

      Invert the lift color

      :type: boolean, default False

   .. attribute:: lift

      Color balance lift (shadows)

      :type: float array of 3 items in [0, inf], default (1.0, 1.0, 1.0)

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

   * :class:`ColorBalanceModifier.color_balance`


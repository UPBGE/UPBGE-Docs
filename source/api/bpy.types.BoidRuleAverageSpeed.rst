BoidRuleAverageSpeed(BoidRule)
==============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`BoidRule`

.. class:: BoidRuleAverageSpeed(BoidRule)

   

   .. attribute:: level

      How much velocity's z-component is kept constant

      :type: float in [0, 1], default 0.0

   .. attribute:: speed

      Percentage of maximum speed

      :type: float in [0, 1], default 0.0

   .. attribute:: wander

      How fast velocity's direction is randomized

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
   * :class:`BoidRule.name`
   * :class:`BoidRule.type`
   * :class:`BoidRule.use_in_air`
   * :class:`BoidRule.use_on_land`

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


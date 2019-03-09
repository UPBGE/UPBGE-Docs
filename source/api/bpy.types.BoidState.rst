BoidState(bpy_struct)
=====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BoidState(bpy_struct)

   Boid state for boid physics

   .. data:: active_boid_rule

      :type: :class:`BoidRule`, (readonly)

   .. attribute:: active_boid_rule_index

      :type: int in [0, inf], default 0

   .. attribute:: falloff

      :type: float in [0, 10], default 0.0

   .. attribute:: name

      Boid state name

      :type: string, default "", (never None)

   .. attribute:: rule_fuzzy

      :type: float in [0, 1], default 0.0

   .. data:: rules

      :type: :class:`bpy_prop_collection` of :class:`BoidRule`, (readonly)

   .. attribute:: ruleset_type

      How the rules in the list are evaluated

      * ``FUZZY`` Fuzzy, Rules are gone through top to bottom (only the first rule which effect is above fuzziness threshold is evaluated).
      * ``RANDOM`` Random, A random rule is selected for each boid.
      * ``AVERAGE`` Average, All rules are averaged.

      :type: enum in ['FUZZY', 'RANDOM', 'AVERAGE'], default 'FUZZY'

   .. attribute:: volume

      :type: float in [0, 100], default 0.0

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

   * :class:`BoidSettings.states`


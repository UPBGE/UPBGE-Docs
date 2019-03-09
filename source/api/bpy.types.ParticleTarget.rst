ParticleTarget(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ParticleTarget(bpy_struct)

   Target particle system

   .. attribute:: alliance

      :type: enum in ['FRIEND', 'NEUTRAL', 'ENEMY'], default 'NEUTRAL'

   .. attribute:: duration

      :type: float in [0, 30000], default 0.0

   .. attribute:: is_valid

      Keyed particles target is valid

      :type: boolean, default False

   .. data:: name

      Particle target name

      :type: string, default "", (readonly, never None)

   .. attribute:: object

      The object that has the target particle system (empty if same object)

      :type: :class:`Object`

   .. attribute:: system

      The index of particle system on the target object

      :type: int in [1, inf], default 0

   .. attribute:: time

      :type: float in [0, 30000], default 0.0

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

   * :class:`ParticleSystem.active_particle_target`
   * :class:`ParticleSystem.targets`


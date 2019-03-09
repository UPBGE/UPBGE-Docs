Particle(bpy_struct)
====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Particle(bpy_struct)

   Particle in a particle system

   .. attribute:: alive_state

      :type: enum in ['DEAD', 'UNBORN', 'ALIVE', 'DYING'], default 'DEAD'

   .. attribute:: angular_velocity

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: birth_time

      :type: float in [-inf, inf], default 0.0

   .. attribute:: die_time

      :type: float in [-inf, inf], default 0.0

   .. data:: hair_keys

      :type: :class:`bpy_prop_collection` of :class:`ParticleHairKey`, (readonly)

   .. data:: is_exist

      :type: boolean, default False, (readonly)

   .. data:: is_visible

      :type: boolean, default False, (readonly)

   .. attribute:: lifetime

      :type: float in [-inf, inf], default 0.0

   .. attribute:: location

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. data:: particle_keys

      :type: :class:`bpy_prop_collection` of :class:`ParticleKey`, (readonly)

   .. attribute:: prev_angular_velocity

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: prev_location

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: prev_rotation

      :type: float array of 4 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: prev_velocity

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: rotation

      :type: float array of 4 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: size

      :type: float in [-inf, inf], default 0.0

   .. attribute:: velocity

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. method:: uv_on_emitter(modifier)

      Obtain uv for particle on derived mesh

      :arg modifier:

         Particle modifier

      :type modifier: :class:`ParticleSystemModifier`, (never None)
      :return:

         uv

      :rtype: float array of 2 items in [-inf, inf]

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

   * :class:`ParticleHairKey.co_object`
   * :class:`ParticleSystem.mcol_on_emitter`
   * :class:`ParticleSystem.particles`
   * :class:`ParticleSystem.uv_on_emitter`


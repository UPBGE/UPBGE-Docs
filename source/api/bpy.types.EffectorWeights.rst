EffectorWeights(bpy_struct)
===========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: EffectorWeights(bpy_struct)

   Effector weights for physics simulation

   .. attribute:: all

      All effector's weight

      :type: float in [-200, 200], default 0.0

   .. attribute:: apply_to_hair_growing

      Use force fields when growing hair

      :type: boolean, default False

   .. attribute:: boid

      Boid effector weight

      :type: float in [-200, 200], default 0.0

   .. attribute:: charge

      Charge effector weight

      :type: float in [-200, 200], default 0.0

   .. attribute:: curve_guide

      Curve guide effector weight

      :type: float in [-200, 200], default 0.0

   .. attribute:: drag

      Drag effector weight

      :type: float in [-200, 200], default 0.0

   .. attribute:: force

      Force effector weight

      :type: float in [-200, 200], default 0.0

   .. attribute:: gravity

      Global gravity weight

      :type: float in [-200, 200], default 0.0

   .. attribute:: group

      Limit effectors to this Group

      :type: :class:`Group`

   .. attribute:: harmonic

      Harmonic effector weight

      :type: float in [-200, 200], default 0.0

   .. attribute:: lennardjones

      Lennard-Jones effector weight

      :type: float in [-200, 200], default 0.0

   .. attribute:: magnetic

      Magnetic effector weight

      :type: float in [-200, 200], default 0.0

   .. attribute:: smokeflow

      Smoke Flow effector weight

      :type: float in [-200, 200], default 0.0

   .. attribute:: texture

      Texture effector weight

      :type: float in [-200, 200], default 0.0

   .. attribute:: turbulence

      Turbulence effector weight

      :type: float in [-200, 200], default 0.0

   .. attribute:: vortex

      Vortex effector weight

      :type: float in [-200, 200], default 0.0

   .. attribute:: wind

      Wind effector weight

      :type: float in [-200, 200], default 0.0

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

   * :class:`ClothSettings.effector_weights`
   * :class:`DynamicPaintSurface.effector_weights`
   * :class:`ParticleSettings.effector_weights`
   * :class:`RigidBodyWorld.effector_weights`
   * :class:`SmokeDomainSettings.effector_weights`
   * :class:`SoftBodySettings.effector_weights`


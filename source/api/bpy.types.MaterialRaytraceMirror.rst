MaterialRaytraceMirror(bpy_struct)
==================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MaterialRaytraceMirror(bpy_struct)

   Raytraced reflection settings for a Material data-block

   .. attribute:: depth

      Maximum allowed number of light inter-reflections

      :type: int in [0, 32767], default 0

   .. attribute:: distance

      Maximum distance of reflected rays (reflections further than this range fade to sky color or material color)

      :type: float in [0, 10000], default 0.0

   .. attribute:: fade_to

      The color that rays with no intersection within the Max Distance take (material color can be best for indoor scenes, sky color for outdoor)

      :type: enum in ['FADE_TO_SKY', 'FADE_TO_MATERIAL'], default 'FADE_TO_SKY'

   .. attribute:: fresnel

      Power of Fresnel for mirror reflection

      :type: float in [0, 5], default 0.0

   .. attribute:: fresnel_factor

      Blending factor for Fresnel

      :type: float in [0, 5], default 0.0

   .. attribute:: gloss_anisotropic

      The shape of the reflection, from 0.0 (circular) to 1.0 (fully stretched along the tangent

      :type: float in [0, 1], default 0.0

   .. attribute:: gloss_factor

      The shininess of the reflection (values < 1.0 give diffuse, blurry reflections)

      :type: float in [0, 1], default 0.0

   .. attribute:: gloss_samples

      Number of cone samples averaged for blurry reflections

      :type: int in [0, 1024], default 0

   .. attribute:: gloss_threshold

      Threshold for adaptive sampling (if a sample contributes less than this amount [as a percentage], sampling is stopped)

      :type: float in [0, 1], default 0.0

   .. attribute:: reflect_factor

      Amount of mirror reflection for raytrace

      :type: float in [0, 1], default 0.0

   .. attribute:: use

      Enable raytraced reflections

      :type: boolean, default False

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

   * :class:`Material.raytrace_mirror`


MaterialRaytraceTransparency(bpy_struct)
========================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MaterialRaytraceTransparency(bpy_struct)

   Raytraced refraction settings for a Material data-block

   .. attribute:: depth

      Maximum allowed number of light inter-refractions

      :type: int in [0, 32767], default 0

   .. attribute:: depth_max

      Maximum depth for light to travel through the transparent material before becoming fully filtered (0.0 is disabled)

      :type: float in [0, 100], default 0.0

   .. attribute:: falloff

      Falloff power for transmissivity filter effect (1.0 is linear)

      :type: float in [0.1, 10], default 0.0

   .. attribute:: filter

      Amount to blend in the material's diffuse color in raytraced transparency (simulating absorption)

      :type: float in [0, 1], default 0.0

   .. attribute:: fresnel

      Power of Fresnel for transparency (Ray or ZTransp)

      :type: float in [0, 5], default 0.0

   .. attribute:: fresnel_factor

      Blending factor for Fresnel

      :type: float in [1, 5], default 0.0

   .. attribute:: gloss_factor

      The clarity of the refraction. Values < 1.0 give diffuse, blurry refractions

      :type: float in [0, 1], default 0.0

   .. attribute:: gloss_samples

      Number of cone samples averaged for blurry refractions

      :type: int in [0, 1024], default 0

   .. attribute:: gloss_threshold

      Threshold for adaptive sampling. If a sample contributes less than this amount (as a percentage), sampling is stopped

      :type: float in [0, 1], default 0.0

   .. attribute:: ior

      Angular index of refraction for raytraced refraction

      :type: float in [0.25, 4], default 0.0

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

   * :class:`Material.raytrace_transparency`


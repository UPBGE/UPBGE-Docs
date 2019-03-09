CyclesRenderLayerSettings(bpy_struct)
=====================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: CyclesRenderLayerSettings(bpy_struct)

   

   .. attribute:: denoising_diffuse_direct

      Denoise the direct diffuse lighting

      :type: boolean, default True

   .. attribute:: denoising_diffuse_indirect

      Denoise the indirect diffuse lighting

      :type: boolean, default True

   .. attribute:: denoising_feature_strength

      Controls removal of noisy image feature passes (lower values preserve more detail, but aren't as smooth)

      :type: float in [0, 1], default 0.5

   .. attribute:: denoising_glossy_direct

      Denoise the direct glossy lighting

      :type: boolean, default True

   .. attribute:: denoising_glossy_indirect

      Denoise the indirect glossy lighting

      :type: boolean, default True

   .. attribute:: denoising_radius

      Size of the image area that's used to denoise a pixel (higher values are smoother, but might lose detail and are slower)

      :type: int in [1, 25], default 8

   .. attribute:: denoising_relative_pca

      When removing pixels that don't carry information, use a relative threshold instead of an absolute one (can help to reduce artifacts, but might cause detail loss around edges)

      :type: boolean, default False

   .. attribute:: denoising_store_passes

      Store the denoising feature passes and the noisy image

      :type: boolean, default False

   .. attribute:: denoising_strength

      Controls neighbor pixel weighting for the denoising filter (lower values preserve more detail, but aren't as smooth)

      :type: float in [0, 1], default 0.5

   .. attribute:: denoising_subsurface_direct

      Denoise the direct subsurface lighting

      :type: boolean, default True

   .. attribute:: denoising_subsurface_indirect

      Denoise the indirect subsurface lighting

      :type: boolean, default True

   .. attribute:: denoising_transmission_direct

      Denoise the direct transmission lighting

      :type: boolean, default True

   .. attribute:: denoising_transmission_indirect

      Denoise the indirect transmission lighting

      :type: boolean, default True

   .. attribute:: pass_debug_bvh_intersections

      Store Debug BVH Intersections

      :type: boolean, default False

   .. attribute:: pass_debug_bvh_traversed_instances

      Store Debug BVH Traversed Instances pass

      :type: boolean, default False

   .. attribute:: pass_debug_bvh_traversed_nodes

      Store Debug BVH Traversed Nodes pass

      :type: boolean, default False

   .. attribute:: pass_debug_ray_bounces

      Store Debug Ray Bounces pass

      :type: boolean, default False

   .. attribute:: pass_debug_render_time

      Render time in milliseconds per sample and pixel

      :type: boolean, default False

   .. attribute:: use_denoising

      Denoise the rendered image

      :type: boolean, default False

   .. attribute:: use_pass_volume_direct

      Deliver direct volumetric scattering pass

      :type: boolean, default False

   .. attribute:: use_pass_volume_indirect

      Deliver indirect volumetric scattering pass

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


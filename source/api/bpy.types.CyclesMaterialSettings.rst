CyclesMaterialSettings(bpy_struct)
==================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: CyclesMaterialSettings(bpy_struct)

   

   .. attribute:: displacement_method

      Method to use for the displacement

      * ``BUMP`` Bump, Bump mapping to simulate the appearance of displacement.
      * ``TRUE`` True, Use true displacement only, requires fine subdivision.
      * ``BOTH`` Both, Combination of displacement and bump mapping.

      :type: enum in ['BUMP', 'TRUE', 'BOTH'], default 'BUMP'

   .. attribute:: homogeneous_volume

      When using volume rendering, assume volume has the same density everywhere (not using any textures), for faster rendering

      :type: boolean, default False

   .. attribute:: sample_as_light

      Use multiple importance sampling for this material, disabling may reduce overall noise for large objects that emit little light compared to other light sources

      :type: boolean, default True

   .. attribute:: use_transparent_shadow

      Use transparent shadows for this material if it contains a Transparent BSDF, disabling will render faster but not give accurate shadows

      :type: boolean, default True

   .. attribute:: volume_interpolation

      Interpolation method to use for smoke/fire volumes

      * ``LINEAR`` Linear, Good smoothness and speed.
      * ``CUBIC`` Cubic, Smoothed high quality interpolation, but slower.

      :type: enum in ['LINEAR', 'CUBIC'], default 'LINEAR'

   .. attribute:: volume_sampling

      Sampling method to use for volumes

      * ``DISTANCE`` Distance, Use distance sampling, best for dense volumes with lights far away.
      * ``EQUIANGULAR`` Equiangular, Use equiangular sampling, best for volumes with low density with light inside or near the volume.
      * ``MULTIPLE_IMPORTANCE`` Multiple Importance, Combine distance and equi-angular sampling for volumes where neither method is ideal.

      :type: enum in ['DISTANCE', 'EQUIANGULAR', 'MULTIPLE_IMPORTANCE'], default 'MULTIPLE_IMPORTANCE'

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


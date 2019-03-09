CyclesWorldSettings(bpy_struct)
===============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: CyclesWorldSettings(bpy_struct)

   

   .. attribute:: homogeneous_volume

      When using volume rendering, assume volume has the same density everywhere(not using any textures), for faster rendering

      :type: boolean, default False

   .. attribute:: max_bounces

      Maximum number of bounces the background light will contribute to the render

      :type: int in [0, 1024], default 1024

   .. attribute:: sample_as_light

      Use multiple importance sampling for the environment, enabling for non-solid colors is recommended

      :type: boolean, default True

   .. attribute:: sample_map_resolution

      Importance map size is resolution x resolution; higher values potentially produce less noise, at the cost of memory and speed

      :type: int in [4, 8192], default 1024

   .. attribute:: samples

      Number of light samples to render for each AA sample

      :type: int in [1, 10000], default 1

   .. attribute:: volume_interpolation

      Interpolation method to use for volumes

      * ``LINEAR`` Linear, Good smoothness and speed.
      * ``CUBIC`` Cubic, Smoothed high quality interpolation, but slower.

      :type: enum in ['LINEAR', 'CUBIC'], default 'LINEAR'

   .. attribute:: volume_sampling

      Sampling method to use for volumes

      * ``DISTANCE`` Distance, Use distance sampling, best for dense volumes with lights far away.
      * ``EQUIANGULAR`` Equiangular, Use equiangular sampling, best for volumes with low density with light inside or near the volume.
      * ``MULTIPLE_IMPORTANCE`` Multiple Importance, Combine distance and equi-angular sampling for volumes where neither method is ideal.

      :type: enum in ['DISTANCE', 'EQUIANGULAR', 'MULTIPLE_IMPORTANCE'], default 'EQUIANGULAR'

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


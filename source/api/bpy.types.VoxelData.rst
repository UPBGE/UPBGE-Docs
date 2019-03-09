VoxelData(bpy_struct)
=====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: VoxelData(bpy_struct)

   Voxel data settings

   .. attribute:: domain_object

      Object used as the smoke simulation domain

      :type: :class:`Object`

   .. attribute:: extension

      How the texture is extrapolated past its original bounds

      * ``EXTEND`` Extend, Extend by repeating edge pixels of the image.
      * ``CLIP`` Clip, Clip to image size and set exterior pixels as transparent.
      * ``REPEAT`` Repeat, Cause the image to repeat horizontally and vertically.

      :type: enum in ['EXTEND', 'CLIP', 'REPEAT'], default 'EXTEND'

   .. attribute:: file_format

      Format of the source data set to render

      * ``BLENDER_VOXEL`` Blender Voxel, Default binary voxel file format.
      * ``RAW_8BIT`` 8 bit RAW, 8 bit grayscale binary data.
      * ``IMAGE_SEQUENCE`` Image Sequence, Generate voxels from a sequence of image slices.
      * ``SMOKE`` Smoke, Render voxels from a Blender smoke simulation.
      * ``HAIR`` Hair, Render voxels from a Blender hair simulation.

      :type: enum in ['BLENDER_VOXEL', 'RAW_8BIT', 'IMAGE_SEQUENCE', 'SMOKE', 'HAIR'], default 'BLENDER_VOXEL'

   .. attribute:: filepath

      The external source data file to use

      :type: string, default "", (never None)

   .. attribute:: hair_data_type

      Simulation value to be used as a texture

      * ``HAIRDENSITY`` Density, Use hair density as texture data.
      * ``HAIRRESTDENSITY`` Rest Density, Use hair rest density as texture data.
      * ``HAIRVELOCITY`` Velocity, Use hair velocity as texture data.
      * ``HAIRENERGY`` Energy, Use potential hair energy as texture data.

      :type: enum in ['HAIRDENSITY', 'HAIRRESTDENSITY', 'HAIRVELOCITY', 'HAIRENERGY'], default 'HAIRDENSITY'

   .. attribute:: intensity

      Multiplier for intensity values

      :type: float in [0.01, inf], default 0.0

   .. attribute:: interpolation

      Method to interpolate/smooth values between voxel cells

      * ``NEREASTNEIGHBOR`` Nearest Neighbor, No interpolation, fast but blocky and low quality.
      * ``TRILINEAR`` Linear, Good smoothness and speed.
      * ``QUADRATIC`` Quadratic, Mid-range quality and speed.
      * ``TRICUBIC_CATROM`` Cubic Catmull-Rom, High quality interpolation, but slower.
      * ``TRICUBIC_BSPLINE`` Cubic B-Spline, Smoothed high quality interpolation, but slower.

      :type: enum in ['NEREASTNEIGHBOR', 'TRILINEAR', 'QUADRATIC', 'TRICUBIC_CATROM', 'TRICUBIC_BSPLINE'], default 'NEREASTNEIGHBOR'

   .. attribute:: resolution

      Resolution of the voxel grid

      :type: int array of 3 items in [1, 100000], default (0, 0, 0)

   .. attribute:: smoke_data_type

      Simulation value to be used as a texture

      * ``SMOKEDENSITY`` Smoke, Use smoke density and color as texture data.
      * ``SMOKEFLAME`` Flame, Use flame temperature as texture data.
      * ``SMOKEHEAT`` Heat, Use smoke heat as texture data. Values from -2.0 to 2.0 are used.
      * ``SMOKEVEL`` Velocity, Use smoke velocity as texture data.

      :type: enum in ['SMOKEDENSITY', 'SMOKEFLAME', 'SMOKEHEAT', 'SMOKEVEL'], default 'SMOKEDENSITY'

   .. attribute:: still_frame

      The frame number to always use

      :type: int in [-1048574, 1048574], default 0

   .. attribute:: use_still_frame

      Always render a still frame from the voxel data sequence

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

   * :class:`VoxelDataTexture.voxel_data`


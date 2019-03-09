ImageFormatSettings(bpy_struct)
===============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ImageFormatSettings(bpy_struct)

   Settings for image formats

   .. attribute:: cineon_black

      Log conversion reference blackpoint

      :type: int in [0, 1024], default 0

   .. attribute:: cineon_gamma

      Log conversion gamma

      :type: float in [0, 10], default 0.0

   .. attribute:: cineon_white

      Log conversion reference whitepoint

      :type: int in [0, 1024], default 0

   .. attribute:: color_depth

      Bit depth per channel

      * ``8`` 8, 8 bit color channels.
      * ``10`` 10, 10 bit color channels.
      * ``12`` 12, 12 bit color channels.
      * ``16`` 16, 16 bit color channels.
      * ``32`` 32, 32 bit color channels.

      :type: enum in ['8', '10', '12', '16', '32'], default '8'

   .. attribute:: color_mode

      Choose BW for saving grayscale images, RGB for saving red, green and blue channels, and RGBA for saving red, green, blue and alpha channels

      * ``BW`` BW, Images get saved in 8 bits grayscale (only PNG, JPEG, TGA, TIF).
      * ``RGB`` RGB, Images are saved with RGB (color) data.
      * ``RGBA`` RGBA, Images are saved with RGB and Alpha data (if supported).

      :type: enum in ['BW', 'RGB', 'RGBA'], default 'BW'

   .. attribute:: compression

      Amount of time to determine best compression: 0 = no compression with fast file output, 100 = maximum lossless compression with slow file output

      :type: int in [0, 100], default 0

   .. data:: display_settings

      Settings of device saved image would be displayed on

      :type: :class:`ColorManagedDisplaySettings`, (readonly)

   .. attribute:: exr_codec

      Codec settings for OpenEXR

      :type: enum in ['NONE', 'PXR24', 'ZIP', 'PIZ', 'RLE', 'ZIPS', 'B44', 'B44A', 'DWAA'], default 'NONE'

   .. attribute:: file_format

      File format to save the rendered images as

      * ``BMP`` BMP, Output image in bitmap format.
      * ``IRIS`` Iris, Output image in (old!) SGI IRIS format.
      * ``PNG`` PNG, Output image in PNG format.
      * ``JPEG`` JPEG, Output image in JPEG format.
      * ``JPEG2000`` JPEG 2000, Output image in JPEG 2000 format.
      * ``TARGA`` Targa, Output image in Targa format.
      * ``TARGA_RAW`` Targa Raw, Output image in uncompressed Targa format.
      * ``CINEON`` Cineon, Output image in Cineon format.
      * ``DPX`` DPX, Output image in DPX format.
      * ``OPEN_EXR_MULTILAYER`` OpenEXR MultiLayer, Output image in multilayer OpenEXR format.
      * ``OPEN_EXR`` OpenEXR, Output image in OpenEXR format.
      * ``HDR`` Radiance HDR, Output image in Radiance HDR format.
      * ``TIFF`` TIFF, Output image in TIFF format.
      * ``AVI_JPEG`` AVI JPEG, Output video in AVI JPEG format.
      * ``AVI_RAW`` AVI Raw, Output video in AVI Raw format.
      * ``FRAMESERVER`` Frame Server, Output image to a frameserver.
      * ``FFMPEG`` FFmpeg video, The most versatile way to output video files.

      :type: enum in ['BMP', 'IRIS', 'PNG', 'JPEG', 'JPEG2000', 'TARGA', 'TARGA_RAW', 'CINEON', 'DPX', 'OPEN_EXR_MULTILAYER', 'OPEN_EXR', 'HDR', 'TIFF', 'AVI_JPEG', 'AVI_RAW', 'FRAMESERVER', 'FFMPEG'], default 'TARGA'

   .. attribute:: jpeg2k_codec

      Codec settings for Jpeg2000

      :type: enum in ['JP2', 'J2K'], default 'JP2'

   .. attribute:: quality

      Quality for image formats that support lossy compression

      :type: int in [0, 100], default 0

   .. data:: stereo_3d_format

      Settings for stereo 3d

      :type: :class:`Stereo3dFormat`, (readonly, never None)

   .. attribute:: tiff_codec

      Compression mode for TIFF

      :type: enum in ['NONE', 'DEFLATE', 'LZW', 'PACKBITS'], default 'DEFLATE'

   .. attribute:: use_cineon_log

      Convert to logarithmic color space

      :type: boolean, default False

   .. attribute:: use_jpeg2k_cinema_48

      Use Openjpeg Cinema Preset (48fps)

      :type: boolean, default False

   .. attribute:: use_jpeg2k_cinema_preset

      Use Openjpeg Cinema Preset

      :type: boolean, default False

   .. attribute:: use_jpeg2k_ycc

      Save luminance-chrominance-chrominance channels instead of RGB colors

      :type: boolean, default False

   .. attribute:: use_preview

      When rendering animations, save JPG preview images in same directory

      :type: boolean, default False

   .. attribute:: use_zbuffer

      Save the z-depth per pixel (32 bit unsigned int z-buffer)

      :type: boolean, default False

   .. data:: view_settings

      Color management settings applied on image before saving

      :type: :class:`ColorManagedViewSettings`, (readonly)

   .. attribute:: views_format

      Format of multiview media

      * ``INDIVIDUAL`` Individual, Individual files for each view with the prefix as defined by the scene views.
      * ``STEREO_3D`` Stereo 3D, Single file with an encoded stereo pair.

      :type: enum in ['INDIVIDUAL', 'STEREO_3D'], default 'INDIVIDUAL'

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

   * :class:`CompositorNodeOutputFile.format`
   * :class:`NodeOutputFileSlotFile.format`
   * :class:`BakeSettings.image_settings`
   * :class:`RenderSettings.image_settings`
   * :class:`UILayout.template_image_settings`
   * :class:`UILayout.template_image_views`


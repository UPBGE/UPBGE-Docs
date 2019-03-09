Image(ID)
=========

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Image(ID)

   Image data-block referencing an external or packed image

   .. attribute:: alpha_mode

      Representation of alpha information in the RGBA pixels

      * ``STRAIGHT`` Straight, Transparent RGB and alpha pixels are unmodified.
      * ``PREMUL`` Premultiplied, Transparent RGB pixels are multiplied by the alpha channel.

      :type: enum in ['STRAIGHT', 'PREMUL'], default 'STRAIGHT'

   .. data:: bindcode

      OpenGL bindcode

      :type: int array of 2 items in [0, inf], default (0, 0), (readonly)

   .. data:: channels

      Number of channels in pixels buffer

      :type: int in [0, inf], default 0, (readonly)

   .. data:: colorspace_settings

      Input color space settings

      :type: :class:`ColorManagedInputColorspaceSettings`, (readonly)

   .. data:: depth

      Image bit depth

      :type: int in [0, inf], default 0, (readonly)

   .. attribute:: display_aspect

      Display Aspect for this image, does not affect rendering

      :type: float array of 2 items in [0.1, inf], default (0.0, 0.0)

   .. attribute:: field_order

      Order of video fields (select which lines are displayed first)

      * ``EVEN`` Upper First, Upper field first.
      * ``ODD`` Lower First, Lower field first.

      :type: enum in ['EVEN', 'ODD'], default 'EVEN'

   .. attribute:: file_format

      Format used for re-saving this file

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

   .. attribute:: filepath

      Image/Movie file name

      :type: string, default "", (never None)

   .. attribute:: filepath_raw

      Image/Movie file name (without data refreshing)

      :type: string, default "", (never None)

   .. attribute:: fps

      Speed of the animation in frames per second

      :type: int in [1, 100], default 0

   .. data:: frame_duration

      Duration (in frames) of the image (1 when not a video/sequence)

      :type: int in [0, inf], default 0, (readonly)

   .. attribute:: frame_end

      End frame of an animated texture

      :type: int in [0, 255], default 0

   .. attribute:: frame_start

      Start frame of an animated texture

      :type: int in [0, 255], default 0

   .. attribute:: generated_color

      Fill color for the generated image

      :type: float array of 4 items in [0, inf], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: generated_height

      Generated image height

      :type: int in [1, 65536], default 0

   .. attribute:: generated_type

      Generated image type

      * ``BLANK`` Blank, Generate a blank image.
      * ``UV_GRID`` UV Grid, Generated grid to test UV mappings.
      * ``COLOR_GRID`` Color Grid, Generated improved UV grid to test UV mappings.

      :type: enum in ['BLANK', 'UV_GRID', 'COLOR_GRID'], default 'BLANK'

   .. attribute:: generated_width

      Generated image width

      :type: int in [1, 65536], default 0

   .. data:: has_data

      True if the image data is loaded into memory

      :type: boolean, default False, (readonly)

   .. data:: is_dirty

      Image has changed and is not saved

      :type: boolean, default False, (readonly)

   .. data:: is_float

      True if this image is stored in float buffer

      :type: boolean, default False, (readonly)

   .. data:: is_multiview

      Image has more than one view

      :type: boolean, default False, (readonly)

   .. data:: is_stereo_3d

      Image has left and right views

      :type: boolean, default False, (readonly)

   .. attribute:: mapping

      Mapping type to use for this image in the game engine

      * ``UV`` UV Coordinates, Use UV coordinates for mapping the image.
      * ``REFLECTION`` Reflection, Use reflection mapping for mapping the image.

      :type: enum in ['UV', 'REFLECTION'], default 'UV'

   .. data:: packed_file

      First packed file of the image

      :type: :class:`PackedFile`, (readonly)

   .. data:: packed_files

      Collection of packed images

      :type: :class:`bpy_prop_collection` of :class:`ImagePackedFile`, (readonly)

   .. attribute:: pixels

      Image pixels in floating point values

      :type: float in [-inf, inf], default 0.0

   .. data:: render_slots

      Render slots of the image

      :type: :class:`RenderSlots` :class:`bpy_prop_collection` of :class:`RenderSlot`, (readonly)

   .. attribute:: resolution

      X/Y pixels per meter

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. data:: size

      Width and height in pixels, zero when image data cant be loaded

      :type: int array of 2 items in [-inf, inf], default (0, 0), (readonly)

   .. attribute:: source

      Where the image comes from

      * ``FILE`` Single Image, Single image file.
      * ``SEQUENCE`` Image Sequence, Multiple image files, as a sequence.
      * ``MOVIE`` Movie, Movie file.
      * ``GENERATED`` Generated, Generated image.
      * ``VIEWER`` Viewer, Compositing node viewer.

      :type: enum in ['FILE', 'SEQUENCE', 'MOVIE', 'GENERATED', 'VIEWER'], default 'FILE'

   .. data:: stereo_3d_format

      Settings for stereo 3d

      :type: :class:`Stereo3dFormat`, (readonly, never None)

   .. attribute:: tiles_x

      Degree of repetition in the X direction

      :type: int in [1, 16], default 0

   .. attribute:: tiles_y

      Degree of repetition in the Y direction

      :type: int in [1, 16], default 0

   .. data:: type

      How to generate the image

      :type: enum in ['IMAGE', 'MULTILAYER', 'UV_TEST', 'RENDER_RESULT', 'COMPOSITING'], default 'IMAGE', (readonly)

   .. attribute:: use_alpha

      Use the alpha channel information from the image or make image fully opaque

      :type: boolean, default False

   .. attribute:: use_animation

      Use as animated texture in the game engine

      :type: boolean, default False

   .. attribute:: use_clamp_x

      Disable texture repeating horizontally

      :type: boolean, default False

   .. attribute:: use_clamp_y

      Disable texture repeating vertically

      :type: boolean, default False

   .. attribute:: use_deinterlace

      Deinterlace movie file on load

      :type: boolean, default False

   .. attribute:: use_fields

      Use fields of the image

      :type: boolean, default False

   .. attribute:: use_generated_float

      Generate floating point buffer

      :type: boolean, default False

   .. attribute:: use_multiview

      Use Multiple Views (when available)

      :type: boolean, default False

   .. attribute:: use_tiles

      Use of tilemode for faces (default shift-LMB to pick the tile for selected faces)

      :type: boolean, default False

   .. attribute:: use_view_as_render

      Apply render part of display transformation when displaying this image on the screen

      :type: boolean, default False

   .. attribute:: views_format

      Mode to load image views

      * ``INDIVIDUAL`` Individual, Individual files for each view with the prefix as defined by the scene views.
      * ``STEREO_3D`` Stereo 3D, Single file with an encoded stereo pair.

      :type: enum in ['INDIVIDUAL', 'STEREO_3D'], default 'INDIVIDUAL'

   .. method:: save_render(filepath, scene=None)

      Save image to a specific path using a scenes render settings

      :arg filepath:

         Save path

      :type filepath: string, (never None)
      :arg scene:

         Scene to take image parameters from

      :type scene: :class:`Scene`, (optional)

   .. method:: save()

      Save image to its source path


   .. method:: pack(as_png=False, data="", data_len=0)

      Pack an image as embedded data into the .blend file

      :arg as_png:

         as_png, Pack the image as PNG (needed for generated/dirty images)

      :type as_png: boolean, (optional)
      :arg data:

         data, Raw data (bytes, exact content of the embedded file)

      :type data: string, (optional, never None)
      :arg data_len:

         data_len, length of given data (mandatory if data is provided)

      :type data_len: int in [0, inf], (optional)

   .. method:: unpack(method='USE_LOCAL')

      Save an image packed in the .blend file to disk

      :arg method:

         method, How to unpack

      :type method: enum in ['USE_LOCAL', 'WRITE_LOCAL', 'USE_ORIGINAL', 'WRITE_ORIGINAL'], (optional)

   .. method:: reload()

      Reload the image from its source path


   .. method:: update()

      Update the display image from the floating point buffer


   .. method:: scale(width, height)

      Scale the image in pixels

      :arg width:

         Width

      :type width: int in [1, 10000]
      :arg height:

         Height

      :type height: int in [1, 10000]

   .. method:: gl_touch(frame=0, filter=9985, mag=9729)

      Delay the image from being cleaned from the cache due inactivity

      :arg frame:

         Frame, Frame of image sequence or movie

      :type frame: int in [0, inf], (optional)
      :arg filter:

         Filter, The texture minifying function to use if the image wasn't loaded

      :type filter: int in [-inf, inf], (optional)
      :arg mag:

         Magnification, The texture magnification function to use if the image wasn't loaded

      :type mag: int in [-inf, inf], (optional)
      :return:

         Error, OpenGL error value

      :rtype: int in [-inf, inf]

   .. method:: gl_load(frame=0, filter=9985, mag=9729)

      Load the image into OpenGL graphics memory

      :arg frame:

         Frame, Frame of image sequence or movie

      :type frame: int in [0, inf], (optional)
      :arg filter:

         Filter, The texture minifying function

      :type filter: int in [-inf, inf], (optional)
      :arg mag:

         Magnification, The texture magnification function

      :type mag: int in [-inf, inf], (optional)
      :return:

         Error, OpenGL error value

      :rtype: int in [-inf, inf]

   .. method:: gl_free()

      Free the image from OpenGL graphics memory


   .. method:: filepath_from_user(image_user=None)

      Return the absolute path to the filepath of an image frame specified by the image user

      :arg image_user:

         Image user of the image to get filepath for

      :type image_user: :class:`ImageUser`, (optional)
      :return:

         File Path, The resulting filepath from the image and it's user

      :rtype: string, (never None)

   .. method:: buffers_free()

      Free the image buffers from memory


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
   * :class:`ID.name`
   * :class:`ID.users`
   * :class:`ID.use_fake_user`
   * :class:`ID.tag`
   * :class:`ID.is_updated`
   * :class:`ID.is_updated_data`
   * :class:`ID.is_library_indirect`
   * :class:`ID.library`
   * :class:`ID.preview`

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
   * :class:`ID.copy`
   * :class:`ID.user_clear`
   * :class:`ID.user_remap`
   * :class:`ID.make_local`
   * :class:`ID.user_of_id`
   * :class:`ID.animation_data_create`
   * :class:`ID.animation_data_clear`
   * :class:`ID.update_tag`

.. rubric:: References

.. hlist::
   :columns: 2

   * :mod:`bpy.context.edit_image`
   * :class:`BackgroundImage.image`
   * :class:`BlendData.images`
   * :class:`BlendDataImages.load`
   * :class:`BlendDataImages.new`
   * :class:`BlendDataImages.remove`
   * :class:`Brush.clone_image`
   * :class:`CompositorNodeImage.image`
   * :class:`EnvironmentMapTexture.image`
   * :class:`ImagePaint.canvas`
   * :class:`ImagePaint.clone_image`
   * :class:`ImagePaint.stencil_image`
   * :class:`ImageTexture.image`
   * :class:`Material.texture_paint_images`
   * :class:`MeshTextureFace.image`
   * :class:`MeshTexturePoly.image`
   * :class:`MovieTrackingPlaneTrack.image`
   * :class:`ShaderNodeTexEnvironment.image`
   * :class:`ShaderNodeTexImage.image`
   * :class:`SpaceImageEditor.image`
   * :class:`TextureNodeImage.image`
   * :class:`UILayout.template_image_layers`
   * :class:`UVProjectModifier.image`
   * :class:`VoxelDataTexture.image`


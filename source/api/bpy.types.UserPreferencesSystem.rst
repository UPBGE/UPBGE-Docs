UserPreferencesSystem(bpy_struct)
=================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: UserPreferencesSystem(bpy_struct)

   Graphics driver and operating system settings

   .. attribute:: anisotropic_filter

      Quality of the anisotropic filtering (values greater than 1.0 enable anisotropic filtering)

      :type: enum in ['FILTER_0', 'FILTER_2', 'FILTER_4', 'FILTER_8', 'FILTER_16'], default 'FILTER_0'

   .. attribute:: audio_channels

      Audio channel count

      * ``MONO`` Mono, Set audio channels to mono.
      * ``STEREO`` Stereo, Set audio channels to stereo.
      * ``SURROUND4`` 4 Channels, Set audio channels to 4 channels.
      * ``SURROUND51`` 5.1 Surround, Set audio channels to 5.1 surround sound.
      * ``SURROUND71`` 7.1 Surround, Set audio channels to 7.1 surround sound.

      :type: enum in ['MONO', 'STEREO', 'SURROUND4', 'SURROUND51', 'SURROUND71'], default 'MONO'

   .. attribute:: audio_device

      Audio output device

      * ``NONE`` None, Null device - there will be no audio output.
      * ``SDL`` SDL, SDL device - simple direct media layer, recommended for sequencer usage.
      * ``OPENAL`` OpenAL, OpenAL device - supports 3D audio, recommended for game engine usage.

      :type: enum in ['NONE', 'SDL', 'OPENAL'], default 'NONE'

   .. attribute:: audio_mixing_buffer

      Number of samples used by the audio mixing buffer

      * ``SAMPLES_256`` 256, Set audio mixing buffer size to 256 samples.
      * ``SAMPLES_512`` 512, Set audio mixing buffer size to 512 samples.
      * ``SAMPLES_1024`` 1024, Set audio mixing buffer size to 1024 samples.
      * ``SAMPLES_2048`` 2048, Set audio mixing buffer size to 2048 samples.
      * ``SAMPLES_4096`` 4096, Set audio mixing buffer size to 4096 samples.
      * ``SAMPLES_8192`` 8192, Set audio mixing buffer size to 8192 samples.
      * ``SAMPLES_16384`` 16384, Set audio mixing buffer size to 16384 samples.
      * ``SAMPLES_32768`` 32768, Set audio mixing buffer size to 32768 samples.

      :type: enum in ['SAMPLES_256', 'SAMPLES_512', 'SAMPLES_1024', 'SAMPLES_2048', 'SAMPLES_4096', 'SAMPLES_8192', 'SAMPLES_16384', 'SAMPLES_32768'], default 'SAMPLES_256'

   .. attribute:: audio_sample_format

      Audio sample format

      * ``U8`` 8-bit Unsigned, Set audio sample format to 8 bit unsigned integer.
      * ``S16`` 16-bit Signed, Set audio sample format to 16 bit signed integer.
      * ``S24`` 24-bit Signed, Set audio sample format to 24 bit signed integer.
      * ``S32`` 32-bit Signed, Set audio sample format to 32 bit signed integer.
      * ``FLOAT`` 32-bit Float, Set audio sample format to 32 bit float.
      * ``DOUBLE`` 64-bit Float, Set audio sample format to 64 bit float.

      :type: enum in ['U8', 'S16', 'S24', 'S32', 'FLOAT', 'DOUBLE'], default 'U8'

   .. attribute:: audio_sample_rate

      Audio sample rate

      * ``RATE_44100`` 44.1 kHz, Set audio sampling rate to 44100 samples per second.
      * ``RATE_48000`` 48 kHz, Set audio sampling rate to 48000 samples per second.
      * ``RATE_96000`` 96 kHz, Set audio sampling rate to 96000 samples per second.
      * ``RATE_192000`` 192 kHz, Set audio sampling rate to 192000 samples per second.

      :type: enum in ['RATE_44100', 'RATE_48000', 'RATE_96000', 'RATE_192000'], default 'RATE_44100'

   .. attribute:: author

      Name that will be used in exported files when format supports such feature

      :type: string, default "", (never None)

   .. attribute:: color_picker_type

      Different styles of displaying the color picker widget

      * ``CIRCLE_HSV`` Circle (HSV), A circular Hue/Saturation color wheel, with Value slider.
      * ``CIRCLE_HSL`` Circle (HSL), A circular Hue/Saturation color wheel, with Lightness slider.
      * ``SQUARE_SV`` Square (SV + H), A square showing Saturation/Value, with Hue slider.
      * ``SQUARE_HS`` Square (HS + V), A square showing Hue/Saturation, with Value slider.
      * ``SQUARE_HV`` Square (HV + S), A square showing Hue/Value, with Saturation slider.

      :type: enum in ['CIRCLE_HSV', 'CIRCLE_HSL', 'SQUARE_SV', 'SQUARE_HS', 'SQUARE_HV'], default 'CIRCLE_HSV'

   .. data:: dpi

      DPI for add-ons to use when drawing custom user interface elements, controlled by operating system settings and Blender UI scale, with a reference value of 72 DPI (note that since this value includes a user defined scale, it is not always the actual monitor DPI)

      :type: int in [-inf, inf], default 0, (readonly)

   .. attribute:: font_path_ui

      Path to interface font

      :type: string, default "", (never None)

   .. attribute:: font_path_ui_mono

      Path to interface mono-space Font

      :type: string, default "", (never None)

   .. attribute:: frame_server_port

      Frameserver Port for Frameserver Rendering

      :type: int in [0, 32727], default 0

   .. attribute:: gl_clip_alpha

      Clip alpha below this threshold in the 3D textured view

      :type: float in [0, 1], default 0.0

   .. attribute:: gl_texture_limit

      Limit the texture size to save graphics memory

      :type: enum in ['CLAMP_OFF', 'CLAMP_8192', 'CLAMP_4096', 'CLAMP_2048', 'CLAMP_1024', 'CLAMP_512', 'CLAMP_256', 'CLAMP_128'], default 'CLAMP_OFF'

   .. attribute:: image_draw_method

      Method used for displaying images on the screen

      * ``2DTEXTURE`` 2D Texture, Use CPU for display transform and draw image with 2D texture.
      * ``GLSL`` GLSL, Use GLSL shaders for display transform and draw image with 2D texture.
      * ``DRAWPIXELS`` DrawPixels, Use CPU for display transform and draw image using DrawPixels.

      :type: enum in ['2DTEXTURE', 'GLSL', 'DRAWPIXELS'], default '2DTEXTURE'

   .. data:: legacy_compute_device_type

      For backwards compatibility only

      :type: int in [-inf, inf], default 0, (readonly)

   .. attribute:: memory_cache_limit

      Memory cache limit (in megabytes)

      :type: int in [0, 1024], default 0

   .. attribute:: multi_sample

      Enable OpenGL multi-sampling, only for systems that support it, requires restart

      * ``NONE`` No MultiSample, Do not use OpenGL MultiSample.
      * ``2`` MultiSample: 2, Use 2x OpenGL MultiSample (requires restart).
      * ``4`` MultiSample: 4, Use 4x OpenGL MultiSample (requires restart).
      * ``8`` MultiSample: 8, Use 8x OpenGL MultiSample (requires restart).
      * ``16`` MultiSample: 16, Use 16x OpenGL MultiSample (requires restart).

      :type: enum in ['NONE', '2', '4', '8', '16'], default 'NONE'

   .. attribute:: opensubdiv_compute_type

      Type of computer back-end used with OpenSubdiv

      :type: enum in ['NONE'], default 'NONE'

   .. data:: pixel_size

      Suggested line thickness and point size in pixels, for add-ons drawing custom user interface elements, controlled by operating system settings and Blender UI scale

      :type: float in [-inf, inf], default 0.0, (readonly)

   .. attribute:: prefetch_frames

      Number of frames to render ahead during playback (sequencer only)

      :type: int in [0, inf], default 0

   .. attribute:: screencast_fps

      Frame rate for the screencast to be played back

      :type: int in [10, 100], default 0

   .. attribute:: screencast_wait_time

      Time in milliseconds between each frame recorded for screencast

      :type: int in [10, 1000], default 0

   .. attribute:: scrollback

      Maximum number of lines to store for the console buffer

      :type: int in [32, 32768], default 0

   .. attribute:: select_method

      Use OpenGL occlusion queries or selection render mode to accelerate selection

      :type: enum in ['AUTO', 'GL_SELECT', 'GL_QUERY'], default 'AUTO'

   .. data:: solid_lights

      Lights user to display objects in solid draw mode

      :type: :class:`bpy_prop_collection` of :class:`UserSolidLight`, (readonly)

   .. attribute:: texture_collection_rate

      Number of seconds between each run of the GL texture garbage collector

      :type: int in [1, 3600], default 0

   .. attribute:: texture_time_out

      Time since last access of a GL texture in seconds after which it is freed (set to 0 to keep textures allocated)

      :type: int in [0, 3600], default 0

   .. attribute:: use_16bit_textures

      Use 16 bit per component texture for float images

      :type: boolean, default False

   .. attribute:: use_gpu_mipmap

      Generate Image Mipmaps on the GPU

      :type: boolean, default False

   .. attribute:: use_international_fonts

      Use international fonts

      :type: boolean, default False

   .. attribute:: use_mipmaps

      Scale textures for the 3D View (looks nicer but uses more memory and slows image reloading)

      :type: boolean, default False

   .. attribute:: use_preview_images

      Allow user to choose any codec (Windows only, might generate instability)

      :type: boolean, default False

   .. attribute:: use_region_overlap

      Draw tool/property regions over the main region, when using Triple Buffer

      :type: boolean, default False

   .. attribute:: use_scripts_auto_execute

      Allow any .blend file to run scripts automatically (unsafe with blend files from an untrusted source)

      :type: boolean, default False

   .. attribute:: use_select_pick_depth

      Use the depth buffer for picking 3D View selection

      :type: boolean, default False

   .. attribute:: use_tabs_as_spaces

      Automatically convert all new tabs into spaces for new and loaded text files

      :type: boolean, default False

   .. attribute:: use_text_antialiasing

      Draw user interface text anti-aliased

      :type: boolean, default False

   .. attribute:: use_translate_interface

      Translate interface

      :type: boolean, default False

   .. attribute:: use_translate_new_dataname

      Translate new data names (when adding/creating some)

      :type: boolean, default False

   .. attribute:: use_translate_tooltips

      Translate tooltips

      :type: boolean, default False

   .. attribute:: use_weight_color_range

      Enable color range used for weight visualization in weight painting mode

      :type: boolean, default False

   .. data:: weight_color_range

      Color range used for weight visualization in weight painting mode

      :type: :class:`ColorRamp`, (readonly, never None)

   .. attribute:: window_draw_method

      Drawing method used by the window manager

      * ``AUTOMATIC`` Automatic, Automatically set based on graphics card and driver.
      * ``TRIPLE_BUFFER`` Triple Buffer, Use a third buffer for minimal redraws at the cost of more memory.
      * ``OVERLAP`` Overlap, Redraw all overlapping regions, minimal memory usage but more redraws.
      * ``OVERLAP_FLIP`` Overlap Flip, Redraw all overlapping regions, minimal memory usage but more redraws (for graphics drivers that do flipping).
      * ``FULL`` Full, Do a full redraw each time, slow, only use for reference or when everything else fails.

      :type: enum in ['AUTOMATIC', 'TRIPLE_BUFFER', 'OVERLAP', 'OVERLAP_FLIP', 'FULL'], default 'TRIPLE_BUFFER'

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

   * :class:`UserPreferences.system`


FFmpegSettings(bpy_struct)
==========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FFmpegSettings(bpy_struct)

   FFmpeg related settings for the scene

   .. attribute:: audio_bitrate

      Audio bitrate (kb/s)

      :type: int in [32, 384], default 0

   .. attribute:: audio_channels

      Audio channel count

      * ``MONO`` Mono, Set audio channels to mono.
      * ``STEREO`` Stereo, Set audio channels to stereo.
      * ``SURROUND4`` 4 Channels, Set audio channels to 4 channels.
      * ``SURROUND51`` 5.1 Surround, Set audio channels to 5.1 surround sound.
      * ``SURROUND71`` 7.1 Surround, Set audio channels to 7.1 surround sound.

      :type: enum in ['MONO', 'STEREO', 'SURROUND4', 'SURROUND51', 'SURROUND71'], default 'MONO'

   .. attribute:: audio_codec

      FFmpeg audio codec to use

      :type: enum in ['NONE', 'MP2', 'MP3', 'AC3', 'AAC', 'VORBIS', 'FLAC', 'PCM'], default 'NONE'

   .. attribute:: audio_mixrate

      Audio samplerate(samples/s)

      :type: int in [8000, 192000], default 0

   .. attribute:: audio_volume

      Audio volume

      :type: float in [0, 1], default 0.0

   .. attribute:: buffersize

      Rate control: buffer size (kb)

      :type: int in [0, 2000], default 0

   .. attribute:: codec

      FFmpeg codec to use

      :type: enum in ['NONE', 'MPEG1', 'MPEG2', 'MPEG4', 'HUFFYUV', 'DV', 'H264', 'THEORA', 'FLASH', 'FFV1', 'QTRLE', 'DNXHD', 'PNG'], default 'H264'

   .. attribute:: constant_rate_factor

      Constant Rate Factor (CRF); tradeoff between video quality and file size

      * ``NONE`` None; use custom bitrate, Use constant bit rate, rather than constant output quality.
      * ``LOSSLESS`` Lossless.
      * ``PERC_LOSSLESS`` Perceptually lossless.
      * ``HIGH`` High quality.
      * ``MEDIUM`` Medium quality.
      * ``LOW`` Low quality.
      * ``VERYLOW`` Very low quality.
      * ``LOWEST`` Lowest quality.

      :type: enum in ['NONE', 'LOSSLESS', 'PERC_LOSSLESS', 'HIGH', 'MEDIUM', 'LOW', 'VERYLOW', 'LOWEST'], default 'MEDIUM'

   .. attribute:: ffmpeg_preset

      Tradeoff between encoding speed and compression ratio

      :type: enum in ['ULTRAFAST', 'SUPERFAST', 'VERYFAST', 'FASTER', 'FAST', 'MEDIUM', 'SLOW', 'SLOWER', 'VERYSLOW'], default 'MEDIUM'

   .. attribute:: format

      Output file container

      :type: enum in ['MPEG1', 'MPEG2', 'MPEG4', 'AVI', 'QUICKTIME', 'DV', 'OGG', 'MKV', 'FLASH'], default 'MKV'

   .. attribute:: gopsize

      Distance between key frames, also known as GOP size; influences file size and seekability

      :type: int in [0, 500], default 25

   .. attribute:: max_b_frames

      Maximum number of B-frames between non-B-frames; influences file size and seekability

      :type: int in [0, 16], default 0

   .. attribute:: maxrate

      Rate control: max rate (kb/s)

      :type: int in [-inf, inf], default 0

   .. attribute:: minrate

      Rate control: min rate (kb/s)

      :type: int in [-inf, inf], default 0

   .. attribute:: muxrate

      Mux rate (bits/s(!))

      :type: int in [0, inf], default 0

   .. attribute:: packetsize

      Mux packet size (byte)

      :type: int in [0, 16384], default 0

   .. attribute:: use_autosplit

      Autosplit output at 2GB boundary

      :type: boolean, default False

   .. attribute:: use_lossless_output

      Use lossless output for video streams

      :type: boolean, default False

   .. attribute:: use_max_b_frames

      Set a maximum number of B-frames

      :type: boolean, default False

   .. attribute:: video_bitrate

      Video bitrate (kb/s)

      :type: int in [-inf, inf], default 0

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

   * :class:`RenderSettings.ffmpeg`

